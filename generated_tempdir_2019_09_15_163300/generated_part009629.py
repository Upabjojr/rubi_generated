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


class CommutativeMatcher2919(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i3.1.1', 1, 1, None), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({3: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({4: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({5: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({6: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({7: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({3: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({8: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({9: 1}), [
      (VariableWithCount('i3.1.0_2', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({10: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({11: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({12: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({13: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({8: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({2: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({}), [
      (VariableWithCount('i3.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i3.1.1', 1, 1, None), Mul)
]),
    20: (20, Multiset({3: 1}), [
      (VariableWithCount('i3.1.0_2', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({}), [
      (VariableWithCount('i3.1.0_3', 1, 1, S(1)), Mul),
      (VariableWithCount('i3.1.1', 1, 1, None), Mul)
]),
    22: (22, Multiset({14: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({15: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({16: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({17: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({18: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    27: (27, Multiset({19: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({20: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({21: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({22: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    31: (31, Multiset({23: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({24: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    33: (33, Multiset({25: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({25: 1, 24: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({24: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    36: (36, Multiset({26: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    37: (37, Multiset({27: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    38: (38, Multiset({28: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({29: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({30: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    41: (41, Multiset({31: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    42: (42, Multiset({32: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    43: (43, Multiset({33: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    44: (44, Multiset({34: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    45: (45, Multiset({35: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    46: (46, Multiset({36: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    47: (47, Multiset({37: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    48: (48, Multiset({38: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    49: (49, Multiset({39: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    50: (50, Multiset({40: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    51: (51, Multiset({41: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    52: (52, Multiset({42: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    53: (53, Multiset({29: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    54: (54, Multiset({43: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    55: (55, Multiset({44: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    56: (56, Multiset({45: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    57: (57, Multiset({46: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    58: (58, Multiset({47: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    59: (59, Multiset({48: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    60: (60, Multiset({49: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    61: (61, Multiset({50: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    62: (62, Multiset({51: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    63: (63, Multiset({52: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    64: (64, Multiset({53: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    65: (65, Multiset({54: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    66: (66, Multiset({55: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    67: (67, Multiset({56: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    68: (68, Multiset({57: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    69: (69, Multiset({58: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    70: (70, Multiset({59: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    71: (71, Multiset({60: 1}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    72: (72, Multiset({61: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    73: (73, Multiset({62: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    74: (74, Multiset({63: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    75: (75, Multiset({64: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    76: (76, Multiset({65: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    77: (77, Multiset({66: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    78: (78, Multiset({67: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    79: (79, Multiset({68: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    80: (80, Multiset({69: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    81: (81, Multiset({70: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    82: (82, Multiset({71: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    83: (83, Multiset({72: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    84: (84, Multiset({73: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    85: (85, Multiset({74: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    86: (86, Multiset({75: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    87: (87, Multiset({76: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    88: (88, Multiset({77: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    89: (89, Multiset({78: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    90: (90, Multiset({79: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    91: (91, Multiset({80: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    92: (92, Multiset({81: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    93: (93, Multiset({82: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    94: (94, Multiset({83: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    95: (95, Multiset({84: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    96: (96, Multiset({85: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    97: (97, Multiset({86: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    98: (98, Multiset({87: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    99: (99, Multiset({88: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    100: (100, Multiset({89: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    101: (101, Multiset({90: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    102: (102, Multiset({91: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    103: (103, Multiset({92: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    104: (104, Multiset({93: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    105: (105, Multiset({94: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    106: (106, Multiset({95: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    107: (107, Multiset({96: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    108: (108, Multiset({97: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    109: (109, Multiset({98: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    110: (110, Multiset({99: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    111: (111, Multiset({100: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    112: (112, Multiset({101: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    113: (113, Multiset({102: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    114: (114, Multiset({103: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    115: (115, Multiset({104: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    116: (116, Multiset({105: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 1
    anonymous_patterns = {22, 23}

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher2919._instance is None:
            CommutativeMatcher2919._instance = CommutativeMatcher2919()
        return CommutativeMatcher2919._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2918
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 3894
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 3895
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp5 = subjects2.popleft()
                        # State 3896
                        if len(subjects2) == 0:
                            pass
                            # State 3897
                            if len(subjects) == 0:
                                pass
                                # 0: x**2
                                yield 0, subst1
                        subjects2.appendleft(tmp5)
                    if len(subjects2) >= 1:
                        tmp6 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp6)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 6080
                            if len(subjects2) == 0:
                                pass
                                # State 6081
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                                    yield 1, subst2
                        subjects2.appendleft(tmp6)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8178
                        if len(subjects2) == 0:
                            pass
                            # State 8179
                            if len(subjects) == 0:
                                pass
                                # 6: x**n2
                                yield 6, subst2
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2_1', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8178
                            if len(subjects2) == 0:
                                pass
                                # State 8179
                                if len(subjects) == 0:
                                    pass
                                    # 6: x**n2
                                    yield 6, subst2
                        subjects2.appendleft(tmp9)
                    if len(subjects2) >= 1:
                        tmp11 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2_1', tmp11)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8208
                            if len(subjects2) == 0:
                                pass
                                # State 8209
                                if len(subjects) == 0:
                                    pass
                                    # 7: x**n2
                                    yield 7, subst2
                        subjects2.appendleft(tmp11)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9757
                        if len(subjects2) == 0:
                            pass
                            # State 9758
                            if len(subjects) == 0:
                                pass
                                # 8: x**n
                                yield 8, subst2
                    if len(subjects2) >= 1:
                        tmp14 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp14)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9757
                            if len(subjects2) == 0:
                                pass
                                # State 9758
                                if len(subjects) == 0:
                                    pass
                                    # 8: x**n
                                    yield 8, subst2
                        subjects2.appendleft(tmp14)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2_2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9769
                        if len(subjects2) == 0:
                            pass
                            # State 9770
                            if len(subjects) == 0:
                                pass
                                # 9: x**r
                                yield 9, subst2
                    if len(subjects2) >= 1:
                        tmp17 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2_2', tmp17)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9769
                            if len(subjects2) == 0:
                                pass
                                # State 9770
                                if len(subjects) == 0:
                                    pass
                                    # 9: x**r
                                    yield 9, subst2
                        subjects2.appendleft(tmp17)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101193
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 101194
                            if len(subjects2) >= 1:
                                tmp21 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp21)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 101195
                                    if len(subjects2) == 0:
                                        pass
                                        # State 101196
                                        if len(subjects) == 0:
                                            pass
                                            # 65: F**(c + x*d)
                                            yield 65, subst4
                                subjects2.appendleft(tmp21)
                        if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                            tmp23 = subjects2.popleft()
                            associative1 = tmp23
                            associative_type1 = type(tmp23)
                            subjects24 = deque(tmp23._args)
                            matcher = CommutativeMatcher101198.get()
                            tmp25 = subjects24
                            subjects24 = []
                            for s in tmp25:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp25, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 101199
                                    if len(subjects2) == 0:
                                        pass
                                        # State 101200
                                        if len(subjects) == 0:
                                            pass
                                            # 65: F**(c + x*d)
                                            yield 65, subst3
                            subjects2.appendleft(tmp23)
                    if len(subjects2) >= 1 and subjects2[0] == Integer(3):
                        tmp26 = subjects2.popleft()
                        # State 6125
                        if len(subjects2) == 0:
                            pass
                            # State 6126
                            if len(subjects) == 0:
                                pass
                                # 2: x**3
                                yield 2, subst1
                        subjects2.appendleft(tmp26)
                    if len(subjects2) >= 1 and subjects2[0] == Integer(4):
                        tmp27 = subjects2.popleft()
                        # State 6185
                        if len(subjects2) == 0:
                            pass
                            # State 6186
                            if len(subjects) == 0:
                                pass
                                # 3: x**4
                                yield 3, subst1
                        subjects2.appendleft(tmp27)
                    if len(subjects2) >= 1 and subjects2[0] == Integer(6):
                        tmp28 = subjects2.popleft()
                        # State 6250
                        if len(subjects2) == 0:
                            pass
                            # State 6251
                            if len(subjects) == 0:
                                pass
                                # 4: x**6
                                yield 4, subst1
                        subjects2.appendleft(tmp28)
                    if len(subjects2) >= 1 and subjects2[0] == Integer(8):
                        tmp29 = subjects2.popleft()
                        # State 6260
                        if len(subjects2) == 0:
                            pass
                            # State 6261
                            if len(subjects) == 0:
                                pass
                                # 5: x**8
                                yield 5, subst1
                        subjects2.appendleft(tmp29)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                        tmp30 = subjects2.popleft()
                        associative1 = tmp30
                        associative_type1 = type(tmp30)
                        subjects31 = deque(tmp30._args)
                        matcher = CommutativeMatcher101202.get()
                        tmp32 = subjects31
                        subjects31 = []
                        for s in tmp32:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp32, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 101208
                                if len(subjects2) == 0:
                                    pass
                                    # State 101209
                                    if len(subjects) == 0:
                                        pass
                                        # 65: F**(c + x*d)
                                        yield 65, subst2
                        subjects2.appendleft(tmp30)
                subjects2.appendleft(tmp3)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10097
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp34 = subjects2.popleft()
                    subjects35 = deque(tmp34._args)
                    # State 10098
                    if len(subjects35) >= 1:
                        tmp36 = subjects35.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.1', tmp36)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10099
                            if len(subjects35) >= 1:
                                tmp38 = subjects35.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', tmp38)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10100
                                    if len(subjects35) == 0:
                                        pass
                                        # State 10101
                                        if len(subjects2) >= 1:
                                            tmp40 = subjects2.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2', tmp40)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 10102
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 10103
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 10: (c*x**n)**q
                                                        yield 10, subst4
                                            subjects2.appendleft(tmp40)
                                subjects35.appendleft(tmp38)
                            if len(subjects35) >= 1 and subjects35[0] == Integer(-1):
                                tmp42 = subjects35.popleft()
                                # State 10627
                                if len(subjects35) == 0:
                                    pass
                                    # State 10628
                                    if len(subjects2) >= 1:
                                        tmp43 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2', tmp43)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 10629
                                            if len(subjects2) == 0:
                                                pass
                                                # State 10630
                                                if len(subjects) == 0:
                                                    pass
                                                    # 11: (c/x)**n
                                                    yield 11, subst3
                                        subjects2.appendleft(tmp43)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.2_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 10975
                                        if len(subjects2) == 0:
                                            pass
                                            # State 10976
                                            if len(subjects) == 0:
                                                pass
                                                # 12: (c/x)**n2
                                                yield 12, subst3
                                    if len(subjects2) >= 1:
                                        tmp46 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2_1', tmp46)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 10975
                                            if len(subjects2) == 0:
                                                pass
                                                # State 10976
                                                if len(subjects) == 0:
                                                    pass
                                                    # 12: (c/x)**n2
                                                    yield 12, subst3
                                        subjects2.appendleft(tmp46)
                                subjects35.appendleft(tmp42)
                        subjects35.appendleft(tmp36)
                    if len(subjects35) >= 1 and isinstance(subjects35[0], tan):
                        tmp48 = subjects35.popleft()
                        subjects49 = deque(tmp48._args)
                        # State 82304
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.3.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 82305
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.3.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 82306
                                if len(subjects49) >= 1:
                                    tmp52 = subjects49.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.3.1.0', tmp52)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 82307
                                        if len(subjects49) == 0:
                                            pass
                                            # State 82308
                                            if len(subjects35) >= 1 and subjects35[0] == Integer(-1):
                                                tmp54 = subjects35.popleft()
                                                # State 82309
                                                if len(subjects35) == 0:
                                                    pass
                                                    # State 82310
                                                    if len(subjects2) >= 1:
                                                        tmp55 = subjects2.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.2', tmp55)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 82311
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 82312
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 46: (e/tan(c + x*d))**n
                                                                    yield 46, subst5
                                                        subjects2.appendleft(tmp55)
                                                subjects35.appendleft(tmp54)
                                    subjects49.appendleft(tmp52)
                            if len(subjects49) >= 1 and isinstance(subjects49[0], Mul):
                                tmp57 = subjects49.popleft()
                                associative1 = tmp57
                                associative_type1 = type(tmp57)
                                subjects58 = deque(tmp57._args)
                                matcher = CommutativeMatcher82314.get()
                                tmp59 = subjects58
                                subjects58 = []
                                for s in tmp59:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp59, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 82315
                                        if len(subjects49) == 0:
                                            pass
                                            # State 82316
                                            if len(subjects35) >= 1 and subjects35[0] == Integer(-1):
                                                tmp60 = subjects35.popleft()
                                                # State 82317
                                                if len(subjects35) == 0:
                                                    pass
                                                    # State 82318
                                                    if len(subjects2) >= 1:
                                                        tmp61 = subjects2.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i3.1.2', tmp61)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 82319
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 82320
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 46: (e/tan(c + x*d))**n
                                                                    yield 46, subst4
                                                        subjects2.appendleft(tmp61)
                                                subjects35.appendleft(tmp60)
                                subjects49.appendleft(tmp57)
                        if len(subjects49) >= 1 and isinstance(subjects49[0], Add):
                            tmp63 = subjects49.popleft()
                            associative1 = tmp63
                            associative_type1 = type(tmp63)
                            subjects64 = deque(tmp63._args)
                            matcher = CommutativeMatcher82322.get()
                            tmp65 = subjects64
                            subjects64 = []
                            for s in tmp65:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp65, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 82328
                                    if len(subjects49) == 0:
                                        pass
                                        # State 82329
                                        if len(subjects35) >= 1 and subjects35[0] == Integer(-1):
                                            tmp66 = subjects35.popleft()
                                            # State 82330
                                            if len(subjects35) == 0:
                                                pass
                                                # State 82331
                                                if len(subjects2) >= 1:
                                                    tmp67 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.2', tmp67)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 82332
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 82333
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 46: (e/tan(c + x*d))**n
                                                                yield 46, subst3
                                                    subjects2.appendleft(tmp67)
                                            subjects35.appendleft(tmp66)
                            subjects49.appendleft(tmp63)
                        subjects35.appendleft(tmp48)
                    subjects2.appendleft(tmp34)
                if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                    tmp69 = subjects2.popleft()
                    subjects70 = deque(tmp69._args)
                    # State 82196
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 82197
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 82198
                            if len(subjects70) >= 1:
                                tmp73 = subjects70.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.2.1.0', tmp73)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 82199
                                    if len(subjects70) == 0:
                                        pass
                                        # State 82200
                                        if len(subjects2) >= 1:
                                            tmp75 = subjects2.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.2', tmp75)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 82201
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 82202
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 45: (e*tan(c + x*d))**n
                                                        yield 45, subst5
                                            subjects2.appendleft(tmp75)
                                subjects70.appendleft(tmp73)
                        if len(subjects70) >= 1 and isinstance(subjects70[0], Mul):
                            tmp77 = subjects70.popleft()
                            associative1 = tmp77
                            associative_type1 = type(tmp77)
                            subjects78 = deque(tmp77._args)
                            matcher = CommutativeMatcher82204.get()
                            tmp79 = subjects78
                            subjects78 = []
                            for s in tmp79:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp79, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 82205
                                    if len(subjects70) == 0:
                                        pass
                                        # State 82206
                                        if len(subjects2) >= 1:
                                            tmp80 = subjects2.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2', tmp80)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 82207
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 82208
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 45: (e*tan(c + x*d))**n
                                                        yield 45, subst4
                                            subjects2.appendleft(tmp80)
                            subjects70.appendleft(tmp77)
                    if len(subjects70) >= 1 and isinstance(subjects70[0], Add):
                        tmp82 = subjects70.popleft()
                        associative1 = tmp82
                        associative_type1 = type(tmp82)
                        subjects83 = deque(tmp82._args)
                        matcher = CommutativeMatcher82210.get()
                        tmp84 = subjects83
                        subjects83 = []
                        for s in tmp84:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp84, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 82216
                                if len(subjects70) == 0:
                                    pass
                                    # State 82217
                                    if len(subjects2) >= 1:
                                        tmp85 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2', tmp85)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 82218
                                            if len(subjects2) == 0:
                                                pass
                                                # State 82219
                                                if len(subjects) == 0:
                                                    pass
                                                    # 45: (e*tan(c + x*d))**n
                                                    yield 45, subst3
                                        subjects2.appendleft(tmp85)
                        subjects70.appendleft(tmp82)
                    subjects2.appendleft(tmp69)
            if len(subjects2) >= 1:
                tmp87 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.2.1', tmp87)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11181
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 11182
                        if len(subjects2) == 0:
                            pass
                            # State 11183
                            if len(subjects) == 0:
                                pass
                                # 13: x**n2
                                yield 13, subst2
                    if len(subjects2) >= 1:
                        tmp90 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2_1', tmp90)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 11182
                            if len(subjects2) == 0:
                                pass
                                # State 11183
                                if len(subjects) == 0:
                                    pass
                                    # 13: x**n2
                                    yield 13, subst2
                        subjects2.appendleft(tmp90)
                subjects2.appendleft(tmp87)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp92 = subjects2.popleft()
                associative1 = tmp92
                associative_type1 = type(tmp92)
                subjects93 = deque(tmp92._args)
                matcher = CommutativeMatcher10105.get()
                tmp94 = subjects93
                subjects93 = []
                for s in tmp94:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp94, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10110
                        if len(subjects2) >= 1:
                            tmp95 = []
                            tmp95.append(subjects2.popleft())
                            while True:
                                if len(tmp95) > 1:
                                    tmp96 = create_operation_expression(associative1, tmp95)
                                elif len(tmp95) == 1:
                                    tmp96 = tmp95[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp96)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10111
                                    if len(subjects2) == 0:
                                        pass
                                        # State 10112
                                        if len(subjects) == 0:
                                            pass
                                            # 10: (c*x**n)**q
                                            yield 10, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp95.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp95))
                    if pattern_index == 1:
                        pass
                        # State 10633
                        if len(subjects2) >= 1:
                            tmp98 = []
                            tmp98.append(subjects2.popleft())
                            while True:
                                if len(tmp98) > 1:
                                    tmp99 = create_operation_expression(associative1, tmp98)
                                elif len(tmp98) == 1:
                                    tmp99 = tmp98[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp99)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10634
                                    if len(subjects2) == 0:
                                        pass
                                        # State 10635
                                        if len(subjects) == 0:
                                            pass
                                            # 11: (c/x)**n
                                            yield 11, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp98.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp98))
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10977
                            if len(subjects2) == 0:
                                pass
                                # State 10978
                                if len(subjects) == 0:
                                    pass
                                    # 12: (c/x)**n2
                                    yield 12, subst2
                        if len(subjects2) >= 1:
                            tmp102 = []
                            tmp102.append(subjects2.popleft())
                            while True:
                                if len(tmp102) > 1:
                                    tmp103 = create_operation_expression(associative1, tmp102)
                                elif len(tmp102) == 1:
                                    tmp103 = tmp102[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2_1', tmp103)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10977
                                    if len(subjects2) == 0:
                                        pass
                                        # State 10978
                                        if len(subjects) == 0:
                                            pass
                                            # 12: (c/x)**n2
                                            yield 12, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp102.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp102))
                    if pattern_index == 2:
                        pass
                        # State 82238
                        if len(subjects2) >= 1:
                            tmp105 = []
                            tmp105.append(subjects2.popleft())
                            while True:
                                if len(tmp105) > 1:
                                    tmp106 = create_operation_expression(associative1, tmp105)
                                elif len(tmp105) == 1:
                                    tmp106 = tmp105[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp106)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 82239
                                    if len(subjects2) == 0:
                                        pass
                                        # State 82240
                                        if len(subjects) == 0:
                                            pass
                                            # 45: (e*tan(c + x*d))**n
                                            yield 45, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp105.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp105))
                    if pattern_index == 3:
                        pass
                        # State 82358
                        if len(subjects2) >= 1:
                            tmp108 = []
                            tmp108.append(subjects2.popleft())
                            while True:
                                if len(tmp108) > 1:
                                    tmp109 = create_operation_expression(associative1, tmp108)
                                elif len(tmp108) == 1:
                                    tmp109 = tmp108[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp109)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 82359
                                    if len(subjects2) == 0:
                                        pass
                                        # State 82360
                                        if len(subjects) == 0:
                                            pass
                                            # 46: (e/tan(c + x*d))**n
                                            yield 46, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp108.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp108))
                subjects2.appendleft(tmp92)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp111 = subjects2.popleft()
                associative1 = tmp111
                associative_type1 = type(tmp111)
                subjects112 = deque(tmp111._args)
                matcher = CommutativeMatcher13509.get()
                tmp113 = subjects112
                subjects112 = []
                for s in tmp113:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp113, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 13559
                        if len(subjects2) >= 1:
                            tmp114 = []
                            tmp114.append(subjects2.popleft())
                            while True:
                                if len(tmp114) > 1:
                                    tmp115 = create_operation_expression(associative1, tmp114)
                                elif len(tmp114) == 1:
                                    tmp115 = tmp114[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp115)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 13560
                                    if len(subjects2) == 0:
                                        pass
                                        # State 13561
                                        if len(subjects) == 0:
                                            pass
                                            # 14: (d + e*x + f*sqrt(a + b*x + c*x**2))**n
                                            yield 14, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp114.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp114))
                    if pattern_index == 1:
                        pass
                        # State 13663
                        if len(subjects2) >= 1:
                            tmp117 = []
                            tmp117.append(subjects2.popleft())
                            while True:
                                if len(tmp117) > 1:
                                    tmp118 = create_operation_expression(associative1, tmp117)
                                elif len(tmp117) == 1:
                                    tmp118 = tmp117[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp118)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 13664
                                    if len(subjects2) == 0:
                                        pass
                                        # State 13665
                                        if len(subjects) == 0:
                                            pass
                                            # 15: (d + e*x + f*sqrt(a + c*x**2))**n
                                            yield 15, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp117.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp117))
                    if pattern_index == 2:
                        pass
                        # State 13767
                        if len(subjects2) >= 1:
                            tmp120 = []
                            tmp120.append(subjects2.popleft())
                            while True:
                                if len(tmp120) > 1:
                                    tmp121 = create_operation_expression(associative1, tmp120)
                                elif len(tmp120) == 1:
                                    tmp121 = tmp120[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp121)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 13768
                                    if len(subjects2) == 0:
                                        pass
                                        # State 13769
                                        if len(subjects) == 0:
                                            pass
                                            # 16: (u + f*sqrt(v))**n
                                            yield 16, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp120.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp120))
                    if pattern_index == 3:
                        pass
                        # State 14130
                        if len(subjects2) >= 1 and subjects2[0] == Rational(1, 2):
                            tmp123 = subjects2.popleft()
                            # State 14131
                            if len(subjects2) == 0:
                                pass
                                # State 14132
                                if len(subjects) == 0:
                                    pass
                                    # 17: sqrt(c + d*x**2)
                                    yield 17, subst1
                            subjects2.appendleft(tmp123)
                subjects2.appendleft(tmp111)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp124 = subjects2.popleft()
                subjects125 = deque(tmp124._args)
                # State 67113
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 67114
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 67115
                        if len(subjects125) >= 1:
                            tmp128 = subjects125.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.3.1.0', tmp128)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 67116
                                if len(subjects125) == 0:
                                    pass
                                    # State 67117
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp130 = subjects2.popleft()
                                        # State 67118
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67119
                                            if len(subjects) == 0:
                                                pass
                                                # 26: 1/cos(d + x*e)
                                                yield 26, subst3
                                        subjects2.appendleft(tmp130)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                        tmp131 = subjects2.popleft()
                                        # State 67777
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67778
                                            if len(subjects) == 0:
                                                pass
                                                # 31: cos(d + x*e)**2
                                                yield 31, subst3
                                        subjects2.appendleft(tmp131)
                                    if len(subjects2) >= 1:
                                        tmp132 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', tmp132)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 67843
                                            if len(subjects2) == 0:
                                                pass
                                                # State 67844
                                                if len(subjects) == 0:
                                                    pass
                                                    # 33: cos(d + x*e)**n
                                                    yield 33, subst4
                                        subjects2.appendleft(tmp132)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69214
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69215
                                            if len(subjects) == 0:
                                                pass
                                                # 36: cos(d + x*e)**n
                                                yield 36, subst4
                                    if len(subjects2) >= 1:
                                        tmp135 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', tmp135)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69214
                                            if len(subjects2) == 0:
                                                pass
                                                # State 69215
                                                if len(subjects) == 0:
                                                    pass
                                                    # 36: cos(d + x*e)**n
                                                    yield 36, subst4
                                        subjects2.appendleft(tmp135)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69281
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69282
                                            if len(subjects) == 0:
                                                pass
                                                # 37: cos(d + x*e)**n2
                                                yield 37, subst4
                                    if len(subjects2) >= 1:
                                        tmp138 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3_1', tmp138)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69281
                                            if len(subjects2) == 0:
                                                pass
                                                # State 69282
                                                if len(subjects) == 0:
                                                    pass
                                                    # 37: cos(d + x*e)**n2
                                                    yield 37, subst4
                                        subjects2.appendleft(tmp138)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                        tmp140 = subjects2.popleft()
                                        # State 94785
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94786
                                            if len(subjects) == 0:
                                                pass
                                                # 55: cos(d + x*e)**(-2)
                                                yield 55, subst3
                                        subjects2.appendleft(tmp140)
                            subjects125.appendleft(tmp128)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 97690
                        if len(subjects125) >= 1 and isinstance(subjects125[0], Pow):
                            tmp142 = subjects125.popleft()
                            subjects143 = deque(tmp142._args)
                            # State 97691
                            if len(subjects143) >= 1:
                                tmp144 = subjects143.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp144)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 97692
                                    if len(subjects143) >= 1:
                                        tmp146 = subjects143.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp146)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 97693
                                            if len(subjects143) == 0:
                                                pass
                                                # State 97694
                                                if len(subjects125) == 0:
                                                    pass
                                                    # State 97695
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp148 = subjects2.popleft()
                                                        # State 97696
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 97697
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 61: 1/cos(c + d*x**n)
                                                                yield 61, subst4
                                                        subjects2.appendleft(tmp148)
                                        subjects143.appendleft(tmp146)
                                subjects143.appendleft(tmp144)
                            subjects125.appendleft(tmp142)
                    if len(subjects125) >= 1 and isinstance(subjects125[0], Mul):
                        tmp149 = subjects125.popleft()
                        associative1 = tmp149
                        associative_type1 = type(tmp149)
                        subjects150 = deque(tmp149._args)
                        matcher = CommutativeMatcher67121.get()
                        tmp151 = subjects150
                        subjects150 = []
                        for s in tmp151:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp151, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 67122
                                if len(subjects125) == 0:
                                    pass
                                    # State 67123
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp152 = subjects2.popleft()
                                        # State 67124
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67125
                                            if len(subjects) == 0:
                                                pass
                                                # 26: 1/cos(d + x*e)
                                                yield 26, subst2
                                        subjects2.appendleft(tmp152)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                        tmp153 = subjects2.popleft()
                                        # State 67779
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67780
                                            if len(subjects) == 0:
                                                pass
                                                # 31: cos(d + x*e)**2
                                                yield 31, subst2
                                        subjects2.appendleft(tmp153)
                                    if len(subjects2) >= 1:
                                        tmp154 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp154)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 67845
                                            if len(subjects2) == 0:
                                                pass
                                                # State 67846
                                                if len(subjects) == 0:
                                                    pass
                                                    # 33: cos(d + x*e)**n
                                                    yield 33, subst3
                                        subjects2.appendleft(tmp154)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69216
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69217
                                            if len(subjects) == 0:
                                                pass
                                                # 36: cos(d + x*e)**n
                                                yield 36, subst3
                                    if len(subjects2) >= 1:
                                        tmp157 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp157)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69216
                                            if len(subjects2) == 0:
                                                pass
                                                # State 69217
                                                if len(subjects) == 0:
                                                    pass
                                                    # 36: cos(d + x*e)**n
                                                    yield 36, subst3
                                        subjects2.appendleft(tmp157)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69283
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69284
                                            if len(subjects) == 0:
                                                pass
                                                # 37: cos(d + x*e)**n2
                                                yield 37, subst3
                                    if len(subjects2) >= 1:
                                        tmp160 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3_1', tmp160)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69283
                                            if len(subjects2) == 0:
                                                pass
                                                # State 69284
                                                if len(subjects) == 0:
                                                    pass
                                                    # 37: cos(d + x*e)**n2
                                                    yield 37, subst3
                                        subjects2.appendleft(tmp160)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                        tmp162 = subjects2.popleft()
                                        # State 94787
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94788
                                            if len(subjects) == 0:
                                                pass
                                                # 55: cos(d + x*e)**(-2)
                                                yield 55, subst2
                                        subjects2.appendleft(tmp162)
                            if pattern_index == 1:
                                pass
                                # State 97702
                                if len(subjects125) == 0:
                                    pass
                                    # State 97703
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp163 = subjects2.popleft()
                                        # State 97704
                                        if len(subjects2) == 0:
                                            pass
                                            # State 97705
                                            if len(subjects) == 0:
                                                pass
                                                # 61: 1/cos(c + d*x**n)
                                                yield 61, subst2
                                        subjects2.appendleft(tmp163)
                        subjects125.appendleft(tmp149)
                if len(subjects125) >= 1:
                    tmp164 = subjects125.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp164)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98264
                        if len(subjects125) == 0:
                            pass
                            # State 98265
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp166 = subjects2.popleft()
                                # State 98266
                                if len(subjects2) == 0:
                                    pass
                                    # State 98267
                                    if len(subjects) == 0:
                                        pass
                                        # 63: 1/cos(u)
                                        yield 63, subst1
                                subjects2.appendleft(tmp166)
                    subjects125.appendleft(tmp164)
                if len(subjects125) >= 1 and isinstance(subjects125[0], Add):
                    tmp167 = subjects125.popleft()
                    associative1 = tmp167
                    associative_type1 = type(tmp167)
                    subjects168 = deque(tmp167._args)
                    matcher = CommutativeMatcher67127.get()
                    tmp169 = subjects168
                    subjects168 = []
                    for s in tmp169:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp169, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 67133
                            if len(subjects125) == 0:
                                pass
                                # State 67134
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp170 = subjects2.popleft()
                                    # State 67135
                                    if len(subjects2) == 0:
                                        pass
                                        # State 67136
                                        if len(subjects) == 0:
                                            pass
                                            # 26: 1/cos(d + x*e)
                                            yield 26, subst1
                                    subjects2.appendleft(tmp170)
                                if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                    tmp171 = subjects2.popleft()
                                    # State 67781
                                    if len(subjects2) == 0:
                                        pass
                                        # State 67782
                                        if len(subjects) == 0:
                                            pass
                                            # 31: cos(d + x*e)**2
                                            yield 31, subst1
                                    subjects2.appendleft(tmp171)
                                if len(subjects2) >= 1:
                                    tmp172 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3', tmp172)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 67847
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67848
                                            if len(subjects) == 0:
                                                pass
                                                # 33: cos(d + x*e)**n
                                                yield 33, subst2
                                    subjects2.appendleft(tmp172)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 69218
                                    if len(subjects2) == 0:
                                        pass
                                        # State 69219
                                        if len(subjects) == 0:
                                            pass
                                            # 36: cos(d + x*e)**n
                                            yield 36, subst2
                                if len(subjects2) >= 1:
                                    tmp175 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3', tmp175)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69218
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69219
                                            if len(subjects) == 0:
                                                pass
                                                # 36: cos(d + x*e)**n
                                                yield 36, subst2
                                    subjects2.appendleft(tmp175)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.3_1', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 69285
                                    if len(subjects2) == 0:
                                        pass
                                        # State 69286
                                        if len(subjects) == 0:
                                            pass
                                            # 37: cos(d + x*e)**n2
                                            yield 37, subst2
                                if len(subjects2) >= 1:
                                    tmp178 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3_1', tmp178)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69285
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69286
                                            if len(subjects) == 0:
                                                pass
                                                # 37: cos(d + x*e)**n2
                                                yield 37, subst2
                                    subjects2.appendleft(tmp178)
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                    tmp180 = subjects2.popleft()
                                    # State 94789
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94790
                                        if len(subjects) == 0:
                                            pass
                                            # 55: cos(d + x*e)**(-2)
                                            yield 55, subst1
                                    subjects2.appendleft(tmp180)
                        if pattern_index == 1:
                            pass
                            # State 97716
                            if len(subjects125) == 0:
                                pass
                                # State 97717
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp181 = subjects2.popleft()
                                    # State 97718
                                    if len(subjects2) == 0:
                                        pass
                                        # State 97719
                                        if len(subjects) == 0:
                                            pass
                                            # 61: 1/cos(c + d*x**n)
                                            yield 61, subst1
                                    subjects2.appendleft(tmp181)
                    subjects125.appendleft(tmp167)
                subjects2.appendleft(tmp124)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp182 = subjects2.popleft()
                subjects183 = deque(tmp182._args)
                # State 67204
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 67205
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 67206
                        if len(subjects183) >= 1:
                            tmp186 = subjects183.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.3.1.0', tmp186)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 67207
                                if len(subjects183) == 0:
                                    pass
                                    # State 67208
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp188 = subjects2.popleft()
                                        # State 67209
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67210
                                            if len(subjects) == 0:
                                                pass
                                                # 28: 1/sin(d + x*e)
                                                yield 28, subst3
                                        subjects2.appendleft(tmp188)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                        tmp189 = subjects2.popleft()
                                        # State 67759
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67760
                                            if len(subjects) == 0:
                                                pass
                                                # 30: sin(d + x*e)**2
                                                yield 30, subst3
                                        subjects2.appendleft(tmp189)
                                    if len(subjects2) >= 1:
                                        tmp190 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', tmp190)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 67825
                                            if len(subjects2) == 0:
                                                pass
                                                # State 67826
                                                if len(subjects) == 0:
                                                    pass
                                                    # 32: sin(d + x*e)**n
                                                    yield 32, subst4
                                        subjects2.appendleft(tmp190)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 68936
                                        if len(subjects2) == 0:
                                            pass
                                            # State 68937
                                            if len(subjects) == 0:
                                                pass
                                                # 34: sin(d + x*e)**n
                                                yield 34, subst4
                                    if len(subjects2) >= 1:
                                        tmp193 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', tmp193)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68936
                                            if len(subjects2) == 0:
                                                pass
                                                # State 68937
                                                if len(subjects) == 0:
                                                    pass
                                                    # 34: sin(d + x*e)**n
                                                    yield 34, subst4
                                        subjects2.appendleft(tmp193)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69005
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69006
                                            if len(subjects) == 0:
                                                pass
                                                # 35: sin(d + x*e)**n2
                                                yield 35, subst4
                                    if len(subjects2) >= 1:
                                        tmp196 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3_1', tmp196)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69005
                                            if len(subjects2) == 0:
                                                pass
                                                # State 69006
                                                if len(subjects) == 0:
                                                    pass
                                                    # 35: sin(d + x*e)**n2
                                                    yield 35, subst4
                                        subjects2.appendleft(tmp196)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                        tmp198 = subjects2.popleft()
                                        # State 94803
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94804
                                            if len(subjects) == 0:
                                                pass
                                                # 56: sin(d + x*e)**(-2)
                                                yield 56, subst3
                                        subjects2.appendleft(tmp198)
                            subjects183.appendleft(tmp186)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 97998
                        if len(subjects183) >= 1 and isinstance(subjects183[0], Pow):
                            tmp200 = subjects183.popleft()
                            subjects201 = deque(tmp200._args)
                            # State 97999
                            if len(subjects201) >= 1:
                                tmp202 = subjects201.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp202)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 98000
                                    if len(subjects201) >= 1:
                                        tmp204 = subjects201.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp204)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 98001
                                            if len(subjects201) == 0:
                                                pass
                                                # State 98002
                                                if len(subjects183) == 0:
                                                    pass
                                                    # State 98003
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp206 = subjects2.popleft()
                                                        # State 98004
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 98005
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 62: 1/sin(c + d*x**n)
                                                                yield 62, subst4
                                                        subjects2.appendleft(tmp206)
                                        subjects201.appendleft(tmp204)
                                subjects201.appendleft(tmp202)
                            subjects183.appendleft(tmp200)
                    if len(subjects183) >= 1 and isinstance(subjects183[0], Mul):
                        tmp207 = subjects183.popleft()
                        associative1 = tmp207
                        associative_type1 = type(tmp207)
                        subjects208 = deque(tmp207._args)
                        matcher = CommutativeMatcher67212.get()
                        tmp209 = subjects208
                        subjects208 = []
                        for s in tmp209:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp209, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 67213
                                if len(subjects183) == 0:
                                    pass
                                    # State 67214
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp210 = subjects2.popleft()
                                        # State 67215
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67216
                                            if len(subjects) == 0:
                                                pass
                                                # 28: 1/sin(d + x*e)
                                                yield 28, subst2
                                        subjects2.appendleft(tmp210)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                        tmp211 = subjects2.popleft()
                                        # State 67761
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67762
                                            if len(subjects) == 0:
                                                pass
                                                # 30: sin(d + x*e)**2
                                                yield 30, subst2
                                        subjects2.appendleft(tmp211)
                                    if len(subjects2) >= 1:
                                        tmp212 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp212)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 67827
                                            if len(subjects2) == 0:
                                                pass
                                                # State 67828
                                                if len(subjects) == 0:
                                                    pass
                                                    # 32: sin(d + x*e)**n
                                                    yield 32, subst3
                                        subjects2.appendleft(tmp212)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 68938
                                        if len(subjects2) == 0:
                                            pass
                                            # State 68939
                                            if len(subjects) == 0:
                                                pass
                                                # 34: sin(d + x*e)**n
                                                yield 34, subst3
                                    if len(subjects2) >= 1:
                                        tmp215 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp215)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 68938
                                            if len(subjects2) == 0:
                                                pass
                                                # State 68939
                                                if len(subjects) == 0:
                                                    pass
                                                    # 34: sin(d + x*e)**n
                                                    yield 34, subst3
                                        subjects2.appendleft(tmp215)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69007
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69008
                                            if len(subjects) == 0:
                                                pass
                                                # 35: sin(d + x*e)**n2
                                                yield 35, subst3
                                    if len(subjects2) >= 1:
                                        tmp218 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3_1', tmp218)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 69007
                                            if len(subjects2) == 0:
                                                pass
                                                # State 69008
                                                if len(subjects) == 0:
                                                    pass
                                                    # 35: sin(d + x*e)**n2
                                                    yield 35, subst3
                                        subjects2.appendleft(tmp218)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                        tmp220 = subjects2.popleft()
                                        # State 94805
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94806
                                            if len(subjects) == 0:
                                                pass
                                                # 56: sin(d + x*e)**(-2)
                                                yield 56, subst2
                                        subjects2.appendleft(tmp220)
                            if pattern_index == 1:
                                pass
                                # State 98010
                                if len(subjects183) == 0:
                                    pass
                                    # State 98011
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp221 = subjects2.popleft()
                                        # State 98012
                                        if len(subjects2) == 0:
                                            pass
                                            # State 98013
                                            if len(subjects) == 0:
                                                pass
                                                # 62: 1/sin(c + d*x**n)
                                                yield 62, subst2
                                        subjects2.appendleft(tmp221)
                        subjects183.appendleft(tmp207)
                if len(subjects183) >= 1:
                    tmp222 = subjects183.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp222)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98320
                        if len(subjects183) == 0:
                            pass
                            # State 98321
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp224 = subjects2.popleft()
                                # State 98322
                                if len(subjects2) == 0:
                                    pass
                                    # State 98323
                                    if len(subjects) == 0:
                                        pass
                                        # 64: 1/sin(u)
                                        yield 64, subst1
                                subjects2.appendleft(tmp224)
                    subjects183.appendleft(tmp222)
                if len(subjects183) >= 1 and isinstance(subjects183[0], Add):
                    tmp225 = subjects183.popleft()
                    associative1 = tmp225
                    associative_type1 = type(tmp225)
                    subjects226 = deque(tmp225._args)
                    matcher = CommutativeMatcher67218.get()
                    tmp227 = subjects226
                    subjects226 = []
                    for s in tmp227:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp227, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 67224
                            if len(subjects183) == 0:
                                pass
                                # State 67225
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp228 = subjects2.popleft()
                                    # State 67226
                                    if len(subjects2) == 0:
                                        pass
                                        # State 67227
                                        if len(subjects) == 0:
                                            pass
                                            # 28: 1/sin(d + x*e)
                                            yield 28, subst1
                                    subjects2.appendleft(tmp228)
                                if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                    tmp229 = subjects2.popleft()
                                    # State 67763
                                    if len(subjects2) == 0:
                                        pass
                                        # State 67764
                                        if len(subjects) == 0:
                                            pass
                                            # 30: sin(d + x*e)**2
                                            yield 30, subst1
                                    subjects2.appendleft(tmp229)
                                if len(subjects2) >= 1:
                                    tmp230 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3', tmp230)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 67829
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67830
                                            if len(subjects) == 0:
                                                pass
                                                # 32: sin(d + x*e)**n
                                                yield 32, subst2
                                    subjects2.appendleft(tmp230)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 68940
                                    if len(subjects2) == 0:
                                        pass
                                        # State 68941
                                        if len(subjects) == 0:
                                            pass
                                            # 34: sin(d + x*e)**n
                                            yield 34, subst2
                                if len(subjects2) >= 1:
                                    tmp233 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3', tmp233)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 68940
                                        if len(subjects2) == 0:
                                            pass
                                            # State 68941
                                            if len(subjects) == 0:
                                                pass
                                                # 34: sin(d + x*e)**n
                                                yield 34, subst2
                                    subjects2.appendleft(tmp233)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.3_1', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 69009
                                    if len(subjects2) == 0:
                                        pass
                                        # State 69010
                                        if len(subjects) == 0:
                                            pass
                                            # 35: sin(d + x*e)**n2
                                            yield 35, subst2
                                if len(subjects2) >= 1:
                                    tmp236 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3_1', tmp236)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 69009
                                        if len(subjects2) == 0:
                                            pass
                                            # State 69010
                                            if len(subjects) == 0:
                                                pass
                                                # 35: sin(d + x*e)**n2
                                                yield 35, subst2
                                    subjects2.appendleft(tmp236)
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                    tmp238 = subjects2.popleft()
                                    # State 94807
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94808
                                        if len(subjects) == 0:
                                            pass
                                            # 56: sin(d + x*e)**(-2)
                                            yield 56, subst1
                                    subjects2.appendleft(tmp238)
                        if pattern_index == 1:
                            pass
                            # State 98024
                            if len(subjects183) == 0:
                                pass
                                # State 98025
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp239 = subjects2.popleft()
                                    # State 98026
                                    if len(subjects2) == 0:
                                        pass
                                        # State 98027
                                        if len(subjects) == 0:
                                            pass
                                            # 62: 1/sin(c + d*x**n)
                                            yield 62, subst1
                                    subjects2.appendleft(tmp239)
                    subjects183.appendleft(tmp225)
                subjects2.appendleft(tmp182)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp240 = subjects2.popleft()
                subjects241 = deque(tmp240._args)
                # State 67253
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 67254
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 67255
                        if len(subjects241) >= 1:
                            tmp244 = subjects241.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.3.1.0', tmp244)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 67256
                                if len(subjects241) == 0:
                                    pass
                                    # State 67257
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp246 = subjects2.popleft()
                                        # State 67258
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67259
                                            if len(subjects) == 0:
                                                pass
                                                # 29: 1/tan(d + x*e)
                                                yield 29, subst3
                                        subjects2.appendleft(tmp246)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                        tmp247 = subjects2.popleft()
                                        # State 82111
                                        if len(subjects2) == 0:
                                            pass
                                            # State 82112
                                            if len(subjects) == 0:
                                                pass
                                                # 43: tan(d + x*e)**2
                                                yield 43, subst3
                                        subjects2.appendleft(tmp247)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                        tmp248 = subjects2.popleft()
                                        # State 82129
                                        if len(subjects2) == 0:
                                            pass
                                            # State 82130
                                            if len(subjects) == 0:
                                                pass
                                                # 44: tan(d + x*e)**(-2)
                                                yield 44, subst3
                                        subjects2.appendleft(tmp248)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83537
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83538
                                            if len(subjects) == 0:
                                                pass
                                                # 47: tan(d + x*e)**n
                                                yield 47, subst4
                                    if len(subjects2) >= 1:
                                        tmp250 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3', tmp250)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83537
                                            if len(subjects2) == 0:
                                                pass
                                                # State 83538
                                                if len(subjects) == 0:
                                                    pass
                                                    # 47: tan(d + x*e)**n
                                                    yield 47, subst4
                                        subjects2.appendleft(tmp250)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83586
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83587
                                            if len(subjects) == 0:
                                                pass
                                                # 48: tan(d + x*e)**n2
                                                yield 48, subst4
                                    if len(subjects2) >= 1:
                                        tmp253 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3_1', tmp253)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83586
                                            if len(subjects2) == 0:
                                                pass
                                                # State 83587
                                                if len(subjects) == 0:
                                                    pass
                                                    # 48: tan(d + x*e)**n2
                                                    yield 48, subst4
                                        subjects2.appendleft(tmp253)
                            subjects241.appendleft(tmp244)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 87635
                        if len(subjects241) >= 1 and isinstance(subjects241[0], Pow):
                            tmp256 = subjects241.popleft()
                            subjects257 = deque(tmp256._args)
                            # State 87636
                            if len(subjects257) >= 1:
                                tmp258 = subjects257.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp258)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 87637
                                    if len(subjects257) >= 1:
                                        tmp260 = subjects257.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp260)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 87638
                                            if len(subjects257) == 0:
                                                pass
                                                # State 87639
                                                if len(subjects241) == 0:
                                                    pass
                                                    # State 87640
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp262 = subjects2.popleft()
                                                        # State 87641
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 87642
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 52: 1/tan(c + d*x**n)
                                                                yield 52, subst4
                                                        subjects2.appendleft(tmp262)
                                        subjects257.appendleft(tmp260)
                                subjects257.appendleft(tmp258)
                            subjects241.appendleft(tmp256)
                    if len(subjects241) >= 1 and isinstance(subjects241[0], Mul):
                        tmp263 = subjects241.popleft()
                        associative1 = tmp263
                        associative_type1 = type(tmp263)
                        subjects264 = deque(tmp263._args)
                        matcher = CommutativeMatcher67261.get()
                        tmp265 = subjects264
                        subjects264 = []
                        for s in tmp265:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp265, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 67262
                                if len(subjects241) == 0:
                                    pass
                                    # State 67263
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp266 = subjects2.popleft()
                                        # State 67264
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67265
                                            if len(subjects) == 0:
                                                pass
                                                # 29: 1/tan(d + x*e)
                                                yield 29, subst2
                                        subjects2.appendleft(tmp266)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                        tmp267 = subjects2.popleft()
                                        # State 82113
                                        if len(subjects2) == 0:
                                            pass
                                            # State 82114
                                            if len(subjects) == 0:
                                                pass
                                                # 43: tan(d + x*e)**2
                                                yield 43, subst2
                                        subjects2.appendleft(tmp267)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                        tmp268 = subjects2.popleft()
                                        # State 82131
                                        if len(subjects2) == 0:
                                            pass
                                            # State 82132
                                            if len(subjects) == 0:
                                                pass
                                                # 44: tan(d + x*e)**(-2)
                                                yield 44, subst2
                                        subjects2.appendleft(tmp268)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83539
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83540
                                            if len(subjects) == 0:
                                                pass
                                                # 47: tan(d + x*e)**n
                                                yield 47, subst3
                                    if len(subjects2) >= 1:
                                        tmp270 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3', tmp270)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83539
                                            if len(subjects2) == 0:
                                                pass
                                                # State 83540
                                                if len(subjects) == 0:
                                                    pass
                                                    # 47: tan(d + x*e)**n
                                                    yield 47, subst3
                                        subjects2.appendleft(tmp270)
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.1.3_1', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83588
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83589
                                            if len(subjects) == 0:
                                                pass
                                                # 48: tan(d + x*e)**n2
                                                yield 48, subst3
                                    if len(subjects2) >= 1:
                                        tmp273 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.3_1', tmp273)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 83588
                                            if len(subjects2) == 0:
                                                pass
                                                # State 83589
                                                if len(subjects) == 0:
                                                    pass
                                                    # 48: tan(d + x*e)**n2
                                                    yield 48, subst3
                                        subjects2.appendleft(tmp273)
                            if pattern_index == 1:
                                pass
                                # State 87647
                                if len(subjects241) == 0:
                                    pass
                                    # State 87648
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp275 = subjects2.popleft()
                                        # State 87649
                                        if len(subjects2) == 0:
                                            pass
                                            # State 87650
                                            if len(subjects) == 0:
                                                pass
                                                # 52: 1/tan(c + d*x**n)
                                                yield 52, subst2
                                        subjects2.appendleft(tmp275)
                        subjects241.appendleft(tmp263)
                if len(subjects241) >= 1:
                    tmp276 = subjects241.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp276)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 87925
                        if len(subjects241) == 0:
                            pass
                            # State 87926
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp278 = subjects2.popleft()
                                # State 87927
                                if len(subjects2) == 0:
                                    pass
                                    # State 87928
                                    if len(subjects) == 0:
                                        pass
                                        # 54: 1/tan(u)
                                        yield 54, subst1
                                subjects2.appendleft(tmp278)
                    subjects241.appendleft(tmp276)
                if len(subjects241) >= 1 and isinstance(subjects241[0], Add):
                    tmp279 = subjects241.popleft()
                    associative1 = tmp279
                    associative_type1 = type(tmp279)
                    subjects280 = deque(tmp279._args)
                    matcher = CommutativeMatcher67267.get()
                    tmp281 = subjects280
                    subjects280 = []
                    for s in tmp281:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp281, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 67273
                            if len(subjects241) == 0:
                                pass
                                # State 67274
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp282 = subjects2.popleft()
                                    # State 67275
                                    if len(subjects2) == 0:
                                        pass
                                        # State 67276
                                        if len(subjects) == 0:
                                            pass
                                            # 29: 1/tan(d + x*e)
                                            yield 29, subst1
                                    subjects2.appendleft(tmp282)
                                if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                    tmp283 = subjects2.popleft()
                                    # State 82115
                                    if len(subjects2) == 0:
                                        pass
                                        # State 82116
                                        if len(subjects) == 0:
                                            pass
                                            # 43: tan(d + x*e)**2
                                            yield 43, subst1
                                    subjects2.appendleft(tmp283)
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                    tmp284 = subjects2.popleft()
                                    # State 82133
                                    if len(subjects2) == 0:
                                        pass
                                        # State 82134
                                        if len(subjects) == 0:
                                            pass
                                            # 44: tan(d + x*e)**(-2)
                                            yield 44, subst1
                                    subjects2.appendleft(tmp284)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83541
                                    if len(subjects2) == 0:
                                        pass
                                        # State 83542
                                        if len(subjects) == 0:
                                            pass
                                            # 47: tan(d + x*e)**n
                                            yield 47, subst2
                                if len(subjects2) >= 1:
                                    tmp286 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3', tmp286)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83541
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83542
                                            if len(subjects) == 0:
                                                pass
                                                # 47: tan(d + x*e)**n
                                                yield 47, subst2
                                    subjects2.appendleft(tmp286)
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.3_1', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83590
                                    if len(subjects2) == 0:
                                        pass
                                        # State 83591
                                        if len(subjects) == 0:
                                            pass
                                            # 48: tan(d + x*e)**n2
                                            yield 48, subst2
                                if len(subjects2) >= 1:
                                    tmp289 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i3.1.3_1', tmp289)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 83590
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83591
                                            if len(subjects) == 0:
                                                pass
                                                # 48: tan(d + x*e)**n2
                                                yield 48, subst2
                                    subjects2.appendleft(tmp289)
                        if pattern_index == 1:
                            pass
                            # State 87661
                            if len(subjects241) == 0:
                                pass
                                # State 87662
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp291 = subjects2.popleft()
                                    # State 87663
                                    if len(subjects2) == 0:
                                        pass
                                        # State 87664
                                        if len(subjects) == 0:
                                            pass
                                            # 52: 1/tan(c + d*x**n)
                                            yield 52, subst1
                                    subjects2.appendleft(tmp291)
                    subjects241.appendleft(tmp279)
                subjects2.appendleft(tmp240)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                tmp292 = subjects2.popleft()
                subjects293 = deque(tmp292._args)
                # State 83889
                if len(subjects293) >= 1 and isinstance(subjects293[0], tan):
                    tmp294 = subjects293.popleft()
                    subjects295 = deque(tmp294._args)
                    # State 83890
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83891
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83892
                            if len(subjects295) >= 1:
                                tmp298 = subjects295.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.4.1.0', tmp298)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83893
                                    if len(subjects295) == 0:
                                        pass
                                        # State 83894
                                        if len(subjects293) >= 1 and subjects293[0] == Integer(-1):
                                            tmp300 = subjects293.popleft()
                                            # State 83895
                                            if len(subjects293) == 0:
                                                pass
                                                # State 83896
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 83897
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 83898
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 49: (1/tan(d + x*e))**n
                                                            yield 49, subst4
                                                if len(subjects2) >= 1:
                                                    tmp302 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5', tmp302)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83897
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 83898
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 49: (1/tan(d + x*e))**n
                                                                yield 49, subst4
                                                    subjects2.appendleft(tmp302)
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 84004
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 84005
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 50: (1/tan(d + x*e))**n2
                                                            yield 50, subst4
                                                if len(subjects2) >= 1:
                                                    tmp305 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5_1', tmp305)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 84004
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 84005
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 50: (1/tan(d + x*e))**n2
                                                                yield 50, subst4
                                                    subjects2.appendleft(tmp305)
                                            subjects293.appendleft(tmp300)
                                subjects295.appendleft(tmp298)
                        if len(subjects295) >= 1 and isinstance(subjects295[0], Mul):
                            tmp307 = subjects295.popleft()
                            associative1 = tmp307
                            associative_type1 = type(tmp307)
                            subjects308 = deque(tmp307._args)
                            matcher = CommutativeMatcher83900.get()
                            tmp309 = subjects308
                            subjects308 = []
                            for s in tmp309:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp309, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83901
                                    if len(subjects295) == 0:
                                        pass
                                        # State 83902
                                        if len(subjects293) >= 1 and subjects293[0] == Integer(-1):
                                            tmp310 = subjects293.popleft()
                                            # State 83903
                                            if len(subjects293) == 0:
                                                pass
                                                # State 83904
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 83905
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 83906
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 49: (1/tan(d + x*e))**n
                                                            yield 49, subst3
                                                if len(subjects2) >= 1:
                                                    tmp312 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5', tmp312)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 83905
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 83906
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 49: (1/tan(d + x*e))**n
                                                                yield 49, subst3
                                                    subjects2.appendleft(tmp312)
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 84006
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 84007
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 50: (1/tan(d + x*e))**n2
                                                            yield 50, subst3
                                                if len(subjects2) >= 1:
                                                    tmp315 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5_1', tmp315)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 84006
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 84007
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 50: (1/tan(d + x*e))**n2
                                                                yield 50, subst3
                                                    subjects2.appendleft(tmp315)
                                            subjects293.appendleft(tmp310)
                            subjects295.appendleft(tmp307)
                    if len(subjects295) >= 1 and isinstance(subjects295[0], Add):
                        tmp317 = subjects295.popleft()
                        associative1 = tmp317
                        associative_type1 = type(tmp317)
                        subjects318 = deque(tmp317._args)
                        matcher = CommutativeMatcher83908.get()
                        tmp319 = subjects318
                        subjects318 = []
                        for s in tmp319:
                            matcher.add_subject(s)
                        for pattern_index, subst1 in matcher.match(tmp319, subst0):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83914
                                if len(subjects295) == 0:
                                    pass
                                    # State 83915
                                    if len(subjects293) >= 1 and subjects293[0] == Integer(-1):
                                        tmp320 = subjects293.popleft()
                                        # State 83916
                                        if len(subjects293) == 0:
                                            pass
                                            # State 83917
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i3.1.5', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 83918
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 83919
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 49: (1/tan(d + x*e))**n
                                                        yield 49, subst2
                                            if len(subjects2) >= 1:
                                                tmp322 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i3.1.5', tmp322)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 83918
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 83919
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 49: (1/tan(d + x*e))**n
                                                            yield 49, subst2
                                                subjects2.appendleft(tmp322)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i3.1.5_1', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 84008
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 84009
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 50: (1/tan(d + x*e))**n2
                                                        yield 50, subst2
                                            if len(subjects2) >= 1:
                                                tmp325 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i3.1.5_1', tmp325)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 84008
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 84009
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 50: (1/tan(d + x*e))**n2
                                                            yield 50, subst2
                                                subjects2.appendleft(tmp325)
                                        subjects293.appendleft(tmp320)
                        subjects295.appendleft(tmp317)
                    subjects293.appendleft(tmp294)
                if len(subjects293) >= 1 and isinstance(subjects293[0], cos):
                    tmp327 = subjects293.popleft()
                    subjects328 = deque(tmp327._args)
                    # State 95595
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 95596
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95597
                            if len(subjects328) >= 1:
                                tmp331 = subjects328.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.4.1.0', tmp331)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 95598
                                    if len(subjects328) == 0:
                                        pass
                                        # State 95599
                                        if len(subjects293) >= 1 and subjects293[0] == Integer(-1):
                                            tmp333 = subjects293.popleft()
                                            # State 95600
                                            if len(subjects293) == 0:
                                                pass
                                                # State 95601
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95602
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95603
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 57: (1/cos(d + x*e))**n
                                                            yield 57, subst4
                                                if len(subjects2) >= 1:
                                                    tmp335 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5', tmp335)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95602
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 95603
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 57: (1/cos(d + x*e))**n
                                                                yield 57, subst4
                                                    subjects2.appendleft(tmp335)
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95704
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95705
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 58: (1/cos(d + x*e))**n2
                                                            yield 58, subst4
                                                if len(subjects2) >= 1:
                                                    tmp338 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5_1', tmp338)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95704
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 95705
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 58: (1/cos(d + x*e))**n2
                                                                yield 58, subst4
                                                    subjects2.appendleft(tmp338)
                                            subjects293.appendleft(tmp333)
                                subjects328.appendleft(tmp331)
                        if len(subjects328) >= 1 and isinstance(subjects328[0], Mul):
                            tmp340 = subjects328.popleft()
                            associative1 = tmp340
                            associative_type1 = type(tmp340)
                            subjects341 = deque(tmp340._args)
                            matcher = CommutativeMatcher95605.get()
                            tmp342 = subjects341
                            subjects341 = []
                            for s in tmp342:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp342, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95606
                                    if len(subjects328) == 0:
                                        pass
                                        # State 95607
                                        if len(subjects293) >= 1 and subjects293[0] == Integer(-1):
                                            tmp343 = subjects293.popleft()
                                            # State 95608
                                            if len(subjects293) == 0:
                                                pass
                                                # State 95609
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95610
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95611
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 57: (1/cos(d + x*e))**n
                                                            yield 57, subst3
                                                if len(subjects2) >= 1:
                                                    tmp345 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5', tmp345)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95610
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 95611
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 57: (1/cos(d + x*e))**n
                                                                yield 57, subst3
                                                    subjects2.appendleft(tmp345)
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95706
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95707
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 58: (1/cos(d + x*e))**n2
                                                            yield 58, subst3
                                                if len(subjects2) >= 1:
                                                    tmp348 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5_1', tmp348)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95706
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 95707
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 58: (1/cos(d + x*e))**n2
                                                                yield 58, subst3
                                                    subjects2.appendleft(tmp348)
                                            subjects293.appendleft(tmp343)
                            subjects328.appendleft(tmp340)
                    if len(subjects328) >= 1 and isinstance(subjects328[0], Add):
                        tmp350 = subjects328.popleft()
                        associative1 = tmp350
                        associative_type1 = type(tmp350)
                        subjects351 = deque(tmp350._args)
                        matcher = CommutativeMatcher95613.get()
                        tmp352 = subjects351
                        subjects351 = []
                        for s in tmp352:
                            matcher.add_subject(s)
                        for pattern_index, subst1 in matcher.match(tmp352, subst0):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 95619
                                if len(subjects328) == 0:
                                    pass
                                    # State 95620
                                    if len(subjects293) >= 1 and subjects293[0] == Integer(-1):
                                        tmp353 = subjects293.popleft()
                                        # State 95621
                                        if len(subjects293) == 0:
                                            pass
                                            # State 95622
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i3.1.5', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 95623
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 95624
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 57: (1/cos(d + x*e))**n
                                                        yield 57, subst2
                                            if len(subjects2) >= 1:
                                                tmp355 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i3.1.5', tmp355)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95623
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95624
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 57: (1/cos(d + x*e))**n
                                                            yield 57, subst2
                                                subjects2.appendleft(tmp355)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i3.1.5_1', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 95708
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 95709
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 58: (1/cos(d + x*e))**n2
                                                        yield 58, subst2
                                            if len(subjects2) >= 1:
                                                tmp358 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i3.1.5_1', tmp358)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95708
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95709
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 58: (1/cos(d + x*e))**n2
                                                            yield 58, subst2
                                                subjects2.appendleft(tmp358)
                                        subjects293.appendleft(tmp353)
                        subjects328.appendleft(tmp350)
                    subjects293.appendleft(tmp327)
                if len(subjects293) >= 1 and isinstance(subjects293[0], sin):
                    tmp360 = subjects293.popleft()
                    subjects361 = deque(tmp360._args)
                    # State 95991
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 95992
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95993
                            if len(subjects361) >= 1:
                                tmp364 = subjects361.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.4.1.0', tmp364)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 95994
                                    if len(subjects361) == 0:
                                        pass
                                        # State 95995
                                        if len(subjects293) >= 1 and subjects293[0] == Integer(-1):
                                            tmp366 = subjects293.popleft()
                                            # State 95996
                                            if len(subjects293) == 0:
                                                pass
                                                # State 95997
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 95998
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 95999
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 59: (1/sin(d + x*e))**n
                                                            yield 59, subst4
                                                if len(subjects2) >= 1:
                                                    tmp368 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5', tmp368)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 95998
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 95999
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 59: (1/sin(d + x*e))**n
                                                                yield 59, subst4
                                                    subjects2.appendleft(tmp368)
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 96100
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 96101
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 60: (1/sin(d + x*e))**n2
                                                            yield 60, subst4
                                                if len(subjects2) >= 1:
                                                    tmp371 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i3.1.5_1', tmp371)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 96100
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 96101
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 60: (1/sin(d + x*e))**n2
                                                                yield 60, subst4
                                                    subjects2.appendleft(tmp371)
                                            subjects293.appendleft(tmp366)
                                subjects361.appendleft(tmp364)
                        if len(subjects361) >= 1 and isinstance(subjects361[0], Mul):
                            tmp373 = subjects361.popleft()
                            associative1 = tmp373
                            associative_type1 = type(tmp373)
                            subjects374 = deque(tmp373._args)
                            matcher = CommutativeMatcher96001.get()
                            tmp375 = subjects374
                            subjects374 = []
                            for s in tmp375:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp375, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 96002
                                    if len(subjects361) == 0:
                                        pass
                                        # State 96003
                                        if len(subjects293) >= 1 and subjects293[0] == Integer(-1):
                                            tmp376 = subjects293.popleft()
                                            # State 96004
                                            if len(subjects293) == 0:
                                                pass
                                                # State 96005
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 96006
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 96007
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 59: (1/sin(d + x*e))**n
                                                            yield 59, subst3
                                                if len(subjects2) >= 1:
                                                    tmp378 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5', tmp378)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 96006
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 96007
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 59: (1/sin(d + x*e))**n
                                                                yield 59, subst3
                                                    subjects2.appendleft(tmp378)
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i3.1.5_1', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 96102
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 96103
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 60: (1/sin(d + x*e))**n2
                                                            yield 60, subst3
                                                if len(subjects2) >= 1:
                                                    tmp381 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i3.1.5_1', tmp381)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 96102
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 96103
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 60: (1/sin(d + x*e))**n2
                                                                yield 60, subst3
                                                    subjects2.appendleft(tmp381)
                                            subjects293.appendleft(tmp376)
                            subjects361.appendleft(tmp373)
                    if len(subjects361) >= 1 and isinstance(subjects361[0], Add):
                        tmp383 = subjects361.popleft()
                        associative1 = tmp383
                        associative_type1 = type(tmp383)
                        subjects384 = deque(tmp383._args)
                        matcher = CommutativeMatcher96009.get()
                        tmp385 = subjects384
                        subjects384 = []
                        for s in tmp385:
                            matcher.add_subject(s)
                        for pattern_index, subst1 in matcher.match(tmp385, subst0):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 96015
                                if len(subjects361) == 0:
                                    pass
                                    # State 96016
                                    if len(subjects293) >= 1 and subjects293[0] == Integer(-1):
                                        tmp386 = subjects293.popleft()
                                        # State 96017
                                        if len(subjects293) == 0:
                                            pass
                                            # State 96018
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i3.1.5', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 96019
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 96020
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 59: (1/sin(d + x*e))**n
                                                        yield 59, subst2
                                            if len(subjects2) >= 1:
                                                tmp388 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i3.1.5', tmp388)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 96019
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 96020
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 59: (1/sin(d + x*e))**n
                                                            yield 59, subst2
                                                subjects2.appendleft(tmp388)
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i3.1.5_1', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 96104
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 96105
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 60: (1/sin(d + x*e))**n2
                                                        yield 60, subst2
                                            if len(subjects2) >= 1:
                                                tmp391 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i3.1.5_1', tmp391)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 96104
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 96105
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 60: (1/sin(d + x*e))**n2
                                                            yield 60, subst2
                                                subjects2.appendleft(tmp391)
                                        subjects293.appendleft(tmp386)
                        subjects361.appendleft(tmp383)
                    subjects293.appendleft(tmp360)
                subjects2.appendleft(tmp292)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tanh):
                tmp393 = subjects2.popleft()
                subjects394 = deque(tmp393._args)
                # State 127122
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 127123
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 127124
                        if len(subjects394) >= 1 and isinstance(subjects394[0], Pow):
                            tmp397 = subjects394.popleft()
                            subjects398 = deque(tmp397._args)
                            # State 127125
                            if len(subjects398) >= 1:
                                tmp399 = subjects398.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp399)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 127126
                                    if len(subjects398) >= 1:
                                        tmp401 = subjects398.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp401)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 127127
                                            if len(subjects398) == 0:
                                                pass
                                                # State 127128
                                                if len(subjects394) == 0:
                                                    pass
                                                    # State 127129
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp403 = subjects2.popleft()
                                                        # State 127130
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 127131
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 85: 1/tanh(c + d*x**n)
                                                                yield 85, subst4
                                                        subjects2.appendleft(tmp403)
                                        subjects398.appendleft(tmp401)
                                subjects398.appendleft(tmp399)
                            subjects394.appendleft(tmp397)
                    if len(subjects394) >= 1 and isinstance(subjects394[0], Mul):
                        tmp404 = subjects394.popleft()
                        associative1 = tmp404
                        associative_type1 = type(tmp404)
                        subjects405 = deque(tmp404._args)
                        matcher = CommutativeMatcher127133.get()
                        tmp406 = subjects405
                        subjects405 = []
                        for s in tmp406:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp406, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 127138
                                if len(subjects394) == 0:
                                    pass
                                    # State 127139
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp407 = subjects2.popleft()
                                        # State 127140
                                        if len(subjects2) == 0:
                                            pass
                                            # State 127141
                                            if len(subjects) == 0:
                                                pass
                                                # 85: 1/tanh(c + d*x**n)
                                                yield 85, subst2
                                        subjects2.appendleft(tmp407)
                        subjects394.appendleft(tmp404)
                if len(subjects394) >= 1:
                    tmp408 = subjects394.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp408)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 127420
                        if len(subjects394) == 0:
                            pass
                            # State 127421
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp410 = subjects2.popleft()
                                # State 127422
                                if len(subjects2) == 0:
                                    pass
                                    # State 127423
                                    if len(subjects) == 0:
                                        pass
                                        # 87: 1/tanh(u)
                                        yield 87, subst1
                                subjects2.appendleft(tmp410)
                    subjects394.appendleft(tmp408)
                if len(subjects394) >= 1 and isinstance(subjects394[0], Add):
                    tmp411 = subjects394.popleft()
                    associative1 = tmp411
                    associative_type1 = type(tmp411)
                    subjects412 = deque(tmp411._args)
                    matcher = CommutativeMatcher127143.get()
                    tmp413 = subjects412
                    subjects412 = []
                    for s in tmp413:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp413, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 127156
                            if len(subjects394) == 0:
                                pass
                                # State 127157
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp414 = subjects2.popleft()
                                    # State 127158
                                    if len(subjects2) == 0:
                                        pass
                                        # State 127159
                                        if len(subjects) == 0:
                                            pass
                                            # 85: 1/tanh(c + d*x**n)
                                            yield 85, subst1
                                    subjects2.appendleft(tmp414)
                    subjects394.appendleft(tmp411)
                subjects2.appendleft(tmp393)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cosh):
                tmp415 = subjects2.popleft()
                subjects416 = deque(tmp415._args)
                # State 129899
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 129900
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 129901
                        if len(subjects416) >= 1 and isinstance(subjects416[0], Pow):
                            tmp419 = subjects416.popleft()
                            subjects420 = deque(tmp419._args)
                            # State 129902
                            if len(subjects420) >= 1:
                                tmp421 = subjects420.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp421)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 129903
                                    if len(subjects420) >= 1:
                                        tmp423 = subjects420.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp423)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 129904
                                            if len(subjects420) == 0:
                                                pass
                                                # State 129905
                                                if len(subjects416) == 0:
                                                    pass
                                                    # State 129906
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp425 = subjects2.popleft()
                                                        # State 129907
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 129908
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 88: 1/cosh(c + d*x**n)
                                                                yield 88, subst4
                                                        subjects2.appendleft(tmp425)
                                        subjects420.appendleft(tmp423)
                                subjects420.appendleft(tmp421)
                            subjects416.appendleft(tmp419)
                    if len(subjects416) >= 1 and isinstance(subjects416[0], Mul):
                        tmp426 = subjects416.popleft()
                        associative1 = tmp426
                        associative_type1 = type(tmp426)
                        subjects427 = deque(tmp426._args)
                        matcher = CommutativeMatcher129910.get()
                        tmp428 = subjects427
                        subjects427 = []
                        for s in tmp428:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp428, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 129915
                                if len(subjects416) == 0:
                                    pass
                                    # State 129916
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp429 = subjects2.popleft()
                                        # State 129917
                                        if len(subjects2) == 0:
                                            pass
                                            # State 129918
                                            if len(subjects) == 0:
                                                pass
                                                # 88: 1/cosh(c + d*x**n)
                                                yield 88, subst2
                                        subjects2.appendleft(tmp429)
                        subjects416.appendleft(tmp426)
                if len(subjects416) >= 1:
                    tmp430 = subjects416.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp430)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130513
                        if len(subjects416) == 0:
                            pass
                            # State 130514
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp432 = subjects2.popleft()
                                # State 130515
                                if len(subjects2) == 0:
                                    pass
                                    # State 130516
                                    if len(subjects) == 0:
                                        pass
                                        # 90: 1/cosh(u)
                                        yield 90, subst1
                                subjects2.appendleft(tmp432)
                    subjects416.appendleft(tmp430)
                if len(subjects416) >= 1 and isinstance(subjects416[0], Add):
                    tmp433 = subjects416.popleft()
                    associative1 = tmp433
                    associative_type1 = type(tmp433)
                    subjects434 = deque(tmp433._args)
                    matcher = CommutativeMatcher129920.get()
                    tmp435 = subjects434
                    subjects434 = []
                    for s in tmp435:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp435, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 129933
                            if len(subjects416) == 0:
                                pass
                                # State 129934
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp436 = subjects2.popleft()
                                    # State 129935
                                    if len(subjects2) == 0:
                                        pass
                                        # State 129936
                                        if len(subjects) == 0:
                                            pass
                                            # 88: 1/cosh(c + d*x**n)
                                            yield 88, subst1
                                    subjects2.appendleft(tmp436)
                    subjects416.appendleft(tmp433)
                subjects2.appendleft(tmp415)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sinh):
                tmp437 = subjects2.popleft()
                subjects438 = deque(tmp437._args)
                # State 130239
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 130240
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130241
                        if len(subjects438) >= 1 and isinstance(subjects438[0], Pow):
                            tmp441 = subjects438.popleft()
                            subjects442 = deque(tmp441._args)
                            # State 130242
                            if len(subjects442) >= 1:
                                tmp443 = subjects442.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp443)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 130243
                                    if len(subjects442) >= 1:
                                        tmp445 = subjects442.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp445)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 130244
                                            if len(subjects442) == 0:
                                                pass
                                                # State 130245
                                                if len(subjects438) == 0:
                                                    pass
                                                    # State 130246
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp447 = subjects2.popleft()
                                                        # State 130247
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 130248
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 89: 1/sinh(c + d*x**n)
                                                                yield 89, subst4
                                                        subjects2.appendleft(tmp447)
                                        subjects442.appendleft(tmp445)
                                subjects442.appendleft(tmp443)
                            subjects438.appendleft(tmp441)
                    if len(subjects438) >= 1 and isinstance(subjects438[0], Mul):
                        tmp448 = subjects438.popleft()
                        associative1 = tmp448
                        associative_type1 = type(tmp448)
                        subjects449 = deque(tmp448._args)
                        matcher = CommutativeMatcher130250.get()
                        tmp450 = subjects449
                        subjects449 = []
                        for s in tmp450:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp450, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 130255
                                if len(subjects438) == 0:
                                    pass
                                    # State 130256
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp451 = subjects2.popleft()
                                        # State 130257
                                        if len(subjects2) == 0:
                                            pass
                                            # State 130258
                                            if len(subjects) == 0:
                                                pass
                                                # 89: 1/sinh(c + d*x**n)
                                                yield 89, subst2
                                        subjects2.appendleft(tmp451)
                        subjects438.appendleft(tmp448)
                if len(subjects438) >= 1:
                    tmp452 = subjects438.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp452)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130569
                        if len(subjects438) == 0:
                            pass
                            # State 130570
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp454 = subjects2.popleft()
                                # State 130571
                                if len(subjects2) == 0:
                                    pass
                                    # State 130572
                                    if len(subjects) == 0:
                                        pass
                                        # 91: 1/sinh(u)
                                        yield 91, subst1
                                subjects2.appendleft(tmp454)
                    subjects438.appendleft(tmp452)
                if len(subjects438) >= 1 and isinstance(subjects438[0], Add):
                    tmp455 = subjects438.popleft()
                    associative1 = tmp455
                    associative_type1 = type(tmp455)
                    subjects456 = deque(tmp455._args)
                    matcher = CommutativeMatcher130260.get()
                    tmp457 = subjects456
                    subjects456 = []
                    for s in tmp457:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp457, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 130273
                            if len(subjects438) == 0:
                                pass
                                # State 130274
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp458 = subjects2.popleft()
                                    # State 130275
                                    if len(subjects2) == 0:
                                        pass
                                        # State 130276
                                        if len(subjects) == 0:
                                            pass
                                            # 89: 1/sinh(c + d*x**n)
                                            yield 89, subst1
                                    subjects2.appendleft(tmp458)
                    subjects438.appendleft(tmp455)
                subjects2.appendleft(tmp437)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 8176
            if len(subjects) >= 1:
                tmp460 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.1', tmp460)
                except ValueError:
                    pass
                else:
                    pass
                    # State 8177
                    if len(subjects) == 0:
                        pass
                        # 6: x**n2
                        yield 6, subst2
                subjects.appendleft(tmp460)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10963
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp463 = subjects.popleft()
                    subjects464 = deque(tmp463._args)
                    # State 10964
                    if len(subjects464) >= 1:
                        tmp465 = subjects464.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1', tmp465)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10965
                            if len(subjects464) >= 1 and subjects464[0] == Integer(-1):
                                tmp467 = subjects464.popleft()
                                # State 10966
                                if len(subjects464) == 0:
                                    pass
                                    # State 10967
                                    if len(subjects) == 0:
                                        pass
                                        # 12: (c/x)**n2
                                        yield 12, subst3
                                subjects464.appendleft(tmp467)
                        subjects464.appendleft(tmp465)
                    subjects.appendleft(tmp463)
            if len(subjects) >= 1:
                tmp468 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1', tmp468)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11180
                    if len(subjects) == 0:
                        pass
                        # 13: x**n2
                        yield 13, subst2
                subjects.appendleft(tmp468)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp470 = subjects.popleft()
                associative1 = tmp470
                associative_type1 = type(tmp470)
                subjects471 = deque(tmp470._args)
                matcher = CommutativeMatcher10969.get()
                tmp472 = subjects471
                subjects471 = []
                for s in tmp472:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp472, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10974
                        if len(subjects) == 0:
                            pass
                            # 12: (c/x)**n2
                            yield 12, subst2
                subjects.appendleft(tmp470)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 9755
            if len(subjects) >= 1:
                tmp474 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.1', tmp474)
                except ValueError:
                    pass
                else:
                    pass
                    # State 9756
                    if len(subjects) == 0:
                        pass
                        # 8: x**n
                        yield 8, subst2
                subjects.appendleft(tmp474)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 9767
            if len(subjects) >= 1:
                tmp477 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.1', tmp477)
                except ValueError:
                    pass
                else:
                    pass
                    # State 9768
                    if len(subjects) == 0:
                        pass
                        # 9: x**r
                        yield 9, subst2
                subjects.appendleft(tmp477)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 68917
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp480 = subjects.popleft()
                subjects481 = deque(tmp480._args)
                # State 68918
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68919
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 68920
                        if len(subjects481) >= 1:
                            tmp484 = subjects481.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0', tmp484)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 68921
                                if len(subjects481) == 0:
                                    pass
                                    # State 68922
                                    if len(subjects) == 0:
                                        pass
                                        # 34: sin(d + x*e)**n
                                        yield 34, subst4
                            subjects481.appendleft(tmp484)
                    if len(subjects481) >= 1 and isinstance(subjects481[0], Mul):
                        tmp486 = subjects481.popleft()
                        associative1 = tmp486
                        associative_type1 = type(tmp486)
                        subjects487 = deque(tmp486._args)
                        matcher = CommutativeMatcher68924.get()
                        tmp488 = subjects487
                        subjects487 = []
                        for s in tmp488:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp488, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 68925
                                if len(subjects481) == 0:
                                    pass
                                    # State 68926
                                    if len(subjects) == 0:
                                        pass
                                        # 34: sin(d + x*e)**n
                                        yield 34, subst3
                        subjects481.appendleft(tmp486)
                if len(subjects481) >= 1 and isinstance(subjects481[0], Add):
                    tmp489 = subjects481.popleft()
                    associative1 = tmp489
                    associative_type1 = type(tmp489)
                    subjects490 = deque(tmp489._args)
                    matcher = CommutativeMatcher68928.get()
                    tmp491 = subjects490
                    subjects490 = []
                    for s in tmp491:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp491, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 68934
                            if len(subjects481) == 0:
                                pass
                                # State 68935
                                if len(subjects) == 0:
                                    pass
                                    # 34: sin(d + x*e)**n
                                    yield 34, subst2
                    subjects481.appendleft(tmp489)
                subjects.appendleft(tmp480)
            if len(subjects) >= 1 and isinstance(subjects[0], cos):
                tmp492 = subjects.popleft()
                subjects493 = deque(tmp492._args)
                # State 69196
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 69197
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 69198
                        if len(subjects493) >= 1:
                            tmp496 = subjects493.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0', tmp496)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 69199
                                if len(subjects493) == 0:
                                    pass
                                    # State 69200
                                    if len(subjects) == 0:
                                        pass
                                        # 36: cos(d + x*e)**n
                                        yield 36, subst4
                            subjects493.appendleft(tmp496)
                    if len(subjects493) >= 1 and isinstance(subjects493[0], Mul):
                        tmp498 = subjects493.popleft()
                        associative1 = tmp498
                        associative_type1 = type(tmp498)
                        subjects499 = deque(tmp498._args)
                        matcher = CommutativeMatcher69202.get()
                        tmp500 = subjects499
                        subjects499 = []
                        for s in tmp500:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp500, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 69203
                                if len(subjects493) == 0:
                                    pass
                                    # State 69204
                                    if len(subjects) == 0:
                                        pass
                                        # 36: cos(d + x*e)**n
                                        yield 36, subst3
                        subjects493.appendleft(tmp498)
                if len(subjects493) >= 1 and isinstance(subjects493[0], Add):
                    tmp501 = subjects493.popleft()
                    associative1 = tmp501
                    associative_type1 = type(tmp501)
                    subjects502 = deque(tmp501._args)
                    matcher = CommutativeMatcher69206.get()
                    tmp503 = subjects502
                    subjects502 = []
                    for s in tmp503:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp503, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 69212
                            if len(subjects493) == 0:
                                pass
                                # State 69213
                                if len(subjects) == 0:
                                    pass
                                    # 36: cos(d + x*e)**n
                                    yield 36, subst2
                    subjects493.appendleft(tmp501)
                subjects.appendleft(tmp492)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp504 = subjects.popleft()
                subjects505 = deque(tmp504._args)
                # State 83519
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 83520
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83521
                        if len(subjects505) >= 1:
                            tmp508 = subjects505.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0', tmp508)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83522
                                if len(subjects505) == 0:
                                    pass
                                    # State 83523
                                    if len(subjects) == 0:
                                        pass
                                        # 47: tan(d + x*e)**n
                                        yield 47, subst4
                            subjects505.appendleft(tmp508)
                    if len(subjects505) >= 1 and isinstance(subjects505[0], Mul):
                        tmp510 = subjects505.popleft()
                        associative1 = tmp510
                        associative_type1 = type(tmp510)
                        subjects511 = deque(tmp510._args)
                        matcher = CommutativeMatcher83525.get()
                        tmp512 = subjects511
                        subjects511 = []
                        for s in tmp512:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp512, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83526
                                if len(subjects505) == 0:
                                    pass
                                    # State 83527
                                    if len(subjects) == 0:
                                        pass
                                        # 47: tan(d + x*e)**n
                                        yield 47, subst3
                        subjects505.appendleft(tmp510)
                if len(subjects505) >= 1 and isinstance(subjects505[0], Add):
                    tmp513 = subjects505.popleft()
                    associative1 = tmp513
                    associative_type1 = type(tmp513)
                    subjects514 = deque(tmp513._args)
                    matcher = CommutativeMatcher83529.get()
                    tmp515 = subjects514
                    subjects514 = []
                    for s in tmp515:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp515, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 83535
                            if len(subjects505) == 0:
                                pass
                                # State 83536
                                if len(subjects) == 0:
                                    pass
                                    # 47: tan(d + x*e)**n
                                    yield 47, subst2
                    subjects505.appendleft(tmp513)
                subjects.appendleft(tmp504)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.3_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 68986
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp517 = subjects.popleft()
                subjects518 = deque(tmp517._args)
                # State 68987
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68988
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 68989
                        if len(subjects518) >= 1:
                            tmp521 = subjects518.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0', tmp521)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 68990
                                if len(subjects518) == 0:
                                    pass
                                    # State 68991
                                    if len(subjects) == 0:
                                        pass
                                        # 35: sin(d + x*e)**n2
                                        yield 35, subst4
                            subjects518.appendleft(tmp521)
                    if len(subjects518) >= 1 and isinstance(subjects518[0], Mul):
                        tmp523 = subjects518.popleft()
                        associative1 = tmp523
                        associative_type1 = type(tmp523)
                        subjects524 = deque(tmp523._args)
                        matcher = CommutativeMatcher68993.get()
                        tmp525 = subjects524
                        subjects524 = []
                        for s in tmp525:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp525, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 68994
                                if len(subjects518) == 0:
                                    pass
                                    # State 68995
                                    if len(subjects) == 0:
                                        pass
                                        # 35: sin(d + x*e)**n2
                                        yield 35, subst3
                        subjects518.appendleft(tmp523)
                if len(subjects518) >= 1 and isinstance(subjects518[0], Add):
                    tmp526 = subjects518.popleft()
                    associative1 = tmp526
                    associative_type1 = type(tmp526)
                    subjects527 = deque(tmp526._args)
                    matcher = CommutativeMatcher68997.get()
                    tmp528 = subjects527
                    subjects527 = []
                    for s in tmp528:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp528, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 69003
                            if len(subjects518) == 0:
                                pass
                                # State 69004
                                if len(subjects) == 0:
                                    pass
                                    # 35: sin(d + x*e)**n2
                                    yield 35, subst2
                    subjects518.appendleft(tmp526)
                subjects.appendleft(tmp517)
            if len(subjects) >= 1 and isinstance(subjects[0], cos):
                tmp529 = subjects.popleft()
                subjects530 = deque(tmp529._args)
                # State 69263
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 69264
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 69265
                        if len(subjects530) >= 1:
                            tmp533 = subjects530.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0', tmp533)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 69266
                                if len(subjects530) == 0:
                                    pass
                                    # State 69267
                                    if len(subjects) == 0:
                                        pass
                                        # 37: cos(d + x*e)**n2
                                        yield 37, subst4
                            subjects530.appendleft(tmp533)
                    if len(subjects530) >= 1 and isinstance(subjects530[0], Mul):
                        tmp535 = subjects530.popleft()
                        associative1 = tmp535
                        associative_type1 = type(tmp535)
                        subjects536 = deque(tmp535._args)
                        matcher = CommutativeMatcher69269.get()
                        tmp537 = subjects536
                        subjects536 = []
                        for s in tmp537:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp537, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 69270
                                if len(subjects530) == 0:
                                    pass
                                    # State 69271
                                    if len(subjects) == 0:
                                        pass
                                        # 37: cos(d + x*e)**n2
                                        yield 37, subst3
                        subjects530.appendleft(tmp535)
                if len(subjects530) >= 1 and isinstance(subjects530[0], Add):
                    tmp538 = subjects530.popleft()
                    associative1 = tmp538
                    associative_type1 = type(tmp538)
                    subjects539 = deque(tmp538._args)
                    matcher = CommutativeMatcher69273.get()
                    tmp540 = subjects539
                    subjects539 = []
                    for s in tmp540:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp540, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 69279
                            if len(subjects530) == 0:
                                pass
                                # State 69280
                                if len(subjects) == 0:
                                    pass
                                    # 37: cos(d + x*e)**n2
                                    yield 37, subst2
                    subjects530.appendleft(tmp538)
                subjects.appendleft(tmp529)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp541 = subjects.popleft()
                subjects542 = deque(tmp541._args)
                # State 83568
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 83569
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83570
                        if len(subjects542) >= 1:
                            tmp545 = subjects542.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0', tmp545)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83571
                                if len(subjects542) == 0:
                                    pass
                                    # State 83572
                                    if len(subjects) == 0:
                                        pass
                                        # 48: tan(d + x*e)**n2
                                        yield 48, subst4
                            subjects542.appendleft(tmp545)
                    if len(subjects542) >= 1 and isinstance(subjects542[0], Mul):
                        tmp547 = subjects542.popleft()
                        associative1 = tmp547
                        associative_type1 = type(tmp547)
                        subjects548 = deque(tmp547._args)
                        matcher = CommutativeMatcher83574.get()
                        tmp549 = subjects548
                        subjects548 = []
                        for s in tmp549:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp549, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83575
                                if len(subjects542) == 0:
                                    pass
                                    # State 83576
                                    if len(subjects) == 0:
                                        pass
                                        # 48: tan(d + x*e)**n2
                                        yield 48, subst3
                        subjects542.appendleft(tmp547)
                if len(subjects542) >= 1 and isinstance(subjects542[0], Add):
                    tmp550 = subjects542.popleft()
                    associative1 = tmp550
                    associative_type1 = type(tmp550)
                    subjects551 = deque(tmp550._args)
                    matcher = CommutativeMatcher83578.get()
                    tmp552 = subjects551
                    subjects551 = []
                    for s in tmp552:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp552, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 83584
                            if len(subjects542) == 0:
                                pass
                                # State 83585
                                if len(subjects) == 0:
                                    pass
                                    # 48: tan(d + x*e)**n2
                                    yield 48, subst2
                    subjects542.appendleft(tmp550)
                subjects.appendleft(tmp541)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.5', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 83863
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp554 = subjects.popleft()
                subjects555 = deque(tmp554._args)
                # State 83864
                if len(subjects555) >= 1 and isinstance(subjects555[0], tan):
                    tmp556 = subjects555.popleft()
                    subjects557 = deque(tmp556._args)
                    # State 83865
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83866
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83867
                            if len(subjects557) >= 1:
                                tmp560 = subjects557.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.0', tmp560)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83868
                                    if len(subjects557) == 0:
                                        pass
                                        # State 83869
                                        if len(subjects555) >= 1 and subjects555[0] == Integer(-1):
                                            tmp562 = subjects555.popleft()
                                            # State 83870
                                            if len(subjects555) == 0:
                                                pass
                                                # State 83871
                                                if len(subjects) == 0:
                                                    pass
                                                    # 49: (1/tan(d + x*e))**n
                                                    yield 49, subst4
                                            subjects555.appendleft(tmp562)
                                subjects557.appendleft(tmp560)
                        if len(subjects557) >= 1 and isinstance(subjects557[0], Mul):
                            tmp563 = subjects557.popleft()
                            associative1 = tmp563
                            associative_type1 = type(tmp563)
                            subjects564 = deque(tmp563._args)
                            matcher = CommutativeMatcher83873.get()
                            tmp565 = subjects564
                            subjects564 = []
                            for s in tmp565:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp565, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83874
                                    if len(subjects557) == 0:
                                        pass
                                        # State 83875
                                        if len(subjects555) >= 1 and subjects555[0] == Integer(-1):
                                            tmp566 = subjects555.popleft()
                                            # State 83876
                                            if len(subjects555) == 0:
                                                pass
                                                # State 83877
                                                if len(subjects) == 0:
                                                    pass
                                                    # 49: (1/tan(d + x*e))**n
                                                    yield 49, subst3
                                            subjects555.appendleft(tmp566)
                            subjects557.appendleft(tmp563)
                    if len(subjects557) >= 1 and isinstance(subjects557[0], Add):
                        tmp567 = subjects557.popleft()
                        associative1 = tmp567
                        associative_type1 = type(tmp567)
                        subjects568 = deque(tmp567._args)
                        matcher = CommutativeMatcher83879.get()
                        tmp569 = subjects568
                        subjects568 = []
                        for s in tmp569:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp569, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83885
                                if len(subjects557) == 0:
                                    pass
                                    # State 83886
                                    if len(subjects555) >= 1 and subjects555[0] == Integer(-1):
                                        tmp570 = subjects555.popleft()
                                        # State 83887
                                        if len(subjects555) == 0:
                                            pass
                                            # State 83888
                                            if len(subjects) == 0:
                                                pass
                                                # 49: (1/tan(d + x*e))**n
                                                yield 49, subst2
                                        subjects555.appendleft(tmp570)
                        subjects557.appendleft(tmp567)
                    subjects555.appendleft(tmp556)
                if len(subjects555) >= 1 and isinstance(subjects555[0], cos):
                    tmp571 = subjects555.popleft()
                    subjects572 = deque(tmp571._args)
                    # State 95571
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 95572
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95573
                            if len(subjects572) >= 1:
                                tmp575 = subjects572.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.0', tmp575)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 95574
                                    if len(subjects572) == 0:
                                        pass
                                        # State 95575
                                        if len(subjects555) >= 1 and subjects555[0] == Integer(-1):
                                            tmp577 = subjects555.popleft()
                                            # State 95576
                                            if len(subjects555) == 0:
                                                pass
                                                # State 95577
                                                if len(subjects) == 0:
                                                    pass
                                                    # 57: (1/cos(d + x*e))**n
                                                    yield 57, subst4
                                            subjects555.appendleft(tmp577)
                                subjects572.appendleft(tmp575)
                        if len(subjects572) >= 1 and isinstance(subjects572[0], Mul):
                            tmp578 = subjects572.popleft()
                            associative1 = tmp578
                            associative_type1 = type(tmp578)
                            subjects579 = deque(tmp578._args)
                            matcher = CommutativeMatcher95579.get()
                            tmp580 = subjects579
                            subjects579 = []
                            for s in tmp580:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp580, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95580
                                    if len(subjects572) == 0:
                                        pass
                                        # State 95581
                                        if len(subjects555) >= 1 and subjects555[0] == Integer(-1):
                                            tmp581 = subjects555.popleft()
                                            # State 95582
                                            if len(subjects555) == 0:
                                                pass
                                                # State 95583
                                                if len(subjects) == 0:
                                                    pass
                                                    # 57: (1/cos(d + x*e))**n
                                                    yield 57, subst3
                                            subjects555.appendleft(tmp581)
                            subjects572.appendleft(tmp578)
                    if len(subjects572) >= 1 and isinstance(subjects572[0], Add):
                        tmp582 = subjects572.popleft()
                        associative1 = tmp582
                        associative_type1 = type(tmp582)
                        subjects583 = deque(tmp582._args)
                        matcher = CommutativeMatcher95585.get()
                        tmp584 = subjects583
                        subjects583 = []
                        for s in tmp584:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp584, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 95591
                                if len(subjects572) == 0:
                                    pass
                                    # State 95592
                                    if len(subjects555) >= 1 and subjects555[0] == Integer(-1):
                                        tmp585 = subjects555.popleft()
                                        # State 95593
                                        if len(subjects555) == 0:
                                            pass
                                            # State 95594
                                            if len(subjects) == 0:
                                                pass
                                                # 57: (1/cos(d + x*e))**n
                                                yield 57, subst2
                                        subjects555.appendleft(tmp585)
                        subjects572.appendleft(tmp582)
                    subjects555.appendleft(tmp571)
                if len(subjects555) >= 1 and isinstance(subjects555[0], sin):
                    tmp586 = subjects555.popleft()
                    subjects587 = deque(tmp586._args)
                    # State 95967
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 95968
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95969
                            if len(subjects587) >= 1:
                                tmp590 = subjects587.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.0', tmp590)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 95970
                                    if len(subjects587) == 0:
                                        pass
                                        # State 95971
                                        if len(subjects555) >= 1 and subjects555[0] == Integer(-1):
                                            tmp592 = subjects555.popleft()
                                            # State 95972
                                            if len(subjects555) == 0:
                                                pass
                                                # State 95973
                                                if len(subjects) == 0:
                                                    pass
                                                    # 59: (1/sin(d + x*e))**n
                                                    yield 59, subst4
                                            subjects555.appendleft(tmp592)
                                subjects587.appendleft(tmp590)
                        if len(subjects587) >= 1 and isinstance(subjects587[0], Mul):
                            tmp593 = subjects587.popleft()
                            associative1 = tmp593
                            associative_type1 = type(tmp593)
                            subjects594 = deque(tmp593._args)
                            matcher = CommutativeMatcher95975.get()
                            tmp595 = subjects594
                            subjects594 = []
                            for s in tmp595:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp595, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95976
                                    if len(subjects587) == 0:
                                        pass
                                        # State 95977
                                        if len(subjects555) >= 1 and subjects555[0] == Integer(-1):
                                            tmp596 = subjects555.popleft()
                                            # State 95978
                                            if len(subjects555) == 0:
                                                pass
                                                # State 95979
                                                if len(subjects) == 0:
                                                    pass
                                                    # 59: (1/sin(d + x*e))**n
                                                    yield 59, subst3
                                            subjects555.appendleft(tmp596)
                            subjects587.appendleft(tmp593)
                    if len(subjects587) >= 1 and isinstance(subjects587[0], Add):
                        tmp597 = subjects587.popleft()
                        associative1 = tmp597
                        associative_type1 = type(tmp597)
                        subjects598 = deque(tmp597._args)
                        matcher = CommutativeMatcher95981.get()
                        tmp599 = subjects598
                        subjects598 = []
                        for s in tmp599:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp599, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 95987
                                if len(subjects587) == 0:
                                    pass
                                    # State 95988
                                    if len(subjects555) >= 1 and subjects555[0] == Integer(-1):
                                        tmp600 = subjects555.popleft()
                                        # State 95989
                                        if len(subjects555) == 0:
                                            pass
                                            # State 95990
                                            if len(subjects) == 0:
                                                pass
                                                # 59: (1/sin(d + x*e))**n
                                                yield 59, subst2
                                        subjects555.appendleft(tmp600)
                        subjects587.appendleft(tmp597)
                    subjects555.appendleft(tmp586)
                subjects.appendleft(tmp554)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.5_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 83978
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp602 = subjects.popleft()
                subjects603 = deque(tmp602._args)
                # State 83979
                if len(subjects603) >= 1 and isinstance(subjects603[0], tan):
                    tmp604 = subjects603.popleft()
                    subjects605 = deque(tmp604._args)
                    # State 83980
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83981
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 83982
                            if len(subjects605) >= 1:
                                tmp608 = subjects605.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.0', tmp608)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 83983
                                    if len(subjects605) == 0:
                                        pass
                                        # State 83984
                                        if len(subjects603) >= 1 and subjects603[0] == Integer(-1):
                                            tmp610 = subjects603.popleft()
                                            # State 83985
                                            if len(subjects603) == 0:
                                                pass
                                                # State 83986
                                                if len(subjects) == 0:
                                                    pass
                                                    # 50: (1/tan(d + x*e))**n2
                                                    yield 50, subst4
                                            subjects603.appendleft(tmp610)
                                subjects605.appendleft(tmp608)
                        if len(subjects605) >= 1 and isinstance(subjects605[0], Mul):
                            tmp611 = subjects605.popleft()
                            associative1 = tmp611
                            associative_type1 = type(tmp611)
                            subjects612 = deque(tmp611._args)
                            matcher = CommutativeMatcher83988.get()
                            tmp613 = subjects612
                            subjects612 = []
                            for s in tmp613:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp613, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 83989
                                    if len(subjects605) == 0:
                                        pass
                                        # State 83990
                                        if len(subjects603) >= 1 and subjects603[0] == Integer(-1):
                                            tmp614 = subjects603.popleft()
                                            # State 83991
                                            if len(subjects603) == 0:
                                                pass
                                                # State 83992
                                                if len(subjects) == 0:
                                                    pass
                                                    # 50: (1/tan(d + x*e))**n2
                                                    yield 50, subst3
                                            subjects603.appendleft(tmp614)
                            subjects605.appendleft(tmp611)
                    if len(subjects605) >= 1 and isinstance(subjects605[0], Add):
                        tmp615 = subjects605.popleft()
                        associative1 = tmp615
                        associative_type1 = type(tmp615)
                        subjects616 = deque(tmp615._args)
                        matcher = CommutativeMatcher83994.get()
                        tmp617 = subjects616
                        subjects616 = []
                        for s in tmp617:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp617, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 84000
                                if len(subjects605) == 0:
                                    pass
                                    # State 84001
                                    if len(subjects603) >= 1 and subjects603[0] == Integer(-1):
                                        tmp618 = subjects603.popleft()
                                        # State 84002
                                        if len(subjects603) == 0:
                                            pass
                                            # State 84003
                                            if len(subjects) == 0:
                                                pass
                                                # 50: (1/tan(d + x*e))**n2
                                                yield 50, subst2
                                        subjects603.appendleft(tmp618)
                        subjects605.appendleft(tmp615)
                    subjects603.appendleft(tmp604)
                if len(subjects603) >= 1 and isinstance(subjects603[0], cos):
                    tmp619 = subjects603.popleft()
                    subjects620 = deque(tmp619._args)
                    # State 95680
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 95681
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 95682
                            if len(subjects620) >= 1:
                                tmp623 = subjects620.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.0', tmp623)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 95683
                                    if len(subjects620) == 0:
                                        pass
                                        # State 95684
                                        if len(subjects603) >= 1 and subjects603[0] == Integer(-1):
                                            tmp625 = subjects603.popleft()
                                            # State 95685
                                            if len(subjects603) == 0:
                                                pass
                                                # State 95686
                                                if len(subjects) == 0:
                                                    pass
                                                    # 58: (1/cos(d + x*e))**n2
                                                    yield 58, subst4
                                            subjects603.appendleft(tmp625)
                                subjects620.appendleft(tmp623)
                        if len(subjects620) >= 1 and isinstance(subjects620[0], Mul):
                            tmp626 = subjects620.popleft()
                            associative1 = tmp626
                            associative_type1 = type(tmp626)
                            subjects627 = deque(tmp626._args)
                            matcher = CommutativeMatcher95688.get()
                            tmp628 = subjects627
                            subjects627 = []
                            for s in tmp628:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp628, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 95689
                                    if len(subjects620) == 0:
                                        pass
                                        # State 95690
                                        if len(subjects603) >= 1 and subjects603[0] == Integer(-1):
                                            tmp629 = subjects603.popleft()
                                            # State 95691
                                            if len(subjects603) == 0:
                                                pass
                                                # State 95692
                                                if len(subjects) == 0:
                                                    pass
                                                    # 58: (1/cos(d + x*e))**n2
                                                    yield 58, subst3
                                            subjects603.appendleft(tmp629)
                            subjects620.appendleft(tmp626)
                    if len(subjects620) >= 1 and isinstance(subjects620[0], Add):
                        tmp630 = subjects620.popleft()
                        associative1 = tmp630
                        associative_type1 = type(tmp630)
                        subjects631 = deque(tmp630._args)
                        matcher = CommutativeMatcher95694.get()
                        tmp632 = subjects631
                        subjects631 = []
                        for s in tmp632:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp632, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 95700
                                if len(subjects620) == 0:
                                    pass
                                    # State 95701
                                    if len(subjects603) >= 1 and subjects603[0] == Integer(-1):
                                        tmp633 = subjects603.popleft()
                                        # State 95702
                                        if len(subjects603) == 0:
                                            pass
                                            # State 95703
                                            if len(subjects) == 0:
                                                pass
                                                # 58: (1/cos(d + x*e))**n2
                                                yield 58, subst2
                                        subjects603.appendleft(tmp633)
                        subjects620.appendleft(tmp630)
                    subjects603.appendleft(tmp619)
                if len(subjects603) >= 1 and isinstance(subjects603[0], sin):
                    tmp634 = subjects603.popleft()
                    subjects635 = deque(tmp634._args)
                    # State 96076
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 96077
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 96078
                            if len(subjects635) >= 1:
                                tmp638 = subjects635.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.0', tmp638)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 96079
                                    if len(subjects635) == 0:
                                        pass
                                        # State 96080
                                        if len(subjects603) >= 1 and subjects603[0] == Integer(-1):
                                            tmp640 = subjects603.popleft()
                                            # State 96081
                                            if len(subjects603) == 0:
                                                pass
                                                # State 96082
                                                if len(subjects) == 0:
                                                    pass
                                                    # 60: (1/sin(d + x*e))**n2
                                                    yield 60, subst4
                                            subjects603.appendleft(tmp640)
                                subjects635.appendleft(tmp638)
                        if len(subjects635) >= 1 and isinstance(subjects635[0], Mul):
                            tmp641 = subjects635.popleft()
                            associative1 = tmp641
                            associative_type1 = type(tmp641)
                            subjects642 = deque(tmp641._args)
                            matcher = CommutativeMatcher96084.get()
                            tmp643 = subjects642
                            subjects642 = []
                            for s in tmp643:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp643, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 96085
                                    if len(subjects635) == 0:
                                        pass
                                        # State 96086
                                        if len(subjects603) >= 1 and subjects603[0] == Integer(-1):
                                            tmp644 = subjects603.popleft()
                                            # State 96087
                                            if len(subjects603) == 0:
                                                pass
                                                # State 96088
                                                if len(subjects) == 0:
                                                    pass
                                                    # 60: (1/sin(d + x*e))**n2
                                                    yield 60, subst3
                                            subjects603.appendleft(tmp644)
                            subjects635.appendleft(tmp641)
                    if len(subjects635) >= 1 and isinstance(subjects635[0], Add):
                        tmp645 = subjects635.popleft()
                        associative1 = tmp645
                        associative_type1 = type(tmp645)
                        subjects646 = deque(tmp645._args)
                        matcher = CommutativeMatcher96090.get()
                        tmp647 = subjects646
                        subjects646 = []
                        for s in tmp647:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp647, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 96096
                                if len(subjects635) == 0:
                                    pass
                                    # State 96097
                                    if len(subjects603) >= 1 and subjects603[0] == Integer(-1):
                                        tmp648 = subjects603.popleft()
                                        # State 96098
                                        if len(subjects603) == 0:
                                            pass
                                            # State 96099
                                            if len(subjects) == 0:
                                                pass
                                                # 60: (1/sin(d + x*e))**n2
                                                yield 60, subst2
                                        subjects603.appendleft(tmp648)
                        subjects635.appendleft(tmp645)
                    subjects603.appendleft(tmp634)
                subjects.appendleft(tmp602)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp649 = subjects.popleft()
            subjects650 = deque(tmp649._args)
            # State 20094
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 20095
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 20096
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 20097
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 20098
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i3.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 20099
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20100
                                    if len(subjects650) >= 1:
                                        tmp657 = subjects650.popleft()
                                        subst7 = Substitution(subst6)
                                        try:
                                            subst7.try_add_variable('i3.1.2.2.2.1.0', tmp657)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20101
                                            if len(subjects650) == 0:
                                                pass
                                                # State 20102
                                                if len(subjects) == 0:
                                                    pass
                                                    # 18: log(c*(d*(e + x*f)**p)**q)
                                                    yield 18, subst7
                                        subjects650.appendleft(tmp657)
                                if len(subjects650) >= 1 and isinstance(subjects650[0], Mul):
                                    tmp659 = subjects650.popleft()
                                    associative1 = tmp659
                                    associative_type1 = type(tmp659)
                                    subjects660 = deque(tmp659._args)
                                    matcher = CommutativeMatcher20104.get()
                                    tmp661 = subjects660
                                    subjects660 = []
                                    for s in tmp661:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp661, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 20105
                                            if len(subjects650) == 0:
                                                pass
                                                # State 20106
                                                if len(subjects) == 0:
                                                    pass
                                                    # 18: log(c*(d*(e + x*f)**p)**q)
                                                    yield 18, subst6
                                    subjects650.appendleft(tmp659)
                            if len(subjects650) >= 1 and isinstance(subjects650[0], Add):
                                tmp662 = subjects650.popleft()
                                associative1 = tmp662
                                associative_type1 = type(tmp662)
                                subjects663 = deque(tmp662._args)
                                matcher = CommutativeMatcher20108.get()
                                tmp664 = subjects663
                                subjects663 = []
                                for s in tmp664:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp664, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 20114
                                        if len(subjects650) == 0:
                                            pass
                                            # State 20115
                                            if len(subjects) == 0:
                                                pass
                                                # 18: log(c*(d*(e + x*f)**p)**q)
                                                yield 18, subst5
                                subjects650.appendleft(tmp662)
                        if len(subjects650) >= 1 and isinstance(subjects650[0], Pow):
                            tmp665 = subjects650.popleft()
                            subjects666 = deque(tmp665._args)
                            # State 20116
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 20117
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20118
                                    if len(subjects666) >= 1:
                                        tmp669 = subjects666.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i3.1.2.2.2.1.0', tmp669)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20119
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i3.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 20120
                                                if len(subjects666) == 0:
                                                    pass
                                                    # State 20121
                                                    if len(subjects650) == 0:
                                                        pass
                                                        # State 20122
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 18: log(c*(d*(e + x*f)**p)**q)
                                                            yield 18, subst7
                                            if len(subjects666) >= 1:
                                                tmp672 = subjects666.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i3.1.2.2.2', tmp672)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 20120
                                                    if len(subjects666) == 0:
                                                        pass
                                                        # State 20121
                                                        if len(subjects650) == 0:
                                                            pass
                                                            # State 20122
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 18: log(c*(d*(e + x*f)**p)**q)
                                                                yield 18, subst7
                                                subjects666.appendleft(tmp672)
                                        subjects666.appendleft(tmp669)
                                if len(subjects666) >= 1 and isinstance(subjects666[0], Mul):
                                    tmp674 = subjects666.popleft()
                                    associative1 = tmp674
                                    associative_type1 = type(tmp674)
                                    subjects675 = deque(tmp674._args)
                                    matcher = CommutativeMatcher20124.get()
                                    tmp676 = subjects675
                                    subjects675 = []
                                    for s in tmp676:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp676, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 20125
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i3.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 20126
                                                if len(subjects666) == 0:
                                                    pass
                                                    # State 20127
                                                    if len(subjects650) == 0:
                                                        pass
                                                        # State 20128
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 18: log(c*(d*(e + x*f)**p)**q)
                                                            yield 18, subst6
                                            if len(subjects666) >= 1:
                                                tmp678 = []
                                                tmp678.append(subjects666.popleft())
                                                while True:
                                                    if len(tmp678) > 1:
                                                        tmp679 = create_operation_expression(associative1, tmp678)
                                                    elif len(tmp678) == 1:
                                                        tmp679 = tmp678[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i3.1.2.2.2', tmp679)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 20126
                                                        if len(subjects666) == 0:
                                                            pass
                                                            # State 20127
                                                            if len(subjects650) == 0:
                                                                pass
                                                                # State 20128
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 18: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 18, subst6
                                                    if len(subjects666) == 0:
                                                        break
                                                    tmp678.append(subjects666.popleft())
                                                subjects666.extendleft(reversed(tmp678))
                                    subjects666.appendleft(tmp674)
                            if len(subjects666) >= 1 and isinstance(subjects666[0], Add):
                                tmp681 = subjects666.popleft()
                                associative1 = tmp681
                                associative_type1 = type(tmp681)
                                subjects682 = deque(tmp681._args)
                                matcher = CommutativeMatcher20130.get()
                                tmp683 = subjects682
                                subjects682 = []
                                for s in tmp683:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp683, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 20136
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20137
                                            if len(subjects666) == 0:
                                                pass
                                                # State 20138
                                                if len(subjects650) == 0:
                                                    pass
                                                    # State 20139
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 18: log(c*(d*(e + x*f)**p)**q)
                                                        yield 18, subst5
                                        if len(subjects666) >= 1:
                                            tmp685 = []
                                            tmp685.append(subjects666.popleft())
                                            while True:
                                                if len(tmp685) > 1:
                                                    tmp686 = create_operation_expression(associative1, tmp685)
                                                elif len(tmp685) == 1:
                                                    tmp686 = tmp685[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.1.2.2.2', tmp686)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 20137
                                                    if len(subjects666) == 0:
                                                        pass
                                                        # State 20138
                                                        if len(subjects650) == 0:
                                                            pass
                                                            # State 20139
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 18: log(c*(d*(e + x*f)**p)**q)
                                                                yield 18, subst5
                                                if len(subjects666) == 0:
                                                    break
                                                tmp685.append(subjects666.popleft())
                                            subjects666.extendleft(reversed(tmp685))
                                subjects666.appendleft(tmp681)
                            subjects650.appendleft(tmp665)
                    if len(subjects650) >= 1:
                        tmp688 = subjects650.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1', tmp688)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53195
                            if len(subjects650) == 0:
                                pass
                                # State 53196
                                if len(subjects) == 0:
                                    pass
                                    # 21: log(c*RFx**p)
                                    yield 21, subst3
                        subjects650.appendleft(tmp688)
                    if len(subjects650) >= 1 and isinstance(subjects650[0], Mul):
                        tmp690 = subjects650.popleft()
                        associative1 = tmp690
                        associative_type1 = type(tmp690)
                        subjects691 = deque(tmp690._args)
                        matcher = CommutativeMatcher20141.get()
                        tmp692 = subjects691
                        subjects691 = []
                        for s in tmp692:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp692, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 20178
                                if len(subjects650) == 0:
                                    pass
                                    # State 20179
                                    if len(subjects) == 0:
                                        pass
                                        # 18: log(c*(d*(e + x*f)**p)**q)
                                        yield 18, subst3
                        subjects650.appendleft(tmp690)
                    if len(subjects650) >= 1 and isinstance(subjects650[0], Add):
                        tmp693 = subjects650.popleft()
                        associative1 = tmp693
                        associative_type1 = type(tmp693)
                        subjects694 = deque(tmp693._args)
                        matcher = CommutativeMatcher50736.get()
                        tmp695 = subjects694
                        subjects694 = []
                        for s in tmp695:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp695, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 50749
                                if len(subjects650) == 0:
                                    pass
                                    # State 50750
                                    if len(subjects) == 0:
                                        pass
                                        # 19: log(c*(d + e*x**2)**p)
                                        yield 19, subst3
                            if pattern_index == 1:
                                pass
                                # State 52940
                                if len(subjects650) == 0:
                                    pass
                                    # State 52941
                                    if len(subjects) == 0:
                                        pass
                                        # 20: log(c*(d + e/(f + x*g))**p)
                                        yield 20, subst3
                        subjects650.appendleft(tmp693)
                if len(subjects650) >= 1 and isinstance(subjects650[0], Pow):
                    tmp696 = subjects650.popleft()
                    subjects697 = deque(tmp696._args)
                    # State 20180
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 20181
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 20182
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 20183
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20184
                                    if len(subjects697) >= 1:
                                        tmp702 = subjects697.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i3.1.2.2.2.1.0', tmp702)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20185
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i3.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 20186
                                                if len(subjects697) == 0:
                                                    pass
                                                    # State 20187
                                                    if len(subjects650) == 0:
                                                        pass
                                                        # State 20188
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 18: log(c*(d*(e + x*f)**p)**q)
                                                            yield 18, subst7
                                            if len(subjects697) >= 1:
                                                tmp705 = subjects697.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i3.1.2.2', tmp705)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 20186
                                                    if len(subjects697) == 0:
                                                        pass
                                                        # State 20187
                                                        if len(subjects650) == 0:
                                                            pass
                                                            # State 20188
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 18: log(c*(d*(e + x*f)**p)**q)
                                                                yield 18, subst7
                                                subjects697.appendleft(tmp705)
                                        subjects697.appendleft(tmp702)
                                if len(subjects697) >= 1 and isinstance(subjects697[0], Mul):
                                    tmp707 = subjects697.popleft()
                                    associative1 = tmp707
                                    associative_type1 = type(tmp707)
                                    subjects708 = deque(tmp707._args)
                                    matcher = CommutativeMatcher20190.get()
                                    tmp709 = subjects708
                                    subjects708 = []
                                    for s in tmp709:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp709, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 20191
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i3.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 20192
                                                if len(subjects697) == 0:
                                                    pass
                                                    # State 20193
                                                    if len(subjects650) == 0:
                                                        pass
                                                        # State 20194
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 18: log(c*(d*(e + x*f)**p)**q)
                                                            yield 18, subst6
                                            if len(subjects697) >= 1:
                                                tmp711 = []
                                                tmp711.append(subjects697.popleft())
                                                while True:
                                                    if len(tmp711) > 1:
                                                        tmp712 = create_operation_expression(associative1, tmp711)
                                                    elif len(tmp711) == 1:
                                                        tmp712 = tmp711[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i3.1.2.2', tmp712)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 20192
                                                        if len(subjects697) == 0:
                                                            pass
                                                            # State 20193
                                                            if len(subjects650) == 0:
                                                                pass
                                                                # State 20194
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 18: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 18, subst6
                                                    if len(subjects697) == 0:
                                                        break
                                                    tmp711.append(subjects697.popleft())
                                                subjects697.extendleft(reversed(tmp711))
                                    subjects697.appendleft(tmp707)
                            if len(subjects697) >= 1 and isinstance(subjects697[0], Add):
                                tmp714 = subjects697.popleft()
                                associative1 = tmp714
                                associative_type1 = type(tmp714)
                                subjects715 = deque(tmp714._args)
                                matcher = CommutativeMatcher20196.get()
                                tmp716 = subjects715
                                subjects715 = []
                                for s in tmp716:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp716, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 20202
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20203
                                            if len(subjects697) == 0:
                                                pass
                                                # State 20204
                                                if len(subjects650) == 0:
                                                    pass
                                                    # State 20205
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 18: log(c*(d*(e + x*f)**p)**q)
                                                        yield 18, subst5
                                        if len(subjects697) >= 1:
                                            tmp718 = []
                                            tmp718.append(subjects697.popleft())
                                            while True:
                                                if len(tmp718) > 1:
                                                    tmp719 = create_operation_expression(associative1, tmp718)
                                                elif len(tmp718) == 1:
                                                    tmp719 = tmp718[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.1.2.2', tmp719)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 20203
                                                    if len(subjects697) == 0:
                                                        pass
                                                        # State 20204
                                                        if len(subjects650) == 0:
                                                            pass
                                                            # State 20205
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 18: log(c*(d*(e + x*f)**p)**q)
                                                                yield 18, subst5
                                                if len(subjects697) == 0:
                                                    break
                                                tmp718.append(subjects697.popleft())
                                            subjects697.extendleft(reversed(tmp718))
                                subjects697.appendleft(tmp714)
                        if len(subjects697) >= 1 and isinstance(subjects697[0], Pow):
                            tmp721 = subjects697.popleft()
                            subjects722 = deque(tmp721._args)
                            # State 20206
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 20207
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20208
                                    if len(subjects722) >= 1:
                                        tmp725 = subjects722.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.2.2.1.0', tmp725)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20209
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i3.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 20210
                                                if len(subjects722) == 0:
                                                    pass
                                                    # State 20211
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i3.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 20212
                                                        if len(subjects697) == 0:
                                                            pass
                                                            # State 20213
                                                            if len(subjects650) == 0:
                                                                pass
                                                                # State 20214
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 18: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 18, subst7
                                                    if len(subjects697) >= 1:
                                                        tmp729 = subjects697.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i3.1.2.2', tmp729)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 20212
                                                            if len(subjects697) == 0:
                                                                pass
                                                                # State 20213
                                                                if len(subjects650) == 0:
                                                                    pass
                                                                    # State 20214
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 18: log(c*(d*(e + x*f)**p)**q)
                                                                        yield 18, subst7
                                                        subjects697.appendleft(tmp729)
                                            if len(subjects722) >= 1:
                                                tmp731 = subjects722.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i3.1.2.2.2', tmp731)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 20210
                                                    if len(subjects722) == 0:
                                                        pass
                                                        # State 20211
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i3.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 20212
                                                            if len(subjects697) == 0:
                                                                pass
                                                                # State 20213
                                                                if len(subjects650) == 0:
                                                                    pass
                                                                    # State 20214
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 18: log(c*(d*(e + x*f)**p)**q)
                                                                        yield 18, subst7
                                                        if len(subjects697) >= 1:
                                                            tmp734 = subjects697.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i3.1.2.2', tmp734)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 20212
                                                                if len(subjects697) == 0:
                                                                    pass
                                                                    # State 20213
                                                                    if len(subjects650) == 0:
                                                                        pass
                                                                        # State 20214
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 18: log(c*(d*(e + x*f)**p)**q)
                                                                            yield 18, subst7
                                                            subjects697.appendleft(tmp734)
                                                subjects722.appendleft(tmp731)
                                        subjects722.appendleft(tmp725)
                                if len(subjects722) >= 1 and isinstance(subjects722[0], Mul):
                                    tmp736 = subjects722.popleft()
                                    associative1 = tmp736
                                    associative_type1 = type(tmp736)
                                    subjects737 = deque(tmp736._args)
                                    matcher = CommutativeMatcher20216.get()
                                    tmp738 = subjects737
                                    subjects737 = []
                                    for s in tmp738:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp738, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 20217
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 20218
                                                if len(subjects722) == 0:
                                                    pass
                                                    # State 20219
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i3.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 20220
                                                        if len(subjects697) == 0:
                                                            pass
                                                            # State 20221
                                                            if len(subjects650) == 0:
                                                                pass
                                                                # State 20222
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 18: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 18, subst6
                                                    if len(subjects697) >= 1:
                                                        tmp741 = subjects697.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i3.1.2.2', tmp741)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 20220
                                                            if len(subjects697) == 0:
                                                                pass
                                                                # State 20221
                                                                if len(subjects650) == 0:
                                                                    pass
                                                                    # State 20222
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 18: log(c*(d*(e + x*f)**p)**q)
                                                                        yield 18, subst6
                                                        subjects697.appendleft(tmp741)
                                            if len(subjects722) >= 1:
                                                tmp743 = []
                                                tmp743.append(subjects722.popleft())
                                                while True:
                                                    if len(tmp743) > 1:
                                                        tmp744 = create_operation_expression(associative1, tmp743)
                                                    elif len(tmp743) == 1:
                                                        tmp744 = tmp743[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.2.2.2', tmp744)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 20218
                                                        if len(subjects722) == 0:
                                                            pass
                                                            # State 20219
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i3.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 20220
                                                                if len(subjects697) == 0:
                                                                    pass
                                                                    # State 20221
                                                                    if len(subjects650) == 0:
                                                                        pass
                                                                        # State 20222
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 18: log(c*(d*(e + x*f)**p)**q)
                                                                            yield 18, subst6
                                                            if len(subjects697) >= 1:
                                                                tmp747 = subjects697.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i3.1.2.2', tmp747)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 20220
                                                                    if len(subjects697) == 0:
                                                                        pass
                                                                        # State 20221
                                                                        if len(subjects650) == 0:
                                                                            pass
                                                                            # State 20222
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 18: log(c*(d*(e + x*f)**p)**q)
                                                                                yield 18, subst6
                                                                subjects697.appendleft(tmp747)
                                                    if len(subjects722) == 0:
                                                        break
                                                    tmp743.append(subjects722.popleft())
                                                subjects722.extendleft(reversed(tmp743))
                                    subjects722.appendleft(tmp736)
                            if len(subjects722) >= 1 and isinstance(subjects722[0], Add):
                                tmp749 = subjects722.popleft()
                                associative1 = tmp749
                                associative_type1 = type(tmp749)
                                subjects750 = deque(tmp749._args)
                                matcher = CommutativeMatcher20224.get()
                                tmp751 = subjects750
                                subjects750 = []
                                for s in tmp751:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp751, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 20230
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20231
                                            if len(subjects722) == 0:
                                                pass
                                                # State 20232
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 20233
                                                    if len(subjects697) == 0:
                                                        pass
                                                        # State 20234
                                                        if len(subjects650) == 0:
                                                            pass
                                                            # State 20235
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 18: log(c*(d*(e + x*f)**p)**q)
                                                                yield 18, subst5
                                                if len(subjects697) >= 1:
                                                    tmp754 = subjects697.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.2.2', tmp754)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 20233
                                                        if len(subjects697) == 0:
                                                            pass
                                                            # State 20234
                                                            if len(subjects650) == 0:
                                                                pass
                                                                # State 20235
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 18: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 18, subst5
                                                    subjects697.appendleft(tmp754)
                                        if len(subjects722) >= 1:
                                            tmp756 = []
                                            tmp756.append(subjects722.popleft())
                                            while True:
                                                if len(tmp756) > 1:
                                                    tmp757 = create_operation_expression(associative1, tmp756)
                                                elif len(tmp756) == 1:
                                                    tmp757 = tmp756[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.2.2.2', tmp757)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 20231
                                                    if len(subjects722) == 0:
                                                        pass
                                                        # State 20232
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 20233
                                                            if len(subjects697) == 0:
                                                                pass
                                                                # State 20234
                                                                if len(subjects650) == 0:
                                                                    pass
                                                                    # State 20235
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 18: log(c*(d*(e + x*f)**p)**q)
                                                                        yield 18, subst5
                                                        if len(subjects697) >= 1:
                                                            tmp760 = subjects697.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i3.1.2.2', tmp760)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 20233
                                                                if len(subjects697) == 0:
                                                                    pass
                                                                    # State 20234
                                                                    if len(subjects650) == 0:
                                                                        pass
                                                                        # State 20235
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 18: log(c*(d*(e + x*f)**p)**q)
                                                                            yield 18, subst5
                                                            subjects697.appendleft(tmp760)
                                                if len(subjects722) == 0:
                                                    break
                                                tmp756.append(subjects722.popleft())
                                            subjects722.extendleft(reversed(tmp756))
                                subjects722.appendleft(tmp749)
                            subjects697.appendleft(tmp721)
                    if len(subjects697) >= 1:
                        tmp762 = subjects697.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.1', tmp762)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53197
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53198
                                if len(subjects697) == 0:
                                    pass
                                    # State 53199
                                    if len(subjects650) == 0:
                                        pass
                                        # State 53200
                                        if len(subjects) == 0:
                                            pass
                                            # 21: log(c*RFx**p)
                                            yield 21, subst3
                            if len(subjects697) >= 1:
                                tmp765 = subjects697.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', tmp765)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53198
                                    if len(subjects697) == 0:
                                        pass
                                        # State 53199
                                        if len(subjects650) == 0:
                                            pass
                                            # State 53200
                                            if len(subjects) == 0:
                                                pass
                                                # 21: log(c*RFx**p)
                                                yield 21, subst3
                                subjects697.appendleft(tmp765)
                        subjects697.appendleft(tmp762)
                    if len(subjects697) >= 1 and isinstance(subjects697[0], Mul):
                        tmp767 = subjects697.popleft()
                        associative1 = tmp767
                        associative_type1 = type(tmp767)
                        subjects768 = deque(tmp767._args)
                        matcher = CommutativeMatcher20237.get()
                        tmp769 = subjects768
                        subjects768 = []
                        for s in tmp769:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp769, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 20274
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 20275
                                    if len(subjects697) == 0:
                                        pass
                                        # State 20276
                                        if len(subjects650) == 0:
                                            pass
                                            # State 20277
                                            if len(subjects) == 0:
                                                pass
                                                # 18: log(c*(d*(e + x*f)**p)**q)
                                                yield 18, subst3
                                if len(subjects697) >= 1:
                                    tmp771 = []
                                    tmp771.append(subjects697.popleft())
                                    while True:
                                        if len(tmp771) > 1:
                                            tmp772 = create_operation_expression(associative1, tmp771)
                                        elif len(tmp771) == 1:
                                            tmp772 = tmp771[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2.2', tmp772)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 20275
                                            if len(subjects697) == 0:
                                                pass
                                                # State 20276
                                                if len(subjects650) == 0:
                                                    pass
                                                    # State 20277
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 18: log(c*(d*(e + x*f)**p)**q)
                                                        yield 18, subst3
                                        if len(subjects697) == 0:
                                            break
                                        tmp771.append(subjects697.popleft())
                                    subjects697.extendleft(reversed(tmp771))
                        subjects697.appendleft(tmp767)
                    if len(subjects697) >= 1 and isinstance(subjects697[0], Add):
                        tmp774 = subjects697.popleft()
                        associative1 = tmp774
                        associative_type1 = type(tmp774)
                        subjects775 = deque(tmp774._args)
                        matcher = CommutativeMatcher50752.get()
                        tmp776 = subjects775
                        subjects775 = []
                        for s in tmp776:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp776, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 50765
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 50766
                                    if len(subjects697) == 0:
                                        pass
                                        # State 50767
                                        if len(subjects650) == 0:
                                            pass
                                            # State 50768
                                            if len(subjects) == 0:
                                                pass
                                                # 19: log(c*(d + e*x**2)**p)
                                                yield 19, subst3
                                if len(subjects697) >= 1:
                                    tmp778 = []
                                    tmp778.append(subjects697.popleft())
                                    while True:
                                        if len(tmp778) > 1:
                                            tmp779 = create_operation_expression(associative1, tmp778)
                                        elif len(tmp778) == 1:
                                            tmp779 = tmp778[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2.2', tmp779)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 50766
                                            if len(subjects697) == 0:
                                                pass
                                                # State 50767
                                                if len(subjects650) == 0:
                                                    pass
                                                    # State 50768
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 19: log(c*(d + e*x**2)**p)
                                                        yield 19, subst3
                                        if len(subjects697) == 0:
                                            break
                                        tmp778.append(subjects697.popleft())
                                    subjects697.extendleft(reversed(tmp778))
                            if pattern_index == 1:
                                pass
                                # State 52983
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 52984
                                    if len(subjects697) == 0:
                                        pass
                                        # State 52985
                                        if len(subjects650) == 0:
                                            pass
                                            # State 52986
                                            if len(subjects) == 0:
                                                pass
                                                # 20: log(c*(d + e/(f + x*g))**p)
                                                yield 20, subst3
                                if len(subjects697) >= 1:
                                    tmp782 = []
                                    tmp782.append(subjects697.popleft())
                                    while True:
                                        if len(tmp782) > 1:
                                            tmp783 = create_operation_expression(associative1, tmp782)
                                        elif len(tmp782) == 1:
                                            tmp783 = tmp782[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2.2', tmp783)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 52984
                                            if len(subjects697) == 0:
                                                pass
                                                # State 52985
                                                if len(subjects650) == 0:
                                                    pass
                                                    # State 52986
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 20: log(c*(d + e/(f + x*g))**p)
                                                        yield 20, subst3
                                        if len(subjects697) == 0:
                                            break
                                        tmp782.append(subjects697.popleft())
                                    subjects697.extendleft(reversed(tmp782))
                        subjects697.appendleft(tmp774)
                    subjects650.appendleft(tmp696)
            if len(subjects650) >= 1 and isinstance(subjects650[0], Mul):
                tmp785 = subjects650.popleft()
                associative1 = tmp785
                associative_type1 = type(tmp785)
                subjects786 = deque(tmp785._args)
                matcher = CommutativeMatcher20279.get()
                tmp787 = subjects786
                subjects786 = []
                for s in tmp787:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp787, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 20448
                        if len(subjects650) == 0:
                            pass
                            # State 20449
                            if len(subjects) == 0:
                                pass
                                # 18: log(c*(d*(e + x*f)**p)**q)
                                yield 18, subst1
                    if pattern_index == 1:
                        pass
                        # State 50801
                        if len(subjects650) == 0:
                            pass
                            # State 50802
                            if len(subjects) == 0:
                                pass
                                # 19: log(c*(d + e*x**2)**p)
                                yield 19, subst1
                    if pattern_index == 2:
                        pass
                        # State 53073
                        if len(subjects650) == 0:
                            pass
                            # State 53074
                            if len(subjects) == 0:
                                pass
                                # 20: log(c*(d + e/(f + x*g))**p)
                                yield 20, subst1
                    if pattern_index == 3:
                        pass
                        # State 53205
                        if len(subjects650) == 0:
                            pass
                            # State 53206
                            if len(subjects) == 0:
                                pass
                                # 21: log(c*RFx**p)
                                yield 21, subst1
                subjects650.appendleft(tmp785)
            subjects.appendleft(tmp649)
        if len(subjects) >= 1 and subjects[0] == LambertW(Add(Symbol('a'), Mul(Symbol('b'), Symbol('x')))):
            tmp788 = subjects.popleft()
            # State 56774
            if len(subjects) == 0:
                pass
                # 22: LambertW(a + b*x)
                yield 22, subst0
            subjects.appendleft(tmp788)
        if len(subjects) >= 1 and subjects[0] == LambertW(Mul(Symbol('a'), Pow(Symbol('x'), Symbol('n')))):
            tmp789 = subjects.popleft()
            # State 56843
            if len(subjects) == 0:
                pass
                # 23: LambertW(a*x**n)
                yield 23, subst0
            subjects.appendleft(tmp789)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp790 = subjects.popleft()
            subjects791 = deque(tmp790._args)
            # State 58090
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 58091
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 58092
                    if len(subjects791) >= 1:
                        tmp794 = subjects791.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1.0', tmp794)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 58093
                            if len(subjects791) == 0:
                                pass
                                # State 58094
                                if len(subjects) == 0:
                                    pass
                                    # 24: sin(c + x*d)
                                    yield 24, subst3
                        subjects791.appendleft(tmp794)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 72742
                    if len(subjects791) >= 1 and isinstance(subjects791[0], Pow):
                        tmp797 = subjects791.popleft()
                        subjects798 = deque(tmp797._args)
                        # State 72743
                        if len(subjects798) >= 1:
                            tmp799 = subjects798.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp799)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 72744
                                if len(subjects798) >= 1:
                                    tmp801 = subjects798.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp801)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 72745
                                        if len(subjects798) == 0:
                                            pass
                                            # State 72746
                                            if len(subjects791) == 0:
                                                pass
                                                # State 72747
                                                if len(subjects) == 0:
                                                    pass
                                                    # 38: sin(c + d*x**n)
                                                    yield 38, subst4
                                    subjects798.appendleft(tmp801)
                            subjects798.appendleft(tmp799)
                        subjects791.appendleft(tmp797)
                if len(subjects791) >= 1 and isinstance(subjects791[0], Mul):
                    tmp803 = subjects791.popleft()
                    associative1 = tmp803
                    associative_type1 = type(tmp803)
                    subjects804 = deque(tmp803._args)
                    matcher = CommutativeMatcher58096.get()
                    tmp805 = subjects804
                    subjects804 = []
                    for s in tmp805:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp805, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 58097
                            if len(subjects791) == 0:
                                pass
                                # State 58098
                                if len(subjects) == 0:
                                    pass
                                    # 24: sin(c + x*d)
                                    yield 24, subst2
                        if pattern_index == 1:
                            pass
                            # State 72752
                            if len(subjects791) == 0:
                                pass
                                # State 72753
                                if len(subjects) == 0:
                                    pass
                                    # 38: sin(c + d*x**n)
                                    yield 38, subst2
                    subjects791.appendleft(tmp803)
            if len(subjects791) >= 1:
                tmp806 = subjects791.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp806)
                except ValueError:
                    pass
                else:
                    pass
                    # State 73533
                    if len(subjects791) == 0:
                        pass
                        # State 73534
                        if len(subjects) == 0:
                            pass
                            # 40: sin(u)
                            yield 40, subst1
                subjects791.appendleft(tmp806)
            if len(subjects791) >= 1 and isinstance(subjects791[0], Add):
                tmp808 = subjects791.popleft()
                associative1 = tmp808
                associative_type1 = type(tmp808)
                subjects809 = deque(tmp808._args)
                matcher = CommutativeMatcher58100.get()
                tmp810 = subjects809
                subjects809 = []
                for s in tmp810:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp810, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 58106
                        if len(subjects791) == 0:
                            pass
                            # State 58107
                            if len(subjects) == 0:
                                pass
                                # 24: sin(c + x*d)
                                yield 24, subst1
                    if pattern_index == 1:
                        pass
                        # State 72764
                        if len(subjects791) == 0:
                            pass
                            # State 72765
                            if len(subjects) == 0:
                                pass
                                # 38: sin(c + d*x**n)
                                yield 38, subst1
                subjects791.appendleft(tmp808)
            subjects.appendleft(tmp790)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp811 = subjects.popleft()
            subjects812 = deque(tmp811._args)
            # State 58132
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 58133
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 58134
                    if len(subjects812) >= 1:
                        tmp815 = subjects812.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1.0', tmp815)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 58135
                            if len(subjects812) == 0:
                                pass
                                # State 58136
                                if len(subjects) == 0:
                                    pass
                                    # 25: cos(c + x*d)
                                    yield 25, subst3
                        subjects812.appendleft(tmp815)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 72877
                    if len(subjects812) >= 1 and isinstance(subjects812[0], Pow):
                        tmp818 = subjects812.popleft()
                        subjects819 = deque(tmp818._args)
                        # State 72878
                        if len(subjects819) >= 1:
                            tmp820 = subjects819.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp820)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 72879
                                if len(subjects819) >= 1:
                                    tmp822 = subjects819.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp822)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 72880
                                        if len(subjects819) == 0:
                                            pass
                                            # State 72881
                                            if len(subjects812) == 0:
                                                pass
                                                # State 72882
                                                if len(subjects) == 0:
                                                    pass
                                                    # 39: cos(c + d*x**n)
                                                    yield 39, subst4
                                    subjects819.appendleft(tmp822)
                            subjects819.appendleft(tmp820)
                        subjects812.appendleft(tmp818)
                if len(subjects812) >= 1 and isinstance(subjects812[0], Mul):
                    tmp824 = subjects812.popleft()
                    associative1 = tmp824
                    associative_type1 = type(tmp824)
                    subjects825 = deque(tmp824._args)
                    matcher = CommutativeMatcher58138.get()
                    tmp826 = subjects825
                    subjects825 = []
                    for s in tmp826:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp826, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 58139
                            if len(subjects812) == 0:
                                pass
                                # State 58140
                                if len(subjects) == 0:
                                    pass
                                    # 25: cos(c + x*d)
                                    yield 25, subst2
                        if pattern_index == 1:
                            pass
                            # State 72887
                            if len(subjects812) == 0:
                                pass
                                # State 72888
                                if len(subjects) == 0:
                                    pass
                                    # 39: cos(c + d*x**n)
                                    yield 39, subst2
                    subjects812.appendleft(tmp824)
            if len(subjects812) >= 1:
                tmp827 = subjects812.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp827)
                except ValueError:
                    pass
                else:
                    pass
                    # State 73573
                    if len(subjects812) == 0:
                        pass
                        # State 73574
                        if len(subjects) == 0:
                            pass
                            # 41: cos(u)
                            yield 41, subst1
                subjects812.appendleft(tmp827)
            if len(subjects812) >= 1 and isinstance(subjects812[0], Add):
                tmp829 = subjects812.popleft()
                associative1 = tmp829
                associative_type1 = type(tmp829)
                subjects830 = deque(tmp829._args)
                matcher = CommutativeMatcher58142.get()
                tmp831 = subjects830
                subjects830 = []
                for s in tmp831:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp831, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 58148
                        if len(subjects812) == 0:
                            pass
                            # State 58149
                            if len(subjects) == 0:
                                pass
                                # 25: cos(c + x*d)
                                yield 25, subst1
                    if pattern_index == 1:
                        pass
                        # State 72899
                        if len(subjects812) == 0:
                            pass
                            # State 72900
                            if len(subjects) == 0:
                                pass
                                # 39: cos(c + d*x**n)
                                yield 39, subst1
                subjects812.appendleft(tmp829)
            subjects.appendleft(tmp811)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp832 = subjects.popleft()
            subjects833 = deque(tmp832._args)
            # State 67156
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 67157
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 67158
                    if len(subjects833) >= 1:
                        tmp836 = subjects833.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0', tmp836)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 67159
                            if len(subjects833) == 0:
                                pass
                                # State 67160
                                if len(subjects) == 0:
                                    pass
                                    # 27: tan(d + x*e)
                                    yield 27, subst3
                        subjects833.appendleft(tmp836)
                if len(subjects833) >= 1 and isinstance(subjects833[0], Mul):
                    tmp838 = subjects833.popleft()
                    associative1 = tmp838
                    associative_type1 = type(tmp838)
                    subjects839 = deque(tmp838._args)
                    matcher = CommutativeMatcher67162.get()
                    tmp840 = subjects839
                    subjects839 = []
                    for s in tmp840:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp840, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 67163
                            if len(subjects833) == 0:
                                pass
                                # State 67164
                                if len(subjects) == 0:
                                    pass
                                    # 27: tan(d + x*e)
                                    yield 27, subst2
                    subjects833.appendleft(tmp838)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 77469
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 77470
                    if len(subjects833) >= 1:
                        tmp843 = subjects833.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1.0', tmp843)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 77471
                            if len(subjects833) == 0:
                                pass
                                # State 77472
                                if len(subjects) == 0:
                                    pass
                                    # 42: tan(c + x*d)
                                    yield 42, subst3
                        subjects833.appendleft(tmp843)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 87333
                    if len(subjects833) >= 1 and isinstance(subjects833[0], Pow):
                        tmp846 = subjects833.popleft()
                        subjects847 = deque(tmp846._args)
                        # State 87334
                        if len(subjects847) >= 1:
                            tmp848 = subjects847.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp848)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 87335
                                if len(subjects847) >= 1:
                                    tmp850 = subjects847.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp850)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 87336
                                        if len(subjects847) == 0:
                                            pass
                                            # State 87337
                                            if len(subjects833) == 0:
                                                pass
                                                # State 87338
                                                if len(subjects) == 0:
                                                    pass
                                                    # 51: tan(c + d*x**n)
                                                    yield 51, subst4
                                    subjects847.appendleft(tmp850)
                            subjects847.appendleft(tmp848)
                        subjects833.appendleft(tmp846)
                if len(subjects833) >= 1 and isinstance(subjects833[0], Mul):
                    tmp852 = subjects833.popleft()
                    associative1 = tmp852
                    associative_type1 = type(tmp852)
                    subjects853 = deque(tmp852._args)
                    matcher = CommutativeMatcher77474.get()
                    tmp854 = subjects853
                    subjects853 = []
                    for s in tmp854:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp854, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 77475
                            if len(subjects833) == 0:
                                pass
                                # State 77476
                                if len(subjects) == 0:
                                    pass
                                    # 42: tan(c + x*d)
                                    yield 42, subst2
                        if pattern_index == 1:
                            pass
                            # State 87343
                            if len(subjects833) == 0:
                                pass
                                # State 87344
                                if len(subjects) == 0:
                                    pass
                                    # 51: tan(c + d*x**n)
                                    yield 51, subst2
                    subjects833.appendleft(tmp852)
            if len(subjects833) >= 1:
                tmp855 = subjects833.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp855)
                except ValueError:
                    pass
                else:
                    pass
                    # State 87871
                    if len(subjects833) == 0:
                        pass
                        # State 87872
                        if len(subjects) == 0:
                            pass
                            # 53: tan(u)
                            yield 53, subst1
                subjects833.appendleft(tmp855)
            if len(subjects833) >= 1 and isinstance(subjects833[0], Add):
                tmp857 = subjects833.popleft()
                associative1 = tmp857
                associative_type1 = type(tmp857)
                subjects858 = deque(tmp857._args)
                matcher = CommutativeMatcher67166.get()
                tmp859 = subjects858
                subjects858 = []
                for s in tmp859:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp859, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 67172
                        if len(subjects833) == 0:
                            pass
                            # State 67173
                            if len(subjects) == 0:
                                pass
                                # 27: tan(d + x*e)
                                yield 27, subst1
                    if pattern_index == 1:
                        pass
                        # State 77480
                        if len(subjects833) == 0:
                            pass
                            # State 77481
                            if len(subjects) == 0:
                                pass
                                # 42: tan(c + x*d)
                                yield 42, subst1
                    if pattern_index == 2:
                        pass
                        # State 87355
                        if len(subjects833) == 0:
                            pass
                            # State 87356
                            if len(subjects) == 0:
                                pass
                                # 51: tan(c + d*x**n)
                                yield 51, subst1
                subjects833.appendleft(tmp857)
            subjects.appendleft(tmp832)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp860 = subjects.popleft()
            subjects861 = deque(tmp860._args)
            # State 108035
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108036
                if len(subjects861) >= 1:
                    tmp863 = subjects861.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp863)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108037
                        if len(subjects861) == 0:
                            pass
                            # State 108038
                            if len(subjects) == 0:
                                pass
                                # 66: asin(x*c)
                                yield 66, subst2
                    subjects861.appendleft(tmp863)
            if len(subjects861) >= 1 and isinstance(subjects861[0], Mul):
                tmp865 = subjects861.popleft()
                associative1 = tmp865
                associative_type1 = type(tmp865)
                subjects866 = deque(tmp865._args)
                matcher = CommutativeMatcher108040.get()
                tmp867 = subjects866
                subjects866 = []
                for s in tmp867:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp867, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108041
                        if len(subjects861) == 0:
                            pass
                            # State 108042
                            if len(subjects) == 0:
                                pass
                                # 66: asin(x*c)
                                yield 66, subst1
                subjects861.appendleft(tmp865)
            if len(subjects861) >= 1 and isinstance(subjects861[0], Add):
                tmp868 = subjects861.popleft()
                associative1 = tmp868
                associative_type1 = type(tmp868)
                subjects869 = deque(tmp868._args)
                matcher = CommutativeMatcher110336.get()
                tmp870 = subjects869
                subjects869 = []
                for s in tmp870:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp870, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110342
                        if len(subjects861) == 0:
                            pass
                            # State 110343
                            if len(subjects) == 0:
                                pass
                                # 68: asin(c + x*d)
                                yield 68, subst1
                    if pattern_index == 1:
                        pass
                        # State 110728
                        if len(subjects861) == 0:
                            pass
                            # State 110729
                            if len(subjects) == 0:
                                pass
                                # 70: asin(c + d*x**2)
                                yield 70, subst1
                subjects861.appendleft(tmp868)
            subjects.appendleft(tmp860)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp871 = subjects.popleft()
            subjects872 = deque(tmp871._args)
            # State 108129
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108130
                if len(subjects872) >= 1:
                    tmp874 = subjects872.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp874)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108131
                        if len(subjects872) == 0:
                            pass
                            # State 108132
                            if len(subjects) == 0:
                                pass
                                # 67: acos(x*c)
                                yield 67, subst2
                    subjects872.appendleft(tmp874)
            if len(subjects872) >= 1 and isinstance(subjects872[0], Mul):
                tmp876 = subjects872.popleft()
                associative1 = tmp876
                associative_type1 = type(tmp876)
                subjects877 = deque(tmp876._args)
                matcher = CommutativeMatcher108134.get()
                tmp878 = subjects877
                subjects877 = []
                for s in tmp878:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp878, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108135
                        if len(subjects872) == 0:
                            pass
                            # State 108136
                            if len(subjects) == 0:
                                pass
                                # 67: acos(x*c)
                                yield 67, subst1
                subjects872.appendleft(tmp876)
            if len(subjects872) >= 1 and isinstance(subjects872[0], Add):
                tmp879 = subjects872.popleft()
                associative1 = tmp879
                associative_type1 = type(tmp879)
                subjects880 = deque(tmp879._args)
                matcher = CommutativeMatcher110432.get()
                tmp881 = subjects880
                subjects880 = []
                for s in tmp881:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp881, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110438
                        if len(subjects872) == 0:
                            pass
                            # State 110439
                            if len(subjects) == 0:
                                pass
                                # 69: acos(c + x*d)
                                yield 69, subst1
                    if pattern_index == 1:
                        pass
                        # State 110795
                        if len(subjects872) == 0:
                            pass
                            # State 110796
                            if len(subjects) == 0:
                                pass
                                # 71: acos(d*x**2 + 1)
                                yield 71, subst1
                    if pattern_index == 2:
                        pass
                        # State 110822
                        if len(subjects872) == 0:
                            pass
                            # State 110823
                            if len(subjects) == 0:
                                pass
                                # 72: acos(d*x**2 - 1)
                                yield 72, subst1
                    if pattern_index == 3:
                        pass
                        # State 110857
                        if len(subjects872) == 0:
                            pass
                            # State 110858
                            if len(subjects) == 0:
                                pass
                                # 73: acos(c + d*x**2)
                                yield 73, subst1
                subjects872.appendleft(tmp879)
            subjects.appendleft(tmp871)
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp882 = subjects.popleft()
            subjects883 = deque(tmp882._args)
            # State 112670
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 112671
                if len(subjects883) >= 1:
                    tmp885 = subjects883.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp885)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112672
                        if len(subjects883) == 0:
                            pass
                            # State 112673
                            if len(subjects) == 0:
                                pass
                                # 74: atan(x*c)
                                yield 74, subst2
                    subjects883.appendleft(tmp885)
            if len(subjects883) >= 1 and isinstance(subjects883[0], Mul):
                tmp887 = subjects883.popleft()
                associative1 = tmp887
                associative_type1 = type(tmp887)
                subjects888 = deque(tmp887._args)
                matcher = CommutativeMatcher112675.get()
                tmp889 = subjects888
                subjects888 = []
                for s in tmp889:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp889, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 112676
                        if len(subjects883) == 0:
                            pass
                            # State 112677
                            if len(subjects) == 0:
                                pass
                                # 74: atan(x*c)
                                yield 74, subst1
                subjects883.appendleft(tmp887)
            if len(subjects883) >= 1 and isinstance(subjects883[0], Add):
                tmp890 = subjects883.popleft()
                associative1 = tmp890
                associative_type1 = type(tmp890)
                subjects891 = deque(tmp890._args)
                matcher = CommutativeMatcher115534.get()
                tmp892 = subjects891
                subjects891 = []
                for s in tmp892:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp892, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115540
                        if len(subjects883) == 0:
                            pass
                            # State 115541
                            if len(subjects) == 0:
                                pass
                                # 76: atan(c + x*d)
                                yield 76, subst1
                subjects883.appendleft(tmp890)
            subjects.appendleft(tmp882)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp893 = subjects.popleft()
            subjects894 = deque(tmp893._args)
            # State 112764
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 112765
                if len(subjects894) >= 1:
                    tmp896 = subjects894.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp896)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112766
                        if len(subjects894) == 0:
                            pass
                            # State 112767
                            if len(subjects) == 0:
                                pass
                                # 75: acot(x*c)
                                yield 75, subst2
                    subjects894.appendleft(tmp896)
            if len(subjects894) >= 1 and isinstance(subjects894[0], Mul):
                tmp898 = subjects894.popleft()
                associative1 = tmp898
                associative_type1 = type(tmp898)
                subjects899 = deque(tmp898._args)
                matcher = CommutativeMatcher112769.get()
                tmp900 = subjects899
                subjects899 = []
                for s in tmp900:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp900, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 112770
                        if len(subjects894) == 0:
                            pass
                            # State 112771
                            if len(subjects) == 0:
                                pass
                                # 75: acot(x*c)
                                yield 75, subst1
                subjects894.appendleft(tmp898)
            if len(subjects894) >= 1 and isinstance(subjects894[0], Add):
                tmp901 = subjects894.popleft()
                associative1 = tmp901
                associative_type1 = type(tmp901)
                subjects902 = deque(tmp901._args)
                matcher = CommutativeMatcher115630.get()
                tmp903 = subjects902
                subjects902 = []
                for s in tmp903:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp903, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115636
                        if len(subjects894) == 0:
                            pass
                            # State 115637
                            if len(subjects) == 0:
                                pass
                                # 77: acot(c + x*d)
                                yield 77, subst1
                subjects894.appendleft(tmp901)
            subjects.appendleft(tmp893)
        if len(subjects) >= 1 and isinstance(subjects[0], asec):
            tmp904 = subjects.popleft()
            subjects905 = deque(tmp904._args)
            # State 119564
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119565
                if len(subjects905) >= 1:
                    tmp907 = subjects905.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp907)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119566
                        if len(subjects905) == 0:
                            pass
                            # State 119567
                            if len(subjects) == 0:
                                pass
                                # 78: asec(x*c)
                                yield 78, subst2
                    subjects905.appendleft(tmp907)
            if len(subjects905) >= 1 and isinstance(subjects905[0], Mul):
                tmp909 = subjects905.popleft()
                associative1 = tmp909
                associative_type1 = type(tmp909)
                subjects910 = deque(tmp909._args)
                matcher = CommutativeMatcher119569.get()
                tmp911 = subjects910
                subjects910 = []
                for s in tmp911:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp911, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119570
                        if len(subjects905) == 0:
                            pass
                            # State 119571
                            if len(subjects) == 0:
                                pass
                                # 78: asec(x*c)
                                yield 78, subst1
                subjects905.appendleft(tmp909)
            subjects.appendleft(tmp904)
        if len(subjects) >= 1 and isinstance(subjects[0], acsc):
            tmp912 = subjects.popleft()
            subjects913 = deque(tmp912._args)
            # State 119615
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119616
                if len(subjects913) >= 1:
                    tmp915 = subjects913.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp915)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119617
                        if len(subjects913) == 0:
                            pass
                            # State 119618
                            if len(subjects) == 0:
                                pass
                                # 79: acsc(x*c)
                                yield 79, subst2
                    subjects913.appendleft(tmp915)
            if len(subjects913) >= 1 and isinstance(subjects913[0], Mul):
                tmp917 = subjects913.popleft()
                associative1 = tmp917
                associative_type1 = type(tmp917)
                subjects918 = deque(tmp917._args)
                matcher = CommutativeMatcher119620.get()
                tmp919 = subjects918
                subjects918 = []
                for s in tmp919:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp919, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119621
                        if len(subjects913) == 0:
                            pass
                            # State 119622
                            if len(subjects) == 0:
                                pass
                                # 79: acsc(x*c)
                                yield 79, subst1
                subjects913.appendleft(tmp917)
            subjects.appendleft(tmp912)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp920 = subjects.popleft()
            subjects921 = deque(tmp920._args)
            # State 122579
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 122580
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122581
                    if len(subjects921) >= 1 and isinstance(subjects921[0], Pow):
                        tmp924 = subjects921.popleft()
                        subjects925 = deque(tmp924._args)
                        # State 122582
                        if len(subjects925) >= 1:
                            tmp926 = subjects925.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp926)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 122583
                                if len(subjects925) >= 1:
                                    tmp928 = subjects925.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp928)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 122584
                                        if len(subjects925) == 0:
                                            pass
                                            # State 122585
                                            if len(subjects921) == 0:
                                                pass
                                                # State 122586
                                                if len(subjects) == 0:
                                                    pass
                                                    # 80: sinh(c + d*x**n)
                                                    yield 80, subst4
                                    subjects925.appendleft(tmp928)
                            subjects925.appendleft(tmp926)
                        subjects921.appendleft(tmp924)
                if len(subjects921) >= 1 and isinstance(subjects921[0], Mul):
                    tmp930 = subjects921.popleft()
                    associative1 = tmp930
                    associative_type1 = type(tmp930)
                    subjects931 = deque(tmp930._args)
                    matcher = CommutativeMatcher122588.get()
                    tmp932 = subjects931
                    subjects931 = []
                    for s in tmp932:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp932, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122593
                            if len(subjects921) == 0:
                                pass
                                # State 122594
                                if len(subjects) == 0:
                                    pass
                                    # 80: sinh(c + d*x**n)
                                    yield 80, subst2
                    subjects921.appendleft(tmp930)
            if len(subjects921) >= 1:
                tmp933 = subjects921.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp933)
                except ValueError:
                    pass
                else:
                    pass
                    # State 123394
                    if len(subjects921) == 0:
                        pass
                        # State 123395
                        if len(subjects) == 0:
                            pass
                            # 82: sinh(u)
                            yield 82, subst1
                subjects921.appendleft(tmp933)
            if len(subjects921) >= 1 and isinstance(subjects921[0], Add):
                tmp935 = subjects921.popleft()
                associative1 = tmp935
                associative_type1 = type(tmp935)
                subjects936 = deque(tmp935._args)
                matcher = CommutativeMatcher122596.get()
                tmp937 = subjects936
                subjects936 = []
                for s in tmp937:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp937, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 122609
                        if len(subjects921) == 0:
                            pass
                            # State 122610
                            if len(subjects) == 0:
                                pass
                                # 80: sinh(c + d*x**n)
                                yield 80, subst1
                subjects921.appendleft(tmp935)
            subjects.appendleft(tmp920)
        if len(subjects) >= 1 and isinstance(subjects[0], cosh):
            tmp938 = subjects.popleft()
            subjects939 = deque(tmp938._args)
            # State 122730
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 122731
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122732
                    if len(subjects939) >= 1 and isinstance(subjects939[0], Pow):
                        tmp942 = subjects939.popleft()
                        subjects943 = deque(tmp942._args)
                        # State 122733
                        if len(subjects943) >= 1:
                            tmp944 = subjects943.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp944)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 122734
                                if len(subjects943) >= 1:
                                    tmp946 = subjects943.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp946)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 122735
                                        if len(subjects943) == 0:
                                            pass
                                            # State 122736
                                            if len(subjects939) == 0:
                                                pass
                                                # State 122737
                                                if len(subjects) == 0:
                                                    pass
                                                    # 81: cosh(c + d*x**n)
                                                    yield 81, subst4
                                    subjects943.appendleft(tmp946)
                            subjects943.appendleft(tmp944)
                        subjects939.appendleft(tmp942)
                if len(subjects939) >= 1 and isinstance(subjects939[0], Mul):
                    tmp948 = subjects939.popleft()
                    associative1 = tmp948
                    associative_type1 = type(tmp948)
                    subjects949 = deque(tmp948._args)
                    matcher = CommutativeMatcher122739.get()
                    tmp950 = subjects949
                    subjects949 = []
                    for s in tmp950:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp950, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122744
                            if len(subjects939) == 0:
                                pass
                                # State 122745
                                if len(subjects) == 0:
                                    pass
                                    # 81: cosh(c + d*x**n)
                                    yield 81, subst2
                    subjects939.appendleft(tmp948)
            if len(subjects939) >= 1:
                tmp951 = subjects939.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp951)
                except ValueError:
                    pass
                else:
                    pass
                    # State 123434
                    if len(subjects939) == 0:
                        pass
                        # State 123435
                        if len(subjects) == 0:
                            pass
                            # 83: cosh(u)
                            yield 83, subst1
                subjects939.appendleft(tmp951)
            if len(subjects939) >= 1 and isinstance(subjects939[0], Add):
                tmp953 = subjects939.popleft()
                associative1 = tmp953
                associative_type1 = type(tmp953)
                subjects954 = deque(tmp953._args)
                matcher = CommutativeMatcher122747.get()
                tmp955 = subjects954
                subjects954 = []
                for s in tmp955:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp955, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 122760
                        if len(subjects939) == 0:
                            pass
                            # State 122761
                            if len(subjects) == 0:
                                pass
                                # 81: cosh(c + d*x**n)
                                yield 81, subst1
                subjects939.appendleft(tmp953)
            subjects.appendleft(tmp938)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp956 = subjects.popleft()
            subjects957 = deque(tmp956._args)
            # State 126788
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 126789
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 126790
                    if len(subjects957) >= 1 and isinstance(subjects957[0], Pow):
                        tmp960 = subjects957.popleft()
                        subjects961 = deque(tmp960._args)
                        # State 126791
                        if len(subjects961) >= 1:
                            tmp962 = subjects961.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp962)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 126792
                                if len(subjects961) >= 1:
                                    tmp964 = subjects961.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp964)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 126793
                                        if len(subjects961) == 0:
                                            pass
                                            # State 126794
                                            if len(subjects957) == 0:
                                                pass
                                                # State 126795
                                                if len(subjects) == 0:
                                                    pass
                                                    # 84: tanh(c + d*x**n)
                                                    yield 84, subst4
                                    subjects961.appendleft(tmp964)
                            subjects961.appendleft(tmp962)
                        subjects957.appendleft(tmp960)
                if len(subjects957) >= 1 and isinstance(subjects957[0], Mul):
                    tmp966 = subjects957.popleft()
                    associative1 = tmp966
                    associative_type1 = type(tmp966)
                    subjects967 = deque(tmp966._args)
                    matcher = CommutativeMatcher126797.get()
                    tmp968 = subjects967
                    subjects967 = []
                    for s in tmp968:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp968, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 126802
                            if len(subjects957) == 0:
                                pass
                                # State 126803
                                if len(subjects) == 0:
                                    pass
                                    # 84: tanh(c + d*x**n)
                                    yield 84, subst2
                    subjects957.appendleft(tmp966)
            if len(subjects957) >= 1:
                tmp969 = subjects957.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp969)
                except ValueError:
                    pass
                else:
                    pass
                    # State 127366
                    if len(subjects957) == 0:
                        pass
                        # State 127367
                        if len(subjects) == 0:
                            pass
                            # 86: tanh(u)
                            yield 86, subst1
                subjects957.appendleft(tmp969)
            if len(subjects957) >= 1 and isinstance(subjects957[0], Add):
                tmp971 = subjects957.popleft()
                associative1 = tmp971
                associative_type1 = type(tmp971)
                subjects972 = deque(tmp971._args)
                matcher = CommutativeMatcher126805.get()
                tmp973 = subjects972
                subjects972 = []
                for s in tmp973:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp973, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 126818
                        if len(subjects957) == 0:
                            pass
                            # State 126819
                            if len(subjects) == 0:
                                pass
                                # 84: tanh(c + d*x**n)
                                yield 84, subst1
                subjects957.appendleft(tmp971)
            subjects.appendleft(tmp956)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp974 = subjects.popleft()
            subjects975 = deque(tmp974._args)
            # State 137774
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 137775
                if len(subjects975) >= 1:
                    tmp977 = subjects975.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp977)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137776
                        if len(subjects975) == 0:
                            pass
                            # State 137777
                            if len(subjects) == 0:
                                pass
                                # 92: asinh(x*c)
                                yield 92, subst2
                    subjects975.appendleft(tmp977)
            if len(subjects975) >= 1 and isinstance(subjects975[0], Mul):
                tmp979 = subjects975.popleft()
                associative1 = tmp979
                associative_type1 = type(tmp979)
                subjects980 = deque(tmp979._args)
                matcher = CommutativeMatcher137779.get()
                tmp981 = subjects980
                subjects980 = []
                for s in tmp981:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp981, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 137780
                        if len(subjects975) == 0:
                            pass
                            # State 137781
                            if len(subjects) == 0:
                                pass
                                # 92: asinh(x*c)
                                yield 92, subst1
                subjects975.appendleft(tmp979)
            if len(subjects975) >= 1 and isinstance(subjects975[0], Add):
                tmp982 = subjects975.popleft()
                associative1 = tmp982
                associative_type1 = type(tmp982)
                subjects983 = deque(tmp982._args)
                matcher = CommutativeMatcher140071.get()
                tmp984 = subjects983
                subjects983 = []
                for s in tmp984:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp984, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 140077
                        if len(subjects975) == 0:
                            pass
                            # State 140078
                            if len(subjects) == 0:
                                pass
                                # 94: asinh(c + x*d)
                                yield 94, subst1
                    if pattern_index == 1:
                        pass
                        # State 140422
                        if len(subjects975) == 0:
                            pass
                            # State 140423
                            if len(subjects) == 0:
                                pass
                                # 96: asinh(c + d*x**2)
                                yield 96, subst1
                subjects975.appendleft(tmp982)
            subjects.appendleft(tmp974)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp985 = subjects.popleft()
            subjects986 = deque(tmp985._args)
            # State 137868
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 137869
                if len(subjects986) >= 1:
                    tmp988 = subjects986.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp988)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137870
                        if len(subjects986) == 0:
                            pass
                            # State 137871
                            if len(subjects) == 0:
                                pass
                                # 93: acosh(x*c)
                                yield 93, subst2
                    subjects986.appendleft(tmp988)
            if len(subjects986) >= 1 and isinstance(subjects986[0], Mul):
                tmp990 = subjects986.popleft()
                associative1 = tmp990
                associative_type1 = type(tmp990)
                subjects991 = deque(tmp990._args)
                matcher = CommutativeMatcher137873.get()
                tmp992 = subjects991
                subjects991 = []
                for s in tmp992:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp992, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 137874
                        if len(subjects986) == 0:
                            pass
                            # State 137875
                            if len(subjects) == 0:
                                pass
                                # 93: acosh(x*c)
                                yield 93, subst1
                subjects986.appendleft(tmp990)
            if len(subjects986) >= 1 and isinstance(subjects986[0], Add):
                tmp993 = subjects986.popleft()
                associative1 = tmp993
                associative_type1 = type(tmp993)
                subjects994 = deque(tmp993._args)
                matcher = CommutativeMatcher140167.get()
                tmp995 = subjects994
                subjects994 = []
                for s in tmp995:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp995, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 140173
                        if len(subjects986) == 0:
                            pass
                            # State 140174
                            if len(subjects) == 0:
                                pass
                                # 95: acosh(c + x*d)
                                yield 95, subst1
                    if pattern_index == 1:
                        pass
                        # State 140549
                        if len(subjects986) == 0:
                            pass
                            # State 140550
                            if len(subjects) == 0:
                                pass
                                # 97: acosh(d*x**2 + 1)
                                yield 97, subst1
                    if pattern_index == 2:
                        pass
                        # State 140576
                        if len(subjects986) == 0:
                            pass
                            # State 140577
                            if len(subjects) == 0:
                                pass
                                # 98: acosh(d*x**2 - 1)
                                yield 98, subst1
                    if pattern_index == 3:
                        pass
                        # State 140599
                        if len(subjects986) == 0:
                            pass
                            # State 140600
                            if len(subjects) == 0:
                                pass
                                # 99: acosh(c + d*x**2)
                                yield 99, subst1
                subjects986.appendleft(tmp993)
            subjects.appendleft(tmp985)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp996 = subjects.popleft()
            subjects997 = deque(tmp996._args)
            # State 142302
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142303
                if len(subjects997) >= 1:
                    tmp999 = subjects997.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp999)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142304
                        if len(subjects997) == 0:
                            pass
                            # State 142305
                            if len(subjects) == 0:
                                pass
                                # 100: atanh(x*c)
                                yield 100, subst2
                    subjects997.appendleft(tmp999)
            if len(subjects997) >= 1 and isinstance(subjects997[0], Mul):
                tmp1001 = subjects997.popleft()
                associative1 = tmp1001
                associative_type1 = type(tmp1001)
                subjects1002 = deque(tmp1001._args)
                matcher = CommutativeMatcher142307.get()
                tmp1003 = subjects1002
                subjects1002 = []
                for s in tmp1003:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1003, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142308
                        if len(subjects997) == 0:
                            pass
                            # State 142309
                            if len(subjects) == 0:
                                pass
                                # 100: atanh(x*c)
                                yield 100, subst1
                subjects997.appendleft(tmp1001)
            if len(subjects997) >= 1 and isinstance(subjects997[0], Add):
                tmp1004 = subjects997.popleft()
                associative1 = tmp1004
                associative_type1 = type(tmp1004)
                subjects1005 = deque(tmp1004._args)
                matcher = CommutativeMatcher144759.get()
                tmp1006 = subjects1005
                subjects1005 = []
                for s in tmp1006:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1006, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144765
                        if len(subjects997) == 0:
                            pass
                            # State 144766
                            if len(subjects) == 0:
                                pass
                                # 102: atanh(c + x*d)
                                yield 102, subst1
                subjects997.appendleft(tmp1004)
            subjects.appendleft(tmp996)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp1007 = subjects.popleft()
            subjects1008 = deque(tmp1007._args)
            # State 142396
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142397
                if len(subjects1008) >= 1:
                    tmp1010 = subjects1008.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp1010)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142398
                        if len(subjects1008) == 0:
                            pass
                            # State 142399
                            if len(subjects) == 0:
                                pass
                                # 101: acoth(x*c)
                                yield 101, subst2
                    subjects1008.appendleft(tmp1010)
            if len(subjects1008) >= 1 and isinstance(subjects1008[0], Mul):
                tmp1012 = subjects1008.popleft()
                associative1 = tmp1012
                associative_type1 = type(tmp1012)
                subjects1013 = deque(tmp1012._args)
                matcher = CommutativeMatcher142401.get()
                tmp1014 = subjects1013
                subjects1013 = []
                for s in tmp1014:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1014, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142402
                        if len(subjects1008) == 0:
                            pass
                            # State 142403
                            if len(subjects) == 0:
                                pass
                                # 101: acoth(x*c)
                                yield 101, subst1
                subjects1008.appendleft(tmp1012)
            if len(subjects1008) >= 1 and isinstance(subjects1008[0], Add):
                tmp1015 = subjects1008.popleft()
                associative1 = tmp1015
                associative_type1 = type(tmp1015)
                subjects1016 = deque(tmp1015._args)
                matcher = CommutativeMatcher144855.get()
                tmp1017 = subjects1016
                subjects1016 = []
                for s in tmp1017:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1017, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144861
                        if len(subjects1008) == 0:
                            pass
                            # State 144862
                            if len(subjects) == 0:
                                pass
                                # 103: acoth(c + x*d)
                                yield 103, subst1
                subjects1008.appendleft(tmp1015)
            subjects.appendleft(tmp1007)
        if len(subjects) >= 1 and isinstance(subjects[0], asech):
            tmp1018 = subjects.popleft()
            subjects1019 = deque(tmp1018._args)
            # State 148740
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 148741
                if len(subjects1019) >= 1:
                    tmp1021 = subjects1019.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp1021)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148742
                        if len(subjects1019) == 0:
                            pass
                            # State 148743
                            if len(subjects) == 0:
                                pass
                                # 104: asech(x*c)
                                yield 104, subst2
                    subjects1019.appendleft(tmp1021)
            if len(subjects1019) >= 1 and isinstance(subjects1019[0], Mul):
                tmp1023 = subjects1019.popleft()
                associative1 = tmp1023
                associative_type1 = type(tmp1023)
                subjects1024 = deque(tmp1023._args)
                matcher = CommutativeMatcher148745.get()
                tmp1025 = subjects1024
                subjects1024 = []
                for s in tmp1025:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1025, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 148746
                        if len(subjects1019) == 0:
                            pass
                            # State 148747
                            if len(subjects) == 0:
                                pass
                                # 104: asech(x*c)
                                yield 104, subst1
                subjects1019.appendleft(tmp1023)
            subjects.appendleft(tmp1018)
        if len(subjects) >= 1 and isinstance(subjects[0], acsch):
            tmp1026 = subjects.popleft()
            subjects1027 = deque(tmp1026._args)
            # State 148791
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 148792
                if len(subjects1027) >= 1:
                    tmp1029 = subjects1027.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp1029)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148793
                        if len(subjects1027) == 0:
                            pass
                            # State 148794
                            if len(subjects) == 0:
                                pass
                                # 105: acsch(x*c)
                                yield 105, subst2
                    subjects1027.appendleft(tmp1029)
            if len(subjects1027) >= 1 and isinstance(subjects1027[0], Mul):
                tmp1031 = subjects1027.popleft()
                associative1 = tmp1031
                associative_type1 = type(tmp1031)
                subjects1032 = deque(tmp1031._args)
                matcher = CommutativeMatcher148796.get()
                tmp1033 = subjects1032
                subjects1032 = []
                for s in tmp1033:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp1033, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 148797
                        if len(subjects1027) == 0:
                            pass
                            # State 148798
                            if len(subjects) == 0:
                                pass
                                # 105: acsch(x*c)
                                yield 105, subst1
                subjects1027.appendleft(tmp1031)
            subjects.appendleft(tmp1026)
        return
        yield


from .generated_part009690 import *
from .generated_part009667 import *
from .generated_part009674 import *
from .generated_part009818 import *
from .generated_part009693 import *
from .generated_part009716 import *
from .generated_part009738 import *
from .generated_part009646 import *
from collections import deque
from .generated_part009677 import *
from .generated_part009844 import *
from .generated_part009668 import *
from matchpy.utils import VariableWithCount
from .generated_part009653 import *
from .generated_part009679 import *
from .generated_part009673 import *
from .generated_part009821 import *
from .generated_part009846 import *
from .generated_part009804 import *
from .generated_part009684 import *
from .generated_part009812 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part009631 import *
from .generated_part009826 import *
from .generated_part009686 import *
from .generated_part009808 import *
from .generated_part009633 import *
from .generated_part009698 import *
from .generated_part009831 import *
from .generated_part009817 import *
from .generated_part009704 import *
from .generated_part009637 import *
from .generated_part009630 import *
from .generated_part009758 import *
from .generated_part009740 import *
from .generated_part009639 import *
from .generated_part009802 import *
from .generated_part009656 import *
from .generated_part009689 import *
from .generated_part009741 import *
from .generated_part009814 import *
from .generated_part009720 import *
from multiset import Multiset
from .generated_part009815 import *
from .generated_part009713 import *
from .generated_part009658 import *
from .generated_part009702 import *
from .generated_part009708 import *
from .generated_part009729 import *
from .generated_part009705 import *
from .generated_part009717 import *
from .generated_part009837 import *
from .generated_part009701 import *
from .generated_part009743 import *
from .generated_part009809 import *
from .generated_part009634 import *
from .generated_part009847 import *
from .generated_part009659 import *
from .generated_part009719 import *
from .generated_part009662 import *
from .generated_part009823 import *
from .generated_part009664 import *
from .generated_part009683 import *
from .generated_part009820 import *
from .generated_part009838 import *
from .generated_part009695 import *
from .generated_part009714 import *
from .generated_part009801 import *
from .generated_part009652 import *
from .generated_part009670 import *
from .generated_part009707 import *
from .generated_part009665 import *
from .generated_part009825 import *
from .generated_part009737 import *
from .generated_part009699 import *
from .generated_part009807 import *
from .generated_part009696 import *
from .generated_part009636 import *
from .generated_part009710 import *
from .generated_part009687 import *
from .generated_part009811 import *
from .generated_part009692 import *
from .generated_part009805 import *
from .generated_part009841 import *
from .generated_part009671 import *
from .generated_part009834 import *
from .generated_part009824 import *
from .generated_part009840 import *
from .generated_part009661 import *
from .generated_part009835 import *
from .generated_part009750 import *
from .generated_part009829 import *
from .generated_part009828 import *
from .generated_part009843 import *
from .generated_part009676 import *
from .generated_part009681 import *
from .generated_part009680 import *
from .generated_part009722 import *
from .generated_part009832 import *
from .generated_part009711 import *
from .generated_part009655 import *