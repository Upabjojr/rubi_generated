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

class CommutativeMatcher3229(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_4', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    5: (5, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_4', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_5', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    10: (10, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    27: (27, Multiset({13: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({14: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({15: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({16: 1}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
]),
    31: (31, Multiset({17: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.4.1.1.0', 1, 1, None), Mul)
]),
    33: (33, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.3.1.1.0', 1, 1, None), Mul)
]),
    34: (34, Multiset({18: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({19: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    36: (36, Multiset({20: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    37: (37, Multiset({21: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    38: (38, Multiset({22: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({23: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({24: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    41: (41, Multiset({25: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    42: (42, Multiset({26: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    43: (43, Multiset({27: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    44: (44, Multiset({28: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    45: (45, Multiset({29: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    46: (46, Multiset({30: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    47: (47, Multiset({31: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    48: (48, Multiset({32: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    49: (49, Multiset({33: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    50: (50, Multiset({34: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    51: (51, Multiset({35: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    52: (52, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Mul)
]),
    53: (53, Multiset({36: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    54: (54, Multiset({}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul)
]),
    55: (55, Multiset({37: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    56: (56, Multiset({38: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    57: (57, Multiset({}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Mul)
]),
    58: (58, Multiset({}), [
      (VariableWithCount('i2.2.1.0_4', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_5', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher3229._instance is None:
            CommutativeMatcher3229._instance = CommutativeMatcher3229()
        return CommutativeMatcher3229._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3228
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 4601
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.0', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 4602
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp5 = subjects2.popleft()
                        # State 4603
                        if len(subjects2) == 0:
                            pass
                            # State 4604
                            if len(subjects) == 0:
                                pass
                                # 0: v**2
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp6 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 5861
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp8 = subjects2.popleft()
                        # State 5862
                        if len(subjects2) == 0:
                            pass
                            # State 5863
                            if len(subjects) == 0:
                                pass
                                # 1: x**2
                        subjects2.appendleft(tmp8)
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7603
                            if len(subjects2) == 0:
                                pass
                                # State 7604
                                if len(subjects) == 0:
                                    pass
                                    # 6: x**j
                        subjects2.appendleft(tmp9)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7872
                        if len(subjects2) == 0:
                            pass
                            # State 7873
                            if len(subjects) == 0:
                                pass
                                # 8: x**n
                    if len(subjects2) >= 1:
                        tmp12 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp12)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7872
                            if len(subjects2) == 0:
                                pass
                                # State 7873
                                if len(subjects) == 0:
                                    pass
                                    # 8: x**n
                        subjects2.appendleft(tmp12)
                    if len(subjects2) >= 1:
                        tmp14 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp14)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9076
                            if len(subjects2) == 0:
                                pass
                                # State 9077
                                if len(subjects) == 0:
                                    pass
                                    # 9: x**n2
                        subjects2.appendleft(tmp14)
                subjects2.appendleft(tmp6)
            if len(subjects2) >= 1:
                tmp16 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1', tmp16)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7131
                    if len(subjects2) >= 1:
                        tmp18 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp18)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7132
                            if len(subjects2) == 0:
                                pass
                                # State 7133
                                if len(subjects) == 0:
                                    pass
                                    # 2: x**n
                        subjects2.appendleft(tmp18)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9152
                        if len(subjects2) == 0:
                            pass
                            # State 9153
                            if len(subjects) == 0:
                                pass
                                # 10: x**n2
                    if len(subjects2) >= 1:
                        tmp21 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp21)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9152
                            if len(subjects2) == 0:
                                pass
                                # State 9153
                                if len(subjects) == 0:
                                    pass
                                    # 10: x**n2
                        subjects2.appendleft(tmp21)
                subjects2.appendleft(tmp16)
            if len(subjects2) >= 1:
                tmp23 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0_1', tmp23)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7184
                    if len(subjects2) >= 1:
                        tmp25 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp25)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7185
                            if len(subjects2) == 0:
                                pass
                                # State 7186
                                if len(subjects) == 0:
                                    pass
                                    # 3: x**n
                        subjects2.appendleft(tmp25)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7501
                        if len(subjects2) == 0:
                            pass
                            # State 7502
                            if len(subjects) == 0:
                                pass
                                # 5: x**n
                    if len(subjects2) >= 1:
                        tmp28 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp28)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7501
                            if len(subjects2) == 0:
                                pass
                                # State 7502
                                if len(subjects) == 0:
                                    pass
                                    # 5: x**n
                        subjects2.appendleft(tmp28)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9675
                        if len(subjects2) == 0:
                            pass
                            # State 9676
                            if len(subjects) == 0:
                                pass
                                # 13: x**n2
                    if len(subjects2) >= 1:
                        tmp31 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_2', tmp31)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9675
                            if len(subjects2) == 0:
                                pass
                                # State 9676
                                if len(subjects) == 0:
                                    pass
                                    # 13: x**n2
                        subjects2.appendleft(tmp31)
                    if len(subjects2) >= 1:
                        tmp33 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp33)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9703
                            if len(subjects2) == 0:
                                pass
                                # State 9704
                                if len(subjects) == 0:
                                    pass
                                    # 14: x**mn
                        subjects2.appendleft(tmp33)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9711
                        if len(subjects2) == 0:
                            pass
                            # State 9712
                            if len(subjects) == 0:
                                pass
                                # 15: x**mn
                    if len(subjects2) >= 1:
                        tmp36 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp36)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9711
                            if len(subjects2) == 0:
                                pass
                                # State 9712
                                if len(subjects) == 0:
                                    pass
                                    # 15: x**mn
                        subjects2.appendleft(tmp36)
                subjects2.appendleft(tmp23)
            if len(subjects2) >= 1:
                tmp38 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0', tmp38)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7197
                    if len(subjects2) >= 1:
                        tmp40 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp40)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7198
                            if len(subjects2) == 0:
                                pass
                                # State 7199
                                if len(subjects) == 0:
                                    pass
                                    # 4: x**n
                        subjects2.appendleft(tmp40)
                    if len(subjects2) >= 1:
                        tmp42 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp42)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9247
                            if len(subjects2) == 0:
                                pass
                                # State 9248
                                if len(subjects) == 0:
                                    pass
                                    # 11: x**n2
                        subjects2.appendleft(tmp42)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9303
                        if len(subjects2) == 0:
                            pass
                            # State 9304
                            if len(subjects) == 0:
                                pass
                                # 12: x**n2
                    if len(subjects2) >= 1:
                        tmp45 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp45)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9303
                            if len(subjects2) == 0:
                                pass
                                # State 9304
                                if len(subjects) == 0:
                                    pass
                                    # 12: x**n2
                        subjects2.appendleft(tmp45)
                    if len(subjects2) >= 1:
                        tmp47 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_2', tmp47)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9733
                            if len(subjects2) == 0:
                                pass
                                # State 9734
                                if len(subjects) == 0:
                                    pass
                                    # 16: x**n2
                        subjects2.appendleft(tmp47)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12247
                        if len(subjects2) == 0:
                            pass
                            # State 12248
                            if len(subjects) == 0:
                                pass
                                # 17: x**n
                    if len(subjects2) >= 1:
                        tmp50 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_2', tmp50)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 12247
                            if len(subjects2) == 0:
                                pass
                                # State 12248
                                if len(subjects) == 0:
                                    pass
                                    # 17: x**n
                        subjects2.appendleft(tmp50)
                subjects2.appendleft(tmp38)
            if len(subjects2) >= 1:
                tmp52 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1_2', tmp52)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7808
                    if len(subjects2) >= 1:
                        tmp54 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp54)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7809
                            if len(subjects2) == 0:
                                pass
                                # State 7810
                                if len(subjects) == 0:
                                    pass
                                    # 7: w**n
                        subjects2.appendleft(tmp54)
                subjects2.appendleft(tmp52)
            if len(subjects2) >= 1:
                tmp56 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1.0', tmp56)
                except ValueError:
                    pass
                else:
                    pass
                    # State 110651
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp58 = subjects2.popleft()
                        # State 110652
                        if len(subjects2) == 0:
                            pass
                            # State 110653
                            if len(subjects) == 0:
                                pass
                                # 36: x**2
                        subjects2.appendleft(tmp58)
                subjects2.appendleft(tmp56)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp59 = subjects2.popleft()
                subjects60 = deque(tmp59._args)
                # State 63951
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63952
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 63953
                        if len(subjects60) >= 1:
                            tmp63 = subjects60.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp63)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 63954
                                if len(subjects60) == 0:
                                    pass
                                    # State 63955
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp65 = subjects2.popleft()
                                        # State 63956
                                        if len(subjects2) == 0:
                                            pass
                                            # State 63957
                                            if len(subjects) == 0:
                                                pass
                                                # 22: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp65)
                            subjects60.appendleft(tmp63)
                    if len(subjects60) >= 1 and isinstance(subjects60[0], Mul):
                        tmp66 = subjects60.popleft()
                        associative1 = tmp66
                        associative_type1 = type(tmp66)
                        subjects67 = deque(tmp66._args)
                        matcher = CommutativeMatcher63959.get()
                        tmp68 = subjects67
                        subjects67 = []
                        for s in tmp68:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp68, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 63960
                                if len(subjects60) == 0:
                                    pass
                                    # State 63961
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp69 = subjects2.popleft()
                                        # State 63962
                                        if len(subjects2) == 0:
                                            pass
                                            # State 63963
                                            if len(subjects) == 0:
                                                pass
                                                # 22: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp69)
                        subjects60.appendleft(tmp66)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 92316
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 92317
                        if len(subjects60) >= 1:
                            tmp72 = subjects60.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp72)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 92318
                                if len(subjects60) == 0:
                                    pass
                                    # State 92319
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp74 = subjects2.popleft()
                                        # State 92320
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92321
                                            if len(subjects) == 0:
                                                pass
                                                # 31: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp74)
                            subjects60.appendleft(tmp72)
                    if len(subjects60) >= 1 and isinstance(subjects60[0], Mul):
                        tmp75 = subjects60.popleft()
                        associative1 = tmp75
                        associative_type1 = type(tmp75)
                        subjects76 = deque(tmp75._args)
                        matcher = CommutativeMatcher92323.get()
                        tmp77 = subjects76
                        subjects76 = []
                        for s in tmp77:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp77, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 92324
                                if len(subjects60) == 0:
                                    pass
                                    # State 92325
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp78 = subjects2.popleft()
                                        # State 92326
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92327
                                            if len(subjects) == 0:
                                                pass
                                                # 31: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp78)
                        subjects60.appendleft(tmp75)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 93384
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 93385
                        if len(subjects60) >= 1:
                            tmp81 = subjects60.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp81)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 93386
                                if len(subjects60) == 0:
                                    pass
                                    # State 93387
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp83 = subjects2.popleft()
                                        # State 93388
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93389
                                            if len(subjects) == 0:
                                                pass
                                                # 33: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp83)
                            subjects60.appendleft(tmp81)
                    if len(subjects60) >= 1 and isinstance(subjects60[0], Mul):
                        tmp84 = subjects60.popleft()
                        associative1 = tmp84
                        associative_type1 = type(tmp84)
                        subjects85 = deque(tmp84._args)
                        matcher = CommutativeMatcher93391.get()
                        tmp86 = subjects85
                        subjects85 = []
                        for s in tmp86:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp86, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 93392
                                if len(subjects60) == 0:
                                    pass
                                    # State 93393
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp87 = subjects2.popleft()
                                        # State 93394
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93395
                                            if len(subjects) == 0:
                                                pass
                                                # 33: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp87)
                        subjects60.appendleft(tmp84)
                if len(subjects60) >= 1 and isinstance(subjects60[0], Add):
                    tmp88 = subjects60.popleft()
                    associative1 = tmp88
                    associative_type1 = type(tmp88)
                    subjects89 = deque(tmp88._args)
                    matcher = CommutativeMatcher63965.get()
                    tmp90 = subjects89
                    subjects89 = []
                    for s in tmp90:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp90, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63971
                            if len(subjects60) == 0:
                                pass
                                # State 63972
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp91 = subjects2.popleft()
                                    # State 63973
                                    if len(subjects2) == 0:
                                        pass
                                        # State 63974
                                        if len(subjects) == 0:
                                            pass
                                            # 22: 1/sin(e + x*f)
                                    subjects2.appendleft(tmp91)
                        if pattern_index == 1:
                            pass
                            # State 92331
                            if len(subjects60) == 0:
                                pass
                                # State 92332
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp92 = subjects2.popleft()
                                    # State 92333
                                    if len(subjects2) == 0:
                                        pass
                                        # State 92334
                                        if len(subjects) == 0:
                                            pass
                                            # 31: 1/sin(e + x*f)
                                    subjects2.appendleft(tmp92)
                        if pattern_index == 2:
                            pass
                            # State 93399
                            if len(subjects60) == 0:
                                pass
                                # State 93400
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp93 = subjects2.popleft()
                                    # State 93401
                                    if len(subjects2) == 0:
                                        pass
                                        # State 93402
                                        if len(subjects) == 0:
                                            pass
                                            # 33: 1/sin(e + x*f)
                                    subjects2.appendleft(tmp93)
                    subjects60.appendleft(tmp88)
                subjects2.appendleft(tmp59)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp94 = subjects2.popleft()
                subjects95 = deque(tmp94._args)
                # State 64230
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 64231
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 64232
                        if len(subjects95) >= 1:
                            tmp98 = subjects95.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp98)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 64233
                                if len(subjects95) == 0:
                                    pass
                                    # State 64234
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp100 = subjects2.popleft()
                                        # State 64235
                                        if len(subjects2) == 0:
                                            pass
                                            # State 64236
                                            if len(subjects) == 0:
                                                pass
                                                # 23: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp100)
                            subjects95.appendleft(tmp98)
                    if len(subjects95) >= 1 and isinstance(subjects95[0], Mul):
                        tmp101 = subjects95.popleft()
                        associative1 = tmp101
                        associative_type1 = type(tmp101)
                        subjects102 = deque(tmp101._args)
                        matcher = CommutativeMatcher64238.get()
                        tmp103 = subjects102
                        subjects102 = []
                        for s in tmp103:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp103, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 64239
                                if len(subjects95) == 0:
                                    pass
                                    # State 64240
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp104 = subjects2.popleft()
                                        # State 64241
                                        if len(subjects2) == 0:
                                            pass
                                            # State 64242
                                            if len(subjects) == 0:
                                                pass
                                                # 23: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp104)
                        subjects95.appendleft(tmp101)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 92250
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 92251
                        if len(subjects95) >= 1:
                            tmp107 = subjects95.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp107)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 92252
                                if len(subjects95) == 0:
                                    pass
                                    # State 92253
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp109 = subjects2.popleft()
                                        # State 92254
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92255
                                            if len(subjects) == 0:
                                                pass
                                                # 30: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp109)
                            subjects95.appendleft(tmp107)
                    if len(subjects95) >= 1 and isinstance(subjects95[0], Mul):
                        tmp110 = subjects95.popleft()
                        associative1 = tmp110
                        associative_type1 = type(tmp110)
                        subjects111 = deque(tmp110._args)
                        matcher = CommutativeMatcher92257.get()
                        tmp112 = subjects111
                        subjects111 = []
                        for s in tmp112:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp112, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 92258
                                if len(subjects95) == 0:
                                    pass
                                    # State 92259
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp113 = subjects2.popleft()
                                        # State 92260
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92261
                                            if len(subjects) == 0:
                                                pass
                                                # 30: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp113)
                        subjects95.appendleft(tmp110)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 93198
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 93199
                        if len(subjects95) >= 1:
                            tmp116 = subjects95.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp116)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 93200
                                if len(subjects95) == 0:
                                    pass
                                    # State 93201
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp118 = subjects2.popleft()
                                        # State 93202
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93203
                                            if len(subjects) == 0:
                                                pass
                                                # 32: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp118)
                            subjects95.appendleft(tmp116)
                    if len(subjects95) >= 1 and isinstance(subjects95[0], Mul):
                        tmp119 = subjects95.popleft()
                        associative1 = tmp119
                        associative_type1 = type(tmp119)
                        subjects120 = deque(tmp119._args)
                        matcher = CommutativeMatcher93205.get()
                        tmp121 = subjects120
                        subjects120 = []
                        for s in tmp121:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp121, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 93206
                                if len(subjects95) == 0:
                                    pass
                                    # State 93207
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp122 = subjects2.popleft()
                                        # State 93208
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93209
                                            if len(subjects) == 0:
                                                pass
                                                # 32: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp122)
                        subjects95.appendleft(tmp119)
                if len(subjects95) >= 1 and isinstance(subjects95[0], Add):
                    tmp123 = subjects95.popleft()
                    associative1 = tmp123
                    associative_type1 = type(tmp123)
                    subjects124 = deque(tmp123._args)
                    matcher = CommutativeMatcher64244.get()
                    tmp125 = subjects124
                    subjects124 = []
                    for s in tmp125:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp125, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 64250
                            if len(subjects95) == 0:
                                pass
                                # State 64251
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp126 = subjects2.popleft()
                                    # State 64252
                                    if len(subjects2) == 0:
                                        pass
                                        # State 64253
                                        if len(subjects) == 0:
                                            pass
                                            # 23: 1/cos(e + x*f)
                                    subjects2.appendleft(tmp126)
                        if pattern_index == 1:
                            pass
                            # State 92265
                            if len(subjects95) == 0:
                                pass
                                # State 92266
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp127 = subjects2.popleft()
                                    # State 92267
                                    if len(subjects2) == 0:
                                        pass
                                        # State 92268
                                        if len(subjects) == 0:
                                            pass
                                            # 30: 1/cos(e + x*f)
                                    subjects2.appendleft(tmp127)
                        if pattern_index == 2:
                            pass
                            # State 93213
                            if len(subjects95) == 0:
                                pass
                                # State 93214
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp128 = subjects2.popleft()
                                    # State 93215
                                    if len(subjects2) == 0:
                                        pass
                                        # State 93216
                                        if len(subjects) == 0:
                                            pass
                                            # 32: 1/cos(e + x*f)
                                    subjects2.appendleft(tmp128)
                    subjects95.appendleft(tmp123)
                subjects2.appendleft(tmp94)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp129 = subjects2.popleft()
                subjects130 = deque(tmp129._args)
                # State 80589
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80590
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80591
                        if len(subjects130) >= 1:
                            tmp133 = subjects130.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp133)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80592
                                if len(subjects130) == 0:
                                    pass
                                    # State 80593
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp135 = subjects2.popleft()
                                        # State 80594
                                        if len(subjects2) == 0:
                                            pass
                                            # State 80595
                                            if len(subjects) == 0:
                                                pass
                                                # 27: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp135)
                            subjects130.appendleft(tmp133)
                    if len(subjects130) >= 1 and isinstance(subjects130[0], Mul):
                        tmp136 = subjects130.popleft()
                        associative1 = tmp136
                        associative_type1 = type(tmp136)
                        subjects137 = deque(tmp136._args)
                        matcher = CommutativeMatcher80597.get()
                        tmp138 = subjects137
                        subjects137 = []
                        for s in tmp138:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp138, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80598
                                if len(subjects130) == 0:
                                    pass
                                    # State 80599
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp139 = subjects2.popleft()
                                        # State 80600
                                        if len(subjects2) == 0:
                                            pass
                                            # State 80601
                                            if len(subjects) == 0:
                                                pass
                                                # 27: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp139)
                        subjects130.appendleft(tmp136)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80923
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80924
                        if len(subjects130) >= 1:
                            tmp142 = subjects130.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.4.1.0', tmp142)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80925
                                if len(subjects130) == 0:
                                    pass
                                    # State 80926
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp144 = subjects2.popleft()
                                        # State 80927
                                        if len(subjects2) == 0:
                                            pass
                                            # State 80928
                                            if len(subjects) == 0:
                                                pass
                                                # 28: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp144)
                            subjects130.appendleft(tmp142)
                    if len(subjects130) >= 1 and isinstance(subjects130[0], Mul):
                        tmp145 = subjects130.popleft()
                        associative1 = tmp145
                        associative_type1 = type(tmp145)
                        subjects146 = deque(tmp145._args)
                        matcher = CommutativeMatcher80930.get()
                        tmp147 = subjects146
                        subjects146 = []
                        for s in tmp147:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp147, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80931
                                if len(subjects130) == 0:
                                    pass
                                    # State 80932
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp148 = subjects2.popleft()
                                        # State 80933
                                        if len(subjects2) == 0:
                                            pass
                                            # State 80934
                                            if len(subjects) == 0:
                                                pass
                                                # 28: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp148)
                        subjects130.appendleft(tmp145)
                if len(subjects130) >= 1 and isinstance(subjects130[0], Add):
                    tmp149 = subjects130.popleft()
                    associative1 = tmp149
                    associative_type1 = type(tmp149)
                    subjects150 = deque(tmp149._args)
                    matcher = CommutativeMatcher80603.get()
                    tmp151 = subjects150
                    subjects150 = []
                    for s in tmp151:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp151, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 80609
                            if len(subjects130) == 0:
                                pass
                                # State 80610
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp152 = subjects2.popleft()
                                    # State 80611
                                    if len(subjects2) == 0:
                                        pass
                                        # State 80612
                                        if len(subjects) == 0:
                                            pass
                                            # 27: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp152)
                        if pattern_index == 1:
                            pass
                            # State 80938
                            if len(subjects130) == 0:
                                pass
                                # State 80939
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp153 = subjects2.popleft()
                                    # State 80940
                                    if len(subjects2) == 0:
                                        pass
                                        # State 80941
                                        if len(subjects) == 0:
                                            pass
                                            # 28: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp153)
                    subjects130.appendleft(tmp149)
                subjects2.appendleft(tmp129)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 7499
            if len(subjects) >= 1:
                tmp155 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0_1', tmp155)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7500
                    if len(subjects) == 0:
                        pass
                        # 5: x**n
                subjects.appendleft(tmp155)
            if len(subjects) >= 1:
                tmp157 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp157)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7871
                    if len(subjects) == 0:
                        pass
                        # 8: x**n
                subjects.appendleft(tmp157)
            if len(subjects) >= 1:
                tmp159 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp159)
                except ValueError:
                    pass
                else:
                    pass
                    # State 9302
                    if len(subjects) == 0:
                        pass
                        # 12: x**n2
                subjects.appendleft(tmp159)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 9150
            if len(subjects) >= 1:
                tmp162 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1', tmp162)
                except ValueError:
                    pass
                else:
                    pass
                    # State 9151
                    if len(subjects) == 0:
                        pass
                        # 10: x**n2
                subjects.appendleft(tmp162)
            if len(subjects) >= 1:
                tmp164 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0_1', tmp164)
                except ValueError:
                    pass
                else:
                    pass
                    # State 9710
                    if len(subjects) == 0:
                        pass
                        # 15: x**mn
                subjects.appendleft(tmp164)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 9673
            if len(subjects) >= 1:
                tmp167 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0_1', tmp167)
                except ValueError:
                    pass
                else:
                    pass
                    # State 9674
                    if len(subjects) == 0:
                        pass
                        # 13: x**n2
                subjects.appendleft(tmp167)
            if len(subjects) >= 1:
                tmp169 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp169)
                except ValueError:
                    pass
                else:
                    pass
                    # State 12246
                    if len(subjects) == 0:
                        pass
                        # 17: x**n
                subjects.appendleft(tmp169)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp171 = subjects.popleft()
            subjects172 = deque(tmp171._args)
            # State 62277
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 62278
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 62279
                    if len(subjects172) >= 1:
                        tmp175 = subjects172.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp175)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 62280
                            if len(subjects172) == 0:
                                pass
                                # State 62281
                                if len(subjects) == 0:
                                    pass
                                    # 18: sin(e + x*f)
                        subjects172.appendleft(tmp175)
                if len(subjects172) >= 1 and isinstance(subjects172[0], Mul):
                    tmp177 = subjects172.popleft()
                    associative1 = tmp177
                    associative_type1 = type(tmp177)
                    subjects178 = deque(tmp177._args)
                    matcher = CommutativeMatcher62283.get()
                    tmp179 = subjects178
                    subjects178 = []
                    for s in tmp179:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp179, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 62284
                            if len(subjects172) == 0:
                                pass
                                # State 62285
                                if len(subjects) == 0:
                                    pass
                                    # 18: sin(e + x*f)
                    subjects172.appendleft(tmp177)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63295
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63296
                    if len(subjects172) >= 1:
                        tmp182 = subjects172.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp182)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63297
                            if len(subjects172) == 0:
                                pass
                                # State 63298
                                if len(subjects) == 0:
                                    pass
                                    # 20: sin(e + x*f)
                        subjects172.appendleft(tmp182)
                if len(subjects172) >= 1 and isinstance(subjects172[0], Mul):
                    tmp184 = subjects172.popleft()
                    associative1 = tmp184
                    associative_type1 = type(tmp184)
                    subjects185 = deque(tmp184._args)
                    matcher = CommutativeMatcher63300.get()
                    tmp186 = subjects185
                    subjects185 = []
                    for s in tmp186:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp186, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63301
                            if len(subjects172) == 0:
                                pass
                                # State 63302
                                if len(subjects) == 0:
                                    pass
                                    # 20: sin(e + x*f)
                    subjects172.appendleft(tmp184)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 65415
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65416
                    if len(subjects172) >= 1:
                        tmp189 = subjects172.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp189)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 65417
                            if len(subjects172) == 0:
                                pass
                                # State 65418
                                if len(subjects) == 0:
                                    pass
                                    # 24: sin(c + x*d)
                        subjects172.appendleft(tmp189)
                if len(subjects172) >= 1 and isinstance(subjects172[0], Mul):
                    tmp191 = subjects172.popleft()
                    associative1 = tmp191
                    associative_type1 = type(tmp191)
                    subjects192 = deque(tmp191._args)
                    matcher = CommutativeMatcher65420.get()
                    tmp193 = subjects192
                    subjects192 = []
                    for s in tmp193:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp193, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 65421
                            if len(subjects172) == 0:
                                pass
                                # State 65422
                                if len(subjects) == 0:
                                    pass
                                    # 24: sin(c + x*d)
                    subjects172.appendleft(tmp191)
            if len(subjects172) >= 1 and isinstance(subjects172[0], Add):
                tmp194 = subjects172.popleft()
                associative1 = tmp194
                associative_type1 = type(tmp194)
                subjects195 = deque(tmp194._args)
                matcher = CommutativeMatcher62287.get()
                tmp196 = subjects195
                subjects195 = []
                for s in tmp196:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp196, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 62293
                        if len(subjects172) == 0:
                            pass
                            # State 62294
                            if len(subjects) == 0:
                                pass
                                # 18: sin(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 63306
                        if len(subjects172) == 0:
                            pass
                            # State 63307
                            if len(subjects) == 0:
                                pass
                                # 20: sin(e + x*f)
                    if pattern_index == 2:
                        pass
                        # State 65426
                        if len(subjects172) == 0:
                            pass
                            # State 65427
                            if len(subjects) == 0:
                                pass
                                # 24: sin(c + x*d)
                subjects172.appendleft(tmp194)
            subjects.appendleft(tmp171)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp197 = subjects.popleft()
            subjects198 = deque(tmp197._args)
            # State 62335
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 62336
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 62337
                    if len(subjects198) >= 1:
                        tmp201 = subjects198.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp201)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 62338
                            if len(subjects198) == 0:
                                pass
                                # State 62339
                                if len(subjects) == 0:
                                    pass
                                    # 19: cos(e + x*f)
                        subjects198.appendleft(tmp201)
                if len(subjects198) >= 1 and isinstance(subjects198[0], Mul):
                    tmp203 = subjects198.popleft()
                    associative1 = tmp203
                    associative_type1 = type(tmp203)
                    subjects204 = deque(tmp203._args)
                    matcher = CommutativeMatcher62341.get()
                    tmp205 = subjects204
                    subjects204 = []
                    for s in tmp205:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp205, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 62342
                            if len(subjects198) == 0:
                                pass
                                # State 62343
                                if len(subjects) == 0:
                                    pass
                                    # 19: cos(e + x*f)
                    subjects198.appendleft(tmp203)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63471
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63472
                    if len(subjects198) >= 1:
                        tmp208 = subjects198.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp208)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63473
                            if len(subjects198) == 0:
                                pass
                                # State 63474
                                if len(subjects) == 0:
                                    pass
                                    # 21: cos(e + x*f)
                        subjects198.appendleft(tmp208)
                if len(subjects198) >= 1 and isinstance(subjects198[0], Mul):
                    tmp210 = subjects198.popleft()
                    associative1 = tmp210
                    associative_type1 = type(tmp210)
                    subjects211 = deque(tmp210._args)
                    matcher = CommutativeMatcher63476.get()
                    tmp212 = subjects211
                    subjects211 = []
                    for s in tmp212:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp212, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63477
                            if len(subjects198) == 0:
                                pass
                                # State 63478
                                if len(subjects) == 0:
                                    pass
                                    # 21: cos(e + x*f)
                    subjects198.appendleft(tmp210)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 65473
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65474
                    if len(subjects198) >= 1:
                        tmp215 = subjects198.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp215)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 65475
                            if len(subjects198) == 0:
                                pass
                                # State 65476
                                if len(subjects) == 0:
                                    pass
                                    # 25: cos(c + x*d)
                        subjects198.appendleft(tmp215)
                if len(subjects198) >= 1 and isinstance(subjects198[0], Mul):
                    tmp217 = subjects198.popleft()
                    associative1 = tmp217
                    associative_type1 = type(tmp217)
                    subjects218 = deque(tmp217._args)
                    matcher = CommutativeMatcher65478.get()
                    tmp219 = subjects218
                    subjects218 = []
                    for s in tmp219:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp219, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 65479
                            if len(subjects198) == 0:
                                pass
                                # State 65480
                                if len(subjects) == 0:
                                    pass
                                    # 25: cos(c + x*d)
                    subjects198.appendleft(tmp217)
            if len(subjects198) >= 1 and isinstance(subjects198[0], Add):
                tmp220 = subjects198.popleft()
                associative1 = tmp220
                associative_type1 = type(tmp220)
                subjects221 = deque(tmp220._args)
                matcher = CommutativeMatcher62345.get()
                tmp222 = subjects221
                subjects221 = []
                for s in tmp222:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp222, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 62351
                        if len(subjects198) == 0:
                            pass
                            # State 62352
                            if len(subjects) == 0:
                                pass
                                # 19: cos(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 63482
                        if len(subjects198) == 0:
                            pass
                            # State 63483
                            if len(subjects) == 0:
                                pass
                                # 21: cos(e + x*f)
                    if pattern_index == 2:
                        pass
                        # State 65484
                        if len(subjects198) == 0:
                            pass
                            # State 65485
                            if len(subjects) == 0:
                                pass
                                # 25: cos(c + x*d)
                subjects198.appendleft(tmp220)
            subjects.appendleft(tmp197)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp223 = subjects.popleft()
            subjects224 = deque(tmp223._args)
            # State 80525
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 80526
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80527
                    if len(subjects224) >= 1:
                        tmp227 = subjects224.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp227)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 80528
                            if len(subjects224) == 0:
                                pass
                                # State 80529
                                if len(subjects) == 0:
                                    pass
                                    # 26: tan(e + x*f)
                        subjects224.appendleft(tmp227)
                if len(subjects224) >= 1 and isinstance(subjects224[0], Mul):
                    tmp229 = subjects224.popleft()
                    associative1 = tmp229
                    associative_type1 = type(tmp229)
                    subjects230 = deque(tmp229._args)
                    matcher = CommutativeMatcher80531.get()
                    tmp231 = subjects230
                    subjects230 = []
                    for s in tmp231:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp231, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 80532
                            if len(subjects224) == 0:
                                pass
                                # State 80533
                                if len(subjects) == 0:
                                    pass
                                    # 26: tan(e + x*f)
                    subjects224.appendleft(tmp229)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 80983
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80984
                    if len(subjects224) >= 1:
                        tmp234 = subjects224.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp234)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 80985
                            if len(subjects224) == 0:
                                pass
                                # State 80986
                                if len(subjects) == 0:
                                    pass
                                    # 29: tan(e + x*f)
                        subjects224.appendleft(tmp234)
                if len(subjects224) >= 1 and isinstance(subjects224[0], Mul):
                    tmp236 = subjects224.popleft()
                    associative1 = tmp236
                    associative_type1 = type(tmp236)
                    subjects237 = deque(tmp236._args)
                    matcher = CommutativeMatcher80988.get()
                    tmp238 = subjects237
                    subjects237 = []
                    for s in tmp238:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp238, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 80989
                            if len(subjects224) == 0:
                                pass
                                # State 80990
                                if len(subjects) == 0:
                                    pass
                                    # 29: tan(e + x*f)
                    subjects224.appendleft(tmp236)
            if len(subjects224) >= 1 and isinstance(subjects224[0], Add):
                tmp239 = subjects224.popleft()
                associative1 = tmp239
                associative_type1 = type(tmp239)
                subjects240 = deque(tmp239._args)
                matcher = CommutativeMatcher80535.get()
                tmp241 = subjects240
                subjects240 = []
                for s in tmp241:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp241, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 80541
                        if len(subjects224) == 0:
                            pass
                            # State 80542
                            if len(subjects) == 0:
                                pass
                                # 26: tan(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 80994
                        if len(subjects224) == 0:
                            pass
                            # State 80995
                            if len(subjects) == 0:
                                pass
                                # 29: tan(e + x*f)
                subjects224.appendleft(tmp239)
            subjects.appendleft(tmp223)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp242 = subjects.popleft()
            subjects243 = deque(tmp242._args)
            # State 109036
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109037
                if len(subjects243) >= 1:
                    tmp245 = subjects243.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp245)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109038
                        if len(subjects243) == 0:
                            pass
                            # State 109039
                            if len(subjects) == 0:
                                pass
                                # 34: asin(x*c)
                    subjects243.appendleft(tmp245)
            if len(subjects243) >= 1 and isinstance(subjects243[0], Mul):
                tmp247 = subjects243.popleft()
                associative1 = tmp247
                associative_type1 = type(tmp247)
                subjects248 = deque(tmp247._args)
                matcher = CommutativeMatcher109041.get()
                tmp249 = subjects248
                subjects248 = []
                for s in tmp249:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp249, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 109042
                        if len(subjects243) == 0:
                            pass
                            # State 109043
                            if len(subjects) == 0:
                                pass
                                # 34: asin(x*c)
                subjects243.appendleft(tmp247)
            subjects.appendleft(tmp242)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp250 = subjects.popleft()
            subjects251 = deque(tmp250._args)
            # State 109105
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109106
                if len(subjects251) >= 1:
                    tmp253 = subjects251.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp253)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109107
                        if len(subjects251) == 0:
                            pass
                            # State 109108
                            if len(subjects) == 0:
                                pass
                                # 35: acos(x*c)
                    subjects251.appendleft(tmp253)
            if len(subjects251) >= 1 and isinstance(subjects251[0], Mul):
                tmp255 = subjects251.popleft()
                associative1 = tmp255
                associative_type1 = type(tmp255)
                subjects256 = deque(tmp255._args)
                matcher = CommutativeMatcher109110.get()
                tmp257 = subjects256
                subjects256 = []
                for s in tmp257:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp257, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 109111
                        if len(subjects251) == 0:
                            pass
                            # State 109112
                            if len(subjects) == 0:
                                pass
                                # 35: acos(x*c)
                subjects251.appendleft(tmp255)
            subjects.appendleft(tmp250)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp258 = subjects.popleft()
            subjects259 = deque(tmp258._args)
            # State 138795
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138796
                if len(subjects259) >= 1:
                    tmp261 = subjects259.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp261)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138797
                        if len(subjects259) == 0:
                            pass
                            # State 138798
                            if len(subjects) == 0:
                                pass
                                # 37: acosh(x*c)
                    subjects259.appendleft(tmp261)
            if len(subjects259) >= 1 and isinstance(subjects259[0], Mul):
                tmp263 = subjects259.popleft()
                associative1 = tmp263
                associative_type1 = type(tmp263)
                subjects264 = deque(tmp263._args)
                matcher = CommutativeMatcher138800.get()
                tmp265 = subjects264
                subjects264 = []
                for s in tmp265:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp265, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138801
                        if len(subjects259) == 0:
                            pass
                            # State 138802
                            if len(subjects) == 0:
                                pass
                                # 37: acosh(x*c)
                subjects259.appendleft(tmp263)
            subjects.appendleft(tmp258)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp266 = subjects.popleft()
            subjects267 = deque(tmp266._args)
            # State 138864
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138865
                if len(subjects267) >= 1:
                    tmp269 = subjects267.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp269)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138866
                        if len(subjects267) == 0:
                            pass
                            # State 138867
                            if len(subjects) == 0:
                                pass
                                # 38: asinh(x*c)
                    subjects267.appendleft(tmp269)
            if len(subjects267) >= 1 and isinstance(subjects267[0], Mul):
                tmp271 = subjects267.popleft()
                associative1 = tmp271
                associative_type1 = type(tmp271)
                subjects272 = deque(tmp271._args)
                matcher = CommutativeMatcher138869.get()
                tmp273 = subjects272
                subjects272 = []
                for s in tmp273:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp273, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138870
                        if len(subjects267) == 0:
                            pass
                            # State 138871
                            if len(subjects) == 0:
                                pass
                                # 38: asinh(x*c)
                subjects267.appendleft(tmp271)
            subjects.appendleft(tmp266)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
