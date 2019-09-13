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

class CommutativeMatcher8142(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    1: (1, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    2: (2, Multiset({4: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({5: 1, 6: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({7: 1, 8: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({9: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({10: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({11: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({12: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({13: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    10: (10, Multiset({14: 1, 15: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    11: (11, Multiset({16: 1, 17: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    12: (12, Multiset({18: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    13: (13, Multiset({19: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    14: (14, Multiset({20: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    15: (15, Multiset({21: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    16: (16, Multiset({22: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    17: (17, Multiset({23: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    18: (18, Multiset({24: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    19: (19, Multiset({25: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    20: (20, Multiset({26: 1, 27: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    21: (21, Multiset({28: 1, 29: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    22: (22, Multiset({30: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    23: (23, Multiset({31: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    24: (24, Multiset({32: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    25: (25, Multiset({33: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    26: (26, Multiset({34: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    27: (27, Multiset({35: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    28: (28, Multiset({36: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    29: (29, Multiset({37: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    30: (30, Multiset({38: 1, 39: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    31: (31, Multiset({40: 1, 41: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    32: (32, Multiset({42: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    33: (33, Multiset({43: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    34: (34, Multiset({44: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    35: (35, Multiset({45: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    36: (36, Multiset({46: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    37: (37, Multiset({47: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    38: (38, Multiset({48: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    39: (39, Multiset({49: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    40: (40, Multiset({50: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    41: (41, Multiset({51: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    42: (42, Multiset({52: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    43: (43, Multiset({53: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    44: (44, Multiset({54: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    45: (45, Multiset({55: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    46: (46, Multiset({56: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    47: (47, Multiset({57: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    48: (48, Multiset({58: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    49: (49, Multiset({59: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    50: (50, Multiset({60: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    51: (51, Multiset({61: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    52: (52, Multiset({62: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    53: (53, Multiset({63: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    54: (54, Multiset({64: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    55: (55, Multiset({65: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    56: (56, Multiset({66: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    57: (57, Multiset({67: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    58: (58, Multiset({68: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    59: (59, Multiset({69: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    60: (60, Multiset({70: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    61: (61, Multiset({71: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    62: (62, Multiset({72: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    63: (63, Multiset({73: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    64: (64, Multiset({74: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    65: (65, Multiset({75: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    66: (66, Multiset({76: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    67: (67, Multiset({77: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    68: (68, Multiset({78: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    69: (69, Multiset({79: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    70: (70, Multiset({80: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    71: (71, Multiset({81: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    72: (72, Multiset({82: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    73: (73, Multiset({83: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    74: (74, Multiset({84: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    75: (75, Multiset({85: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    76: (76, Multiset({86: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    77: (77, Multiset({87: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    78: (78, Multiset({88: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    79: (79, Multiset({89: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 1
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher8142._instance is None:
            CommutativeMatcher8142._instance = CommutativeMatcher8142()
        return CommutativeMatcher8142._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 8141
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 8143
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 8144
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8145
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 8146
                                if len(subjects3) == 0:
                                    pass
                                    # State 8147
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48) and (cons_f89) and (cons_f465)
                                        # 2: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f587)
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 10000
                    if len(subjects3) >= 1 and isinstance(subjects3[0], Pow):
                        tmp9 = subjects3.popleft()
                        subjects10 = deque(tmp9._args)
                        # State 10001
                        if len(subjects10) >= 1:
                            tmp11 = subjects10.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1', tmp11)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 10002
                                if len(subjects10) >= 1:
                                    tmp13 = subjects10.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.2', tmp13)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 10003
                                        if len(subjects10) == 0:
                                            pass
                                            # State 10004
                                            if len(subjects3) >= 1:
                                                tmp15 = subjects3.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.1.2', tmp15)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 10005
                                                    if len(subjects3) == 0:
                                                        pass
                                                        # State 10006
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: b*(c*x**n)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f52) and (cons_f4) and (cons_f5) and (cons_f800)
                                                subjects3.appendleft(tmp15)
                                    subjects10.appendleft(tmp13)
                                if len(subjects10) >= 1 and subjects10[0] == -1:
                                    tmp17 = subjects10.popleft()
                                    # State 10868
                                    if len(subjects10) == 0:
                                        pass
                                        # State 10869
                                        if len(subjects3) >= 1:
                                            tmp18 = subjects3.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2', tmp18)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 10870
                                                if len(subjects3) == 0:
                                                    pass
                                                    # State 10871
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                                        # 7: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809) and (cons_f810)
                                            subjects3.appendleft(tmp18)
                                    subjects10.appendleft(tmp17)
                            subjects10.appendleft(tmp11)
                        subjects3.appendleft(tmp9)
                if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                    tmp20 = subjects3.popleft()
                    associative1 = tmp20
                    associative_type1 = type(tmp20)
                    subjects21 = deque(tmp20._args)
                    matcher = CommutativeMatcher10008.get()
                    tmp22 = subjects21
                    subjects21 = []
                    for s in tmp22:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp22, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 10013
                            if len(subjects3) >= 1:
                                tmp23 = []
                                tmp23.append(subjects3.popleft())
                                while True:
                                    if len(tmp23) > 1:
                                        tmp24 = create_operation_expression(associative1, tmp23)
                                    elif len(tmp23) == 1:
                                        tmp24 = tmp23[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2', tmp24)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 10014
                                        if len(subjects3) == 0:
                                            pass
                                            # State 10015
                                            if len(subjects) == 0:
                                                pass
                                                # 4: b*(c*x**n)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f52) and (cons_f4) and (cons_f5) and (cons_f800)
                                    if len(subjects3) == 0:
                                        break
                                    tmp23.append(subjects3.popleft())
                                subjects3.extendleft(reversed(tmp23))
                        if pattern_index == 1:
                            pass
                            # State 10874
                            if len(subjects3) >= 1:
                                tmp26 = []
                                tmp26.append(subjects3.popleft())
                                while True:
                                    if len(tmp26) > 1:
                                        tmp27 = create_operation_expression(associative1, tmp26)
                                    elif len(tmp26) == 1:
                                        tmp27 = tmp26[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2', tmp27)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 10875
                                        if len(subjects3) == 0:
                                            pass
                                            # State 10876
                                            if len(subjects) == 0:
                                                pass
                                                # 5: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                                # 7: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809) and (cons_f810)
                                    if len(subjects3) == 0:
                                        break
                                    tmp26.append(subjects3.popleft())
                                subjects3.extendleft(reversed(tmp26))
                    subjects3.appendleft(tmp20)
                if len(subjects3) >= 1 and isinstance(subjects3[0], Add):
                    tmp29 = subjects3.popleft()
                    associative1 = tmp29
                    associative_type1 = type(tmp29)
                    subjects30 = deque(tmp29._args)
                    matcher = CommutativeMatcher13226.get()
                    tmp31 = subjects30
                    subjects30 = []
                    for s in tmp31:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp31, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 13276
                            if len(subjects3) >= 1:
                                tmp32 = []
                                tmp32.append(subjects3.popleft())
                                while True:
                                    if len(tmp32) > 1:
                                        tmp33 = create_operation_expression(associative1, tmp32)
                                    elif len(tmp32) == 1:
                                        tmp33 = tmp32[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2', tmp33)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 13277
                                        if len(subjects3) == 0:
                                            pass
                                            # State 13278
                                            if len(subjects) == 0:
                                                pass
                                                # 9: h*(d + e*x + f*sqrt(a + b*x + c*x**2))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                                    if len(subjects3) == 0:
                                        break
                                    tmp32.append(subjects3.popleft())
                                subjects3.extendleft(reversed(tmp32))
                        if pattern_index == 1:
                            pass
                            # State 13600
                            if len(subjects3) >= 1:
                                tmp35 = []
                                tmp35.append(subjects3.popleft())
                                while True:
                                    if len(tmp35) > 1:
                                        tmp36 = create_operation_expression(associative1, tmp35)
                                    elif len(tmp35) == 1:
                                        tmp36 = tmp35[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2', tmp36)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 13601
                                        if len(subjects3) == 0:
                                            pass
                                            # State 13602
                                            if len(subjects) == 0:
                                                pass
                                                # 10: h*(d + e*x + f*sqrt(a + c*x**2))**n /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                                    if len(subjects3) == 0:
                                        break
                                    tmp35.append(subjects3.popleft())
                                subjects3.extendleft(reversed(tmp35))
                        if pattern_index == 2:
                            pass
                            # State 13704
                            if len(subjects3) >= 1:
                                tmp38 = []
                                tmp38.append(subjects3.popleft())
                                while True:
                                    if len(tmp38) > 1:
                                        tmp39 = create_operation_expression(associative1, tmp38)
                                    elif len(tmp38) == 1:
                                        tmp39 = tmp38[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2', tmp39)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 13705
                                        if len(subjects3) == 0:
                                            pass
                                            # State 13706
                                            if len(subjects) == 0:
                                                pass
                                                # 11: h*(u + f*sqrt(v))**n /; (cons_f127) and (cons_f211) and (cons_f4) and (cons_f70) and (cons_f820) and (cons_f821) and (cons_f1058)
                                    if len(subjects3) == 0:
                                        break
                                    tmp38.append(subjects3.popleft())
                                subjects3.extendleft(reversed(tmp38))
                    subjects3.appendleft(tmp29)
                if len(subjects3) >= 1 and isinstance(subjects3[0], sin):
                    tmp41 = subjects3.popleft()
                    subjects42 = deque(tmp41._args)
                    # State 68752
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 68753
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68754
                            if len(subjects42) >= 1:
                                tmp45 = subjects42.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp45)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 68755
                                    if len(subjects42) == 0:
                                        pass
                                        # State 68756
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.3', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68757
                                            if len(subjects3) == 0:
                                                pass
                                                # State 68758
                                                if len(subjects) == 0:
                                                    pass
                                                    # 14: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        if len(subjects3) >= 1:
                                            tmp48 = subjects3.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3', tmp48)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 68757
                                                if len(subjects3) == 0:
                                                    pass
                                                    # State 68758
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 14: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects3.appendleft(tmp48)
                                subjects42.appendleft(tmp45)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 97811
                            if len(subjects42) >= 1 and isinstance(subjects42[0], Pow):
                                tmp51 = subjects42.popleft()
                                subjects52 = deque(tmp51._args)
                                # State 97812
                                if len(subjects52) >= 1:
                                    tmp53 = subjects52.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3.1.1', tmp53)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 97813
                                        if len(subjects52) >= 1:
                                            tmp55 = subjects52.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3.1.2', tmp55)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 97814
                                                if len(subjects52) == 0:
                                                    pass
                                                    # State 97815
                                                    if len(subjects42) == 0:
                                                        pass
                                                        # State 97816
                                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                                            tmp57 = subjects3.popleft()
                                                            # State 97817
                                                            if len(subjects3) == 0:
                                                                pass
                                                                # State 97818
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 43: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                    # 45: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                    # 47: b/sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                            subjects3.appendleft(tmp57)
                                            subjects52.appendleft(tmp55)
                                    subjects52.appendleft(tmp53)
                                subjects42.appendleft(tmp51)
                        if len(subjects42) >= 1 and isinstance(subjects42[0], Mul):
                            tmp58 = subjects42.popleft()
                            associative1 = tmp58
                            associative_type1 = type(tmp58)
                            subjects59 = deque(tmp58._args)
                            matcher = CommutativeMatcher68760.get()
                            tmp60 = subjects59
                            subjects59 = []
                            for s in tmp60:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp60, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 68761
                                    if len(subjects42) == 0:
                                        pass
                                        # State 68762
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68763
                                            if len(subjects3) == 0:
                                                pass
                                                # State 68764
                                                if len(subjects) == 0:
                                                    pass
                                                    # 14: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        if len(subjects3) >= 1:
                                            tmp62 = subjects3.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3', tmp62)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 68763
                                                if len(subjects3) == 0:
                                                    pass
                                                    # State 68764
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 14: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects3.appendleft(tmp62)
                                if pattern_index == 1:
                                    pass
                                    # State 97823
                                    if len(subjects42) == 0:
                                        pass
                                        # State 97824
                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                            tmp64 = subjects3.popleft()
                                            # State 97825
                                            if len(subjects3) == 0:
                                                pass
                                                # State 97826
                                                if len(subjects) == 0:
                                                    pass
                                                    # 43: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                    # 45: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    # 47: b/sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            subjects3.appendleft(tmp64)
                            subjects42.appendleft(tmp58)
                    if len(subjects42) >= 1:
                        tmp65 = subjects42.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp65)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 98287
                            if len(subjects42) == 0:
                                pass
                                # State 98288
                                if len(subjects3) >= 1 and subjects3[0] == -1:
                                    tmp67 = subjects3.popleft()
                                    # State 98289
                                    if len(subjects3) == 0:
                                        pass
                                        # State 98290
                                        if len(subjects) == 0:
                                            pass
                                            # 49: b/sin(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                    subjects3.appendleft(tmp67)
                        subjects42.appendleft(tmp65)
                    if len(subjects42) >= 1 and isinstance(subjects42[0], Add):
                        tmp68 = subjects42.popleft()
                        associative1 = tmp68
                        associative_type1 = type(tmp68)
                        subjects69 = deque(tmp68._args)
                        matcher = CommutativeMatcher68766.get()
                        tmp70 = subjects69
                        subjects69 = []
                        for s in tmp70:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp70, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 68772
                                if len(subjects42) == 0:
                                    pass
                                    # State 68773
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 68774
                                        if len(subjects3) == 0:
                                            pass
                                            # State 68775
                                            if len(subjects) == 0:
                                                pass
                                                # 14: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                    if len(subjects3) >= 1:
                                        tmp72 = subjects3.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp72)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68774
                                            if len(subjects3) == 0:
                                                pass
                                                # State 68775
                                                if len(subjects) == 0:
                                                    pass
                                                    # 14: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        subjects3.appendleft(tmp72)
                            if pattern_index == 1:
                                pass
                                # State 97837
                                if len(subjects42) == 0:
                                    pass
                                    # State 97838
                                    if len(subjects3) >= 1 and subjects3[0] == -1:
                                        tmp74 = subjects3.popleft()
                                        # State 97839
                                        if len(subjects3) == 0:
                                            pass
                                            # State 97840
                                            if len(subjects) == 0:
                                                pass
                                                # 43: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                # 45: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                # 47: b/sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        subjects3.appendleft(tmp74)
                        subjects42.appendleft(tmp68)
                    subjects3.appendleft(tmp41)
                if len(subjects3) >= 1 and isinstance(subjects3[0], cos):
                    tmp75 = subjects3.popleft()
                    subjects76 = deque(tmp75._args)
                    # State 69035
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 69036
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 69037
                            if len(subjects76) >= 1:
                                tmp79 = subjects76.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp79)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 69038
                                    if len(subjects76) == 0:
                                        pass
                                        # State 69039
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.3', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69040
                                            if len(subjects3) == 0:
                                                pass
                                                # State 69041
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        if len(subjects3) >= 1:
                                            tmp82 = subjects3.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3', tmp82)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 69040
                                                if len(subjects3) == 0:
                                                    pass
                                                    # State 69041
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 16: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects3.appendleft(tmp82)
                                subjects76.appendleft(tmp79)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 97503
                            if len(subjects76) >= 1 and isinstance(subjects76[0], Pow):
                                tmp85 = subjects76.popleft()
                                subjects86 = deque(tmp85._args)
                                # State 97504
                                if len(subjects86) >= 1:
                                    tmp87 = subjects86.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3.1.1', tmp87)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 97505
                                        if len(subjects86) >= 1:
                                            tmp89 = subjects86.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3.1.2', tmp89)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 97506
                                                if len(subjects86) == 0:
                                                    pass
                                                    # State 97507
                                                    if len(subjects76) == 0:
                                                        pass
                                                        # State 97508
                                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                                            tmp91 = subjects3.popleft()
                                                            # State 97509
                                                            if len(subjects3) == 0:
                                                                pass
                                                                # State 97510
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 42: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                    # 44: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                    # 46: b/cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                            subjects3.appendleft(tmp91)
                                            subjects86.appendleft(tmp89)
                                    subjects86.appendleft(tmp87)
                                subjects76.appendleft(tmp85)
                        if len(subjects76) >= 1 and isinstance(subjects76[0], Mul):
                            tmp92 = subjects76.popleft()
                            associative1 = tmp92
                            associative_type1 = type(tmp92)
                            subjects93 = deque(tmp92._args)
                            matcher = CommutativeMatcher69043.get()
                            tmp94 = subjects93
                            subjects93 = []
                            for s in tmp94:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp94, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 69044
                                    if len(subjects76) == 0:
                                        pass
                                        # State 69045
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69046
                                            if len(subjects3) == 0:
                                                pass
                                                # State 69047
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        if len(subjects3) >= 1:
                                            tmp96 = subjects3.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3', tmp96)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 69046
                                                if len(subjects3) == 0:
                                                    pass
                                                    # State 69047
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 16: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects3.appendleft(tmp96)
                                if pattern_index == 1:
                                    pass
                                    # State 97515
                                    if len(subjects76) == 0:
                                        pass
                                        # State 97516
                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                            tmp98 = subjects3.popleft()
                                            # State 97517
                                            if len(subjects3) == 0:
                                                pass
                                                # State 97518
                                                if len(subjects) == 0:
                                                    pass
                                                    # 42: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                    # 44: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    # 46: b/cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            subjects3.appendleft(tmp98)
                            subjects76.appendleft(tmp92)
                    if len(subjects76) >= 1:
                        tmp99 = subjects76.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp99)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 98231
                            if len(subjects76) == 0:
                                pass
                                # State 98232
                                if len(subjects3) >= 1 and subjects3[0] == -1:
                                    tmp101 = subjects3.popleft()
                                    # State 98233
                                    if len(subjects3) == 0:
                                        pass
                                        # State 98234
                                        if len(subjects) == 0:
                                            pass
                                            # 48: b/cos(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                    subjects3.appendleft(tmp101)
                        subjects76.appendleft(tmp99)
                    if len(subjects76) >= 1 and isinstance(subjects76[0], Add):
                        tmp102 = subjects76.popleft()
                        associative1 = tmp102
                        associative_type1 = type(tmp102)
                        subjects103 = deque(tmp102._args)
                        matcher = CommutativeMatcher69049.get()
                        tmp104 = subjects103
                        subjects103 = []
                        for s in tmp104:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp104, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 69055
                                if len(subjects76) == 0:
                                    pass
                                    # State 69056
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69057
                                        if len(subjects3) == 0:
                                            pass
                                            # State 69058
                                            if len(subjects) == 0:
                                                pass
                                                # 16: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                    if len(subjects3) >= 1:
                                        tmp106 = subjects3.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp106)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69057
                                            if len(subjects3) == 0:
                                                pass
                                                # State 69058
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        subjects3.appendleft(tmp106)
                            if pattern_index == 1:
                                pass
                                # State 97529
                                if len(subjects76) == 0:
                                    pass
                                    # State 97530
                                    if len(subjects3) >= 1 and subjects3[0] == -1:
                                        tmp108 = subjects3.popleft()
                                        # State 97531
                                        if len(subjects3) == 0:
                                            pass
                                            # State 97532
                                            if len(subjects) == 0:
                                                pass
                                                # 42: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                # 44: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                # 46: b/cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        subjects3.appendleft(tmp108)
                        subjects76.appendleft(tmp102)
                    subjects3.appendleft(tmp75)
                if len(subjects3) >= 1 and isinstance(subjects3[0], tan):
                    tmp109 = subjects3.popleft()
                    subjects110 = deque(tmp109._args)
                    # State 83358
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83359
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83360
                            if len(subjects110) >= 1:
                                tmp113 = subjects110.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp113)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83361
                                    if len(subjects110) == 0:
                                        pass
                                        # State 83362
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.3', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83363
                                            if len(subjects3) == 0:
                                                pass
                                                # State 83364
                                                if len(subjects) == 0:
                                                    pass
                                                    # 26: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        if len(subjects3) >= 1:
                                            tmp116 = subjects3.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3', tmp116)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 83363
                                                if len(subjects3) == 0:
                                                    pass
                                                    # State 83364
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 26: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects3.appendleft(tmp116)
                                subjects110.appendleft(tmp113)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 87448
                            if len(subjects110) >= 1 and isinstance(subjects110[0], Pow):
                                tmp119 = subjects110.popleft()
                                subjects120 = deque(tmp119._args)
                                # State 87449
                                if len(subjects120) >= 1:
                                    tmp121 = subjects120.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3.1.1', tmp121)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 87450
                                        if len(subjects120) >= 1:
                                            tmp123 = subjects120.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3.1.2', tmp123)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 87451
                                                if len(subjects120) == 0:
                                                    pass
                                                    # State 87452
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 87453
                                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                                            tmp125 = subjects3.popleft()
                                                            # State 87454
                                                            if len(subjects3) == 0:
                                                                pass
                                                                # State 87455
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 33: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                    # 35: b/tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                    # 31: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                            subjects3.appendleft(tmp125)
                                            subjects120.appendleft(tmp123)
                                    subjects120.appendleft(tmp121)
                                subjects110.appendleft(tmp119)
                        if len(subjects110) >= 1 and isinstance(subjects110[0], Mul):
                            tmp126 = subjects110.popleft()
                            associative1 = tmp126
                            associative_type1 = type(tmp126)
                            subjects127 = deque(tmp126._args)
                            matcher = CommutativeMatcher83366.get()
                            tmp128 = subjects127
                            subjects127 = []
                            for s in tmp128:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp128, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83367
                                    if len(subjects110) == 0:
                                        pass
                                        # State 83368
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83369
                                            if len(subjects3) == 0:
                                                pass
                                                # State 83370
                                                if len(subjects) == 0:
                                                    pass
                                                    # 26: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        if len(subjects3) >= 1:
                                            tmp130 = subjects3.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3', tmp130)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 83369
                                                if len(subjects3) == 0:
                                                    pass
                                                    # State 83370
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 26: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects3.appendleft(tmp130)
                                if pattern_index == 1:
                                    pass
                                    # State 87460
                                    if len(subjects110) == 0:
                                        pass
                                        # State 87461
                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                            tmp132 = subjects3.popleft()
                                            # State 87462
                                            if len(subjects3) == 0:
                                                pass
                                                # State 87463
                                                if len(subjects) == 0:
                                                    pass
                                                    # 33: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    # 35: b/tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    # 31: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                            subjects3.appendleft(tmp132)
                            subjects110.appendleft(tmp126)
                    if len(subjects110) >= 1:
                        tmp133 = subjects110.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp133)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 87892
                            if len(subjects110) == 0:
                                pass
                                # State 87893
                                if len(subjects3) >= 1 and subjects3[0] == -1:
                                    tmp135 = subjects3.popleft()
                                    # State 87894
                                    if len(subjects3) == 0:
                                        pass
                                        # State 87895
                                        if len(subjects) == 0:
                                            pass
                                            # 37: b/tan(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                    subjects3.appendleft(tmp135)
                        subjects110.appendleft(tmp133)
                    if len(subjects110) >= 1 and isinstance(subjects110[0], Add):
                        tmp136 = subjects110.popleft()
                        associative1 = tmp136
                        associative_type1 = type(tmp136)
                        subjects137 = deque(tmp136._args)
                        matcher = CommutativeMatcher83372.get()
                        tmp138 = subjects137
                        subjects137 = []
                        for s in tmp138:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp138, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83378
                                if len(subjects110) == 0:
                                    pass
                                    # State 83379
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83380
                                        if len(subjects3) == 0:
                                            pass
                                            # State 83381
                                            if len(subjects) == 0:
                                                pass
                                                # 26: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                    if len(subjects3) >= 1:
                                        tmp140 = subjects3.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp140)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83380
                                            if len(subjects3) == 0:
                                                pass
                                                # State 83381
                                                if len(subjects) == 0:
                                                    pass
                                                    # 26: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        subjects3.appendleft(tmp140)
                            if pattern_index == 1:
                                pass
                                # State 87474
                                if len(subjects110) == 0:
                                    pass
                                    # State 87475
                                    if len(subjects3) >= 1 and subjects3[0] == -1:
                                        tmp142 = subjects3.popleft()
                                        # State 87476
                                        if len(subjects3) == 0:
                                            pass
                                            # State 87477
                                            if len(subjects) == 0:
                                                pass
                                                # 33: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                # 35: b/tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                # 31: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                        subjects3.appendleft(tmp142)
                        subjects110.appendleft(tmp136)
                    subjects3.appendleft(tmp109)
                if len(subjects3) >= 1 and isinstance(subjects3[0], Pow):
                    tmp143 = subjects3.popleft()
                    subjects144 = deque(tmp143._args)
                    # State 83624
                    if len(subjects144) >= 1 and isinstance(subjects144[0], tan):
                        tmp145 = subjects144.popleft()
                        subjects146 = deque(tmp145._args)
                        # State 83625
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83626
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83627
                                if len(subjects146) >= 1:
                                    tmp149 = subjects146.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.4.1.0', tmp149)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83628
                                        if len(subjects146) == 0:
                                            pass
                                            # State 83629
                                            if len(subjects144) >= 1 and subjects144[0] == -1:
                                                tmp151 = subjects144.popleft()
                                                # State 83630
                                                if len(subjects144) == 0:
                                                    pass
                                                    # State 83631
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83632
                                                        if len(subjects3) == 0:
                                                            pass
                                                            # State 83633
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    if len(subjects3) >= 1:
                                                        tmp153 = subjects3.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.5', tmp153)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 83632
                                                            if len(subjects3) == 0:
                                                                pass
                                                                # State 83633
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 28: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        subjects3.appendleft(tmp153)
                                                subjects144.appendleft(tmp151)
                                    subjects146.appendleft(tmp149)
                            if len(subjects146) >= 1 and isinstance(subjects146[0], Mul):
                                tmp155 = subjects146.popleft()
                                associative1 = tmp155
                                associative_type1 = type(tmp155)
                                subjects156 = deque(tmp155._args)
                                matcher = CommutativeMatcher83635.get()
                                tmp157 = subjects156
                                subjects156 = []
                                for s in tmp157:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp157, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 83636
                                        if len(subjects146) == 0:
                                            pass
                                            # State 83637
                                            if len(subjects144) >= 1 and subjects144[0] == -1:
                                                tmp158 = subjects144.popleft()
                                                # State 83638
                                                if len(subjects144) == 0:
                                                    pass
                                                    # State 83639
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83640
                                                        if len(subjects3) == 0:
                                                            pass
                                                            # State 83641
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    if len(subjects3) >= 1:
                                                        tmp160 = subjects3.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.5', tmp160)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 83640
                                                            if len(subjects3) == 0:
                                                                pass
                                                                # State 83641
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 28: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        subjects3.appendleft(tmp160)
                                                subjects144.appendleft(tmp158)
                                subjects146.appendleft(tmp155)
                        if len(subjects146) >= 1 and isinstance(subjects146[0], Add):
                            tmp162 = subjects146.popleft()
                            associative1 = tmp162
                            associative_type1 = type(tmp162)
                            subjects163 = deque(tmp162._args)
                            matcher = CommutativeMatcher83643.get()
                            tmp164 = subjects163
                            subjects163 = []
                            for s in tmp164:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp164, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83649
                                    if len(subjects146) == 0:
                                        pass
                                        # State 83650
                                        if len(subjects144) >= 1 and subjects144[0] == -1:
                                            tmp165 = subjects144.popleft()
                                            # State 83651
                                            if len(subjects144) == 0:
                                                pass
                                                # State 83652
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 83653
                                                    if len(subjects3) == 0:
                                                        pass
                                                        # State 83654
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 28: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                if len(subjects3) >= 1:
                                                    tmp167 = subjects3.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5', tmp167)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83653
                                                        if len(subjects3) == 0:
                                                            pass
                                                            # State 83654
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    subjects3.appendleft(tmp167)
                                            subjects144.appendleft(tmp165)
                            subjects146.appendleft(tmp162)
                        subjects144.appendleft(tmp145)
                    if len(subjects144) >= 1 and isinstance(subjects144[0], cos):
                        tmp169 = subjects144.popleft()
                        subjects170 = deque(tmp169._args)
                        # State 95344
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95345
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95346
                                if len(subjects170) >= 1:
                                    tmp173 = subjects170.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.4.1.0', tmp173)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95347
                                        if len(subjects170) == 0:
                                            pass
                                            # State 95348
                                            if len(subjects144) >= 1 and subjects144[0] == -1:
                                                tmp175 = subjects144.popleft()
                                                # State 95349
                                                if len(subjects144) == 0:
                                                    pass
                                                    # State 95350
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95351
                                                        if len(subjects3) == 0:
                                                            pass
                                                            # State 95352
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 38: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    if len(subjects3) >= 1:
                                                        tmp177 = subjects3.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.5', tmp177)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95351
                                                            if len(subjects3) == 0:
                                                                pass
                                                                # State 95352
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 38: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        subjects3.appendleft(tmp177)
                                                subjects144.appendleft(tmp175)
                                    subjects170.appendleft(tmp173)
                            if len(subjects170) >= 1 and isinstance(subjects170[0], Mul):
                                tmp179 = subjects170.popleft()
                                associative1 = tmp179
                                associative_type1 = type(tmp179)
                                subjects180 = deque(tmp179._args)
                                matcher = CommutativeMatcher95354.get()
                                tmp181 = subjects180
                                subjects180 = []
                                for s in tmp181:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp181, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95355
                                        if len(subjects170) == 0:
                                            pass
                                            # State 95356
                                            if len(subjects144) >= 1 and subjects144[0] == -1:
                                                tmp182 = subjects144.popleft()
                                                # State 95357
                                                if len(subjects144) == 0:
                                                    pass
                                                    # State 95358
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95359
                                                        if len(subjects3) == 0:
                                                            pass
                                                            # State 95360
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 38: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    if len(subjects3) >= 1:
                                                        tmp184 = subjects3.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.5', tmp184)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95359
                                                            if len(subjects3) == 0:
                                                                pass
                                                                # State 95360
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 38: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        subjects3.appendleft(tmp184)
                                                subjects144.appendleft(tmp182)
                                subjects170.appendleft(tmp179)
                        if len(subjects170) >= 1 and isinstance(subjects170[0], Add):
                            tmp186 = subjects170.popleft()
                            associative1 = tmp186
                            associative_type1 = type(tmp186)
                            subjects187 = deque(tmp186._args)
                            matcher = CommutativeMatcher95362.get()
                            tmp188 = subjects187
                            subjects187 = []
                            for s in tmp188:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp188, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95368
                                    if len(subjects170) == 0:
                                        pass
                                        # State 95369
                                        if len(subjects144) >= 1 and subjects144[0] == -1:
                                            tmp189 = subjects144.popleft()
                                            # State 95370
                                            if len(subjects144) == 0:
                                                pass
                                                # State 95371
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95372
                                                    if len(subjects3) == 0:
                                                        pass
                                                        # State 95373
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 38: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                if len(subjects3) >= 1:
                                                    tmp191 = subjects3.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5', tmp191)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95372
                                                        if len(subjects3) == 0:
                                                            pass
                                                            # State 95373
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 38: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    subjects3.appendleft(tmp191)
                                            subjects144.appendleft(tmp189)
                            subjects170.appendleft(tmp186)
                        subjects144.appendleft(tmp169)
                    if len(subjects144) >= 1 and isinstance(subjects144[0], sin):
                        tmp193 = subjects144.popleft()
                        subjects194 = deque(tmp193._args)
                        # State 95740
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95741
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95742
                                if len(subjects194) >= 1:
                                    tmp197 = subjects194.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.4.1.0', tmp197)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95743
                                        if len(subjects194) == 0:
                                            pass
                                            # State 95744
                                            if len(subjects144) >= 1 and subjects144[0] == -1:
                                                tmp199 = subjects144.popleft()
                                                # State 95745
                                                if len(subjects144) == 0:
                                                    pass
                                                    # State 95746
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95747
                                                        if len(subjects3) == 0:
                                                            pass
                                                            # State 95748
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 40: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    if len(subjects3) >= 1:
                                                        tmp201 = subjects3.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.5', tmp201)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95747
                                                            if len(subjects3) == 0:
                                                                pass
                                                                # State 95748
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 40: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        subjects3.appendleft(tmp201)
                                                subjects144.appendleft(tmp199)
                                    subjects194.appendleft(tmp197)
                            if len(subjects194) >= 1 and isinstance(subjects194[0], Mul):
                                tmp203 = subjects194.popleft()
                                associative1 = tmp203
                                associative_type1 = type(tmp203)
                                subjects204 = deque(tmp203._args)
                                matcher = CommutativeMatcher95750.get()
                                tmp205 = subjects204
                                subjects204 = []
                                for s in tmp205:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp205, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95751
                                        if len(subjects194) == 0:
                                            pass
                                            # State 95752
                                            if len(subjects144) >= 1 and subjects144[0] == -1:
                                                tmp206 = subjects144.popleft()
                                                # State 95753
                                                if len(subjects144) == 0:
                                                    pass
                                                    # State 95754
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95755
                                                        if len(subjects3) == 0:
                                                            pass
                                                            # State 95756
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 40: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    if len(subjects3) >= 1:
                                                        tmp208 = subjects3.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.5', tmp208)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95755
                                                            if len(subjects3) == 0:
                                                                pass
                                                                # State 95756
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 40: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        subjects3.appendleft(tmp208)
                                                subjects144.appendleft(tmp206)
                                subjects194.appendleft(tmp203)
                        if len(subjects194) >= 1 and isinstance(subjects194[0], Add):
                            tmp210 = subjects194.popleft()
                            associative1 = tmp210
                            associative_type1 = type(tmp210)
                            subjects211 = deque(tmp210._args)
                            matcher = CommutativeMatcher95758.get()
                            tmp212 = subjects211
                            subjects211 = []
                            for s in tmp212:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp212, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95764
                                    if len(subjects194) == 0:
                                        pass
                                        # State 95765
                                        if len(subjects144) >= 1 and subjects144[0] == -1:
                                            tmp213 = subjects144.popleft()
                                            # State 95766
                                            if len(subjects144) == 0:
                                                pass
                                                # State 95767
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95768
                                                    if len(subjects3) == 0:
                                                        pass
                                                        # State 95769
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 40: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                if len(subjects3) >= 1:
                                                    tmp215 = subjects3.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5', tmp215)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95768
                                                        if len(subjects3) == 0:
                                                            pass
                                                            # State 95769
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 40: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    subjects3.appendleft(tmp215)
                                            subjects144.appendleft(tmp213)
                            subjects194.appendleft(tmp210)
                        subjects144.appendleft(tmp193)
                    subjects3.appendleft(tmp143)
                if len(subjects3) >= 1 and isinstance(subjects3[0], tanh):
                    tmp217 = subjects3.popleft()
                    subjects218 = deque(tmp217._args)
                    # State 126911
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 126912
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 126913
                            if len(subjects218) >= 1 and isinstance(subjects218[0], Pow):
                                tmp221 = subjects218.popleft()
                                subjects222 = deque(tmp221._args)
                                # State 126914
                                if len(subjects222) >= 1:
                                    tmp223 = subjects222.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3.1.1', tmp223)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 126915
                                        if len(subjects222) >= 1:
                                            tmp225 = subjects222.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3.1.2', tmp225)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 126916
                                                if len(subjects222) == 0:
                                                    pass
                                                    # State 126917
                                                    if len(subjects218) == 0:
                                                        pass
                                                        # State 126918
                                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                                            tmp227 = subjects3.popleft()
                                                            # State 126919
                                                            if len(subjects3) == 0:
                                                                pass
                                                                # State 126920
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 67: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                    # 69: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                    # 71: b/tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                            subjects3.appendleft(tmp227)
                                            subjects222.appendleft(tmp225)
                                    subjects222.appendleft(tmp223)
                                subjects218.appendleft(tmp221)
                        if len(subjects218) >= 1 and isinstance(subjects218[0], Mul):
                            tmp228 = subjects218.popleft()
                            associative1 = tmp228
                            associative_type1 = type(tmp228)
                            subjects229 = deque(tmp228._args)
                            matcher = CommutativeMatcher126922.get()
                            tmp230 = subjects229
                            subjects229 = []
                            for s in tmp230:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp230, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 126927
                                    if len(subjects218) == 0:
                                        pass
                                        # State 126928
                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                            tmp231 = subjects3.popleft()
                                            # State 126929
                                            if len(subjects3) == 0:
                                                pass
                                                # State 126930
                                                if len(subjects) == 0:
                                                    pass
                                                    # 67: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                    # 69: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    # 71: b/tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            subjects3.appendleft(tmp231)
                            subjects218.appendleft(tmp228)
                    if len(subjects218) >= 1:
                        tmp232 = subjects218.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp232)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 127387
                            if len(subjects218) == 0:
                                pass
                                # State 127388
                                if len(subjects3) >= 1 and subjects3[0] == -1:
                                    tmp234 = subjects3.popleft()
                                    # State 127389
                                    if len(subjects3) == 0:
                                        pass
                                        # State 127390
                                        if len(subjects) == 0:
                                            pass
                                            # 73: b/tanh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                    subjects3.appendleft(tmp234)
                        subjects218.appendleft(tmp232)
                    if len(subjects218) >= 1 and isinstance(subjects218[0], Add):
                        tmp235 = subjects218.popleft()
                        associative1 = tmp235
                        associative_type1 = type(tmp235)
                        subjects236 = deque(tmp235._args)
                        matcher = CommutativeMatcher126932.get()
                        tmp237 = subjects236
                        subjects236 = []
                        for s in tmp237:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp237, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 126945
                                if len(subjects218) == 0:
                                    pass
                                    # State 126946
                                    if len(subjects3) >= 1 and subjects3[0] == -1:
                                        tmp238 = subjects3.popleft()
                                        # State 126947
                                        if len(subjects3) == 0:
                                            pass
                                            # State 126948
                                            if len(subjects) == 0:
                                                pass
                                                # 67: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                # 69: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                # 71: b/tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        subjects3.appendleft(tmp238)
                        subjects218.appendleft(tmp235)
                    subjects3.appendleft(tmp217)
                if len(subjects3) >= 1 and isinstance(subjects3[0], cosh):
                    tmp239 = subjects3.popleft()
                    subjects240 = deque(tmp239._args)
                    # State 129688
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 129689
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 129690
                            if len(subjects240) >= 1 and isinstance(subjects240[0], Pow):
                                tmp243 = subjects240.popleft()
                                subjects244 = deque(tmp243._args)
                                # State 129691
                                if len(subjects244) >= 1:
                                    tmp245 = subjects244.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3.1.1', tmp245)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 129692
                                        if len(subjects244) >= 1:
                                            tmp247 = subjects244.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3.1.2', tmp247)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 129693
                                                if len(subjects244) == 0:
                                                    pass
                                                    # State 129694
                                                    if len(subjects240) == 0:
                                                        pass
                                                        # State 129695
                                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                                            tmp249 = subjects3.popleft()
                                                            # State 129696
                                                            if len(subjects3) == 0:
                                                                pass
                                                                # State 129697
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 74: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                    # 76: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                    # 78: b/cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                            subjects3.appendleft(tmp249)
                                            subjects244.appendleft(tmp247)
                                    subjects244.appendleft(tmp245)
                                subjects240.appendleft(tmp243)
                        if len(subjects240) >= 1 and isinstance(subjects240[0], Mul):
                            tmp250 = subjects240.popleft()
                            associative1 = tmp250
                            associative_type1 = type(tmp250)
                            subjects251 = deque(tmp250._args)
                            matcher = CommutativeMatcher129699.get()
                            tmp252 = subjects251
                            subjects251 = []
                            for s in tmp252:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp252, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 129704
                                    if len(subjects240) == 0:
                                        pass
                                        # State 129705
                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                            tmp253 = subjects3.popleft()
                                            # State 129706
                                            if len(subjects3) == 0:
                                                pass
                                                # State 129707
                                                if len(subjects) == 0:
                                                    pass
                                                    # 74: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                    # 76: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    # 78: b/cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            subjects3.appendleft(tmp253)
                            subjects240.appendleft(tmp250)
                    if len(subjects240) >= 1:
                        tmp254 = subjects240.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp254)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 130480
                            if len(subjects240) == 0:
                                pass
                                # State 130481
                                if len(subjects3) >= 1 and subjects3[0] == -1:
                                    tmp256 = subjects3.popleft()
                                    # State 130482
                                    if len(subjects3) == 0:
                                        pass
                                        # State 130483
                                        if len(subjects) == 0:
                                            pass
                                            # 80: b/cosh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                    subjects3.appendleft(tmp256)
                        subjects240.appendleft(tmp254)
                    if len(subjects240) >= 1 and isinstance(subjects240[0], Add):
                        tmp257 = subjects240.popleft()
                        associative1 = tmp257
                        associative_type1 = type(tmp257)
                        subjects258 = deque(tmp257._args)
                        matcher = CommutativeMatcher129709.get()
                        tmp259 = subjects258
                        subjects258 = []
                        for s in tmp259:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp259, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 129722
                                if len(subjects240) == 0:
                                    pass
                                    # State 129723
                                    if len(subjects3) >= 1 and subjects3[0] == -1:
                                        tmp260 = subjects3.popleft()
                                        # State 129724
                                        if len(subjects3) == 0:
                                            pass
                                            # State 129725
                                            if len(subjects) == 0:
                                                pass
                                                # 74: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                # 76: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                # 78: b/cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        subjects3.appendleft(tmp260)
                        subjects240.appendleft(tmp257)
                    subjects3.appendleft(tmp239)
                if len(subjects3) >= 1 and isinstance(subjects3[0], sinh):
                    tmp261 = subjects3.popleft()
                    subjects262 = deque(tmp261._args)
                    # State 130028
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130029
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 130030
                            if len(subjects262) >= 1 and isinstance(subjects262[0], Pow):
                                tmp265 = subjects262.popleft()
                                subjects266 = deque(tmp265._args)
                                # State 130031
                                if len(subjects266) >= 1:
                                    tmp267 = subjects266.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3.1.1', tmp267)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 130032
                                        if len(subjects266) >= 1:
                                            tmp269 = subjects266.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3.1.2', tmp269)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 130033
                                                if len(subjects266) == 0:
                                                    pass
                                                    # State 130034
                                                    if len(subjects262) == 0:
                                                        pass
                                                        # State 130035
                                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                                            tmp271 = subjects3.popleft()
                                                            # State 130036
                                                            if len(subjects3) == 0:
                                                                pass
                                                                # State 130037
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 75: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                    # 77: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                    # 79: b/sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                            subjects3.appendleft(tmp271)
                                            subjects266.appendleft(tmp269)
                                    subjects266.appendleft(tmp267)
                                subjects262.appendleft(tmp265)
                        if len(subjects262) >= 1 and isinstance(subjects262[0], Mul):
                            tmp272 = subjects262.popleft()
                            associative1 = tmp272
                            associative_type1 = type(tmp272)
                            subjects273 = deque(tmp272._args)
                            matcher = CommutativeMatcher130039.get()
                            tmp274 = subjects273
                            subjects273 = []
                            for s in tmp274:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp274, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 130044
                                    if len(subjects262) == 0:
                                        pass
                                        # State 130045
                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                            tmp275 = subjects3.popleft()
                                            # State 130046
                                            if len(subjects3) == 0:
                                                pass
                                                # State 130047
                                                if len(subjects) == 0:
                                                    pass
                                                    # 75: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                    # 77: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    # 79: b/sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            subjects3.appendleft(tmp275)
                            subjects262.appendleft(tmp272)
                    if len(subjects262) >= 1:
                        tmp276 = subjects262.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp276)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 130536
                            if len(subjects262) == 0:
                                pass
                                # State 130537
                                if len(subjects3) >= 1 and subjects3[0] == -1:
                                    tmp278 = subjects3.popleft()
                                    # State 130538
                                    if len(subjects3) == 0:
                                        pass
                                        # State 130539
                                        if len(subjects) == 0:
                                            pass
                                            # 81: b/sinh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                                    subjects3.appendleft(tmp278)
                        subjects262.appendleft(tmp276)
                    if len(subjects262) >= 1 and isinstance(subjects262[0], Add):
                        tmp279 = subjects262.popleft()
                        associative1 = tmp279
                        associative_type1 = type(tmp279)
                        subjects280 = deque(tmp279._args)
                        matcher = CommutativeMatcher130049.get()
                        tmp281 = subjects280
                        subjects280 = []
                        for s in tmp281:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp281, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 130062
                                if len(subjects262) == 0:
                                    pass
                                    # State 130063
                                    if len(subjects3) >= 1 and subjects3[0] == -1:
                                        tmp282 = subjects3.popleft()
                                        # State 130064
                                        if len(subjects3) == 0:
                                            pass
                                            # State 130065
                                            if len(subjects) == 0:
                                                pass
                                                # 75: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                # 77: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                # 79: b/sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        subjects3.appendleft(tmp282)
                        subjects262.appendleft(tmp279)
                    subjects3.appendleft(tmp261)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp283 = subjects.popleft()
                subjects284 = deque(tmp283._args)
                # State 51926
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 51927
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 51928
                        if len(subjects284) >= 1 and isinstance(subjects284[0], Add):
                            tmp287 = subjects284.popleft()
                            associative1 = tmp287
                            associative_type1 = type(tmp287)
                            subjects288 = deque(tmp287._args)
                            matcher = CommutativeMatcher51930.get()
                            tmp289 = subjects288
                            subjects288 = []
                            for s in tmp289:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp289, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 51977
                                    if len(subjects284) == 0:
                                        pass
                                        # State 51978
                                        if len(subjects) == 0:
                                            pass
                                            # 12: b*log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                            subjects284.appendleft(tmp287)
                        if len(subjects284) >= 1:
                            tmp290 = subjects284.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1', tmp290)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53114
                                if len(subjects284) == 0:
                                    pass
                                    # State 53115
                                    if len(subjects) == 0:
                                        pass
                                        # 13: b*log(c*RFx**p) /; (cons_f3) and (cons_f8) and (cons_f5) and (cons_f1200)
                            subjects284.appendleft(tmp290)
                    if len(subjects284) >= 1 and isinstance(subjects284[0], Pow):
                        tmp292 = subjects284.popleft()
                        subjects293 = deque(tmp292._args)
                        # State 51979
                        if len(subjects293) >= 1 and isinstance(subjects293[0], Add):
                            tmp294 = subjects293.popleft()
                            associative1 = tmp294
                            associative_type1 = type(tmp294)
                            subjects295 = deque(tmp294._args)
                            matcher = CommutativeMatcher51981.get()
                            tmp296 = subjects295
                            subjects295 = []
                            for s in tmp296:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp296, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 52028
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 52029
                                        if len(subjects293) == 0:
                                            pass
                                            # State 52030
                                            if len(subjects284) == 0:
                                                pass
                                                # State 52031
                                                if len(subjects) == 0:
                                                    pass
                                                    # 12: b*log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                                    if len(subjects293) >= 1:
                                        tmp298 = []
                                        tmp298.append(subjects293.popleft())
                                        while True:
                                            if len(tmp298) > 1:
                                                tmp299 = create_operation_expression(associative1, tmp298)
                                            elif len(tmp298) == 1:
                                                tmp299 = tmp298[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2.2', tmp299)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 52029
                                                if len(subjects293) == 0:
                                                    pass
                                                    # State 52030
                                                    if len(subjects284) == 0:
                                                        pass
                                                        # State 52031
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 12: b*log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                                            if len(subjects293) == 0:
                                                break
                                            tmp298.append(subjects293.popleft())
                                        subjects293.extendleft(reversed(tmp298))
                            subjects293.appendleft(tmp294)
                        if len(subjects293) >= 1:
                            tmp301 = subjects293.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1', tmp301)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53116
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53117
                                    if len(subjects293) == 0:
                                        pass
                                        # State 53118
                                        if len(subjects284) == 0:
                                            pass
                                            # State 53119
                                            if len(subjects) == 0:
                                                pass
                                                # 13: b*log(c*RFx**p) /; (cons_f3) and (cons_f8) and (cons_f5) and (cons_f1200)
                                if len(subjects293) >= 1:
                                    tmp304 = subjects293.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.2', tmp304)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 53117
                                        if len(subjects293) == 0:
                                            pass
                                            # State 53118
                                            if len(subjects284) == 0:
                                                pass
                                                # State 53119
                                                if len(subjects) == 0:
                                                    pass
                                                    # 13: b*log(c*RFx**p) /; (cons_f3) and (cons_f8) and (cons_f5) and (cons_f1200)
                                    subjects293.appendleft(tmp304)
                            subjects293.appendleft(tmp301)
                        subjects284.appendleft(tmp292)
                if len(subjects284) >= 1 and isinstance(subjects284[0], Mul):
                    tmp306 = subjects284.popleft()
                    associative1 = tmp306
                    associative_type1 = type(tmp306)
                    subjects307 = deque(tmp306._args)
                    matcher = CommutativeMatcher52033.get()
                    tmp308 = subjects307
                    subjects307 = []
                    for s in tmp308:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp308, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 52136
                            if len(subjects284) == 0:
                                pass
                                # State 52137
                                if len(subjects) == 0:
                                    pass
                                    # 12: b*log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                        if pattern_index == 1:
                            pass
                            # State 53124
                            if len(subjects284) == 0:
                                pass
                                # State 53125
                                if len(subjects) == 0:
                                    pass
                                    # 13: b*log(c*RFx**p) /; (cons_f3) and (cons_f8) and (cons_f5) and (cons_f1200)
                    subjects284.appendleft(tmp306)
                subjects.appendleft(tmp283)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.3', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 68733
                if len(subjects) >= 1 and isinstance(subjects[0], sin):
                    tmp310 = subjects.popleft()
                    subjects311 = deque(tmp310._args)
                    # State 68734
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 68735
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68736
                            if len(subjects311) >= 1:
                                tmp314 = subjects311.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.3.1.0', tmp314)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 68737
                                    if len(subjects311) == 0:
                                        pass
                                        # State 68738
                                        if len(subjects) == 0:
                                            pass
                                            # 14: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                subjects311.appendleft(tmp314)
                        if len(subjects311) >= 1 and isinstance(subjects311[0], Mul):
                            tmp316 = subjects311.popleft()
                            associative1 = tmp316
                            associative_type1 = type(tmp316)
                            subjects317 = deque(tmp316._args)
                            matcher = CommutativeMatcher68740.get()
                            tmp318 = subjects317
                            subjects317 = []
                            for s in tmp318:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp318, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 68741
                                    if len(subjects311) == 0:
                                        pass
                                        # State 68742
                                        if len(subjects) == 0:
                                            pass
                                            # 14: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                            subjects311.appendleft(tmp316)
                    if len(subjects311) >= 1 and isinstance(subjects311[0], Add):
                        tmp319 = subjects311.popleft()
                        associative1 = tmp319
                        associative_type1 = type(tmp319)
                        subjects320 = deque(tmp319._args)
                        matcher = CommutativeMatcher68744.get()
                        tmp321 = subjects320
                        subjects320 = []
                        for s in tmp321:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp321, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 68750
                                if len(subjects311) == 0:
                                    pass
                                    # State 68751
                                    if len(subjects) == 0:
                                        pass
                                        # 14: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        subjects311.appendleft(tmp319)
                    subjects.appendleft(tmp310)
                if len(subjects) >= 1 and isinstance(subjects[0], cos):
                    tmp322 = subjects.popleft()
                    subjects323 = deque(tmp322._args)
                    # State 69017
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 69018
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 69019
                            if len(subjects323) >= 1:
                                tmp326 = subjects323.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.3.1.0', tmp326)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 69020
                                    if len(subjects323) == 0:
                                        pass
                                        # State 69021
                                        if len(subjects) == 0:
                                            pass
                                            # 16: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                subjects323.appendleft(tmp326)
                        if len(subjects323) >= 1 and isinstance(subjects323[0], Mul):
                            tmp328 = subjects323.popleft()
                            associative1 = tmp328
                            associative_type1 = type(tmp328)
                            subjects329 = deque(tmp328._args)
                            matcher = CommutativeMatcher69023.get()
                            tmp330 = subjects329
                            subjects329 = []
                            for s in tmp330:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp330, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 69024
                                    if len(subjects323) == 0:
                                        pass
                                        # State 69025
                                        if len(subjects) == 0:
                                            pass
                                            # 16: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                            subjects323.appendleft(tmp328)
                    if len(subjects323) >= 1 and isinstance(subjects323[0], Add):
                        tmp331 = subjects323.popleft()
                        associative1 = tmp331
                        associative_type1 = type(tmp331)
                        subjects332 = deque(tmp331._args)
                        matcher = CommutativeMatcher69027.get()
                        tmp333 = subjects332
                        subjects332 = []
                        for s in tmp333:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp333, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 69033
                                if len(subjects323) == 0:
                                    pass
                                    # State 69034
                                    if len(subjects) == 0:
                                        pass
                                        # 16: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        subjects323.appendleft(tmp331)
                    subjects.appendleft(tmp322)
                if len(subjects) >= 1 and isinstance(subjects[0], tan):
                    tmp334 = subjects.popleft()
                    subjects335 = deque(tmp334._args)
                    # State 83340
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83341
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83342
                            if len(subjects335) >= 1:
                                tmp338 = subjects335.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.3.1.0', tmp338)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83343
                                    if len(subjects335) == 0:
                                        pass
                                        # State 83344
                                        if len(subjects) == 0:
                                            pass
                                            # 26: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                subjects335.appendleft(tmp338)
                        if len(subjects335) >= 1 and isinstance(subjects335[0], Mul):
                            tmp340 = subjects335.popleft()
                            associative1 = tmp340
                            associative_type1 = type(tmp340)
                            subjects341 = deque(tmp340._args)
                            matcher = CommutativeMatcher83346.get()
                            tmp342 = subjects341
                            subjects341 = []
                            for s in tmp342:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp342, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83347
                                    if len(subjects335) == 0:
                                        pass
                                        # State 83348
                                        if len(subjects) == 0:
                                            pass
                                            # 26: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                            subjects335.appendleft(tmp340)
                    if len(subjects335) >= 1 and isinstance(subjects335[0], Add):
                        tmp343 = subjects335.popleft()
                        associative1 = tmp343
                        associative_type1 = type(tmp343)
                        subjects344 = deque(tmp343._args)
                        matcher = CommutativeMatcher83350.get()
                        tmp345 = subjects344
                        subjects344 = []
                        for s in tmp345:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp345, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83356
                                if len(subjects335) == 0:
                                    pass
                                    # State 83357
                                    if len(subjects) == 0:
                                        pass
                                        # 26: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        subjects335.appendleft(tmp343)
                    subjects.appendleft(tmp334)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.5', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 83598
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp347 = subjects.popleft()
                    subjects348 = deque(tmp347._args)
                    # State 83599
                    if len(subjects348) >= 1 and isinstance(subjects348[0], tan):
                        tmp349 = subjects348.popleft()
                        subjects350 = deque(tmp349._args)
                        # State 83600
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83601
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83602
                                if len(subjects350) >= 1:
                                    tmp353 = subjects350.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.4.1.0', tmp353)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83603
                                        if len(subjects350) == 0:
                                            pass
                                            # State 83604
                                            if len(subjects348) >= 1 and subjects348[0] == -1:
                                                tmp355 = subjects348.popleft()
                                                # State 83605
                                                if len(subjects348) == 0:
                                                    pass
                                                    # State 83606
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 28: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                subjects348.appendleft(tmp355)
                                    subjects350.appendleft(tmp353)
                            if len(subjects350) >= 1 and isinstance(subjects350[0], Mul):
                                tmp356 = subjects350.popleft()
                                associative1 = tmp356
                                associative_type1 = type(tmp356)
                                subjects357 = deque(tmp356._args)
                                matcher = CommutativeMatcher83608.get()
                                tmp358 = subjects357
                                subjects357 = []
                                for s in tmp358:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp358, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 83609
                                        if len(subjects350) == 0:
                                            pass
                                            # State 83610
                                            if len(subjects348) >= 1 and subjects348[0] == -1:
                                                tmp359 = subjects348.popleft()
                                                # State 83611
                                                if len(subjects348) == 0:
                                                    pass
                                                    # State 83612
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 28: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                subjects348.appendleft(tmp359)
                                subjects350.appendleft(tmp356)
                        if len(subjects350) >= 1 and isinstance(subjects350[0], Add):
                            tmp360 = subjects350.popleft()
                            associative1 = tmp360
                            associative_type1 = type(tmp360)
                            subjects361 = deque(tmp360._args)
                            matcher = CommutativeMatcher83614.get()
                            tmp362 = subjects361
                            subjects361 = []
                            for s in tmp362:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp362, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83620
                                    if len(subjects350) == 0:
                                        pass
                                        # State 83621
                                        if len(subjects348) >= 1 and subjects348[0] == -1:
                                            tmp363 = subjects348.popleft()
                                            # State 83622
                                            if len(subjects348) == 0:
                                                pass
                                                # State 83623
                                                if len(subjects) == 0:
                                                    pass
                                                    # 28: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects348.appendleft(tmp363)
                            subjects350.appendleft(tmp360)
                        subjects348.appendleft(tmp349)
                    if len(subjects348) >= 1 and isinstance(subjects348[0], cos):
                        tmp364 = subjects348.popleft()
                        subjects365 = deque(tmp364._args)
                        # State 95320
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95321
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95322
                                if len(subjects365) >= 1:
                                    tmp368 = subjects365.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.4.1.0', tmp368)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95323
                                        if len(subjects365) == 0:
                                            pass
                                            # State 95324
                                            if len(subjects348) >= 1 and subjects348[0] == -1:
                                                tmp370 = subjects348.popleft()
                                                # State 95325
                                                if len(subjects348) == 0:
                                                    pass
                                                    # State 95326
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 38: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                subjects348.appendleft(tmp370)
                                    subjects365.appendleft(tmp368)
                            if len(subjects365) >= 1 and isinstance(subjects365[0], Mul):
                                tmp371 = subjects365.popleft()
                                associative1 = tmp371
                                associative_type1 = type(tmp371)
                                subjects372 = deque(tmp371._args)
                                matcher = CommutativeMatcher95328.get()
                                tmp373 = subjects372
                                subjects372 = []
                                for s in tmp373:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp373, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95329
                                        if len(subjects365) == 0:
                                            pass
                                            # State 95330
                                            if len(subjects348) >= 1 and subjects348[0] == -1:
                                                tmp374 = subjects348.popleft()
                                                # State 95331
                                                if len(subjects348) == 0:
                                                    pass
                                                    # State 95332
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 38: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                subjects348.appendleft(tmp374)
                                subjects365.appendleft(tmp371)
                        if len(subjects365) >= 1 and isinstance(subjects365[0], Add):
                            tmp375 = subjects365.popleft()
                            associative1 = tmp375
                            associative_type1 = type(tmp375)
                            subjects376 = deque(tmp375._args)
                            matcher = CommutativeMatcher95334.get()
                            tmp377 = subjects376
                            subjects376 = []
                            for s in tmp377:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp377, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95340
                                    if len(subjects365) == 0:
                                        pass
                                        # State 95341
                                        if len(subjects348) >= 1 and subjects348[0] == -1:
                                            tmp378 = subjects348.popleft()
                                            # State 95342
                                            if len(subjects348) == 0:
                                                pass
                                                # State 95343
                                                if len(subjects) == 0:
                                                    pass
                                                    # 38: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects348.appendleft(tmp378)
                            subjects365.appendleft(tmp375)
                        subjects348.appendleft(tmp364)
                    if len(subjects348) >= 1 and isinstance(subjects348[0], sin):
                        tmp379 = subjects348.popleft()
                        subjects380 = deque(tmp379._args)
                        # State 95716
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95717
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95718
                                if len(subjects380) >= 1:
                                    tmp383 = subjects380.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.4.1.0', tmp383)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95719
                                        if len(subjects380) == 0:
                                            pass
                                            # State 95720
                                            if len(subjects348) >= 1 and subjects348[0] == -1:
                                                tmp385 = subjects348.popleft()
                                                # State 95721
                                                if len(subjects348) == 0:
                                                    pass
                                                    # State 95722
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 40: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                subjects348.appendleft(tmp385)
                                    subjects380.appendleft(tmp383)
                            if len(subjects380) >= 1 and isinstance(subjects380[0], Mul):
                                tmp386 = subjects380.popleft()
                                associative1 = tmp386
                                associative_type1 = type(tmp386)
                                subjects387 = deque(tmp386._args)
                                matcher = CommutativeMatcher95724.get()
                                tmp388 = subjects387
                                subjects387 = []
                                for s in tmp388:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp388, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95725
                                        if len(subjects380) == 0:
                                            pass
                                            # State 95726
                                            if len(subjects348) >= 1 and subjects348[0] == -1:
                                                tmp389 = subjects348.popleft()
                                                # State 95727
                                                if len(subjects348) == 0:
                                                    pass
                                                    # State 95728
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 40: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                subjects348.appendleft(tmp389)
                                subjects380.appendleft(tmp386)
                        if len(subjects380) >= 1 and isinstance(subjects380[0], Add):
                            tmp390 = subjects380.popleft()
                            associative1 = tmp390
                            associative_type1 = type(tmp390)
                            subjects391 = deque(tmp390._args)
                            matcher = CommutativeMatcher95730.get()
                            tmp392 = subjects391
                            subjects391 = []
                            for s in tmp392:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp392, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95736
                                    if len(subjects380) == 0:
                                        pass
                                        # State 95737
                                        if len(subjects348) >= 1 and subjects348[0] == -1:
                                            tmp393 = subjects348.popleft()
                                            # State 95738
                                            if len(subjects348) == 0:
                                                pass
                                                # State 95739
                                                if len(subjects) == 0:
                                                    pass
                                                    # 40: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects348.appendleft(tmp393)
                            subjects380.appendleft(tmp390)
                        subjects348.appendleft(tmp379)
                    subjects.appendleft(tmp347)
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp394 = subjects.popleft()
                subjects395 = deque(tmp394._args)
                # State 72980
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 72981
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 72982
                        if len(subjects395) >= 1 and isinstance(subjects395[0], Pow):
                            tmp398 = subjects395.popleft()
                            subjects399 = deque(tmp398._args)
                            # State 72983
                            if len(subjects399) >= 1:
                                tmp400 = subjects399.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.1.1', tmp400)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 72984
                                    if len(subjects399) >= 1:
                                        tmp402 = subjects399.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.1.2', tmp402)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 72985
                                            if len(subjects399) == 0:
                                                pass
                                                # State 72986
                                                if len(subjects395) == 0:
                                                    pass
                                                    # State 72987
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 18: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                                        # 20: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                        # 22: b*sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        subjects399.appendleft(tmp402)
                                subjects399.appendleft(tmp400)
                            subjects395.appendleft(tmp398)
                    if len(subjects395) >= 1 and isinstance(subjects395[0], Mul):
                        tmp404 = subjects395.popleft()
                        associative1 = tmp404
                        associative_type1 = type(tmp404)
                        subjects405 = deque(tmp404._args)
                        matcher = CommutativeMatcher72989.get()
                        tmp406 = subjects405
                        subjects405 = []
                        for s in tmp406:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp406, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 72994
                                if len(subjects395) == 0:
                                    pass
                                    # State 72995
                                    if len(subjects) == 0:
                                        pass
                                        # 18: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                        # 20: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                        # 22: b*sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        subjects395.appendleft(tmp404)
                if len(subjects395) >= 1:
                    tmp407 = subjects395.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp407)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 73510
                        if len(subjects395) == 0:
                            pass
                            # State 73511
                            if len(subjects) == 0:
                                pass
                                # 24: b*sin(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                    subjects395.appendleft(tmp407)
                if len(subjects395) >= 1 and isinstance(subjects395[0], Add):
                    tmp409 = subjects395.popleft()
                    associative1 = tmp409
                    associative_type1 = type(tmp409)
                    subjects410 = deque(tmp409._args)
                    matcher = CommutativeMatcher72997.get()
                    tmp411 = subjects410
                    subjects410 = []
                    for s in tmp411:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp411, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 73010
                            if len(subjects395) == 0:
                                pass
                                # State 73011
                                if len(subjects) == 0:
                                    pass
                                    # 18: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    # 20: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    # 22: b*sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                    subjects395.appendleft(tmp409)
                subjects.appendleft(tmp394)
            if len(subjects) >= 1 and isinstance(subjects[0], cos):
                tmp412 = subjects.popleft()
                subjects413 = deque(tmp412._args)
                # State 73147
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 73148
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 73149
                        if len(subjects413) >= 1 and isinstance(subjects413[0], Pow):
                            tmp416 = subjects413.popleft()
                            subjects417 = deque(tmp416._args)
                            # State 73150
                            if len(subjects417) >= 1:
                                tmp418 = subjects417.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.1.1', tmp418)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 73151
                                    if len(subjects417) >= 1:
                                        tmp420 = subjects417.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.1.2', tmp420)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 73152
                                            if len(subjects417) == 0:
                                                pass
                                                # State 73153
                                                if len(subjects413) == 0:
                                                    pass
                                                    # State 73154
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 19: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                                        # 21: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                        # 23: b*cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        subjects417.appendleft(tmp420)
                                subjects417.appendleft(tmp418)
                            subjects413.appendleft(tmp416)
                    if len(subjects413) >= 1 and isinstance(subjects413[0], Mul):
                        tmp422 = subjects413.popleft()
                        associative1 = tmp422
                        associative_type1 = type(tmp422)
                        subjects423 = deque(tmp422._args)
                        matcher = CommutativeMatcher73156.get()
                        tmp424 = subjects423
                        subjects423 = []
                        for s in tmp424:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp424, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 73161
                                if len(subjects413) == 0:
                                    pass
                                    # State 73162
                                    if len(subjects) == 0:
                                        pass
                                        # 19: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                        # 21: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                        # 23: b*cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        subjects413.appendleft(tmp422)
                if len(subjects413) >= 1:
                    tmp425 = subjects413.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp425)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 73550
                        if len(subjects413) == 0:
                            pass
                            # State 73551
                            if len(subjects) == 0:
                                pass
                                # 25: b*cos(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                    subjects413.appendleft(tmp425)
                if len(subjects413) >= 1 and isinstance(subjects413[0], Add):
                    tmp427 = subjects413.popleft()
                    associative1 = tmp427
                    associative_type1 = type(tmp427)
                    subjects428 = deque(tmp427._args)
                    matcher = CommutativeMatcher73164.get()
                    tmp429 = subjects428
                    subjects428 = []
                    for s in tmp429:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp429, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 73177
                            if len(subjects413) == 0:
                                pass
                                # State 73178
                                if len(subjects) == 0:
                                    pass
                                    # 19: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    # 21: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    # 23: b*cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                    subjects413.appendleft(tmp427)
                subjects.appendleft(tmp412)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp430 = subjects.popleft()
                subjects431 = deque(tmp430._args)
                # State 87160
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 87161
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 87162
                        if len(subjects431) >= 1 and isinstance(subjects431[0], Pow):
                            tmp434 = subjects431.popleft()
                            subjects435 = deque(tmp434._args)
                            # State 87163
                            if len(subjects435) >= 1:
                                tmp436 = subjects435.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.1.1', tmp436)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 87164
                                    if len(subjects435) >= 1:
                                        tmp438 = subjects435.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.1.2', tmp438)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 87165
                                            if len(subjects435) == 0:
                                                pass
                                                # State 87166
                                                if len(subjects431) == 0:
                                                    pass
                                                    # State 87167
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 32: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                        # 34: b*tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                        # 30: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                        subjects435.appendleft(tmp438)
                                subjects435.appendleft(tmp436)
                            subjects431.appendleft(tmp434)
                    if len(subjects431) >= 1 and isinstance(subjects431[0], Mul):
                        tmp440 = subjects431.popleft()
                        associative1 = tmp440
                        associative_type1 = type(tmp440)
                        subjects441 = deque(tmp440._args)
                        matcher = CommutativeMatcher87169.get()
                        tmp442 = subjects441
                        subjects441 = []
                        for s in tmp442:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp442, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 87174
                                if len(subjects431) == 0:
                                    pass
                                    # State 87175
                                    if len(subjects) == 0:
                                        pass
                                        # 32: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                        # 34: b*tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        # 30: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        subjects431.appendleft(tmp440)
                if len(subjects431) >= 1:
                    tmp443 = subjects431.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp443)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 87848
                        if len(subjects431) == 0:
                            pass
                            # State 87849
                            if len(subjects) == 0:
                                pass
                                # 36: b*tan(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                    subjects431.appendleft(tmp443)
                if len(subjects431) >= 1 and isinstance(subjects431[0], Add):
                    tmp445 = subjects431.popleft()
                    associative1 = tmp445
                    associative_type1 = type(tmp445)
                    subjects446 = deque(tmp445._args)
                    matcher = CommutativeMatcher87177.get()
                    tmp447 = subjects446
                    subjects446 = []
                    for s in tmp447:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp447, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 87190
                            if len(subjects431) == 0:
                                pass
                                # State 87191
                                if len(subjects) == 0:
                                    pass
                                    # 32: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                    # 34: b*tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    # 30: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                    subjects431.appendleft(tmp445)
                subjects.appendleft(tmp430)
            if len(subjects) >= 1 and isinstance(subjects[0], asin):
                tmp448 = subjects.popleft()
                subjects449 = deque(tmp448._args)
                # State 107978
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 107979
                    if len(subjects449) >= 1:
                        tmp451 = subjects449.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp451)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 107980
                            if len(subjects449) == 0:
                                pass
                                # State 107981
                                if len(subjects) == 0:
                                    pass
                                    # 50: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        subjects449.appendleft(tmp451)
                if len(subjects449) >= 1 and isinstance(subjects449[0], Mul):
                    tmp453 = subjects449.popleft()
                    associative1 = tmp453
                    associative_type1 = type(tmp453)
                    subjects454 = deque(tmp453._args)
                    matcher = CommutativeMatcher107983.get()
                    tmp455 = subjects454
                    subjects454 = []
                    for s in tmp455:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp455, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 107984
                            if len(subjects449) == 0:
                                pass
                                # State 107985
                                if len(subjects) == 0:
                                    pass
                                    # 50: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects449.appendleft(tmp453)
                if len(subjects449) >= 1 and isinstance(subjects449[0], Add):
                    tmp456 = subjects449.popleft()
                    associative1 = tmp456
                    associative_type1 = type(tmp456)
                    subjects457 = deque(tmp456._args)
                    matcher = CommutativeMatcher110278.get()
                    tmp458 = subjects457
                    subjects457 = []
                    for s in tmp458:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp458, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 110284
                            if len(subjects449) == 0:
                                pass
                                # State 110285
                                if len(subjects) == 0:
                                    pass
                                    # 52: b*asin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                    subjects449.appendleft(tmp456)
                subjects.appendleft(tmp448)
            if len(subjects) >= 1 and isinstance(subjects[0], acos):
                tmp459 = subjects.popleft()
                subjects460 = deque(tmp459._args)
                # State 108072
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 108073
                    if len(subjects460) >= 1:
                        tmp462 = subjects460.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp462)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 108074
                            if len(subjects460) == 0:
                                pass
                                # State 108075
                                if len(subjects) == 0:
                                    pass
                                    # 51: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        subjects460.appendleft(tmp462)
                if len(subjects460) >= 1 and isinstance(subjects460[0], Mul):
                    tmp464 = subjects460.popleft()
                    associative1 = tmp464
                    associative_type1 = type(tmp464)
                    subjects465 = deque(tmp464._args)
                    matcher = CommutativeMatcher108077.get()
                    tmp466 = subjects465
                    subjects465 = []
                    for s in tmp466:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp466, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 108078
                            if len(subjects460) == 0:
                                pass
                                # State 108079
                                if len(subjects) == 0:
                                    pass
                                    # 51: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects460.appendleft(tmp464)
                if len(subjects460) >= 1 and isinstance(subjects460[0], Add):
                    tmp467 = subjects460.popleft()
                    associative1 = tmp467
                    associative_type1 = type(tmp467)
                    subjects468 = deque(tmp467._args)
                    matcher = CommutativeMatcher110374.get()
                    tmp469 = subjects468
                    subjects468 = []
                    for s in tmp469:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp469, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 110380
                            if len(subjects460) == 0:
                                pass
                                # State 110381
                                if len(subjects) == 0:
                                    pass
                                    # 53: b*acos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                    subjects460.appendleft(tmp467)
                subjects.appendleft(tmp459)
            if len(subjects) >= 1 and isinstance(subjects[0], atan):
                tmp470 = subjects.popleft()
                subjects471 = deque(tmp470._args)
                # State 112613
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 112614
                    if len(subjects471) >= 1:
                        tmp473 = subjects471.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp473)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 112615
                            if len(subjects471) == 0:
                                pass
                                # State 112616
                                if len(subjects) == 0:
                                    pass
                                    # 54: b*atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        subjects471.appendleft(tmp473)
                if len(subjects471) >= 1 and isinstance(subjects471[0], Mul):
                    tmp475 = subjects471.popleft()
                    associative1 = tmp475
                    associative_type1 = type(tmp475)
                    subjects476 = deque(tmp475._args)
                    matcher = CommutativeMatcher112618.get()
                    tmp477 = subjects476
                    subjects476 = []
                    for s in tmp477:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp477, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 112619
                            if len(subjects471) == 0:
                                pass
                                # State 112620
                                if len(subjects) == 0:
                                    pass
                                    # 54: b*atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects471.appendleft(tmp475)
                if len(subjects471) >= 1 and isinstance(subjects471[0], Add):
                    tmp478 = subjects471.popleft()
                    associative1 = tmp478
                    associative_type1 = type(tmp478)
                    subjects479 = deque(tmp478._args)
                    matcher = CommutativeMatcher115476.get()
                    tmp480 = subjects479
                    subjects479 = []
                    for s in tmp480:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp480, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 115482
                            if len(subjects471) == 0:
                                pass
                                # State 115483
                                if len(subjects) == 0:
                                    pass
                                    # 56: b*atan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                    subjects471.appendleft(tmp478)
                subjects.appendleft(tmp470)
            if len(subjects) >= 1 and isinstance(subjects[0], acot):
                tmp481 = subjects.popleft()
                subjects482 = deque(tmp481._args)
                # State 112707
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 112708
                    if len(subjects482) >= 1:
                        tmp484 = subjects482.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp484)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 112709
                            if len(subjects482) == 0:
                                pass
                                # State 112710
                                if len(subjects) == 0:
                                    pass
                                    # 55: b*acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        subjects482.appendleft(tmp484)
                if len(subjects482) >= 1 and isinstance(subjects482[0], Mul):
                    tmp486 = subjects482.popleft()
                    associative1 = tmp486
                    associative_type1 = type(tmp486)
                    subjects487 = deque(tmp486._args)
                    matcher = CommutativeMatcher112712.get()
                    tmp488 = subjects487
                    subjects487 = []
                    for s in tmp488:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp488, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 112713
                            if len(subjects482) == 0:
                                pass
                                # State 112714
                                if len(subjects) == 0:
                                    pass
                                    # 55: b*acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects482.appendleft(tmp486)
                if len(subjects482) >= 1 and isinstance(subjects482[0], Add):
                    tmp489 = subjects482.popleft()
                    associative1 = tmp489
                    associative_type1 = type(tmp489)
                    subjects490 = deque(tmp489._args)
                    matcher = CommutativeMatcher115572.get()
                    tmp491 = subjects490
                    subjects490 = []
                    for s in tmp491:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp491, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 115578
                            if len(subjects482) == 0:
                                pass
                                # State 115579
                                if len(subjects) == 0:
                                    pass
                                    # 57: b*acot(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                    subjects482.appendleft(tmp489)
                subjects.appendleft(tmp481)
            if len(subjects) >= 1 and isinstance(subjects[0], sinh):
                tmp492 = subjects.popleft()
                subjects493 = deque(tmp492._args)
                # State 122841
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122842
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 122843
                        if len(subjects493) >= 1 and isinstance(subjects493[0], Pow):
                            tmp496 = subjects493.popleft()
                            subjects497 = deque(tmp496._args)
                            # State 122844
                            if len(subjects497) >= 1:
                                tmp498 = subjects497.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.1.1', tmp498)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 122845
                                    if len(subjects497) >= 1:
                                        tmp500 = subjects497.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.1.2', tmp500)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 122846
                                            if len(subjects497) == 0:
                                                pass
                                                # State 122847
                                                if len(subjects493) == 0:
                                                    pass
                                                    # State 122848
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 58: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                                        # 60: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                        # 62: b*sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        subjects497.appendleft(tmp500)
                                subjects497.appendleft(tmp498)
                            subjects493.appendleft(tmp496)
                    if len(subjects493) >= 1 and isinstance(subjects493[0], Mul):
                        tmp502 = subjects493.popleft()
                        associative1 = tmp502
                        associative_type1 = type(tmp502)
                        subjects503 = deque(tmp502._args)
                        matcher = CommutativeMatcher122850.get()
                        tmp504 = subjects503
                        subjects503 = []
                        for s in tmp504:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp504, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 122855
                                if len(subjects493) == 0:
                                    pass
                                    # State 122856
                                    if len(subjects) == 0:
                                        pass
                                        # 58: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                        # 60: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                        # 62: b*sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        subjects493.appendleft(tmp502)
                if len(subjects493) >= 1:
                    tmp505 = subjects493.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp505)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 123371
                        if len(subjects493) == 0:
                            pass
                            # State 123372
                            if len(subjects) == 0:
                                pass
                                # 64: b*sinh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                    subjects493.appendleft(tmp505)
                if len(subjects493) >= 1 and isinstance(subjects493[0], Add):
                    tmp507 = subjects493.popleft()
                    associative1 = tmp507
                    associative_type1 = type(tmp507)
                    subjects508 = deque(tmp507._args)
                    matcher = CommutativeMatcher122858.get()
                    tmp509 = subjects508
                    subjects508 = []
                    for s in tmp509:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp509, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122871
                            if len(subjects493) == 0:
                                pass
                                # State 122872
                                if len(subjects) == 0:
                                    pass
                                    # 58: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    # 60: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    # 62: b*sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                    subjects493.appendleft(tmp507)
                subjects.appendleft(tmp492)
            if len(subjects) >= 1 and isinstance(subjects[0], cosh):
                tmp510 = subjects.popleft()
                subjects511 = deque(tmp510._args)
                # State 123008
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 123009
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 123010
                        if len(subjects511) >= 1 and isinstance(subjects511[0], Pow):
                            tmp514 = subjects511.popleft()
                            subjects515 = deque(tmp514._args)
                            # State 123011
                            if len(subjects515) >= 1:
                                tmp516 = subjects515.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.1.1', tmp516)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 123012
                                    if len(subjects515) >= 1:
                                        tmp518 = subjects515.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.1.2', tmp518)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 123013
                                            if len(subjects515) == 0:
                                                pass
                                                # State 123014
                                                if len(subjects511) == 0:
                                                    pass
                                                    # State 123015
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 59: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                                        # 61: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                        # 63: b*cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        subjects515.appendleft(tmp518)
                                subjects515.appendleft(tmp516)
                            subjects511.appendleft(tmp514)
                    if len(subjects511) >= 1 and isinstance(subjects511[0], Mul):
                        tmp520 = subjects511.popleft()
                        associative1 = tmp520
                        associative_type1 = type(tmp520)
                        subjects521 = deque(tmp520._args)
                        matcher = CommutativeMatcher123017.get()
                        tmp522 = subjects521
                        subjects521 = []
                        for s in tmp522:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp522, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 123022
                                if len(subjects511) == 0:
                                    pass
                                    # State 123023
                                    if len(subjects) == 0:
                                        pass
                                        # 59: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                        # 61: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                        # 63: b*cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        subjects511.appendleft(tmp520)
                if len(subjects511) >= 1:
                    tmp523 = subjects511.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp523)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 123411
                        if len(subjects511) == 0:
                            pass
                            # State 123412
                            if len(subjects) == 0:
                                pass
                                # 65: b*cosh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                    subjects511.appendleft(tmp523)
                if len(subjects511) >= 1 and isinstance(subjects511[0], Add):
                    tmp525 = subjects511.popleft()
                    associative1 = tmp525
                    associative_type1 = type(tmp525)
                    subjects526 = deque(tmp525._args)
                    matcher = CommutativeMatcher123025.get()
                    tmp527 = subjects526
                    subjects526 = []
                    for s in tmp527:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp527, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 123038
                            if len(subjects511) == 0:
                                pass
                                # State 123039
                                if len(subjects) == 0:
                                    pass
                                    # 59: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    # 61: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    # 63: b*cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                    subjects511.appendleft(tmp525)
                subjects.appendleft(tmp510)
            if len(subjects) >= 1 and isinstance(subjects[0], tanh):
                tmp528 = subjects.popleft()
                subjects529 = deque(tmp528._args)
                # State 126607
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 126608
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 126609
                        if len(subjects529) >= 1 and isinstance(subjects529[0], Pow):
                            tmp532 = subjects529.popleft()
                            subjects533 = deque(tmp532._args)
                            # State 126610
                            if len(subjects533) >= 1:
                                tmp534 = subjects533.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.1.1', tmp534)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 126611
                                    if len(subjects533) >= 1:
                                        tmp536 = subjects533.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.1.2', tmp536)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 126612
                                            if len(subjects533) == 0:
                                                pass
                                                # State 126613
                                                if len(subjects529) == 0:
                                                    pass
                                                    # State 126614
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 66: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                        # 68: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                        # 70: b*tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                        subjects533.appendleft(tmp536)
                                subjects533.appendleft(tmp534)
                            subjects529.appendleft(tmp532)
                    if len(subjects529) >= 1 and isinstance(subjects529[0], Mul):
                        tmp538 = subjects529.popleft()
                        associative1 = tmp538
                        associative_type1 = type(tmp538)
                        subjects539 = deque(tmp538._args)
                        matcher = CommutativeMatcher126616.get()
                        tmp540 = subjects539
                        subjects539 = []
                        for s in tmp540:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp540, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 126621
                                if len(subjects529) == 0:
                                    pass
                                    # State 126622
                                    if len(subjects) == 0:
                                        pass
                                        # 66: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                        # 68: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                        # 70: b*tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        subjects529.appendleft(tmp538)
                if len(subjects529) >= 1:
                    tmp541 = subjects529.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp541)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 127343
                        if len(subjects529) == 0:
                            pass
                            # State 127344
                            if len(subjects) == 0:
                                pass
                                # 72: b*tanh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                    subjects529.appendleft(tmp541)
                if len(subjects529) >= 1 and isinstance(subjects529[0], Add):
                    tmp543 = subjects529.popleft()
                    associative1 = tmp543
                    associative_type1 = type(tmp543)
                    subjects544 = deque(tmp543._args)
                    matcher = CommutativeMatcher126624.get()
                    tmp545 = subjects544
                    subjects544 = []
                    for s in tmp545:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp545, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 126637
                            if len(subjects529) == 0:
                                pass
                                # State 126638
                                if len(subjects) == 0:
                                    pass
                                    # 66: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                    # 68: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                    # 70: b*tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                    subjects529.appendleft(tmp543)
                subjects.appendleft(tmp528)
            if len(subjects) >= 1 and isinstance(subjects[0], asinh):
                tmp546 = subjects.popleft()
                subjects547 = deque(tmp546._args)
                # State 137717
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 137718
                    if len(subjects547) >= 1:
                        tmp549 = subjects547.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp549)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 137719
                            if len(subjects547) == 0:
                                pass
                                # State 137720
                                if len(subjects) == 0:
                                    pass
                                    # 82: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        subjects547.appendleft(tmp549)
                if len(subjects547) >= 1 and isinstance(subjects547[0], Mul):
                    tmp551 = subjects547.popleft()
                    associative1 = tmp551
                    associative_type1 = type(tmp551)
                    subjects552 = deque(tmp551._args)
                    matcher = CommutativeMatcher137722.get()
                    tmp553 = subjects552
                    subjects552 = []
                    for s in tmp553:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp553, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 137723
                            if len(subjects547) == 0:
                                pass
                                # State 137724
                                if len(subjects) == 0:
                                    pass
                                    # 82: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects547.appendleft(tmp551)
                if len(subjects547) >= 1 and isinstance(subjects547[0], Add):
                    tmp554 = subjects547.popleft()
                    associative1 = tmp554
                    associative_type1 = type(tmp554)
                    subjects555 = deque(tmp554._args)
                    matcher = CommutativeMatcher140013.get()
                    tmp556 = subjects555
                    subjects555 = []
                    for s in tmp556:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp556, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 140019
                            if len(subjects547) == 0:
                                pass
                                # State 140020
                                if len(subjects) == 0:
                                    pass
                                    # 84: b*asinh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                    subjects547.appendleft(tmp554)
                subjects.appendleft(tmp546)
            if len(subjects) >= 1 and isinstance(subjects[0], acosh):
                tmp557 = subjects.popleft()
                subjects558 = deque(tmp557._args)
                # State 137811
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 137812
                    if len(subjects558) >= 1:
                        tmp560 = subjects558.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp560)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 137813
                            if len(subjects558) == 0:
                                pass
                                # State 137814
                                if len(subjects) == 0:
                                    pass
                                    # 83: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        subjects558.appendleft(tmp560)
                if len(subjects558) >= 1 and isinstance(subjects558[0], Mul):
                    tmp562 = subjects558.popleft()
                    associative1 = tmp562
                    associative_type1 = type(tmp562)
                    subjects563 = deque(tmp562._args)
                    matcher = CommutativeMatcher137816.get()
                    tmp564 = subjects563
                    subjects563 = []
                    for s in tmp564:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp564, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 137817
                            if len(subjects558) == 0:
                                pass
                                # State 137818
                                if len(subjects) == 0:
                                    pass
                                    # 83: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects558.appendleft(tmp562)
                if len(subjects558) >= 1 and isinstance(subjects558[0], Add):
                    tmp565 = subjects558.popleft()
                    associative1 = tmp565
                    associative_type1 = type(tmp565)
                    subjects566 = deque(tmp565._args)
                    matcher = CommutativeMatcher140109.get()
                    tmp567 = subjects566
                    subjects566 = []
                    for s in tmp567:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp567, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 140115
                            if len(subjects558) == 0:
                                pass
                                # State 140116
                                if len(subjects) == 0:
                                    pass
                                    # 85: b*acosh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                    subjects558.appendleft(tmp565)
                subjects.appendleft(tmp557)
            if len(subjects) >= 1 and isinstance(subjects[0], atanh):
                tmp568 = subjects.popleft()
                subjects569 = deque(tmp568._args)
                # State 142245
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 142246
                    if len(subjects569) >= 1:
                        tmp571 = subjects569.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp571)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 142247
                            if len(subjects569) == 0:
                                pass
                                # State 142248
                                if len(subjects) == 0:
                                    pass
                                    # 86: b*atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        subjects569.appendleft(tmp571)
                if len(subjects569) >= 1 and isinstance(subjects569[0], Mul):
                    tmp573 = subjects569.popleft()
                    associative1 = tmp573
                    associative_type1 = type(tmp573)
                    subjects574 = deque(tmp573._args)
                    matcher = CommutativeMatcher142250.get()
                    tmp575 = subjects574
                    subjects574 = []
                    for s in tmp575:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp575, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 142251
                            if len(subjects569) == 0:
                                pass
                                # State 142252
                                if len(subjects) == 0:
                                    pass
                                    # 86: b*atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects569.appendleft(tmp573)
                if len(subjects569) >= 1 and isinstance(subjects569[0], Add):
                    tmp576 = subjects569.popleft()
                    associative1 = tmp576
                    associative_type1 = type(tmp576)
                    subjects577 = deque(tmp576._args)
                    matcher = CommutativeMatcher144701.get()
                    tmp578 = subjects577
                    subjects577 = []
                    for s in tmp578:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp578, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 144707
                            if len(subjects569) == 0:
                                pass
                                # State 144708
                                if len(subjects) == 0:
                                    pass
                                    # 88: b*atanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                    subjects569.appendleft(tmp576)
                subjects.appendleft(tmp568)
            if len(subjects) >= 1 and isinstance(subjects[0], acoth):
                tmp579 = subjects.popleft()
                subjects580 = deque(tmp579._args)
                # State 142339
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 142340
                    if len(subjects580) >= 1:
                        tmp582 = subjects580.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.0', tmp582)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 142341
                            if len(subjects580) == 0:
                                pass
                                # State 142342
                                if len(subjects) == 0:
                                    pass
                                    # 87: b*acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                        subjects580.appendleft(tmp582)
                if len(subjects580) >= 1 and isinstance(subjects580[0], Mul):
                    tmp584 = subjects580.popleft()
                    associative1 = tmp584
                    associative_type1 = type(tmp584)
                    subjects585 = deque(tmp584._args)
                    matcher = CommutativeMatcher142344.get()
                    tmp586 = subjects585
                    subjects585 = []
                    for s in tmp586:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp586, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 142345
                            if len(subjects580) == 0:
                                pass
                                # State 142346
                                if len(subjects) == 0:
                                    pass
                                    # 87: b*acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects580.appendleft(tmp584)
                if len(subjects580) >= 1 and isinstance(subjects580[0], Add):
                    tmp587 = subjects580.popleft()
                    associative1 = tmp587
                    associative_type1 = type(tmp587)
                    subjects588 = deque(tmp587._args)
                    matcher = CommutativeMatcher144797.get()
                    tmp589 = subjects588
                    subjects588 = []
                    for s in tmp589:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp589, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 144803
                            if len(subjects580) == 0:
                                pass
                                # State 144804
                                if len(subjects) == 0:
                                    pass
                                    # 89: b*acoth(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                    subjects580.appendleft(tmp587)
                subjects.appendleft(tmp579)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 8155
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 8156
                if len(subjects) >= 1:
                    tmp592 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.1', tmp592)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8157
                        if len(subjects) == 0:
                            pass
                            # 1: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48)
                            # 3: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f587) and (cons_f683)
                    subjects.appendleft(tmp592)
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 10887
                    if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                        tmp595 = subjects.popleft()
                        subjects596 = deque(tmp595._args)
                        # State 10888
                        if len(subjects596) >= 1:
                            tmp597 = subjects596.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1', tmp597)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 10889
                                if len(subjects596) >= 1 and subjects596[0] == -1:
                                    tmp599 = subjects596.popleft()
                                    # State 10890
                                    if len(subjects596) == 0:
                                        pass
                                        # State 10891
                                        if len(subjects) == 0:
                                            pass
                                            # 6: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                    subjects596.appendleft(tmp599)
                            subjects596.appendleft(tmp597)
                        subjects.appendleft(tmp595)
                if len(subjects) >= 1:
                    tmp600 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1', tmp600)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11164
                        if len(subjects) == 0:
                            pass
                            # 8: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809)
                    subjects.appendleft(tmp600)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp602 = subjects.popleft()
                    associative1 = tmp602
                    associative_type1 = type(tmp602)
                    subjects603 = deque(tmp602._args)
                    matcher = CommutativeMatcher10893.get()
                    tmp604 = subjects603
                    subjects603 = []
                    for s in tmp604:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp604, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 10898
                            if len(subjects) == 0:
                                pass
                                # 6: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                    subjects.appendleft(tmp602)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.3_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 68820
                if len(subjects) >= 1 and isinstance(subjects[0], sin):
                    tmp606 = subjects.popleft()
                    subjects607 = deque(tmp606._args)
                    # State 68821
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 68822
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68823
                            if len(subjects607) >= 1:
                                tmp610 = subjects607.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.3.1.0', tmp610)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 68824
                                    if len(subjects607) == 0:
                                        pass
                                        # State 68825
                                        if len(subjects) == 0:
                                            pass
                                            # 15: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                subjects607.appendleft(tmp610)
                        if len(subjects607) >= 1 and isinstance(subjects607[0], Mul):
                            tmp612 = subjects607.popleft()
                            associative1 = tmp612
                            associative_type1 = type(tmp612)
                            subjects613 = deque(tmp612._args)
                            matcher = CommutativeMatcher68827.get()
                            tmp614 = subjects613
                            subjects613 = []
                            for s in tmp614:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp614, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 68828
                                    if len(subjects607) == 0:
                                        pass
                                        # State 68829
                                        if len(subjects) == 0:
                                            pass
                                            # 15: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                            subjects607.appendleft(tmp612)
                    if len(subjects607) >= 1 and isinstance(subjects607[0], Add):
                        tmp615 = subjects607.popleft()
                        associative1 = tmp615
                        associative_type1 = type(tmp615)
                        subjects616 = deque(tmp615._args)
                        matcher = CommutativeMatcher68831.get()
                        tmp617 = subjects616
                        subjects616 = []
                        for s in tmp617:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp617, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 68837
                                if len(subjects607) == 0:
                                    pass
                                    # State 68838
                                    if len(subjects) == 0:
                                        pass
                                        # 15: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        subjects607.appendleft(tmp615)
                    subjects.appendleft(tmp606)
                if len(subjects) >= 1 and isinstance(subjects[0], cos):
                    tmp618 = subjects.popleft()
                    subjects619 = deque(tmp618._args)
                    # State 69102
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 69103
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 69104
                            if len(subjects619) >= 1:
                                tmp622 = subjects619.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.3.1.0', tmp622)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 69105
                                    if len(subjects619) == 0:
                                        pass
                                        # State 69106
                                        if len(subjects) == 0:
                                            pass
                                            # 17: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                subjects619.appendleft(tmp622)
                        if len(subjects619) >= 1 and isinstance(subjects619[0], Mul):
                            tmp624 = subjects619.popleft()
                            associative1 = tmp624
                            associative_type1 = type(tmp624)
                            subjects625 = deque(tmp624._args)
                            matcher = CommutativeMatcher69108.get()
                            tmp626 = subjects625
                            subjects625 = []
                            for s in tmp626:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp626, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 69109
                                    if len(subjects619) == 0:
                                        pass
                                        # State 69110
                                        if len(subjects) == 0:
                                            pass
                                            # 17: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                            subjects619.appendleft(tmp624)
                    if len(subjects619) >= 1 and isinstance(subjects619[0], Add):
                        tmp627 = subjects619.popleft()
                        associative1 = tmp627
                        associative_type1 = type(tmp627)
                        subjects628 = deque(tmp627._args)
                        matcher = CommutativeMatcher69112.get()
                        tmp629 = subjects628
                        subjects628 = []
                        for s in tmp629:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp629, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 69118
                                if len(subjects619) == 0:
                                    pass
                                    # State 69119
                                    if len(subjects) == 0:
                                        pass
                                        # 17: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        subjects619.appendleft(tmp627)
                    subjects.appendleft(tmp618)
                if len(subjects) >= 1 and isinstance(subjects[0], tan):
                    tmp630 = subjects.popleft()
                    subjects631 = deque(tmp630._args)
                    # State 83425
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83426
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83427
                            if len(subjects631) >= 1:
                                tmp634 = subjects631.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.3.1.0', tmp634)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83428
                                    if len(subjects631) == 0:
                                        pass
                                        # State 83429
                                        if len(subjects) == 0:
                                            pass
                                            # 27: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                subjects631.appendleft(tmp634)
                        if len(subjects631) >= 1 and isinstance(subjects631[0], Mul):
                            tmp636 = subjects631.popleft()
                            associative1 = tmp636
                            associative_type1 = type(tmp636)
                            subjects637 = deque(tmp636._args)
                            matcher = CommutativeMatcher83431.get()
                            tmp638 = subjects637
                            subjects637 = []
                            for s in tmp638:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp638, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83432
                                    if len(subjects631) == 0:
                                        pass
                                        # State 83433
                                        if len(subjects) == 0:
                                            pass
                                            # 27: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                            subjects631.appendleft(tmp636)
                    if len(subjects631) >= 1 and isinstance(subjects631[0], Add):
                        tmp639 = subjects631.popleft()
                        associative1 = tmp639
                        associative_type1 = type(tmp639)
                        subjects640 = deque(tmp639._args)
                        matcher = CommutativeMatcher83435.get()
                        tmp641 = subjects640
                        subjects640 = []
                        for s in tmp641:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp641, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83441
                                if len(subjects631) == 0:
                                    pass
                                    # State 83442
                                    if len(subjects) == 0:
                                        pass
                                        # 27: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                        subjects631.appendleft(tmp639)
                    subjects.appendleft(tmp630)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.5_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 83713
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp643 = subjects.popleft()
                    subjects644 = deque(tmp643._args)
                    # State 83714
                    if len(subjects644) >= 1 and isinstance(subjects644[0], tan):
                        tmp645 = subjects644.popleft()
                        subjects646 = deque(tmp645._args)
                        # State 83715
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83716
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83717
                                if len(subjects646) >= 1:
                                    tmp649 = subjects646.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.4.1.0', tmp649)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83718
                                        if len(subjects646) == 0:
                                            pass
                                            # State 83719
                                            if len(subjects644) >= 1 and subjects644[0] == -1:
                                                tmp651 = subjects644.popleft()
                                                # State 83720
                                                if len(subjects644) == 0:
                                                    pass
                                                    # State 83721
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 29: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                subjects644.appendleft(tmp651)
                                    subjects646.appendleft(tmp649)
                            if len(subjects646) >= 1 and isinstance(subjects646[0], Mul):
                                tmp652 = subjects646.popleft()
                                associative1 = tmp652
                                associative_type1 = type(tmp652)
                                subjects653 = deque(tmp652._args)
                                matcher = CommutativeMatcher83723.get()
                                tmp654 = subjects653
                                subjects653 = []
                                for s in tmp654:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp654, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 83724
                                        if len(subjects646) == 0:
                                            pass
                                            # State 83725
                                            if len(subjects644) >= 1 and subjects644[0] == -1:
                                                tmp655 = subjects644.popleft()
                                                # State 83726
                                                if len(subjects644) == 0:
                                                    pass
                                                    # State 83727
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 29: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                subjects644.appendleft(tmp655)
                                subjects646.appendleft(tmp652)
                        if len(subjects646) >= 1 and isinstance(subjects646[0], Add):
                            tmp656 = subjects646.popleft()
                            associative1 = tmp656
                            associative_type1 = type(tmp656)
                            subjects657 = deque(tmp656._args)
                            matcher = CommutativeMatcher83729.get()
                            tmp658 = subjects657
                            subjects657 = []
                            for s in tmp658:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp658, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83735
                                    if len(subjects646) == 0:
                                        pass
                                        # State 83736
                                        if len(subjects644) >= 1 and subjects644[0] == -1:
                                            tmp659 = subjects644.popleft()
                                            # State 83737
                                            if len(subjects644) == 0:
                                                pass
                                                # State 83738
                                                if len(subjects) == 0:
                                                    pass
                                                    # 29: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects644.appendleft(tmp659)
                            subjects646.appendleft(tmp656)
                        subjects644.appendleft(tmp645)
                    if len(subjects644) >= 1 and isinstance(subjects644[0], cos):
                        tmp660 = subjects644.popleft()
                        subjects661 = deque(tmp660._args)
                        # State 95429
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95430
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95431
                                if len(subjects661) >= 1:
                                    tmp664 = subjects661.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.4.1.0', tmp664)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95432
                                        if len(subjects661) == 0:
                                            pass
                                            # State 95433
                                            if len(subjects644) >= 1 and subjects644[0] == -1:
                                                tmp666 = subjects644.popleft()
                                                # State 95434
                                                if len(subjects644) == 0:
                                                    pass
                                                    # State 95435
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 39: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                subjects644.appendleft(tmp666)
                                    subjects661.appendleft(tmp664)
                            if len(subjects661) >= 1 and isinstance(subjects661[0], Mul):
                                tmp667 = subjects661.popleft()
                                associative1 = tmp667
                                associative_type1 = type(tmp667)
                                subjects668 = deque(tmp667._args)
                                matcher = CommutativeMatcher95437.get()
                                tmp669 = subjects668
                                subjects668 = []
                                for s in tmp669:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp669, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95438
                                        if len(subjects661) == 0:
                                            pass
                                            # State 95439
                                            if len(subjects644) >= 1 and subjects644[0] == -1:
                                                tmp670 = subjects644.popleft()
                                                # State 95440
                                                if len(subjects644) == 0:
                                                    pass
                                                    # State 95441
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 39: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                subjects644.appendleft(tmp670)
                                subjects661.appendleft(tmp667)
                        if len(subjects661) >= 1 and isinstance(subjects661[0], Add):
                            tmp671 = subjects661.popleft()
                            associative1 = tmp671
                            associative_type1 = type(tmp671)
                            subjects672 = deque(tmp671._args)
                            matcher = CommutativeMatcher95443.get()
                            tmp673 = subjects672
                            subjects672 = []
                            for s in tmp673:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp673, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95449
                                    if len(subjects661) == 0:
                                        pass
                                        # State 95450
                                        if len(subjects644) >= 1 and subjects644[0] == -1:
                                            tmp674 = subjects644.popleft()
                                            # State 95451
                                            if len(subjects644) == 0:
                                                pass
                                                # State 95452
                                                if len(subjects) == 0:
                                                    pass
                                                    # 39: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects644.appendleft(tmp674)
                            subjects661.appendleft(tmp671)
                        subjects644.appendleft(tmp660)
                    if len(subjects644) >= 1 and isinstance(subjects644[0], sin):
                        tmp675 = subjects644.popleft()
                        subjects676 = deque(tmp675._args)
                        # State 95825
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95826
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95827
                                if len(subjects676) >= 1:
                                    tmp679 = subjects676.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.4.1.0', tmp679)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95828
                                        if len(subjects676) == 0:
                                            pass
                                            # State 95829
                                            if len(subjects644) >= 1 and subjects644[0] == -1:
                                                tmp681 = subjects644.popleft()
                                                # State 95830
                                                if len(subjects644) == 0:
                                                    pass
                                                    # State 95831
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 41: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                subjects644.appendleft(tmp681)
                                    subjects676.appendleft(tmp679)
                            if len(subjects676) >= 1 and isinstance(subjects676[0], Mul):
                                tmp682 = subjects676.popleft()
                                associative1 = tmp682
                                associative_type1 = type(tmp682)
                                subjects683 = deque(tmp682._args)
                                matcher = CommutativeMatcher95833.get()
                                tmp684 = subjects683
                                subjects683 = []
                                for s in tmp684:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp684, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95834
                                        if len(subjects676) == 0:
                                            pass
                                            # State 95835
                                            if len(subjects644) >= 1 and subjects644[0] == -1:
                                                tmp685 = subjects644.popleft()
                                                # State 95836
                                                if len(subjects644) == 0:
                                                    pass
                                                    # State 95837
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 41: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                subjects644.appendleft(tmp685)
                                subjects676.appendleft(tmp682)
                        if len(subjects676) >= 1 and isinstance(subjects676[0], Add):
                            tmp686 = subjects676.popleft()
                            associative1 = tmp686
                            associative_type1 = type(tmp686)
                            subjects687 = deque(tmp686._args)
                            matcher = CommutativeMatcher95839.get()
                            tmp688 = subjects687
                            subjects687 = []
                            for s in tmp688:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp688, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95845
                                    if len(subjects676) == 0:
                                        pass
                                        # State 95846
                                        if len(subjects644) >= 1 and subjects644[0] == -1:
                                            tmp689 = subjects644.popleft()
                                            # State 95847
                                            if len(subjects644) == 0:
                                                pass
                                                # State 95848
                                                if len(subjects) == 0:
                                                    pass
                                                    # 41: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects644.appendleft(tmp689)
                            subjects676.appendleft(tmp686)
                        subjects644.appendleft(tmp675)
                    subjects.appendleft(tmp643)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp690 = subjects.popleft()
                subjects691 = deque(tmp690._args)
                # State 8158
                if len(subjects691) >= 1:
                    tmp692 = subjects691.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp692)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8159
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8160
                            if len(subjects691) == 0:
                                pass
                                # State 8161
                                if len(subjects) == 0:
                                    pass
                                    # 1: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48)
                                    # 3: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f587) and (cons_f683)
                        if len(subjects691) >= 1:
                            tmp695 = subjects691.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2_1', tmp695)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 8160
                                if len(subjects691) == 0:
                                    pass
                                    # State 8161
                                    if len(subjects) == 0:
                                        pass
                                        # 1: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48)
                                        # 3: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f587) and (cons_f683)
                            subjects691.appendleft(tmp695)
                    subjects691.appendleft(tmp692)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 10899
                    if len(subjects691) >= 1 and isinstance(subjects691[0], Pow):
                        tmp698 = subjects691.popleft()
                        subjects699 = deque(tmp698._args)
                        # State 10900
                        if len(subjects699) >= 1:
                            tmp700 = subjects699.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1', tmp700)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 10901
                                if len(subjects699) >= 1 and subjects699[0] == -1:
                                    tmp702 = subjects699.popleft()
                                    # State 10902
                                    if len(subjects699) == 0:
                                        pass
                                        # State 10903
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.2_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 10904
                                            if len(subjects691) == 0:
                                                pass
                                                # State 10905
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                        if len(subjects691) >= 1:
                                            tmp704 = subjects691.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2_1', tmp704)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 10904
                                                if len(subjects691) == 0:
                                                    pass
                                                    # State 10905
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                            subjects691.appendleft(tmp704)
                                    subjects699.appendleft(tmp702)
                            subjects699.appendleft(tmp700)
                        subjects691.appendleft(tmp698)
                if len(subjects691) >= 1:
                    tmp706 = subjects691.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.1', tmp706)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11165
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11166
                            if len(subjects691) == 0:
                                pass
                                # State 11167
                                if len(subjects) == 0:
                                    pass
                                    # 8: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809)
                        if len(subjects691) >= 1:
                            tmp709 = subjects691.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2_1', tmp709)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 11166
                                if len(subjects691) == 0:
                                    pass
                                    # State 11167
                                    if len(subjects) == 0:
                                        pass
                                        # 8: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809)
                            subjects691.appendleft(tmp709)
                    subjects691.appendleft(tmp706)
                if len(subjects691) >= 1 and isinstance(subjects691[0], Mul):
                    tmp711 = subjects691.popleft()
                    associative1 = tmp711
                    associative_type1 = type(tmp711)
                    subjects712 = deque(tmp711._args)
                    matcher = CommutativeMatcher10907.get()
                    tmp713 = subjects712
                    subjects712 = []
                    for s in tmp713:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp713, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 10912
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2_1', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 10913
                                if len(subjects691) == 0:
                                    pass
                                    # State 10914
                                    if len(subjects) == 0:
                                        pass
                                        # 6: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                            if len(subjects691) >= 1:
                                tmp715 = []
                                tmp715.append(subjects691.popleft())
                                while True:
                                    if len(tmp715) > 1:
                                        tmp716 = create_operation_expression(associative1, tmp715)
                                    elif len(tmp715) == 1:
                                        tmp716 = tmp715[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2_1', tmp716)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 10913
                                        if len(subjects691) == 0:
                                            pass
                                            # State 10914
                                            if len(subjects) == 0:
                                                pass
                                                # 6: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                                    if len(subjects691) == 0:
                                        break
                                    tmp715.append(subjects691.popleft())
                                subjects691.extendleft(reversed(tmp715))
                    subjects691.appendleft(tmp711)
                if len(subjects691) >= 1 and isinstance(subjects691[0], sin):
                    tmp718 = subjects691.popleft()
                    subjects719 = deque(tmp718._args)
                    # State 68839
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 68840
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68841
                            if len(subjects719) >= 1:
                                tmp722 = subjects719.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp722)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 68842
                                    if len(subjects719) == 0:
                                        pass
                                        # State 68843
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.3_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68844
                                            if len(subjects691) == 0:
                                                pass
                                                # State 68845
                                                if len(subjects) == 0:
                                                    pass
                                                    # 15: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        if len(subjects691) >= 1:
                                            tmp725 = subjects691.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3_1', tmp725)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 68844
                                                if len(subjects691) == 0:
                                                    pass
                                                    # State 68845
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 15: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects691.appendleft(tmp725)
                                subjects719.appendleft(tmp722)
                        if len(subjects719) >= 1 and isinstance(subjects719[0], Mul):
                            tmp727 = subjects719.popleft()
                            associative1 = tmp727
                            associative_type1 = type(tmp727)
                            subjects728 = deque(tmp727._args)
                            matcher = CommutativeMatcher68847.get()
                            tmp729 = subjects728
                            subjects728 = []
                            for s in tmp729:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp729, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 68848
                                    if len(subjects719) == 0:
                                        pass
                                        # State 68849
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68850
                                            if len(subjects691) == 0:
                                                pass
                                                # State 68851
                                                if len(subjects) == 0:
                                                    pass
                                                    # 15: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        if len(subjects691) >= 1:
                                            tmp731 = subjects691.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3_1', tmp731)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 68850
                                                if len(subjects691) == 0:
                                                    pass
                                                    # State 68851
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 15: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects691.appendleft(tmp731)
                            subjects719.appendleft(tmp727)
                    if len(subjects719) >= 1 and isinstance(subjects719[0], Add):
                        tmp733 = subjects719.popleft()
                        associative1 = tmp733
                        associative_type1 = type(tmp733)
                        subjects734 = deque(tmp733._args)
                        matcher = CommutativeMatcher68853.get()
                        tmp735 = subjects734
                        subjects734 = []
                        for s in tmp735:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp735, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 68859
                                if len(subjects719) == 0:
                                    pass
                                    # State 68860
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 68861
                                        if len(subjects691) == 0:
                                            pass
                                            # State 68862
                                            if len(subjects) == 0:
                                                pass
                                                # 15: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                    if len(subjects691) >= 1:
                                        tmp737 = subjects691.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3_1', tmp737)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68861
                                            if len(subjects691) == 0:
                                                pass
                                                # State 68862
                                                if len(subjects) == 0:
                                                    pass
                                                    # 15: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        subjects691.appendleft(tmp737)
                        subjects719.appendleft(tmp733)
                    subjects691.appendleft(tmp718)
                if len(subjects691) >= 1 and isinstance(subjects691[0], cos):
                    tmp739 = subjects691.popleft()
                    subjects740 = deque(tmp739._args)
                    # State 69120
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 69121
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 69122
                            if len(subjects740) >= 1:
                                tmp743 = subjects740.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp743)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 69123
                                    if len(subjects740) == 0:
                                        pass
                                        # State 69124
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.3_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69125
                                            if len(subjects691) == 0:
                                                pass
                                                # State 69126
                                                if len(subjects) == 0:
                                                    pass
                                                    # 17: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        if len(subjects691) >= 1:
                                            tmp746 = subjects691.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3_1', tmp746)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 69125
                                                if len(subjects691) == 0:
                                                    pass
                                                    # State 69126
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 17: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects691.appendleft(tmp746)
                                subjects740.appendleft(tmp743)
                        if len(subjects740) >= 1 and isinstance(subjects740[0], Mul):
                            tmp748 = subjects740.popleft()
                            associative1 = tmp748
                            associative_type1 = type(tmp748)
                            subjects749 = deque(tmp748._args)
                            matcher = CommutativeMatcher69128.get()
                            tmp750 = subjects749
                            subjects749 = []
                            for s in tmp750:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp750, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 69129
                                    if len(subjects740) == 0:
                                        pass
                                        # State 69130
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69131
                                            if len(subjects691) == 0:
                                                pass
                                                # State 69132
                                                if len(subjects) == 0:
                                                    pass
                                                    # 17: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        if len(subjects691) >= 1:
                                            tmp752 = subjects691.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3_1', tmp752)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 69131
                                                if len(subjects691) == 0:
                                                    pass
                                                    # State 69132
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 17: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects691.appendleft(tmp752)
                            subjects740.appendleft(tmp748)
                    if len(subjects740) >= 1 and isinstance(subjects740[0], Add):
                        tmp754 = subjects740.popleft()
                        associative1 = tmp754
                        associative_type1 = type(tmp754)
                        subjects755 = deque(tmp754._args)
                        matcher = CommutativeMatcher69134.get()
                        tmp756 = subjects755
                        subjects755 = []
                        for s in tmp756:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp756, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 69140
                                if len(subjects740) == 0:
                                    pass
                                    # State 69141
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69142
                                        if len(subjects691) == 0:
                                            pass
                                            # State 69143
                                            if len(subjects) == 0:
                                                pass
                                                # 17: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                    if len(subjects691) >= 1:
                                        tmp758 = subjects691.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3_1', tmp758)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69142
                                            if len(subjects691) == 0:
                                                pass
                                                # State 69143
                                                if len(subjects) == 0:
                                                    pass
                                                    # 17: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        subjects691.appendleft(tmp758)
                        subjects740.appendleft(tmp754)
                    subjects691.appendleft(tmp739)
                if len(subjects691) >= 1 and isinstance(subjects691[0], tan):
                    tmp760 = subjects691.popleft()
                    subjects761 = deque(tmp760._args)
                    # State 83443
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83444
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83445
                            if len(subjects761) >= 1:
                                tmp764 = subjects761.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp764)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83446
                                    if len(subjects761) == 0:
                                        pass
                                        # State 83447
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.3_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83448
                                            if len(subjects691) == 0:
                                                pass
                                                # State 83449
                                                if len(subjects) == 0:
                                                    pass
                                                    # 27: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        if len(subjects691) >= 1:
                                            tmp767 = subjects691.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.3_1', tmp767)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 83448
                                                if len(subjects691) == 0:
                                                    pass
                                                    # State 83449
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 27: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects691.appendleft(tmp767)
                                subjects761.appendleft(tmp764)
                        if len(subjects761) >= 1 and isinstance(subjects761[0], Mul):
                            tmp769 = subjects761.popleft()
                            associative1 = tmp769
                            associative_type1 = type(tmp769)
                            subjects770 = deque(tmp769._args)
                            matcher = CommutativeMatcher83451.get()
                            tmp771 = subjects770
                            subjects770 = []
                            for s in tmp771:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp771, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83452
                                    if len(subjects761) == 0:
                                        pass
                                        # State 83453
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3_1', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83454
                                            if len(subjects691) == 0:
                                                pass
                                                # State 83455
                                                if len(subjects) == 0:
                                                    pass
                                                    # 27: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        if len(subjects691) >= 1:
                                            tmp773 = subjects691.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.3_1', tmp773)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 83454
                                                if len(subjects691) == 0:
                                                    pass
                                                    # State 83455
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 27: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                            subjects691.appendleft(tmp773)
                            subjects761.appendleft(tmp769)
                    if len(subjects761) >= 1 and isinstance(subjects761[0], Add):
                        tmp775 = subjects761.popleft()
                        associative1 = tmp775
                        associative_type1 = type(tmp775)
                        subjects776 = deque(tmp775._args)
                        matcher = CommutativeMatcher83457.get()
                        tmp777 = subjects776
                        subjects776 = []
                        for s in tmp777:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp777, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83463
                                if len(subjects761) == 0:
                                    pass
                                    # State 83464
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83465
                                        if len(subjects691) == 0:
                                            pass
                                            # State 83466
                                            if len(subjects) == 0:
                                                pass
                                                # 27: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                    if len(subjects691) >= 1:
                                        tmp779 = subjects691.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3_1', tmp779)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83465
                                            if len(subjects691) == 0:
                                                pass
                                                # State 83466
                                                if len(subjects) == 0:
                                                    pass
                                                    # 27: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                        subjects691.appendleft(tmp779)
                        subjects761.appendleft(tmp775)
                    subjects691.appendleft(tmp760)
                if len(subjects691) >= 1 and isinstance(subjects691[0], Pow):
                    tmp781 = subjects691.popleft()
                    subjects782 = deque(tmp781._args)
                    # State 83739
                    if len(subjects782) >= 1 and isinstance(subjects782[0], tan):
                        tmp783 = subjects782.popleft()
                        subjects784 = deque(tmp783._args)
                        # State 83740
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83741
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83742
                                if len(subjects784) >= 1:
                                    tmp787 = subjects784.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.4.1.0', tmp787)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83743
                                        if len(subjects784) == 0:
                                            pass
                                            # State 83744
                                            if len(subjects782) >= 1 and subjects782[0] == -1:
                                                tmp789 = subjects782.popleft()
                                                # State 83745
                                                if len(subjects782) == 0:
                                                    pass
                                                    # State 83746
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.5_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83747
                                                        if len(subjects691) == 0:
                                                            pass
                                                            # State 83748
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 29: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    if len(subjects691) >= 1:
                                                        tmp791 = subjects691.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.5_1', tmp791)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 83747
                                                            if len(subjects691) == 0:
                                                                pass
                                                                # State 83748
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 29: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        subjects691.appendleft(tmp791)
                                                subjects782.appendleft(tmp789)
                                    subjects784.appendleft(tmp787)
                            if len(subjects784) >= 1 and isinstance(subjects784[0], Mul):
                                tmp793 = subjects784.popleft()
                                associative1 = tmp793
                                associative_type1 = type(tmp793)
                                subjects794 = deque(tmp793._args)
                                matcher = CommutativeMatcher83750.get()
                                tmp795 = subjects794
                                subjects794 = []
                                for s in tmp795:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp795, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 83751
                                        if len(subjects784) == 0:
                                            pass
                                            # State 83752
                                            if len(subjects782) >= 1 and subjects782[0] == -1:
                                                tmp796 = subjects782.popleft()
                                                # State 83753
                                                if len(subjects782) == 0:
                                                    pass
                                                    # State 83754
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83755
                                                        if len(subjects691) == 0:
                                                            pass
                                                            # State 83756
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 29: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    if len(subjects691) >= 1:
                                                        tmp798 = subjects691.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.5_1', tmp798)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 83755
                                                            if len(subjects691) == 0:
                                                                pass
                                                                # State 83756
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 29: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        subjects691.appendleft(tmp798)
                                                subjects782.appendleft(tmp796)
                                subjects784.appendleft(tmp793)
                        if len(subjects784) >= 1 and isinstance(subjects784[0], Add):
                            tmp800 = subjects784.popleft()
                            associative1 = tmp800
                            associative_type1 = type(tmp800)
                            subjects801 = deque(tmp800._args)
                            matcher = CommutativeMatcher83758.get()
                            tmp802 = subjects801
                            subjects801 = []
                            for s in tmp802:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp802, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83764
                                    if len(subjects784) == 0:
                                        pass
                                        # State 83765
                                        if len(subjects782) >= 1 and subjects782[0] == -1:
                                            tmp803 = subjects782.popleft()
                                            # State 83766
                                            if len(subjects782) == 0:
                                                pass
                                                # State 83767
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 83768
                                                    if len(subjects691) == 0:
                                                        pass
                                                        # State 83769
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 29: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                if len(subjects691) >= 1:
                                                    tmp805 = subjects691.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5_1', tmp805)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83768
                                                        if len(subjects691) == 0:
                                                            pass
                                                            # State 83769
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 29: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    subjects691.appendleft(tmp805)
                                            subjects782.appendleft(tmp803)
                            subjects784.appendleft(tmp800)
                        subjects782.appendleft(tmp783)
                    if len(subjects782) >= 1 and isinstance(subjects782[0], cos):
                        tmp807 = subjects782.popleft()
                        subjects808 = deque(tmp807._args)
                        # State 95453
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95454
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95455
                                if len(subjects808) >= 1:
                                    tmp811 = subjects808.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.4.1.0', tmp811)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95456
                                        if len(subjects808) == 0:
                                            pass
                                            # State 95457
                                            if len(subjects782) >= 1 and subjects782[0] == -1:
                                                tmp813 = subjects782.popleft()
                                                # State 95458
                                                if len(subjects782) == 0:
                                                    pass
                                                    # State 95459
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.5_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95460
                                                        if len(subjects691) == 0:
                                                            pass
                                                            # State 95461
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 39: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    if len(subjects691) >= 1:
                                                        tmp815 = subjects691.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.5_1', tmp815)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95460
                                                            if len(subjects691) == 0:
                                                                pass
                                                                # State 95461
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 39: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        subjects691.appendleft(tmp815)
                                                subjects782.appendleft(tmp813)
                                    subjects808.appendleft(tmp811)
                            if len(subjects808) >= 1 and isinstance(subjects808[0], Mul):
                                tmp817 = subjects808.popleft()
                                associative1 = tmp817
                                associative_type1 = type(tmp817)
                                subjects818 = deque(tmp817._args)
                                matcher = CommutativeMatcher95463.get()
                                tmp819 = subjects818
                                subjects818 = []
                                for s in tmp819:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp819, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95464
                                        if len(subjects808) == 0:
                                            pass
                                            # State 95465
                                            if len(subjects782) >= 1 and subjects782[0] == -1:
                                                tmp820 = subjects782.popleft()
                                                # State 95466
                                                if len(subjects782) == 0:
                                                    pass
                                                    # State 95467
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95468
                                                        if len(subjects691) == 0:
                                                            pass
                                                            # State 95469
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 39: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    if len(subjects691) >= 1:
                                                        tmp822 = subjects691.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.5_1', tmp822)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95468
                                                            if len(subjects691) == 0:
                                                                pass
                                                                # State 95469
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 39: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        subjects691.appendleft(tmp822)
                                                subjects782.appendleft(tmp820)
                                subjects808.appendleft(tmp817)
                        if len(subjects808) >= 1 and isinstance(subjects808[0], Add):
                            tmp824 = subjects808.popleft()
                            associative1 = tmp824
                            associative_type1 = type(tmp824)
                            subjects825 = deque(tmp824._args)
                            matcher = CommutativeMatcher95471.get()
                            tmp826 = subjects825
                            subjects825 = []
                            for s in tmp826:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp826, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95477
                                    if len(subjects808) == 0:
                                        pass
                                        # State 95478
                                        if len(subjects782) >= 1 and subjects782[0] == -1:
                                            tmp827 = subjects782.popleft()
                                            # State 95479
                                            if len(subjects782) == 0:
                                                pass
                                                # State 95480
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95481
                                                    if len(subjects691) == 0:
                                                        pass
                                                        # State 95482
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 39: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                if len(subjects691) >= 1:
                                                    tmp829 = subjects691.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5_1', tmp829)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95481
                                                        if len(subjects691) == 0:
                                                            pass
                                                            # State 95482
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 39: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    subjects691.appendleft(tmp829)
                                            subjects782.appendleft(tmp827)
                            subjects808.appendleft(tmp824)
                        subjects782.appendleft(tmp807)
                    if len(subjects782) >= 1 and isinstance(subjects782[0], sin):
                        tmp831 = subjects782.popleft()
                        subjects832 = deque(tmp831._args)
                        # State 95849
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95850
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 95851
                                if len(subjects832) >= 1:
                                    tmp835 = subjects832.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.4.1.0', tmp835)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 95852
                                        if len(subjects832) == 0:
                                            pass
                                            # State 95853
                                            if len(subjects782) >= 1 and subjects782[0] == -1:
                                                tmp837 = subjects782.popleft()
                                                # State 95854
                                                if len(subjects782) == 0:
                                                    pass
                                                    # State 95855
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.5_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95856
                                                        if len(subjects691) == 0:
                                                            pass
                                                            # State 95857
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 41: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    if len(subjects691) >= 1:
                                                        tmp839 = subjects691.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.5_1', tmp839)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95856
                                                            if len(subjects691) == 0:
                                                                pass
                                                                # State 95857
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 41: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        subjects691.appendleft(tmp839)
                                                subjects782.appendleft(tmp837)
                                    subjects832.appendleft(tmp835)
                            if len(subjects832) >= 1 and isinstance(subjects832[0], Mul):
                                tmp841 = subjects832.popleft()
                                associative1 = tmp841
                                associative_type1 = type(tmp841)
                                subjects842 = deque(tmp841._args)
                                matcher = CommutativeMatcher95859.get()
                                tmp843 = subjects842
                                subjects842 = []
                                for s in tmp843:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp843, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 95860
                                        if len(subjects832) == 0:
                                            pass
                                            # State 95861
                                            if len(subjects782) >= 1 and subjects782[0] == -1:
                                                tmp844 = subjects782.popleft()
                                                # State 95862
                                                if len(subjects782) == 0:
                                                    pass
                                                    # State 95863
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5_1', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95864
                                                        if len(subjects691) == 0:
                                                            pass
                                                            # State 95865
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 41: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    if len(subjects691) >= 1:
                                                        tmp846 = subjects691.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.5_1', tmp846)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 95864
                                                            if len(subjects691) == 0:
                                                                pass
                                                                # State 95865
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 41: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                        subjects691.appendleft(tmp846)
                                                subjects782.appendleft(tmp844)
                                subjects832.appendleft(tmp841)
                        if len(subjects832) >= 1 and isinstance(subjects832[0], Add):
                            tmp848 = subjects832.popleft()
                            associative1 = tmp848
                            associative_type1 = type(tmp848)
                            subjects849 = deque(tmp848._args)
                            matcher = CommutativeMatcher95867.get()
                            tmp850 = subjects849
                            subjects849 = []
                            for s in tmp850:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp850, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95873
                                    if len(subjects832) == 0:
                                        pass
                                        # State 95874
                                        if len(subjects782) >= 1 and subjects782[0] == -1:
                                            tmp851 = subjects782.popleft()
                                            # State 95875
                                            if len(subjects782) == 0:
                                                pass
                                                # State 95876
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95877
                                                    if len(subjects691) == 0:
                                                        pass
                                                        # State 95878
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 41: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                if len(subjects691) >= 1:
                                                    tmp853 = subjects691.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5_1', tmp853)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95877
                                                        if len(subjects691) == 0:
                                                            pass
                                                            # State 95878
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 41: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                                                    subjects691.appendleft(tmp853)
                                            subjects782.appendleft(tmp851)
                            subjects832.appendleft(tmp848)
                        subjects782.appendleft(tmp831)
                    subjects691.appendleft(tmp781)
                subjects.appendleft(tmp690)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp855 = subjects.popleft()
            associative1 = tmp855
            associative_type1 = type(tmp855)
            subjects856 = deque(tmp855._args)
            matcher = CommutativeMatcher8149.get()
            tmp857 = subjects856
            subjects856 = []
            for s in tmp857:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp857, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 8154
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48) and (cons_f89) and (cons_f465)
                        # 2: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f587)
                if pattern_index == 1:
                    pass
                    # State 8166
                    if len(subjects) == 0:
                        pass
                        # 1: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f48)
                        # 3: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f587) and (cons_f683)
                if pattern_index == 2:
                    pass
                    # State 10032
                    if len(subjects) == 0:
                        pass
                        # 4: b*(c*x**n)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f52) and (cons_f4) and (cons_f5) and (cons_f800)
                if pattern_index == 3:
                    pass
                    # State 10886
                    if len(subjects) == 0:
                        pass
                        # 5: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                        # 7: b*(c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809) and (cons_f810)
                if pattern_index == 4:
                    pass
                    # State 10931
                    if len(subjects) == 0:
                        pass
                        # 6: c*(c/x)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f48)
                if pattern_index == 5:
                    pass
                    # State 11172
                    if len(subjects) == 0:
                        pass
                        # 8: c*x**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f809)
                if pattern_index == 6:
                    pass
                    # State 13333
                    if len(subjects) == 0:
                        pass
                        # 9: h*(d + e*x + f*sqrt(a + b*x + c*x**2))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                if pattern_index == 7:
                    pass
                    # State 13613
                    if len(subjects) == 0:
                        pass
                        # 10: h*(d + e*x + f*sqrt(a + c*x**2))**n /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                if pattern_index == 8:
                    pass
                    # State 13717
                    if len(subjects) == 0:
                        pass
                        # 11: h*(u + f*sqrt(v))**n /; (cons_f127) and (cons_f211) and (cons_f4) and (cons_f70) and (cons_f820) and (cons_f821) and (cons_f1058)
                if pattern_index == 9:
                    pass
                    # State 52350
                    if len(subjects) == 0:
                        pass
                        # 12: b*log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                if pattern_index == 10:
                    pass
                    # State 53138
                    if len(subjects) == 0:
                        pass
                        # 13: b*log(c*RFx**p) /; (cons_f3) and (cons_f8) and (cons_f5) and (cons_f1200)
                if pattern_index == 11:
                    pass
                    # State 68819
                    if len(subjects) == 0:
                        pass
                        # 14: b*sin(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                if pattern_index == 12:
                    pass
                    # State 68888
                    if len(subjects) == 0:
                        pass
                        # 15: c*sin(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                if pattern_index == 13:
                    pass
                    # State 69101
                    if len(subjects) == 0:
                        pass
                        # 16: b*cos(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                if pattern_index == 14:
                    pass
                    # State 69168
                    if len(subjects) == 0:
                        pass
                        # 17: c*cos(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                if pattern_index == 15:
                    pass
                    # State 73044
                    if len(subjects) == 0:
                        pass
                        # 18: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                        # 20: b*sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                        # 22: b*sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                if pattern_index == 16:
                    pass
                    # State 73211
                    if len(subjects) == 0:
                        pass
                        # 19: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                        # 21: b*cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                        # 23: b*cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                if pattern_index == 17:
                    pass
                    # State 73514
                    if len(subjects) == 0:
                        pass
                        # 24: b*sin(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                if pattern_index == 18:
                    pass
                    # State 73554
                    if len(subjects) == 0:
                        pass
                        # 25: b*cos(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                if pattern_index == 19:
                    pass
                    # State 83424
                    if len(subjects) == 0:
                        pass
                        # 26: b*tan(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                if pattern_index == 20:
                    pass
                    # State 83491
                    if len(subjects) == 0:
                        pass
                        # 27: c*tan(d + x*e)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                if pattern_index == 21:
                    pass
                    # State 83712
                    if len(subjects) == 0:
                        pass
                        # 28: b*(1/tan(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                if pattern_index == 22:
                    pass
                    # State 83802
                    if len(subjects) == 0:
                        pass
                        # 29: c*(1/tan(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                if pattern_index == 23:
                    pass
                    # State 87224
                    if len(subjects) == 0:
                        pass
                        # 32: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        # 34: b*tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        # 30: b*tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                if pattern_index == 24:
                    pass
                    # State 87508
                    if len(subjects) == 0:
                        pass
                        # 33: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        # 35: b/tan(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                        # 31: b/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                if pattern_index == 25:
                    pass
                    # State 87852
                    if len(subjects) == 0:
                        pass
                        # 36: b*tan(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                if pattern_index == 26:
                    pass
                    # State 87900
                    if len(subjects) == 0:
                        pass
                        # 37: b/tan(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                if pattern_index == 27:
                    pass
                    # State 95428
                    if len(subjects) == 0:
                        pass
                        # 38: b*(1/cos(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                if pattern_index == 28:
                    pass
                    # State 95513
                    if len(subjects) == 0:
                        pass
                        # 39: c*(1/cos(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                if pattern_index == 29:
                    pass
                    # State 95824
                    if len(subjects) == 0:
                        pass
                        # 40: b*(1/sin(d + x*e))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                if pattern_index == 30:
                    pass
                    # State 95909
                    if len(subjects) == 0:
                        pass
                        # 41: c*(1/sin(d + x*e))**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f48) and (cons_f47)
                if pattern_index == 31:
                    pass
                    # State 97563
                    if len(subjects) == 0:
                        pass
                        # 42: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        # 44: b/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        # 46: b/cos(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                if pattern_index == 32:
                    pass
                    # State 97871
                    if len(subjects) == 0:
                        pass
                        # 43: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        # 45: b/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        # 47: b/sin(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                if pattern_index == 33:
                    pass
                    # State 98239
                    if len(subjects) == 0:
                        pass
                        # 48: b/cos(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                if pattern_index == 34:
                    pass
                    # State 98295
                    if len(subjects) == 0:
                        pass
                        # 49: b/sin(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                if pattern_index == 35:
                    pass
                    # State 107994
                    if len(subjects) == 0:
                        pass
                        # 50: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                if pattern_index == 36:
                    pass
                    # State 108088
                    if len(subjects) == 0:
                        pass
                        # 51: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                if pattern_index == 37:
                    pass
                    # State 110295
                    if len(subjects) == 0:
                        pass
                        # 52: b*asin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                if pattern_index == 38:
                    pass
                    # State 110391
                    if len(subjects) == 0:
                        pass
                        # 53: b*acos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                if pattern_index == 39:
                    pass
                    # State 112629
                    if len(subjects) == 0:
                        pass
                        # 54: b*atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                if pattern_index == 40:
                    pass
                    # State 112723
                    if len(subjects) == 0:
                        pass
                        # 55: b*acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                if pattern_index == 41:
                    pass
                    # State 115493
                    if len(subjects) == 0:
                        pass
                        # 56: b*atan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                if pattern_index == 42:
                    pass
                    # State 115589
                    if len(subjects) == 0:
                        pass
                        # 57: b*acot(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                if pattern_index == 43:
                    pass
                    # State 122905
                    if len(subjects) == 0:
                        pass
                        # 58: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                        # 60: b*sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                        # 62: b*sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                if pattern_index == 44:
                    pass
                    # State 123072
                    if len(subjects) == 0:
                        pass
                        # 59: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                        # 61: b*cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                        # 63: b*cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                if pattern_index == 45:
                    pass
                    # State 123375
                    if len(subjects) == 0:
                        pass
                        # 64: b*sinh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                if pattern_index == 46:
                    pass
                    # State 123415
                    if len(subjects) == 0:
                        pass
                        # 65: b*cosh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                if pattern_index == 47:
                    pass
                    # State 126671
                    if len(subjects) == 0:
                        pass
                        # 66: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        # 68: b*tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        # 70: b*tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                if pattern_index == 48:
                    pass
                    # State 126987
                    if len(subjects) == 0:
                        pass
                        # 67: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        # 69: b/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        # 71: b/tanh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                if pattern_index == 49:
                    pass
                    # State 127347
                    if len(subjects) == 0:
                        pass
                        # 72: b*tanh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                if pattern_index == 50:
                    pass
                    # State 127395
                    if len(subjects) == 0:
                        pass
                        # 73: b/tanh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                if pattern_index == 51:
                    pass
                    # State 129764
                    if len(subjects) == 0:
                        pass
                        # 74: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        # 76: b/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        # 78: b/cosh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                if pattern_index == 52:
                    pass
                    # State 130104
                    if len(subjects) == 0:
                        pass
                        # 75: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                        # 77: b/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                        # 79: b/sinh(c + d*x**n) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                if pattern_index == 53:
                    pass
                    # State 130488
                    if len(subjects) == 0:
                        pass
                        # 80: b/cosh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                if pattern_index == 54:
                    pass
                    # State 130544
                    if len(subjects) == 0:
                        pass
                        # 81: b/sinh(u) /; (cons_f3) and (cons_f825) and (cons_f826)
                if pattern_index == 55:
                    pass
                    # State 137733
                    if len(subjects) == 0:
                        pass
                        # 82: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                if pattern_index == 56:
                    pass
                    # State 137827
                    if len(subjects) == 0:
                        pass
                        # 83: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                if pattern_index == 57:
                    pass
                    # State 140030
                    if len(subjects) == 0:
                        pass
                        # 84: b*asinh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                if pattern_index == 58:
                    pass
                    # State 140126
                    if len(subjects) == 0:
                        pass
                        # 85: b*acosh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                if pattern_index == 59:
                    pass
                    # State 142261
                    if len(subjects) == 0:
                        pass
                        # 86: b*atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                if pattern_index == 60:
                    pass
                    # State 142355
                    if len(subjects) == 0:
                        pass
                        # 87: b*acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                if pattern_index == 61:
                    pass
                    # State 144718
                    if len(subjects) == 0:
                        pass
                        # 88: b*atanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                if pattern_index == 62:
                    pass
                    # State 144814
                    if len(subjects) == 0:
                        pass
                        # 89: b*acoth(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
            subjects.appendleft(tmp855)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
