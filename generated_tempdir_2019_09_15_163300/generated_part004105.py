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


class CommutativeMatcher3798(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_4', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_4', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_5', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({}), [
      (VariableWithCount('i2.2.1.0_6', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_7', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher3798._instance is None:
            CommutativeMatcher3798._instance = CommutativeMatcher3798()
        return CommutativeMatcher3798._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3797
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 5890
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.0', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 5891
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp5 = subjects2.popleft()
                        # State 5892
                        if len(subjects2) == 0:
                            pass
                            # State 5893
                            if len(subjects) == 0:
                                pass
                                # 0: v**2
                                yield 0, subst1
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp6 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7913
                    if len(subjects2) >= 1:
                        tmp8 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp8)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7914
                            if len(subjects2) == 0:
                                pass
                                # State 7915
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                                    yield 1, subst2
                        subjects2.appendleft(tmp8)
                subjects2.appendleft(tmp6)
            if len(subjects2) >= 1:
                tmp10 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0', tmp10)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7939
                    if len(subjects2) >= 1:
                        tmp12 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp12)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7940
                            if len(subjects2) == 0:
                                pass
                                # State 7941
                                if len(subjects) == 0:
                                    pass
                                    # 2: x**n
                                    yield 2, subst2
                        subjects2.appendleft(tmp12)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8104
                        if len(subjects2) == 0:
                            pass
                            # State 8105
                            if len(subjects) == 0:
                                pass
                                # 5: x**n2
                                yield 5, subst2
                    if len(subjects2) >= 1:
                        tmp15 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp15)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8104
                            if len(subjects2) == 0:
                                pass
                                # State 8105
                                if len(subjects) == 0:
                                    pass
                                    # 5: x**n2
                                    yield 5, subst2
                        subjects2.appendleft(tmp15)
                subjects2.appendleft(tmp10)
            if len(subjects2) >= 1:
                tmp17 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0_1', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7969
                    if len(subjects2) >= 1:
                        tmp19 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp19)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7970
                            if len(subjects2) == 0:
                                pass
                                # State 7971
                                if len(subjects) == 0:
                                    pass
                                    # 3: x**n
                                    yield 3, subst2
                        subjects2.appendleft(tmp19)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8077
                        if len(subjects2) == 0:
                            pass
                            # State 8078
                            if len(subjects) == 0:
                                pass
                                # 4: x**n
                                yield 4, subst2
                    if len(subjects2) >= 1:
                        tmp22 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp22)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8077
                            if len(subjects2) == 0:
                                pass
                                # State 8078
                                if len(subjects) == 0:
                                    pass
                                    # 4: x**n
                                    yield 4, subst2
                        subjects2.appendleft(tmp22)
                subjects2.appendleft(tmp17)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 8075
            if len(subjects) >= 1:
                tmp25 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0_1', tmp25)
                except ValueError:
                    pass
                else:
                    pass
                    # State 8076
                    if len(subjects) == 0:
                        pass
                        # 4: x**n
                        yield 4, subst2
                subjects.appendleft(tmp25)
            if len(subjects) >= 1:
                tmp27 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp27)
                except ValueError:
                    pass
                else:
                    pass
                    # State 8103
                    if len(subjects) == 0:
                        pass
                        # 5: x**n2
                        yield 5, subst2
                subjects.appendleft(tmp27)
        return
        yield


from collections import deque