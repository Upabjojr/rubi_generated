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


class CommutativeMatcher54133(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.1.1.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.1.1.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher54133._instance is None:
            CommutativeMatcher54133._instance = CommutativeMatcher54133()
        return CommutativeMatcher54133._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 54132
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 114020
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.2.0', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 114021
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp5 = subjects2.popleft()
                        # State 114022
                        if len(subjects2) == 0:
                            pass
                            # State 114023
                            if len(subjects) == 0:
                                pass
                                # 0: x**2
                                yield 0, subst1
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp6 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 114168
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp8 = subjects2.popleft()
                        # State 114169
                        if len(subjects2) == 0:
                            pass
                            # State 114170
                            if len(subjects) == 0:
                                pass
                                # 1: x**2
                                yield 1, subst1
                        subjects2.appendleft(tmp8)
                subjects2.appendleft(tmp6)
            if len(subjects2) >= 1:
                tmp9 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.0', tmp9)
                except ValueError:
                    pass
                else:
                    pass
                    # State 114261
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp11 = subjects2.popleft()
                        # State 114262
                        if len(subjects2) == 0:
                            pass
                            # State 114263
                            if len(subjects) == 0:
                                pass
                                # 2: x**2
                                yield 2, subst1
                        subjects2.appendleft(tmp11)
                subjects2.appendleft(tmp9)
            subjects.appendleft(tmp1)
        return
        yield


from collections import deque