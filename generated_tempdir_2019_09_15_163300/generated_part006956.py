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


class CommutativeMatcher59373(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.2.1.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.3.1.0_1', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({}), [
      (VariableWithCount('i2.2.1.4.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.4.1.0_1', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({0: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({1: 1}), [
      (VariableWithCount('i2.4.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({2: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({}), [
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.3.1.1', 1, 1, None), Mul)
]),
    11: (11, Multiset({3: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({}), [
      (VariableWithCount('i2.4.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.4.1.0_1', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({}), [
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.3.1.1.0', 1, 1, None), Mul)
]),
    15: (15, Multiset({}), [
      (VariableWithCount('i2.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0_2', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher59373._instance is None:
            CommutativeMatcher59373._instance = CommutativeMatcher59373()
        return CommutativeMatcher59373._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 59372
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 88426
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 88427
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 88428
                            if len(subjects2) == 0:
                                pass
                                # State 88429
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp7 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.1.1', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 89196
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89197
                        if len(subjects2) == 0:
                            pass
                            # State 89198
                            if len(subjects) == 0:
                                pass
                                # 1: x**n
                                yield 1, subst2
                    if len(subjects2) >= 1:
                        tmp10 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.4.1.2', tmp10)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 89197
                            if len(subjects2) == 0:
                                pass
                                # State 89198
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                                    yield 1, subst2
                        subjects2.appendleft(tmp10)
                subjects2.appendleft(tmp7)
            if len(subjects2) >= 1:
                tmp12 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1.1', tmp12)
                except ValueError:
                    pass
                else:
                    pass
                    # State 89513
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp14 = subjects2.popleft()
                        # State 89514
                        if len(subjects2) == 0:
                            pass
                            # State 89515
                            if len(subjects) == 0:
                                pass
                                # 2: x**2
                                yield 2, subst1
                        subjects2.appendleft(tmp14)
                subjects2.appendleft(tmp12)
            if len(subjects2) >= 1:
                tmp15 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.0', tmp15)
                except ValueError:
                    pass
                else:
                    pass
                    # State 89550
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp17 = subjects2.popleft()
                        # State 89551
                        if len(subjects2) == 0:
                            pass
                            # State 89552
                            if len(subjects) == 0:
                                pass
                                # 3: v**2
                                yield 3, subst1
                        subjects2.appendleft(tmp17)
                subjects2.appendleft(tmp15)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 89194
            if len(subjects) >= 1:
                tmp19 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.1', tmp19)
                except ValueError:
                    pass
                else:
                    pass
                    # State 89195
                    if len(subjects) == 0:
                        pass
                        # 1: x**n
                        yield 1, subst2
                subjects.appendleft(tmp19)
        return
        yield


from collections import deque