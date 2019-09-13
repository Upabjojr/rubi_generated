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

class CommutativeMatcher3255(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.1', 1, 1, None), Mul)
]),
    6: (6, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.3.1.1', 1, 1, None), Mul)
]),
    7: (7, Multiset({3: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({4: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({5: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({6: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({7: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({8: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({9: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({10: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({11: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({12: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({13: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({14: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({15: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({16: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({17: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({18: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({19: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({20: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({21: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({22: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    27: (27, Multiset({23: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({24: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({25: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.2.1.0', 1, 1, None), Mul)
]),
    31: (31, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({26: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    33: (33, Multiset({27: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({28: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({29: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    36: (36, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul)
]),
    37: (37, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.3.1.0', 1, 1, None), Mul)
]),
    38: (38, Multiset({30: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({31: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({32: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    41: (41, Multiset({33: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    42: (42, Multiset({34: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    43: (43, Multiset({35: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    44: (44, Multiset({36: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    45: (45, Multiset({37: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    46: (46, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.3.1.0', 1, 1, None), Mul)
]),
    47: (47, Multiset({38: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    48: (48, Multiset({39: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    49: (49, Multiset({40: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    50: (50, Multiset({41: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    51: (51, Multiset({42: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    52: (52, Multiset({43: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    53: (53, Multiset({44: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    54: (54, Multiset({45: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    55: (55, Multiset({46: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    56: (56, Multiset({47: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    57: (57, Multiset({48: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    58: (58, Multiset({49: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    59: (59, Multiset({50: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    60: (60, Multiset({51: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    61: (61, Multiset({52: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    62: (62, Multiset({53: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    63: (63, Multiset({54: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    64: (64, Multiset({55: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    65: (65, Multiset({56: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    66: (66, Multiset({57: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    67: (67, Multiset({58: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    68: (68, Multiset({59: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    69: (69, Multiset({60: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    70: (70, Multiset({61: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    71: (71, Multiset({62: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    72: (72, Multiset({63: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    73: (73, Multiset({64: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    74: (74, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.4.1.0', 1, 1, None), Mul)
]),
    75: (75, Multiset({65: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    76: (76, Multiset({66: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    77: (77, Multiset({67: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    78: (78, Multiset({68: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    79: (79, Multiset({69: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    80: (80, Multiset({70: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    81: (81, Multiset({71: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    82: (82, Multiset({72: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    83: (83, Multiset({73: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    84: (84, Multiset({74: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    85: (85, Multiset({75: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    86: (86, Multiset({76: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    87: (87, Multiset({77: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    88: (88, Multiset({78: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    89: (89, Multiset({79: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    90: (90, Multiset({80: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    91: (91, Multiset({81: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    92: (92, Multiset({82: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    93: (93, Multiset({83: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    94: (94, Multiset({84: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    95: (95, Multiset({85: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    96: (96, Multiset({86: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    97: (97, Multiset({87: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    98: (98, Multiset({88: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    99: (99, Multiset({89: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
]),
    100: (100, Multiset({90: 1}), [
      (VariableWithCount('i2.1.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher3255._instance is None:
            CommutativeMatcher3255._instance = CommutativeMatcher3255()
        return CommutativeMatcher3255._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3254
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 5637
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 5638
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp5 = subjects2.popleft()
                        # State 5639
                        if len(subjects2) == 0:
                            pass
                            # State 5640
                            if len(subjects) == 0:
                                pass
                                # 0: x**2
                        subjects2.appendleft(tmp5)
                    if len(subjects2) >= 1 and subjects2[0] == 4:
                        tmp6 = subjects2.popleft()
                        # State 11425
                        if len(subjects2) == 0:
                            pass
                            # State 11426
                            if len(subjects) == 0:
                                pass
                                # 2: x**4
                        subjects2.appendleft(tmp6)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp7 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.0', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 5655
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp9 = subjects2.popleft()
                        # State 5656
                        if len(subjects2) == 0:
                            pass
                            # State 5657
                            if len(subjects) == 0:
                                pass
                                # 1: v**2
                        subjects2.appendleft(tmp9)
                subjects2.appendleft(tmp7)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp10 = subjects2.popleft()
                subjects11 = deque(tmp10._args)
                # State 65927
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65928
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 65929
                        if len(subjects11) >= 1:
                            tmp14 = subjects11.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.0', tmp14)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 65930
                                if len(subjects11) == 0:
                                    pass
                                    # State 65931
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp16 = subjects2.popleft()
                                        # State 65932
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65933
                                            if len(subjects) == 0:
                                                pass
                                                # 20: sin(c + x*d)**2
                                        subjects2.appendleft(tmp16)
                            subjects11.appendleft(tmp14)
                    if len(subjects11) >= 1 and isinstance(subjects11[0], Mul):
                        tmp17 = subjects11.popleft()
                        associative1 = tmp17
                        associative_type1 = type(tmp17)
                        subjects18 = deque(tmp17._args)
                        matcher = CommutativeMatcher65935.get()
                        tmp19 = subjects18
                        subjects18 = []
                        for s in tmp19:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp19, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 65936
                                if len(subjects11) == 0:
                                    pass
                                    # State 65937
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp20 = subjects2.popleft()
                                        # State 65938
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65939
                                            if len(subjects) == 0:
                                                pass
                                                # 20: sin(c + x*d)**2
                                        subjects2.appendleft(tmp20)
                        subjects11.appendleft(tmp17)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 66258
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 66259
                        if len(subjects11) >= 1:
                            tmp23 = subjects11.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp23)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 66260
                                if len(subjects11) == 0:
                                    pass
                                    # State 66261
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp25 = subjects2.popleft()
                                        # State 66262
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66263
                                            if len(subjects) == 0:
                                                pass
                                                # 22: sin(e + x*f)**2
                                        subjects2.appendleft(tmp25)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp26 = subjects2.popleft()
                                        # State 94518
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94519
                                            if len(subjects) == 0:
                                                pass
                                                # 37: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp26)
                            subjects11.appendleft(tmp23)
                    if len(subjects11) >= 1 and isinstance(subjects11[0], Mul):
                        tmp27 = subjects11.popleft()
                        associative1 = tmp27
                        associative_type1 = type(tmp27)
                        subjects28 = deque(tmp27._args)
                        matcher = CommutativeMatcher66265.get()
                        tmp29 = subjects28
                        subjects28 = []
                        for s in tmp29:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp29, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 66266
                                if len(subjects11) == 0:
                                    pass
                                    # State 66267
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp30 = subjects2.popleft()
                                        # State 66268
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66269
                                            if len(subjects) == 0:
                                                pass
                                                # 22: sin(e + x*f)**2
                                        subjects2.appendleft(tmp30)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp31 = subjects2.popleft()
                                        # State 94520
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94521
                                            if len(subjects) == 0:
                                                pass
                                                # 37: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp31)
                        subjects11.appendleft(tmp27)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 66564
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 66565
                        if len(subjects11) >= 1:
                            tmp34 = subjects11.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp34)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 66566
                                if len(subjects11) == 0:
                                    pass
                                    # State 66567
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp36 = subjects2.popleft()
                                        # State 66568
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66569
                                            if len(subjects) == 0:
                                                pass
                                                # 24: sin(e + x*f)**2
                                        subjects2.appendleft(tmp36)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp37 = subjects2.popleft()
                                        # State 94049
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94050
                                            if len(subjects) == 0:
                                                pass
                                                # 33: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp37)
                            subjects11.appendleft(tmp34)
                    if len(subjects11) >= 1 and isinstance(subjects11[0], Mul):
                        tmp38 = subjects11.popleft()
                        associative1 = tmp38
                        associative_type1 = type(tmp38)
                        subjects39 = deque(tmp38._args)
                        matcher = CommutativeMatcher66571.get()
                        tmp40 = subjects39
                        subjects39 = []
                        for s in tmp40:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp40, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 66572
                                if len(subjects11) == 0:
                                    pass
                                    # State 66573
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp41 = subjects2.popleft()
                                        # State 66574
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66575
                                            if len(subjects) == 0:
                                                pass
                                                # 24: sin(e + x*f)**2
                                        subjects2.appendleft(tmp41)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp42 = subjects2.popleft()
                                        # State 94051
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94052
                                            if len(subjects) == 0:
                                                pass
                                                # 33: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp42)
                        subjects11.appendleft(tmp38)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 93565
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 93566
                        if len(subjects11) >= 1:
                            tmp45 = subjects11.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp45)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 93567
                                if len(subjects11) == 0:
                                    pass
                                    # State 93568
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp47 = subjects2.popleft()
                                        # State 93569
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93570
                                            if len(subjects) == 0:
                                                pass
                                                # 31: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp47)
                            subjects11.appendleft(tmp45)
                    if len(subjects11) >= 1 and isinstance(subjects11[0], Mul):
                        tmp48 = subjects11.popleft()
                        associative1 = tmp48
                        associative_type1 = type(tmp48)
                        subjects49 = deque(tmp48._args)
                        matcher = CommutativeMatcher93572.get()
                        tmp50 = subjects49
                        subjects49 = []
                        for s in tmp50:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp50, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 93573
                                if len(subjects11) == 0:
                                    pass
                                    # State 93574
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp51 = subjects2.popleft()
                                        # State 93575
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93576
                                            if len(subjects) == 0:
                                                pass
                                                # 31: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp51)
                        subjects11.appendleft(tmp48)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 94274
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 94275
                        if len(subjects11) >= 1:
                            tmp54 = subjects11.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp54)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 94276
                                if len(subjects11) == 0:
                                    pass
                                    # State 94277
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp56 = subjects2.popleft()
                                        # State 94278
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94279
                                            if len(subjects) == 0:
                                                pass
                                                # 35: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp56)
                            subjects11.appendleft(tmp54)
                    if len(subjects11) >= 1 and isinstance(subjects11[0], Mul):
                        tmp57 = subjects11.popleft()
                        associative1 = tmp57
                        associative_type1 = type(tmp57)
                        subjects58 = deque(tmp57._args)
                        matcher = CommutativeMatcher94281.get()
                        tmp59 = subjects58
                        subjects58 = []
                        for s in tmp59:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp59, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 94282
                                if len(subjects11) == 0:
                                    pass
                                    # State 94283
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp60 = subjects2.popleft()
                                        # State 94284
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94285
                                            if len(subjects) == 0:
                                                pass
                                                # 35: sin(e + x*f)**(-2)
                                        subjects2.appendleft(tmp60)
                        subjects11.appendleft(tmp57)
                if len(subjects11) >= 1 and isinstance(subjects11[0], Add):
                    tmp61 = subjects11.popleft()
                    associative1 = tmp61
                    associative_type1 = type(tmp61)
                    subjects62 = deque(tmp61._args)
                    matcher = CommutativeMatcher65941.get()
                    tmp63 = subjects62
                    subjects62 = []
                    for s in tmp63:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp63, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 65947
                            if len(subjects11) == 0:
                                pass
                                # State 65948
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp64 = subjects2.popleft()
                                    # State 65949
                                    if len(subjects2) == 0:
                                        pass
                                        # State 65950
                                        if len(subjects) == 0:
                                            pass
                                            # 20: sin(c + x*d)**2
                                    subjects2.appendleft(tmp64)
                        if pattern_index == 1:
                            pass
                            # State 66273
                            if len(subjects11) == 0:
                                pass
                                # State 66274
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp65 = subjects2.popleft()
                                    # State 66275
                                    if len(subjects2) == 0:
                                        pass
                                        # State 66276
                                        if len(subjects) == 0:
                                            pass
                                            # 22: sin(e + x*f)**2
                                    subjects2.appendleft(tmp65)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp66 = subjects2.popleft()
                                    # State 94522
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94523
                                        if len(subjects) == 0:
                                            pass
                                            # 37: sin(e + x*f)**(-2)
                                    subjects2.appendleft(tmp66)
                        if pattern_index == 2:
                            pass
                            # State 66579
                            if len(subjects11) == 0:
                                pass
                                # State 66580
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp67 = subjects2.popleft()
                                    # State 66581
                                    if len(subjects2) == 0:
                                        pass
                                        # State 66582
                                        if len(subjects) == 0:
                                            pass
                                            # 24: sin(e + x*f)**2
                                    subjects2.appendleft(tmp67)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp68 = subjects2.popleft()
                                    # State 94053
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94054
                                        if len(subjects) == 0:
                                            pass
                                            # 33: sin(e + x*f)**(-2)
                                    subjects2.appendleft(tmp68)
                        if pattern_index == 3:
                            pass
                            # State 93580
                            if len(subjects11) == 0:
                                pass
                                # State 93581
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp69 = subjects2.popleft()
                                    # State 93582
                                    if len(subjects2) == 0:
                                        pass
                                        # State 93583
                                        if len(subjects) == 0:
                                            pass
                                            # 31: sin(e + x*f)**(-2)
                                    subjects2.appendleft(tmp69)
                        if pattern_index == 4:
                            pass
                            # State 94289
                            if len(subjects11) == 0:
                                pass
                                # State 94290
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp70 = subjects2.popleft()
                                    # State 94291
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94292
                                        if len(subjects) == 0:
                                            pass
                                            # 35: sin(e + x*f)**(-2)
                                    subjects2.appendleft(tmp70)
                    subjects11.appendleft(tmp61)
                subjects2.appendleft(tmp10)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp71 = subjects2.popleft()
                subjects72 = deque(tmp71._args)
                # State 65980
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65981
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 65982
                        if len(subjects72) >= 1:
                            tmp75 = subjects72.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.0', tmp75)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 65983
                                if len(subjects72) == 0:
                                    pass
                                    # State 65984
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp77 = subjects2.popleft()
                                        # State 65985
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65986
                                            if len(subjects) == 0:
                                                pass
                                                # 21: cos(c + x*d)**2
                                        subjects2.appendleft(tmp77)
                            subjects72.appendleft(tmp75)
                    if len(subjects72) >= 1 and isinstance(subjects72[0], Mul):
                        tmp78 = subjects72.popleft()
                        associative1 = tmp78
                        associative_type1 = type(tmp78)
                        subjects79 = deque(tmp78._args)
                        matcher = CommutativeMatcher65988.get()
                        tmp80 = subjects79
                        subjects79 = []
                        for s in tmp80:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp80, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 65989
                                if len(subjects72) == 0:
                                    pass
                                    # State 65990
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp81 = subjects2.popleft()
                                        # State 65991
                                        if len(subjects2) == 0:
                                            pass
                                            # State 65992
                                            if len(subjects) == 0:
                                                pass
                                                # 21: cos(c + x*d)**2
                                        subjects2.appendleft(tmp81)
                        subjects72.appendleft(tmp78)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 66301
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 66302
                        if len(subjects72) >= 1:
                            tmp84 = subjects72.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp84)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 66303
                                if len(subjects72) == 0:
                                    pass
                                    # State 66304
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp86 = subjects2.popleft()
                                        # State 66305
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66306
                                            if len(subjects) == 0:
                                                pass
                                                # 23: cos(e + x*f)**2
                                        subjects2.appendleft(tmp86)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp87 = subjects2.popleft()
                                        # State 94501
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94502
                                            if len(subjects) == 0:
                                                pass
                                                # 36: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp87)
                            subjects72.appendleft(tmp84)
                    if len(subjects72) >= 1 and isinstance(subjects72[0], Mul):
                        tmp88 = subjects72.popleft()
                        associative1 = tmp88
                        associative_type1 = type(tmp88)
                        subjects89 = deque(tmp88._args)
                        matcher = CommutativeMatcher66308.get()
                        tmp90 = subjects89
                        subjects89 = []
                        for s in tmp90:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp90, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 66309
                                if len(subjects72) == 0:
                                    pass
                                    # State 66310
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp91 = subjects2.popleft()
                                        # State 66311
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66312
                                            if len(subjects) == 0:
                                                pass
                                                # 23: cos(e + x*f)**2
                                        subjects2.appendleft(tmp91)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp92 = subjects2.popleft()
                                        # State 94503
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94504
                                            if len(subjects) == 0:
                                                pass
                                                # 36: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp92)
                        subjects72.appendleft(tmp88)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 66607
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 66608
                        if len(subjects72) >= 1:
                            tmp95 = subjects72.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp95)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 66609
                                if len(subjects72) == 0:
                                    pass
                                    # State 66610
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp97 = subjects2.popleft()
                                        # State 66611
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66612
                                            if len(subjects) == 0:
                                                pass
                                                # 25: cos(e + x*f)**2
                                        subjects2.appendleft(tmp97)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp98 = subjects2.popleft()
                                        # State 94025
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94026
                                            if len(subjects) == 0:
                                                pass
                                                # 32: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp98)
                            subjects72.appendleft(tmp95)
                    if len(subjects72) >= 1 and isinstance(subjects72[0], Mul):
                        tmp99 = subjects72.popleft()
                        associative1 = tmp99
                        associative_type1 = type(tmp99)
                        subjects100 = deque(tmp99._args)
                        matcher = CommutativeMatcher66614.get()
                        tmp101 = subjects100
                        subjects100 = []
                        for s in tmp101:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp101, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 66615
                                if len(subjects72) == 0:
                                    pass
                                    # State 66616
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp102 = subjects2.popleft()
                                        # State 66617
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66618
                                            if len(subjects) == 0:
                                                pass
                                                # 25: cos(e + x*f)**2
                                        subjects2.appendleft(tmp102)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp103 = subjects2.popleft()
                                        # State 94027
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94028
                                            if len(subjects) == 0:
                                                pass
                                                # 32: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp103)
                        subjects72.appendleft(tmp99)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 93515
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 93516
                        if len(subjects72) >= 1:
                            tmp106 = subjects72.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp106)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 93517
                                if len(subjects72) == 0:
                                    pass
                                    # State 93518
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp108 = subjects2.popleft()
                                        # State 93519
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93520
                                            if len(subjects) == 0:
                                                pass
                                                # 30: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp108)
                            subjects72.appendleft(tmp106)
                    if len(subjects72) >= 1 and isinstance(subjects72[0], Mul):
                        tmp109 = subjects72.popleft()
                        associative1 = tmp109
                        associative_type1 = type(tmp109)
                        subjects110 = deque(tmp109._args)
                        matcher = CommutativeMatcher93522.get()
                        tmp111 = subjects110
                        subjects110 = []
                        for s in tmp111:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp111, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 93523
                                if len(subjects72) == 0:
                                    pass
                                    # State 93524
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp112 = subjects2.popleft()
                                        # State 93525
                                        if len(subjects2) == 0:
                                            pass
                                            # State 93526
                                            if len(subjects) == 0:
                                                pass
                                                # 30: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp112)
                        subjects72.appendleft(tmp109)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 94224
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 94225
                        if len(subjects72) >= 1:
                            tmp115 = subjects72.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp115)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 94226
                                if len(subjects72) == 0:
                                    pass
                                    # State 94227
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp117 = subjects2.popleft()
                                        # State 94228
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94229
                                            if len(subjects) == 0:
                                                pass
                                                # 34: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp117)
                            subjects72.appendleft(tmp115)
                    if len(subjects72) >= 1 and isinstance(subjects72[0], Mul):
                        tmp118 = subjects72.popleft()
                        associative1 = tmp118
                        associative_type1 = type(tmp118)
                        subjects119 = deque(tmp118._args)
                        matcher = CommutativeMatcher94231.get()
                        tmp120 = subjects119
                        subjects119 = []
                        for s in tmp120:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp120, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 94232
                                if len(subjects72) == 0:
                                    pass
                                    # State 94233
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp121 = subjects2.popleft()
                                        # State 94234
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94235
                                            if len(subjects) == 0:
                                                pass
                                                # 34: cos(e + x*f)**(-2)
                                        subjects2.appendleft(tmp121)
                        subjects72.appendleft(tmp118)
                if len(subjects72) >= 1 and isinstance(subjects72[0], Add):
                    tmp122 = subjects72.popleft()
                    associative1 = tmp122
                    associative_type1 = type(tmp122)
                    subjects123 = deque(tmp122._args)
                    matcher = CommutativeMatcher65994.get()
                    tmp124 = subjects123
                    subjects123 = []
                    for s in tmp124:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp124, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 66000
                            if len(subjects72) == 0:
                                pass
                                # State 66001
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp125 = subjects2.popleft()
                                    # State 66002
                                    if len(subjects2) == 0:
                                        pass
                                        # State 66003
                                        if len(subjects) == 0:
                                            pass
                                            # 21: cos(c + x*d)**2
                                    subjects2.appendleft(tmp125)
                        if pattern_index == 1:
                            pass
                            # State 66316
                            if len(subjects72) == 0:
                                pass
                                # State 66317
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp126 = subjects2.popleft()
                                    # State 66318
                                    if len(subjects2) == 0:
                                        pass
                                        # State 66319
                                        if len(subjects) == 0:
                                            pass
                                            # 23: cos(e + x*f)**2
                                    subjects2.appendleft(tmp126)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp127 = subjects2.popleft()
                                    # State 94505
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94506
                                        if len(subjects) == 0:
                                            pass
                                            # 36: cos(e + x*f)**(-2)
                                    subjects2.appendleft(tmp127)
                        if pattern_index == 2:
                            pass
                            # State 66622
                            if len(subjects72) == 0:
                                pass
                                # State 66623
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp128 = subjects2.popleft()
                                    # State 66624
                                    if len(subjects2) == 0:
                                        pass
                                        # State 66625
                                        if len(subjects) == 0:
                                            pass
                                            # 25: cos(e + x*f)**2
                                    subjects2.appendleft(tmp128)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp129 = subjects2.popleft()
                                    # State 94029
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94030
                                        if len(subjects) == 0:
                                            pass
                                            # 32: cos(e + x*f)**(-2)
                                    subjects2.appendleft(tmp129)
                        if pattern_index == 3:
                            pass
                            # State 93530
                            if len(subjects72) == 0:
                                pass
                                # State 93531
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp130 = subjects2.popleft()
                                    # State 93532
                                    if len(subjects2) == 0:
                                        pass
                                        # State 93533
                                        if len(subjects) == 0:
                                            pass
                                            # 30: cos(e + x*f)**(-2)
                                    subjects2.appendleft(tmp130)
                        if pattern_index == 4:
                            pass
                            # State 94239
                            if len(subjects72) == 0:
                                pass
                                # State 94240
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp131 = subjects2.popleft()
                                    # State 94241
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94242
                                        if len(subjects) == 0:
                                            pass
                                            # 34: cos(e + x*f)**(-2)
                                    subjects2.appendleft(tmp131)
                    subjects72.appendleft(tmp122)
                subjects2.appendleft(tmp71)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp132 = subjects2.popleft()
                subjects133 = deque(tmp132._args)
                # State 79077
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 79078
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 79079
                        if len(subjects133) >= 1:
                            tmp136 = subjects133.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp136)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 79080
                                if len(subjects133) == 0:
                                    pass
                                    # State 79081
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp138 = subjects2.popleft()
                                        # State 79082
                                        if len(subjects2) == 0:
                                            pass
                                            # State 79083
                                            if len(subjects) == 0:
                                                pass
                                                # 27: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp138)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp139 = subjects2.popleft()
                                        # State 81600
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81601
                                            if len(subjects) == 0:
                                                pass
                                                # 29: tan(e + x*f)**(-2)
                                        subjects2.appendleft(tmp139)
                            subjects133.appendleft(tmp136)
                    if len(subjects133) >= 1 and isinstance(subjects133[0], Mul):
                        tmp140 = subjects133.popleft()
                        associative1 = tmp140
                        associative_type1 = type(tmp140)
                        subjects141 = deque(tmp140._args)
                        matcher = CommutativeMatcher79085.get()
                        tmp142 = subjects141
                        subjects141 = []
                        for s in tmp142:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp142, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 79086
                                if len(subjects133) == 0:
                                    pass
                                    # State 79087
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp143 = subjects2.popleft()
                                        # State 79088
                                        if len(subjects2) == 0:
                                            pass
                                            # State 79089
                                            if len(subjects) == 0:
                                                pass
                                                # 27: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp143)
                                    if len(subjects2) >= 1 and subjects2[0] == -2:
                                        tmp144 = subjects2.popleft()
                                        # State 81602
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81603
                                            if len(subjects) == 0:
                                                pass
                                                # 29: tan(e + x*f)**(-2)
                                        subjects2.appendleft(tmp144)
                        subjects133.appendleft(tmp140)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 81570
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 81571
                        if len(subjects133) >= 1:
                            tmp147 = subjects133.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.0', tmp147)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 81572
                                if len(subjects133) == 0:
                                    pass
                                    # State 81573
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp149 = subjects2.popleft()
                                        # State 81574
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81575
                                            if len(subjects) == 0:
                                                pass
                                                # 28: tan(c + x*d)**2
                                        subjects2.appendleft(tmp149)
                            subjects133.appendleft(tmp147)
                    if len(subjects133) >= 1 and isinstance(subjects133[0], Mul):
                        tmp150 = subjects133.popleft()
                        associative1 = tmp150
                        associative_type1 = type(tmp150)
                        subjects151 = deque(tmp150._args)
                        matcher = CommutativeMatcher81577.get()
                        tmp152 = subjects151
                        subjects151 = []
                        for s in tmp152:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp152, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 81578
                                if len(subjects133) == 0:
                                    pass
                                    # State 81579
                                    if len(subjects2) >= 1 and subjects2[0] == 2:
                                        tmp153 = subjects2.popleft()
                                        # State 81580
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81581
                                            if len(subjects) == 0:
                                                pass
                                                # 28: tan(c + x*d)**2
                                        subjects2.appendleft(tmp153)
                        subjects133.appendleft(tmp150)
                if len(subjects133) >= 1 and isinstance(subjects133[0], Add):
                    tmp154 = subjects133.popleft()
                    associative1 = tmp154
                    associative_type1 = type(tmp154)
                    subjects155 = deque(tmp154._args)
                    matcher = CommutativeMatcher79091.get()
                    tmp156 = subjects155
                    subjects155 = []
                    for s in tmp156:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp156, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 79097
                            if len(subjects133) == 0:
                                pass
                                # State 79098
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp157 = subjects2.popleft()
                                    # State 79099
                                    if len(subjects2) == 0:
                                        pass
                                        # State 79100
                                        if len(subjects) == 0:
                                            pass
                                            # 27: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp157)
                                if len(subjects2) >= 1 and subjects2[0] == -2:
                                    tmp158 = subjects2.popleft()
                                    # State 81604
                                    if len(subjects2) == 0:
                                        pass
                                        # State 81605
                                        if len(subjects) == 0:
                                            pass
                                            # 29: tan(e + x*f)**(-2)
                                    subjects2.appendleft(tmp158)
                        if pattern_index == 1:
                            pass
                            # State 81585
                            if len(subjects133) == 0:
                                pass
                                # State 81586
                                if len(subjects2) >= 1 and subjects2[0] == 2:
                                    tmp159 = subjects2.popleft()
                                    # State 81587
                                    if len(subjects2) == 0:
                                        pass
                                        # State 81588
                                        if len(subjects) == 0:
                                            pass
                                            # 28: tan(c + x*d)**2
                                    subjects2.appendleft(tmp159)
                    subjects133.appendleft(tmp154)
                subjects2.appendleft(tmp132)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp160 = subjects.popleft()
            subjects161 = deque(tmp160._args)
            # State 23936
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 23937
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 23938
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.2.1.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 23939
                        if len(subjects161) >= 1:
                            tmp165 = subjects161.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp165)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 23940
                                if len(subjects161) == 0:
                                    pass
                                    # State 23941
                                    if len(subjects) == 0:
                                        pass
                                        # 3: log(c*(e + f*x))
                            subjects161.appendleft(tmp165)
                    if len(subjects161) >= 1 and isinstance(subjects161[0], Mul):
                        tmp167 = subjects161.popleft()
                        associative1 = tmp167
                        associative_type1 = type(tmp167)
                        subjects168 = deque(tmp167._args)
                        matcher = CommutativeMatcher23943.get()
                        tmp169 = subjects168
                        subjects168 = []
                        for s in tmp169:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp169, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 23944
                                if len(subjects161) == 0:
                                    pass
                                    # State 23945
                                    if len(subjects) == 0:
                                        pass
                                        # 3: log(c*(e + f*x))
                        subjects161.appendleft(tmp167)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 24405
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 24406
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.1.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24407
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.1.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 24408
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24409
                                    if len(subjects161) >= 1:
                                        tmp175 = subjects161.popleft()
                                        subst7 = Substitution(subst6)
                                        try:
                                            subst7.try_add_variable('i2.2.1.0', tmp175)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24410
                                            if len(subjects161) == 0:
                                                pass
                                                # State 24411
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: log(c*(d*(e + f*x)**p)**q)
                                        subjects161.appendleft(tmp175)
                                    if len(subjects161) >= 1:
                                        tmp177 = subjects161.popleft()
                                        subst7 = Substitution(subst6)
                                        try:
                                            subst7.try_add_variable('i2.2.1.1', tmp177)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26699
                                            if len(subjects161) == 0:
                                                pass
                                                # State 26700
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: log(c*(d*(e + f*x)**p)**q)
                                        subjects161.appendleft(tmp177)
                                    if len(subjects161) >= 1:
                                        tmp179 = subjects161.popleft()
                                        subst7 = Substitution(subst6)
                                        try:
                                            subst7.try_add_variable('i2.3.1.0', tmp179)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27766
                                            if len(subjects161) == 0:
                                                pass
                                                # State 27767
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: log(c*(d*(e + f*x)**p)**q)
                                        subjects161.appendleft(tmp179)
                                if len(subjects161) >= 1 and isinstance(subjects161[0], Mul):
                                    tmp181 = subjects161.popleft()
                                    associative1 = tmp181
                                    associative_type1 = type(tmp181)
                                    subjects182 = deque(tmp181._args)
                                    matcher = CommutativeMatcher24413.get()
                                    tmp183 = subjects182
                                    subjects182 = []
                                    for s in tmp183:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp183, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 24414
                                            if len(subjects161) == 0:
                                                pass
                                                # State 24415
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: log(c*(d*(e + f*x)**p)**q)
                                        if pattern_index == 1:
                                            pass
                                            # State 26701
                                            if len(subjects161) == 0:
                                                pass
                                                # State 26702
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: log(c*(d*(e + f*x)**p)**q)
                                        if pattern_index == 2:
                                            pass
                                            # State 27768
                                            if len(subjects161) == 0:
                                                pass
                                                # State 27769
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: log(c*(d*(e + f*x)**p)**q)
                                    subjects161.appendleft(tmp181)
                            if len(subjects161) >= 1 and isinstance(subjects161[0], Add):
                                tmp184 = subjects161.popleft()
                                associative1 = tmp184
                                associative_type1 = type(tmp184)
                                subjects185 = deque(tmp184._args)
                                matcher = CommutativeMatcher24417.get()
                                tmp186 = subjects185
                                subjects185 = []
                                for s in tmp186:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp186, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 24423
                                        if len(subjects161) == 0:
                                            pass
                                            # State 24424
                                            if len(subjects) == 0:
                                                pass
                                                # 4: log(c*(d*(e + f*x)**p)**q)
                                    if pattern_index == 1:
                                        pass
                                        # State 26705
                                        if len(subjects161) == 0:
                                            pass
                                            # State 26706
                                            if len(subjects) == 0:
                                                pass
                                                # 6: log(c*(d*(e + f*x)**p)**q)
                                    if pattern_index == 2:
                                        pass
                                        # State 27289
                                        if len(subjects161) == 0:
                                            pass
                                            # State 27290
                                            if len(subjects) == 0:
                                                pass
                                                # 7: log(c*(d*(e + f*x)**p)**q)
                                    if pattern_index == 3:
                                        pass
                                        # State 27772
                                        if len(subjects161) == 0:
                                            pass
                                            # State 27773
                                            if len(subjects) == 0:
                                                pass
                                                # 8: log(c*(d*(e + f*x)**p)**q)
                                subjects161.appendleft(tmp184)
                        if len(subjects161) >= 1 and isinstance(subjects161[0], Pow):
                            tmp187 = subjects161.popleft()
                            subjects188 = deque(tmp187._args)
                            # State 24425
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 24426
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24427
                                    if len(subjects188) >= 1:
                                        tmp191 = subjects188.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.0', tmp191)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24428
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24429
                                                if len(subjects188) == 0:
                                                    pass
                                                    # State 24430
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 24431
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects188) >= 1:
                                                tmp194 = subjects188.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.1.1.2.2.2', tmp194)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24429
                                                    if len(subjects188) == 0:
                                                        pass
                                                        # State 24430
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 24431
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: log(c*(d*(e + f*x)**p)**q)
                                                subjects188.appendleft(tmp194)
                                        subjects188.appendleft(tmp191)
                                    if len(subjects188) >= 1:
                                        tmp196 = subjects188.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.1', tmp196)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26707
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26708
                                                if len(subjects188) == 0:
                                                    pass
                                                    # State 26709
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 26710
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects188) >= 1:
                                                tmp199 = subjects188.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.1.1.2.2.2', tmp199)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26708
                                                    if len(subjects188) == 0:
                                                        pass
                                                        # State 26709
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 26710
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: log(c*(d*(e + f*x)**p)**q)
                                                subjects188.appendleft(tmp199)
                                        subjects188.appendleft(tmp196)
                                    if len(subjects188) >= 1:
                                        tmp201 = subjects188.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.3.1.0', tmp201)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27774
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27775
                                                if len(subjects188) == 0:
                                                    pass
                                                    # State 27776
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 27777
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 8: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects188) >= 1:
                                                tmp204 = subjects188.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.1.1.2.2.2', tmp204)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27775
                                                    if len(subjects188) == 0:
                                                        pass
                                                        # State 27776
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 27777
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + f*x)**p)**q)
                                                subjects188.appendleft(tmp204)
                                        subjects188.appendleft(tmp201)
                                if len(subjects188) >= 1 and isinstance(subjects188[0], Mul):
                                    tmp206 = subjects188.popleft()
                                    associative1 = tmp206
                                    associative_type1 = type(tmp206)
                                    subjects207 = deque(tmp206._args)
                                    matcher = CommutativeMatcher24433.get()
                                    tmp208 = subjects207
                                    subjects207 = []
                                    for s in tmp208:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp208, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 24434
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24435
                                                if len(subjects188) == 0:
                                                    pass
                                                    # State 24436
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 24437
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects188) >= 1:
                                                tmp210 = []
                                                tmp210.append(subjects188.popleft())
                                                while True:
                                                    if len(tmp210) > 1:
                                                        tmp211 = create_operation_expression(associative1, tmp210)
                                                    elif len(tmp210) == 1:
                                                        tmp211 = tmp210[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2.2', tmp211)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 24435
                                                        if len(subjects188) == 0:
                                                            pass
                                                            # State 24436
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 24437
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 4: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects188) == 0:
                                                        break
                                                    tmp210.append(subjects188.popleft())
                                                subjects188.extendleft(reversed(tmp210))
                                        if pattern_index == 1:
                                            pass
                                            # State 26711
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26712
                                                if len(subjects188) == 0:
                                                    pass
                                                    # State 26713
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 26714
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects188) >= 1:
                                                tmp214 = []
                                                tmp214.append(subjects188.popleft())
                                                while True:
                                                    if len(tmp214) > 1:
                                                        tmp215 = create_operation_expression(associative1, tmp214)
                                                    elif len(tmp214) == 1:
                                                        tmp215 = tmp214[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2.2', tmp215)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 26712
                                                        if len(subjects188) == 0:
                                                            pass
                                                            # State 26713
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 26714
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects188) == 0:
                                                        break
                                                    tmp214.append(subjects188.popleft())
                                                subjects188.extendleft(reversed(tmp214))
                                        if pattern_index == 2:
                                            pass
                                            # State 27778
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27779
                                                if len(subjects188) == 0:
                                                    pass
                                                    # State 27780
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 27781
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 8: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects188) >= 1:
                                                tmp218 = []
                                                tmp218.append(subjects188.popleft())
                                                while True:
                                                    if len(tmp218) > 1:
                                                        tmp219 = create_operation_expression(associative1, tmp218)
                                                    elif len(tmp218) == 1:
                                                        tmp219 = tmp218[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2.2', tmp219)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27779
                                                        if len(subjects188) == 0:
                                                            pass
                                                            # State 27780
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 27781
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects188) == 0:
                                                        break
                                                    tmp218.append(subjects188.popleft())
                                                subjects188.extendleft(reversed(tmp218))
                                    subjects188.appendleft(tmp206)
                            if len(subjects188) >= 1 and isinstance(subjects188[0], Add):
                                tmp221 = subjects188.popleft()
                                associative1 = tmp221
                                associative_type1 = type(tmp221)
                                subjects222 = deque(tmp221._args)
                                matcher = CommutativeMatcher24439.get()
                                tmp223 = subjects222
                                subjects222 = []
                                for s in tmp223:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp223, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 24445
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24446
                                            if len(subjects188) == 0:
                                                pass
                                                # State 24447
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 24448
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects188) >= 1:
                                            tmp225 = []
                                            tmp225.append(subjects188.popleft())
                                            while True:
                                                if len(tmp225) > 1:
                                                    tmp226 = create_operation_expression(associative1, tmp225)
                                                elif len(tmp225) == 1:
                                                    tmp226 = tmp225[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2.2', tmp226)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24446
                                                    if len(subjects188) == 0:
                                                        pass
                                                        # State 24447
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 24448
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects188) == 0:
                                                    break
                                                tmp225.append(subjects188.popleft())
                                            subjects188.extendleft(reversed(tmp225))
                                    if pattern_index == 1:
                                        pass
                                        # State 26717
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26718
                                            if len(subjects188) == 0:
                                                pass
                                                # State 26719
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 26720
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects188) >= 1:
                                            tmp229 = []
                                            tmp229.append(subjects188.popleft())
                                            while True:
                                                if len(tmp229) > 1:
                                                    tmp230 = create_operation_expression(associative1, tmp229)
                                                elif len(tmp229) == 1:
                                                    tmp230 = tmp229[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2.2', tmp230)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26718
                                                    if len(subjects188) == 0:
                                                        pass
                                                        # State 26719
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 26720
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects188) == 0:
                                                    break
                                                tmp229.append(subjects188.popleft())
                                            subjects188.extendleft(reversed(tmp229))
                                    if pattern_index == 2:
                                        pass
                                        # State 27291
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27292
                                            if len(subjects188) == 0:
                                                pass
                                                # State 27293
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 27294
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects188) >= 1:
                                            tmp233 = []
                                            tmp233.append(subjects188.popleft())
                                            while True:
                                                if len(tmp233) > 1:
                                                    tmp234 = create_operation_expression(associative1, tmp233)
                                                elif len(tmp233) == 1:
                                                    tmp234 = tmp233[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2.2', tmp234)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27292
                                                    if len(subjects188) == 0:
                                                        pass
                                                        # State 27293
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 27294
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 7: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects188) == 0:
                                                    break
                                                tmp233.append(subjects188.popleft())
                                            subjects188.extendleft(reversed(tmp233))
                                    if pattern_index == 3:
                                        pass
                                        # State 27784
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27785
                                            if len(subjects188) == 0:
                                                pass
                                                # State 27786
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 27787
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 8: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects188) >= 1:
                                            tmp237 = []
                                            tmp237.append(subjects188.popleft())
                                            while True:
                                                if len(tmp237) > 1:
                                                    tmp238 = create_operation_expression(associative1, tmp237)
                                                elif len(tmp237) == 1:
                                                    tmp238 = tmp237[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2.2', tmp238)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27785
                                                    if len(subjects188) == 0:
                                                        pass
                                                        # State 27786
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 27787
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects188) == 0:
                                                    break
                                                tmp237.append(subjects188.popleft())
                                            subjects188.extendleft(reversed(tmp237))
                                subjects188.appendleft(tmp221)
                            subjects161.appendleft(tmp187)
                    if len(subjects161) >= 1:
                        tmp240 = subjects161.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp240)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40409
                            if len(subjects161) == 0:
                                pass
                                # State 40410
                                if len(subjects) == 0:
                                    pass
                                    # 9: log(c*x**n)
                        subjects161.appendleft(tmp240)
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 49415
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.1.1.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49416
                            if len(subjects161) >= 1 and isinstance(subjects161[0], Pow):
                                tmp244 = subjects161.popleft()
                                subjects245 = deque(tmp244._args)
                                # State 49417
                                if len(subjects245) >= 1:
                                    tmp246 = subjects245.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.0', tmp246)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49418
                                        if len(subjects245) >= 1:
                                            tmp248 = subjects245.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.1.2', tmp248)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49419
                                                if len(subjects245) == 0:
                                                    pass
                                                    # State 49420
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 49421
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 10: log(c*(d + e*x**n)**p)
                                            subjects245.appendleft(tmp248)
                                    subjects245.appendleft(tmp246)
                                if len(subjects245) >= 1:
                                    tmp250 = subjects245.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.3.1.0', tmp250)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49942
                                        if len(subjects245) >= 1:
                                            tmp252 = subjects245.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.1.2', tmp252)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49943
                                                if len(subjects245) == 0:
                                                    pass
                                                    # State 49944
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 49945
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 12: log(c*(d + e*x**n)**p)
                                            subjects245.appendleft(tmp252)
                                    subjects245.appendleft(tmp250)
                                if len(subjects245) >= 1:
                                    tmp254 = subjects245.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.1', tmp254)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50268
                                        if len(subjects245) >= 1 and subjects245[0] == 2:
                                            tmp256 = subjects245.popleft()
                                            # State 50269
                                            if len(subjects245) == 0:
                                                pass
                                                # State 50270
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 50271
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 13: log(c*(d + e*x**2)**p)
                                            subjects245.appendleft(tmp256)
                                    subjects245.appendleft(tmp254)
                                subjects161.appendleft(tmp244)
                        if len(subjects161) >= 1 and isinstance(subjects161[0], Mul):
                            tmp257 = subjects161.popleft()
                            associative1 = tmp257
                            associative_type1 = type(tmp257)
                            subjects258 = deque(tmp257._args)
                            matcher = CommutativeMatcher49423.get()
                            tmp259 = subjects258
                            subjects258 = []
                            for s in tmp259:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp259, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 49428
                                    if len(subjects161) == 0:
                                        pass
                                        # State 49429
                                        if len(subjects) == 0:
                                            pass
                                            # 10: log(c*(d + e*x**n)**p)
                                if pattern_index == 1:
                                    pass
                                    # State 49949
                                    if len(subjects161) == 0:
                                        pass
                                        # State 49950
                                        if len(subjects) == 0:
                                            pass
                                            # 12: log(c*(d + e*x**n)**p)
                                if pattern_index == 2:
                                    pass
                                    # State 50275
                                    if len(subjects161) == 0:
                                        pass
                                        # State 50276
                                        if len(subjects) == 0:
                                            pass
                                            # 13: log(c*(d + e*x**2)**p)
                            subjects161.appendleft(tmp257)
                    if len(subjects161) >= 1:
                        tmp260 = subjects161.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.1', tmp260)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49778
                            if len(subjects161) == 0:
                                pass
                                # State 49779
                                if len(subjects) == 0:
                                    pass
                                    # 11: log(c*v**p)
                        subjects161.appendleft(tmp260)
                    if len(subjects161) >= 1 and isinstance(subjects161[0], Mul):
                        tmp262 = subjects161.popleft()
                        associative1 = tmp262
                        associative_type1 = type(tmp262)
                        subjects263 = deque(tmp262._args)
                        matcher = CommutativeMatcher24450.get()
                        tmp264 = subjects263
                        subjects263 = []
                        for s in tmp264:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp264, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 24487
                                if len(subjects161) == 0:
                                    pass
                                    # State 24488
                                    if len(subjects) == 0:
                                        pass
                                        # 4: log(c*(d*(e + f*x)**p)**q)
                            if pattern_index == 1:
                                pass
                                # State 26737
                                if len(subjects161) == 0:
                                    pass
                                    # State 26738
                                    if len(subjects) == 0:
                                        pass
                                        # 6: log(c*(d*(e + f*x)**p)**q)
                            if pattern_index == 2:
                                pass
                                # State 27299
                                if len(subjects161) == 0:
                                    pass
                                    # State 27300
                                    if len(subjects) == 0:
                                        pass
                                        # 7: log(c*(d*(e + f*x)**p)**q)
                            if pattern_index == 3:
                                pass
                                # State 27804
                                if len(subjects161) == 0:
                                    pass
                                    # State 27805
                                    if len(subjects) == 0:
                                        pass
                                        # 8: log(c*(d*(e + f*x)**p)**q)
                        subjects161.appendleft(tmp262)
                    if len(subjects161) >= 1 and isinstance(subjects161[0], Add):
                        tmp265 = subjects161.popleft()
                        associative1 = tmp265
                        associative_type1 = type(tmp265)
                        subjects266 = deque(tmp265._args)
                        matcher = CommutativeMatcher49431.get()
                        tmp267 = subjects266
                        subjects266 = []
                        for s in tmp267:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp267, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 49444
                                if len(subjects161) == 0:
                                    pass
                                    # State 49445
                                    if len(subjects) == 0:
                                        pass
                                        # 10: log(c*(d + e*x**n)**p)
                            if pattern_index == 1:
                                pass
                                # State 49958
                                if len(subjects161) == 0:
                                    pass
                                    # State 49959
                                    if len(subjects) == 0:
                                        pass
                                        # 12: log(c*(d + e*x**n)**p)
                            if pattern_index == 2:
                                pass
                                # State 50284
                                if len(subjects161) == 0:
                                    pass
                                    # State 50285
                                    if len(subjects) == 0:
                                        pass
                                        # 13: log(c*(d + e*x**2)**p)
                        subjects161.appendleft(tmp265)
                if len(subjects161) >= 1 and isinstance(subjects161[0], Add):
                    tmp268 = subjects161.popleft()
                    associative1 = tmp268
                    associative_type1 = type(tmp268)
                    subjects269 = deque(tmp268._args)
                    matcher = CommutativeMatcher23947.get()
                    tmp270 = subjects269
                    subjects269 = []
                    for s in tmp270:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp270, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 23953
                            if len(subjects161) == 0:
                                pass
                                # State 23954
                                if len(subjects) == 0:
                                    pass
                                    # 3: log(c*(e + f*x))
                    subjects161.appendleft(tmp268)
                if len(subjects161) >= 1 and isinstance(subjects161[0], Pow):
                    tmp271 = subjects161.popleft()
                    subjects272 = deque(tmp271._args)
                    # State 24489
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 24490
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24491
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 24492
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24493
                                    if len(subjects272) >= 1:
                                        tmp277 = subjects272.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.0', tmp277)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24494
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24495
                                                if len(subjects272) == 0:
                                                    pass
                                                    # State 24496
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 24497
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects272) >= 1:
                                                tmp280 = subjects272.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.1.1.2.2', tmp280)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24495
                                                    if len(subjects272) == 0:
                                                        pass
                                                        # State 24496
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 24497
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: log(c*(d*(e + f*x)**p)**q)
                                                subjects272.appendleft(tmp280)
                                        subjects272.appendleft(tmp277)
                                    if len(subjects272) >= 1:
                                        tmp282 = subjects272.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.1', tmp282)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26739
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26740
                                                if len(subjects272) == 0:
                                                    pass
                                                    # State 26741
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 26742
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects272) >= 1:
                                                tmp285 = subjects272.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.1.1.2.2', tmp285)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26740
                                                    if len(subjects272) == 0:
                                                        pass
                                                        # State 26741
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 26742
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: log(c*(d*(e + f*x)**p)**q)
                                                subjects272.appendleft(tmp285)
                                        subjects272.appendleft(tmp282)
                                    if len(subjects272) >= 1:
                                        tmp287 = subjects272.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.3.1.0', tmp287)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27806
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27807
                                                if len(subjects272) == 0:
                                                    pass
                                                    # State 27808
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 27809
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 8: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects272) >= 1:
                                                tmp290 = subjects272.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.1.1.2.2', tmp290)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27807
                                                    if len(subjects272) == 0:
                                                        pass
                                                        # State 27808
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 27809
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + f*x)**p)**q)
                                                subjects272.appendleft(tmp290)
                                        subjects272.appendleft(tmp287)
                                if len(subjects272) >= 1 and isinstance(subjects272[0], Mul):
                                    tmp292 = subjects272.popleft()
                                    associative1 = tmp292
                                    associative_type1 = type(tmp292)
                                    subjects293 = deque(tmp292._args)
                                    matcher = CommutativeMatcher24499.get()
                                    tmp294 = subjects293
                                    subjects293 = []
                                    for s in tmp294:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp294, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 24500
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24501
                                                if len(subjects272) == 0:
                                                    pass
                                                    # State 24502
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 24503
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects272) >= 1:
                                                tmp296 = []
                                                tmp296.append(subjects272.popleft())
                                                while True:
                                                    if len(tmp296) > 1:
                                                        tmp297 = create_operation_expression(associative1, tmp296)
                                                    elif len(tmp296) == 1:
                                                        tmp297 = tmp296[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp297)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 24501
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 24502
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 24503
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 4: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects272) == 0:
                                                        break
                                                    tmp296.append(subjects272.popleft())
                                                subjects272.extendleft(reversed(tmp296))
                                        if pattern_index == 1:
                                            pass
                                            # State 26743
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26744
                                                if len(subjects272) == 0:
                                                    pass
                                                    # State 26745
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 26746
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects272) >= 1:
                                                tmp300 = []
                                                tmp300.append(subjects272.popleft())
                                                while True:
                                                    if len(tmp300) > 1:
                                                        tmp301 = create_operation_expression(associative1, tmp300)
                                                    elif len(tmp300) == 1:
                                                        tmp301 = tmp300[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp301)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 26744
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 26745
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 26746
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects272) == 0:
                                                        break
                                                    tmp300.append(subjects272.popleft())
                                                subjects272.extendleft(reversed(tmp300))
                                        if pattern_index == 2:
                                            pass
                                            # State 27810
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27811
                                                if len(subjects272) == 0:
                                                    pass
                                                    # State 27812
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 27813
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 8: log(c*(d*(e + f*x)**p)**q)
                                            if len(subjects272) >= 1:
                                                tmp304 = []
                                                tmp304.append(subjects272.popleft())
                                                while True:
                                                    if len(tmp304) > 1:
                                                        tmp305 = create_operation_expression(associative1, tmp304)
                                                    elif len(tmp304) == 1:
                                                        tmp305 = tmp304[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp305)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27811
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 27812
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 27813
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects272) == 0:
                                                        break
                                                    tmp304.append(subjects272.popleft())
                                                subjects272.extendleft(reversed(tmp304))
                                    subjects272.appendleft(tmp292)
                            if len(subjects272) >= 1 and isinstance(subjects272[0], Add):
                                tmp307 = subjects272.popleft()
                                associative1 = tmp307
                                associative_type1 = type(tmp307)
                                subjects308 = deque(tmp307._args)
                                matcher = CommutativeMatcher24505.get()
                                tmp309 = subjects308
                                subjects308 = []
                                for s in tmp309:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp309, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 24511
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24512
                                            if len(subjects272) == 0:
                                                pass
                                                # State 24513
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 24514
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects272) >= 1:
                                            tmp311 = []
                                            tmp311.append(subjects272.popleft())
                                            while True:
                                                if len(tmp311) > 1:
                                                    tmp312 = create_operation_expression(associative1, tmp311)
                                                elif len(tmp311) == 1:
                                                    tmp312 = tmp311[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp312)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24512
                                                    if len(subjects272) == 0:
                                                        pass
                                                        # State 24513
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 24514
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects272) == 0:
                                                    break
                                                tmp311.append(subjects272.popleft())
                                            subjects272.extendleft(reversed(tmp311))
                                    if pattern_index == 1:
                                        pass
                                        # State 26749
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26750
                                            if len(subjects272) == 0:
                                                pass
                                                # State 26751
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 26752
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects272) >= 1:
                                            tmp315 = []
                                            tmp315.append(subjects272.popleft())
                                            while True:
                                                if len(tmp315) > 1:
                                                    tmp316 = create_operation_expression(associative1, tmp315)
                                                elif len(tmp315) == 1:
                                                    tmp316 = tmp315[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp316)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26750
                                                    if len(subjects272) == 0:
                                                        pass
                                                        # State 26751
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 26752
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects272) == 0:
                                                    break
                                                tmp315.append(subjects272.popleft())
                                            subjects272.extendleft(reversed(tmp315))
                                    if pattern_index == 2:
                                        pass
                                        # State 27301
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27302
                                            if len(subjects272) == 0:
                                                pass
                                                # State 27303
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 27304
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects272) >= 1:
                                            tmp319 = []
                                            tmp319.append(subjects272.popleft())
                                            while True:
                                                if len(tmp319) > 1:
                                                    tmp320 = create_operation_expression(associative1, tmp319)
                                                elif len(tmp319) == 1:
                                                    tmp320 = tmp319[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp320)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27302
                                                    if len(subjects272) == 0:
                                                        pass
                                                        # State 27303
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 27304
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 7: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects272) == 0:
                                                    break
                                                tmp319.append(subjects272.popleft())
                                            subjects272.extendleft(reversed(tmp319))
                                    if pattern_index == 3:
                                        pass
                                        # State 27816
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27817
                                            if len(subjects272) == 0:
                                                pass
                                                # State 27818
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 27819
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 8: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects272) >= 1:
                                            tmp323 = []
                                            tmp323.append(subjects272.popleft())
                                            while True:
                                                if len(tmp323) > 1:
                                                    tmp324 = create_operation_expression(associative1, tmp323)
                                                elif len(tmp323) == 1:
                                                    tmp324 = tmp323[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp324)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27817
                                                    if len(subjects272) == 0:
                                                        pass
                                                        # State 27818
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 27819
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects272) == 0:
                                                    break
                                                tmp323.append(subjects272.popleft())
                                            subjects272.extendleft(reversed(tmp323))
                                subjects272.appendleft(tmp307)
                        if len(subjects272) >= 1 and isinstance(subjects272[0], Pow):
                            tmp326 = subjects272.popleft()
                            subjects327 = deque(tmp326._args)
                            # State 24515
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 24516
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24517
                                    if len(subjects327) >= 1:
                                        tmp330 = subjects327.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.0', tmp330)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24518
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24519
                                                if len(subjects327) == 0:
                                                    pass
                                                    # State 24520
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 24521
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 24522
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 24523
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 4: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects272) >= 1:
                                                        tmp334 = subjects272.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.1.1.2.2', tmp334)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 24521
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 24522
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 24523
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 4: log(c*(d*(e + f*x)**p)**q)
                                                        subjects272.appendleft(tmp334)
                                            if len(subjects327) >= 1:
                                                tmp336 = subjects327.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2.2', tmp336)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24519
                                                    if len(subjects327) == 0:
                                                        pass
                                                        # State 24520
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 24521
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 24522
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 24523
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 4: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects272) >= 1:
                                                            tmp339 = subjects272.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.1.1.2.2', tmp339)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 24521
                                                                if len(subjects272) == 0:
                                                                    pass
                                                                    # State 24522
                                                                    if len(subjects161) == 0:
                                                                        pass
                                                                        # State 24523
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 4: log(c*(d*(e + f*x)**p)**q)
                                                            subjects272.appendleft(tmp339)
                                                subjects327.appendleft(tmp336)
                                        subjects327.appendleft(tmp330)
                                    if len(subjects327) >= 1:
                                        tmp341 = subjects327.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.1', tmp341)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26753
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26754
                                                if len(subjects327) == 0:
                                                    pass
                                                    # State 26755
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 26756
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 26757
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 26758
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects272) >= 1:
                                                        tmp345 = subjects272.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.1.1.2.2', tmp345)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 26756
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 26757
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 26758
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 6: log(c*(d*(e + f*x)**p)**q)
                                                        subjects272.appendleft(tmp345)
                                            if len(subjects327) >= 1:
                                                tmp347 = subjects327.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2.2', tmp347)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26754
                                                    if len(subjects327) == 0:
                                                        pass
                                                        # State 26755
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 26756
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 26757
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 26758
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 6: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects272) >= 1:
                                                            tmp350 = subjects272.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.1.1.2.2', tmp350)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 26756
                                                                if len(subjects272) == 0:
                                                                    pass
                                                                    # State 26757
                                                                    if len(subjects161) == 0:
                                                                        pass
                                                                        # State 26758
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 6: log(c*(d*(e + f*x)**p)**q)
                                                            subjects272.appendleft(tmp350)
                                                subjects327.appendleft(tmp347)
                                        subjects327.appendleft(tmp341)
                                    if len(subjects327) >= 1:
                                        tmp352 = subjects327.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.3.1.0', tmp352)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27820
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27821
                                                if len(subjects327) == 0:
                                                    pass
                                                    # State 27822
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27823
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 27824
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 27825
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects272) >= 1:
                                                        tmp356 = subjects272.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.1.1.2.2', tmp356)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 27823
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 27824
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 27825
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 8: log(c*(d*(e + f*x)**p)**q)
                                                        subjects272.appendleft(tmp356)
                                            if len(subjects327) >= 1:
                                                tmp358 = subjects327.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2.2', tmp358)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27821
                                                    if len(subjects327) == 0:
                                                        pass
                                                        # State 27822
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 27823
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 27824
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 27825
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 8: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects272) >= 1:
                                                            tmp361 = subjects272.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.1.1.2.2', tmp361)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 27823
                                                                if len(subjects272) == 0:
                                                                    pass
                                                                    # State 27824
                                                                    if len(subjects161) == 0:
                                                                        pass
                                                                        # State 27825
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 8: log(c*(d*(e + f*x)**p)**q)
                                                            subjects272.appendleft(tmp361)
                                                subjects327.appendleft(tmp358)
                                        subjects327.appendleft(tmp352)
                                if len(subjects327) >= 1 and isinstance(subjects327[0], Mul):
                                    tmp363 = subjects327.popleft()
                                    associative1 = tmp363
                                    associative_type1 = type(tmp363)
                                    subjects364 = deque(tmp363._args)
                                    matcher = CommutativeMatcher24525.get()
                                    tmp365 = subjects364
                                    subjects364 = []
                                    for s in tmp365:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp365, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 24526
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24527
                                                if len(subjects327) == 0:
                                                    pass
                                                    # State 24528
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 24529
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 24530
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 24531
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 4: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects272) >= 1:
                                                        tmp368 = subjects272.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.1.1.2.2', tmp368)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 24529
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 24530
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 24531
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 4: log(c*(d*(e + f*x)**p)**q)
                                                        subjects272.appendleft(tmp368)
                                            if len(subjects327) >= 1:
                                                tmp370 = []
                                                tmp370.append(subjects327.popleft())
                                                while True:
                                                    if len(tmp370) > 1:
                                                        tmp371 = create_operation_expression(associative1, tmp370)
                                                    elif len(tmp370) == 1:
                                                        tmp371 = tmp370[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2.2', tmp371)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 24527
                                                        if len(subjects327) == 0:
                                                            pass
                                                            # State 24528
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 24529
                                                                if len(subjects272) == 0:
                                                                    pass
                                                                    # State 24530
                                                                    if len(subjects161) == 0:
                                                                        pass
                                                                        # State 24531
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 4: log(c*(d*(e + f*x)**p)**q)
                                                            if len(subjects272) >= 1:
                                                                tmp374 = subjects272.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.1.1.2.2', tmp374)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 24529
                                                                    if len(subjects272) == 0:
                                                                        pass
                                                                        # State 24530
                                                                        if len(subjects161) == 0:
                                                                            pass
                                                                            # State 24531
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 4: log(c*(d*(e + f*x)**p)**q)
                                                                subjects272.appendleft(tmp374)
                                                    if len(subjects327) == 0:
                                                        break
                                                    tmp370.append(subjects327.popleft())
                                                subjects327.extendleft(reversed(tmp370))
                                        if pattern_index == 1:
                                            pass
                                            # State 26759
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26760
                                                if len(subjects327) == 0:
                                                    pass
                                                    # State 26761
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 26762
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 26763
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 26764
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects272) >= 1:
                                                        tmp378 = subjects272.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.1.1.2.2', tmp378)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 26762
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 26763
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 26764
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 6: log(c*(d*(e + f*x)**p)**q)
                                                        subjects272.appendleft(tmp378)
                                            if len(subjects327) >= 1:
                                                tmp380 = []
                                                tmp380.append(subjects327.popleft())
                                                while True:
                                                    if len(tmp380) > 1:
                                                        tmp381 = create_operation_expression(associative1, tmp380)
                                                    elif len(tmp380) == 1:
                                                        tmp381 = tmp380[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2.2', tmp381)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 26760
                                                        if len(subjects327) == 0:
                                                            pass
                                                            # State 26761
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 26762
                                                                if len(subjects272) == 0:
                                                                    pass
                                                                    # State 26763
                                                                    if len(subjects161) == 0:
                                                                        pass
                                                                        # State 26764
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 6: log(c*(d*(e + f*x)**p)**q)
                                                            if len(subjects272) >= 1:
                                                                tmp384 = subjects272.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.1.1.2.2', tmp384)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 26762
                                                                    if len(subjects272) == 0:
                                                                        pass
                                                                        # State 26763
                                                                        if len(subjects161) == 0:
                                                                            pass
                                                                            # State 26764
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 6: log(c*(d*(e + f*x)**p)**q)
                                                                subjects272.appendleft(tmp384)
                                                    if len(subjects327) == 0:
                                                        break
                                                    tmp380.append(subjects327.popleft())
                                                subjects327.extendleft(reversed(tmp380))
                                        if pattern_index == 2:
                                            pass
                                            # State 27826
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27827
                                                if len(subjects327) == 0:
                                                    pass
                                                    # State 27828
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27829
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 27830
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 27831
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + f*x)**p)**q)
                                                    if len(subjects272) >= 1:
                                                        tmp388 = subjects272.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.1.1.2.2', tmp388)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 27829
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 27830
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 27831
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 8: log(c*(d*(e + f*x)**p)**q)
                                                        subjects272.appendleft(tmp388)
                                            if len(subjects327) >= 1:
                                                tmp390 = []
                                                tmp390.append(subjects327.popleft())
                                                while True:
                                                    if len(tmp390) > 1:
                                                        tmp391 = create_operation_expression(associative1, tmp390)
                                                    elif len(tmp390) == 1:
                                                        tmp391 = tmp390[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2.2', tmp391)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27827
                                                        if len(subjects327) == 0:
                                                            pass
                                                            # State 27828
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 27829
                                                                if len(subjects272) == 0:
                                                                    pass
                                                                    # State 27830
                                                                    if len(subjects161) == 0:
                                                                        pass
                                                                        # State 27831
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 8: log(c*(d*(e + f*x)**p)**q)
                                                            if len(subjects272) >= 1:
                                                                tmp394 = subjects272.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.1.1.2.2', tmp394)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 27829
                                                                    if len(subjects272) == 0:
                                                                        pass
                                                                        # State 27830
                                                                        if len(subjects161) == 0:
                                                                            pass
                                                                            # State 27831
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 8: log(c*(d*(e + f*x)**p)**q)
                                                                subjects272.appendleft(tmp394)
                                                    if len(subjects327) == 0:
                                                        break
                                                    tmp390.append(subjects327.popleft())
                                                subjects327.extendleft(reversed(tmp390))
                                    subjects327.appendleft(tmp363)
                            if len(subjects327) >= 1 and isinstance(subjects327[0], Add):
                                tmp396 = subjects327.popleft()
                                associative1 = tmp396
                                associative_type1 = type(tmp396)
                                subjects397 = deque(tmp396._args)
                                matcher = CommutativeMatcher24533.get()
                                tmp398 = subjects397
                                subjects397 = []
                                for s in tmp398:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp398, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 24539
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24540
                                            if len(subjects327) == 0:
                                                pass
                                                # State 24541
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24542
                                                    if len(subjects272) == 0:
                                                        pass
                                                        # State 24543
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 24544
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects272) >= 1:
                                                    tmp401 = subjects272.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', tmp401)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 24542
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 24543
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 24544
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 4: log(c*(d*(e + f*x)**p)**q)
                                                    subjects272.appendleft(tmp401)
                                        if len(subjects327) >= 1:
                                            tmp403 = []
                                            tmp403.append(subjects327.popleft())
                                            while True:
                                                if len(tmp403) > 1:
                                                    tmp404 = create_operation_expression(associative1, tmp403)
                                                elif len(tmp403) == 1:
                                                    tmp404 = tmp403[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2.2', tmp404)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24540
                                                    if len(subjects327) == 0:
                                                        pass
                                                        # State 24541
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 24542
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 24543
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 24544
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 4: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects272) >= 1:
                                                            tmp407 = subjects272.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.1.1.2.2', tmp407)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 24542
                                                                if len(subjects272) == 0:
                                                                    pass
                                                                    # State 24543
                                                                    if len(subjects161) == 0:
                                                                        pass
                                                                        # State 24544
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 4: log(c*(d*(e + f*x)**p)**q)
                                                            subjects272.appendleft(tmp407)
                                                if len(subjects327) == 0:
                                                    break
                                                tmp403.append(subjects327.popleft())
                                            subjects327.extendleft(reversed(tmp403))
                                    if pattern_index == 1:
                                        pass
                                        # State 26767
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26768
                                            if len(subjects327) == 0:
                                                pass
                                                # State 26769
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26770
                                                    if len(subjects272) == 0:
                                                        pass
                                                        # State 26771
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 26772
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects272) >= 1:
                                                    tmp411 = subjects272.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', tmp411)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 26770
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 26771
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 26772
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: log(c*(d*(e + f*x)**p)**q)
                                                    subjects272.appendleft(tmp411)
                                        if len(subjects327) >= 1:
                                            tmp413 = []
                                            tmp413.append(subjects327.popleft())
                                            while True:
                                                if len(tmp413) > 1:
                                                    tmp414 = create_operation_expression(associative1, tmp413)
                                                elif len(tmp413) == 1:
                                                    tmp414 = tmp413[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2.2', tmp414)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26768
                                                    if len(subjects327) == 0:
                                                        pass
                                                        # State 26769
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 26770
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 26771
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 26772
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 6: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects272) >= 1:
                                                            tmp417 = subjects272.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.1.1.2.2', tmp417)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 26770
                                                                if len(subjects272) == 0:
                                                                    pass
                                                                    # State 26771
                                                                    if len(subjects161) == 0:
                                                                        pass
                                                                        # State 26772
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 6: log(c*(d*(e + f*x)**p)**q)
                                                            subjects272.appendleft(tmp417)
                                                if len(subjects327) == 0:
                                                    break
                                                tmp413.append(subjects327.popleft())
                                            subjects327.extendleft(reversed(tmp413))
                                    if pattern_index == 2:
                                        pass
                                        # State 27305
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27306
                                            if len(subjects327) == 0:
                                                pass
                                                # State 27307
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27308
                                                    if len(subjects272) == 0:
                                                        pass
                                                        # State 27309
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 27310
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 7: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects272) >= 1:
                                                    tmp421 = subjects272.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', tmp421)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27308
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 27309
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 27310
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 7: log(c*(d*(e + f*x)**p)**q)
                                                    subjects272.appendleft(tmp421)
                                        if len(subjects327) >= 1:
                                            tmp423 = []
                                            tmp423.append(subjects327.popleft())
                                            while True:
                                                if len(tmp423) > 1:
                                                    tmp424 = create_operation_expression(associative1, tmp423)
                                                elif len(tmp423) == 1:
                                                    tmp424 = tmp423[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2.2', tmp424)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27306
                                                    if len(subjects327) == 0:
                                                        pass
                                                        # State 27307
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 27308
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 27309
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 27310
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 7: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects272) >= 1:
                                                            tmp427 = subjects272.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.1.1.2.2', tmp427)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 27308
                                                                if len(subjects272) == 0:
                                                                    pass
                                                                    # State 27309
                                                                    if len(subjects161) == 0:
                                                                        pass
                                                                        # State 27310
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 7: log(c*(d*(e + f*x)**p)**q)
                                                            subjects272.appendleft(tmp427)
                                                if len(subjects327) == 0:
                                                    break
                                                tmp423.append(subjects327.popleft())
                                            subjects327.extendleft(reversed(tmp423))
                                    if pattern_index == 3:
                                        pass
                                        # State 27834
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27835
                                            if len(subjects327) == 0:
                                                pass
                                                # State 27836
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27837
                                                    if len(subjects272) == 0:
                                                        pass
                                                        # State 27838
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 27839
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + f*x)**p)**q)
                                                if len(subjects272) >= 1:
                                                    tmp431 = subjects272.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', tmp431)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27837
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 27838
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 27839
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + f*x)**p)**q)
                                                    subjects272.appendleft(tmp431)
                                        if len(subjects327) >= 1:
                                            tmp433 = []
                                            tmp433.append(subjects327.popleft())
                                            while True:
                                                if len(tmp433) > 1:
                                                    tmp434 = create_operation_expression(associative1, tmp433)
                                                elif len(tmp433) == 1:
                                                    tmp434 = tmp433[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2.2', tmp434)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27835
                                                    if len(subjects327) == 0:
                                                        pass
                                                        # State 27836
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 27837
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 27838
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 27839
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 8: log(c*(d*(e + f*x)**p)**q)
                                                        if len(subjects272) >= 1:
                                                            tmp437 = subjects272.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.1.1.2.2', tmp437)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 27837
                                                                if len(subjects272) == 0:
                                                                    pass
                                                                    # State 27838
                                                                    if len(subjects161) == 0:
                                                                        pass
                                                                        # State 27839
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 8: log(c*(d*(e + f*x)**p)**q)
                                                            subjects272.appendleft(tmp437)
                                                if len(subjects327) == 0:
                                                    break
                                                tmp433.append(subjects327.popleft())
                                            subjects327.extendleft(reversed(tmp433))
                                subjects327.appendleft(tmp396)
                            subjects272.appendleft(tmp326)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 26418
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 26419
                            if len(subjects272) >= 1:
                                tmp441 = subjects272.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.1', tmp441)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26420
                                    if len(subjects272) >= 1 and subjects272[0] == -1:
                                        tmp443 = subjects272.popleft()
                                        # State 26421
                                        if len(subjects272) == 0:
                                            pass
                                            # State 26422
                                            if len(subjects161) == 0:
                                                pass
                                                # State 26423
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: log(c/(e + f*x))
                                        subjects272.appendleft(tmp443)
                                subjects272.appendleft(tmp441)
                            if len(subjects272) >= 1 and isinstance(subjects272[0], Pow):
                                tmp444 = subjects272.popleft()
                                subjects445 = deque(tmp444._args)
                                # State 49446
                                if len(subjects445) >= 1:
                                    tmp446 = subjects445.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.0', tmp446)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49447
                                        if len(subjects445) >= 1:
                                            tmp448 = subjects445.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.1.2', tmp448)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49448
                                                if len(subjects445) == 0:
                                                    pass
                                                    # State 49449
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 49450
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 49451
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 49452
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 10: log(c*(d + e*x**n)**p)
                                                    if len(subjects272) >= 1:
                                                        tmp451 = subjects272.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.1.1.2.2', tmp451)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 49450
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 49451
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 49452
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 10: log(c*(d + e*x**n)**p)
                                                        subjects272.appendleft(tmp451)
                                            subjects445.appendleft(tmp448)
                                    subjects445.appendleft(tmp446)
                                if len(subjects445) >= 1:
                                    tmp453 = subjects445.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.1.0', tmp453)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49960
                                        if len(subjects445) >= 1:
                                            tmp455 = subjects445.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.1.2', tmp455)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49961
                                                if len(subjects445) == 0:
                                                    pass
                                                    # State 49962
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 49963
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 49964
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 49965
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 12: log(c*(d + e*x**n)**p)
                                                    if len(subjects272) >= 1:
                                                        tmp458 = subjects272.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.1.1.2.2', tmp458)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 49963
                                                            if len(subjects272) == 0:
                                                                pass
                                                                # State 49964
                                                                if len(subjects161) == 0:
                                                                    pass
                                                                    # State 49965
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 12: log(c*(d + e*x**n)**p)
                                                        subjects272.appendleft(tmp458)
                                            subjects445.appendleft(tmp455)
                                    subjects445.appendleft(tmp453)
                                if len(subjects445) >= 1:
                                    tmp460 = subjects445.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.1', tmp460)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50286
                                        if len(subjects445) >= 1 and subjects445[0] == 2:
                                            tmp462 = subjects445.popleft()
                                            # State 50287
                                            if len(subjects445) == 0:
                                                pass
                                                # State 50288
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 50289
                                                    if len(subjects272) == 0:
                                                        pass
                                                        # State 50290
                                                        if len(subjects161) == 0:
                                                            pass
                                                            # State 50291
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 13: log(c*(d + e*x**2)**p)
                                                if len(subjects272) >= 1:
                                                    tmp464 = subjects272.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', tmp464)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 50289
                                                        if len(subjects272) == 0:
                                                            pass
                                                            # State 50290
                                                            if len(subjects161) == 0:
                                                                pass
                                                                # State 50291
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 13: log(c*(d + e*x**2)**p)
                                                    subjects272.appendleft(tmp464)
                                            subjects445.appendleft(tmp462)
                                    subjects445.appendleft(tmp460)
                                subjects272.appendleft(tmp444)
                        if len(subjects272) >= 1 and isinstance(subjects272[0], Mul):
                            tmp466 = subjects272.popleft()
                            associative1 = tmp466
                            associative_type1 = type(tmp466)
                            subjects467 = deque(tmp466._args)
                            matcher = CommutativeMatcher26425.get()
                            tmp468 = subjects467
                            subjects467 = []
                            for s in tmp468:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp468, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 26426
                                    if len(subjects272) >= 1 and subjects272[0] == -1:
                                        tmp469 = subjects272.popleft()
                                        # State 26427
                                        if len(subjects272) == 0:
                                            pass
                                            # State 26428
                                            if len(subjects161) == 0:
                                                pass
                                                # State 26429
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: log(c/(e + f*x))
                                        subjects272.appendleft(tmp469)
                                if pattern_index == 1:
                                    pass
                                    # State 49457
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49458
                                        if len(subjects272) == 0:
                                            pass
                                            # State 49459
                                            if len(subjects161) == 0:
                                                pass
                                                # State 49460
                                                if len(subjects) == 0:
                                                    pass
                                                    # 10: log(c*(d + e*x**n)**p)
                                    if len(subjects272) >= 1:
                                        tmp471 = []
                                        tmp471.append(subjects272.popleft())
                                        while True:
                                            if len(tmp471) > 1:
                                                tmp472 = create_operation_expression(associative1, tmp471)
                                            elif len(tmp471) == 1:
                                                tmp472 = tmp471[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp472)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49458
                                                if len(subjects272) == 0:
                                                    pass
                                                    # State 49459
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 49460
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 10: log(c*(d + e*x**n)**p)
                                            if len(subjects272) == 0:
                                                break
                                            tmp471.append(subjects272.popleft())
                                        subjects272.extendleft(reversed(tmp471))
                                if pattern_index == 2:
                                    pass
                                    # State 49969
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49970
                                        if len(subjects272) == 0:
                                            pass
                                            # State 49971
                                            if len(subjects161) == 0:
                                                pass
                                                # State 49972
                                                if len(subjects) == 0:
                                                    pass
                                                    # 12: log(c*(d + e*x**n)**p)
                                    if len(subjects272) >= 1:
                                        tmp475 = []
                                        tmp475.append(subjects272.popleft())
                                        while True:
                                            if len(tmp475) > 1:
                                                tmp476 = create_operation_expression(associative1, tmp475)
                                            elif len(tmp475) == 1:
                                                tmp476 = tmp475[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp476)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49970
                                                if len(subjects272) == 0:
                                                    pass
                                                    # State 49971
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 49972
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 12: log(c*(d + e*x**n)**p)
                                            if len(subjects272) == 0:
                                                break
                                            tmp475.append(subjects272.popleft())
                                        subjects272.extendleft(reversed(tmp475))
                                if pattern_index == 3:
                                    pass
                                    # State 50295
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50296
                                        if len(subjects272) == 0:
                                            pass
                                            # State 50297
                                            if len(subjects161) == 0:
                                                pass
                                                # State 50298
                                                if len(subjects) == 0:
                                                    pass
                                                    # 13: log(c*(d + e*x**2)**p)
                                    if len(subjects272) >= 1:
                                        tmp479 = []
                                        tmp479.append(subjects272.popleft())
                                        while True:
                                            if len(tmp479) > 1:
                                                tmp480 = create_operation_expression(associative1, tmp479)
                                            elif len(tmp479) == 1:
                                                tmp480 = tmp479[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp480)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 50296
                                                if len(subjects272) == 0:
                                                    pass
                                                    # State 50297
                                                    if len(subjects161) == 0:
                                                        pass
                                                        # State 50298
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 13: log(c*(d + e*x**2)**p)
                                            if len(subjects272) == 0:
                                                break
                                            tmp479.append(subjects272.popleft())
                                        subjects272.extendleft(reversed(tmp479))
                            subjects272.appendleft(tmp466)
                    if len(subjects272) >= 1:
                        tmp482 = subjects272.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.1', tmp482)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40411
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 40412
                                if len(subjects272) == 0:
                                    pass
                                    # State 40413
                                    if len(subjects161) == 0:
                                        pass
                                        # State 40414
                                        if len(subjects) == 0:
                                            pass
                                            # 9: log(c*x**n)
                            if len(subjects272) >= 1:
                                tmp485 = subjects272.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', tmp485)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40412
                                    if len(subjects272) == 0:
                                        pass
                                        # State 40413
                                        if len(subjects161) == 0:
                                            pass
                                            # State 40414
                                            if len(subjects) == 0:
                                                pass
                                                # 9: log(c*x**n)
                                subjects272.appendleft(tmp485)
                        subjects272.appendleft(tmp482)
                    if len(subjects272) >= 1:
                        tmp487 = subjects272.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.1', tmp487)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49780
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49781
                                if len(subjects272) == 0:
                                    pass
                                    # State 49782
                                    if len(subjects161) == 0:
                                        pass
                                        # State 49783
                                        if len(subjects) == 0:
                                            pass
                                            # 11: log(c*v**p)
                            if len(subjects272) >= 1:
                                tmp490 = subjects272.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', tmp490)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49781
                                    if len(subjects272) == 0:
                                        pass
                                        # State 49782
                                        if len(subjects161) == 0:
                                            pass
                                            # State 49783
                                            if len(subjects) == 0:
                                                pass
                                                # 11: log(c*v**p)
                                subjects272.appendleft(tmp490)
                        subjects272.appendleft(tmp487)
                    if len(subjects272) >= 1 and isinstance(subjects272[0], Mul):
                        tmp492 = subjects272.popleft()
                        associative1 = tmp492
                        associative_type1 = type(tmp492)
                        subjects493 = deque(tmp492._args)
                        matcher = CommutativeMatcher24546.get()
                        tmp494 = subjects493
                        subjects493 = []
                        for s in tmp494:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp494, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 24583
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24584
                                    if len(subjects272) == 0:
                                        pass
                                        # State 24585
                                        if len(subjects161) == 0:
                                            pass
                                            # State 24586
                                            if len(subjects) == 0:
                                                pass
                                                # 4: log(c*(d*(e + f*x)**p)**q)
                                if len(subjects272) >= 1:
                                    tmp496 = []
                                    tmp496.append(subjects272.popleft())
                                    while True:
                                        if len(tmp496) > 1:
                                            tmp497 = create_operation_expression(associative1, tmp496)
                                        elif len(tmp496) == 1:
                                            tmp497 = tmp496[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp497)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24584
                                            if len(subjects272) == 0:
                                                pass
                                                # State 24585
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 24586
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects272) == 0:
                                            break
                                        tmp496.append(subjects272.popleft())
                                    subjects272.extendleft(reversed(tmp496))
                            if pattern_index == 1:
                                pass
                                # State 26789
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26790
                                    if len(subjects272) == 0:
                                        pass
                                        # State 26791
                                        if len(subjects161) == 0:
                                            pass
                                            # State 26792
                                            if len(subjects) == 0:
                                                pass
                                                # 6: log(c*(d*(e + f*x)**p)**q)
                                if len(subjects272) >= 1:
                                    tmp500 = []
                                    tmp500.append(subjects272.popleft())
                                    while True:
                                        if len(tmp500) > 1:
                                            tmp501 = create_operation_expression(associative1, tmp500)
                                        elif len(tmp500) == 1:
                                            tmp501 = tmp500[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp501)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26790
                                            if len(subjects272) == 0:
                                                pass
                                                # State 26791
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 26792
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects272) == 0:
                                            break
                                        tmp500.append(subjects272.popleft())
                                    subjects272.extendleft(reversed(tmp500))
                            if pattern_index == 2:
                                pass
                                # State 27315
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27316
                                    if len(subjects272) == 0:
                                        pass
                                        # State 27317
                                        if len(subjects161) == 0:
                                            pass
                                            # State 27318
                                            if len(subjects) == 0:
                                                pass
                                                # 7: log(c*(d*(e + f*x)**p)**q)
                                if len(subjects272) >= 1:
                                    tmp504 = []
                                    tmp504.append(subjects272.popleft())
                                    while True:
                                        if len(tmp504) > 1:
                                            tmp505 = create_operation_expression(associative1, tmp504)
                                        elif len(tmp504) == 1:
                                            tmp505 = tmp504[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp505)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27316
                                            if len(subjects272) == 0:
                                                pass
                                                # State 27317
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 27318
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects272) == 0:
                                            break
                                        tmp504.append(subjects272.popleft())
                                    subjects272.extendleft(reversed(tmp504))
                            if pattern_index == 3:
                                pass
                                # State 27856
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27857
                                    if len(subjects272) == 0:
                                        pass
                                        # State 27858
                                        if len(subjects161) == 0:
                                            pass
                                            # State 27859
                                            if len(subjects) == 0:
                                                pass
                                                # 8: log(c*(d*(e + f*x)**p)**q)
                                if len(subjects272) >= 1:
                                    tmp508 = []
                                    tmp508.append(subjects272.popleft())
                                    while True:
                                        if len(tmp508) > 1:
                                            tmp509 = create_operation_expression(associative1, tmp508)
                                        elif len(tmp508) == 1:
                                            tmp509 = tmp508[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp509)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27857
                                            if len(subjects272) == 0:
                                                pass
                                                # State 27858
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 27859
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 8: log(c*(d*(e + f*x)**p)**q)
                                        if len(subjects272) == 0:
                                            break
                                        tmp508.append(subjects272.popleft())
                                    subjects272.extendleft(reversed(tmp508))
                        subjects272.appendleft(tmp492)
                    if len(subjects272) >= 1 and isinstance(subjects272[0], Add):
                        tmp511 = subjects272.popleft()
                        associative1 = tmp511
                        associative_type1 = type(tmp511)
                        subjects512 = deque(tmp511._args)
                        matcher = CommutativeMatcher26431.get()
                        tmp513 = subjects512
                        subjects512 = []
                        for s in tmp513:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp513, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 26437
                                if len(subjects272) >= 1 and subjects272[0] == -1:
                                    tmp514 = subjects272.popleft()
                                    # State 26438
                                    if len(subjects272) == 0:
                                        pass
                                        # State 26439
                                        if len(subjects161) == 0:
                                            pass
                                            # State 26440
                                            if len(subjects) == 0:
                                                pass
                                                # 5: log(c/(e + f*x))
                                    subjects272.appendleft(tmp514)
                            if pattern_index == 1:
                                pass
                                # State 49470
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49471
                                    if len(subjects272) == 0:
                                        pass
                                        # State 49472
                                        if len(subjects161) == 0:
                                            pass
                                            # State 49473
                                            if len(subjects) == 0:
                                                pass
                                                # 10: log(c*(d + e*x**n)**p)
                                if len(subjects272) >= 1:
                                    tmp516 = []
                                    tmp516.append(subjects272.popleft())
                                    while True:
                                        if len(tmp516) > 1:
                                            tmp517 = create_operation_expression(associative1, tmp516)
                                        elif len(tmp516) == 1:
                                            tmp517 = tmp516[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp517)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 49471
                                            if len(subjects272) == 0:
                                                pass
                                                # State 49472
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 49473
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 10: log(c*(d + e*x**n)**p)
                                        if len(subjects272) == 0:
                                            break
                                        tmp516.append(subjects272.popleft())
                                    subjects272.extendleft(reversed(tmp516))
                            if pattern_index == 2:
                                pass
                                # State 49980
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49981
                                    if len(subjects272) == 0:
                                        pass
                                        # State 49982
                                        if len(subjects161) == 0:
                                            pass
                                            # State 49983
                                            if len(subjects) == 0:
                                                pass
                                                # 12: log(c*(d + e*x**n)**p)
                                if len(subjects272) >= 1:
                                    tmp520 = []
                                    tmp520.append(subjects272.popleft())
                                    while True:
                                        if len(tmp520) > 1:
                                            tmp521 = create_operation_expression(associative1, tmp520)
                                        elif len(tmp520) == 1:
                                            tmp521 = tmp520[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp521)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 49981
                                            if len(subjects272) == 0:
                                                pass
                                                # State 49982
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 49983
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 12: log(c*(d + e*x**n)**p)
                                        if len(subjects272) == 0:
                                            break
                                        tmp520.append(subjects272.popleft())
                                    subjects272.extendleft(reversed(tmp520))
                            if pattern_index == 3:
                                pass
                                # State 50306
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 50307
                                    if len(subjects272) == 0:
                                        pass
                                        # State 50308
                                        if len(subjects161) == 0:
                                            pass
                                            # State 50309
                                            if len(subjects) == 0:
                                                pass
                                                # 13: log(c*(d + e*x**2)**p)
                                if len(subjects272) >= 1:
                                    tmp524 = []
                                    tmp524.append(subjects272.popleft())
                                    while True:
                                        if len(tmp524) > 1:
                                            tmp525 = create_operation_expression(associative1, tmp524)
                                        elif len(tmp524) == 1:
                                            tmp525 = tmp524[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2', tmp525)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 50307
                                            if len(subjects272) == 0:
                                                pass
                                                # State 50308
                                                if len(subjects161) == 0:
                                                    pass
                                                    # State 50309
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 13: log(c*(d + e*x**2)**p)
                                        if len(subjects272) == 0:
                                            break
                                        tmp524.append(subjects272.popleft())
                                    subjects272.extendleft(reversed(tmp524))
                        subjects272.appendleft(tmp511)
                    subjects161.appendleft(tmp271)
            if len(subjects161) >= 1:
                tmp527 = subjects161.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp527)
                except ValueError:
                    pass
                else:
                    pass
                    # State 51109
                    if len(subjects161) == 0:
                        pass
                        # State 51110
                        if len(subjects) == 0:
                            pass
                            # 14: log(u)
                subjects161.appendleft(tmp527)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 54085
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 54086
                    if len(subjects161) >= 1:
                        tmp531 = subjects161.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp531)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 54087
                            if len(subjects161) == 0:
                                pass
                                # State 54088
                                if len(subjects) == 0:
                                    pass
                                    # 15: log(c + x*d)
                        subjects161.appendleft(tmp531)
                if len(subjects161) >= 1 and isinstance(subjects161[0], Mul):
                    tmp533 = subjects161.popleft()
                    associative1 = tmp533
                    associative_type1 = type(tmp533)
                    subjects534 = deque(tmp533._args)
                    matcher = CommutativeMatcher54090.get()
                    tmp535 = subjects534
                    subjects534 = []
                    for s in tmp535:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp535, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 54091
                            if len(subjects161) == 0:
                                pass
                                # State 54092
                                if len(subjects) == 0:
                                    pass
                                    # 15: log(c + x*d)
                    subjects161.appendleft(tmp533)
            if len(subjects161) >= 1 and isinstance(subjects161[0], Mul):
                tmp536 = subjects161.popleft()
                associative1 = tmp536
                associative_type1 = type(tmp536)
                subjects537 = deque(tmp536._args)
                matcher = CommutativeMatcher23956.get()
                tmp538 = subjects537
                subjects537 = []
                for s in tmp538:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp538, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 23971
                        if len(subjects161) == 0:
                            pass
                            # State 23972
                            if len(subjects) == 0:
                                pass
                                # 3: log(c*(e + f*x))
                    if pattern_index == 1:
                        pass
                        # State 24755
                        if len(subjects161) == 0:
                            pass
                            # State 24756
                            if len(subjects) == 0:
                                pass
                                # 4: log(c*(d*(e + f*x)**p)**q)
                    if pattern_index == 2:
                        pass
                        # State 26461
                        if len(subjects161) == 0:
                            pass
                            # State 26462
                            if len(subjects) == 0:
                                pass
                                # 5: log(c/(e + f*x))
                    if pattern_index == 3:
                        pass
                        # State 26873
                        if len(subjects161) == 0:
                            pass
                            # State 26874
                            if len(subjects) == 0:
                                pass
                                # 6: log(c*(d*(e + f*x)**p)**q)
                    if pattern_index == 4:
                        pass
                        # State 27343
                        if len(subjects161) == 0:
                            pass
                            # State 27344
                            if len(subjects) == 0:
                                pass
                                # 7: log(c*(d*(e + f*x)**p)**q)
                    if pattern_index == 5:
                        pass
                        # State 27940
                        if len(subjects161) == 0:
                            pass
                            # State 27941
                            if len(subjects) == 0:
                                pass
                                # 8: log(c*(d*(e + f*x)**p)**q)
                    if pattern_index == 6:
                        pass
                        # State 40419
                        if len(subjects161) == 0:
                            pass
                            # State 40420
                            if len(subjects) == 0:
                                pass
                                # 9: log(c*x**n)
                    if pattern_index == 7:
                        pass
                        # State 49527
                        if len(subjects161) == 0:
                            pass
                            # State 49528
                            if len(subjects) == 0:
                                pass
                                # 10: log(c*(d + e*x**n)**p)
                    if pattern_index == 8:
                        pass
                        # State 49788
                        if len(subjects161) == 0:
                            pass
                            # State 49789
                            if len(subjects) == 0:
                                pass
                                # 11: log(c*v**p)
                    if pattern_index == 9:
                        pass
                        # State 50020
                        if len(subjects161) == 0:
                            pass
                            # State 50021
                            if len(subjects) == 0:
                                pass
                                # 12: log(c*(d + e*x**n)**p)
                    if pattern_index == 10:
                        pass
                        # State 50346
                        if len(subjects161) == 0:
                            pass
                            # State 50347
                            if len(subjects) == 0:
                                pass
                                # 13: log(c*(d + e*x**2)**p)
                subjects161.appendleft(tmp536)
            if len(subjects161) >= 1 and isinstance(subjects161[0], Add):
                tmp539 = subjects161.popleft()
                associative1 = tmp539
                associative_type1 = type(tmp539)
                subjects540 = deque(tmp539._args)
                matcher = CommutativeMatcher54094.get()
                tmp541 = subjects540
                subjects540 = []
                for s in tmp541:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp541, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 54100
                        if len(subjects161) == 0:
                            pass
                            # State 54101
                            if len(subjects) == 0:
                                pass
                                # 15: log(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 114243
                        if len(subjects161) == 0:
                            pass
                            # State 114244
                            if len(subjects) == 0:
                                pass
                                # 56: log(f + g*x**2)
                subjects161.appendleft(tmp539)
            subjects.appendleft(tmp160)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp542 = subjects.popleft()
            subjects543 = deque(tmp542._args)
            # State 59991
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 59992
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59993
                    if len(subjects543) >= 1:
                        tmp546 = subjects543.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp546)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 59994
                            if len(subjects543) == 0:
                                pass
                                # State 59995
                                if len(subjects) == 0:
                                    pass
                                    # 16: sin(c + x*d)
                        subjects543.appendleft(tmp546)
                if len(subjects543) >= 1 and isinstance(subjects543[0], Mul):
                    tmp548 = subjects543.popleft()
                    associative1 = tmp548
                    associative_type1 = type(tmp548)
                    subjects549 = deque(tmp548._args)
                    matcher = CommutativeMatcher59997.get()
                    tmp550 = subjects549
                    subjects549 = []
                    for s in tmp550:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp550, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 59998
                            if len(subjects543) == 0:
                                pass
                                # State 59999
                                if len(subjects) == 0:
                                    pass
                                    # 16: sin(c + x*d)
                    subjects543.appendleft(tmp548)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 62478
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 62479
                    if len(subjects543) >= 1:
                        tmp553 = subjects543.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp553)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 62480
                            if len(subjects543) == 0:
                                pass
                                # State 62481
                                if len(subjects) == 0:
                                    pass
                                    # 18: sin(e + x*f)
                        subjects543.appendleft(tmp553)
                if len(subjects543) >= 1 and isinstance(subjects543[0], Mul):
                    tmp555 = subjects543.popleft()
                    associative1 = tmp555
                    associative_type1 = type(tmp555)
                    subjects556 = deque(tmp555._args)
                    matcher = CommutativeMatcher62483.get()
                    tmp557 = subjects556
                    subjects556 = []
                    for s in tmp557:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp557, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 62484
                            if len(subjects543) == 0:
                                pass
                                # State 62485
                                if len(subjects) == 0:
                                    pass
                                    # 18: sin(e + x*f)
                    subjects543.appendleft(tmp555)
            if len(subjects543) >= 1 and isinstance(subjects543[0], Add):
                tmp558 = subjects543.popleft()
                associative1 = tmp558
                associative_type1 = type(tmp558)
                subjects559 = deque(tmp558._args)
                matcher = CommutativeMatcher60001.get()
                tmp560 = subjects559
                subjects559 = []
                for s in tmp560:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp560, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 60007
                        if len(subjects543) == 0:
                            pass
                            # State 60008
                            if len(subjects) == 0:
                                pass
                                # 16: sin(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 62489
                        if len(subjects543) == 0:
                            pass
                            # State 62490
                            if len(subjects) == 0:
                                pass
                                # 18: sin(e + x*f)
                subjects543.appendleft(tmp558)
            subjects.appendleft(tmp542)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp561 = subjects.popleft()
            subjects562 = deque(tmp561._args)
            # State 60107
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 60108
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 60109
                    if len(subjects562) >= 1:
                        tmp565 = subjects562.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp565)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 60110
                            if len(subjects562) == 0:
                                pass
                                # State 60111
                                if len(subjects) == 0:
                                    pass
                                    # 17: cos(c + x*d)
                        subjects562.appendleft(tmp565)
                if len(subjects562) >= 1 and isinstance(subjects562[0], Mul):
                    tmp567 = subjects562.popleft()
                    associative1 = tmp567
                    associative_type1 = type(tmp567)
                    subjects568 = deque(tmp567._args)
                    matcher = CommutativeMatcher60113.get()
                    tmp569 = subjects568
                    subjects568 = []
                    for s in tmp569:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp569, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 60114
                            if len(subjects562) == 0:
                                pass
                                # State 60115
                                if len(subjects) == 0:
                                    pass
                                    # 17: cos(c + x*d)
                    subjects562.appendleft(tmp567)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 62509
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 62510
                    if len(subjects562) >= 1:
                        tmp572 = subjects562.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp572)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 62511
                            if len(subjects562) == 0:
                                pass
                                # State 62512
                                if len(subjects) == 0:
                                    pass
                                    # 19: cos(e + x*f)
                        subjects562.appendleft(tmp572)
                if len(subjects562) >= 1 and isinstance(subjects562[0], Mul):
                    tmp574 = subjects562.popleft()
                    associative1 = tmp574
                    associative_type1 = type(tmp574)
                    subjects575 = deque(tmp574._args)
                    matcher = CommutativeMatcher62514.get()
                    tmp576 = subjects575
                    subjects575 = []
                    for s in tmp576:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp576, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 62515
                            if len(subjects562) == 0:
                                pass
                                # State 62516
                                if len(subjects) == 0:
                                    pass
                                    # 19: cos(e + x*f)
                    subjects562.appendleft(tmp574)
            if len(subjects562) >= 1 and isinstance(subjects562[0], Add):
                tmp577 = subjects562.popleft()
                associative1 = tmp577
                associative_type1 = type(tmp577)
                subjects578 = deque(tmp577._args)
                matcher = CommutativeMatcher60117.get()
                tmp579 = subjects578
                subjects578 = []
                for s in tmp579:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp579, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 60123
                        if len(subjects562) == 0:
                            pass
                            # State 60124
                            if len(subjects) == 0:
                                pass
                                # 17: cos(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 62520
                        if len(subjects562) == 0:
                            pass
                            # State 62521
                            if len(subjects) == 0:
                                pass
                                # 19: cos(e + x*f)
                subjects562.appendleft(tmp577)
            subjects.appendleft(tmp561)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp580 = subjects.popleft()
            subjects581 = deque(tmp580._args)
            # State 79003
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 79004
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 79005
                    if len(subjects581) >= 1:
                        tmp584 = subjects581.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp584)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 79006
                            if len(subjects581) == 0:
                                pass
                                # State 79007
                                if len(subjects) == 0:
                                    pass
                                    # 26: tan(c + x*d)
                        subjects581.appendleft(tmp584)
                if len(subjects581) >= 1 and isinstance(subjects581[0], Mul):
                    tmp586 = subjects581.popleft()
                    associative1 = tmp586
                    associative_type1 = type(tmp586)
                    subjects587 = deque(tmp586._args)
                    matcher = CommutativeMatcher79009.get()
                    tmp588 = subjects587
                    subjects587 = []
                    for s in tmp588:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp588, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 79010
                            if len(subjects581) == 0:
                                pass
                                # State 79011
                                if len(subjects) == 0:
                                    pass
                                    # 26: tan(c + x*d)
                    subjects581.appendleft(tmp586)
            if len(subjects581) >= 1 and isinstance(subjects581[0], Add):
                tmp589 = subjects581.popleft()
                associative1 = tmp589
                associative_type1 = type(tmp589)
                subjects590 = deque(tmp589._args)
                matcher = CommutativeMatcher79013.get()
                tmp591 = subjects590
                subjects590 = []
                for s in tmp591:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp591, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 79019
                        if len(subjects581) == 0:
                            pass
                            # State 79020
                            if len(subjects) == 0:
                                pass
                                # 26: tan(c + x*d)
                subjects581.appendleft(tmp589)
            subjects.appendleft(tmp580)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp592 = subjects.popleft()
            subjects593 = deque(tmp592._args)
            # State 108743
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108744
                if len(subjects593) >= 1:
                    tmp595 = subjects593.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp595)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108745
                        if len(subjects593) == 0:
                            pass
                            # State 108746
                            if len(subjects) == 0:
                                pass
                                # 38: asin(c*x)
                    subjects593.appendleft(tmp595)
                if len(subjects593) >= 1:
                    tmp597 = subjects593.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp597)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109159
                        if len(subjects593) == 0:
                            pass
                            # State 109160
                            if len(subjects) == 0:
                                pass
                                # 40: asin(c*x)
                    subjects593.appendleft(tmp597)
                if len(subjects593) >= 1:
                    tmp599 = subjects593.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp599)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109565
                        if len(subjects593) == 0:
                            pass
                            # State 109566
                            if len(subjects) == 0:
                                pass
                                # 44: asin(c*x)
                    subjects593.appendleft(tmp599)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109508
                if len(subjects593) >= 1:
                    tmp602 = subjects593.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp602)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109509
                        if len(subjects593) == 0:
                            pass
                            # State 109510
                            if len(subjects) == 0:
                                pass
                                # 42: asin(x*c)
                    subjects593.appendleft(tmp602)
            if len(subjects593) >= 1:
                tmp604 = subjects593.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp604)
                except ValueError:
                    pass
                else:
                    pass
                    # State 112558
                    if len(subjects593) == 0:
                        pass
                        # State 112559
                        if len(subjects) == 0:
                            pass
                            # 46: asin(u)
                subjects593.appendleft(tmp604)
            if len(subjects593) >= 1 and isinstance(subjects593[0], Mul):
                tmp606 = subjects593.popleft()
                associative1 = tmp606
                associative_type1 = type(tmp606)
                subjects607 = deque(tmp606._args)
                matcher = CommutativeMatcher108748.get()
                tmp608 = subjects607
                subjects607 = []
                for s in tmp608:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp608, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108749
                        if len(subjects593) == 0:
                            pass
                            # State 108750
                            if len(subjects) == 0:
                                pass
                                # 38: asin(c*x)
                    if pattern_index == 1:
                        pass
                        # State 109161
                        if len(subjects593) == 0:
                            pass
                            # State 109162
                            if len(subjects) == 0:
                                pass
                                # 40: asin(c*x)
                    if pattern_index == 2:
                        pass
                        # State 109511
                        if len(subjects593) == 0:
                            pass
                            # State 109512
                            if len(subjects) == 0:
                                pass
                                # 42: asin(x*c)
                    if pattern_index == 3:
                        pass
                        # State 109567
                        if len(subjects593) == 0:
                            pass
                            # State 109568
                            if len(subjects) == 0:
                                pass
                                # 44: asin(c*x)
                subjects593.appendleft(tmp606)
            subjects.appendleft(tmp592)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp609 = subjects.popleft()
            subjects610 = deque(tmp609._args)
            # State 108781
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108782
                if len(subjects610) >= 1:
                    tmp612 = subjects610.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp612)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108783
                        if len(subjects610) == 0:
                            pass
                            # State 108784
                            if len(subjects) == 0:
                                pass
                                # 39: acos(c*x)
                    subjects610.appendleft(tmp612)
                if len(subjects610) >= 1:
                    tmp614 = subjects610.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp614)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109181
                        if len(subjects610) == 0:
                            pass
                            # State 109182
                            if len(subjects) == 0:
                                pass
                                # 41: acos(c*x)
                    subjects610.appendleft(tmp614)
                if len(subjects610) >= 1:
                    tmp616 = subjects610.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp616)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109587
                        if len(subjects610) == 0:
                            pass
                            # State 109588
                            if len(subjects) == 0:
                                pass
                                # 45: acos(c*x)
                    subjects610.appendleft(tmp616)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109534
                if len(subjects610) >= 1:
                    tmp619 = subjects610.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp619)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109535
                        if len(subjects610) == 0:
                            pass
                            # State 109536
                            if len(subjects) == 0:
                                pass
                                # 43: acos(x*c)
                    subjects610.appendleft(tmp619)
            if len(subjects610) >= 1:
                tmp621 = subjects610.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp621)
                except ValueError:
                    pass
                else:
                    pass
                    # State 112572
                    if len(subjects610) == 0:
                        pass
                        # State 112573
                        if len(subjects) == 0:
                            pass
                            # 47: acos(u)
                subjects610.appendleft(tmp621)
            if len(subjects610) >= 1 and isinstance(subjects610[0], Mul):
                tmp623 = subjects610.popleft()
                associative1 = tmp623
                associative_type1 = type(tmp623)
                subjects624 = deque(tmp623._args)
                matcher = CommutativeMatcher108786.get()
                tmp625 = subjects624
                subjects624 = []
                for s in tmp625:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp625, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108787
                        if len(subjects610) == 0:
                            pass
                            # State 108788
                            if len(subjects) == 0:
                                pass
                                # 39: acos(c*x)
                    if pattern_index == 1:
                        pass
                        # State 109183
                        if len(subjects610) == 0:
                            pass
                            # State 109184
                            if len(subjects) == 0:
                                pass
                                # 41: acos(c*x)
                    if pattern_index == 2:
                        pass
                        # State 109537
                        if len(subjects610) == 0:
                            pass
                            # State 109538
                            if len(subjects) == 0:
                                pass
                                # 43: acos(x*c)
                    if pattern_index == 3:
                        pass
                        # State 109589
                        if len(subjects610) == 0:
                            pass
                            # State 109590
                            if len(subjects) == 0:
                                pass
                                # 45: acos(c*x)
                subjects610.appendleft(tmp623)
            subjects.appendleft(tmp609)
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp626 = subjects.popleft()
            subjects627 = deque(tmp626._args)
            # State 113051
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113052
                if len(subjects627) >= 1:
                    tmp629 = subjects627.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp629)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113053
                        if len(subjects627) == 0:
                            pass
                            # State 113054
                            if len(subjects) == 0:
                                pass
                                # 48: atan(c*x)
                    subjects627.appendleft(tmp629)
                if len(subjects627) >= 1:
                    tmp631 = subjects627.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp631)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113164
                        if len(subjects627) == 0:
                            pass
                            # State 113165
                            if len(subjects) == 0:
                                pass
                                # 50: atan(c*x)
                    subjects627.appendleft(tmp631)
                if len(subjects627) >= 1:
                    tmp633 = subjects627.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp633)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114062
                        if len(subjects627) == 0:
                            pass
                            # State 114063
                            if len(subjects) == 0:
                                pass
                                # 54: atan(c*x)
                    subjects627.appendleft(tmp633)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113885
                if len(subjects627) >= 1:
                    tmp636 = subjects627.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp636)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113886
                        if len(subjects627) == 0:
                            pass
                            # State 113887
                            if len(subjects) == 0:
                                pass
                                # 52: atan(x*c)
                    subjects627.appendleft(tmp636)
            if len(subjects627) >= 1:
                tmp638 = subjects627.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp638)
                except ValueError:
                    pass
                else:
                    pass
                    # State 119452
                    if len(subjects627) == 0:
                        pass
                        # State 119453
                        if len(subjects) == 0:
                            pass
                            # 57: atan(u)
                subjects627.appendleft(tmp638)
            if len(subjects627) >= 1 and isinstance(subjects627[0], Mul):
                tmp640 = subjects627.popleft()
                associative1 = tmp640
                associative_type1 = type(tmp640)
                subjects641 = deque(tmp640._args)
                matcher = CommutativeMatcher113056.get()
                tmp642 = subjects641
                subjects641 = []
                for s in tmp642:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp642, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 113057
                        if len(subjects627) == 0:
                            pass
                            # State 113058
                            if len(subjects) == 0:
                                pass
                                # 48: atan(c*x)
                    if pattern_index == 1:
                        pass
                        # State 113166
                        if len(subjects627) == 0:
                            pass
                            # State 113167
                            if len(subjects) == 0:
                                pass
                                # 50: atan(c*x)
                    if pattern_index == 2:
                        pass
                        # State 113888
                        if len(subjects627) == 0:
                            pass
                            # State 113889
                            if len(subjects) == 0:
                                pass
                                # 52: atan(x*c)
                    if pattern_index == 3:
                        pass
                        # State 114064
                        if len(subjects627) == 0:
                            pass
                            # State 114065
                            if len(subjects) == 0:
                                pass
                                # 54: atan(c*x)
                subjects627.appendleft(tmp640)
            subjects.appendleft(tmp626)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp643 = subjects.popleft()
            subjects644 = deque(tmp643._args)
            # State 113072
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113073
                if len(subjects644) >= 1:
                    tmp646 = subjects644.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp646)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113074
                        if len(subjects644) == 0:
                            pass
                            # State 113075
                            if len(subjects) == 0:
                                pass
                                # 49: acot(c*x)
                    subjects644.appendleft(tmp646)
                if len(subjects644) >= 1:
                    tmp648 = subjects644.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp648)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113186
                        if len(subjects644) == 0:
                            pass
                            # State 113187
                            if len(subjects) == 0:
                                pass
                                # 51: acot(c*x)
                    subjects644.appendleft(tmp648)
                if len(subjects644) >= 1:
                    tmp650 = subjects644.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp650)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114183
                        if len(subjects644) == 0:
                            pass
                            # State 114184
                            if len(subjects) == 0:
                                pass
                                # 55: acot(c*x)
                    subjects644.appendleft(tmp650)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 114037
                if len(subjects644) >= 1:
                    tmp653 = subjects644.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp653)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114038
                        if len(subjects644) == 0:
                            pass
                            # State 114039
                            if len(subjects) == 0:
                                pass
                                # 53: acot(x*c)
                    subjects644.appendleft(tmp653)
            if len(subjects644) >= 1:
                tmp655 = subjects644.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp655)
                except ValueError:
                    pass
                else:
                    pass
                    # State 119466
                    if len(subjects644) == 0:
                        pass
                        # State 119467
                        if len(subjects) == 0:
                            pass
                            # 58: acot(u)
                subjects644.appendleft(tmp655)
            if len(subjects644) >= 1 and isinstance(subjects644[0], Mul):
                tmp657 = subjects644.popleft()
                associative1 = tmp657
                associative_type1 = type(tmp657)
                subjects658 = deque(tmp657._args)
                matcher = CommutativeMatcher113077.get()
                tmp659 = subjects658
                subjects658 = []
                for s in tmp659:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp659, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 113078
                        if len(subjects644) == 0:
                            pass
                            # State 113079
                            if len(subjects) == 0:
                                pass
                                # 49: acot(c*x)
                    if pattern_index == 1:
                        pass
                        # State 113188
                        if len(subjects644) == 0:
                            pass
                            # State 113189
                            if len(subjects) == 0:
                                pass
                                # 51: acot(c*x)
                    if pattern_index == 2:
                        pass
                        # State 114040
                        if len(subjects644) == 0:
                            pass
                            # State 114041
                            if len(subjects) == 0:
                                pass
                                # 53: acot(x*c)
                    if pattern_index == 3:
                        pass
                        # State 114185
                        if len(subjects644) == 0:
                            pass
                            # State 114186
                            if len(subjects) == 0:
                                pass
                                # 55: acot(c*x)
                subjects644.appendleft(tmp657)
            subjects.appendleft(tmp643)
        if len(subjects) >= 1 and isinstance(subjects[0], asec):
            tmp660 = subjects.popleft()
            subjects661 = deque(tmp660._args)
            # State 119637
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119638
                if len(subjects661) >= 1:
                    tmp663 = subjects661.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp663)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119639
                        if len(subjects661) == 0:
                            pass
                            # State 119640
                            if len(subjects) == 0:
                                pass
                                # 59: asec(c*x)
                    subjects661.appendleft(tmp663)
                if len(subjects661) >= 1:
                    tmp665 = subjects661.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp665)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119899
                        if len(subjects661) == 0:
                            pass
                            # State 119900
                            if len(subjects) == 0:
                                pass
                                # 61: asec(c*x)
                    subjects661.appendleft(tmp665)
            if len(subjects661) >= 1:
                tmp667 = subjects661.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp667)
                except ValueError:
                    pass
                else:
                    pass
                    # State 121557
                    if len(subjects661) == 0:
                        pass
                        # State 121558
                        if len(subjects) == 0:
                            pass
                            # 63: asec(u)
                subjects661.appendleft(tmp667)
            if len(subjects661) >= 1 and isinstance(subjects661[0], Mul):
                tmp669 = subjects661.popleft()
                associative1 = tmp669
                associative_type1 = type(tmp669)
                subjects670 = deque(tmp669._args)
                matcher = CommutativeMatcher119642.get()
                tmp671 = subjects670
                subjects670 = []
                for s in tmp671:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp671, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119643
                        if len(subjects661) == 0:
                            pass
                            # State 119644
                            if len(subjects) == 0:
                                pass
                                # 59: asec(c*x)
                    if pattern_index == 1:
                        pass
                        # State 119901
                        if len(subjects661) == 0:
                            pass
                            # State 119902
                            if len(subjects) == 0:
                                pass
                                # 61: asec(c*x)
                subjects661.appendleft(tmp669)
            subjects.appendleft(tmp660)
        if len(subjects) >= 1 and isinstance(subjects[0], acsc):
            tmp672 = subjects.popleft()
            subjects673 = deque(tmp672._args)
            # State 119675
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119676
                if len(subjects673) >= 1:
                    tmp675 = subjects673.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp675)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119677
                        if len(subjects673) == 0:
                            pass
                            # State 119678
                            if len(subjects) == 0:
                                pass
                                # 60: acsc(c*x)
                    subjects673.appendleft(tmp675)
                if len(subjects673) >= 1:
                    tmp677 = subjects673.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp677)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119921
                        if len(subjects673) == 0:
                            pass
                            # State 119922
                            if len(subjects) == 0:
                                pass
                                # 62: acsc(c*x)
                    subjects673.appendleft(tmp677)
            if len(subjects673) >= 1:
                tmp679 = subjects673.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp679)
                except ValueError:
                    pass
                else:
                    pass
                    # State 121571
                    if len(subjects673) == 0:
                        pass
                        # State 121572
                        if len(subjects) == 0:
                            pass
                            # 64: acsc(u)
                subjects673.appendleft(tmp679)
            if len(subjects673) >= 1 and isinstance(subjects673[0], Mul):
                tmp681 = subjects673.popleft()
                associative1 = tmp681
                associative_type1 = type(tmp681)
                subjects682 = deque(tmp681._args)
                matcher = CommutativeMatcher119680.get()
                tmp683 = subjects682
                subjects682 = []
                for s in tmp683:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp683, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119681
                        if len(subjects673) == 0:
                            pass
                            # State 119682
                            if len(subjects) == 0:
                                pass
                                # 60: acsc(c*x)
                    if pattern_index == 1:
                        pass
                        # State 119923
                        if len(subjects673) == 0:
                            pass
                            # State 119924
                            if len(subjects) == 0:
                                pass
                                # 62: acsc(c*x)
                subjects673.appendleft(tmp681)
            subjects.appendleft(tmp672)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp684 = subjects.popleft()
            subjects685 = deque(tmp684._args)
            # State 138409
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138410
                if len(subjects685) >= 1:
                    tmp687 = subjects685.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp687)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138411
                        if len(subjects685) == 0:
                            pass
                            # State 138412
                            if len(subjects) == 0:
                                pass
                                # 65: asinh(c*x)
                    subjects685.appendleft(tmp687)
                if len(subjects685) >= 1:
                    tmp689 = subjects685.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp689)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138930
                        if len(subjects685) == 0:
                            pass
                            # State 138931
                            if len(subjects) == 0:
                                pass
                                # 67: asinh(c*x)
                    subjects685.appendleft(tmp689)
                if len(subjects685) >= 1:
                    tmp691 = subjects685.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp691)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139387
                        if len(subjects685) == 0:
                            pass
                            # State 139388
                            if len(subjects) == 0:
                                pass
                                # 72: asinh(c*x)
                    subjects685.appendleft(tmp691)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139330
                if len(subjects685) >= 1:
                    tmp694 = subjects685.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp694)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139331
                        if len(subjects685) == 0:
                            pass
                            # State 139332
                            if len(subjects) == 0:
                                pass
                                # 70: asinh(x*c)
                    subjects685.appendleft(tmp694)
            if len(subjects685) >= 1:
                tmp696 = subjects685.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp696)
                except ValueError:
                    pass
                else:
                    pass
                    # State 142140
                    if len(subjects685) == 0:
                        pass
                        # State 142141
                        if len(subjects) == 0:
                            pass
                            # 73: asinh(u)
                subjects685.appendleft(tmp696)
            if len(subjects685) >= 1 and isinstance(subjects685[0], Mul):
                tmp698 = subjects685.popleft()
                associative1 = tmp698
                associative_type1 = type(tmp698)
                subjects699 = deque(tmp698._args)
                matcher = CommutativeMatcher138414.get()
                tmp700 = subjects699
                subjects699 = []
                for s in tmp700:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp700, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138415
                        if len(subjects685) == 0:
                            pass
                            # State 138416
                            if len(subjects) == 0:
                                pass
                                # 65: asinh(c*x)
                    if pattern_index == 1:
                        pass
                        # State 138932
                        if len(subjects685) == 0:
                            pass
                            # State 138933
                            if len(subjects) == 0:
                                pass
                                # 67: asinh(c*x)
                    if pattern_index == 2:
                        pass
                        # State 139333
                        if len(subjects685) == 0:
                            pass
                            # State 139334
                            if len(subjects) == 0:
                                pass
                                # 70: asinh(x*c)
                    if pattern_index == 3:
                        pass
                        # State 139389
                        if len(subjects685) == 0:
                            pass
                            # State 139390
                            if len(subjects) == 0:
                                pass
                                # 72: asinh(c*x)
                subjects685.appendleft(tmp698)
            subjects.appendleft(tmp684)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp701 = subjects.popleft()
            subjects702 = deque(tmp701._args)
            # State 138447
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138448
                if len(subjects702) >= 1:
                    tmp704 = subjects702.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp704)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138449
                        if len(subjects702) == 0:
                            pass
                            # State 138450
                            if len(subjects) == 0:
                                pass
                                # 66: acosh(c*x)
                    subjects702.appendleft(tmp704)
                if len(subjects702) >= 1:
                    tmp706 = subjects702.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp706)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138952
                        if len(subjects702) == 0:
                            pass
                            # State 138953
                            if len(subjects) == 0:
                                pass
                                # 68: acosh(c*x)
                    subjects702.appendleft(tmp706)
                if len(subjects702) >= 1:
                    tmp708 = subjects702.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp708)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138985
                        if len(subjects702) == 0:
                            pass
                            # State 138986
                            if len(subjects) == 0:
                                pass
                                # 69: acosh(c*x)
                    subjects702.appendleft(tmp708)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139356
                if len(subjects702) >= 1:
                    tmp711 = subjects702.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp711)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139357
                        if len(subjects702) == 0:
                            pass
                            # State 139358
                            if len(subjects) == 0:
                                pass
                                # 71: acosh(x*c)
                    subjects702.appendleft(tmp711)
            if len(subjects702) >= 1:
                tmp713 = subjects702.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp713)
                except ValueError:
                    pass
                else:
                    pass
                    # State 142154
                    if len(subjects702) == 0:
                        pass
                        # State 142155
                        if len(subjects) == 0:
                            pass
                            # 74: acosh(u)
                subjects702.appendleft(tmp713)
            if len(subjects702) >= 1 and isinstance(subjects702[0], Mul):
                tmp715 = subjects702.popleft()
                associative1 = tmp715
                associative_type1 = type(tmp715)
                subjects716 = deque(tmp715._args)
                matcher = CommutativeMatcher138452.get()
                tmp717 = subjects716
                subjects716 = []
                for s in tmp717:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp717, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138453
                        if len(subjects702) == 0:
                            pass
                            # State 138454
                            if len(subjects) == 0:
                                pass
                                # 66: acosh(c*x)
                    if pattern_index == 1:
                        pass
                        # State 138954
                        if len(subjects702) == 0:
                            pass
                            # State 138955
                            if len(subjects) == 0:
                                pass
                                # 68: acosh(c*x)
                    if pattern_index == 2:
                        pass
                        # State 138987
                        if len(subjects702) == 0:
                            pass
                            # State 138988
                            if len(subjects) == 0:
                                pass
                                # 69: acosh(c*x)
                    if pattern_index == 3:
                        pass
                        # State 139359
                        if len(subjects702) == 0:
                            pass
                            # State 139360
                            if len(subjects) == 0:
                                pass
                                # 71: acosh(x*c)
                subjects702.appendleft(tmp715)
            subjects.appendleft(tmp701)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp718 = subjects.popleft()
            subjects719 = deque(tmp718._args)
            # State 142681
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142682
                if len(subjects719) >= 1:
                    tmp721 = subjects719.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp721)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142683
                        if len(subjects719) == 0:
                            pass
                            # State 142684
                            if len(subjects) == 0:
                                pass
                                # 75: atanh(c*x)
                    subjects719.appendleft(tmp721)
                if len(subjects719) >= 1:
                    tmp723 = subjects719.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp723)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142789
                        if len(subjects719) == 0:
                            pass
                            # State 142790
                            if len(subjects) == 0:
                                pass
                                # 77: atanh(c*x)
                    subjects719.appendleft(tmp723)
                if len(subjects719) >= 1:
                    tmp725 = subjects719.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp725)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143554
                        if len(subjects719) == 0:
                            pass
                            # State 143555
                            if len(subjects) == 0:
                                pass
                                # 81: atanh(c*x)
                    subjects719.appendleft(tmp725)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 143503
                if len(subjects719) >= 1:
                    tmp728 = subjects719.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp728)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143504
                        if len(subjects719) == 0:
                            pass
                            # State 143505
                            if len(subjects) == 0:
                                pass
                                # 79: atanh(x*c)
                    subjects719.appendleft(tmp728)
            if len(subjects719) >= 1:
                tmp730 = subjects719.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp730)
                except ValueError:
                    pass
                else:
                    pass
                    # State 148647
                    if len(subjects719) == 0:
                        pass
                        # State 148648
                        if len(subjects) == 0:
                            pass
                            # 83: atanh(u)
                subjects719.appendleft(tmp730)
            if len(subjects719) >= 1 and isinstance(subjects719[0], Mul):
                tmp732 = subjects719.popleft()
                associative1 = tmp732
                associative_type1 = type(tmp732)
                subjects733 = deque(tmp732._args)
                matcher = CommutativeMatcher142686.get()
                tmp734 = subjects733
                subjects733 = []
                for s in tmp734:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp734, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142687
                        if len(subjects719) == 0:
                            pass
                            # State 142688
                            if len(subjects) == 0:
                                pass
                                # 75: atanh(c*x)
                    if pattern_index == 1:
                        pass
                        # State 142791
                        if len(subjects719) == 0:
                            pass
                            # State 142792
                            if len(subjects) == 0:
                                pass
                                # 77: atanh(c*x)
                    if pattern_index == 2:
                        pass
                        # State 143506
                        if len(subjects719) == 0:
                            pass
                            # State 143507
                            if len(subjects) == 0:
                                pass
                                # 79: atanh(x*c)
                    if pattern_index == 3:
                        pass
                        # State 143556
                        if len(subjects719) == 0:
                            pass
                            # State 143557
                            if len(subjects) == 0:
                                pass
                                # 81: atanh(c*x)
                subjects719.appendleft(tmp732)
            subjects.appendleft(tmp718)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp735 = subjects.popleft()
            subjects736 = deque(tmp735._args)
            # State 142702
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142703
                if len(subjects736) >= 1:
                    tmp738 = subjects736.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp738)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142704
                        if len(subjects736) == 0:
                            pass
                            # State 142705
                            if len(subjects) == 0:
                                pass
                                # 76: acoth(c*x)
                    subjects736.appendleft(tmp738)
                if len(subjects736) >= 1:
                    tmp740 = subjects736.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp740)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142811
                        if len(subjects736) == 0:
                            pass
                            # State 142812
                            if len(subjects) == 0:
                                pass
                                # 78: acoth(c*x)
                    subjects736.appendleft(tmp740)
                if len(subjects736) >= 1:
                    tmp742 = subjects736.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp742)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143576
                        if len(subjects736) == 0:
                            pass
                            # State 143577
                            if len(subjects) == 0:
                                pass
                                # 82: acoth(c*x)
                    subjects736.appendleft(tmp742)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 143529
                if len(subjects736) >= 1:
                    tmp745 = subjects736.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp745)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143530
                        if len(subjects736) == 0:
                            pass
                            # State 143531
                            if len(subjects) == 0:
                                pass
                                # 80: acoth(x*c)
                    subjects736.appendleft(tmp745)
            if len(subjects736) >= 1:
                tmp747 = subjects736.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp747)
                except ValueError:
                    pass
                else:
                    pass
                    # State 148661
                    if len(subjects736) == 0:
                        pass
                        # State 148662
                        if len(subjects) == 0:
                            pass
                            # 84: acoth(u)
                subjects736.appendleft(tmp747)
            if len(subjects736) >= 1 and isinstance(subjects736[0], Mul):
                tmp749 = subjects736.popleft()
                associative1 = tmp749
                associative_type1 = type(tmp749)
                subjects750 = deque(tmp749._args)
                matcher = CommutativeMatcher142707.get()
                tmp751 = subjects750
                subjects750 = []
                for s in tmp751:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp751, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142708
                        if len(subjects736) == 0:
                            pass
                            # State 142709
                            if len(subjects) == 0:
                                pass
                                # 76: acoth(c*x)
                    if pattern_index == 1:
                        pass
                        # State 142813
                        if len(subjects736) == 0:
                            pass
                            # State 142814
                            if len(subjects) == 0:
                                pass
                                # 78: acoth(c*x)
                    if pattern_index == 2:
                        pass
                        # State 143532
                        if len(subjects736) == 0:
                            pass
                            # State 143533
                            if len(subjects) == 0:
                                pass
                                # 80: acoth(x*c)
                    if pattern_index == 3:
                        pass
                        # State 143578
                        if len(subjects736) == 0:
                            pass
                            # State 143579
                            if len(subjects) == 0:
                                pass
                                # 82: acoth(c*x)
                subjects736.appendleft(tmp749)
            subjects.appendleft(tmp735)
        if len(subjects) >= 1 and isinstance(subjects[0], asech):
            tmp752 = subjects.popleft()
            subjects753 = deque(tmp752._args)
            # State 148813
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 148814
                if len(subjects753) >= 1:
                    tmp755 = subjects753.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp755)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148815
                        if len(subjects753) == 0:
                            pass
                            # State 148816
                            if len(subjects) == 0:
                                pass
                                # 85: asech(c*x)
                    subjects753.appendleft(tmp755)
                if len(subjects753) >= 1:
                    tmp757 = subjects753.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp757)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 149075
                        if len(subjects753) == 0:
                            pass
                            # State 149076
                            if len(subjects) == 0:
                                pass
                                # 87: asech(c*x)
                    subjects753.appendleft(tmp757)
            if len(subjects753) >= 1:
                tmp759 = subjects753.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp759)
                except ValueError:
                    pass
                else:
                    pass
                    # State 150497
                    if len(subjects753) == 0:
                        pass
                        # State 150498
                        if len(subjects) == 0:
                            pass
                            # 89: asech(u)
                subjects753.appendleft(tmp759)
            if len(subjects753) >= 1 and isinstance(subjects753[0], Mul):
                tmp761 = subjects753.popleft()
                associative1 = tmp761
                associative_type1 = type(tmp761)
                subjects762 = deque(tmp761._args)
                matcher = CommutativeMatcher148818.get()
                tmp763 = subjects762
                subjects762 = []
                for s in tmp763:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp763, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 148819
                        if len(subjects753) == 0:
                            pass
                            # State 148820
                            if len(subjects) == 0:
                                pass
                                # 85: asech(c*x)
                    if pattern_index == 1:
                        pass
                        # State 149077
                        if len(subjects753) == 0:
                            pass
                            # State 149078
                            if len(subjects) == 0:
                                pass
                                # 87: asech(c*x)
                subjects753.appendleft(tmp761)
            subjects.appendleft(tmp752)
        if len(subjects) >= 1 and isinstance(subjects[0], acsch):
            tmp764 = subjects.popleft()
            subjects765 = deque(tmp764._args)
            # State 148851
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 148852
                if len(subjects765) >= 1:
                    tmp767 = subjects765.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp767)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148853
                        if len(subjects765) == 0:
                            pass
                            # State 148854
                            if len(subjects) == 0:
                                pass
                                # 86: acsch(c*x)
                    subjects765.appendleft(tmp767)
                if len(subjects765) >= 1:
                    tmp769 = subjects765.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp769)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 149097
                        if len(subjects765) == 0:
                            pass
                            # State 149098
                            if len(subjects) == 0:
                                pass
                                # 88: acsch(c*x)
                    subjects765.appendleft(tmp769)
            if len(subjects765) >= 1:
                tmp771 = subjects765.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.1', tmp771)
                except ValueError:
                    pass
                else:
                    pass
                    # State 150511
                    if len(subjects765) == 0:
                        pass
                        # State 150512
                        if len(subjects) == 0:
                            pass
                            # 90: acsch(u)
                subjects765.appendleft(tmp771)
            if len(subjects765) >= 1 and isinstance(subjects765[0], Mul):
                tmp773 = subjects765.popleft()
                associative1 = tmp773
                associative_type1 = type(tmp773)
                subjects774 = deque(tmp773._args)
                matcher = CommutativeMatcher148856.get()
                tmp775 = subjects774
                subjects774 = []
                for s in tmp775:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp775, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 148857
                        if len(subjects765) == 0:
                            pass
                            # State 148858
                            if len(subjects) == 0:
                                pass
                                # 86: acsch(c*x)
                    if pattern_index == 1:
                        pass
                        # State 149099
                        if len(subjects765) == 0:
                            pass
                            # State 149100
                            if len(subjects) == 0:
                                pass
                                # 88: acsch(c*x)
                subjects765.appendleft(tmp773)
            subjects.appendleft(tmp764)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
