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


class CommutativeMatcher65727(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 1
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher65727._instance is None:
            CommutativeMatcher65727._instance = CommutativeMatcher65727()
        return CommutativeMatcher65727._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 65726
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 75531
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75532
                    if len(subjects) == 0:
                        pass
                        # 0: x**n
                        yield 0, subst2
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 75533
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75534
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75535
                        if len(subjects5) == 0:
                            pass
                            # State 75536
                            if len(subjects) == 0:
                                pass
                                # 0: x**n
                                yield 0, subst2
                    if len(subjects5) >= 1:
                        tmp9 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 75535
                            if len(subjects5) == 0:
                                pass
                                # State 75536
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects5.appendleft(tmp9)
                subjects5.appendleft(tmp6)
            if len(subjects5) >= 1 and isinstance(subjects5[0], Add):
                tmp11 = subjects5.popleft()
                associative1 = tmp11
                associative_type1 = type(tmp11)
                subjects12 = deque(tmp11._args)
                matcher = CommutativeMatcher107402.get()
                tmp13 = subjects12
                subjects12 = []
                for s in tmp13:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp13, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 107408
                        if len(subjects5) >= 1:
                            tmp14 = []
                            tmp14.append(subjects5.popleft())
                            while True:
                                if len(tmp14) > 1:
                                    tmp15 = create_operation_expression(associative1, tmp14)
                                elif len(tmp14) == 1:
                                    tmp15 = tmp14[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.1.2', tmp15)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 107409
                                    if len(subjects5) == 0:
                                        pass
                                        # State 107410
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (x*d + c)**n
                                            yield 2, subst2
                                if len(subjects5) == 0:
                                    break
                                tmp14.append(subjects5.popleft())
                            subjects5.extendleft(reversed(tmp14))
                subjects5.appendleft(tmp11)
            subjects.appendleft(tmp4)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp17 = subjects.popleft()
            subjects18 = deque(tmp17._args)
            # State 105268
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 105269
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 105270
                    if len(subjects18) >= 1:
                        tmp21 = subjects18.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2.1', tmp21)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 105271
                            if len(subjects18) == 0:
                                pass
                                # State 105272
                                if len(subjects) == 0:
                                    pass
                                    # 1: log(c*x**n)
                                    yield 1, subst3
                        subjects18.appendleft(tmp21)
                if len(subjects18) >= 1 and isinstance(subjects18[0], Pow):
                    tmp23 = subjects18.popleft()
                    subjects24 = deque(tmp23._args)
                    # State 105273
                    if len(subjects24) >= 1:
                        tmp25 = subjects24.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2.1', tmp25)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 105274
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105275
                                if len(subjects24) == 0:
                                    pass
                                    # State 105276
                                    if len(subjects18) == 0:
                                        pass
                                        # State 105277
                                        if len(subjects) == 0:
                                            pass
                                            # 1: log(c*x**n)
                                            yield 1, subst3
                            if len(subjects24) >= 1:
                                tmp28 = subjects24.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.3.1.2.2', tmp28)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 105275
                                    if len(subjects24) == 0:
                                        pass
                                        # State 105276
                                        if len(subjects18) == 0:
                                            pass
                                            # State 105277
                                            if len(subjects) == 0:
                                                pass
                                                # 1: log(c*x**n)
                                                yield 1, subst3
                                subjects24.appendleft(tmp28)
                        subjects24.appendleft(tmp25)
                    subjects18.appendleft(tmp23)
            if len(subjects18) >= 1 and isinstance(subjects18[0], Mul):
                tmp30 = subjects18.popleft()
                associative1 = tmp30
                associative_type1 = type(tmp30)
                subjects31 = deque(tmp30._args)
                matcher = CommutativeMatcher105279.get()
                tmp32 = subjects31
                subjects31 = []
                for s in tmp32:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp32, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 105286
                        if len(subjects18) == 0:
                            pass
                            # State 105287
                            if len(subjects) == 0:
                                pass
                                # 1: log(c*x**n)
                                yield 1, subst1
                subjects18.appendleft(tmp30)
            subjects.appendleft(tmp17)
        return
        yield


from .generated_part004186 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part004188 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset