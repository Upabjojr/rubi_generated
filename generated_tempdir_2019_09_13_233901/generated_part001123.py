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

class CommutativeMatcher9979(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({10: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({11: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({12: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({13: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({14: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({15: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({16: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({17: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({18: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({19: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({20: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({21: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({22: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({23: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({24: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({25: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({26: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    27: (27, Multiset({27: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({28: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({29: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({30: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    31: (31, Multiset({31: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({32: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    33: (33, Multiset({33: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({34: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({35: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    36: (36, Multiset({36: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    37: (37, Multiset({37: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    38: (38, Multiset({38: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({39: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({40: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    41: (41, Multiset({41: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    42: (42, Multiset({42: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    43: (43, Multiset({43: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    44: (44, Multiset({44: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    45: (45, Multiset({45: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    46: (46, Multiset({46: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    47: (47, Multiset({47: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    48: (48, Multiset({48: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    49: (49, Multiset({49: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    50: (50, Multiset({50: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    51: (51, Multiset({51: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    52: (52, Multiset({52: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    53: (53, Multiset({53: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    54: (54, Multiset({54: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    55: (55, Multiset({55: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    56: (56, Multiset({56: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    57: (57, Multiset({57: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    58: (58, Multiset({58: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    59: (59, Multiset({59: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    60: (60, Multiset({60: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    61: (61, Multiset({61: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    62: (62, Multiset({62: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    63: (63, Multiset({63: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    64: (64, Multiset({64: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    65: (65, Multiset({65: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    66: (66, Multiset({66: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    67: (67, Multiset({67: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    68: (68, Multiset({68: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    69: (69, Multiset({69: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher9979._instance is None:
            CommutativeMatcher9979._instance = CommutativeMatcher9979()
        return CommutativeMatcher9979._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 9978
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 9980
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 9981
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp4 = subjects2.popleft()
                    subjects5 = deque(tmp4._args)
                    # State 9982
                    if len(subjects5) >= 1:
                        tmp6 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.1', tmp6)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9983
                            if len(subjects5) >= 1:
                                tmp8 = subjects5.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', tmp8)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 9984
                                    if len(subjects5) == 0:
                                        pass
                                        # State 9985
                                        if len(subjects2) >= 1:
                                            tmp10 = subjects2.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2', tmp10)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 9986
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 9987
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (c*x**n)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f52) and (cons_f4) and (cons_f5) and (cons_f800)
                                            subjects2.appendleft(tmp10)
                                subjects5.appendleft(tmp8)
                        subjects5.appendleft(tmp6)
                    subjects2.appendleft(tmp4)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp12 = subjects2.popleft()
                associative1 = tmp12
                associative_type1 = type(tmp12)
                subjects13 = deque(tmp12._args)
                matcher = CommutativeMatcher9989.get()
                tmp14 = subjects13
                subjects13 = []
                for s in tmp14:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp14, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 9994
                        if len(subjects2) >= 1:
                            tmp15 = []
                            tmp15.append(subjects2.popleft())
                            while True:
                                if len(tmp15) > 1:
                                    tmp16 = create_operation_expression(associative1, tmp15)
                                elif len(tmp15) == 1:
                                    tmp16 = tmp15[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp16)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 9995
                                    if len(subjects2) == 0:
                                        pass
                                        # State 9996
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (c*x**n)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f52) and (cons_f4) and (cons_f5) and (cons_f800)
                                if len(subjects2) == 0:
                                    break
                                tmp15.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp15))
                subjects2.appendleft(tmp12)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp18 = subjects2.popleft()
                associative1 = tmp18
                associative_type1 = type(tmp18)
                subjects19 = deque(tmp18._args)
                matcher = CommutativeMatcher13169.get()
                tmp20 = subjects19
                subjects19 = []
                for s in tmp20:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp20, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 13219
                        if len(subjects2) >= 1:
                            tmp21 = []
                            tmp21.append(subjects2.popleft())
                            while True:
                                if len(tmp21) > 1:
                                    tmp22 = create_operation_expression(associative1, tmp21)
                                elif len(tmp21) == 1:
                                    tmp22 = tmp21[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp22)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 13220
                                    if len(subjects2) == 0:
                                        pass
                                        # State 13221
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d + e*x + f*sqrt(a + b*x + c*x**2))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                                if len(subjects2) == 0:
                                    break
                                tmp21.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp21))
                    if pattern_index == 1:
                        pass
                        # State 13587
                        if len(subjects2) >= 1:
                            tmp24 = []
                            tmp24.append(subjects2.popleft())
                            while True:
                                if len(tmp24) > 1:
                                    tmp25 = create_operation_expression(associative1, tmp24)
                                elif len(tmp24) == 1:
                                    tmp25 = tmp24[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp25)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 13588
                                    if len(subjects2) == 0:
                                        pass
                                        # State 13589
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (d + e*x + f*sqrt(a + c*x**2))**n /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                                if len(subjects2) == 0:
                                    break
                                tmp24.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp24))
                    if pattern_index == 2:
                        pass
                        # State 13691
                        if len(subjects2) >= 1:
                            tmp27 = []
                            tmp27.append(subjects2.popleft())
                            while True:
                                if len(tmp27) > 1:
                                    tmp28 = create_operation_expression(associative1, tmp27)
                                elif len(tmp27) == 1:
                                    tmp28 = tmp27[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp28)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 13692
                                    if len(subjects2) == 0:
                                        pass
                                        # State 13693
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (u + f*sqrt(v))**n /; (cons_f127) and (cons_f4) and (cons_f70) and (cons_f820) and (cons_f821) and (cons_f1058)
                                if len(subjects2) == 0:
                                    break
                                tmp27.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp27))
                subjects2.appendleft(tmp18)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp30 = subjects2.popleft()
                subjects31 = deque(tmp30._args)
                # State 87407
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 87408
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 87409
                        if len(subjects31) >= 1 and isinstance(subjects31[0], Pow):
                            tmp34 = subjects31.popleft()
                            subjects35 = deque(tmp34._args)
                            # State 87410
                            if len(subjects35) >= 1:
                                tmp36 = subjects35.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp36)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 87411
                                    if len(subjects35) >= 1:
                                        tmp38 = subjects35.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp38)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 87412
                                            if len(subjects35) == 0:
                                                pass
                                                # State 87413
                                                if len(subjects31) == 0:
                                                    pass
                                                    # State 87414
                                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                                        tmp40 = subjects2.popleft()
                                                        # State 87415
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 87416
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 17: 1/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                # 19: 1/tan(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                # 15: 1/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                        subjects2.appendleft(tmp40)
                                        subjects35.appendleft(tmp38)
                                subjects35.appendleft(tmp36)
                            subjects31.appendleft(tmp34)
                    if len(subjects31) >= 1 and isinstance(subjects31[0], Mul):
                        tmp41 = subjects31.popleft()
                        associative1 = tmp41
                        associative_type1 = type(tmp41)
                        subjects42 = deque(tmp41._args)
                        matcher = CommutativeMatcher87418.get()
                        tmp43 = subjects42
                        subjects42 = []
                        for s in tmp43:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp43, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 87423
                                if len(subjects31) == 0:
                                    pass
                                    # State 87424
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp44 = subjects2.popleft()
                                        # State 87425
                                        if len(subjects2) == 0:
                                            pass
                                            # State 87426
                                            if len(subjects) == 0:
                                                pass
                                                # 17: 1/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                # 19: 1/tan(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                # 15: 1/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                        subjects2.appendleft(tmp44)
                        subjects31.appendleft(tmp41)
                if len(subjects31) >= 1:
                    tmp45 = subjects31.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp45)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 87885
                        if len(subjects31) == 0:
                            pass
                            # State 87886
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp47 = subjects2.popleft()
                                # State 87887
                                if len(subjects2) == 0:
                                    pass
                                    # State 87888
                                    if len(subjects) == 0:
                                        pass
                                        # 21: 1/tan(u) /; (cons_f825) and (cons_f826)
                                subjects2.appendleft(tmp47)
                    subjects31.appendleft(tmp45)
                if len(subjects31) >= 1 and isinstance(subjects31[0], Add):
                    tmp48 = subjects31.popleft()
                    associative1 = tmp48
                    associative_type1 = type(tmp48)
                    subjects49 = deque(tmp48._args)
                    matcher = CommutativeMatcher87428.get()
                    tmp50 = subjects49
                    subjects49 = []
                    for s in tmp50:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp50, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 87441
                            if len(subjects31) == 0:
                                pass
                                # State 87442
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp51 = subjects2.popleft()
                                    # State 87443
                                    if len(subjects2) == 0:
                                        pass
                                        # State 87444
                                        if len(subjects) == 0:
                                            pass
                                            # 17: 1/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                            # 19: 1/tan(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            # 15: 1/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                    subjects2.appendleft(tmp51)
                    subjects31.appendleft(tmp48)
                subjects2.appendleft(tmp30)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp52 = subjects2.popleft()
                subjects53 = deque(tmp52._args)
                # State 97462
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 97463
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 97464
                        if len(subjects53) >= 1 and isinstance(subjects53[0], Pow):
                            tmp56 = subjects53.popleft()
                            subjects57 = deque(tmp56._args)
                            # State 97465
                            if len(subjects57) >= 1:
                                tmp58 = subjects57.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp58)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 97466
                                    if len(subjects57) >= 1:
                                        tmp60 = subjects57.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp60)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 97467
                                            if len(subjects57) == 0:
                                                pass
                                                # State 97468
                                                if len(subjects53) == 0:
                                                    pass
                                                    # State 97469
                                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                                        tmp62 = subjects2.popleft()
                                                        # State 97470
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 97471
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 24: 1/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                # 26: 1/cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                # 22: 1/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                        subjects2.appendleft(tmp62)
                                        subjects57.appendleft(tmp60)
                                subjects57.appendleft(tmp58)
                            subjects53.appendleft(tmp56)
                    if len(subjects53) >= 1 and isinstance(subjects53[0], Mul):
                        tmp63 = subjects53.popleft()
                        associative1 = tmp63
                        associative_type1 = type(tmp63)
                        subjects64 = deque(tmp63._args)
                        matcher = CommutativeMatcher97473.get()
                        tmp65 = subjects64
                        subjects64 = []
                        for s in tmp65:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp65, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 97478
                                if len(subjects53) == 0:
                                    pass
                                    # State 97479
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp66 = subjects2.popleft()
                                        # State 97480
                                        if len(subjects2) == 0:
                                            pass
                                            # State 97481
                                            if len(subjects) == 0:
                                                pass
                                                # 24: 1/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                # 26: 1/cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                # 22: 1/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                        subjects2.appendleft(tmp66)
                        subjects53.appendleft(tmp63)
                if len(subjects53) >= 1:
                    tmp67 = subjects53.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp67)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98224
                        if len(subjects53) == 0:
                            pass
                            # State 98225
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp69 = subjects2.popleft()
                                # State 98226
                                if len(subjects2) == 0:
                                    pass
                                    # State 98227
                                    if len(subjects) == 0:
                                        pass
                                        # 28: 1/cos(u) /; (cons_f825) and (cons_f826)
                                subjects2.appendleft(tmp69)
                    subjects53.appendleft(tmp67)
                if len(subjects53) >= 1 and isinstance(subjects53[0], Add):
                    tmp70 = subjects53.popleft()
                    associative1 = tmp70
                    associative_type1 = type(tmp70)
                    subjects71 = deque(tmp70._args)
                    matcher = CommutativeMatcher97483.get()
                    tmp72 = subjects71
                    subjects71 = []
                    for s in tmp72:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp72, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 97496
                            if len(subjects53) == 0:
                                pass
                                # State 97497
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp73 = subjects2.popleft()
                                    # State 97498
                                    if len(subjects2) == 0:
                                        pass
                                        # State 97499
                                        if len(subjects) == 0:
                                            pass
                                            # 24: 1/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                            # 26: 1/cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            # 22: 1/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                    subjects2.appendleft(tmp73)
                    subjects53.appendleft(tmp70)
                subjects2.appendleft(tmp52)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp74 = subjects2.popleft()
                subjects75 = deque(tmp74._args)
                # State 97770
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 97771
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 97772
                        if len(subjects75) >= 1 and isinstance(subjects75[0], Pow):
                            tmp78 = subjects75.popleft()
                            subjects79 = deque(tmp78._args)
                            # State 97773
                            if len(subjects79) >= 1:
                                tmp80 = subjects79.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp80)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 97774
                                    if len(subjects79) >= 1:
                                        tmp82 = subjects79.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp82)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 97775
                                            if len(subjects79) == 0:
                                                pass
                                                # State 97776
                                                if len(subjects75) == 0:
                                                    pass
                                                    # State 97777
                                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                                        tmp84 = subjects2.popleft()
                                                        # State 97778
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 97779
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 25: 1/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                # 27: 1/sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                # 23: 1/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                        subjects2.appendleft(tmp84)
                                        subjects79.appendleft(tmp82)
                                subjects79.appendleft(tmp80)
                            subjects75.appendleft(tmp78)
                    if len(subjects75) >= 1 and isinstance(subjects75[0], Mul):
                        tmp85 = subjects75.popleft()
                        associative1 = tmp85
                        associative_type1 = type(tmp85)
                        subjects86 = deque(tmp85._args)
                        matcher = CommutativeMatcher97781.get()
                        tmp87 = subjects86
                        subjects86 = []
                        for s in tmp87:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp87, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 97786
                                if len(subjects75) == 0:
                                    pass
                                    # State 97787
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp88 = subjects2.popleft()
                                        # State 97788
                                        if len(subjects2) == 0:
                                            pass
                                            # State 97789
                                            if len(subjects) == 0:
                                                pass
                                                # 25: 1/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                # 27: 1/sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                # 23: 1/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                        subjects2.appendleft(tmp88)
                        subjects75.appendleft(tmp85)
                if len(subjects75) >= 1:
                    tmp89 = subjects75.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp89)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98280
                        if len(subjects75) == 0:
                            pass
                            # State 98281
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp91 = subjects2.popleft()
                                # State 98282
                                if len(subjects2) == 0:
                                    pass
                                    # State 98283
                                    if len(subjects) == 0:
                                        pass
                                        # 29: 1/sin(u) /; (cons_f825) and (cons_f826)
                                subjects2.appendleft(tmp91)
                    subjects75.appendleft(tmp89)
                if len(subjects75) >= 1 and isinstance(subjects75[0], Add):
                    tmp92 = subjects75.popleft()
                    associative1 = tmp92
                    associative_type1 = type(tmp92)
                    subjects93 = deque(tmp92._args)
                    matcher = CommutativeMatcher97791.get()
                    tmp94 = subjects93
                    subjects93 = []
                    for s in tmp94:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp94, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 97804
                            if len(subjects75) == 0:
                                pass
                                # State 97805
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp95 = subjects2.popleft()
                                    # State 97806
                                    if len(subjects2) == 0:
                                        pass
                                        # State 97807
                                        if len(subjects) == 0:
                                            pass
                                            # 25: 1/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                            # 27: 1/sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            # 23: 1/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                    subjects2.appendleft(tmp95)
                    subjects75.appendleft(tmp92)
                subjects2.appendleft(tmp74)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tanh):
                tmp96 = subjects2.popleft()
                subjects97 = deque(tmp96._args)
                # State 126870
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 126871
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 126872
                        if len(subjects97) >= 1 and isinstance(subjects97[0], Pow):
                            tmp100 = subjects97.popleft()
                            subjects101 = deque(tmp100._args)
                            # State 126873
                            if len(subjects101) >= 1:
                                tmp102 = subjects101.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp102)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 126874
                                    if len(subjects101) >= 1:
                                        tmp104 = subjects101.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp104)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 126875
                                            if len(subjects101) == 0:
                                                pass
                                                # State 126876
                                                if len(subjects97) == 0:
                                                    pass
                                                    # State 126877
                                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                                        tmp106 = subjects2.popleft()
                                                        # State 126878
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 126879
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 49: 1/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                # 51: 1/tanh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                # 47: 1/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                        subjects2.appendleft(tmp106)
                                        subjects101.appendleft(tmp104)
                                subjects101.appendleft(tmp102)
                            subjects97.appendleft(tmp100)
                    if len(subjects97) >= 1 and isinstance(subjects97[0], Mul):
                        tmp107 = subjects97.popleft()
                        associative1 = tmp107
                        associative_type1 = type(tmp107)
                        subjects108 = deque(tmp107._args)
                        matcher = CommutativeMatcher126881.get()
                        tmp109 = subjects108
                        subjects108 = []
                        for s in tmp109:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp109, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 126886
                                if len(subjects97) == 0:
                                    pass
                                    # State 126887
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp110 = subjects2.popleft()
                                        # State 126888
                                        if len(subjects2) == 0:
                                            pass
                                            # State 126889
                                            if len(subjects) == 0:
                                                pass
                                                # 49: 1/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                # 51: 1/tanh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                # 47: 1/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                        subjects2.appendleft(tmp110)
                        subjects97.appendleft(tmp107)
                if len(subjects97) >= 1:
                    tmp111 = subjects97.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp111)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 127380
                        if len(subjects97) == 0:
                            pass
                            # State 127381
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp113 = subjects2.popleft()
                                # State 127382
                                if len(subjects2) == 0:
                                    pass
                                    # State 127383
                                    if len(subjects) == 0:
                                        pass
                                        # 53: 1/tanh(u) /; (cons_f825) and (cons_f826)
                                subjects2.appendleft(tmp113)
                    subjects97.appendleft(tmp111)
                if len(subjects97) >= 1 and isinstance(subjects97[0], Add):
                    tmp114 = subjects97.popleft()
                    associative1 = tmp114
                    associative_type1 = type(tmp114)
                    subjects115 = deque(tmp114._args)
                    matcher = CommutativeMatcher126891.get()
                    tmp116 = subjects115
                    subjects115 = []
                    for s in tmp116:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp116, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 126904
                            if len(subjects97) == 0:
                                pass
                                # State 126905
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp117 = subjects2.popleft()
                                    # State 126906
                                    if len(subjects2) == 0:
                                        pass
                                        # State 126907
                                        if len(subjects) == 0:
                                            pass
                                            # 49: 1/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                            # 51: 1/tanh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            # 47: 1/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                    subjects2.appendleft(tmp117)
                    subjects97.appendleft(tmp114)
                subjects2.appendleft(tmp96)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cosh):
                tmp118 = subjects2.popleft()
                subjects119 = deque(tmp118._args)
                # State 129647
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 129648
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 129649
                        if len(subjects119) >= 1 and isinstance(subjects119[0], Pow):
                            tmp122 = subjects119.popleft()
                            subjects123 = deque(tmp122._args)
                            # State 129650
                            if len(subjects123) >= 1:
                                tmp124 = subjects123.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp124)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 129651
                                    if len(subjects123) >= 1:
                                        tmp126 = subjects123.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp126)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 129652
                                            if len(subjects123) == 0:
                                                pass
                                                # State 129653
                                                if len(subjects119) == 0:
                                                    pass
                                                    # State 129654
                                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                                        tmp128 = subjects2.popleft()
                                                        # State 129655
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 129656
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 56: 1/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                # 58: 1/cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                # 54: 1/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                        subjects2.appendleft(tmp128)
                                        subjects123.appendleft(tmp126)
                                subjects123.appendleft(tmp124)
                            subjects119.appendleft(tmp122)
                    if len(subjects119) >= 1 and isinstance(subjects119[0], Mul):
                        tmp129 = subjects119.popleft()
                        associative1 = tmp129
                        associative_type1 = type(tmp129)
                        subjects130 = deque(tmp129._args)
                        matcher = CommutativeMatcher129658.get()
                        tmp131 = subjects130
                        subjects130 = []
                        for s in tmp131:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp131, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 129663
                                if len(subjects119) == 0:
                                    pass
                                    # State 129664
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp132 = subjects2.popleft()
                                        # State 129665
                                        if len(subjects2) == 0:
                                            pass
                                            # State 129666
                                            if len(subjects) == 0:
                                                pass
                                                # 56: 1/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                # 58: 1/cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                # 54: 1/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                        subjects2.appendleft(tmp132)
                        subjects119.appendleft(tmp129)
                if len(subjects119) >= 1:
                    tmp133 = subjects119.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp133)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130473
                        if len(subjects119) == 0:
                            pass
                            # State 130474
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp135 = subjects2.popleft()
                                # State 130475
                                if len(subjects2) == 0:
                                    pass
                                    # State 130476
                                    if len(subjects) == 0:
                                        pass
                                        # 60: 1/cosh(u) /; (cons_f825) and (cons_f826)
                                subjects2.appendleft(tmp135)
                    subjects119.appendleft(tmp133)
                if len(subjects119) >= 1 and isinstance(subjects119[0], Add):
                    tmp136 = subjects119.popleft()
                    associative1 = tmp136
                    associative_type1 = type(tmp136)
                    subjects137 = deque(tmp136._args)
                    matcher = CommutativeMatcher129668.get()
                    tmp138 = subjects137
                    subjects137 = []
                    for s in tmp138:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp138, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 129681
                            if len(subjects119) == 0:
                                pass
                                # State 129682
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp139 = subjects2.popleft()
                                    # State 129683
                                    if len(subjects2) == 0:
                                        pass
                                        # State 129684
                                        if len(subjects) == 0:
                                            pass
                                            # 56: 1/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                            # 58: 1/cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            # 54: 1/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                    subjects2.appendleft(tmp139)
                    subjects119.appendleft(tmp136)
                subjects2.appendleft(tmp118)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sinh):
                tmp140 = subjects2.popleft()
                subjects141 = deque(tmp140._args)
                # State 129987
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 129988
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 129989
                        if len(subjects141) >= 1 and isinstance(subjects141[0], Pow):
                            tmp144 = subjects141.popleft()
                            subjects145 = deque(tmp144._args)
                            # State 129990
                            if len(subjects145) >= 1:
                                tmp146 = subjects145.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp146)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 129991
                                    if len(subjects145) >= 1:
                                        tmp148 = subjects145.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp148)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 129992
                                            if len(subjects145) == 0:
                                                pass
                                                # State 129993
                                                if len(subjects141) == 0:
                                                    pass
                                                    # State 129994
                                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                                        tmp150 = subjects2.popleft()
                                                        # State 129995
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 129996
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 57: 1/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                # 59: 1/sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                # 55: 1/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                        subjects2.appendleft(tmp150)
                                        subjects145.appendleft(tmp148)
                                subjects145.appendleft(tmp146)
                            subjects141.appendleft(tmp144)
                    if len(subjects141) >= 1 and isinstance(subjects141[0], Mul):
                        tmp151 = subjects141.popleft()
                        associative1 = tmp151
                        associative_type1 = type(tmp151)
                        subjects152 = deque(tmp151._args)
                        matcher = CommutativeMatcher129998.get()
                        tmp153 = subjects152
                        subjects152 = []
                        for s in tmp153:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp153, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 130003
                                if len(subjects141) == 0:
                                    pass
                                    # State 130004
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp154 = subjects2.popleft()
                                        # State 130005
                                        if len(subjects2) == 0:
                                            pass
                                            # State 130006
                                            if len(subjects) == 0:
                                                pass
                                                # 57: 1/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                # 59: 1/sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                # 55: 1/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                        subjects2.appendleft(tmp154)
                        subjects141.appendleft(tmp151)
                if len(subjects141) >= 1:
                    tmp155 = subjects141.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp155)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130529
                        if len(subjects141) == 0:
                            pass
                            # State 130530
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp157 = subjects2.popleft()
                                # State 130531
                                if len(subjects2) == 0:
                                    pass
                                    # State 130532
                                    if len(subjects) == 0:
                                        pass
                                        # 61: 1/sinh(u) /; (cons_f825) and (cons_f826)
                                subjects2.appendleft(tmp157)
                    subjects141.appendleft(tmp155)
                if len(subjects141) >= 1 and isinstance(subjects141[0], Add):
                    tmp158 = subjects141.popleft()
                    associative1 = tmp158
                    associative_type1 = type(tmp158)
                    subjects159 = deque(tmp158._args)
                    matcher = CommutativeMatcher130008.get()
                    tmp160 = subjects159
                    subjects159 = []
                    for s in tmp160:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp160, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 130021
                            if len(subjects141) == 0:
                                pass
                                # State 130022
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp161 = subjects2.popleft()
                                    # State 130023
                                    if len(subjects2) == 0:
                                        pass
                                        # State 130024
                                        if len(subjects) == 0:
                                            pass
                                            # 57: 1/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                            # 59: 1/sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            # 55: 1/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                    subjects2.appendleft(tmp161)
                    subjects141.appendleft(tmp158)
                subjects2.appendleft(tmp140)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp162 = subjects.popleft()
            subjects163 = deque(tmp162._args)
            # State 51711
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 51712
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 51713
                    if len(subjects163) >= 1 and isinstance(subjects163[0], Add):
                        tmp166 = subjects163.popleft()
                        associative1 = tmp166
                        associative_type1 = type(tmp166)
                        subjects167 = deque(tmp166._args)
                        matcher = CommutativeMatcher51715.get()
                        tmp168 = subjects167
                        subjects167 = []
                        for s in tmp168:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp168, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 51762
                                if len(subjects163) == 0:
                                    pass
                                    # State 51763
                                    if len(subjects) == 0:
                                        pass
                                        # 4: log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                        subjects163.appendleft(tmp166)
                    if len(subjects163) >= 1:
                        tmp169 = subjects163.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1', tmp169)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53099
                            if len(subjects163) == 0:
                                pass
                                # State 53100
                                if len(subjects) == 0:
                                    pass
                                    # 5: log(c*RFx**p) /; (cons_f8) and (cons_f5) and (cons_f1200)
                        subjects163.appendleft(tmp169)
                if len(subjects163) >= 1 and isinstance(subjects163[0], Pow):
                    tmp171 = subjects163.popleft()
                    subjects172 = deque(tmp171._args)
                    # State 51764
                    if len(subjects172) >= 1 and isinstance(subjects172[0], Add):
                        tmp173 = subjects172.popleft()
                        associative1 = tmp173
                        associative_type1 = type(tmp173)
                        subjects174 = deque(tmp173._args)
                        matcher = CommutativeMatcher51766.get()
                        tmp175 = subjects174
                        subjects174 = []
                        for s in tmp175:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp175, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 51813
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51814
                                    if len(subjects172) == 0:
                                        pass
                                        # State 51815
                                        if len(subjects163) == 0:
                                            pass
                                            # State 51816
                                            if len(subjects) == 0:
                                                pass
                                                # 4: log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                                if len(subjects172) >= 1:
                                    tmp177 = []
                                    tmp177.append(subjects172.popleft())
                                    while True:
                                        if len(tmp177) > 1:
                                            tmp178 = create_operation_expression(associative1, tmp177)
                                        elif len(tmp177) == 1:
                                            tmp178 = tmp177[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2.2', tmp178)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 51814
                                            if len(subjects172) == 0:
                                                pass
                                                # State 51815
                                                if len(subjects163) == 0:
                                                    pass
                                                    # State 51816
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                                        if len(subjects172) == 0:
                                            break
                                        tmp177.append(subjects172.popleft())
                                    subjects172.extendleft(reversed(tmp177))
                        subjects172.appendleft(tmp173)
                    if len(subjects172) >= 1:
                        tmp180 = subjects172.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.1', tmp180)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53101
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53102
                                if len(subjects172) == 0:
                                    pass
                                    # State 53103
                                    if len(subjects163) == 0:
                                        pass
                                        # State 53104
                                        if len(subjects) == 0:
                                            pass
                                            # 5: log(c*RFx**p) /; (cons_f8) and (cons_f5) and (cons_f1200)
                            if len(subjects172) >= 1:
                                tmp183 = subjects172.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', tmp183)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53102
                                    if len(subjects172) == 0:
                                        pass
                                        # State 53103
                                        if len(subjects163) == 0:
                                            pass
                                            # State 53104
                                            if len(subjects) == 0:
                                                pass
                                                # 5: log(c*RFx**p) /; (cons_f8) and (cons_f5) and (cons_f1200)
                                subjects172.appendleft(tmp183)
                        subjects172.appendleft(tmp180)
                    subjects163.appendleft(tmp171)
            if len(subjects163) >= 1 and isinstance(subjects163[0], Mul):
                tmp185 = subjects163.popleft()
                associative1 = tmp185
                associative_type1 = type(tmp185)
                subjects186 = deque(tmp185._args)
                matcher = CommutativeMatcher51818.get()
                tmp187 = subjects186
                subjects186 = []
                for s in tmp187:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp187, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 51921
                        if len(subjects163) == 0:
                            pass
                            # State 51922
                            if len(subjects) == 0:
                                pass
                                # 4: log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                    if pattern_index == 1:
                        pass
                        # State 53109
                        if len(subjects163) == 0:
                            pass
                            # State 53110
                            if len(subjects) == 0:
                                pass
                                # 5: log(c*RFx**p) /; (cons_f8) and (cons_f5) and (cons_f1200)
                subjects163.appendleft(tmp185)
            subjects.appendleft(tmp162)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp188 = subjects.popleft()
            subjects189 = deque(tmp188._args)
            # State 72945
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 72946
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 72947
                    if len(subjects189) >= 1 and isinstance(subjects189[0], Pow):
                        tmp192 = subjects189.popleft()
                        subjects193 = deque(tmp192._args)
                        # State 72948
                        if len(subjects193) >= 1:
                            tmp194 = subjects193.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp194)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 72949
                                if len(subjects193) >= 1:
                                    tmp196 = subjects193.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp196)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 72950
                                        if len(subjects193) == 0:
                                            pass
                                            # State 72951
                                            if len(subjects189) == 0:
                                                pass
                                                # State 72952
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                    # 10: sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    # 6: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    subjects193.appendleft(tmp196)
                            subjects193.appendleft(tmp194)
                        subjects189.appendleft(tmp192)
                if len(subjects189) >= 1 and isinstance(subjects189[0], Mul):
                    tmp198 = subjects189.popleft()
                    associative1 = tmp198
                    associative_type1 = type(tmp198)
                    subjects199 = deque(tmp198._args)
                    matcher = CommutativeMatcher72954.get()
                    tmp200 = subjects199
                    subjects199 = []
                    for s in tmp200:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp200, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 72959
                            if len(subjects189) == 0:
                                pass
                                # State 72960
                                if len(subjects) == 0:
                                    pass
                                    # 8: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    # 10: sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    # 6: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                    subjects189.appendleft(tmp198)
            if len(subjects189) >= 1:
                tmp201 = subjects189.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp201)
                except ValueError:
                    pass
                else:
                    pass
                    # State 73505
                    if len(subjects189) == 0:
                        pass
                        # State 73506
                        if len(subjects) == 0:
                            pass
                            # 12: sin(u) /; (cons_f825) and (cons_f826)
                subjects189.appendleft(tmp201)
            if len(subjects189) >= 1 and isinstance(subjects189[0], Add):
                tmp203 = subjects189.popleft()
                associative1 = tmp203
                associative_type1 = type(tmp203)
                subjects204 = deque(tmp203._args)
                matcher = CommutativeMatcher72962.get()
                tmp205 = subjects204
                subjects204 = []
                for s in tmp205:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp205, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 72975
                        if len(subjects189) == 0:
                            pass
                            # State 72976
                            if len(subjects) == 0:
                                pass
                                # 8: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                # 10: sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                # 6: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                subjects189.appendleft(tmp203)
            subjects.appendleft(tmp188)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp206 = subjects.popleft()
            subjects207 = deque(tmp206._args)
            # State 73112
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 73113
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 73114
                    if len(subjects207) >= 1 and isinstance(subjects207[0], Pow):
                        tmp210 = subjects207.popleft()
                        subjects211 = deque(tmp210._args)
                        # State 73115
                        if len(subjects211) >= 1:
                            tmp212 = subjects211.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp212)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 73116
                                if len(subjects211) >= 1:
                                    tmp214 = subjects211.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp214)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 73117
                                        if len(subjects211) == 0:
                                            pass
                                            # State 73118
                                            if len(subjects207) == 0:
                                                pass
                                                # State 73119
                                                if len(subjects) == 0:
                                                    pass
                                                    # 9: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                    # 11: cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    # 7: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    subjects211.appendleft(tmp214)
                            subjects211.appendleft(tmp212)
                        subjects207.appendleft(tmp210)
                if len(subjects207) >= 1 and isinstance(subjects207[0], Mul):
                    tmp216 = subjects207.popleft()
                    associative1 = tmp216
                    associative_type1 = type(tmp216)
                    subjects217 = deque(tmp216._args)
                    matcher = CommutativeMatcher73121.get()
                    tmp218 = subjects217
                    subjects217 = []
                    for s in tmp218:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp218, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 73126
                            if len(subjects207) == 0:
                                pass
                                # State 73127
                                if len(subjects) == 0:
                                    pass
                                    # 9: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    # 11: cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    # 7: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                    subjects207.appendleft(tmp216)
            if len(subjects207) >= 1:
                tmp219 = subjects207.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp219)
                except ValueError:
                    pass
                else:
                    pass
                    # State 73545
                    if len(subjects207) == 0:
                        pass
                        # State 73546
                        if len(subjects) == 0:
                            pass
                            # 13: cos(u) /; (cons_f825) and (cons_f826)
                subjects207.appendleft(tmp219)
            if len(subjects207) >= 1 and isinstance(subjects207[0], Add):
                tmp221 = subjects207.popleft()
                associative1 = tmp221
                associative_type1 = type(tmp221)
                subjects222 = deque(tmp221._args)
                matcher = CommutativeMatcher73129.get()
                tmp223 = subjects222
                subjects222 = []
                for s in tmp223:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp223, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 73142
                        if len(subjects207) == 0:
                            pass
                            # State 73143
                            if len(subjects) == 0:
                                pass
                                # 9: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                # 11: cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                # 7: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                subjects207.appendleft(tmp221)
            subjects.appendleft(tmp206)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp224 = subjects.popleft()
            subjects225 = deque(tmp224._args)
            # State 87125
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 87126
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 87127
                    if len(subjects225) >= 1 and isinstance(subjects225[0], Pow):
                        tmp228 = subjects225.popleft()
                        subjects229 = deque(tmp228._args)
                        # State 87128
                        if len(subjects229) >= 1:
                            tmp230 = subjects229.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp230)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 87129
                                if len(subjects229) >= 1:
                                    tmp232 = subjects229.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp232)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 87130
                                        if len(subjects229) == 0:
                                            pass
                                            # State 87131
                                            if len(subjects225) == 0:
                                                pass
                                                # State 87132
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    # 18: tan(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    # 14: tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                    subjects229.appendleft(tmp232)
                            subjects229.appendleft(tmp230)
                        subjects225.appendleft(tmp228)
                if len(subjects225) >= 1 and isinstance(subjects225[0], Mul):
                    tmp234 = subjects225.popleft()
                    associative1 = tmp234
                    associative_type1 = type(tmp234)
                    subjects235 = deque(tmp234._args)
                    matcher = CommutativeMatcher87134.get()
                    tmp236 = subjects235
                    subjects235 = []
                    for s in tmp236:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp236, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 87139
                            if len(subjects225) == 0:
                                pass
                                # State 87140
                                if len(subjects) == 0:
                                    pass
                                    # 16: tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                    # 18: tan(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    # 14: tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                    subjects225.appendleft(tmp234)
            if len(subjects225) >= 1:
                tmp237 = subjects225.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp237)
                except ValueError:
                    pass
                else:
                    pass
                    # State 87843
                    if len(subjects225) == 0:
                        pass
                        # State 87844
                        if len(subjects) == 0:
                            pass
                            # 20: tan(u) /; (cons_f825) and (cons_f826)
                subjects225.appendleft(tmp237)
            if len(subjects225) >= 1 and isinstance(subjects225[0], Add):
                tmp239 = subjects225.popleft()
                associative1 = tmp239
                associative_type1 = type(tmp239)
                subjects240 = deque(tmp239._args)
                matcher = CommutativeMatcher87142.get()
                tmp241 = subjects240
                subjects240 = []
                for s in tmp241:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp241, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 87155
                        if len(subjects225) == 0:
                            pass
                            # State 87156
                            if len(subjects) == 0:
                                pass
                                # 16: tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                # 18: tan(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                # 14: tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                subjects225.appendleft(tmp239)
            subjects.appendleft(tmp224)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp242 = subjects.popleft()
            subjects243 = deque(tmp242._args)
            # State 107967
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 107968
                if len(subjects243) >= 1:
                    tmp245 = subjects243.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp245)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 107969
                        if len(subjects243) == 0:
                            pass
                            # State 107970
                            if len(subjects) == 0:
                                pass
                                # 30: asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects243.appendleft(tmp245)
            if len(subjects243) >= 1 and isinstance(subjects243[0], Mul):
                tmp247 = subjects243.popleft()
                associative1 = tmp247
                associative_type1 = type(tmp247)
                subjects248 = deque(tmp247._args)
                matcher = CommutativeMatcher107972.get()
                tmp249 = subjects248
                subjects248 = []
                for s in tmp249:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp249, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 107973
                        if len(subjects243) == 0:
                            pass
                            # State 107974
                            if len(subjects) == 0:
                                pass
                                # 30: asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                subjects243.appendleft(tmp247)
            if len(subjects243) >= 1 and isinstance(subjects243[0], Add):
                tmp250 = subjects243.popleft()
                associative1 = tmp250
                associative_type1 = type(tmp250)
                subjects251 = deque(tmp250._args)
                matcher = CommutativeMatcher110266.get()
                tmp252 = subjects251
                subjects251 = []
                for s in tmp252:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp252, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110272
                        if len(subjects243) == 0:
                            pass
                            # State 110273
                            if len(subjects) == 0:
                                pass
                                # 32: asin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                subjects243.appendleft(tmp250)
            subjects.appendleft(tmp242)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp253 = subjects.popleft()
            subjects254 = deque(tmp253._args)
            # State 108061
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108062
                if len(subjects254) >= 1:
                    tmp256 = subjects254.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp256)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108063
                        if len(subjects254) == 0:
                            pass
                            # State 108064
                            if len(subjects) == 0:
                                pass
                                # 31: acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects254.appendleft(tmp256)
            if len(subjects254) >= 1 and isinstance(subjects254[0], Mul):
                tmp258 = subjects254.popleft()
                associative1 = tmp258
                associative_type1 = type(tmp258)
                subjects259 = deque(tmp258._args)
                matcher = CommutativeMatcher108066.get()
                tmp260 = subjects259
                subjects259 = []
                for s in tmp260:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp260, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108067
                        if len(subjects254) == 0:
                            pass
                            # State 108068
                            if len(subjects) == 0:
                                pass
                                # 31: acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                subjects254.appendleft(tmp258)
            if len(subjects254) >= 1 and isinstance(subjects254[0], Add):
                tmp261 = subjects254.popleft()
                associative1 = tmp261
                associative_type1 = type(tmp261)
                subjects262 = deque(tmp261._args)
                matcher = CommutativeMatcher110362.get()
                tmp263 = subjects262
                subjects262 = []
                for s in tmp263:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp263, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110368
                        if len(subjects254) == 0:
                            pass
                            # State 110369
                            if len(subjects) == 0:
                                pass
                                # 33: acos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                subjects254.appendleft(tmp261)
            subjects.appendleft(tmp253)
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp264 = subjects.popleft()
            subjects265 = deque(tmp264._args)
            # State 112602
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 112603
                if len(subjects265) >= 1:
                    tmp267 = subjects265.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp267)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112604
                        if len(subjects265) == 0:
                            pass
                            # State 112605
                            if len(subjects) == 0:
                                pass
                                # 34: atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects265.appendleft(tmp267)
            if len(subjects265) >= 1 and isinstance(subjects265[0], Mul):
                tmp269 = subjects265.popleft()
                associative1 = tmp269
                associative_type1 = type(tmp269)
                subjects270 = deque(tmp269._args)
                matcher = CommutativeMatcher112607.get()
                tmp271 = subjects270
                subjects270 = []
                for s in tmp271:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp271, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 112608
                        if len(subjects265) == 0:
                            pass
                            # State 112609
                            if len(subjects) == 0:
                                pass
                                # 34: atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                subjects265.appendleft(tmp269)
            if len(subjects265) >= 1 and isinstance(subjects265[0], Add):
                tmp272 = subjects265.popleft()
                associative1 = tmp272
                associative_type1 = type(tmp272)
                subjects273 = deque(tmp272._args)
                matcher = CommutativeMatcher115464.get()
                tmp274 = subjects273
                subjects273 = []
                for s in tmp274:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp274, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115470
                        if len(subjects265) == 0:
                            pass
                            # State 115471
                            if len(subjects) == 0:
                                pass
                                # 36: atan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                subjects265.appendleft(tmp272)
            subjects.appendleft(tmp264)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp275 = subjects.popleft()
            subjects276 = deque(tmp275._args)
            # State 112696
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 112697
                if len(subjects276) >= 1:
                    tmp278 = subjects276.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp278)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112698
                        if len(subjects276) == 0:
                            pass
                            # State 112699
                            if len(subjects) == 0:
                                pass
                                # 35: acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects276.appendleft(tmp278)
            if len(subjects276) >= 1 and isinstance(subjects276[0], Mul):
                tmp280 = subjects276.popleft()
                associative1 = tmp280
                associative_type1 = type(tmp280)
                subjects281 = deque(tmp280._args)
                matcher = CommutativeMatcher112701.get()
                tmp282 = subjects281
                subjects281 = []
                for s in tmp282:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp282, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 112702
                        if len(subjects276) == 0:
                            pass
                            # State 112703
                            if len(subjects) == 0:
                                pass
                                # 35: acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                subjects276.appendleft(tmp280)
            if len(subjects276) >= 1 and isinstance(subjects276[0], Add):
                tmp283 = subjects276.popleft()
                associative1 = tmp283
                associative_type1 = type(tmp283)
                subjects284 = deque(tmp283._args)
                matcher = CommutativeMatcher115560.get()
                tmp285 = subjects284
                subjects284 = []
                for s in tmp285:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp285, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115566
                        if len(subjects276) == 0:
                            pass
                            # State 115567
                            if len(subjects) == 0:
                                pass
                                # 37: acot(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                subjects276.appendleft(tmp283)
            subjects.appendleft(tmp275)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp286 = subjects.popleft()
            subjects287 = deque(tmp286._args)
            # State 122806
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 122807
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122808
                    if len(subjects287) >= 1 and isinstance(subjects287[0], Pow):
                        tmp290 = subjects287.popleft()
                        subjects291 = deque(tmp290._args)
                        # State 122809
                        if len(subjects291) >= 1:
                            tmp292 = subjects291.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp292)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 122810
                                if len(subjects291) >= 1:
                                    tmp294 = subjects291.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp294)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 122811
                                        if len(subjects291) == 0:
                                            pass
                                            # State 122812
                                            if len(subjects287) == 0:
                                                pass
                                                # State 122813
                                                if len(subjects) == 0:
                                                    pass
                                                    # 40: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                    # 42: sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    # 38: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    subjects291.appendleft(tmp294)
                            subjects291.appendleft(tmp292)
                        subjects287.appendleft(tmp290)
                if len(subjects287) >= 1 and isinstance(subjects287[0], Mul):
                    tmp296 = subjects287.popleft()
                    associative1 = tmp296
                    associative_type1 = type(tmp296)
                    subjects297 = deque(tmp296._args)
                    matcher = CommutativeMatcher122815.get()
                    tmp298 = subjects297
                    subjects297 = []
                    for s in tmp298:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp298, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122820
                            if len(subjects287) == 0:
                                pass
                                # State 122821
                                if len(subjects) == 0:
                                    pass
                                    # 40: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    # 42: sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    # 38: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                    subjects287.appendleft(tmp296)
            if len(subjects287) >= 1:
                tmp299 = subjects287.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp299)
                except ValueError:
                    pass
                else:
                    pass
                    # State 123366
                    if len(subjects287) == 0:
                        pass
                        # State 123367
                        if len(subjects) == 0:
                            pass
                            # 44: sinh(u) /; (cons_f825) and (cons_f826)
                subjects287.appendleft(tmp299)
            if len(subjects287) >= 1 and isinstance(subjects287[0], Add):
                tmp301 = subjects287.popleft()
                associative1 = tmp301
                associative_type1 = type(tmp301)
                subjects302 = deque(tmp301._args)
                matcher = CommutativeMatcher122823.get()
                tmp303 = subjects302
                subjects302 = []
                for s in tmp303:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp303, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 122836
                        if len(subjects287) == 0:
                            pass
                            # State 122837
                            if len(subjects) == 0:
                                pass
                                # 40: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                # 42: sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                # 38: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                subjects287.appendleft(tmp301)
            subjects.appendleft(tmp286)
        if len(subjects) >= 1 and isinstance(subjects[0], cosh):
            tmp304 = subjects.popleft()
            subjects305 = deque(tmp304._args)
            # State 122973
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 122974
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122975
                    if len(subjects305) >= 1 and isinstance(subjects305[0], Pow):
                        tmp308 = subjects305.popleft()
                        subjects309 = deque(tmp308._args)
                        # State 122976
                        if len(subjects309) >= 1:
                            tmp310 = subjects309.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp310)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 122977
                                if len(subjects309) >= 1:
                                    tmp312 = subjects309.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp312)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 122978
                                        if len(subjects309) == 0:
                                            pass
                                            # State 122979
                                            if len(subjects305) == 0:
                                                pass
                                                # State 122980
                                                if len(subjects) == 0:
                                                    pass
                                                    # 41: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                    # 43: cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    # 39: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    subjects309.appendleft(tmp312)
                            subjects309.appendleft(tmp310)
                        subjects305.appendleft(tmp308)
                if len(subjects305) >= 1 and isinstance(subjects305[0], Mul):
                    tmp314 = subjects305.popleft()
                    associative1 = tmp314
                    associative_type1 = type(tmp314)
                    subjects315 = deque(tmp314._args)
                    matcher = CommutativeMatcher122982.get()
                    tmp316 = subjects315
                    subjects315 = []
                    for s in tmp316:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp316, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122987
                            if len(subjects305) == 0:
                                pass
                                # State 122988
                                if len(subjects) == 0:
                                    pass
                                    # 41: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    # 43: cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    # 39: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                    subjects305.appendleft(tmp314)
            if len(subjects305) >= 1:
                tmp317 = subjects305.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp317)
                except ValueError:
                    pass
                else:
                    pass
                    # State 123406
                    if len(subjects305) == 0:
                        pass
                        # State 123407
                        if len(subjects) == 0:
                            pass
                            # 45: cosh(u) /; (cons_f825) and (cons_f826)
                subjects305.appendleft(tmp317)
            if len(subjects305) >= 1 and isinstance(subjects305[0], Add):
                tmp319 = subjects305.popleft()
                associative1 = tmp319
                associative_type1 = type(tmp319)
                subjects320 = deque(tmp319._args)
                matcher = CommutativeMatcher122990.get()
                tmp321 = subjects320
                subjects320 = []
                for s in tmp321:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp321, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 123003
                        if len(subjects305) == 0:
                            pass
                            # State 123004
                            if len(subjects) == 0:
                                pass
                                # 41: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                # 43: cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                # 39: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                subjects305.appendleft(tmp319)
            subjects.appendleft(tmp304)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp322 = subjects.popleft()
            subjects323 = deque(tmp322._args)
            # State 126572
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 126573
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 126574
                    if len(subjects323) >= 1 and isinstance(subjects323[0], Pow):
                        tmp326 = subjects323.popleft()
                        subjects327 = deque(tmp326._args)
                        # State 126575
                        if len(subjects327) >= 1:
                            tmp328 = subjects327.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp328)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 126576
                                if len(subjects327) >= 1:
                                    tmp330 = subjects327.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp330)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 126577
                                        if len(subjects327) == 0:
                                            pass
                                            # State 126578
                                            if len(subjects323) == 0:
                                                pass
                                                # State 126579
                                                if len(subjects) == 0:
                                                    pass
                                                    # 48: tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    # 50: tanh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    # 46: tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                    subjects327.appendleft(tmp330)
                            subjects327.appendleft(tmp328)
                        subjects323.appendleft(tmp326)
                if len(subjects323) >= 1 and isinstance(subjects323[0], Mul):
                    tmp332 = subjects323.popleft()
                    associative1 = tmp332
                    associative_type1 = type(tmp332)
                    subjects333 = deque(tmp332._args)
                    matcher = CommutativeMatcher126581.get()
                    tmp334 = subjects333
                    subjects333 = []
                    for s in tmp334:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp334, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 126586
                            if len(subjects323) == 0:
                                pass
                                # State 126587
                                if len(subjects) == 0:
                                    pass
                                    # 48: tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                    # 50: tanh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    # 46: tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                    subjects323.appendleft(tmp332)
            if len(subjects323) >= 1:
                tmp335 = subjects323.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp335)
                except ValueError:
                    pass
                else:
                    pass
                    # State 127338
                    if len(subjects323) == 0:
                        pass
                        # State 127339
                        if len(subjects) == 0:
                            pass
                            # 52: tanh(u) /; (cons_f825) and (cons_f826)
                subjects323.appendleft(tmp335)
            if len(subjects323) >= 1 and isinstance(subjects323[0], Add):
                tmp337 = subjects323.popleft()
                associative1 = tmp337
                associative_type1 = type(tmp337)
                subjects338 = deque(tmp337._args)
                matcher = CommutativeMatcher126589.get()
                tmp339 = subjects338
                subjects338 = []
                for s in tmp339:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp339, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 126602
                        if len(subjects323) == 0:
                            pass
                            # State 126603
                            if len(subjects) == 0:
                                pass
                                # 48: tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                # 50: tanh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                # 46: tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                subjects323.appendleft(tmp337)
            subjects.appendleft(tmp322)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp340 = subjects.popleft()
            subjects341 = deque(tmp340._args)
            # State 137706
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 137707
                if len(subjects341) >= 1:
                    tmp343 = subjects341.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp343)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137708
                        if len(subjects341) == 0:
                            pass
                            # State 137709
                            if len(subjects) == 0:
                                pass
                                # 62: asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects341.appendleft(tmp343)
            if len(subjects341) >= 1 and isinstance(subjects341[0], Mul):
                tmp345 = subjects341.popleft()
                associative1 = tmp345
                associative_type1 = type(tmp345)
                subjects346 = deque(tmp345._args)
                matcher = CommutativeMatcher137711.get()
                tmp347 = subjects346
                subjects346 = []
                for s in tmp347:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp347, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 137712
                        if len(subjects341) == 0:
                            pass
                            # State 137713
                            if len(subjects) == 0:
                                pass
                                # 62: asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                subjects341.appendleft(tmp345)
            if len(subjects341) >= 1 and isinstance(subjects341[0], Add):
                tmp348 = subjects341.popleft()
                associative1 = tmp348
                associative_type1 = type(tmp348)
                subjects349 = deque(tmp348._args)
                matcher = CommutativeMatcher140001.get()
                tmp350 = subjects349
                subjects349 = []
                for s in tmp350:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp350, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 140007
                        if len(subjects341) == 0:
                            pass
                            # State 140008
                            if len(subjects) == 0:
                                pass
                                # 64: asinh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                subjects341.appendleft(tmp348)
            subjects.appendleft(tmp340)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp351 = subjects.popleft()
            subjects352 = deque(tmp351._args)
            # State 137800
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 137801
                if len(subjects352) >= 1:
                    tmp354 = subjects352.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp354)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137802
                        if len(subjects352) == 0:
                            pass
                            # State 137803
                            if len(subjects) == 0:
                                pass
                                # 63: acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects352.appendleft(tmp354)
            if len(subjects352) >= 1 and isinstance(subjects352[0], Mul):
                tmp356 = subjects352.popleft()
                associative1 = tmp356
                associative_type1 = type(tmp356)
                subjects357 = deque(tmp356._args)
                matcher = CommutativeMatcher137805.get()
                tmp358 = subjects357
                subjects357 = []
                for s in tmp358:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp358, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 137806
                        if len(subjects352) == 0:
                            pass
                            # State 137807
                            if len(subjects) == 0:
                                pass
                                # 63: acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                subjects352.appendleft(tmp356)
            if len(subjects352) >= 1 and isinstance(subjects352[0], Add):
                tmp359 = subjects352.popleft()
                associative1 = tmp359
                associative_type1 = type(tmp359)
                subjects360 = deque(tmp359._args)
                matcher = CommutativeMatcher140097.get()
                tmp361 = subjects360
                subjects360 = []
                for s in tmp361:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp361, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 140103
                        if len(subjects352) == 0:
                            pass
                            # State 140104
                            if len(subjects) == 0:
                                pass
                                # 65: acosh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                subjects352.appendleft(tmp359)
            subjects.appendleft(tmp351)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp362 = subjects.popleft()
            subjects363 = deque(tmp362._args)
            # State 142234
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142235
                if len(subjects363) >= 1:
                    tmp365 = subjects363.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp365)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142236
                        if len(subjects363) == 0:
                            pass
                            # State 142237
                            if len(subjects) == 0:
                                pass
                                # 66: atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects363.appendleft(tmp365)
            if len(subjects363) >= 1 and isinstance(subjects363[0], Mul):
                tmp367 = subjects363.popleft()
                associative1 = tmp367
                associative_type1 = type(tmp367)
                subjects368 = deque(tmp367._args)
                matcher = CommutativeMatcher142239.get()
                tmp369 = subjects368
                subjects368 = []
                for s in tmp369:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp369, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142240
                        if len(subjects363) == 0:
                            pass
                            # State 142241
                            if len(subjects) == 0:
                                pass
                                # 66: atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                subjects363.appendleft(tmp367)
            if len(subjects363) >= 1 and isinstance(subjects363[0], Add):
                tmp370 = subjects363.popleft()
                associative1 = tmp370
                associative_type1 = type(tmp370)
                subjects371 = deque(tmp370._args)
                matcher = CommutativeMatcher144689.get()
                tmp372 = subjects371
                subjects371 = []
                for s in tmp372:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp372, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144695
                        if len(subjects363) == 0:
                            pass
                            # State 144696
                            if len(subjects) == 0:
                                pass
                                # 68: atanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                subjects363.appendleft(tmp370)
            subjects.appendleft(tmp362)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp373 = subjects.popleft()
            subjects374 = deque(tmp373._args)
            # State 142328
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142329
                if len(subjects374) >= 1:
                    tmp376 = subjects374.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp376)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142330
                        if len(subjects374) == 0:
                            pass
                            # State 142331
                            if len(subjects) == 0:
                                pass
                                # 67: acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects374.appendleft(tmp376)
            if len(subjects374) >= 1 and isinstance(subjects374[0], Mul):
                tmp378 = subjects374.popleft()
                associative1 = tmp378
                associative_type1 = type(tmp378)
                subjects379 = deque(tmp378._args)
                matcher = CommutativeMatcher142333.get()
                tmp380 = subjects379
                subjects379 = []
                for s in tmp380:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp380, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142334
                        if len(subjects374) == 0:
                            pass
                            # State 142335
                            if len(subjects) == 0:
                                pass
                                # 67: acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                subjects374.appendleft(tmp378)
            if len(subjects374) >= 1 and isinstance(subjects374[0], Add):
                tmp381 = subjects374.popleft()
                associative1 = tmp381
                associative_type1 = type(tmp381)
                subjects382 = deque(tmp381._args)
                matcher = CommutativeMatcher144785.get()
                tmp383 = subjects382
                subjects382 = []
                for s in tmp383:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp383, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144791
                        if len(subjects374) == 0:
                            pass
                            # State 144792
                            if len(subjects) == 0:
                                pass
                                # 69: acoth(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                subjects374.appendleft(tmp381)
            subjects.appendleft(tmp373)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
