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


class CommutativeMatcher56687(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 1
    anonymous_patterns = {0, 1}

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher56687._instance is None:
            CommutativeMatcher56687._instance = CommutativeMatcher56687()
        return CommutativeMatcher56687._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 56686
        if len(subjects) >= 1 and subjects[0] == LambertW(Add(Symbol('a'), Mul(Symbol('b'), Symbol('x')))):
            tmp1 = subjects.popleft()
            # State 56688
            if len(subjects) == 0:
                pass
                # 0: LambertW(a + b*x)
                yield 0, subst0
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and subjects[0] == LambertW(Mul(Symbol('a'), Pow(Symbol('x'), Symbol('n')))):
            tmp2 = subjects.popleft()
            # State 56716
            if len(subjects) == 0:
                pass
                # 1: LambertW(a*x**n)
                yield 1, subst0
            subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp3 = subjects.popleft()
            subjects4 = deque(tmp3._args)
            # State 101312
            if len(subjects4) >= 1 and isinstance(subjects4[0], Mul):
                tmp5 = subjects4.popleft()
                associative1 = tmp5
                associative_type1 = type(tmp5)
                subjects6 = deque(tmp5._args)
                matcher = CommutativeMatcher101314.get()
                tmp7 = subjects6
                subjects6 = []
                for s in tmp7:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp7, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 101329
                        if len(subjects4) >= 1:
                            tmp8 = []
                            tmp8.append(subjects4.popleft())
                            while True:
                                if len(tmp8) > 1:
                                    tmp9 = create_operation_expression(associative1, tmp8)
                                elif len(tmp8) == 1:
                                    tmp9 = tmp8[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2', tmp9)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 101330
                                    if len(subjects4) == 0:
                                        pass
                                        # State 101331
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (F*b*(c + x*d))**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1666) and (cons_f149)
                                            yield 2, subst2
                                if len(subjects4) == 0:
                                    break
                                tmp8.append(subjects4.popleft())
                            subjects4.extendleft(reversed(tmp8))
                subjects4.appendleft(tmp5)
            subjects.appendleft(tmp3)
        return
        yield


from .generated_part001542 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset