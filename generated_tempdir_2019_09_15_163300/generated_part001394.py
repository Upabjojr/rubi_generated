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


class CommutativeMatcher8149(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
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
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({13: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({14: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
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
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({21: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({22: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
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
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({29: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({30: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher8149._instance is None:
            CommutativeMatcher8149._instance = CommutativeMatcher8149()
        return CommutativeMatcher8149._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 8148
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 8150
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 8151
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8152
                            if len(subjects2) == 0:
                                pass
                                # State 8153
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8164
                        if len(subjects2) == 0:
                            pass
                            # State 8165
                            if len(subjects) == 0:
                                pass
                                # 1: x**n2
                                yield 1, subst2
                    if len(subjects2) >= 1:
                        tmp8 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2_1', tmp8)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8164
                            if len(subjects2) == 0:
                                pass
                                # State 8165
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n2
                                    yield 1, subst2
                        subjects2.appendleft(tmp8)
                subjects2.appendleft(tmp3)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10016
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp11 = subjects2.popleft()
                    subjects12 = deque(tmp11._args)
                    # State 10017
                    if len(subjects12) >= 1:
                        tmp13 = subjects12.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.1', tmp13)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10018
                            if len(subjects12) >= 1:
                                tmp15 = subjects12.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', tmp15)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10019
                                    if len(subjects12) == 0:
                                        pass
                                        # State 10020
                                        if len(subjects2) >= 1:
                                            tmp17 = subjects2.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2', tmp17)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 10021
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 10022
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: (c*x**n)**q
                                                        yield 2, subst4
                                            subjects2.appendleft(tmp17)
                                subjects12.appendleft(tmp15)
                            if len(subjects12) >= 1 and subjects12[0] == Integer(-1):
                                tmp19 = subjects12.popleft()
                                # State 10877
                                if len(subjects12) == 0:
                                    pass
                                    # State 10878
                                    if len(subjects2) >= 1:
                                        tmp20 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2', tmp20)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 10879
                                            if len(subjects2) == 0:
                                                pass
                                                # State 10880
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (c/x)**n
                                                    yield 3, subst3
                                        subjects2.appendleft(tmp20)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 10927
                                        if len(subjects2) == 0:
                                            pass
                                            # State 10928
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (c/x)**n2
                                                yield 4, subst3
                                    if len(subjects2) >= 1:
                                        tmp23 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2_1', tmp23)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 10927
                                            if len(subjects2) == 0:
                                                pass
                                                # State 10928
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (c/x)**n2
                                                    yield 4, subst3
                                        subjects2.appendleft(tmp23)
                                subjects12.appendleft(tmp19)
                        subjects12.appendleft(tmp13)
                    subjects2.appendleft(tmp11)
            if len(subjects2) >= 1:
                tmp25 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.2.1', tmp25)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11169
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11170
                        if len(subjects2) == 0:
                            pass
                            # State 11171
                            if len(subjects) == 0:
                                pass
                                # 5: x**n2
                                yield 5, subst2
                    if len(subjects2) >= 1:
                        tmp28 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2_1', tmp28)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11170
                            if len(subjects2) == 0:
                                pass
                                # State 11171
                                if len(subjects) == 0:
                                    pass
                                    # 5: x**n2
                                    yield 5, subst2
                        subjects2.appendleft(tmp28)
                subjects2.appendleft(tmp25)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp30 = subjects2.popleft()
                associative1 = tmp30
                associative_type1 = type(tmp30)
                subjects31 = deque(tmp30._args)
                matcher = CommutativeMatcher10024.get()
                tmp32 = subjects31
                subjects31 = []
                for s in tmp32:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp32, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10029
                        if len(subjects2) >= 1:
                            tmp33 = []
                            tmp33.append(subjects2.popleft())
                            while True:
                                if len(tmp33) > 1:
                                    tmp34 = create_operation_expression(associative1, tmp33)
                                elif len(tmp33) == 1:
                                    tmp34 = tmp33[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp34)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10030
                                    if len(subjects2) == 0:
                                        pass
                                        # State 10031
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (c*x**n)**q
                                            yield 2, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp33.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp33))
                    if pattern_index == 1:
                        pass
                        # State 10883
                        if len(subjects2) >= 1:
                            tmp36 = []
                            tmp36.append(subjects2.popleft())
                            while True:
                                if len(tmp36) > 1:
                                    tmp37 = create_operation_expression(associative1, tmp36)
                                elif len(tmp36) == 1:
                                    tmp37 = tmp36[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp37)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10884
                                    if len(subjects2) == 0:
                                        pass
                                        # State 10885
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (c/x)**n
                                            yield 3, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp36.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp36))
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10929
                            if len(subjects2) == 0:
                                pass
                                # State 10930
                                if len(subjects) == 0:
                                    pass
                                    # 4: (c/x)**n2
                                    yield 4, subst2
                        if len(subjects2) >= 1:
                            tmp40 = []
                            tmp40.append(subjects2.popleft())
                            while True:
                                if len(tmp40) > 1:
                                    tmp41 = create_operation_expression(associative1, tmp40)
                                elif len(tmp40) == 1:
                                    tmp41 = tmp40[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2_1', tmp41)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10929
                                    if len(subjects2) == 0:
                                        pass
                                        # State 10930
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (c/x)**n2
                                            yield 4, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp40.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp40))
                subjects2.appendleft(tmp30)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp43 = subjects2.popleft()
                associative1 = tmp43
                associative_type1 = type(tmp43)
                subjects44 = deque(tmp43._args)
                matcher = CommutativeMatcher13280.get()
                tmp45 = subjects44
                subjects44 = []
                for s in tmp45:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp45, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 13330
                        if len(subjects2) >= 1:
                            tmp46 = []
                            tmp46.append(subjects2.popleft())
                            while True:
                                if len(tmp46) > 1:
                                    tmp47 = create_operation_expression(associative1, tmp46)
                                elif len(tmp46) == 1:
                                    tmp47 = tmp46[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp47)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 13331
                                    if len(subjects2) == 0:
                                        pass
                                        # State 13332
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d + e*x + f*sqrt(a + b*x + c*x**2))**n
                                            yield 6, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp46.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp46))
                    if pattern_index == 1:
                        pass
                        # State 13610
                        if len(subjects2) >= 1:
                            tmp49 = []
                            tmp49.append(subjects2.popleft())
                            while True:
                                if len(tmp49) > 1:
                                    tmp50 = create_operation_expression(associative1, tmp49)
                                elif len(tmp49) == 1:
                                    tmp50 = tmp49[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp50)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 13611
                                    if len(subjects2) == 0:
                                        pass
                                        # State 13612
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d + e*x + f*sqrt(a + c*x**2))**n
                                            yield 7, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp49.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp49))
                    if pattern_index == 2:
                        pass
                        # State 13714
                        if len(subjects2) >= 1:
                            tmp52 = []
                            tmp52.append(subjects2.popleft())
                            while True:
                                if len(tmp52) > 1:
                                    tmp53 = create_operation_expression(associative1, tmp52)
                                elif len(tmp52) == 1:
                                    tmp53 = tmp52[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp53)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 13715
                                    if len(subjects2) == 0:
                                        pass
                                        # State 13716
                                        if len(subjects) == 0:
                                            pass
                                            # 8: (u + f*sqrt(v))**n
                                            yield 8, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp52.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp52))
                subjects2.appendleft(tmp43)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp55 = subjects2.popleft()
                subjects56 = deque(tmp55._args)
                # State 68795
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68796
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 68797
                        if len(subjects56) >= 1:
                            tmp59 = subjects56.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.3.1.0', tmp59)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 68798
                                if len(subjects56) == 0:
                                    pass
                                    # State 68799
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 68800
                                        if len(subjects2) == 0:
                                            pass
                                            # State 68801
                                            if len(subjects) == 0:
                                                pass
                                                # 11: sin(d + x*e)**n
                                                yield 11, subst4
                                    if len(subjects2) >= 1:
                                        tmp62 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', tmp62)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68800
                                            if len(subjects2) == 0:
                                                pass
                                                # State 68801
                                                if len(subjects) == 0:
                                                    pass
                                                    # 11: sin(d + x*e)**n
                                                    yield 11, subst4
                                        subjects2.appendleft(tmp62)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 68882
                                        if len(subjects2) == 0:
                                            pass
                                            # State 68883
                                            if len(subjects) == 0:
                                                pass
                                                # 12: sin(d + x*e)**n2
                                                yield 12, subst4
                                    if len(subjects2) >= 1:
                                        tmp65 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3_1', tmp65)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68882
                                            if len(subjects2) == 0:
                                                pass
                                                # State 68883
                                                if len(subjects) == 0:
                                                    pass
                                                    # 12: sin(d + x*e)**n2
                                                    yield 12, subst4
                                        subjects2.appendleft(tmp65)
                            subjects56.appendleft(tmp59)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 97841
                        if len(subjects56) >= 1 and isinstance(subjects56[0], Pow):
                            tmp68 = subjects56.popleft()
                            subjects69 = deque(tmp68._args)
                            # State 97842
                            if len(subjects69) >= 1:
                                tmp70 = subjects69.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp70)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 97843
                                    if len(subjects69) >= 1:
                                        tmp72 = subjects69.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp72)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 97844
                                            if len(subjects69) == 0:
                                                pass
                                                # State 97845
                                                if len(subjects56) == 0:
                                                    pass
                                                    # State 97846
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp74 = subjects2.popleft()
                                                        # State 97847
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 97848
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 32: 1/sin(c + d*x**n)
                                                                yield 32, subst4
                                                        subjects2.appendleft(tmp74)
                                        subjects69.appendleft(tmp72)
                                subjects69.appendleft(tmp70)
                            subjects56.appendleft(tmp68)
                    if len(subjects56) >= 1 and isinstance(subjects56[0], Mul):
                        tmp75 = subjects56.popleft()
                        associative1 = tmp75
                        associative_type1 = type(tmp75)
                        subjects76 = deque(tmp75._args)
                        matcher = CommutativeMatcher68803.get()
                        tmp77 = subjects76
                        subjects76 = []
                        for s in tmp77:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp77, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 68804
                                if len(subjects56) == 0:
                                    pass
                                    # State 68805
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 68806
                                        if len(subjects2) == 0:
                                            pass
                                            # State 68807
                                            if len(subjects) == 0:
                                                pass
                                                # 11: sin(d + x*e)**n
                                                yield 11, subst3
                                    if len(subjects2) >= 1:
                                        tmp79 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp79)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68806
                                            if len(subjects2) == 0:
                                                pass
                                                # State 68807
                                                if len(subjects) == 0:
                                                    pass
                                                    # 11: sin(d + x*e)**n
                                                    yield 11, subst3
                                        subjects2.appendleft(tmp79)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 68884
                                        if len(subjects2) == 0:
                                            pass
                                            # State 68885
                                            if len(subjects) == 0:
                                                pass
                                                # 12: sin(d + x*e)**n2
                                                yield 12, subst3
                                    if len(subjects2) >= 1:
                                        tmp82 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3_1', tmp82)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68884
                                            if len(subjects2) == 0:
                                                pass
                                                # State 68885
                                                if len(subjects) == 0:
                                                    pass
                                                    # 12: sin(d + x*e)**n2
                                                    yield 12, subst3
                                        subjects2.appendleft(tmp82)
                            if pattern_index == 1:
                                pass
                                # State 97853
                                if len(subjects56) == 0:
                                    pass
                                    # State 97854
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp84 = subjects2.popleft()
                                        # State 97855
                                        if len(subjects2) == 0:
                                            pass
                                            # State 97856
                                            if len(subjects) == 0:
                                                pass
                                                # 32: 1/sin(c + d*x**n)
                                                yield 32, subst2
                                        subjects2.appendleft(tmp84)
                        subjects56.appendleft(tmp75)
                if len(subjects56) >= 1:
                    tmp85 = subjects56.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp85)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98291
                        if len(subjects56) == 0:
                            pass
                            # State 98292
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp87 = subjects2.popleft()
                                # State 98293
                                if len(subjects2) == 0:
                                    pass
                                    # State 98294
                                    if len(subjects) == 0:
                                        pass
                                        # 34: 1/sin(u)
                                        yield 34, subst1
                                subjects2.appendleft(tmp87)
                    subjects56.appendleft(tmp85)
                if len(subjects56) >= 1 and isinstance(subjects56[0], Add):
                    tmp88 = subjects56.popleft()
                    associative1 = tmp88
                    associative_type1 = type(tmp88)
                    subjects89 = deque(tmp88._args)
                    matcher = CommutativeMatcher68809.get()
                    tmp90 = subjects89
                    subjects89 = []
                    for s in tmp90:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp90, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 68815
                            if len(subjects56) == 0:
                                pass
                                # State 68816
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 68817
                                    if len(subjects2) == 0:
                                        pass
                                        # State 68818
                                        if len(subjects) == 0:
                                            pass
                                            # 11: sin(d + x*e)**n
                                            yield 11, subst2
                                if len(subjects2) >= 1:
                                    tmp92 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3', tmp92)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 68817
                                        if len(subjects2) == 0:
                                            pass
                                            # State 68818
                                            if len(subjects) == 0:
                                                pass
                                                # 11: sin(d + x*e)**n
                                                yield 11, subst2
                                    subjects2.appendleft(tmp92)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.3_1', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 68886
                                    if len(subjects2) == 0:
                                        pass
                                        # State 68887
                                        if len(subjects) == 0:
                                            pass
                                            # 12: sin(d + x*e)**n2
                                            yield 12, subst2
                                if len(subjects2) >= 1:
                                    tmp95 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3_1', tmp95)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 68886
                                        if len(subjects2) == 0:
                                            pass
                                            # State 68887
                                            if len(subjects) == 0:
                                                pass
                                                # 12: sin(d + x*e)**n2
                                                yield 12, subst2
                                    subjects2.appendleft(tmp95)
                        if pattern_index == 1:
                            pass
                            # State 97867
                            if len(subjects56) == 0:
                                pass
                                # State 97868
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp97 = subjects2.popleft()
                                    # State 97869
                                    if len(subjects2) == 0:
                                        pass
                                        # State 97870
                                        if len(subjects) == 0:
                                            pass
                                            # 32: 1/sin(c + d*x**n)
                                            yield 32, subst1
                                    subjects2.appendleft(tmp97)
                    subjects56.appendleft(tmp88)
                subjects2.appendleft(tmp55)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp98 = subjects2.popleft()
                subjects99 = deque(tmp98._args)
                # State 69077
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 69078
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 69079
                        if len(subjects99) >= 1:
                            tmp102 = subjects99.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.3.1.0', tmp102)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 69080
                                if len(subjects99) == 0:
                                    pass
                                    # State 69081
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69082
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69083
                                            if len(subjects) == 0:
                                                pass
                                                # 13: cos(d + x*e)**n
                                                yield 13, subst4
                                    if len(subjects2) >= 1:
                                        tmp105 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', tmp105)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69082
                                            if len(subjects2) == 0:
                                                pass
                                                # State 69083
                                                if len(subjects) == 0:
                                                    pass
                                                    # 13: cos(d + x*e)**n
                                                    yield 13, subst4
                                        subjects2.appendleft(tmp105)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69162
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69163
                                            if len(subjects) == 0:
                                                pass
                                                # 14: cos(d + x*e)**n2
                                                yield 14, subst4
                                    if len(subjects2) >= 1:
                                        tmp108 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3_1', tmp108)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69162
                                            if len(subjects2) == 0:
                                                pass
                                                # State 69163
                                                if len(subjects) == 0:
                                                    pass
                                                    # 14: cos(d + x*e)**n2
                                                    yield 14, subst4
                                        subjects2.appendleft(tmp108)
                            subjects99.appendleft(tmp102)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 97533
                        if len(subjects99) >= 1 and isinstance(subjects99[0], Pow):
                            tmp111 = subjects99.popleft()
                            subjects112 = deque(tmp111._args)
                            # State 97534
                            if len(subjects112) >= 1:
                                tmp113 = subjects112.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp113)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 97535
                                    if len(subjects112) >= 1:
                                        tmp115 = subjects112.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp115)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 97536
                                            if len(subjects112) == 0:
                                                pass
                                                # State 97537
                                                if len(subjects99) == 0:
                                                    pass
                                                    # State 97538
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp117 = subjects2.popleft()
                                                        # State 97539
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 97540
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 31: 1/cos(c + d*x**n)
                                                                yield 31, subst4
                                                        subjects2.appendleft(tmp117)
                                        subjects112.appendleft(tmp115)
                                subjects112.appendleft(tmp113)
                            subjects99.appendleft(tmp111)
                    if len(subjects99) >= 1 and isinstance(subjects99[0], Mul):
                        tmp118 = subjects99.popleft()
                        associative1 = tmp118
                        associative_type1 = type(tmp118)
                        subjects119 = deque(tmp118._args)
                        matcher = CommutativeMatcher69085.get()
                        tmp120 = subjects119
                        subjects119 = []
                        for s in tmp120:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp120, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 69086
                                if len(subjects99) == 0:
                                    pass
                                    # State 69087
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69088
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69089
                                            if len(subjects) == 0:
                                                pass
                                                # 13: cos(d + x*e)**n
                                                yield 13, subst3
                                    if len(subjects2) >= 1:
                                        tmp122 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp122)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69088
                                            if len(subjects2) == 0:
                                                pass
                                                # State 69089
                                                if len(subjects) == 0:
                                                    pass
                                                    # 13: cos(d + x*e)**n
                                                    yield 13, subst3
                                        subjects2.appendleft(tmp122)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69164
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69165
                                            if len(subjects) == 0:
                                                pass
                                                # 14: cos(d + x*e)**n2
                                                yield 14, subst3
                                    if len(subjects2) >= 1:
                                        tmp125 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3_1', tmp125)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69164
                                            if len(subjects2) == 0:
                                                pass
                                                # State 69165
                                                if len(subjects) == 0:
                                                    pass
                                                    # 14: cos(d + x*e)**n2
                                                    yield 14, subst3
                                        subjects2.appendleft(tmp125)
                            if pattern_index == 1:
                                pass
                                # State 97545
                                if len(subjects99) == 0:
                                    pass
                                    # State 97546
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp127 = subjects2.popleft()
                                        # State 97547
                                        if len(subjects2) == 0:
                                            pass
                                            # State 97548
                                            if len(subjects) == 0:
                                                pass
                                                # 31: 1/cos(c + d*x**n)
                                                yield 31, subst2
                                        subjects2.appendleft(tmp127)
                        subjects99.appendleft(tmp118)
                if len(subjects99) >= 1:
                    tmp128 = subjects99.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp128)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98235
                        if len(subjects99) == 0:
                            pass
                            # State 98236
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp130 = subjects2.popleft()
                                # State 98237
                                if len(subjects2) == 0:
                                    pass
                                    # State 98238
                                    if len(subjects) == 0:
                                        pass
                                        # 33: 1/cos(u)
                                        yield 33, subst1
                                subjects2.appendleft(tmp130)
                    subjects99.appendleft(tmp128)
                if len(subjects99) >= 1 and isinstance(subjects99[0], Add):
                    tmp131 = subjects99.popleft()
                    associative1 = tmp131
                    associative_type1 = type(tmp131)
                    subjects132 = deque(tmp131._args)
                    matcher = CommutativeMatcher69091.get()
                    tmp133 = subjects132
                    subjects132 = []
                    for s in tmp133:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp133, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 69097
                            if len(subjects99) == 0:
                                pass
                                # State 69098
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 69099
                                    if len(subjects2) == 0:
                                        pass
                                        # State 69100
                                        if len(subjects) == 0:
                                            pass
                                            # 13: cos(d + x*e)**n
                                            yield 13, subst2
                                if len(subjects2) >= 1:
                                    tmp135 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3', tmp135)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69099
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69100
                                            if len(subjects) == 0:
                                                pass
                                                # 13: cos(d + x*e)**n
                                                yield 13, subst2
                                    subjects2.appendleft(tmp135)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.3_1', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 69166
                                    if len(subjects2) == 0:
                                        pass
                                        # State 69167
                                        if len(subjects) == 0:
                                            pass
                                            # 14: cos(d + x*e)**n2
                                            yield 14, subst2
                                if len(subjects2) >= 1:
                                    tmp138 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3_1', tmp138)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69166
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69167
                                            if len(subjects) == 0:
                                                pass
                                                # 14: cos(d + x*e)**n2
                                                yield 14, subst2
                                    subjects2.appendleft(tmp138)
                        if pattern_index == 1:
                            pass
                            # State 97559
                            if len(subjects99) == 0:
                                pass
                                # State 97560
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp140 = subjects2.popleft()
                                    # State 97561
                                    if len(subjects2) == 0:
                                        pass
                                        # State 97562
                                        if len(subjects) == 0:
                                            pass
                                            # 31: 1/cos(c + d*x**n)
                                            yield 31, subst1
                                    subjects2.appendleft(tmp140)
                    subjects99.appendleft(tmp131)
                subjects2.appendleft(tmp98)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp141 = subjects2.popleft()
                subjects142 = deque(tmp141._args)
                # State 83400
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 83401
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83402
                        if len(subjects142) >= 1:
                            tmp145 = subjects142.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.3.1.0', tmp145)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83403
                                if len(subjects142) == 0:
                                    pass
                                    # State 83404
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83405
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83406
                                            if len(subjects) == 0:
                                                pass
                                                # 19: tan(d + x*e)**n
                                                yield 19, subst4
                                    if len(subjects2) >= 1:
                                        tmp148 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', tmp148)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83405
                                            if len(subjects2) == 0:
                                                pass
                                                # State 83406
                                                if len(subjects) == 0:
                                                    pass
                                                    # 19: tan(d + x*e)**n
                                                    yield 19, subst4
                                        subjects2.appendleft(tmp148)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83485
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83486
                                            if len(subjects) == 0:
                                                pass
                                                # 20: tan(d + x*e)**n2
                                                yield 20, subst4
                                    if len(subjects2) >= 1:
                                        tmp151 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3_1', tmp151)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83485
                                            if len(subjects2) == 0:
                                                pass
                                                # State 83486
                                                if len(subjects) == 0:
                                                    pass
                                                    # 20: tan(d + x*e)**n2
                                                    yield 20, subst4
                                        subjects2.appendleft(tmp151)
                            subjects142.appendleft(tmp145)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 87478
                        if len(subjects142) >= 1 and isinstance(subjects142[0], Pow):
                            tmp154 = subjects142.popleft()
                            subjects155 = deque(tmp154._args)
                            # State 87479
                            if len(subjects155) >= 1:
                                tmp156 = subjects155.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp156)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 87480
                                    if len(subjects155) >= 1:
                                        tmp158 = subjects155.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp158)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 87481
                                            if len(subjects155) == 0:
                                                pass
                                                # State 87482
                                                if len(subjects142) == 0:
                                                    pass
                                                    # State 87483
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp160 = subjects2.popleft()
                                                        # State 87484
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 87485
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 24: 1/tan(c + d*x**n)
                                                                yield 24, subst4
                                                        subjects2.appendleft(tmp160)
                                        subjects155.appendleft(tmp158)
                                subjects155.appendleft(tmp156)
                            subjects142.appendleft(tmp154)
                    if len(subjects142) >= 1 and isinstance(subjects142[0], Mul):
                        tmp161 = subjects142.popleft()
                        associative1 = tmp161
                        associative_type1 = type(tmp161)
                        subjects162 = deque(tmp161._args)
                        matcher = CommutativeMatcher83408.get()
                        tmp163 = subjects162
                        subjects162 = []
                        for s in tmp163:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp163, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83409
                                if len(subjects142) == 0:
                                    pass
                                    # State 83410
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83411
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83412
                                            if len(subjects) == 0:
                                                pass
                                                # 19: tan(d + x*e)**n
                                                yield 19, subst3
                                    if len(subjects2) >= 1:
                                        tmp165 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp165)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83411
                                            if len(subjects2) == 0:
                                                pass
                                                # State 83412
                                                if len(subjects) == 0:
                                                    pass
                                                    # 19: tan(d + x*e)**n
                                                    yield 19, subst3
                                        subjects2.appendleft(tmp165)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83487
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83488
                                            if len(subjects) == 0:
                                                pass
                                                # 20: tan(d + x*e)**n2
                                                yield 20, subst3
                                    if len(subjects2) >= 1:
                                        tmp168 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3_1', tmp168)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83487
                                            if len(subjects2) == 0:
                                                pass
                                                # State 83488
                                                if len(subjects) == 0:
                                                    pass
                                                    # 20: tan(d + x*e)**n2
                                                    yield 20, subst3
                                        subjects2.appendleft(tmp168)
                            if pattern_index == 1:
                                pass
                                # State 87490
                                if len(subjects142) == 0:
                                    pass
                                    # State 87491
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp170 = subjects2.popleft()
                                        # State 87492
                                        if len(subjects2) == 0:
                                            pass
                                            # State 87493
                                            if len(subjects) == 0:
                                                pass
                                                # 24: 1/tan(c + d*x**n)
                                                yield 24, subst2
                                        subjects2.appendleft(tmp170)
                        subjects142.appendleft(tmp161)
                if len(subjects142) >= 1:
                    tmp171 = subjects142.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp171)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 87896
                        if len(subjects142) == 0:
                            pass
                            # State 87897
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp173 = subjects2.popleft()
                                # State 87898
                                if len(subjects2) == 0:
                                    pass
                                    # State 87899
                                    if len(subjects) == 0:
                                        pass
                                        # 26: 1/tan(u)
                                        yield 26, subst1
                                subjects2.appendleft(tmp173)
                    subjects142.appendleft(tmp171)
                if len(subjects142) >= 1 and isinstance(subjects142[0], Add):
                    tmp174 = subjects142.popleft()
                    associative1 = tmp174
                    associative_type1 = type(tmp174)
                    subjects175 = deque(tmp174._args)
                    matcher = CommutativeMatcher83414.get()
                    tmp176 = subjects175
                    subjects175 = []
                    for s in tmp176:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp176, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 83420
                            if len(subjects142) == 0:
                                pass
                                # State 83421
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83422
                                    if len(subjects2) == 0:
                                        pass
                                        # State 83423
                                        if len(subjects) == 0:
                                            pass
                                            # 19: tan(d + x*e)**n
                                            yield 19, subst2
                                if len(subjects2) >= 1:
                                    tmp178 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3', tmp178)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83422
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83423
                                            if len(subjects) == 0:
                                                pass
                                                # 19: tan(d + x*e)**n
                                                yield 19, subst2
                                    subjects2.appendleft(tmp178)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.3_1', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83489
                                    if len(subjects2) == 0:
                                        pass
                                        # State 83490
                                        if len(subjects) == 0:
                                            pass
                                            # 20: tan(d + x*e)**n2
                                            yield 20, subst2
                                if len(subjects2) >= 1:
                                    tmp181 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3_1', tmp181)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83489
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83490
                                            if len(subjects) == 0:
                                                pass
                                                # 20: tan(d + x*e)**n2
                                                yield 20, subst2
                                    subjects2.appendleft(tmp181)
                        if pattern_index == 1:
                            pass
                            # State 87504
                            if len(subjects142) == 0:
                                pass
                                # State 87505
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp183 = subjects2.popleft()
                                    # State 87506
                                    if len(subjects2) == 0:
                                        pass
                                        # State 87507
                                        if len(subjects) == 0:
                                            pass
                                            # 24: 1/tan(c + d*x**n)
                                            yield 24, subst1
                                    subjects2.appendleft(tmp183)
                    subjects142.appendleft(tmp174)
                subjects2.appendleft(tmp141)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                tmp184 = subjects2.popleft()
                subjects185 = deque(tmp184._args)
                # State 83681
                if len(subjects185) >= 1 and isinstance(subjects185[0], tan):
                    tmp186 = subjects185.popleft()
                    subjects187 = deque(tmp186._args)
                    # State 83682
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83683
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83684
                            if len(subjects187) >= 1:
                                tmp190 = subjects187.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.4.1.0', tmp190)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83685
                                    if len(subjects187) == 0:
                                        pass
                                        # State 83686
                                        if len(subjects185) >= 1 and subjects185[0] == Integer(-1):
                                            tmp192 = subjects185.popleft()
                                            # State 83687
                                            if len(subjects185) == 0:
                                                pass
                                                # State 83688
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 83689
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 83690
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 21: (1/tan(d + x*e))**n
                                                            yield 21, subst4
                                                if len(subjects2) >= 1:
                                                    tmp194 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5', tmp194)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83689
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 83690
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 21: (1/tan(d + x*e))**n
                                                                yield 21, subst4
                                                    subjects2.appendleft(tmp194)
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 83796
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 83797
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 22: (1/tan(d + x*e))**n2
                                                            yield 22, subst4
                                                if len(subjects2) >= 1:
                                                    tmp197 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5_1', tmp197)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83796
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 83797
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 22: (1/tan(d + x*e))**n2
                                                                yield 22, subst4
                                                    subjects2.appendleft(tmp197)
                                            subjects185.appendleft(tmp192)
                                subjects187.appendleft(tmp190)
                        if len(subjects187) >= 1 and isinstance(subjects187[0], Mul):
                            tmp199 = subjects187.popleft()
                            associative1 = tmp199
                            associative_type1 = type(tmp199)
                            subjects200 = deque(tmp199._args)
                            matcher = CommutativeMatcher83692.get()
                            tmp201 = subjects200
                            subjects200 = []
                            for s in tmp201:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp201, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83693
                                    if len(subjects187) == 0:
                                        pass
                                        # State 83694
                                        if len(subjects185) >= 1 and subjects185[0] == Integer(-1):
                                            tmp202 = subjects185.popleft()
                                            # State 83695
                                            if len(subjects185) == 0:
                                                pass
                                                # State 83696
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 83697
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 83698
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 21: (1/tan(d + x*e))**n
                                                            yield 21, subst3
                                                if len(subjects2) >= 1:
                                                    tmp204 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5', tmp204)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83697
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 83698
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 21: (1/tan(d + x*e))**n
                                                                yield 21, subst3
                                                    subjects2.appendleft(tmp204)
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 83798
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 83799
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 22: (1/tan(d + x*e))**n2
                                                            yield 22, subst3
                                                if len(subjects2) >= 1:
                                                    tmp207 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5_1', tmp207)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83798
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 83799
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 22: (1/tan(d + x*e))**n2
                                                                yield 22, subst3
                                                    subjects2.appendleft(tmp207)
                                            subjects185.appendleft(tmp202)
                            subjects187.appendleft(tmp199)
                    if len(subjects187) >= 1 and isinstance(subjects187[0], Add):
                        tmp209 = subjects187.popleft()
                        associative1 = tmp209
                        associative_type1 = type(tmp209)
                        subjects210 = deque(tmp209._args)
                        matcher = CommutativeMatcher83700.get()
                        tmp211 = subjects210
                        subjects210 = []
                        for s in tmp211:
                            matcher.add_subject(s)
                        for pattern_index, subst1 in matcher.match(tmp211, subst0):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83706
                                if len(subjects187) == 0:
                                    pass
                                    # State 83707
                                    if len(subjects185) >= 1 and subjects185[0] == Integer(-1):
                                        tmp212 = subjects185.popleft()
                                        # State 83708
                                        if len(subjects185) == 0:
                                            pass
                                            # State 83709
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i3.1.5', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 83710
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 83711
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 21: (1/tan(d + x*e))**n
                                                        yield 21, subst2
                                            if len(subjects2) >= 1:
                                                tmp214 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i3.1.5', tmp214)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 83710
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 83711
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 21: (1/tan(d + x*e))**n
                                                            yield 21, subst2
                                                subjects2.appendleft(tmp214)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i3.1.5_1', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 83800
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 83801
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 22: (1/tan(d + x*e))**n2
                                                        yield 22, subst2
                                            if len(subjects2) >= 1:
                                                tmp217 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i3.1.5_1', tmp217)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 83800
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 83801
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 22: (1/tan(d + x*e))**n2
                                                            yield 22, subst2
                                                subjects2.appendleft(tmp217)
                                        subjects185.appendleft(tmp212)
                        subjects187.appendleft(tmp209)
                    subjects185.appendleft(tmp186)
                if len(subjects185) >= 1 and isinstance(subjects185[0], cos):
                    tmp219 = subjects185.popleft()
                    subjects220 = deque(tmp219._args)
                    # State 95398
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 95399
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95400
                            if len(subjects220) >= 1:
                                tmp223 = subjects220.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.4.1.0', tmp223)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 95401
                                    if len(subjects220) == 0:
                                        pass
                                        # State 95402
                                        if len(subjects185) >= 1 and subjects185[0] == Integer(-1):
                                            tmp225 = subjects185.popleft()
                                            # State 95403
                                            if len(subjects185) == 0:
                                                pass
                                                # State 95404
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95405
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95406
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 27: (1/cos(d + x*e))**n
                                                            yield 27, subst4
                                                if len(subjects2) >= 1:
                                                    tmp227 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5', tmp227)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95405
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 95406
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 27: (1/cos(d + x*e))**n
                                                                yield 27, subst4
                                                    subjects2.appendleft(tmp227)
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95507
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95508
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 28: (1/cos(d + x*e))**n2
                                                            yield 28, subst4
                                                if len(subjects2) >= 1:
                                                    tmp230 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5_1', tmp230)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95507
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 95508
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: (1/cos(d + x*e))**n2
                                                                yield 28, subst4
                                                    subjects2.appendleft(tmp230)
                                            subjects185.appendleft(tmp225)
                                subjects220.appendleft(tmp223)
                        if len(subjects220) >= 1 and isinstance(subjects220[0], Mul):
                            tmp232 = subjects220.popleft()
                            associative1 = tmp232
                            associative_type1 = type(tmp232)
                            subjects233 = deque(tmp232._args)
                            matcher = CommutativeMatcher95408.get()
                            tmp234 = subjects233
                            subjects233 = []
                            for s in tmp234:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp234, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95409
                                    if len(subjects220) == 0:
                                        pass
                                        # State 95410
                                        if len(subjects185) >= 1 and subjects185[0] == Integer(-1):
                                            tmp235 = subjects185.popleft()
                                            # State 95411
                                            if len(subjects185) == 0:
                                                pass
                                                # State 95412
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95413
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95414
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 27: (1/cos(d + x*e))**n
                                                            yield 27, subst3
                                                if len(subjects2) >= 1:
                                                    tmp237 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5', tmp237)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95413
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 95414
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 27: (1/cos(d + x*e))**n
                                                                yield 27, subst3
                                                    subjects2.appendleft(tmp237)
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95509
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95510
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 28: (1/cos(d + x*e))**n2
                                                            yield 28, subst3
                                                if len(subjects2) >= 1:
                                                    tmp240 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5_1', tmp240)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95509
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 95510
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: (1/cos(d + x*e))**n2
                                                                yield 28, subst3
                                                    subjects2.appendleft(tmp240)
                                            subjects185.appendleft(tmp235)
                            subjects220.appendleft(tmp232)
                    if len(subjects220) >= 1 and isinstance(subjects220[0], Add):
                        tmp242 = subjects220.popleft()
                        associative1 = tmp242
                        associative_type1 = type(tmp242)
                        subjects243 = deque(tmp242._args)
                        matcher = CommutativeMatcher95416.get()
                        tmp244 = subjects243
                        subjects243 = []
                        for s in tmp244:
                            matcher.add_subject(s)
                        for pattern_index, subst1 in matcher.match(tmp244, subst0):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 95422
                                if len(subjects220) == 0:
                                    pass
                                    # State 95423
                                    if len(subjects185) >= 1 and subjects185[0] == Integer(-1):
                                        tmp245 = subjects185.popleft()
                                        # State 95424
                                        if len(subjects185) == 0:
                                            pass
                                            # State 95425
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i3.1.5', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 95426
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 95427
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 27: (1/cos(d + x*e))**n
                                                        yield 27, subst2
                                            if len(subjects2) >= 1:
                                                tmp247 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i3.1.5', tmp247)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95426
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95427
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 27: (1/cos(d + x*e))**n
                                                            yield 27, subst2
                                                subjects2.appendleft(tmp247)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i3.1.5_1', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 95511
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 95512
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 28: (1/cos(d + x*e))**n2
                                                        yield 28, subst2
                                            if len(subjects2) >= 1:
                                                tmp250 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i3.1.5_1', tmp250)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95511
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95512
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 28: (1/cos(d + x*e))**n2
                                                            yield 28, subst2
                                                subjects2.appendleft(tmp250)
                                        subjects185.appendleft(tmp245)
                        subjects220.appendleft(tmp242)
                    subjects185.appendleft(tmp219)
                if len(subjects185) >= 1 and isinstance(subjects185[0], sin):
                    tmp252 = subjects185.popleft()
                    subjects253 = deque(tmp252._args)
                    # State 95794
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 95795
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95796
                            if len(subjects253) >= 1:
                                tmp256 = subjects253.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.4.1.0', tmp256)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 95797
                                    if len(subjects253) == 0:
                                        pass
                                        # State 95798
                                        if len(subjects185) >= 1 and subjects185[0] == Integer(-1):
                                            tmp258 = subjects185.popleft()
                                            # State 95799
                                            if len(subjects185) == 0:
                                                pass
                                                # State 95800
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95801
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95802
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 29: (1/sin(d + x*e))**n
                                                            yield 29, subst4
                                                if len(subjects2) >= 1:
                                                    tmp260 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5', tmp260)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95801
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 95802
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 29: (1/sin(d + x*e))**n
                                                                yield 29, subst4
                                                    subjects2.appendleft(tmp260)
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95903
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95904
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 30: (1/sin(d + x*e))**n2
                                                            yield 30, subst4
                                                if len(subjects2) >= 1:
                                                    tmp263 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5_1', tmp263)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95903
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 95904
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 30: (1/sin(d + x*e))**n2
                                                                yield 30, subst4
                                                    subjects2.appendleft(tmp263)
                                            subjects185.appendleft(tmp258)
                                subjects253.appendleft(tmp256)
                        if len(subjects253) >= 1 and isinstance(subjects253[0], Mul):
                            tmp265 = subjects253.popleft()
                            associative1 = tmp265
                            associative_type1 = type(tmp265)
                            subjects266 = deque(tmp265._args)
                            matcher = CommutativeMatcher95804.get()
                            tmp267 = subjects266
                            subjects266 = []
                            for s in tmp267:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp267, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95805
                                    if len(subjects253) == 0:
                                        pass
                                        # State 95806
                                        if len(subjects185) >= 1 and subjects185[0] == Integer(-1):
                                            tmp268 = subjects185.popleft()
                                            # State 95807
                                            if len(subjects185) == 0:
                                                pass
                                                # State 95808
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95809
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95810
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 29: (1/sin(d + x*e))**n
                                                            yield 29, subst3
                                                if len(subjects2) >= 1:
                                                    tmp270 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5', tmp270)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95809
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 95810
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 29: (1/sin(d + x*e))**n
                                                                yield 29, subst3
                                                    subjects2.appendleft(tmp270)
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95905
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95906
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 30: (1/sin(d + x*e))**n2
                                                            yield 30, subst3
                                                if len(subjects2) >= 1:
                                                    tmp273 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5_1', tmp273)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95905
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 95906
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 30: (1/sin(d + x*e))**n2
                                                                yield 30, subst3
                                                    subjects2.appendleft(tmp273)
                                            subjects185.appendleft(tmp268)
                            subjects253.appendleft(tmp265)
                    if len(subjects253) >= 1 and isinstance(subjects253[0], Add):
                        tmp275 = subjects253.popleft()
                        associative1 = tmp275
                        associative_type1 = type(tmp275)
                        subjects276 = deque(tmp275._args)
                        matcher = CommutativeMatcher95812.get()
                        tmp277 = subjects276
                        subjects276 = []
                        for s in tmp277:
                            matcher.add_subject(s)
                        for pattern_index, subst1 in matcher.match(tmp277, subst0):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 95818
                                if len(subjects253) == 0:
                                    pass
                                    # State 95819
                                    if len(subjects185) >= 1 and subjects185[0] == Integer(-1):
                                        tmp278 = subjects185.popleft()
                                        # State 95820
                                        if len(subjects185) == 0:
                                            pass
                                            # State 95821
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i3.1.5', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 95822
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 95823
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 29: (1/sin(d + x*e))**n
                                                        yield 29, subst2
                                            if len(subjects2) >= 1:
                                                tmp280 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i3.1.5', tmp280)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95822
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95823
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 29: (1/sin(d + x*e))**n
                                                            yield 29, subst2
                                                subjects2.appendleft(tmp280)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i3.1.5_1', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 95907
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 95908
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 30: (1/sin(d + x*e))**n2
                                                        yield 30, subst2
                                            if len(subjects2) >= 1:
                                                tmp283 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i3.1.5_1', tmp283)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95907
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95908
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 30: (1/sin(d + x*e))**n2
                                                            yield 30, subst2
                                                subjects2.appendleft(tmp283)
                                        subjects185.appendleft(tmp278)
                        subjects253.appendleft(tmp275)
                    subjects185.appendleft(tmp252)
                subjects2.appendleft(tmp184)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tanh):
                tmp285 = subjects2.popleft()
                subjects286 = deque(tmp285._args)
                # State 126949
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 126950
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 126951
                        if len(subjects286) >= 1 and isinstance(subjects286[0], Pow):
                            tmp289 = subjects286.popleft()
                            subjects290 = deque(tmp289._args)
                            # State 126952
                            if len(subjects290) >= 1:
                                tmp291 = subjects290.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp291)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 126953
                                    if len(subjects290) >= 1:
                                        tmp293 = subjects290.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp293)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 126954
                                            if len(subjects290) == 0:
                                                pass
                                                # State 126955
                                                if len(subjects286) == 0:
                                                    pass
                                                    # State 126956
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp295 = subjects2.popleft()
                                                        # State 126957
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 126958
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 48: 1/tanh(c + d*x**n)
                                                                yield 48, subst4
                                                        subjects2.appendleft(tmp295)
                                        subjects290.appendleft(tmp293)
                                subjects290.appendleft(tmp291)
                            subjects286.appendleft(tmp289)
                    if len(subjects286) >= 1 and isinstance(subjects286[0], Mul):
                        tmp296 = subjects286.popleft()
                        associative1 = tmp296
                        associative_type1 = type(tmp296)
                        subjects297 = deque(tmp296._args)
                        matcher = CommutativeMatcher126960.get()
                        tmp298 = subjects297
                        subjects297 = []
                        for s in tmp298:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp298, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 126965
                                if len(subjects286) == 0:
                                    pass
                                    # State 126966
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp299 = subjects2.popleft()
                                        # State 126967
                                        if len(subjects2) == 0:
                                            pass
                                            # State 126968
                                            if len(subjects) == 0:
                                                pass
                                                # 48: 1/tanh(c + d*x**n)
                                                yield 48, subst2
                                        subjects2.appendleft(tmp299)
                        subjects286.appendleft(tmp296)
                if len(subjects286) >= 1:
                    tmp300 = subjects286.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp300)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 127391
                        if len(subjects286) == 0:
                            pass
                            # State 127392
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp302 = subjects2.popleft()
                                # State 127393
                                if len(subjects2) == 0:
                                    pass
                                    # State 127394
                                    if len(subjects) == 0:
                                        pass
                                        # 50: 1/tanh(u)
                                        yield 50, subst1
                                subjects2.appendleft(tmp302)
                    subjects286.appendleft(tmp300)
                if len(subjects286) >= 1 and isinstance(subjects286[0], Add):
                    tmp303 = subjects286.popleft()
                    associative1 = tmp303
                    associative_type1 = type(tmp303)
                    subjects304 = deque(tmp303._args)
                    matcher = CommutativeMatcher126970.get()
                    tmp305 = subjects304
                    subjects304 = []
                    for s in tmp305:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp305, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 126983
                            if len(subjects286) == 0:
                                pass
                                # State 126984
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp306 = subjects2.popleft()
                                    # State 126985
                                    if len(subjects2) == 0:
                                        pass
                                        # State 126986
                                        if len(subjects) == 0:
                                            pass
                                            # 48: 1/tanh(c + d*x**n)
                                            yield 48, subst1
                                    subjects2.appendleft(tmp306)
                    subjects286.appendleft(tmp303)
                subjects2.appendleft(tmp285)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cosh):
                tmp307 = subjects2.popleft()
                subjects308 = deque(tmp307._args)
                # State 129726
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 129727
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 129728
                        if len(subjects308) >= 1 and isinstance(subjects308[0], Pow):
                            tmp311 = subjects308.popleft()
                            subjects312 = deque(tmp311._args)
                            # State 129729
                            if len(subjects312) >= 1:
                                tmp313 = subjects312.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp313)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 129730
                                    if len(subjects312) >= 1:
                                        tmp315 = subjects312.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp315)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 129731
                                            if len(subjects312) == 0:
                                                pass
                                                # State 129732
                                                if len(subjects308) == 0:
                                                    pass
                                                    # State 129733
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp317 = subjects2.popleft()
                                                        # State 129734
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 129735
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 51: 1/cosh(c + d*x**n)
                                                                yield 51, subst4
                                                        subjects2.appendleft(tmp317)
                                        subjects312.appendleft(tmp315)
                                subjects312.appendleft(tmp313)
                            subjects308.appendleft(tmp311)
                    if len(subjects308) >= 1 and isinstance(subjects308[0], Mul):
                        tmp318 = subjects308.popleft()
                        associative1 = tmp318
                        associative_type1 = type(tmp318)
                        subjects319 = deque(tmp318._args)
                        matcher = CommutativeMatcher129737.get()
                        tmp320 = subjects319
                        subjects319 = []
                        for s in tmp320:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp320, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 129742
                                if len(subjects308) == 0:
                                    pass
                                    # State 129743
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp321 = subjects2.popleft()
                                        # State 129744
                                        if len(subjects2) == 0:
                                            pass
                                            # State 129745
                                            if len(subjects) == 0:
                                                pass
                                                # 51: 1/cosh(c + d*x**n)
                                                yield 51, subst2
                                        subjects2.appendleft(tmp321)
                        subjects308.appendleft(tmp318)
                if len(subjects308) >= 1:
                    tmp322 = subjects308.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp322)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130484
                        if len(subjects308) == 0:
                            pass
                            # State 130485
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp324 = subjects2.popleft()
                                # State 130486
                                if len(subjects2) == 0:
                                    pass
                                    # State 130487
                                    if len(subjects) == 0:
                                        pass
                                        # 53: 1/cosh(u)
                                        yield 53, subst1
                                subjects2.appendleft(tmp324)
                    subjects308.appendleft(tmp322)
                if len(subjects308) >= 1 and isinstance(subjects308[0], Add):
                    tmp325 = subjects308.popleft()
                    associative1 = tmp325
                    associative_type1 = type(tmp325)
                    subjects326 = deque(tmp325._args)
                    matcher = CommutativeMatcher129747.get()
                    tmp327 = subjects326
                    subjects326 = []
                    for s in tmp327:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp327, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 129760
                            if len(subjects308) == 0:
                                pass
                                # State 129761
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp328 = subjects2.popleft()
                                    # State 129762
                                    if len(subjects2) == 0:
                                        pass
                                        # State 129763
                                        if len(subjects) == 0:
                                            pass
                                            # 51: 1/cosh(c + d*x**n)
                                            yield 51, subst1
                                    subjects2.appendleft(tmp328)
                    subjects308.appendleft(tmp325)
                subjects2.appendleft(tmp307)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sinh):
                tmp329 = subjects2.popleft()
                subjects330 = deque(tmp329._args)
                # State 130066
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 130067
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130068
                        if len(subjects330) >= 1 and isinstance(subjects330[0], Pow):
                            tmp333 = subjects330.popleft()
                            subjects334 = deque(tmp333._args)
                            # State 130069
                            if len(subjects334) >= 1:
                                tmp335 = subjects334.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp335)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 130070
                                    if len(subjects334) >= 1:
                                        tmp337 = subjects334.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp337)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 130071
                                            if len(subjects334) == 0:
                                                pass
                                                # State 130072
                                                if len(subjects330) == 0:
                                                    pass
                                                    # State 130073
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp339 = subjects2.popleft()
                                                        # State 130074
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 130075
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 52: 1/sinh(c + d*x**n)
                                                                yield 52, subst4
                                                        subjects2.appendleft(tmp339)
                                        subjects334.appendleft(tmp337)
                                subjects334.appendleft(tmp335)
                            subjects330.appendleft(tmp333)
                    if len(subjects330) >= 1 and isinstance(subjects330[0], Mul):
                        tmp340 = subjects330.popleft()
                        associative1 = tmp340
                        associative_type1 = type(tmp340)
                        subjects341 = deque(tmp340._args)
                        matcher = CommutativeMatcher130077.get()
                        tmp342 = subjects341
                        subjects341 = []
                        for s in tmp342:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp342, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 130082
                                if len(subjects330) == 0:
                                    pass
                                    # State 130083
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp343 = subjects2.popleft()
                                        # State 130084
                                        if len(subjects2) == 0:
                                            pass
                                            # State 130085
                                            if len(subjects) == 0:
                                                pass
                                                # 52: 1/sinh(c + d*x**n)
                                                yield 52, subst2
                                        subjects2.appendleft(tmp343)
                        subjects330.appendleft(tmp340)
                if len(subjects330) >= 1:
                    tmp344 = subjects330.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp344)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130540
                        if len(subjects330) == 0:
                            pass
                            # State 130541
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp346 = subjects2.popleft()
                                # State 130542
                                if len(subjects2) == 0:
                                    pass
                                    # State 130543
                                    if len(subjects) == 0:
                                        pass
                                        # 54: 1/sinh(u)
                                        yield 54, subst1
                                subjects2.appendleft(tmp346)
                    subjects330.appendleft(tmp344)
                if len(subjects330) >= 1 and isinstance(subjects330[0], Add):
                    tmp347 = subjects330.popleft()
                    associative1 = tmp347
                    associative_type1 = type(tmp347)
                    subjects348 = deque(tmp347._args)
                    matcher = CommutativeMatcher130087.get()
                    tmp349 = subjects348
                    subjects348 = []
                    for s in tmp349:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp349, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 130100
                            if len(subjects330) == 0:
                                pass
                                # State 130101
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp350 = subjects2.popleft()
                                    # State 130102
                                    if len(subjects2) == 0:
                                        pass
                                        # State 130103
                                        if len(subjects) == 0:
                                            pass
                                            # 52: 1/sinh(c + d*x**n)
                                            yield 52, subst1
                                    subjects2.appendleft(tmp350)
                    subjects330.appendleft(tmp347)
                subjects2.appendleft(tmp329)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 8162
            if len(subjects) >= 1:
                tmp352 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.1', tmp352)
                except ValueError:
                    pass
                else:
                    pass
                    # State 8163
                    if len(subjects) == 0:
                        pass
                        # 1: x**n2
                        yield 1, subst2
                subjects.appendleft(tmp352)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10915
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp355 = subjects.popleft()
                    subjects356 = deque(tmp355._args)
                    # State 10916
                    if len(subjects356) >= 1:
                        tmp357 = subjects356.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1', tmp357)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10917
                            if len(subjects356) >= 1 and subjects356[0] == Integer(-1):
                                tmp359 = subjects356.popleft()
                                # State 10918
                                if len(subjects356) == 0:
                                    pass
                                    # State 10919
                                    if len(subjects) == 0:
                                        pass
                                        # 4: (c/x)**n2
                                        yield 4, subst3
                                subjects356.appendleft(tmp359)
                        subjects356.appendleft(tmp357)
                    subjects.appendleft(tmp355)
            if len(subjects) >= 1:
                tmp360 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1', tmp360)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11168
                    if len(subjects) == 0:
                        pass
                        # 5: x**n2
                        yield 5, subst2
                subjects.appendleft(tmp360)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp362 = subjects.popleft()
                associative1 = tmp362
                associative_type1 = type(tmp362)
                subjects363 = deque(tmp362._args)
                matcher = CommutativeMatcher10921.get()
                tmp364 = subjects363
                subjects363 = []
                for s in tmp364:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp364, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10926
                        if len(subjects) == 0:
                            pass
                            # 4: (c/x)**n2
                            yield 4, subst2
                subjects.appendleft(tmp362)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 68776
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp366 = subjects.popleft()
                subjects367 = deque(tmp366._args)
                # State 68777
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68778
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 68779
                        if len(subjects367) >= 1:
                            tmp370 = subjects367.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0', tmp370)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 68780
                                if len(subjects367) == 0:
                                    pass
                                    # State 68781
                                    if len(subjects) == 0:
                                        pass
                                        # 11: sin(d + x*e)**n
                                        yield 11, subst4
                            subjects367.appendleft(tmp370)
                    if len(subjects367) >= 1 and isinstance(subjects367[0], Mul):
                        tmp372 = subjects367.popleft()
                        associative1 = tmp372
                        associative_type1 = type(tmp372)
                        subjects373 = deque(tmp372._args)
                        matcher = CommutativeMatcher68783.get()
                        tmp374 = subjects373
                        subjects373 = []
                        for s in tmp374:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp374, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 68784
                                if len(subjects367) == 0:
                                    pass
                                    # State 68785
                                    if len(subjects) == 0:
                                        pass
                                        # 11: sin(d + x*e)**n
                                        yield 11, subst3
                        subjects367.appendleft(tmp372)
                if len(subjects367) >= 1 and isinstance(subjects367[0], Add):
                    tmp375 = subjects367.popleft()
                    associative1 = tmp375
                    associative_type1 = type(tmp375)
                    subjects376 = deque(tmp375._args)
                    matcher = CommutativeMatcher68787.get()
                    tmp377 = subjects376
                    subjects376 = []
                    for s in tmp377:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp377, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 68793
                            if len(subjects367) == 0:
                                pass
                                # State 68794
                                if len(subjects) == 0:
                                    pass
                                    # 11: sin(d + x*e)**n
                                    yield 11, subst2
                    subjects367.appendleft(tmp375)
                subjects.appendleft(tmp366)
            if len(subjects) >= 1 and isinstance(subjects[0], cos):
                tmp378 = subjects.popleft()
                subjects379 = deque(tmp378._args)
                # State 69059
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 69060
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 69061
                        if len(subjects379) >= 1:
                            tmp382 = subjects379.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0', tmp382)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 69062
                                if len(subjects379) == 0:
                                    pass
                                    # State 69063
                                    if len(subjects) == 0:
                                        pass
                                        # 13: cos(d + x*e)**n
                                        yield 13, subst4
                            subjects379.appendleft(tmp382)
                    if len(subjects379) >= 1 and isinstance(subjects379[0], Mul):
                        tmp384 = subjects379.popleft()
                        associative1 = tmp384
                        associative_type1 = type(tmp384)
                        subjects385 = deque(tmp384._args)
                        matcher = CommutativeMatcher69065.get()
                        tmp386 = subjects385
                        subjects385 = []
                        for s in tmp386:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp386, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 69066
                                if len(subjects379) == 0:
                                    pass
                                    # State 69067
                                    if len(subjects) == 0:
                                        pass
                                        # 13: cos(d + x*e)**n
                                        yield 13, subst3
                        subjects379.appendleft(tmp384)
                if len(subjects379) >= 1 and isinstance(subjects379[0], Add):
                    tmp387 = subjects379.popleft()
                    associative1 = tmp387
                    associative_type1 = type(tmp387)
                    subjects388 = deque(tmp387._args)
                    matcher = CommutativeMatcher69069.get()
                    tmp389 = subjects388
                    subjects388 = []
                    for s in tmp389:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp389, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 69075
                            if len(subjects379) == 0:
                                pass
                                # State 69076
                                if len(subjects) == 0:
                                    pass
                                    # 13: cos(d + x*e)**n
                                    yield 13, subst2
                    subjects379.appendleft(tmp387)
                subjects.appendleft(tmp378)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp390 = subjects.popleft()
                subjects391 = deque(tmp390._args)
                # State 83382
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 83383
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83384
                        if len(subjects391) >= 1:
                            tmp394 = subjects391.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0', tmp394)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83385
                                if len(subjects391) == 0:
                                    pass
                                    # State 83386
                                    if len(subjects) == 0:
                                        pass
                                        # 19: tan(d + x*e)**n
                                        yield 19, subst4
                            subjects391.appendleft(tmp394)
                    if len(subjects391) >= 1 and isinstance(subjects391[0], Mul):
                        tmp396 = subjects391.popleft()
                        associative1 = tmp396
                        associative_type1 = type(tmp396)
                        subjects397 = deque(tmp396._args)
                        matcher = CommutativeMatcher83388.get()
                        tmp398 = subjects397
                        subjects397 = []
                        for s in tmp398:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp398, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83389
                                if len(subjects391) == 0:
                                    pass
                                    # State 83390
                                    if len(subjects) == 0:
                                        pass
                                        # 19: tan(d + x*e)**n
                                        yield 19, subst3
                        subjects391.appendleft(tmp396)
                if len(subjects391) >= 1 and isinstance(subjects391[0], Add):
                    tmp399 = subjects391.popleft()
                    associative1 = tmp399
                    associative_type1 = type(tmp399)
                    subjects400 = deque(tmp399._args)
                    matcher = CommutativeMatcher83392.get()
                    tmp401 = subjects400
                    subjects400 = []
                    for s in tmp401:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp401, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 83398
                            if len(subjects391) == 0:
                                pass
                                # State 83399
                                if len(subjects) == 0:
                                    pass
                                    # 19: tan(d + x*e)**n
                                    yield 19, subst2
                    subjects391.appendleft(tmp399)
                subjects.appendleft(tmp390)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.3_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 68863
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp403 = subjects.popleft()
                subjects404 = deque(tmp403._args)
                # State 68864
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68865
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 68866
                        if len(subjects404) >= 1:
                            tmp407 = subjects404.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0', tmp407)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 68867
                                if len(subjects404) == 0:
                                    pass
                                    # State 68868
                                    if len(subjects) == 0:
                                        pass
                                        # 12: sin(d + x*e)**n2
                                        yield 12, subst4
                            subjects404.appendleft(tmp407)
                    if len(subjects404) >= 1 and isinstance(subjects404[0], Mul):
                        tmp409 = subjects404.popleft()
                        associative1 = tmp409
                        associative_type1 = type(tmp409)
                        subjects410 = deque(tmp409._args)
                        matcher = CommutativeMatcher68870.get()
                        tmp411 = subjects410
                        subjects410 = []
                        for s in tmp411:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp411, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 68871
                                if len(subjects404) == 0:
                                    pass
                                    # State 68872
                                    if len(subjects) == 0:
                                        pass
                                        # 12: sin(d + x*e)**n2
                                        yield 12, subst3
                        subjects404.appendleft(tmp409)
                if len(subjects404) >= 1 and isinstance(subjects404[0], Add):
                    tmp412 = subjects404.popleft()
                    associative1 = tmp412
                    associative_type1 = type(tmp412)
                    subjects413 = deque(tmp412._args)
                    matcher = CommutativeMatcher68874.get()
                    tmp414 = subjects413
                    subjects413 = []
                    for s in tmp414:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp414, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 68880
                            if len(subjects404) == 0:
                                pass
                                # State 68881
                                if len(subjects) == 0:
                                    pass
                                    # 12: sin(d + x*e)**n2
                                    yield 12, subst2
                    subjects404.appendleft(tmp412)
                subjects.appendleft(tmp403)
            if len(subjects) >= 1 and isinstance(subjects[0], cos):
                tmp415 = subjects.popleft()
                subjects416 = deque(tmp415._args)
                # State 69144
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 69145
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 69146
                        if len(subjects416) >= 1:
                            tmp419 = subjects416.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0', tmp419)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 69147
                                if len(subjects416) == 0:
                                    pass
                                    # State 69148
                                    if len(subjects) == 0:
                                        pass
                                        # 14: cos(d + x*e)**n2
                                        yield 14, subst4
                            subjects416.appendleft(tmp419)
                    if len(subjects416) >= 1 and isinstance(subjects416[0], Mul):
                        tmp421 = subjects416.popleft()
                        associative1 = tmp421
                        associative_type1 = type(tmp421)
                        subjects422 = deque(tmp421._args)
                        matcher = CommutativeMatcher69150.get()
                        tmp423 = subjects422
                        subjects422 = []
                        for s in tmp423:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp423, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 69151
                                if len(subjects416) == 0:
                                    pass
                                    # State 69152
                                    if len(subjects) == 0:
                                        pass
                                        # 14: cos(d + x*e)**n2
                                        yield 14, subst3
                        subjects416.appendleft(tmp421)
                if len(subjects416) >= 1 and isinstance(subjects416[0], Add):
                    tmp424 = subjects416.popleft()
                    associative1 = tmp424
                    associative_type1 = type(tmp424)
                    subjects425 = deque(tmp424._args)
                    matcher = CommutativeMatcher69154.get()
                    tmp426 = subjects425
                    subjects425 = []
                    for s in tmp426:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp426, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 69160
                            if len(subjects416) == 0:
                                pass
                                # State 69161
                                if len(subjects) == 0:
                                    pass
                                    # 14: cos(d + x*e)**n2
                                    yield 14, subst2
                    subjects416.appendleft(tmp424)
                subjects.appendleft(tmp415)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp427 = subjects.popleft()
                subjects428 = deque(tmp427._args)
                # State 83467
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 83468
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83469
                        if len(subjects428) >= 1:
                            tmp431 = subjects428.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0', tmp431)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83470
                                if len(subjects428) == 0:
                                    pass
                                    # State 83471
                                    if len(subjects) == 0:
                                        pass
                                        # 20: tan(d + x*e)**n2
                                        yield 20, subst4
                            subjects428.appendleft(tmp431)
                    if len(subjects428) >= 1 and isinstance(subjects428[0], Mul):
                        tmp433 = subjects428.popleft()
                        associative1 = tmp433
                        associative_type1 = type(tmp433)
                        subjects434 = deque(tmp433._args)
                        matcher = CommutativeMatcher83473.get()
                        tmp435 = subjects434
                        subjects434 = []
                        for s in tmp435:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp435, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83474
                                if len(subjects428) == 0:
                                    pass
                                    # State 83475
                                    if len(subjects) == 0:
                                        pass
                                        # 20: tan(d + x*e)**n2
                                        yield 20, subst3
                        subjects428.appendleft(tmp433)
                if len(subjects428) >= 1 and isinstance(subjects428[0], Add):
                    tmp436 = subjects428.popleft()
                    associative1 = tmp436
                    associative_type1 = type(tmp436)
                    subjects437 = deque(tmp436._args)
                    matcher = CommutativeMatcher83477.get()
                    tmp438 = subjects437
                    subjects437 = []
                    for s in tmp438:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp438, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 83483
                            if len(subjects428) == 0:
                                pass
                                # State 83484
                                if len(subjects) == 0:
                                    pass
                                    # 20: tan(d + x*e)**n2
                                    yield 20, subst2
                    subjects428.appendleft(tmp436)
                subjects.appendleft(tmp427)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.5', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 83655
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp440 = subjects.popleft()
                subjects441 = deque(tmp440._args)
                # State 83656
                if len(subjects441) >= 1 and isinstance(subjects441[0], tan):
                    tmp442 = subjects441.popleft()
                    subjects443 = deque(tmp442._args)
                    # State 83657
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83658
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83659
                            if len(subjects443) >= 1:
                                tmp446 = subjects443.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.0', tmp446)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83660
                                    if len(subjects443) == 0:
                                        pass
                                        # State 83661
                                        if len(subjects441) >= 1 and subjects441[0] == Integer(-1):
                                            tmp448 = subjects441.popleft()
                                            # State 83662
                                            if len(subjects441) == 0:
                                                pass
                                                # State 83663
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: (1/tan(d + x*e))**n
                                                    yield 21, subst4
                                            subjects441.appendleft(tmp448)
                                subjects443.appendleft(tmp446)
                        if len(subjects443) >= 1 and isinstance(subjects443[0], Mul):
                            tmp449 = subjects443.popleft()
                            associative1 = tmp449
                            associative_type1 = type(tmp449)
                            subjects450 = deque(tmp449._args)
                            matcher = CommutativeMatcher83665.get()
                            tmp451 = subjects450
                            subjects450 = []
                            for s in tmp451:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp451, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83666
                                    if len(subjects443) == 0:
                                        pass
                                        # State 83667
                                        if len(subjects441) >= 1 and subjects441[0] == Integer(-1):
                                            tmp452 = subjects441.popleft()
                                            # State 83668
                                            if len(subjects441) == 0:
                                                pass
                                                # State 83669
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: (1/tan(d + x*e))**n
                                                    yield 21, subst3
                                            subjects441.appendleft(tmp452)
                            subjects443.appendleft(tmp449)
                    if len(subjects443) >= 1 and isinstance(subjects443[0], Add):
                        tmp453 = subjects443.popleft()
                        associative1 = tmp453
                        associative_type1 = type(tmp453)
                        subjects454 = deque(tmp453._args)
                        matcher = CommutativeMatcher83671.get()
                        tmp455 = subjects454
                        subjects454 = []
                        for s in tmp455:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp455, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83677
                                if len(subjects443) == 0:
                                    pass
                                    # State 83678
                                    if len(subjects441) >= 1 and subjects441[0] == Integer(-1):
                                        tmp456 = subjects441.popleft()
                                        # State 83679
                                        if len(subjects441) == 0:
                                            pass
                                            # State 83680
                                            if len(subjects) == 0:
                                                pass
                                                # 21: (1/tan(d + x*e))**n
                                                yield 21, subst2
                                        subjects441.appendleft(tmp456)
                        subjects443.appendleft(tmp453)
                    subjects441.appendleft(tmp442)
                if len(subjects441) >= 1 and isinstance(subjects441[0], cos):
                    tmp457 = subjects441.popleft()
                    subjects458 = deque(tmp457._args)
                    # State 95374
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 95375
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95376
                            if len(subjects458) >= 1:
                                tmp461 = subjects458.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.0', tmp461)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 95377
                                    if len(subjects458) == 0:
                                        pass
                                        # State 95378
                                        if len(subjects441) >= 1 and subjects441[0] == Integer(-1):
                                            tmp463 = subjects441.popleft()
                                            # State 95379
                                            if len(subjects441) == 0:
                                                pass
                                                # State 95380
                                                if len(subjects) == 0:
                                                    pass
                                                    # 27: (1/cos(d + x*e))**n
                                                    yield 27, subst4
                                            subjects441.appendleft(tmp463)
                                subjects458.appendleft(tmp461)
                        if len(subjects458) >= 1 and isinstance(subjects458[0], Mul):
                            tmp464 = subjects458.popleft()
                            associative1 = tmp464
                            associative_type1 = type(tmp464)
                            subjects465 = deque(tmp464._args)
                            matcher = CommutativeMatcher95382.get()
                            tmp466 = subjects465
                            subjects465 = []
                            for s in tmp466:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp466, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95383
                                    if len(subjects458) == 0:
                                        pass
                                        # State 95384
                                        if len(subjects441) >= 1 and subjects441[0] == Integer(-1):
                                            tmp467 = subjects441.popleft()
                                            # State 95385
                                            if len(subjects441) == 0:
                                                pass
                                                # State 95386
                                                if len(subjects) == 0:
                                                    pass
                                                    # 27: (1/cos(d + x*e))**n
                                                    yield 27, subst3
                                            subjects441.appendleft(tmp467)
                            subjects458.appendleft(tmp464)
                    if len(subjects458) >= 1 and isinstance(subjects458[0], Add):
                        tmp468 = subjects458.popleft()
                        associative1 = tmp468
                        associative_type1 = type(tmp468)
                        subjects469 = deque(tmp468._args)
                        matcher = CommutativeMatcher95388.get()
                        tmp470 = subjects469
                        subjects469 = []
                        for s in tmp470:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp470, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 95394
                                if len(subjects458) == 0:
                                    pass
                                    # State 95395
                                    if len(subjects441) >= 1 and subjects441[0] == Integer(-1):
                                        tmp471 = subjects441.popleft()
                                        # State 95396
                                        if len(subjects441) == 0:
                                            pass
                                            # State 95397
                                            if len(subjects) == 0:
                                                pass
                                                # 27: (1/cos(d + x*e))**n
                                                yield 27, subst2
                                        subjects441.appendleft(tmp471)
                        subjects458.appendleft(tmp468)
                    subjects441.appendleft(tmp457)
                if len(subjects441) >= 1 and isinstance(subjects441[0], sin):
                    tmp472 = subjects441.popleft()
                    subjects473 = deque(tmp472._args)
                    # State 95770
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 95771
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95772
                            if len(subjects473) >= 1:
                                tmp476 = subjects473.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.0', tmp476)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 95773
                                    if len(subjects473) == 0:
                                        pass
                                        # State 95774
                                        if len(subjects441) >= 1 and subjects441[0] == Integer(-1):
                                            tmp478 = subjects441.popleft()
                                            # State 95775
                                            if len(subjects441) == 0:
                                                pass
                                                # State 95776
                                                if len(subjects) == 0:
                                                    pass
                                                    # 29: (1/sin(d + x*e))**n
                                                    yield 29, subst4
                                            subjects441.appendleft(tmp478)
                                subjects473.appendleft(tmp476)
                        if len(subjects473) >= 1 and isinstance(subjects473[0], Mul):
                            tmp479 = subjects473.popleft()
                            associative1 = tmp479
                            associative_type1 = type(tmp479)
                            subjects480 = deque(tmp479._args)
                            matcher = CommutativeMatcher95778.get()
                            tmp481 = subjects480
                            subjects480 = []
                            for s in tmp481:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp481, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95779
                                    if len(subjects473) == 0:
                                        pass
                                        # State 95780
                                        if len(subjects441) >= 1 and subjects441[0] == Integer(-1):
                                            tmp482 = subjects441.popleft()
                                            # State 95781
                                            if len(subjects441) == 0:
                                                pass
                                                # State 95782
                                                if len(subjects) == 0:
                                                    pass
                                                    # 29: (1/sin(d + x*e))**n
                                                    yield 29, subst3
                                            subjects441.appendleft(tmp482)
                            subjects473.appendleft(tmp479)
                    if len(subjects473) >= 1 and isinstance(subjects473[0], Add):
                        tmp483 = subjects473.popleft()
                        associative1 = tmp483
                        associative_type1 = type(tmp483)
                        subjects484 = deque(tmp483._args)
                        matcher = CommutativeMatcher95784.get()
                        tmp485 = subjects484
                        subjects484 = []
                        for s in tmp485:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp485, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 95790
                                if len(subjects473) == 0:
                                    pass
                                    # State 95791
                                    if len(subjects441) >= 1 and subjects441[0] == Integer(-1):
                                        tmp486 = subjects441.popleft()
                                        # State 95792
                                        if len(subjects441) == 0:
                                            pass
                                            # State 95793
                                            if len(subjects) == 0:
                                                pass
                                                # 29: (1/sin(d + x*e))**n
                                                yield 29, subst2
                                        subjects441.appendleft(tmp486)
                        subjects473.appendleft(tmp483)
                    subjects441.appendleft(tmp472)
                subjects.appendleft(tmp440)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.5_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 83770
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp488 = subjects.popleft()
                subjects489 = deque(tmp488._args)
                # State 83771
                if len(subjects489) >= 1 and isinstance(subjects489[0], tan):
                    tmp490 = subjects489.popleft()
                    subjects491 = deque(tmp490._args)
                    # State 83772
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83773
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83774
                            if len(subjects491) >= 1:
                                tmp494 = subjects491.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.0', tmp494)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83775
                                    if len(subjects491) == 0:
                                        pass
                                        # State 83776
                                        if len(subjects489) >= 1 and subjects489[0] == Integer(-1):
                                            tmp496 = subjects489.popleft()
                                            # State 83777
                                            if len(subjects489) == 0:
                                                pass
                                                # State 83778
                                                if len(subjects) == 0:
                                                    pass
                                                    # 22: (1/tan(d + x*e))**n2
                                                    yield 22, subst4
                                            subjects489.appendleft(tmp496)
                                subjects491.appendleft(tmp494)
                        if len(subjects491) >= 1 and isinstance(subjects491[0], Mul):
                            tmp497 = subjects491.popleft()
                            associative1 = tmp497
                            associative_type1 = type(tmp497)
                            subjects498 = deque(tmp497._args)
                            matcher = CommutativeMatcher83780.get()
                            tmp499 = subjects498
                            subjects498 = []
                            for s in tmp499:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp499, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83781
                                    if len(subjects491) == 0:
                                        pass
                                        # State 83782
                                        if len(subjects489) >= 1 and subjects489[0] == Integer(-1):
                                            tmp500 = subjects489.popleft()
                                            # State 83783
                                            if len(subjects489) == 0:
                                                pass
                                                # State 83784
                                                if len(subjects) == 0:
                                                    pass
                                                    # 22: (1/tan(d + x*e))**n2
                                                    yield 22, subst3
                                            subjects489.appendleft(tmp500)
                            subjects491.appendleft(tmp497)
                    if len(subjects491) >= 1 and isinstance(subjects491[0], Add):
                        tmp501 = subjects491.popleft()
                        associative1 = tmp501
                        associative_type1 = type(tmp501)
                        subjects502 = deque(tmp501._args)
                        matcher = CommutativeMatcher83786.get()
                        tmp503 = subjects502
                        subjects502 = []
                        for s in tmp503:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp503, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83792
                                if len(subjects491) == 0:
                                    pass
                                    # State 83793
                                    if len(subjects489) >= 1 and subjects489[0] == Integer(-1):
                                        tmp504 = subjects489.popleft()
                                        # State 83794
                                        if len(subjects489) == 0:
                                            pass
                                            # State 83795
                                            if len(subjects) == 0:
                                                pass
                                                # 22: (1/tan(d + x*e))**n2
                                                yield 22, subst2
                                        subjects489.appendleft(tmp504)
                        subjects491.appendleft(tmp501)
                    subjects489.appendleft(tmp490)
                if len(subjects489) >= 1 and isinstance(subjects489[0], cos):
                    tmp505 = subjects489.popleft()
                    subjects506 = deque(tmp505._args)
                    # State 95483
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 95484
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95485
                            if len(subjects506) >= 1:
                                tmp509 = subjects506.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.0', tmp509)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 95486
                                    if len(subjects506) == 0:
                                        pass
                                        # State 95487
                                        if len(subjects489) >= 1 and subjects489[0] == Integer(-1):
                                            tmp511 = subjects489.popleft()
                                            # State 95488
                                            if len(subjects489) == 0:
                                                pass
                                                # State 95489
                                                if len(subjects) == 0:
                                                    pass
                                                    # 28: (1/cos(d + x*e))**n2
                                                    yield 28, subst4
                                            subjects489.appendleft(tmp511)
                                subjects506.appendleft(tmp509)
                        if len(subjects506) >= 1 and isinstance(subjects506[0], Mul):
                            tmp512 = subjects506.popleft()
                            associative1 = tmp512
                            associative_type1 = type(tmp512)
                            subjects513 = deque(tmp512._args)
                            matcher = CommutativeMatcher95491.get()
                            tmp514 = subjects513
                            subjects513 = []
                            for s in tmp514:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp514, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95492
                                    if len(subjects506) == 0:
                                        pass
                                        # State 95493
                                        if len(subjects489) >= 1 and subjects489[0] == Integer(-1):
                                            tmp515 = subjects489.popleft()
                                            # State 95494
                                            if len(subjects489) == 0:
                                                pass
                                                # State 95495
                                                if len(subjects) == 0:
                                                    pass
                                                    # 28: (1/cos(d + x*e))**n2
                                                    yield 28, subst3
                                            subjects489.appendleft(tmp515)
                            subjects506.appendleft(tmp512)
                    if len(subjects506) >= 1 and isinstance(subjects506[0], Add):
                        tmp516 = subjects506.popleft()
                        associative1 = tmp516
                        associative_type1 = type(tmp516)
                        subjects517 = deque(tmp516._args)
                        matcher = CommutativeMatcher95497.get()
                        tmp518 = subjects517
                        subjects517 = []
                        for s in tmp518:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp518, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 95503
                                if len(subjects506) == 0:
                                    pass
                                    # State 95504
                                    if len(subjects489) >= 1 and subjects489[0] == Integer(-1):
                                        tmp519 = subjects489.popleft()
                                        # State 95505
                                        if len(subjects489) == 0:
                                            pass
                                            # State 95506
                                            if len(subjects) == 0:
                                                pass
                                                # 28: (1/cos(d + x*e))**n2
                                                yield 28, subst2
                                        subjects489.appendleft(tmp519)
                        subjects506.appendleft(tmp516)
                    subjects489.appendleft(tmp505)
                if len(subjects489) >= 1 and isinstance(subjects489[0], sin):
                    tmp520 = subjects489.popleft()
                    subjects521 = deque(tmp520._args)
                    # State 95879
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 95880
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95881
                            if len(subjects521) >= 1:
                                tmp524 = subjects521.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.0', tmp524)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 95882
                                    if len(subjects521) == 0:
                                        pass
                                        # State 95883
                                        if len(subjects489) >= 1 and subjects489[0] == Integer(-1):
                                            tmp526 = subjects489.popleft()
                                            # State 95884
                                            if len(subjects489) == 0:
                                                pass
                                                # State 95885
                                                if len(subjects) == 0:
                                                    pass
                                                    # 30: (1/sin(d + x*e))**n2
                                                    yield 30, subst4
                                            subjects489.appendleft(tmp526)
                                subjects521.appendleft(tmp524)
                        if len(subjects521) >= 1 and isinstance(subjects521[0], Mul):
                            tmp527 = subjects521.popleft()
                            associative1 = tmp527
                            associative_type1 = type(tmp527)
                            subjects528 = deque(tmp527._args)
                            matcher = CommutativeMatcher95887.get()
                            tmp529 = subjects528
                            subjects528 = []
                            for s in tmp529:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp529, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95888
                                    if len(subjects521) == 0:
                                        pass
                                        # State 95889
                                        if len(subjects489) >= 1 and subjects489[0] == Integer(-1):
                                            tmp530 = subjects489.popleft()
                                            # State 95890
                                            if len(subjects489) == 0:
                                                pass
                                                # State 95891
                                                if len(subjects) == 0:
                                                    pass
                                                    # 30: (1/sin(d + x*e))**n2
                                                    yield 30, subst3
                                            subjects489.appendleft(tmp530)
                            subjects521.appendleft(tmp527)
                    if len(subjects521) >= 1 and isinstance(subjects521[0], Add):
                        tmp531 = subjects521.popleft()
                        associative1 = tmp531
                        associative_type1 = type(tmp531)
                        subjects532 = deque(tmp531._args)
                        matcher = CommutativeMatcher95893.get()
                        tmp533 = subjects532
                        subjects532 = []
                        for s in tmp533:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp533, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 95899
                                if len(subjects521) == 0:
                                    pass
                                    # State 95900
                                    if len(subjects489) >= 1 and subjects489[0] == Integer(-1):
                                        tmp534 = subjects489.popleft()
                                        # State 95901
                                        if len(subjects489) == 0:
                                            pass
                                            # State 95902
                                            if len(subjects) == 0:
                                                pass
                                                # 30: (1/sin(d + x*e))**n2
                                                yield 30, subst2
                                        subjects489.appendleft(tmp534)
                        subjects521.appendleft(tmp531)
                    subjects489.appendleft(tmp520)
                subjects.appendleft(tmp488)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp535 = subjects.popleft()
            subjects536 = deque(tmp535._args)
            # State 52138
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 52139
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 52140
                    if len(subjects536) >= 1 and isinstance(subjects536[0], Add):
                        tmp539 = subjects536.popleft()
                        associative1 = tmp539
                        associative_type1 = type(tmp539)
                        subjects540 = deque(tmp539._args)
                        matcher = CommutativeMatcher52142.get()
                        tmp541 = subjects540
                        subjects540 = []
                        for s in tmp541:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp541, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 52189
                                if len(subjects536) == 0:
                                    pass
                                    # State 52190
                                    if len(subjects) == 0:
                                        pass
                                        # 9: log(c*(d + e/(f + x*g))**p)
                                        yield 9, subst3
                        subjects536.appendleft(tmp539)
                    if len(subjects536) >= 1:
                        tmp542 = subjects536.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1', tmp542)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53126
                            if len(subjects536) == 0:
                                pass
                                # State 53127
                                if len(subjects) == 0:
                                    pass
                                    # 10: log(c*RFx**p)
                                    yield 10, subst3
                        subjects536.appendleft(tmp542)
                if len(subjects536) >= 1 and isinstance(subjects536[0], Pow):
                    tmp544 = subjects536.popleft()
                    subjects545 = deque(tmp544._args)
                    # State 52191
                    if len(subjects545) >= 1 and isinstance(subjects545[0], Add):
                        tmp546 = subjects545.popleft()
                        associative1 = tmp546
                        associative_type1 = type(tmp546)
                        subjects547 = deque(tmp546._args)
                        matcher = CommutativeMatcher52193.get()
                        tmp548 = subjects547
                        subjects547 = []
                        for s in tmp548:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp548, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 52240
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 52241
                                    if len(subjects545) == 0:
                                        pass
                                        # State 52242
                                        if len(subjects536) == 0:
                                            pass
                                            # State 52243
                                            if len(subjects) == 0:
                                                pass
                                                # 9: log(c*(d + e/(f + x*g))**p)
                                                yield 9, subst3
                                if len(subjects545) >= 1:
                                    tmp550 = []
                                    tmp550.append(subjects545.popleft())
                                    while True:
                                        if len(tmp550) > 1:
                                            tmp551 = create_operation_expression(associative1, tmp550)
                                        elif len(tmp550) == 1:
                                            tmp551 = tmp550[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2.2', tmp551)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 52241
                                            if len(subjects545) == 0:
                                                pass
                                                # State 52242
                                                if len(subjects536) == 0:
                                                    pass
                                                    # State 52243
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 9: log(c*(d + e/(f + x*g))**p)
                                                        yield 9, subst3
                                        if len(subjects545) == 0:
                                            break
                                        tmp550.append(subjects545.popleft())
                                    subjects545.extendleft(reversed(tmp550))
                        subjects545.appendleft(tmp546)
                    if len(subjects545) >= 1:
                        tmp553 = subjects545.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.1', tmp553)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53128
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53129
                                if len(subjects545) == 0:
                                    pass
                                    # State 53130
                                    if len(subjects536) == 0:
                                        pass
                                        # State 53131
                                        if len(subjects) == 0:
                                            pass
                                            # 10: log(c*RFx**p)
                                            yield 10, subst3
                            if len(subjects545) >= 1:
                                tmp556 = subjects545.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', tmp556)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53129
                                    if len(subjects545) == 0:
                                        pass
                                        # State 53130
                                        if len(subjects536) == 0:
                                            pass
                                            # State 53131
                                            if len(subjects) == 0:
                                                pass
                                                # 10: log(c*RFx**p)
                                                yield 10, subst3
                                subjects545.appendleft(tmp556)
                        subjects545.appendleft(tmp553)
                    subjects536.appendleft(tmp544)
            if len(subjects536) >= 1 and isinstance(subjects536[0], Mul):
                tmp558 = subjects536.popleft()
                associative1 = tmp558
                associative_type1 = type(tmp558)
                subjects559 = deque(tmp558._args)
                matcher = CommutativeMatcher52245.get()
                tmp560 = subjects559
                subjects559 = []
                for s in tmp560:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp560, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 52348
                        if len(subjects536) == 0:
                            pass
                            # State 52349
                            if len(subjects) == 0:
                                pass
                                # 9: log(c*(d + e/(f + x*g))**p)
                                yield 9, subst1
                    if pattern_index == 1:
                        pass
                        # State 53136
                        if len(subjects536) == 0:
                            pass
                            # State 53137
                            if len(subjects) == 0:
                                pass
                                # 10: log(c*RFx**p)
                                yield 10, subst1
                subjects536.appendleft(tmp558)
            subjects.appendleft(tmp535)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp561 = subjects.popleft()
            subjects562 = deque(tmp561._args)
            # State 73012
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 73013
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 73014
                    if len(subjects562) >= 1 and isinstance(subjects562[0], Pow):
                        tmp565 = subjects562.popleft()
                        subjects566 = deque(tmp565._args)
                        # State 73015
                        if len(subjects566) >= 1:
                            tmp567 = subjects566.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp567)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 73016
                                if len(subjects566) >= 1:
                                    tmp569 = subjects566.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp569)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 73017
                                        if len(subjects566) == 0:
                                            pass
                                            # State 73018
                                            if len(subjects562) == 0:
                                                pass
                                                # State 73019
                                                if len(subjects) == 0:
                                                    pass
                                                    # 15: sin(c + d*x**n)
                                                    yield 15, subst4
                                    subjects566.appendleft(tmp569)
                            subjects566.appendleft(tmp567)
                        subjects562.appendleft(tmp565)
                if len(subjects562) >= 1 and isinstance(subjects562[0], Mul):
                    tmp571 = subjects562.popleft()
                    associative1 = tmp571
                    associative_type1 = type(tmp571)
                    subjects572 = deque(tmp571._args)
                    matcher = CommutativeMatcher73021.get()
                    tmp573 = subjects572
                    subjects572 = []
                    for s in tmp573:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp573, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 73026
                            if len(subjects562) == 0:
                                pass
                                # State 73027
                                if len(subjects) == 0:
                                    pass
                                    # 15: sin(c + d*x**n)
                                    yield 15, subst2
                    subjects562.appendleft(tmp571)
            if len(subjects562) >= 1:
                tmp574 = subjects562.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp574)
                except ValueError:
                    pass
                else:
                    pass
                    # State 73512
                    if len(subjects562) == 0:
                        pass
                        # State 73513
                        if len(subjects) == 0:
                            pass
                            # 17: sin(u)
                            yield 17, subst1
                subjects562.appendleft(tmp574)
            if len(subjects562) >= 1 and isinstance(subjects562[0], Add):
                tmp576 = subjects562.popleft()
                associative1 = tmp576
                associative_type1 = type(tmp576)
                subjects577 = deque(tmp576._args)
                matcher = CommutativeMatcher73029.get()
                tmp578 = subjects577
                subjects577 = []
                for s in tmp578:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp578, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 73042
                        if len(subjects562) == 0:
                            pass
                            # State 73043
                            if len(subjects) == 0:
                                pass
                                # 15: sin(c + d*x**n)
                                yield 15, subst1
                subjects562.appendleft(tmp576)
            subjects.appendleft(tmp561)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp579 = subjects.popleft()
            subjects580 = deque(tmp579._args)
            # State 73179
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 73180
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 73181
                    if len(subjects580) >= 1 and isinstance(subjects580[0], Pow):
                        tmp583 = subjects580.popleft()
                        subjects584 = deque(tmp583._args)
                        # State 73182
                        if len(subjects584) >= 1:
                            tmp585 = subjects584.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp585)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 73183
                                if len(subjects584) >= 1:
                                    tmp587 = subjects584.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp587)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 73184
                                        if len(subjects584) == 0:
                                            pass
                                            # State 73185
                                            if len(subjects580) == 0:
                                                pass
                                                # State 73186
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: cos(c + d*x**n)
                                                    yield 16, subst4
                                    subjects584.appendleft(tmp587)
                            subjects584.appendleft(tmp585)
                        subjects580.appendleft(tmp583)
                if len(subjects580) >= 1 and isinstance(subjects580[0], Mul):
                    tmp589 = subjects580.popleft()
                    associative1 = tmp589
                    associative_type1 = type(tmp589)
                    subjects590 = deque(tmp589._args)
                    matcher = CommutativeMatcher73188.get()
                    tmp591 = subjects590
                    subjects590 = []
                    for s in tmp591:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp591, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 73193
                            if len(subjects580) == 0:
                                pass
                                # State 73194
                                if len(subjects) == 0:
                                    pass
                                    # 16: cos(c + d*x**n)
                                    yield 16, subst2
                    subjects580.appendleft(tmp589)
            if len(subjects580) >= 1:
                tmp592 = subjects580.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp592)
                except ValueError:
                    pass
                else:
                    pass
                    # State 73552
                    if len(subjects580) == 0:
                        pass
                        # State 73553
                        if len(subjects) == 0:
                            pass
                            # 18: cos(u)
                            yield 18, subst1
                subjects580.appendleft(tmp592)
            if len(subjects580) >= 1 and isinstance(subjects580[0], Add):
                tmp594 = subjects580.popleft()
                associative1 = tmp594
                associative_type1 = type(tmp594)
                subjects595 = deque(tmp594._args)
                matcher = CommutativeMatcher73196.get()
                tmp596 = subjects595
                subjects595 = []
                for s in tmp596:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp596, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 73209
                        if len(subjects580) == 0:
                            pass
                            # State 73210
                            if len(subjects) == 0:
                                pass
                                # 16: cos(c + d*x**n)
                                yield 16, subst1
                subjects580.appendleft(tmp594)
            subjects.appendleft(tmp579)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp597 = subjects.popleft()
            subjects598 = deque(tmp597._args)
            # State 87192
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 87193
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 87194
                    if len(subjects598) >= 1 and isinstance(subjects598[0], Pow):
                        tmp601 = subjects598.popleft()
                        subjects602 = deque(tmp601._args)
                        # State 87195
                        if len(subjects602) >= 1:
                            tmp603 = subjects602.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp603)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 87196
                                if len(subjects602) >= 1:
                                    tmp605 = subjects602.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp605)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 87197
                                        if len(subjects602) == 0:
                                            pass
                                            # State 87198
                                            if len(subjects598) == 0:
                                                pass
                                                # State 87199
                                                if len(subjects) == 0:
                                                    pass
                                                    # 23: tan(c + d*x**n)
                                                    yield 23, subst4
                                    subjects602.appendleft(tmp605)
                            subjects602.appendleft(tmp603)
                        subjects598.appendleft(tmp601)
                if len(subjects598) >= 1 and isinstance(subjects598[0], Mul):
                    tmp607 = subjects598.popleft()
                    associative1 = tmp607
                    associative_type1 = type(tmp607)
                    subjects608 = deque(tmp607._args)
                    matcher = CommutativeMatcher87201.get()
                    tmp609 = subjects608
                    subjects608 = []
                    for s in tmp609:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp609, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 87206
                            if len(subjects598) == 0:
                                pass
                                # State 87207
                                if len(subjects) == 0:
                                    pass
                                    # 23: tan(c + d*x**n)
                                    yield 23, subst2
                    subjects598.appendleft(tmp607)
            if len(subjects598) >= 1:
                tmp610 = subjects598.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp610)
                except ValueError:
                    pass
                else:
                    pass
                    # State 87850
                    if len(subjects598) == 0:
                        pass
                        # State 87851
                        if len(subjects) == 0:
                            pass
                            # 25: tan(u)
                            yield 25, subst1
                subjects598.appendleft(tmp610)
            if len(subjects598) >= 1 and isinstance(subjects598[0], Add):
                tmp612 = subjects598.popleft()
                associative1 = tmp612
                associative_type1 = type(tmp612)
                subjects613 = deque(tmp612._args)
                matcher = CommutativeMatcher87209.get()
                tmp614 = subjects613
                subjects613 = []
                for s in tmp614:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp614, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 87222
                        if len(subjects598) == 0:
                            pass
                            # State 87223
                            if len(subjects) == 0:
                                pass
                                # 23: tan(c + d*x**n)
                                yield 23, subst1
                subjects598.appendleft(tmp612)
            subjects.appendleft(tmp597)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp615 = subjects.popleft()
            subjects616 = deque(tmp615._args)
            # State 107986
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 107987
                if len(subjects616) >= 1:
                    tmp618 = subjects616.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp618)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 107988
                        if len(subjects616) == 0:
                            pass
                            # State 107989
                            if len(subjects) == 0:
                                pass
                                # 35: asin(x*c)
                                yield 35, subst2
                    subjects616.appendleft(tmp618)
            if len(subjects616) >= 1 and isinstance(subjects616[0], Mul):
                tmp620 = subjects616.popleft()
                associative1 = tmp620
                associative_type1 = type(tmp620)
                subjects621 = deque(tmp620._args)
                matcher = CommutativeMatcher107991.get()
                tmp622 = subjects621
                subjects621 = []
                for s in tmp622:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp622, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 107992
                        if len(subjects616) == 0:
                            pass
                            # State 107993
                            if len(subjects) == 0:
                                pass
                                # 35: asin(x*c)
                                yield 35, subst1
                subjects616.appendleft(tmp620)
            if len(subjects616) >= 1 and isinstance(subjects616[0], Add):
                tmp623 = subjects616.popleft()
                associative1 = tmp623
                associative_type1 = type(tmp623)
                subjects624 = deque(tmp623._args)
                matcher = CommutativeMatcher110287.get()
                tmp625 = subjects624
                subjects624 = []
                for s in tmp625:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp625, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110293
                        if len(subjects616) == 0:
                            pass
                            # State 110294
                            if len(subjects) == 0:
                                pass
                                # 37: asin(c + x*d)
                                yield 37, subst1
                subjects616.appendleft(tmp623)
            subjects.appendleft(tmp615)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp626 = subjects.popleft()
            subjects627 = deque(tmp626._args)
            # State 108080
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108081
                if len(subjects627) >= 1:
                    tmp629 = subjects627.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp629)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108082
                        if len(subjects627) == 0:
                            pass
                            # State 108083
                            if len(subjects) == 0:
                                pass
                                # 36: acos(x*c)
                                yield 36, subst2
                    subjects627.appendleft(tmp629)
            if len(subjects627) >= 1 and isinstance(subjects627[0], Mul):
                tmp631 = subjects627.popleft()
                associative1 = tmp631
                associative_type1 = type(tmp631)
                subjects632 = deque(tmp631._args)
                matcher = CommutativeMatcher108085.get()
                tmp633 = subjects632
                subjects632 = []
                for s in tmp633:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp633, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108086
                        if len(subjects627) == 0:
                            pass
                            # State 108087
                            if len(subjects) == 0:
                                pass
                                # 36: acos(x*c)
                                yield 36, subst1
                subjects627.appendleft(tmp631)
            if len(subjects627) >= 1 and isinstance(subjects627[0], Add):
                tmp634 = subjects627.popleft()
                associative1 = tmp634
                associative_type1 = type(tmp634)
                subjects635 = deque(tmp634._args)
                matcher = CommutativeMatcher110383.get()
                tmp636 = subjects635
                subjects635 = []
                for s in tmp636:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp636, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110389
                        if len(subjects627) == 0:
                            pass
                            # State 110390
                            if len(subjects) == 0:
                                pass
                                # 38: acos(c + x*d)
                                yield 38, subst1
                subjects627.appendleft(tmp634)
            subjects.appendleft(tmp626)
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp637 = subjects.popleft()
            subjects638 = deque(tmp637._args)
            # State 112621
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 112622
                if len(subjects638) >= 1:
                    tmp640 = subjects638.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp640)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112623
                        if len(subjects638) == 0:
                            pass
                            # State 112624
                            if len(subjects) == 0:
                                pass
                                # 39: atan(x*c)
                                yield 39, subst2
                    subjects638.appendleft(tmp640)
            if len(subjects638) >= 1 and isinstance(subjects638[0], Mul):
                tmp642 = subjects638.popleft()
                associative1 = tmp642
                associative_type1 = type(tmp642)
                subjects643 = deque(tmp642._args)
                matcher = CommutativeMatcher112626.get()
                tmp644 = subjects643
                subjects643 = []
                for s in tmp644:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp644, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 112627
                        if len(subjects638) == 0:
                            pass
                            # State 112628
                            if len(subjects) == 0:
                                pass
                                # 39: atan(x*c)
                                yield 39, subst1
                subjects638.appendleft(tmp642)
            if len(subjects638) >= 1 and isinstance(subjects638[0], Add):
                tmp645 = subjects638.popleft()
                associative1 = tmp645
                associative_type1 = type(tmp645)
                subjects646 = deque(tmp645._args)
                matcher = CommutativeMatcher115485.get()
                tmp647 = subjects646
                subjects646 = []
                for s in tmp647:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp647, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115491
                        if len(subjects638) == 0:
                            pass
                            # State 115492
                            if len(subjects) == 0:
                                pass
                                # 41: atan(c + x*d)
                                yield 41, subst1
                subjects638.appendleft(tmp645)
            subjects.appendleft(tmp637)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp648 = subjects.popleft()
            subjects649 = deque(tmp648._args)
            # State 112715
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 112716
                if len(subjects649) >= 1:
                    tmp651 = subjects649.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp651)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112717
                        if len(subjects649) == 0:
                            pass
                            # State 112718
                            if len(subjects) == 0:
                                pass
                                # 40: acot(x*c)
                                yield 40, subst2
                    subjects649.appendleft(tmp651)
            if len(subjects649) >= 1 and isinstance(subjects649[0], Mul):
                tmp653 = subjects649.popleft()
                associative1 = tmp653
                associative_type1 = type(tmp653)
                subjects654 = deque(tmp653._args)
                matcher = CommutativeMatcher112720.get()
                tmp655 = subjects654
                subjects654 = []
                for s in tmp655:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp655, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 112721
                        if len(subjects649) == 0:
                            pass
                            # State 112722
                            if len(subjects) == 0:
                                pass
                                # 40: acot(x*c)
                                yield 40, subst1
                subjects649.appendleft(tmp653)
            if len(subjects649) >= 1 and isinstance(subjects649[0], Add):
                tmp656 = subjects649.popleft()
                associative1 = tmp656
                associative_type1 = type(tmp656)
                subjects657 = deque(tmp656._args)
                matcher = CommutativeMatcher115581.get()
                tmp658 = subjects657
                subjects657 = []
                for s in tmp658:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp658, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115587
                        if len(subjects649) == 0:
                            pass
                            # State 115588
                            if len(subjects) == 0:
                                pass
                                # 42: acot(c + x*d)
                                yield 42, subst1
                subjects649.appendleft(tmp656)
            subjects.appendleft(tmp648)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp659 = subjects.popleft()
            subjects660 = deque(tmp659._args)
            # State 122873
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 122874
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122875
                    if len(subjects660) >= 1 and isinstance(subjects660[0], Pow):
                        tmp663 = subjects660.popleft()
                        subjects664 = deque(tmp663._args)
                        # State 122876
                        if len(subjects664) >= 1:
                            tmp665 = subjects664.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp665)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 122877
                                if len(subjects664) >= 1:
                                    tmp667 = subjects664.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp667)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 122878
                                        if len(subjects664) == 0:
                                            pass
                                            # State 122879
                                            if len(subjects660) == 0:
                                                pass
                                                # State 122880
                                                if len(subjects) == 0:
                                                    pass
                                                    # 43: sinh(c + d*x**n)
                                                    yield 43, subst4
                                    subjects664.appendleft(tmp667)
                            subjects664.appendleft(tmp665)
                        subjects660.appendleft(tmp663)
                if len(subjects660) >= 1 and isinstance(subjects660[0], Mul):
                    tmp669 = subjects660.popleft()
                    associative1 = tmp669
                    associative_type1 = type(tmp669)
                    subjects670 = deque(tmp669._args)
                    matcher = CommutativeMatcher122882.get()
                    tmp671 = subjects670
                    subjects670 = []
                    for s in tmp671:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp671, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122887
                            if len(subjects660) == 0:
                                pass
                                # State 122888
                                if len(subjects) == 0:
                                    pass
                                    # 43: sinh(c + d*x**n)
                                    yield 43, subst2
                    subjects660.appendleft(tmp669)
            if len(subjects660) >= 1:
                tmp672 = subjects660.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp672)
                except ValueError:
                    pass
                else:
                    pass
                    # State 123373
                    if len(subjects660) == 0:
                        pass
                        # State 123374
                        if len(subjects) == 0:
                            pass
                            # 45: sinh(u)
                            yield 45, subst1
                subjects660.appendleft(tmp672)
            if len(subjects660) >= 1 and isinstance(subjects660[0], Add):
                tmp674 = subjects660.popleft()
                associative1 = tmp674
                associative_type1 = type(tmp674)
                subjects675 = deque(tmp674._args)
                matcher = CommutativeMatcher122890.get()
                tmp676 = subjects675
                subjects675 = []
                for s in tmp676:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp676, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 122903
                        if len(subjects660) == 0:
                            pass
                            # State 122904
                            if len(subjects) == 0:
                                pass
                                # 43: sinh(c + d*x**n)
                                yield 43, subst1
                subjects660.appendleft(tmp674)
            subjects.appendleft(tmp659)
        if len(subjects) >= 1 and isinstance(subjects[0], cosh):
            tmp677 = subjects.popleft()
            subjects678 = deque(tmp677._args)
            # State 123040
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 123041
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 123042
                    if len(subjects678) >= 1 and isinstance(subjects678[0], Pow):
                        tmp681 = subjects678.popleft()
                        subjects682 = deque(tmp681._args)
                        # State 123043
                        if len(subjects682) >= 1:
                            tmp683 = subjects682.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp683)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 123044
                                if len(subjects682) >= 1:
                                    tmp685 = subjects682.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp685)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 123045
                                        if len(subjects682) == 0:
                                            pass
                                            # State 123046
                                            if len(subjects678) == 0:
                                                pass
                                                # State 123047
                                                if len(subjects) == 0:
                                                    pass
                                                    # 44: cosh(c + d*x**n)
                                                    yield 44, subst4
                                    subjects682.appendleft(tmp685)
                            subjects682.appendleft(tmp683)
                        subjects678.appendleft(tmp681)
                if len(subjects678) >= 1 and isinstance(subjects678[0], Mul):
                    tmp687 = subjects678.popleft()
                    associative1 = tmp687
                    associative_type1 = type(tmp687)
                    subjects688 = deque(tmp687._args)
                    matcher = CommutativeMatcher123049.get()
                    tmp689 = subjects688
                    subjects688 = []
                    for s in tmp689:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp689, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 123054
                            if len(subjects678) == 0:
                                pass
                                # State 123055
                                if len(subjects) == 0:
                                    pass
                                    # 44: cosh(c + d*x**n)
                                    yield 44, subst2
                    subjects678.appendleft(tmp687)
            if len(subjects678) >= 1:
                tmp690 = subjects678.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp690)
                except ValueError:
                    pass
                else:
                    pass
                    # State 123413
                    if len(subjects678) == 0:
                        pass
                        # State 123414
                        if len(subjects) == 0:
                            pass
                            # 46: cosh(u)
                            yield 46, subst1
                subjects678.appendleft(tmp690)
            if len(subjects678) >= 1 and isinstance(subjects678[0], Add):
                tmp692 = subjects678.popleft()
                associative1 = tmp692
                associative_type1 = type(tmp692)
                subjects693 = deque(tmp692._args)
                matcher = CommutativeMatcher123057.get()
                tmp694 = subjects693
                subjects693 = []
                for s in tmp694:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp694, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 123070
                        if len(subjects678) == 0:
                            pass
                            # State 123071
                            if len(subjects) == 0:
                                pass
                                # 44: cosh(c + d*x**n)
                                yield 44, subst1
                subjects678.appendleft(tmp692)
            subjects.appendleft(tmp677)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp695 = subjects.popleft()
            subjects696 = deque(tmp695._args)
            # State 126639
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 126640
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 126641
                    if len(subjects696) >= 1 and isinstance(subjects696[0], Pow):
                        tmp699 = subjects696.popleft()
                        subjects700 = deque(tmp699._args)
                        # State 126642
                        if len(subjects700) >= 1:
                            tmp701 = subjects700.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp701)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 126643
                                if len(subjects700) >= 1:
                                    tmp703 = subjects700.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp703)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 126644
                                        if len(subjects700) == 0:
                                            pass
                                            # State 126645
                                            if len(subjects696) == 0:
                                                pass
                                                # State 126646
                                                if len(subjects) == 0:
                                                    pass
                                                    # 47: tanh(c + d*x**n)
                                                    yield 47, subst4
                                    subjects700.appendleft(tmp703)
                            subjects700.appendleft(tmp701)
                        subjects696.appendleft(tmp699)
                if len(subjects696) >= 1 and isinstance(subjects696[0], Mul):
                    tmp705 = subjects696.popleft()
                    associative1 = tmp705
                    associative_type1 = type(tmp705)
                    subjects706 = deque(tmp705._args)
                    matcher = CommutativeMatcher126648.get()
                    tmp707 = subjects706
                    subjects706 = []
                    for s in tmp707:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp707, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 126653
                            if len(subjects696) == 0:
                                pass
                                # State 126654
                                if len(subjects) == 0:
                                    pass
                                    # 47: tanh(c + d*x**n)
                                    yield 47, subst2
                    subjects696.appendleft(tmp705)
            if len(subjects696) >= 1:
                tmp708 = subjects696.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp708)
                except ValueError:
                    pass
                else:
                    pass
                    # State 127345
                    if len(subjects696) == 0:
                        pass
                        # State 127346
                        if len(subjects) == 0:
                            pass
                            # 49: tanh(u)
                            yield 49, subst1
                subjects696.appendleft(tmp708)
            if len(subjects696) >= 1 and isinstance(subjects696[0], Add):
                tmp710 = subjects696.popleft()
                associative1 = tmp710
                associative_type1 = type(tmp710)
                subjects711 = deque(tmp710._args)
                matcher = CommutativeMatcher126656.get()
                tmp712 = subjects711
                subjects711 = []
                for s in tmp712:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp712, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 126669
                        if len(subjects696) == 0:
                            pass
                            # State 126670
                            if len(subjects) == 0:
                                pass
                                # 47: tanh(c + d*x**n)
                                yield 47, subst1
                subjects696.appendleft(tmp710)
            subjects.appendleft(tmp695)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp713 = subjects.popleft()
            subjects714 = deque(tmp713._args)
            # State 137725
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 137726
                if len(subjects714) >= 1:
                    tmp716 = subjects714.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp716)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137727
                        if len(subjects714) == 0:
                            pass
                            # State 137728
                            if len(subjects) == 0:
                                pass
                                # 55: asinh(x*c)
                                yield 55, subst2
                    subjects714.appendleft(tmp716)
            if len(subjects714) >= 1 and isinstance(subjects714[0], Mul):
                tmp718 = subjects714.popleft()
                associative1 = tmp718
                associative_type1 = type(tmp718)
                subjects719 = deque(tmp718._args)
                matcher = CommutativeMatcher137730.get()
                tmp720 = subjects719
                subjects719 = []
                for s in tmp720:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp720, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 137731
                        if len(subjects714) == 0:
                            pass
                            # State 137732
                            if len(subjects) == 0:
                                pass
                                # 55: asinh(x*c)
                                yield 55, subst1
                subjects714.appendleft(tmp718)
            if len(subjects714) >= 1 and isinstance(subjects714[0], Add):
                tmp721 = subjects714.popleft()
                associative1 = tmp721
                associative_type1 = type(tmp721)
                subjects722 = deque(tmp721._args)
                matcher = CommutativeMatcher140022.get()
                tmp723 = subjects722
                subjects722 = []
                for s in tmp723:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp723, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 140028
                        if len(subjects714) == 0:
                            pass
                            # State 140029
                            if len(subjects) == 0:
                                pass
                                # 57: asinh(c + x*d)
                                yield 57, subst1
                subjects714.appendleft(tmp721)
            subjects.appendleft(tmp713)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp724 = subjects.popleft()
            subjects725 = deque(tmp724._args)
            # State 137819
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 137820
                if len(subjects725) >= 1:
                    tmp727 = subjects725.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp727)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137821
                        if len(subjects725) == 0:
                            pass
                            # State 137822
                            if len(subjects) == 0:
                                pass
                                # 56: acosh(x*c)
                                yield 56, subst2
                    subjects725.appendleft(tmp727)
            if len(subjects725) >= 1 and isinstance(subjects725[0], Mul):
                tmp729 = subjects725.popleft()
                associative1 = tmp729
                associative_type1 = type(tmp729)
                subjects730 = deque(tmp729._args)
                matcher = CommutativeMatcher137824.get()
                tmp731 = subjects730
                subjects730 = []
                for s in tmp731:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp731, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 137825
                        if len(subjects725) == 0:
                            pass
                            # State 137826
                            if len(subjects) == 0:
                                pass
                                # 56: acosh(x*c)
                                yield 56, subst1
                subjects725.appendleft(tmp729)
            if len(subjects725) >= 1 and isinstance(subjects725[0], Add):
                tmp732 = subjects725.popleft()
                associative1 = tmp732
                associative_type1 = type(tmp732)
                subjects733 = deque(tmp732._args)
                matcher = CommutativeMatcher140118.get()
                tmp734 = subjects733
                subjects733 = []
                for s in tmp734:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp734, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 140124
                        if len(subjects725) == 0:
                            pass
                            # State 140125
                            if len(subjects) == 0:
                                pass
                                # 58: acosh(c + x*d)
                                yield 58, subst1
                subjects725.appendleft(tmp732)
            subjects.appendleft(tmp724)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp735 = subjects.popleft()
            subjects736 = deque(tmp735._args)
            # State 142253
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142254
                if len(subjects736) >= 1:
                    tmp738 = subjects736.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp738)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142255
                        if len(subjects736) == 0:
                            pass
                            # State 142256
                            if len(subjects) == 0:
                                pass
                                # 59: atanh(x*c)
                                yield 59, subst2
                    subjects736.appendleft(tmp738)
            if len(subjects736) >= 1 and isinstance(subjects736[0], Mul):
                tmp740 = subjects736.popleft()
                associative1 = tmp740
                associative_type1 = type(tmp740)
                subjects741 = deque(tmp740._args)
                matcher = CommutativeMatcher142258.get()
                tmp742 = subjects741
                subjects741 = []
                for s in tmp742:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp742, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142259
                        if len(subjects736) == 0:
                            pass
                            # State 142260
                            if len(subjects) == 0:
                                pass
                                # 59: atanh(x*c)
                                yield 59, subst1
                subjects736.appendleft(tmp740)
            if len(subjects736) >= 1 and isinstance(subjects736[0], Add):
                tmp743 = subjects736.popleft()
                associative1 = tmp743
                associative_type1 = type(tmp743)
                subjects744 = deque(tmp743._args)
                matcher = CommutativeMatcher144710.get()
                tmp745 = subjects744
                subjects744 = []
                for s in tmp745:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp745, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144716
                        if len(subjects736) == 0:
                            pass
                            # State 144717
                            if len(subjects) == 0:
                                pass
                                # 61: atanh(c + x*d)
                                yield 61, subst1
                subjects736.appendleft(tmp743)
            subjects.appendleft(tmp735)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp746 = subjects.popleft()
            subjects747 = deque(tmp746._args)
            # State 142347
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142348
                if len(subjects747) >= 1:
                    tmp749 = subjects747.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp749)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142349
                        if len(subjects747) == 0:
                            pass
                            # State 142350
                            if len(subjects) == 0:
                                pass
                                # 60: acoth(x*c)
                                yield 60, subst2
                    subjects747.appendleft(tmp749)
            if len(subjects747) >= 1 and isinstance(subjects747[0], Mul):
                tmp751 = subjects747.popleft()
                associative1 = tmp751
                associative_type1 = type(tmp751)
                subjects752 = deque(tmp751._args)
                matcher = CommutativeMatcher142352.get()
                tmp753 = subjects752
                subjects752 = []
                for s in tmp753:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp753, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142353
                        if len(subjects747) == 0:
                            pass
                            # State 142354
                            if len(subjects) == 0:
                                pass
                                # 60: acoth(x*c)
                                yield 60, subst1
                subjects747.appendleft(tmp751)
            if len(subjects747) >= 1 and isinstance(subjects747[0], Add):
                tmp754 = subjects747.popleft()
                associative1 = tmp754
                associative_type1 = type(tmp754)
                subjects755 = deque(tmp754._args)
                matcher = CommutativeMatcher144806.get()
                tmp756 = subjects755
                subjects755 = []
                for s in tmp756:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp756, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144812
                        if len(subjects747) == 0:
                            pass
                            # State 144813
                            if len(subjects) == 0:
                                pass
                                # 62: acoth(c + x*d)
                                yield 62, subst1
                subjects747.appendleft(tmp754)
            subjects.appendleft(tmp746)
        return
        yield


from .generated_part001396 import *
from .generated_part001521 import *
from .generated_part001427 import *
from .generated_part001532 import *
from .generated_part001530 import *
from .generated_part001512 import *
from collections import deque
from matchpy.utils import VariableWithCount
from .generated_part001411 import *
from .generated_part001505 import *
from .generated_part001436 import *
from .generated_part001415 import *
from .generated_part001515 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part001403 import *
from .generated_part001520 import *
from .generated_part001506 import *
from .generated_part001448 import *
from .generated_part001445 import *
from .generated_part001529 import *
from .generated_part001437 import *
from .generated_part001457 import *
from .generated_part001539 import *
from .generated_part001511 import *
from .generated_part001500 import *
from .generated_part001536 import *
from .generated_part001517 import *
from .generated_part001509 import *
from .generated_part001482 import *
from .generated_part001418 import *
from .generated_part001440 import *
from .generated_part001405 import *
from .generated_part001502 import *
from .generated_part001463 import *
from .generated_part001455 import *
from .generated_part001434 import *
from .generated_part001526 import *
from .generated_part001527 import *
from multiset import Multiset
from .generated_part001443 import *
from .generated_part001429 import *
from .generated_part001461 import *
from .generated_part001409 import *
from .generated_part001431 import *
from .generated_part001439 import *
from .generated_part001402 import *
from .generated_part001433 import *
from .generated_part001449 import *
from .generated_part001421 import *
from .generated_part001466 import *
from .generated_part001420 import *
from .generated_part001414 import *
from .generated_part001446 import *
from .generated_part001458 import *
from .generated_part001464 import *
from .generated_part001408 import *
from .generated_part001533 import *
from .generated_part001423 import *
from .generated_part001452 import *
from .generated_part001474 import *
from .generated_part001406 import *
from .generated_part001523 import *
from .generated_part001451 import *
from .generated_part001535 import *
from .generated_part001503 import *
from .generated_part001514 import *
from .generated_part001442 import *
from .generated_part001412 import *
from .generated_part001454 import *
from .generated_part001508 import *
from .generated_part001430 import *
from .generated_part001538 import *
from .generated_part001460 import *
from .generated_part001395 import *
from .generated_part001417 import *
from .generated_part001424 import *
from .generated_part001499 import *
from .generated_part001426 import *
from .generated_part001524 import *
from .generated_part001518 import *