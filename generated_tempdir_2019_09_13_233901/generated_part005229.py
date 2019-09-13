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

class CommutativeMatcher11780(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.1.0_2', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.1.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.1', 1, 1, None), Mul)
]),
    5: (5, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.1.0_1', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({}), [
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({}), [
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.1.0_1', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.1.0_1', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher11780._instance is None:
            CommutativeMatcher11780._instance = CommutativeMatcher11780()
        return CommutativeMatcher11780._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 11779
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 12833
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 12834
                    if len(subjects) == 0:
                        pass
                        # 0: x**p
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 12835
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 12836
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12837
                        if len(subjects5) == 0:
                            pass
                            # State 12838
                            if len(subjects) == 0:
                                pass
                                # 0: x**p
                    if len(subjects5) >= 1:
                        tmp9 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 12837
                            if len(subjects5) == 0:
                                pass
                                # State 12838
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**p
                        subjects5.appendleft(tmp9)
                    if len(subjects5) >= 1:
                        tmp11 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1.2', tmp11)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 14348
                            if len(subjects5) == 0:
                                pass
                                # State 14349
                                if len(subjects) == 0:
                                    pass
                                    # 4: x**n
                        subjects5.appendleft(tmp11)
                    if len(subjects5) >= 1 and subjects5[0] == 2:
                        tmp13 = subjects5.popleft()
                        # State 12953
                        if len(subjects5) == 0:
                            pass
                            # State 12954
                            if len(subjects) == 0:
                                pass
                                # 1: x**2
                        subjects5.appendleft(tmp13)
                    if len(subjects5) >= 1 and subjects5[0] == 4:
                        tmp14 = subjects5.popleft()
                        # State 14223
                        if len(subjects5) == 0:
                            pass
                            # State 14224
                            if len(subjects) == 0:
                                pass
                                # 3: x**4
                        subjects5.appendleft(tmp14)
                subjects5.appendleft(tmp6)
            if len(subjects5) >= 1:
                tmp15 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp15)
                except ValueError:
                    pass
                else:
                    pass
                    # State 14019
                    if len(subjects5) >= 1 and subjects5[0] == 2:
                        tmp17 = subjects5.popleft()
                        # State 14020
                        if len(subjects5) == 0:
                            pass
                            # State 14021
                            if len(subjects) == 0:
                                pass
                                # 2: x**2
                        subjects5.appendleft(tmp17)
                subjects5.appendleft(tmp15)
            subjects.appendleft(tmp4)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
