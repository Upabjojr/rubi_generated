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

class CommutativeMatcher58486(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.2.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.3.1.0_1', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.4.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.4.1.0_1', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({}), [
      (VariableWithCount('i2.2.1.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.3.1.0_1', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher58486._instance is None:
            CommutativeMatcher58486._instance = CommutativeMatcher58486()
        return CommutativeMatcher58486._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 58485
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 74041
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 74042
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 74043
                            if len(subjects2) == 0:
                                pass
                                # State 74044
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp7 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0_1', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 74498
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 74499
                            if len(subjects2) == 0:
                                pass
                                # State 74500
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                        subjects2.appendleft(tmp9)
                subjects2.appendleft(tmp7)
            if len(subjects2) >= 1:
                tmp11 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75006
                    if len(subjects2) >= 1:
                        tmp13 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1.2', tmp13)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 75007
                            if len(subjects2) == 0:
                                pass
                                # State 75008
                                if len(subjects) == 0:
                                    pass
                                    # 2: x**n
                        subjects2.appendleft(tmp13)
                subjects2.appendleft(tmp11)
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
