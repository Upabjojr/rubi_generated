from datetime import datetime
import sys

from sympy.integrals.rubi.rubimain import get_rubi_object

sys.setrecursionlimit(15000)

import re
import os

#from sympy.core.expr import Basic
#from sympy.integrals.rubi.rubimain import *
from sympy import *
from sympy.core.singleton import Singleton

from matchpy.utils import get_short_lambda_source
from matchpy.matching.code_generation import CodeGenerator
from matchpy import CustomConstraint
import re

MAIN_IMPORTS = """

from sympy.integrals.rubi.constraints import *
from sympy.integrals.rubi.rules.binomial_products import * 
from sympy.integrals.rubi.rules.exponential import * 
from sympy.integrals.rubi.rules.hyperbolic import * 
from sympy.integrals.rubi.rules.integrand_simplification import * 
from sympy.integrals.rubi.rules.inverse_hyperbolic import * 
from sympy.integrals.rubi.rules.inverse_trig import * 
from sympy.integrals.rubi.rules.linear_products import * 
from sympy.integrals.rubi.rules.logarithms import * 
from sympy.integrals.rubi.rules.miscellaneous_algebraic import * 
from sympy.integrals.rubi.rules.miscellaneous_integration import * 
from sympy.integrals.rubi.rules.miscellaneous_trig import * 
from sympy.integrals.rubi.rules.piecewise_linear import * 
from sympy.integrals.rubi.rules.quadratic_products import * 
from sympy.integrals.rubi.rules.secant import * 
from sympy.integrals.rubi.rules.sine import * 
from sympy.integrals.rubi.rules.special_functions import * 
from sympy.integrals.rubi.rules.tangent import * 
from sympy.integrals.rubi.rules.trinomial_products import *

"""


class RubiCodeGenerator(CodeGenerator):

    part = 0

    def __init__(self, *args, **kwargs):
        print("Starting new part: ", self.part)
        self._tempfile = open(self.tempfile.format(self.part), "w")
        self._tempfile_part = self.part
        RubiCodeGenerator.part += 1
        self.final_label_counter = 0
        super().__init__(*args, **kwargs)

    def final_label(self, pattern_index, subst_name):
        label = self._matcher.patterns[pattern_index][1]
        if label is not None:
            self.final_label_counter += 1
            print("Final label number: ", self.final_label_counter,
                  " label ", label)
            return label.__name__
        if self._tempfile_part == 0:
            raise ValueError
        return super().final_label(pattern_index, subst_name)

    def add_line(self, line):
        self._tempfile.write(
            (self._indentation * self._level) + str(line) + '\n'
        )
        self._tempfile.flush()

    def symbol_repr(self, symbol):
        if isinstance(symbol, Basic):
            return srepr(symbol).replace("matchpyWC", "Symbol")
        return super().symbol_repr(symbol)

    def yield_final_substitution(self, pattern_index):
        renaming = self._matcher.pattern_vars[pattern_index]
        subst_name = 'subst{}'.format(self._substs)
        if any(k != v for k, v in renaming.items()):
            self.add_line('tmp_subst = Substitution()')
            for original, renamed in renaming.items():
                self.add_line('tmp_subst[{!r}] = subst{}[{!r}]'.format(original, self._substs, renamed))
            subst_name = 'tmp_subst'
        pattern = self._matcher.patterns[pattern_index][0]
        self.add_line('# {}: {}'.format(pattern_index, pattern))
        final_label = self.final_label(pattern_index, subst_name)
        if self._tempfile_part == 0:
            constraint_list = ", ".join(map(str, pattern.constraints))
            self.add_line('yield {}, {}, [{}]'.format(final_label, subst_name, constraint_list))
        else:
            self.add_line('yield {}, {}'.format(final_label, subst_name))

    def constraint_repr(self, constraint):
        if isinstance(constraint, CustomConstraint) and isinstance(constraint.constraint, type(lambda: 0)):
            src = get_short_lambda_source(constraint.constraint)
            if src is None:
                src = str(constraint.constraint.__name__) + "({0})".format(
                    ", ".join(['{1}=subst{0}["{2}"]'.format(self._substs, k, v)
                               for k, v in constraint._variables.items()])
                )
                return src, False
            mapping = {k: v for v, k in constraint._variables.items()}
            params = constraint._variables.keys()
            pstr = r'\b({})\b'.format('|'.join(map(re.escape, params)))
            new_src = re.sub(pstr, lambda m: 'subst{}[{!r}]'.format(self._substs, constraint._variables[m[0]]), src)
            return new_src, False
        return super().constraint_repr(constraint)

    def expr(self, expr):
        if isinstance(type(expr), Singleton):
            return 'S({!r})'.format(expr)
        return repr(expr)

    def get_args(self, operation, operation_type):
        if issubclass(operation_type, Integral):
            return '({0}._args[0],) + {0}._args[1]'.format(operation)
        if issubclass(operation_type, Basic):
            return '{}._args'.format(operation)
        return super().get_args(operation, operation_type)

    def generate_state_code(self, state):
        if state.matcher is not None:
            self._imports.add('from matchpy.matching.many_to_one import CommutativeMatcher')
            self._imports.add('from multiset import Multiset')
            self._imports.add('from matchpy.utils import VariableWithCount')
            generator = type(self)(state.matcher.automaton)
            patterns = self.commutative_patterns(state.matcher.patterns)
            subjects = repr(state.matcher.subjects)
            subjects_by_id = repr(state.matcher.subjects_by_id)
            associative = self.operation_symbol(state.matcher.associative)
            max_optional_count = repr(state.matcher.max_optional_count)
            anonymous_patterns = repr(state.matcher.anonymous_patterns)
            generator._tempfile.write('''
from sympy.abc import *
from matchpy.matching.many_to_one import CommutativeMatcher
from matchpy import *
from matchpy.utils import VariableWithCount
from collections import deque
from multiset import Multiset
from sympy.integrals.rubi.constraints import *
from sympy.integrals.rubi.utility_function import *
from sympy.integrals.rubi.rules.miscellaneous_integration import *
from sympy import *


class CommutativeMatcher{0}(CommutativeMatcher):
{8}_instance = None
{8}patterns = {1}
{8}subjects = {2}
{8}subjects_by_id = {7}
{8}bipartite = BipartiteGraph()
{8}associative = {3}
{8}max_optional_count = {4}
{8}anonymous_patterns = {5}

{8}def __init__(self):
{8}{8}self.add_subject(None)

{8}@staticmethod
{8}def get():
{8}{8}if CommutativeMatcher{0}._instance is None:
{8}{8}{8}CommutativeMatcher{0}._instance = CommutativeMatcher{0}()
{8}{8}return CommutativeMatcher{0}._instance

{8}@staticmethod
{6}'''.strip().format(
                state.number, patterns, subjects, associative, max_optional_count, anonymous_patterns, "",
                subjects_by_id, self._indentation
            )
            )
            generator.indent()
            global_code, code = generator.generate_code(func_name='get_match_iter', add_imports=True)
            generator._tempfile.write("\n\n")
#            for import_el in sorted(self._imports):
#                generator._tempfile.write(import_el)
#                generator._tempfile.write("\n")
            generator._tempfile.flush()
            for global_line in global_code:
                generator._tempfile.write(global_line)
            #self._global_code.append(global_code)
            #for global_line in self._global_code:
                #self._tempfile.write(global_line)
            self.add_line('matcher = CommutativeMatcher{}.get()'.format(state.number))
            self._imports.add("from .generated_part{0:06} import *".format(generator._tempfile_part))
            tmp = self.get_var_name('tmp')
            self.add_line('{} = {}'.format(tmp, self._subjects[-1]))
            self.add_line('{} = []'.format(self._subjects[-1]))
            self.add_line('for s in {}:'.format(tmp))
            self.indent()
            self.add_line('matcher.add_subject(s)')
            subjects = self._subjects.pop()
            self.dedent()
            self.add_line(
                'for pattern_index, subst{} in matcher.match({}, subst{}):'.format(self._substs + 1, tmp, self._substs)
            )
            self._substs += 1
            self.indent()
            self.add_line('pass')
            for pattern_index, transitions in state.transitions.items():
                self.add_line('if pattern_index == {}:'.format(pattern_index))
                self.indent()
                self.add_line('pass')
                patterns, variables = next((p, v) for i, p, v in state.matcher.patterns.values() if i == pattern_index)
                variables = set(v[0][0] for v in variables)
                from matchpy.matching.code_generation import get_variables
                pvars = iter(get_variables(state.matcher.automaton.patterns[i][0].expression) for i in patterns)
                variables.update(*pvars)
                constraints = []
                if variables:
                    constraints = sorted(
                        set.union(*iter(self._matcher.constraint_vars.get(v, set()) for v in variables))
                    )
                self.generate_constraints(constraints, transitions)
                self.dedent()
            self.dedent()
            self._substs -= 1
            self._subjects.append(subjects)
        else:
            self.add_line('# State {}'.format(state.number))
            if state.number in self._matcher.finals:
                self.add_line('if len({}) == 0:'.format(self._subjects[-1]))
                self.indent()
                self.add_line('pass')
                for pattern_index in self._patterns:
                    constraints = self._matcher.patterns[pattern_index][0].global_constraints
                    for constraint in constraints:
                        self.enter_global_constraint(constraint)
                    self.yield_final_substitution(pattern_index)
                    for constraint in constraints:
                        self.exit_global_constraint(constraint)
                self.dedent()
            else:
                for transitions in state.transitions.values():
                    for transition in transitions:
                        self.generate_transition_code(transition)


GENERATED_TEMPLATE = '''
# -*- coding: utf-8 -*-
from sympy import *
from matchpy import *
from sympy.integrals.rubi.utility_function import *
from sympy.integrals.rubi.constraints import *
# from sympy.integrals.rubi.symbol import *
{}
{}
'''.strip()


def generate_code():
    print("Loading RUBI object...")
    r = get_rubi_object()
    rubi = r[0]
    print("done")

    tempdir = "generated_tempdir_{0}".format(datetime.now().strftime("%Y_%m_%d_%H%M%S"))
    os.mkdir(tempdir)
    os.system(os.path.join(tempdir, "__init__.py"))
    tempfile = "{0}/generated_part{{0:06}}.py".format(tempdir)

    RubiCodeGenerator.tempfile = tempfile
    generator = RubiCodeGenerator(rubi.matcher)
    global_code, code = generator.generate_code()

    mainfile = tempfile.format(0)
    with open(mainfile, 'a', encoding='utf-8') as f:
        f.write("\n\n")
        f.write("from sympy.integrals.rubi.constraints import *\n")
        f.write("from sympy.integrals.rubi.rules.binomial_products import *\n") 
        f.write("from sympy.integrals.rubi.rules.exponential import *\n") 
        f.write("from sympy.integrals.rubi.rules.hyperbolic import *\n") 
        f.write("from sympy.integrals.rubi.rules.integrand_simplification import *\n") 
        f.write("from sympy.integrals.rubi.rules.inverse_hyperbolic import *\n") 
        f.write("from sympy.integrals.rubi.rules.inverse_trig import *\n") 
        f.write("from sympy.integrals.rubi.rules.linear_products import *\n") 
        f.write("from sympy.integrals.rubi.rules.logarithms import *\n") 
        f.write("from sympy.integrals.rubi.rules.miscellaneous_algebraic import *\n") 
        f.write("from sympy.integrals.rubi.rules.miscellaneous_integration import *\n") 
        f.write("from sympy.integrals.rubi.rules.miscellaneous_trig import *\n") 
        f.write("from sympy.integrals.rubi.rules.piecewise_linear import *\n") 
        f.write("from sympy.integrals.rubi.rules.quadratic_products import *\n") 
        f.write("from sympy.integrals.rubi.rules.secant import *\n") 
        f.write("from sympy.integrals.rubi.rules.sine import *\n") 
        f.write("from sympy.integrals.rubi.rules.special_functions import *\n") 
        f.write("from sympy.integrals.rubi.rules.tangent import *\n") 
        f.write("from sympy.integrals.rubi.rules.trinomial_products import *\n")
        for i in range(1, RubiCodeGenerator.part):
            f.write("from .generated_part{0:06} import *\n".format(i))
        f.flush()


if __name__ == "__main__":
    generate_code()
