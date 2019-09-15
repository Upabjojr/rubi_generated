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


class CommutativeMatcher2934(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({3: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({4: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({5: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({6: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({7: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({8: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({9: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({10: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({11: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({12: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({13: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({14: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({15: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({16: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({17: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({18: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({19: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({20: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({21: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({22: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({23: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({24: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({25: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    27: (27, Multiset({26: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({27: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({28: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({29: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    31: (31, Multiset({30: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({31: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    33: (33, Multiset({32: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({33: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({34: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    36: (36, Multiset({35: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    37: (37, Multiset({36: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    38: (38, Multiset({37: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({38: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({39: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    41: (41, Multiset({40: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    42: (42, Multiset({41: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    43: (43, Multiset({42: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    44: (44, Multiset({43: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    45: (45, Multiset({44: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    46: (46, Multiset({45: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    47: (47, Multiset({46: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    48: (48, Multiset({47: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    49: (49, Multiset({48: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    50: (50, Multiset({49: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    51: (51, Multiset({50: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    52: (52, Multiset({51: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    53: (53, Multiset({52: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    54: (54, Multiset({53: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    55: (55, Multiset({54: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    56: (56, Multiset({55: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    57: (57, Multiset({56: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    58: (58, Multiset({57: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    59: (59, Multiset({58: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    60: (60, Multiset({59: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    61: (61, Multiset({60: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    62: (62, Multiset({61: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    63: (63, Multiset({62: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    64: (64, Multiset({63: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    65: (65, Multiset({64: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    66: (66, Multiset({65: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    67: (67, Multiset({66: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    68: (68, Multiset({67: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    69: (69, Multiset({68: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    70: (70, Multiset({69: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    71: (71, Multiset({70: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    72: (72, Multiset({71: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    73: (73, Multiset({72: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    74: (74, Multiset({73: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    75: (75, Multiset({74: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    76: (76, Multiset({75: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    77: (77, Multiset({76: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    78: (78, Multiset({77: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    79: (79, Multiset({78: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    80: (80, Multiset({79: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    81: (81, Multiset({80: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    82: (82, Multiset({81: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    83: (83, Multiset({82: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    84: (84, Multiset({83: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    85: (85, Multiset({84: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    86: (86, Multiset({85: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    87: (87, Multiset({86: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    88: (88, Multiset({87: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    89: (89, Multiset({88: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    90: (90, Multiset({89: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    91: (91, Multiset({90: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    92: (92, Multiset({91: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    93: (93, Multiset({92: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    94: (94, Multiset({93: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    95: (95, Multiset({94: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    96: (96, Multiset({95: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    97: (97, Multiset({96: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    98: (98, Multiset({97: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    99: (99, Multiset({98: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    100: (100, Multiset({99: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    101: (101, Multiset({100: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    102: (102, Multiset({101: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    103: (103, Multiset({102: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    104: (104, Multiset({103: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    105: (105, Multiset({104: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    106: (106, Multiset({105: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    107: (107, Multiset({106: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    108: (108, Multiset({107: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    109: (109, Multiset({108: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    110: (110, Multiset({109: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    111: (111, Multiset({110: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    112: (112, Multiset({111: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    113: (113, Multiset({112: 1}), [
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
        if CommutativeMatcher2934._instance is None:
            CommutativeMatcher2934._instance = CommutativeMatcher2934()
        return CommutativeMatcher2934._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2933
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 6345
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 6346
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 6347
                            if len(subjects2) == 0:
                                pass
                                # State 6348
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n /; (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10060
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp8 = subjects2.popleft()
                    subjects9 = deque(tmp8._args)
                    # State 10061
                    if len(subjects9) >= 1:
                        tmp10 = subjects9.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.1', tmp10)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10062
                            if len(subjects9) >= 1:
                                tmp12 = subjects9.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', tmp12)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10063
                                    if len(subjects9) == 0:
                                        pass
                                        # State 10064
                                        if len(subjects2) >= 1:
                                            tmp14 = subjects2.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.2', tmp14)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 10065
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 10066
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (c*x**n)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f52) and (cons_f4) and (cons_f5) and (cons_f800)
                                                        yield 1, subst4
                                            subjects2.appendleft(tmp14)
                                subjects9.appendleft(tmp12)
                            if len(subjects9) >= 1 and subjects9[0] == Integer(-1):
                                tmp16 = subjects9.popleft()
                                # State 10604
                                if len(subjects9) == 0:
                                    pass
                                    # State 10605
                                    if len(subjects2) >= 1:
                                        tmp17 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2', tmp17)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 10606
                                            if len(subjects2) == 0:
                                                pass
                                                # State 10607
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: (c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                                    yield 2, subst3
                                        subjects2.appendleft(tmp17)
                                subjects9.appendleft(tmp16)
                        subjects9.appendleft(tmp10)
                    subjects2.appendleft(tmp8)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp19 = subjects2.popleft()
                associative1 = tmp19
                associative_type1 = type(tmp19)
                subjects20 = deque(tmp19._args)
                matcher = CommutativeMatcher10068.get()
                tmp21 = subjects20
                subjects20 = []
                for s in tmp21:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp21, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10073
                        if len(subjects2) >= 1:
                            tmp22 = []
                            tmp22.append(subjects2.popleft())
                            while True:
                                if len(tmp22) > 1:
                                    tmp23 = create_operation_expression(associative1, tmp22)
                                elif len(tmp22) == 1:
                                    tmp23 = tmp22[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp23)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10074
                                    if len(subjects2) == 0:
                                        pass
                                        # State 10075
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (c*x**n)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f52) and (cons_f4) and (cons_f5) and (cons_f800)
                                            yield 1, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp22.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp22))
                    if pattern_index == 1:
                        pass
                        # State 10610
                        if len(subjects2) >= 1:
                            tmp25 = []
                            tmp25.append(subjects2.popleft())
                            while True:
                                if len(tmp25) > 1:
                                    tmp26 = create_operation_expression(associative1, tmp25)
                                elif len(tmp25) == 1:
                                    tmp26 = tmp25[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp26)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10611
                                    if len(subjects2) == 0:
                                        pass
                                        # State 10612
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (c/x)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                            yield 2, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp25.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp25))
                subjects2.appendleft(tmp19)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp28 = subjects2.popleft()
                associative1 = tmp28
                associative_type1 = type(tmp28)
                subjects29 = deque(tmp28._args)
                matcher = CommutativeMatcher13396.get()
                tmp30 = subjects29
                subjects29 = []
                for s in tmp30:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp30, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 13446
                        if len(subjects2) >= 1:
                            tmp31 = []
                            tmp31.append(subjects2.popleft())
                            while True:
                                if len(tmp31) > 1:
                                    tmp32 = create_operation_expression(associative1, tmp31)
                                elif len(tmp31) == 1:
                                    tmp32 = tmp31[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp32)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 13447
                                    if len(subjects2) == 0:
                                        pass
                                        # State 13448
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d + e*x + f*sqrt(a + b*x + c*x**2))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                                            yield 3, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp31.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp31))
                    if pattern_index == 1:
                        pass
                        # State 13638
                        if len(subjects2) >= 1:
                            tmp34 = []
                            tmp34.append(subjects2.popleft())
                            while True:
                                if len(tmp34) > 1:
                                    tmp35 = create_operation_expression(associative1, tmp34)
                                elif len(tmp34) == 1:
                                    tmp35 = tmp34[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp35)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 13639
                                    if len(subjects2) == 0:
                                        pass
                                        # State 13640
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d + e*x + f*sqrt(a + c*x**2))**n /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                                            yield 4, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp34.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp34))
                    if pattern_index == 2:
                        pass
                        # State 13742
                        if len(subjects2) >= 1:
                            tmp37 = []
                            tmp37.append(subjects2.popleft())
                            while True:
                                if len(tmp37) > 1:
                                    tmp38 = create_operation_expression(associative1, tmp37)
                                elif len(tmp37) == 1:
                                    tmp38 = tmp37[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.1.2', tmp38)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 13743
                                    if len(subjects2) == 0:
                                        pass
                                        # State 13744
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (u + f*sqrt(v))**n /; (cons_f127) and (cons_f4) and (cons_f70) and (cons_f820) and (cons_f821) and (cons_f1058)
                                            yield 5, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp37.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp37))
                subjects2.appendleft(tmp28)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp40 = subjects2.popleft()
                subjects41 = deque(tmp40._args)
                # State 87562
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 87563
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 87564
                        if len(subjects41) >= 1 and isinstance(subjects41[0], Pow):
                            tmp44 = subjects41.popleft()
                            subjects45 = deque(tmp44._args)
                            # State 87565
                            if len(subjects45) >= 1:
                                tmp46 = subjects45.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp46)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 87566
                                    if len(subjects45) >= 1:
                                        tmp48 = subjects45.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp48)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 87567
                                            if len(subjects45) == 0:
                                                pass
                                                # State 87568
                                                if len(subjects41) == 0:
                                                    pass
                                                    # State 87569
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp50 = subjects2.popleft()
                                                        # State 87570
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 87571
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 32: 1/tan(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                yield 32, subst4
                                                                # 28: 1/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                yield 28, subst4
                                                                # 30: 1/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                yield 30, subst4
                                                        subjects2.appendleft(tmp50)
                                        subjects45.appendleft(tmp48)
                                subjects45.appendleft(tmp46)
                            subjects41.appendleft(tmp44)
                    if len(subjects41) >= 1 and isinstance(subjects41[0], Mul):
                        tmp51 = subjects41.popleft()
                        associative1 = tmp51
                        associative_type1 = type(tmp51)
                        subjects52 = deque(tmp51._args)
                        matcher = CommutativeMatcher87573.get()
                        tmp53 = subjects52
                        subjects52 = []
                        for s in tmp53:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp53, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 87578
                                if len(subjects41) == 0:
                                    pass
                                    # State 87579
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp54 = subjects2.popleft()
                                        # State 87580
                                        if len(subjects2) == 0:
                                            pass
                                            # State 87581
                                            if len(subjects) == 0:
                                                pass
                                                # 32: 1/tan(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                yield 32, subst2
                                                # 28: 1/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                yield 28, subst2
                                                # 30: 1/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                yield 30, subst2
                                        subjects2.appendleft(tmp54)
                        subjects41.appendleft(tmp51)
                if len(subjects41) >= 1:
                    tmp55 = subjects41.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp55)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 87912
                        if len(subjects41) == 0:
                            pass
                            # State 87913
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp57 = subjects2.popleft()
                                # State 87914
                                if len(subjects2) == 0:
                                    pass
                                    # State 87915
                                    if len(subjects) == 0:
                                        pass
                                        # 34: 1/tan(u) /; (cons_f825) and (cons_f826)
                                        yield 34, subst1
                                subjects2.appendleft(tmp57)
                    subjects41.appendleft(tmp55)
                if len(subjects41) >= 1 and isinstance(subjects41[0], Add):
                    tmp58 = subjects41.popleft()
                    associative1 = tmp58
                    associative_type1 = type(tmp58)
                    subjects59 = deque(tmp58._args)
                    matcher = CommutativeMatcher87583.get()
                    tmp60 = subjects59
                    subjects59 = []
                    for s in tmp60:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp60, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 87596
                            if len(subjects41) == 0:
                                pass
                                # State 87597
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp61 = subjects2.popleft()
                                    # State 87598
                                    if len(subjects2) == 0:
                                        pass
                                        # State 87599
                                        if len(subjects) == 0:
                                            pass
                                            # 32: 1/tan(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            yield 32, subst1
                                            # 28: 1/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                            yield 28, subst1
                                            # 30: 1/tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                            yield 30, subst1
                                    subjects2.appendleft(tmp61)
                    subjects41.appendleft(tmp58)
                subjects2.appendleft(tmp40)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp62 = subjects2.popleft()
                subjects63 = deque(tmp62._args)
                # State 97617
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 97618
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 97619
                        if len(subjects63) >= 1 and isinstance(subjects63[0], Pow):
                            tmp66 = subjects63.popleft()
                            subjects67 = deque(tmp66._args)
                            # State 97620
                            if len(subjects67) >= 1:
                                tmp68 = subjects67.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp68)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 97621
                                    if len(subjects67) >= 1:
                                        tmp70 = subjects67.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp70)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 97622
                                            if len(subjects67) == 0:
                                                pass
                                                # State 97623
                                                if len(subjects63) == 0:
                                                    pass
                                                    # State 97624
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp72 = subjects2.popleft()
                                                        # State 97625
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 97626
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 35: 1/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                yield 35, subst4
                                                                # 37: 1/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                yield 37, subst4
                                                                # 39: 1/cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                yield 39, subst4
                                                        subjects2.appendleft(tmp72)
                                        subjects67.appendleft(tmp70)
                                subjects67.appendleft(tmp68)
                            subjects63.appendleft(tmp66)
                    if len(subjects63) >= 1 and isinstance(subjects63[0], Mul):
                        tmp73 = subjects63.popleft()
                        associative1 = tmp73
                        associative_type1 = type(tmp73)
                        subjects74 = deque(tmp73._args)
                        matcher = CommutativeMatcher97628.get()
                        tmp75 = subjects74
                        subjects74 = []
                        for s in tmp75:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp75, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 97633
                                if len(subjects63) == 0:
                                    pass
                                    # State 97634
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp76 = subjects2.popleft()
                                        # State 97635
                                        if len(subjects2) == 0:
                                            pass
                                            # State 97636
                                            if len(subjects) == 0:
                                                pass
                                                # 35: 1/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                yield 35, subst2
                                                # 37: 1/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                yield 37, subst2
                                                # 39: 1/cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                yield 39, subst2
                                        subjects2.appendleft(tmp76)
                        subjects63.appendleft(tmp73)
                if len(subjects63) >= 1:
                    tmp77 = subjects63.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp77)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98251
                        if len(subjects63) == 0:
                            pass
                            # State 98252
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp79 = subjects2.popleft()
                                # State 98253
                                if len(subjects2) == 0:
                                    pass
                                    # State 98254
                                    if len(subjects) == 0:
                                        pass
                                        # 41: 1/cos(u) /; (cons_f825) and (cons_f826)
                                        yield 41, subst1
                                subjects2.appendleft(tmp79)
                    subjects63.appendleft(tmp77)
                if len(subjects63) >= 1 and isinstance(subjects63[0], Add):
                    tmp80 = subjects63.popleft()
                    associative1 = tmp80
                    associative_type1 = type(tmp80)
                    subjects81 = deque(tmp80._args)
                    matcher = CommutativeMatcher97638.get()
                    tmp82 = subjects81
                    subjects81 = []
                    for s in tmp82:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp82, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 97651
                            if len(subjects63) == 0:
                                pass
                                # State 97652
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp83 = subjects2.popleft()
                                    # State 97653
                                    if len(subjects2) == 0:
                                        pass
                                        # State 97654
                                        if len(subjects) == 0:
                                            pass
                                            # 35: 1/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                            yield 35, subst1
                                            # 37: 1/cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                            yield 37, subst1
                                            # 39: 1/cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            yield 39, subst1
                                    subjects2.appendleft(tmp83)
                    subjects63.appendleft(tmp80)
                subjects2.appendleft(tmp62)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp84 = subjects2.popleft()
                subjects85 = deque(tmp84._args)
                # State 97925
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 97926
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 97927
                        if len(subjects85) >= 1 and isinstance(subjects85[0], Pow):
                            tmp88 = subjects85.popleft()
                            subjects89 = deque(tmp88._args)
                            # State 97928
                            if len(subjects89) >= 1:
                                tmp90 = subjects89.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp90)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 97929
                                    if len(subjects89) >= 1:
                                        tmp92 = subjects89.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp92)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 97930
                                            if len(subjects89) == 0:
                                                pass
                                                # State 97931
                                                if len(subjects85) == 0:
                                                    pass
                                                    # State 97932
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp94 = subjects2.popleft()
                                                        # State 97933
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 97934
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 40: 1/sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                yield 40, subst4
                                                                # 36: 1/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                yield 36, subst4
                                                                # 38: 1/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                yield 38, subst4
                                                        subjects2.appendleft(tmp94)
                                        subjects89.appendleft(tmp92)
                                subjects89.appendleft(tmp90)
                            subjects85.appendleft(tmp88)
                    if len(subjects85) >= 1 and isinstance(subjects85[0], Mul):
                        tmp95 = subjects85.popleft()
                        associative1 = tmp95
                        associative_type1 = type(tmp95)
                        subjects96 = deque(tmp95._args)
                        matcher = CommutativeMatcher97936.get()
                        tmp97 = subjects96
                        subjects96 = []
                        for s in tmp97:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp97, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 97941
                                if len(subjects85) == 0:
                                    pass
                                    # State 97942
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp98 = subjects2.popleft()
                                        # State 97943
                                        if len(subjects2) == 0:
                                            pass
                                            # State 97944
                                            if len(subjects) == 0:
                                                pass
                                                # 40: 1/sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                yield 40, subst2
                                                # 36: 1/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                yield 36, subst2
                                                # 38: 1/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                yield 38, subst2
                                        subjects2.appendleft(tmp98)
                        subjects85.appendleft(tmp95)
                if len(subjects85) >= 1:
                    tmp99 = subjects85.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp99)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98307
                        if len(subjects85) == 0:
                            pass
                            # State 98308
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp101 = subjects2.popleft()
                                # State 98309
                                if len(subjects2) == 0:
                                    pass
                                    # State 98310
                                    if len(subjects) == 0:
                                        pass
                                        # 42: 1/sin(u) /; (cons_f825) and (cons_f826)
                                        yield 42, subst1
                                subjects2.appendleft(tmp101)
                    subjects85.appendleft(tmp99)
                if len(subjects85) >= 1 and isinstance(subjects85[0], Add):
                    tmp102 = subjects85.popleft()
                    associative1 = tmp102
                    associative_type1 = type(tmp102)
                    subjects103 = deque(tmp102._args)
                    matcher = CommutativeMatcher97946.get()
                    tmp104 = subjects103
                    subjects103 = []
                    for s in tmp104:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp104, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 97959
                            if len(subjects85) == 0:
                                pass
                                # State 97960
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp105 = subjects2.popleft()
                                    # State 97961
                                    if len(subjects2) == 0:
                                        pass
                                        # State 97962
                                        if len(subjects) == 0:
                                            pass
                                            # 40: 1/sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            yield 40, subst1
                                            # 36: 1/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                            yield 36, subst1
                                            # 38: 1/sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                            yield 38, subst1
                                    subjects2.appendleft(tmp105)
                    subjects85.appendleft(tmp102)
                subjects2.appendleft(tmp84)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tanh):
                tmp106 = subjects2.popleft()
                subjects107 = deque(tmp106._args)
                # State 127041
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 127042
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 127043
                        if len(subjects107) >= 1 and isinstance(subjects107[0], Pow):
                            tmp110 = subjects107.popleft()
                            subjects111 = deque(tmp110._args)
                            # State 127044
                            if len(subjects111) >= 1:
                                tmp112 = subjects111.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp112)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 127045
                                    if len(subjects111) >= 1:
                                        tmp114 = subjects111.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp114)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 127046
                                            if len(subjects111) == 0:
                                                pass
                                                # State 127047
                                                if len(subjects107) == 0:
                                                    pass
                                                    # State 127048
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp116 = subjects2.popleft()
                                                        # State 127049
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 127050
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 80: 1/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                yield 80, subst4
                                                                # 82: 1/tanh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                yield 82, subst4
                                                                # 78: 1/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                yield 78, subst4
                                                        subjects2.appendleft(tmp116)
                                        subjects111.appendleft(tmp114)
                                subjects111.appendleft(tmp112)
                            subjects107.appendleft(tmp110)
                    if len(subjects107) >= 1 and isinstance(subjects107[0], Mul):
                        tmp117 = subjects107.popleft()
                        associative1 = tmp117
                        associative_type1 = type(tmp117)
                        subjects118 = deque(tmp117._args)
                        matcher = CommutativeMatcher127052.get()
                        tmp119 = subjects118
                        subjects118 = []
                        for s in tmp119:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp119, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 127057
                                if len(subjects107) == 0:
                                    pass
                                    # State 127058
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp120 = subjects2.popleft()
                                        # State 127059
                                        if len(subjects2) == 0:
                                            pass
                                            # State 127060
                                            if len(subjects) == 0:
                                                pass
                                                # 80: 1/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                yield 80, subst2
                                                # 82: 1/tanh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                yield 82, subst2
                                                # 78: 1/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                yield 78, subst2
                                        subjects2.appendleft(tmp120)
                        subjects107.appendleft(tmp117)
                if len(subjects107) >= 1:
                    tmp121 = subjects107.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp121)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 127407
                        if len(subjects107) == 0:
                            pass
                            # State 127408
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp123 = subjects2.popleft()
                                # State 127409
                                if len(subjects2) == 0:
                                    pass
                                    # State 127410
                                    if len(subjects) == 0:
                                        pass
                                        # 84: 1/tanh(u) /; (cons_f825) and (cons_f826)
                                        yield 84, subst1
                                subjects2.appendleft(tmp123)
                    subjects107.appendleft(tmp121)
                if len(subjects107) >= 1 and isinstance(subjects107[0], Add):
                    tmp124 = subjects107.popleft()
                    associative1 = tmp124
                    associative_type1 = type(tmp124)
                    subjects125 = deque(tmp124._args)
                    matcher = CommutativeMatcher127062.get()
                    tmp126 = subjects125
                    subjects125 = []
                    for s in tmp126:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp126, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 127075
                            if len(subjects107) == 0:
                                pass
                                # State 127076
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp127 = subjects2.popleft()
                                    # State 127077
                                    if len(subjects2) == 0:
                                        pass
                                        # State 127078
                                        if len(subjects) == 0:
                                            pass
                                            # 80: 1/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                            yield 80, subst1
                                            # 82: 1/tanh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            yield 82, subst1
                                            # 78: 1/tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                            yield 78, subst1
                                    subjects2.appendleft(tmp127)
                    subjects107.appendleft(tmp124)
                subjects2.appendleft(tmp106)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cosh):
                tmp128 = subjects2.popleft()
                subjects129 = deque(tmp128._args)
                # State 129818
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 129819
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 129820
                        if len(subjects129) >= 1 and isinstance(subjects129[0], Pow):
                            tmp132 = subjects129.popleft()
                            subjects133 = deque(tmp132._args)
                            # State 129821
                            if len(subjects133) >= 1:
                                tmp134 = subjects133.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp134)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 129822
                                    if len(subjects133) >= 1:
                                        tmp136 = subjects133.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp136)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 129823
                                            if len(subjects133) == 0:
                                                pass
                                                # State 129824
                                                if len(subjects129) == 0:
                                                    pass
                                                    # State 129825
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp138 = subjects2.popleft()
                                                        # State 129826
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 129827
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 89: 1/cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                yield 89, subst4
                                                                # 85: 1/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                yield 85, subst4
                                                                # 87: 1/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                yield 87, subst4
                                                        subjects2.appendleft(tmp138)
                                        subjects133.appendleft(tmp136)
                                subjects133.appendleft(tmp134)
                            subjects129.appendleft(tmp132)
                    if len(subjects129) >= 1 and isinstance(subjects129[0], Mul):
                        tmp139 = subjects129.popleft()
                        associative1 = tmp139
                        associative_type1 = type(tmp139)
                        subjects140 = deque(tmp139._args)
                        matcher = CommutativeMatcher129829.get()
                        tmp141 = subjects140
                        subjects140 = []
                        for s in tmp141:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp141, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 129834
                                if len(subjects129) == 0:
                                    pass
                                    # State 129835
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp142 = subjects2.popleft()
                                        # State 129836
                                        if len(subjects2) == 0:
                                            pass
                                            # State 129837
                                            if len(subjects) == 0:
                                                pass
                                                # 89: 1/cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                yield 89, subst2
                                                # 85: 1/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                yield 85, subst2
                                                # 87: 1/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                yield 87, subst2
                                        subjects2.appendleft(tmp142)
                        subjects129.appendleft(tmp139)
                if len(subjects129) >= 1:
                    tmp143 = subjects129.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp143)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130500
                        if len(subjects129) == 0:
                            pass
                            # State 130501
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp145 = subjects2.popleft()
                                # State 130502
                                if len(subjects2) == 0:
                                    pass
                                    # State 130503
                                    if len(subjects) == 0:
                                        pass
                                        # 91: 1/cosh(u) /; (cons_f825) and (cons_f826)
                                        yield 91, subst1
                                subjects2.appendleft(tmp145)
                    subjects129.appendleft(tmp143)
                if len(subjects129) >= 1 and isinstance(subjects129[0], Add):
                    tmp146 = subjects129.popleft()
                    associative1 = tmp146
                    associative_type1 = type(tmp146)
                    subjects147 = deque(tmp146._args)
                    matcher = CommutativeMatcher129839.get()
                    tmp148 = subjects147
                    subjects147 = []
                    for s in tmp148:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp148, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 129852
                            if len(subjects129) == 0:
                                pass
                                # State 129853
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp149 = subjects2.popleft()
                                    # State 129854
                                    if len(subjects2) == 0:
                                        pass
                                        # State 129855
                                        if len(subjects) == 0:
                                            pass
                                            # 89: 1/cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            yield 89, subst1
                                            # 85: 1/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                            yield 85, subst1
                                            # 87: 1/cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                            yield 87, subst1
                                    subjects2.appendleft(tmp149)
                    subjects129.appendleft(tmp146)
                subjects2.appendleft(tmp128)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sinh):
                tmp150 = subjects2.popleft()
                subjects151 = deque(tmp150._args)
                # State 130158
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 130159
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130160
                        if len(subjects151) >= 1 and isinstance(subjects151[0], Pow):
                            tmp154 = subjects151.popleft()
                            subjects155 = deque(tmp154._args)
                            # State 130161
                            if len(subjects155) >= 1:
                                tmp156 = subjects155.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.3.1.1', tmp156)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 130162
                                    if len(subjects155) >= 1:
                                        tmp158 = subjects155.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.3.1.2', tmp158)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 130163
                                            if len(subjects155) == 0:
                                                pass
                                                # State 130164
                                                if len(subjects151) == 0:
                                                    pass
                                                    # State 130165
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp160 = subjects2.popleft()
                                                        # State 130166
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 130167
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 88: 1/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                                yield 88, subst4
                                                                # 90: 1/sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                                yield 90, subst4
                                                                # 86: 1/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                                yield 86, subst4
                                                        subjects2.appendleft(tmp160)
                                        subjects155.appendleft(tmp158)
                                subjects155.appendleft(tmp156)
                            subjects151.appendleft(tmp154)
                    if len(subjects151) >= 1 and isinstance(subjects151[0], Mul):
                        tmp161 = subjects151.popleft()
                        associative1 = tmp161
                        associative_type1 = type(tmp161)
                        subjects162 = deque(tmp161._args)
                        matcher = CommutativeMatcher130169.get()
                        tmp163 = subjects162
                        subjects162 = []
                        for s in tmp163:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp163, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 130174
                                if len(subjects151) == 0:
                                    pass
                                    # State 130175
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp164 = subjects2.popleft()
                                        # State 130176
                                        if len(subjects2) == 0:
                                            pass
                                            # State 130177
                                            if len(subjects) == 0:
                                                pass
                                                # 88: 1/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                yield 88, subst2
                                                # 90: 1/sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                yield 90, subst2
                                                # 86: 1/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                yield 86, subst2
                                        subjects2.appendleft(tmp164)
                        subjects151.appendleft(tmp161)
                if len(subjects151) >= 1:
                    tmp165 = subjects151.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp165)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130556
                        if len(subjects151) == 0:
                            pass
                            # State 130557
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp167 = subjects2.popleft()
                                # State 130558
                                if len(subjects2) == 0:
                                    pass
                                    # State 130559
                                    if len(subjects) == 0:
                                        pass
                                        # 92: 1/sinh(u) /; (cons_f825) and (cons_f826)
                                        yield 92, subst1
                                subjects2.appendleft(tmp167)
                    subjects151.appendleft(tmp165)
                if len(subjects151) >= 1 and isinstance(subjects151[0], Add):
                    tmp168 = subjects151.popleft()
                    associative1 = tmp168
                    associative_type1 = type(tmp168)
                    subjects169 = deque(tmp168._args)
                    matcher = CommutativeMatcher130179.get()
                    tmp170 = subjects169
                    subjects169 = []
                    for s in tmp170:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp170, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 130192
                            if len(subjects151) == 0:
                                pass
                                # State 130193
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp171 = subjects2.popleft()
                                    # State 130194
                                    if len(subjects2) == 0:
                                        pass
                                        # State 130195
                                        if len(subjects) == 0:
                                            pass
                                            # 88: 1/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                            yield 88, subst1
                                            # 90: 1/sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                            yield 90, subst1
                                            # 86: 1/sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                            yield 86, subst1
                                    subjects2.appendleft(tmp171)
                    subjects151.appendleft(tmp168)
                subjects2.appendleft(tmp150)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp172 = subjects.popleft()
            subjects173 = deque(tmp172._args)
            # State 19377
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 19378
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 19379
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 19380
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 19381
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i3.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 19382
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 19383
                                    if len(subjects173) >= 1:
                                        tmp180 = subjects173.popleft()
                                        subst7 = Substitution(subst6)
                                        try:
                                            subst7.try_add_variable('i3.1.2.2.2.1.0', tmp180)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 19384
                                            if len(subjects173) == 0:
                                                pass
                                                # State 19385
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                    yield 8, subst7
                                                    # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                    yield 9, subst7
                                                    # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                    yield 6, subst7
                                                    # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                    yield 7, subst7
                                        subjects173.appendleft(tmp180)
                                if len(subjects173) >= 1 and isinstance(subjects173[0], Mul):
                                    tmp182 = subjects173.popleft()
                                    associative1 = tmp182
                                    associative_type1 = type(tmp182)
                                    subjects183 = deque(tmp182._args)
                                    matcher = CommutativeMatcher19387.get()
                                    tmp184 = subjects183
                                    subjects183 = []
                                    for s in tmp184:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp184, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 19388
                                            if len(subjects173) == 0:
                                                pass
                                                # State 19389
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                    yield 8, subst6
                                                    # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                    yield 9, subst6
                                                    # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                    yield 6, subst6
                                                    # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                    yield 7, subst6
                                    subjects173.appendleft(tmp182)
                            if len(subjects173) >= 1 and isinstance(subjects173[0], Add):
                                tmp185 = subjects173.popleft()
                                associative1 = tmp185
                                associative_type1 = type(tmp185)
                                subjects186 = deque(tmp185._args)
                                matcher = CommutativeMatcher19391.get()
                                tmp187 = subjects186
                                subjects186 = []
                                for s in tmp187:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp187, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 19397
                                        if len(subjects173) == 0:
                                            pass
                                            # State 19398
                                            if len(subjects) == 0:
                                                pass
                                                # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                yield 8, subst5
                                                # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                yield 9, subst5
                                                # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                yield 6, subst5
                                                # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                yield 7, subst5
                                subjects173.appendleft(tmp185)
                        if len(subjects173) >= 1 and isinstance(subjects173[0], Pow):
                            tmp188 = subjects173.popleft()
                            subjects189 = deque(tmp188._args)
                            # State 19399
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 19400
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 19401
                                    if len(subjects189) >= 1:
                                        tmp192 = subjects189.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i3.1.2.2.2.1.0', tmp192)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 19402
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i3.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19403
                                                if len(subjects189) == 0:
                                                    pass
                                                    # State 19404
                                                    if len(subjects173) == 0:
                                                        pass
                                                        # State 19405
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                            yield 8, subst7
                                                            # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                            yield 9, subst7
                                                            # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                            yield 6, subst7
                                                            # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                            yield 7, subst7
                                            if len(subjects189) >= 1:
                                                tmp195 = subjects189.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i3.1.2.2.2', tmp195)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 19403
                                                    if len(subjects189) == 0:
                                                        pass
                                                        # State 19404
                                                        if len(subjects173) == 0:
                                                            pass
                                                            # State 19405
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                yield 8, subst7
                                                                # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                yield 9, subst7
                                                                # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                yield 6, subst7
                                                                # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                yield 7, subst7
                                                subjects189.appendleft(tmp195)
                                        subjects189.appendleft(tmp192)
                                if len(subjects189) >= 1 and isinstance(subjects189[0], Mul):
                                    tmp197 = subjects189.popleft()
                                    associative1 = tmp197
                                    associative_type1 = type(tmp197)
                                    subjects198 = deque(tmp197._args)
                                    matcher = CommutativeMatcher19407.get()
                                    tmp199 = subjects198
                                    subjects198 = []
                                    for s in tmp199:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp199, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 19408
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i3.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19409
                                                if len(subjects189) == 0:
                                                    pass
                                                    # State 19410
                                                    if len(subjects173) == 0:
                                                        pass
                                                        # State 19411
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                            yield 8, subst6
                                                            # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                            yield 9, subst6
                                                            # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                            yield 6, subst6
                                                            # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                            yield 7, subst6
                                            if len(subjects189) >= 1:
                                                tmp201 = []
                                                tmp201.append(subjects189.popleft())
                                                while True:
                                                    if len(tmp201) > 1:
                                                        tmp202 = create_operation_expression(associative1, tmp201)
                                                    elif len(tmp201) == 1:
                                                        tmp202 = tmp201[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i3.1.2.2.2', tmp202)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 19409
                                                        if len(subjects189) == 0:
                                                            pass
                                                            # State 19410
                                                            if len(subjects173) == 0:
                                                                pass
                                                                # State 19411
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                    yield 8, subst6
                                                                    # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                    yield 9, subst6
                                                                    # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                    yield 6, subst6
                                                                    # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                    yield 7, subst6
                                                    if len(subjects189) == 0:
                                                        break
                                                    tmp201.append(subjects189.popleft())
                                                subjects189.extendleft(reversed(tmp201))
                                    subjects189.appendleft(tmp197)
                            if len(subjects189) >= 1 and isinstance(subjects189[0], Add):
                                tmp204 = subjects189.popleft()
                                associative1 = tmp204
                                associative_type1 = type(tmp204)
                                subjects205 = deque(tmp204._args)
                                matcher = CommutativeMatcher19413.get()
                                tmp206 = subjects205
                                subjects205 = []
                                for s in tmp206:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp206, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 19419
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 19420
                                            if len(subjects189) == 0:
                                                pass
                                                # State 19421
                                                if len(subjects173) == 0:
                                                    pass
                                                    # State 19422
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                        yield 8, subst5
                                                        # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                        yield 9, subst5
                                                        # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                        yield 6, subst5
                                                        # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                        yield 7, subst5
                                        if len(subjects189) >= 1:
                                            tmp208 = []
                                            tmp208.append(subjects189.popleft())
                                            while True:
                                                if len(tmp208) > 1:
                                                    tmp209 = create_operation_expression(associative1, tmp208)
                                                elif len(tmp208) == 1:
                                                    tmp209 = tmp208[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.1.2.2.2', tmp209)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 19420
                                                    if len(subjects189) == 0:
                                                        pass
                                                        # State 19421
                                                        if len(subjects173) == 0:
                                                            pass
                                                            # State 19422
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                yield 8, subst5
                                                                # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                yield 9, subst5
                                                                # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                yield 6, subst5
                                                                # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                yield 7, subst5
                                                if len(subjects189) == 0:
                                                    break
                                                tmp208.append(subjects189.popleft())
                                            subjects189.extendleft(reversed(tmp208))
                                subjects189.appendleft(tmp204)
                            subjects173.appendleft(tmp188)
                    if len(subjects173) >= 1:
                        tmp211 = subjects173.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1', tmp211)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53166
                            if len(subjects173) == 0:
                                pass
                                # State 53167
                                if len(subjects) == 0:
                                    pass
                                    # 12: log(c*RFx**p) /; (cons_f8) and (cons_f5) and (cons_f1200)
                                    yield 12, subst3
                        subjects173.appendleft(tmp211)
                    if len(subjects173) >= 1 and isinstance(subjects173[0], Mul):
                        tmp213 = subjects173.popleft()
                        associative1 = tmp213
                        associative_type1 = type(tmp213)
                        subjects214 = deque(tmp213._args)
                        matcher = CommutativeMatcher19424.get()
                        tmp215 = subjects214
                        subjects214 = []
                        for s in tmp215:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp215, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 19461
                                if len(subjects173) == 0:
                                    pass
                                    # State 19462
                                    if len(subjects) == 0:
                                        pass
                                        # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                        yield 8, subst3
                                        # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                        yield 9, subst3
                                        # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                        yield 6, subst3
                                        # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                        yield 7, subst3
                        subjects173.appendleft(tmp213)
                    if len(subjects173) >= 1 and isinstance(subjects173[0], Add):
                        tmp216 = subjects173.popleft()
                        associative1 = tmp216
                        associative_type1 = type(tmp216)
                        subjects217 = deque(tmp216._args)
                        matcher = CommutativeMatcher50595.get()
                        tmp218 = subjects217
                        subjects217 = []
                        for s in tmp218:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp218, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 50608
                                if len(subjects173) == 0:
                                    pass
                                    # State 50609
                                    if len(subjects) == 0:
                                        pass
                                        # 10: log(c*(d + e*x**2)**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5)
                                        yield 10, subst3
                            if pattern_index == 1:
                                pass
                                # State 52583
                                if len(subjects173) == 0:
                                    pass
                                    # State 52584
                                    if len(subjects) == 0:
                                        pass
                                        # 11: log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                                        yield 11, subst3
                        subjects173.appendleft(tmp216)
                if len(subjects173) >= 1 and isinstance(subjects173[0], Pow):
                    tmp219 = subjects173.popleft()
                    subjects220 = deque(tmp219._args)
                    # State 19463
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 19464
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 19465
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 19466
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 19467
                                    if len(subjects220) >= 1:
                                        tmp225 = subjects220.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i3.1.2.2.2.1.0', tmp225)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 19468
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i3.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19469
                                                if len(subjects220) == 0:
                                                    pass
                                                    # State 19470
                                                    if len(subjects173) == 0:
                                                        pass
                                                        # State 19471
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                            yield 8, subst7
                                                            # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                            yield 9, subst7
                                                            # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                            yield 6, subst7
                                                            # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                            yield 7, subst7
                                            if len(subjects220) >= 1:
                                                tmp228 = subjects220.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i3.1.2.2', tmp228)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 19469
                                                    if len(subjects220) == 0:
                                                        pass
                                                        # State 19470
                                                        if len(subjects173) == 0:
                                                            pass
                                                            # State 19471
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                yield 8, subst7
                                                                # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                yield 9, subst7
                                                                # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                yield 6, subst7
                                                                # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                yield 7, subst7
                                                subjects220.appendleft(tmp228)
                                        subjects220.appendleft(tmp225)
                                if len(subjects220) >= 1 and isinstance(subjects220[0], Mul):
                                    tmp230 = subjects220.popleft()
                                    associative1 = tmp230
                                    associative_type1 = type(tmp230)
                                    subjects231 = deque(tmp230._args)
                                    matcher = CommutativeMatcher19473.get()
                                    tmp232 = subjects231
                                    subjects231 = []
                                    for s in tmp232:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp232, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 19474
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i3.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19475
                                                if len(subjects220) == 0:
                                                    pass
                                                    # State 19476
                                                    if len(subjects173) == 0:
                                                        pass
                                                        # State 19477
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                            yield 8, subst6
                                                            # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                            yield 9, subst6
                                                            # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                            yield 6, subst6
                                                            # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                            yield 7, subst6
                                            if len(subjects220) >= 1:
                                                tmp234 = []
                                                tmp234.append(subjects220.popleft())
                                                while True:
                                                    if len(tmp234) > 1:
                                                        tmp235 = create_operation_expression(associative1, tmp234)
                                                    elif len(tmp234) == 1:
                                                        tmp235 = tmp234[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i3.1.2.2', tmp235)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 19475
                                                        if len(subjects220) == 0:
                                                            pass
                                                            # State 19476
                                                            if len(subjects173) == 0:
                                                                pass
                                                                # State 19477
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                    yield 8, subst6
                                                                    # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                    yield 9, subst6
                                                                    # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                    yield 6, subst6
                                                                    # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                    yield 7, subst6
                                                    if len(subjects220) == 0:
                                                        break
                                                    tmp234.append(subjects220.popleft())
                                                subjects220.extendleft(reversed(tmp234))
                                    subjects220.appendleft(tmp230)
                            if len(subjects220) >= 1 and isinstance(subjects220[0], Add):
                                tmp237 = subjects220.popleft()
                                associative1 = tmp237
                                associative_type1 = type(tmp237)
                                subjects238 = deque(tmp237._args)
                                matcher = CommutativeMatcher19479.get()
                                tmp239 = subjects238
                                subjects238 = []
                                for s in tmp239:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp239, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 19485
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 19486
                                            if len(subjects220) == 0:
                                                pass
                                                # State 19487
                                                if len(subjects173) == 0:
                                                    pass
                                                    # State 19488
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                        yield 8, subst5
                                                        # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                        yield 9, subst5
                                                        # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                        yield 6, subst5
                                                        # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                        yield 7, subst5
                                        if len(subjects220) >= 1:
                                            tmp241 = []
                                            tmp241.append(subjects220.popleft())
                                            while True:
                                                if len(tmp241) > 1:
                                                    tmp242 = create_operation_expression(associative1, tmp241)
                                                elif len(tmp241) == 1:
                                                    tmp242 = tmp241[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.1.2.2', tmp242)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 19486
                                                    if len(subjects220) == 0:
                                                        pass
                                                        # State 19487
                                                        if len(subjects173) == 0:
                                                            pass
                                                            # State 19488
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                yield 8, subst5
                                                                # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                yield 9, subst5
                                                                # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                yield 6, subst5
                                                                # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                yield 7, subst5
                                                if len(subjects220) == 0:
                                                    break
                                                tmp241.append(subjects220.popleft())
                                            subjects220.extendleft(reversed(tmp241))
                                subjects220.appendleft(tmp237)
                        if len(subjects220) >= 1 and isinstance(subjects220[0], Pow):
                            tmp244 = subjects220.popleft()
                            subjects245 = deque(tmp244._args)
                            # State 19489
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 19490
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 19491
                                    if len(subjects245) >= 1:
                                        tmp248 = subjects245.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.2.2.2.1.0', tmp248)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 19492
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i3.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19493
                                                if len(subjects245) == 0:
                                                    pass
                                                    # State 19494
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i3.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 19495
                                                        if len(subjects220) == 0:
                                                            pass
                                                            # State 19496
                                                            if len(subjects173) == 0:
                                                                pass
                                                                # State 19497
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                    yield 8, subst7
                                                                    # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                    yield 9, subst7
                                                                    # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                    yield 6, subst7
                                                                    # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                    yield 7, subst7
                                                    if len(subjects220) >= 1:
                                                        tmp252 = subjects220.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i3.1.2.2', tmp252)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 19495
                                                            if len(subjects220) == 0:
                                                                pass
                                                                # State 19496
                                                                if len(subjects173) == 0:
                                                                    pass
                                                                    # State 19497
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                        yield 8, subst7
                                                                        # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                        yield 9, subst7
                                                                        # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                        yield 6, subst7
                                                                        # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                        yield 7, subst7
                                                        subjects220.appendleft(tmp252)
                                            if len(subjects245) >= 1:
                                                tmp254 = subjects245.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i3.1.2.2.2', tmp254)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 19493
                                                    if len(subjects245) == 0:
                                                        pass
                                                        # State 19494
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i3.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 19495
                                                            if len(subjects220) == 0:
                                                                pass
                                                                # State 19496
                                                                if len(subjects173) == 0:
                                                                    pass
                                                                    # State 19497
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                        yield 8, subst7
                                                                        # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                        yield 9, subst7
                                                                        # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                        yield 6, subst7
                                                                        # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                        yield 7, subst7
                                                        if len(subjects220) >= 1:
                                                            tmp257 = subjects220.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i3.1.2.2', tmp257)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 19495
                                                                if len(subjects220) == 0:
                                                                    pass
                                                                    # State 19496
                                                                    if len(subjects173) == 0:
                                                                        pass
                                                                        # State 19497
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                            yield 8, subst7
                                                                            # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                            yield 9, subst7
                                                                            # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                            yield 6, subst7
                                                                            # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                            yield 7, subst7
                                                            subjects220.appendleft(tmp257)
                                                subjects245.appendleft(tmp254)
                                        subjects245.appendleft(tmp248)
                                if len(subjects245) >= 1 and isinstance(subjects245[0], Mul):
                                    tmp259 = subjects245.popleft()
                                    associative1 = tmp259
                                    associative_type1 = type(tmp259)
                                    subjects260 = deque(tmp259._args)
                                    matcher = CommutativeMatcher19499.get()
                                    tmp261 = subjects260
                                    subjects260 = []
                                    for s in tmp261:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp261, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 19500
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i3.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 19501
                                                if len(subjects245) == 0:
                                                    pass
                                                    # State 19502
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i3.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 19503
                                                        if len(subjects220) == 0:
                                                            pass
                                                            # State 19504
                                                            if len(subjects173) == 0:
                                                                pass
                                                                # State 19505
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                    yield 8, subst6
                                                                    # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                    yield 9, subst6
                                                                    # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                    yield 6, subst6
                                                                    # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                    yield 7, subst6
                                                    if len(subjects220) >= 1:
                                                        tmp264 = subjects220.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i3.1.2.2', tmp264)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 19503
                                                            if len(subjects220) == 0:
                                                                pass
                                                                # State 19504
                                                                if len(subjects173) == 0:
                                                                    pass
                                                                    # State 19505
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                        yield 8, subst6
                                                                        # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                        yield 9, subst6
                                                                        # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                        yield 6, subst6
                                                                        # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                        yield 7, subst6
                                                        subjects220.appendleft(tmp264)
                                            if len(subjects245) >= 1:
                                                tmp266 = []
                                                tmp266.append(subjects245.popleft())
                                                while True:
                                                    if len(tmp266) > 1:
                                                        tmp267 = create_operation_expression(associative1, tmp266)
                                                    elif len(tmp266) == 1:
                                                        tmp267 = tmp266[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.2.2.2', tmp267)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 19501
                                                        if len(subjects245) == 0:
                                                            pass
                                                            # State 19502
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i3.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 19503
                                                                if len(subjects220) == 0:
                                                                    pass
                                                                    # State 19504
                                                                    if len(subjects173) == 0:
                                                                        pass
                                                                        # State 19505
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                            yield 8, subst6
                                                                            # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                            yield 9, subst6
                                                                            # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                            yield 6, subst6
                                                                            # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                            yield 7, subst6
                                                            if len(subjects220) >= 1:
                                                                tmp270 = subjects220.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i3.1.2.2', tmp270)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 19503
                                                                    if len(subjects220) == 0:
                                                                        pass
                                                                        # State 19504
                                                                        if len(subjects173) == 0:
                                                                            pass
                                                                            # State 19505
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                                yield 8, subst6
                                                                                # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                                yield 9, subst6
                                                                                # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                                yield 6, subst6
                                                                                # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                                yield 7, subst6
                                                                subjects220.appendleft(tmp270)
                                                    if len(subjects245) == 0:
                                                        break
                                                    tmp266.append(subjects245.popleft())
                                                subjects245.extendleft(reversed(tmp266))
                                    subjects245.appendleft(tmp259)
                            if len(subjects245) >= 1 and isinstance(subjects245[0], Add):
                                tmp272 = subjects245.popleft()
                                associative1 = tmp272
                                associative_type1 = type(tmp272)
                                subjects273 = deque(tmp272._args)
                                matcher = CommutativeMatcher19507.get()
                                tmp274 = subjects273
                                subjects273 = []
                                for s in tmp274:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp274, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 19513
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 19514
                                            if len(subjects245) == 0:
                                                pass
                                                # State 19515
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 19516
                                                    if len(subjects220) == 0:
                                                        pass
                                                        # State 19517
                                                        if len(subjects173) == 0:
                                                            pass
                                                            # State 19518
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                yield 8, subst5
                                                                # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                yield 9, subst5
                                                                # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                yield 6, subst5
                                                                # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                yield 7, subst5
                                                if len(subjects220) >= 1:
                                                    tmp277 = subjects220.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.2.2', tmp277)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 19516
                                                        if len(subjects220) == 0:
                                                            pass
                                                            # State 19517
                                                            if len(subjects173) == 0:
                                                                pass
                                                                # State 19518
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                    yield 8, subst5
                                                                    # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                    yield 9, subst5
                                                                    # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                    yield 6, subst5
                                                                    # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                    yield 7, subst5
                                                    subjects220.appendleft(tmp277)
                                        if len(subjects245) >= 1:
                                            tmp279 = []
                                            tmp279.append(subjects245.popleft())
                                            while True:
                                                if len(tmp279) > 1:
                                                    tmp280 = create_operation_expression(associative1, tmp279)
                                                elif len(tmp279) == 1:
                                                    tmp280 = tmp279[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.2.2.2', tmp280)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 19514
                                                    if len(subjects245) == 0:
                                                        pass
                                                        # State 19515
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i3.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 19516
                                                            if len(subjects220) == 0:
                                                                pass
                                                                # State 19517
                                                                if len(subjects173) == 0:
                                                                    pass
                                                                    # State 19518
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                        yield 8, subst5
                                                                        # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                        yield 9, subst5
                                                                        # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                        yield 6, subst5
                                                                        # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                        yield 7, subst5
                                                        if len(subjects220) >= 1:
                                                            tmp283 = subjects220.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i3.1.2.2', tmp283)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 19516
                                                                if len(subjects220) == 0:
                                                                    pass
                                                                    # State 19517
                                                                    if len(subjects173) == 0:
                                                                        pass
                                                                        # State 19518
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                                            yield 8, subst5
                                                                            # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                                            yield 9, subst5
                                                                            # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                                            yield 6, subst5
                                                                            # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                                            yield 7, subst5
                                                            subjects220.appendleft(tmp283)
                                                if len(subjects245) == 0:
                                                    break
                                                tmp279.append(subjects245.popleft())
                                            subjects245.extendleft(reversed(tmp279))
                                subjects245.appendleft(tmp272)
                            subjects220.appendleft(tmp244)
                    if len(subjects220) >= 1:
                        tmp285 = subjects220.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.1', tmp285)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53168
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53169
                                if len(subjects220) == 0:
                                    pass
                                    # State 53170
                                    if len(subjects173) == 0:
                                        pass
                                        # State 53171
                                        if len(subjects) == 0:
                                            pass
                                            # 12: log(c*RFx**p) /; (cons_f8) and (cons_f5) and (cons_f1200)
                                            yield 12, subst3
                            if len(subjects220) >= 1:
                                tmp288 = subjects220.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', tmp288)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53169
                                    if len(subjects220) == 0:
                                        pass
                                        # State 53170
                                        if len(subjects173) == 0:
                                            pass
                                            # State 53171
                                            if len(subjects) == 0:
                                                pass
                                                # 12: log(c*RFx**p) /; (cons_f8) and (cons_f5) and (cons_f1200)
                                                yield 12, subst3
                                subjects220.appendleft(tmp288)
                        subjects220.appendleft(tmp285)
                    if len(subjects220) >= 1 and isinstance(subjects220[0], Mul):
                        tmp290 = subjects220.popleft()
                        associative1 = tmp290
                        associative_type1 = type(tmp290)
                        subjects291 = deque(tmp290._args)
                        matcher = CommutativeMatcher19520.get()
                        tmp292 = subjects291
                        subjects291 = []
                        for s in tmp292:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp292, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 19557
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 19558
                                    if len(subjects220) == 0:
                                        pass
                                        # State 19559
                                        if len(subjects173) == 0:
                                            pass
                                            # State 19560
                                            if len(subjects) == 0:
                                                pass
                                                # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                yield 8, subst3
                                                # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                yield 9, subst3
                                                # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                yield 6, subst3
                                                # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                yield 7, subst3
                                if len(subjects220) >= 1:
                                    tmp294 = []
                                    tmp294.append(subjects220.popleft())
                                    while True:
                                        if len(tmp294) > 1:
                                            tmp295 = create_operation_expression(associative1, tmp294)
                                        elif len(tmp294) == 1:
                                            tmp295 = tmp294[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2.2', tmp295)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 19558
                                            if len(subjects220) == 0:
                                                pass
                                                # State 19559
                                                if len(subjects173) == 0:
                                                    pass
                                                    # State 19560
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                                        yield 8, subst3
                                                        # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                                        yield 9, subst3
                                                        # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                                        yield 6, subst3
                                                        # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                                        yield 7, subst3
                                        if len(subjects220) == 0:
                                            break
                                        tmp294.append(subjects220.popleft())
                                    subjects220.extendleft(reversed(tmp294))
                        subjects220.appendleft(tmp290)
                    if len(subjects220) >= 1 and isinstance(subjects220[0], Add):
                        tmp297 = subjects220.popleft()
                        associative1 = tmp297
                        associative_type1 = type(tmp297)
                        subjects298 = deque(tmp297._args)
                        matcher = CommutativeMatcher50611.get()
                        tmp299 = subjects298
                        subjects298 = []
                        for s in tmp299:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp299, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 50624
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 50625
                                    if len(subjects220) == 0:
                                        pass
                                        # State 50626
                                        if len(subjects173) == 0:
                                            pass
                                            # State 50627
                                            if len(subjects) == 0:
                                                pass
                                                # 10: log(c*(d + e*x**2)**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5)
                                                yield 10, subst3
                                if len(subjects220) >= 1:
                                    tmp301 = []
                                    tmp301.append(subjects220.popleft())
                                    while True:
                                        if len(tmp301) > 1:
                                            tmp302 = create_operation_expression(associative1, tmp301)
                                        elif len(tmp301) == 1:
                                            tmp302 = tmp301[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2.2', tmp302)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 50625
                                            if len(subjects220) == 0:
                                                pass
                                                # State 50626
                                                if len(subjects173) == 0:
                                                    pass
                                                    # State 50627
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 10: log(c*(d + e*x**2)**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5)
                                                        yield 10, subst3
                                        if len(subjects220) == 0:
                                            break
                                        tmp301.append(subjects220.popleft())
                                    subjects220.extendleft(reversed(tmp301))
                            if pattern_index == 1:
                                pass
                                # State 52626
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 52627
                                    if len(subjects220) == 0:
                                        pass
                                        # State 52628
                                        if len(subjects173) == 0:
                                            pass
                                            # State 52629
                                            if len(subjects) == 0:
                                                pass
                                                # 11: log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                                                yield 11, subst3
                                if len(subjects220) >= 1:
                                    tmp305 = []
                                    tmp305.append(subjects220.popleft())
                                    while True:
                                        if len(tmp305) > 1:
                                            tmp306 = create_operation_expression(associative1, tmp305)
                                        elif len(tmp305) == 1:
                                            tmp306 = tmp305[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.2.2', tmp306)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 52627
                                            if len(subjects220) == 0:
                                                pass
                                                # State 52628
                                                if len(subjects173) == 0:
                                                    pass
                                                    # State 52629
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 11: log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                                                        yield 11, subst3
                                        if len(subjects220) == 0:
                                            break
                                        tmp305.append(subjects220.popleft())
                                    subjects220.extendleft(reversed(tmp305))
                        subjects220.appendleft(tmp297)
                    subjects173.appendleft(tmp219)
            if len(subjects173) >= 1 and isinstance(subjects173[0], Mul):
                tmp308 = subjects173.popleft()
                associative1 = tmp308
                associative_type1 = type(tmp308)
                subjects309 = deque(tmp308._args)
                matcher = CommutativeMatcher19562.get()
                tmp310 = subjects309
                subjects309 = []
                for s in tmp310:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp310, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 19731
                        if len(subjects173) == 0:
                            pass
                            # State 19732
                            if len(subjects) == 0:
                                pass
                                # 8: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1160)
                                yield 8, subst1
                                # 9: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f1161)
                                yield 9, subst1
                                # 6: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52)
                                yield 6, subst1
                                # 7: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f5) and (cons_f52) and (cons_f417)
                                yield 7, subst1
                    if pattern_index == 1:
                        pass
                        # State 50660
                        if len(subjects173) == 0:
                            pass
                            # State 50661
                            if len(subjects) == 0:
                                pass
                                # 10: log(c*(d + e*x**2)**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5)
                                yield 10, subst1
                    if pattern_index == 2:
                        pass
                        # State 52716
                        if len(subjects173) == 0:
                            pass
                            # State 52717
                            if len(subjects) == 0:
                                pass
                                # 11: log(c*(d + e/(f + x*g))**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f5)
                                yield 11, subst1
                    if pattern_index == 3:
                        pass
                        # State 53176
                        if len(subjects173) == 0:
                            pass
                            # State 53177
                            if len(subjects) == 0:
                                pass
                                # 12: log(c*RFx**p) /; (cons_f8) and (cons_f5) and (cons_f1200)
                                yield 12, subst1
                subjects173.appendleft(tmp308)
            subjects.appendleft(tmp172)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp311 = subjects.popleft()
            subjects312 = deque(tmp311._args)
            # State 72681
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 72682
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 72683
                    if len(subjects312) >= 1 and isinstance(subjects312[0], Pow):
                        tmp315 = subjects312.popleft()
                        subjects316 = deque(tmp315._args)
                        # State 72684
                        if len(subjects316) >= 1:
                            tmp317 = subjects316.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp317)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 72685
                                if len(subjects316) >= 1:
                                    tmp319 = subjects316.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp319)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 72686
                                        if len(subjects316) == 0:
                                            pass
                                            # State 72687
                                            if len(subjects312) == 0:
                                                pass
                                                # State 72688
                                                if len(subjects) == 0:
                                                    pass
                                                    # 13: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                                    yield 13, subst4
                                                    # 15: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                                    yield 15, subst4
                                                    # 17: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                    yield 17, subst4
                                                    # 19: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                    yield 19, subst4
                                                    # 21: sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    yield 21, subst4
                                                    # 23: sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                                    yield 23, subst4
                                    subjects316.appendleft(tmp319)
                            subjects316.appendleft(tmp317)
                        subjects312.appendleft(tmp315)
                if len(subjects312) >= 1 and isinstance(subjects312[0], Mul):
                    tmp321 = subjects312.popleft()
                    associative1 = tmp321
                    associative_type1 = type(tmp321)
                    subjects322 = deque(tmp321._args)
                    matcher = CommutativeMatcher72690.get()
                    tmp323 = subjects322
                    subjects322 = []
                    for s in tmp323:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp323, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 72695
                            if len(subjects312) == 0:
                                pass
                                # State 72696
                                if len(subjects) == 0:
                                    pass
                                    # 13: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                    yield 13, subst2
                                    # 15: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    yield 15, subst2
                                    # 17: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    yield 17, subst2
                                    # 19: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 19, subst2
                                    # 21: sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 21, subst2
                                    # 23: sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                    yield 23, subst2
                    subjects312.appendleft(tmp321)
            if len(subjects312) >= 1:
                tmp324 = subjects312.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp324)
                except ValueError:
                    pass
                else:
                    pass
                    # State 73524
                    if len(subjects312) == 0:
                        pass
                        # State 73525
                        if len(subjects) == 0:
                            pass
                            # 25: sin(u) /; (cons_f825) and (cons_f826)
                            yield 25, subst1
                subjects312.appendleft(tmp324)
            if len(subjects312) >= 1 and isinstance(subjects312[0], Add):
                tmp326 = subjects312.popleft()
                associative1 = tmp326
                associative_type1 = type(tmp326)
                subjects327 = deque(tmp326._args)
                matcher = CommutativeMatcher72698.get()
                tmp328 = subjects327
                subjects327 = []
                for s in tmp328:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp328, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 72711
                        if len(subjects312) == 0:
                            pass
                            # State 72712
                            if len(subjects) == 0:
                                pass
                                # 13: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                yield 13, subst1
                                # 15: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                yield 15, subst1
                                # 17: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                yield 17, subst1
                                # 19: sin(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                yield 19, subst1
                                # 21: sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                yield 21, subst1
                                # 23: sin(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                yield 23, subst1
                subjects312.appendleft(tmp326)
            subjects.appendleft(tmp311)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp329 = subjects.popleft()
            subjects330 = deque(tmp329._args)
            # State 72816
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 72817
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 72818
                    if len(subjects330) >= 1 and isinstance(subjects330[0], Pow):
                        tmp333 = subjects330.popleft()
                        subjects334 = deque(tmp333._args)
                        # State 72819
                        if len(subjects334) >= 1:
                            tmp335 = subjects334.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp335)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 72820
                                if len(subjects334) >= 1:
                                    tmp337 = subjects334.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp337)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 72821
                                        if len(subjects334) == 0:
                                            pass
                                            # State 72822
                                            if len(subjects330) == 0:
                                                pass
                                                # State 72823
                                                if len(subjects) == 0:
                                                    pass
                                                    # 14: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                                    yield 14, subst4
                                                    # 16: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                                    yield 16, subst4
                                                    # 18: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                    yield 18, subst4
                                                    # 20: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                    yield 20, subst4
                                                    # 22: cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    yield 22, subst4
                                                    # 24: cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                                    yield 24, subst4
                                    subjects334.appendleft(tmp337)
                            subjects334.appendleft(tmp335)
                        subjects330.appendleft(tmp333)
                if len(subjects330) >= 1 and isinstance(subjects330[0], Mul):
                    tmp339 = subjects330.popleft()
                    associative1 = tmp339
                    associative_type1 = type(tmp339)
                    subjects340 = deque(tmp339._args)
                    matcher = CommutativeMatcher72825.get()
                    tmp341 = subjects340
                    subjects340 = []
                    for s in tmp341:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp341, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 72830
                            if len(subjects330) == 0:
                                pass
                                # State 72831
                                if len(subjects) == 0:
                                    pass
                                    # 14: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                    yield 14, subst2
                                    # 16: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    yield 16, subst2
                                    # 18: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    yield 18, subst2
                                    # 20: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 20, subst2
                                    # 22: cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 22, subst2
                                    # 24: cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                    yield 24, subst2
                    subjects330.appendleft(tmp339)
            if len(subjects330) >= 1:
                tmp342 = subjects330.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp342)
                except ValueError:
                    pass
                else:
                    pass
                    # State 73564
                    if len(subjects330) == 0:
                        pass
                        # State 73565
                        if len(subjects) == 0:
                            pass
                            # 26: cos(u) /; (cons_f825) and (cons_f826)
                            yield 26, subst1
                subjects330.appendleft(tmp342)
            if len(subjects330) >= 1 and isinstance(subjects330[0], Add):
                tmp344 = subjects330.popleft()
                associative1 = tmp344
                associative_type1 = type(tmp344)
                subjects345 = deque(tmp344._args)
                matcher = CommutativeMatcher72833.get()
                tmp346 = subjects345
                subjects345 = []
                for s in tmp346:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp346, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 72846
                        if len(subjects330) == 0:
                            pass
                            # State 72847
                            if len(subjects) == 0:
                                pass
                                # 14: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                yield 14, subst1
                                # 16: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                yield 16, subst1
                                # 18: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                yield 18, subst1
                                # 20: cos(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                yield 20, subst1
                                # 22: cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                yield 22, subst1
                                # 24: cos(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                yield 24, subst1
                subjects330.appendleft(tmp344)
            subjects.appendleft(tmp329)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp347 = subjects.popleft()
            subjects348 = deque(tmp347._args)
            # State 87272
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 87273
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 87274
                    if len(subjects348) >= 1 and isinstance(subjects348[0], Pow):
                        tmp351 = subjects348.popleft()
                        subjects352 = deque(tmp351._args)
                        # State 87275
                        if len(subjects352) >= 1:
                            tmp353 = subjects352.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp353)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 87276
                                if len(subjects352) >= 1:
                                    tmp355 = subjects352.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp355)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 87277
                                        if len(subjects352) == 0:
                                            pass
                                            # State 87278
                                            if len(subjects348) == 0:
                                                pass
                                                # State 87279
                                                if len(subjects) == 0:
                                                    pass
                                                    # 27: tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                    yield 27, subst4
                                                    # 29: tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    yield 29, subst4
                                                    # 31: tan(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    yield 31, subst4
                                    subjects352.appendleft(tmp355)
                            subjects352.appendleft(tmp353)
                        subjects348.appendleft(tmp351)
                if len(subjects348) >= 1 and isinstance(subjects348[0], Mul):
                    tmp357 = subjects348.popleft()
                    associative1 = tmp357
                    associative_type1 = type(tmp357)
                    subjects358 = deque(tmp357._args)
                    matcher = CommutativeMatcher87281.get()
                    tmp359 = subjects358
                    subjects358 = []
                    for s in tmp359:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp359, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 87286
                            if len(subjects348) == 0:
                                pass
                                # State 87287
                                if len(subjects) == 0:
                                    pass
                                    # 27: tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                    yield 27, subst2
                                    # 29: tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                    yield 29, subst2
                                    # 31: tan(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 31, subst2
                    subjects348.appendleft(tmp357)
            if len(subjects348) >= 1:
                tmp360 = subjects348.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp360)
                except ValueError:
                    pass
                else:
                    pass
                    # State 87862
                    if len(subjects348) == 0:
                        pass
                        # State 87863
                        if len(subjects) == 0:
                            pass
                            # 33: tan(u) /; (cons_f825) and (cons_f826)
                            yield 33, subst1
                subjects348.appendleft(tmp360)
            if len(subjects348) >= 1 and isinstance(subjects348[0], Add):
                tmp362 = subjects348.popleft()
                associative1 = tmp362
                associative_type1 = type(tmp362)
                subjects363 = deque(tmp362._args)
                matcher = CommutativeMatcher87289.get()
                tmp364 = subjects363
                subjects363 = []
                for s in tmp364:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp364, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 87302
                        if len(subjects348) == 0:
                            pass
                            # State 87303
                            if len(subjects) == 0:
                                pass
                                # 27: tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                yield 27, subst1
                                # 29: tan(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                yield 29, subst1
                                # 31: tan(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                yield 31, subst1
                subjects348.appendleft(tmp362)
            subjects.appendleft(tmp347)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp365 = subjects.popleft()
            subjects366 = deque(tmp365._args)
            # State 108014
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108015
                if len(subjects366) >= 1:
                    tmp368 = subjects366.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp368)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108016
                        if len(subjects366) == 0:
                            pass
                            # State 108017
                            if len(subjects) == 0:
                                pass
                                # 43: asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 43, subst2
                                # 45: asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 45, subst2
                    subjects366.appendleft(tmp368)
            if len(subjects366) >= 1 and isinstance(subjects366[0], Mul):
                tmp370 = subjects366.popleft()
                associative1 = tmp370
                associative_type1 = type(tmp370)
                subjects371 = deque(tmp370._args)
                matcher = CommutativeMatcher108019.get()
                tmp372 = subjects371
                subjects371 = []
                for s in tmp372:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp372, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108020
                        if len(subjects366) == 0:
                            pass
                            # State 108021
                            if len(subjects) == 0:
                                pass
                                # 43: asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 43, subst1
                                # 45: asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 45, subst1
                subjects366.appendleft(tmp370)
            if len(subjects366) >= 1 and isinstance(subjects366[0], Add):
                tmp373 = subjects366.popleft()
                associative1 = tmp373
                associative_type1 = type(tmp373)
                subjects374 = deque(tmp373._args)
                matcher = CommutativeMatcher110313.get()
                tmp375 = subjects374
                subjects374 = []
                for s in tmp375:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp375, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110319
                        if len(subjects366) == 0:
                            pass
                            # State 110320
                            if len(subjects) == 0:
                                pass
                                # 47: asin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                                yield 47, subst1
                    if pattern_index == 1:
                        pass
                        # State 110699
                        if len(subjects366) == 0:
                            pass
                            # State 110700
                            if len(subjects) == 0:
                                pass
                                # 49: asin(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1766)
                                yield 49, subst1
                subjects366.appendleft(tmp373)
            subjects.appendleft(tmp365)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp376 = subjects.popleft()
            subjects377 = deque(tmp376._args)
            # State 108108
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108109
                if len(subjects377) >= 1:
                    tmp379 = subjects377.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp379)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108110
                        if len(subjects377) == 0:
                            pass
                            # State 108111
                            if len(subjects) == 0:
                                pass
                                # 44: acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 44, subst2
                                # 46: acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 46, subst2
                    subjects377.appendleft(tmp379)
            if len(subjects377) >= 1 and isinstance(subjects377[0], Mul):
                tmp381 = subjects377.popleft()
                associative1 = tmp381
                associative_type1 = type(tmp381)
                subjects382 = deque(tmp381._args)
                matcher = CommutativeMatcher108113.get()
                tmp383 = subjects382
                subjects382 = []
                for s in tmp383:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp383, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108114
                        if len(subjects377) == 0:
                            pass
                            # State 108115
                            if len(subjects) == 0:
                                pass
                                # 44: acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 44, subst1
                                # 46: acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 46, subst1
                subjects377.appendleft(tmp381)
            if len(subjects377) >= 1 and isinstance(subjects377[0], Add):
                tmp384 = subjects377.popleft()
                associative1 = tmp384
                associative_type1 = type(tmp384)
                subjects385 = deque(tmp384._args)
                matcher = CommutativeMatcher110409.get()
                tmp386 = subjects385
                subjects385 = []
                for s in tmp386:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp386, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110415
                        if len(subjects377) == 0:
                            pass
                            # State 110416
                            if len(subjects) == 0:
                                pass
                                # 48: acos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                                yield 48, subst1
                    if pattern_index == 1:
                        pass
                        # State 110764
                        if len(subjects377) == 0:
                            pass
                            # State 110765
                            if len(subjects) == 0:
                                pass
                                # 50: acos(d*x**2 + 1) /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                                yield 50, subst1
                    if pattern_index == 2:
                        pass
                        # State 110811
                        if len(subjects377) == 0:
                            pass
                            # State 110812
                            if len(subjects) == 0:
                                pass
                                # 51: acos(d*x**2 - 1) /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                                yield 51, subst1
                    if pattern_index == 3:
                        pass
                        # State 110848
                        if len(subjects377) == 0:
                            pass
                            # State 110849
                            if len(subjects) == 0:
                                pass
                                # 52: acos(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1766)
                                yield 52, subst1
                subjects377.appendleft(tmp384)
            subjects.appendleft(tmp376)
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp387 = subjects.popleft()
            subjects388 = deque(tmp387._args)
            # State 112649
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 112650
                if len(subjects388) >= 1:
                    tmp390 = subjects388.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp390)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112651
                        if len(subjects388) == 0:
                            pass
                            # State 112652
                            if len(subjects) == 0:
                                pass
                                # 53: atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 53, subst2
                                # 55: atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                yield 55, subst2
                    subjects388.appendleft(tmp390)
            if len(subjects388) >= 1 and isinstance(subjects388[0], Mul):
                tmp392 = subjects388.popleft()
                associative1 = tmp392
                associative_type1 = type(tmp392)
                subjects393 = deque(tmp392._args)
                matcher = CommutativeMatcher112654.get()
                tmp394 = subjects393
                subjects393 = []
                for s in tmp394:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp394, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 112655
                        if len(subjects388) == 0:
                            pass
                            # State 112656
                            if len(subjects) == 0:
                                pass
                                # 53: atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 53, subst1
                                # 55: atan(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                yield 55, subst1
                subjects388.appendleft(tmp392)
            if len(subjects388) >= 1 and isinstance(subjects388[0], Add):
                tmp395 = subjects388.popleft()
                associative1 = tmp395
                associative_type1 = type(tmp395)
                subjects396 = deque(tmp395._args)
                matcher = CommutativeMatcher115511.get()
                tmp397 = subjects396
                subjects396 = []
                for s in tmp397:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp397, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115517
                        if len(subjects388) == 0:
                            pass
                            # State 115518
                            if len(subjects) == 0:
                                pass
                                # 57: atan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                yield 57, subst1
                                # 59: atan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                yield 59, subst1
                subjects388.appendleft(tmp395)
            subjects.appendleft(tmp387)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp398 = subjects.popleft()
            subjects399 = deque(tmp398._args)
            # State 112743
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 112744
                if len(subjects399) >= 1:
                    tmp401 = subjects399.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp401)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112745
                        if len(subjects399) == 0:
                            pass
                            # State 112746
                            if len(subjects) == 0:
                                pass
                                # 56: acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                yield 56, subst2
                                # 54: acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 54, subst2
                    subjects399.appendleft(tmp401)
            if len(subjects399) >= 1 and isinstance(subjects399[0], Mul):
                tmp403 = subjects399.popleft()
                associative1 = tmp403
                associative_type1 = type(tmp403)
                subjects404 = deque(tmp403._args)
                matcher = CommutativeMatcher112748.get()
                tmp405 = subjects404
                subjects404 = []
                for s in tmp405:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp405, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 112749
                        if len(subjects399) == 0:
                            pass
                            # State 112750
                            if len(subjects) == 0:
                                pass
                                # 56: acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                yield 56, subst1
                                # 54: acot(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 54, subst1
                subjects399.appendleft(tmp403)
            if len(subjects399) >= 1 and isinstance(subjects399[0], Add):
                tmp406 = subjects399.popleft()
                associative1 = tmp406
                associative_type1 = type(tmp406)
                subjects407 = deque(tmp406._args)
                matcher = CommutativeMatcher115607.get()
                tmp408 = subjects407
                subjects407 = []
                for s in tmp408:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp408, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115613
                        if len(subjects399) == 0:
                            pass
                            # State 115614
                            if len(subjects) == 0:
                                pass
                                # 58: acot(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                yield 58, subst1
                                # 60: acot(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                yield 60, subst1
                subjects399.appendleft(tmp406)
            subjects.appendleft(tmp398)
        if len(subjects) >= 1 and isinstance(subjects[0], asec):
            tmp409 = subjects.popleft()
            subjects410 = deque(tmp409._args)
            # State 119543
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119544
                if len(subjects410) >= 1:
                    tmp412 = subjects410.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp412)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119545
                        if len(subjects410) == 0:
                            pass
                            # State 119546
                            if len(subjects) == 0:
                                pass
                                # 61: asec(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 61, subst2
                    subjects410.appendleft(tmp412)
            if len(subjects410) >= 1 and isinstance(subjects410[0], Mul):
                tmp414 = subjects410.popleft()
                associative1 = tmp414
                associative_type1 = type(tmp414)
                subjects415 = deque(tmp414._args)
                matcher = CommutativeMatcher119548.get()
                tmp416 = subjects415
                subjects415 = []
                for s in tmp416:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp416, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119549
                        if len(subjects410) == 0:
                            pass
                            # State 119550
                            if len(subjects) == 0:
                                pass
                                # 61: asec(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 61, subst1
                subjects410.appendleft(tmp414)
            subjects.appendleft(tmp409)
        if len(subjects) >= 1 and isinstance(subjects[0], acsc):
            tmp417 = subjects.popleft()
            subjects418 = deque(tmp417._args)
            # State 119594
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119595
                if len(subjects418) >= 1:
                    tmp420 = subjects418.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp420)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119596
                        if len(subjects418) == 0:
                            pass
                            # State 119597
                            if len(subjects) == 0:
                                pass
                                # 62: acsc(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 62, subst2
                    subjects418.appendleft(tmp420)
            if len(subjects418) >= 1 and isinstance(subjects418[0], Mul):
                tmp422 = subjects418.popleft()
                associative1 = tmp422
                associative_type1 = type(tmp422)
                subjects423 = deque(tmp422._args)
                matcher = CommutativeMatcher119599.get()
                tmp424 = subjects423
                subjects423 = []
                for s in tmp424:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp424, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119600
                        if len(subjects418) == 0:
                            pass
                            # State 119601
                            if len(subjects) == 0:
                                pass
                                # 62: acsc(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 62, subst1
                subjects418.appendleft(tmp422)
            subjects.appendleft(tmp417)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp425 = subjects.popleft()
            subjects426 = deque(tmp425._args)
            # State 122510
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 122511
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122512
                    if len(subjects426) >= 1 and isinstance(subjects426[0], Pow):
                        tmp429 = subjects426.popleft()
                        subjects430 = deque(tmp429._args)
                        # State 122513
                        if len(subjects430) >= 1:
                            tmp431 = subjects430.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp431)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 122514
                                if len(subjects430) >= 1:
                                    tmp433 = subjects430.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp433)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 122515
                                        if len(subjects430) == 0:
                                            pass
                                            # State 122516
                                            if len(subjects426) == 0:
                                                pass
                                                # State 122517
                                                if len(subjects) == 0:
                                                    pass
                                                    # 65: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                                    yield 65, subst4
                                                    # 67: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                    yield 67, subst4
                                                    # 69: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                    yield 69, subst4
                                                    # 71: sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    yield 71, subst4
                                                    # 73: sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                                    yield 73, subst4
                                                    # 63: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                                    yield 63, subst4
                                    subjects430.appendleft(tmp433)
                            subjects430.appendleft(tmp431)
                        subjects426.appendleft(tmp429)
                if len(subjects426) >= 1 and isinstance(subjects426[0], Mul):
                    tmp435 = subjects426.popleft()
                    associative1 = tmp435
                    associative_type1 = type(tmp435)
                    subjects436 = deque(tmp435._args)
                    matcher = CommutativeMatcher122519.get()
                    tmp437 = subjects436
                    subjects436 = []
                    for s in tmp437:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp437, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122524
                            if len(subjects426) == 0:
                                pass
                                # State 122525
                                if len(subjects) == 0:
                                    pass
                                    # 65: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    yield 65, subst2
                                    # 67: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    yield 67, subst2
                                    # 69: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 69, subst2
                                    # 71: sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 71, subst2
                                    # 73: sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                    yield 73, subst2
                                    # 63: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                    yield 63, subst2
                    subjects426.appendleft(tmp435)
            if len(subjects426) >= 1:
                tmp438 = subjects426.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp438)
                except ValueError:
                    pass
                else:
                    pass
                    # State 123385
                    if len(subjects426) == 0:
                        pass
                        # State 123386
                        if len(subjects) == 0:
                            pass
                            # 75: sinh(u) /; (cons_f825) and (cons_f826)
                            yield 75, subst1
                subjects426.appendleft(tmp438)
            if len(subjects426) >= 1 and isinstance(subjects426[0], Add):
                tmp440 = subjects426.popleft()
                associative1 = tmp440
                associative_type1 = type(tmp440)
                subjects441 = deque(tmp440._args)
                matcher = CommutativeMatcher122527.get()
                tmp442 = subjects441
                subjects441 = []
                for s in tmp442:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp442, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 122540
                        if len(subjects426) == 0:
                            pass
                            # State 122541
                            if len(subjects) == 0:
                                pass
                                # 65: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                yield 65, subst1
                                # 67: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                yield 67, subst1
                                # 69: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                yield 69, subst1
                                # 71: sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                yield 71, subst1
                                # 73: sinh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                yield 73, subst1
                                # 63: sinh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                yield 63, subst1
                subjects426.appendleft(tmp440)
            subjects.appendleft(tmp425)
        if len(subjects) >= 1 and isinstance(subjects[0], cosh):
            tmp443 = subjects.popleft()
            subjects444 = deque(tmp443._args)
            # State 122661
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 122662
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122663
                    if len(subjects444) >= 1 and isinstance(subjects444[0], Pow):
                        tmp447 = subjects444.popleft()
                        subjects448 = deque(tmp447._args)
                        # State 122664
                        if len(subjects448) >= 1:
                            tmp449 = subjects448.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp449)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 122665
                                if len(subjects448) >= 1:
                                    tmp451 = subjects448.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp451)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 122666
                                        if len(subjects448) == 0:
                                            pass
                                            # State 122667
                                            if len(subjects444) == 0:
                                                pass
                                                # State 122668
                                                if len(subjects) == 0:
                                                    pass
                                                    # 64: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                                    yield 64, subst4
                                                    # 66: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                                    yield 66, subst4
                                                    # 68: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                                    yield 68, subst4
                                                    # 70: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                    yield 70, subst4
                                                    # 72: cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    yield 72, subst4
                                                    # 74: cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                                    yield 74, subst4
                                    subjects448.appendleft(tmp451)
                            subjects448.appendleft(tmp449)
                        subjects444.appendleft(tmp447)
                if len(subjects444) >= 1 and isinstance(subjects444[0], Mul):
                    tmp453 = subjects444.popleft()
                    associative1 = tmp453
                    associative_type1 = type(tmp453)
                    subjects454 = deque(tmp453._args)
                    matcher = CommutativeMatcher122670.get()
                    tmp455 = subjects454
                    subjects454 = []
                    for s in tmp455:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp455, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122675
                            if len(subjects444) == 0:
                                pass
                                # State 122676
                                if len(subjects) == 0:
                                    pass
                                    # 64: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                    yield 64, subst2
                                    # 66: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    yield 66, subst2
                                    # 68: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    yield 68, subst2
                                    # 70: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 70, subst2
                                    # 72: cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 72, subst2
                                    # 74: cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                    yield 74, subst2
                    subjects444.appendleft(tmp453)
            if len(subjects444) >= 1:
                tmp456 = subjects444.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp456)
                except ValueError:
                    pass
                else:
                    pass
                    # State 123425
                    if len(subjects444) == 0:
                        pass
                        # State 123426
                        if len(subjects) == 0:
                            pass
                            # 76: cosh(u) /; (cons_f825) and (cons_f826)
                            yield 76, subst1
                subjects444.appendleft(tmp456)
            if len(subjects444) >= 1 and isinstance(subjects444[0], Add):
                tmp458 = subjects444.popleft()
                associative1 = tmp458
                associative_type1 = type(tmp458)
                subjects459 = deque(tmp458._args)
                matcher = CommutativeMatcher122678.get()
                tmp460 = subjects459
                subjects459 = []
                for s in tmp460:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp460, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 122691
                        if len(subjects444) == 0:
                            pass
                            # State 122692
                            if len(subjects) == 0:
                                pass
                                # 64: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                yield 64, subst1
                                # 66: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                yield 66, subst1
                                # 68: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                yield 68, subst1
                                # 70: cosh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                yield 70, subst1
                                # 72: cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                yield 72, subst1
                                # 74: cosh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70)
                                yield 74, subst1
                subjects444.appendleft(tmp458)
            subjects.appendleft(tmp443)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp461 = subjects.popleft()
            subjects462 = deque(tmp461._args)
            # State 126719
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 126720
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 126721
                    if len(subjects462) >= 1 and isinstance(subjects462[0], Pow):
                        tmp465 = subjects462.popleft()
                        subjects466 = deque(tmp465._args)
                        # State 126722
                        if len(subjects466) >= 1:
                            tmp467 = subjects466.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp467)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 126723
                                if len(subjects466) >= 1:
                                    tmp469 = subjects466.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.1.2', tmp469)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 126724
                                        if len(subjects466) == 0:
                                            pass
                                            # State 126725
                                            if len(subjects462) == 0:
                                                pass
                                                # State 126726
                                                if len(subjects) == 0:
                                                    pass
                                                    # 81: tanh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                                    yield 81, subst4
                                                    # 77: tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                                    yield 77, subst4
                                                    # 79: tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                                    yield 79, subst4
                                    subjects466.appendleft(tmp469)
                            subjects466.appendleft(tmp467)
                        subjects462.appendleft(tmp465)
                if len(subjects462) >= 1 and isinstance(subjects462[0], Mul):
                    tmp471 = subjects462.popleft()
                    associative1 = tmp471
                    associative_type1 = type(tmp471)
                    subjects472 = deque(tmp471._args)
                    matcher = CommutativeMatcher126728.get()
                    tmp473 = subjects472
                    subjects472 = []
                    for s in tmp473:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp473, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 126733
                            if len(subjects462) == 0:
                                pass
                                # State 126734
                                if len(subjects) == 0:
                                    pass
                                    # 81: tanh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                    yield 81, subst2
                                    # 77: tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                    yield 77, subst2
                                    # 79: tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                    yield 79, subst2
                    subjects462.appendleft(tmp471)
            if len(subjects462) >= 1:
                tmp474 = subjects462.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp474)
                except ValueError:
                    pass
                else:
                    pass
                    # State 127357
                    if len(subjects462) == 0:
                        pass
                        # State 127358
                        if len(subjects) == 0:
                            pass
                            # 83: tanh(u) /; (cons_f825) and (cons_f826)
                            yield 83, subst1
                subjects462.appendleft(tmp474)
            if len(subjects462) >= 1 and isinstance(subjects462[0], Add):
                tmp476 = subjects462.popleft()
                associative1 = tmp476
                associative_type1 = type(tmp476)
                subjects477 = deque(tmp476._args)
                matcher = CommutativeMatcher126736.get()
                tmp478 = subjects477
                subjects477 = []
                for s in tmp478:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp478, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 126749
                        if len(subjects462) == 0:
                            pass
                            # State 126750
                            if len(subjects) == 0:
                                pass
                                # 81: tanh(c + d*x**n) /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f70) and (cons_f71)
                                yield 81, subst1
                                # 77: tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f1575)
                                yield 77, subst1
                                # 79: tanh(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1497)
                                yield 79, subst1
                subjects462.appendleft(tmp476)
            subjects.appendleft(tmp461)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp479 = subjects.popleft()
            subjects480 = deque(tmp479._args)
            # State 137753
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 137754
                if len(subjects480) >= 1:
                    tmp482 = subjects480.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp482)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137755
                        if len(subjects480) == 0:
                            pass
                            # State 137756
                            if len(subjects) == 0:
                                pass
                                # 93: asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 93, subst2
                                # 95: asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 95, subst2
                    subjects480.appendleft(tmp482)
            if len(subjects480) >= 1 and isinstance(subjects480[0], Mul):
                tmp484 = subjects480.popleft()
                associative1 = tmp484
                associative_type1 = type(tmp484)
                subjects485 = deque(tmp484._args)
                matcher = CommutativeMatcher137758.get()
                tmp486 = subjects485
                subjects485 = []
                for s in tmp486:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp486, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 137759
                        if len(subjects480) == 0:
                            pass
                            # State 137760
                            if len(subjects) == 0:
                                pass
                                # 93: asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 93, subst1
                                # 95: asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 95, subst1
                subjects480.appendleft(tmp484)
            if len(subjects480) >= 1 and isinstance(subjects480[0], Add):
                tmp487 = subjects480.popleft()
                associative1 = tmp487
                associative_type1 = type(tmp487)
                subjects488 = deque(tmp487._args)
                matcher = CommutativeMatcher140048.get()
                tmp489 = subjects488
                subjects488 = []
                for s in tmp489:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp489, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 140054
                        if len(subjects480) == 0:
                            pass
                            # State 140055
                            if len(subjects) == 0:
                                pass
                                # 97: asinh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                                yield 97, subst1
                    if pattern_index == 1:
                        pass
                        # State 140393
                        if len(subjects480) == 0:
                            pass
                            # State 140394
                            if len(subjects) == 0:
                                pass
                                # 99: asinh(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1906)
                                yield 99, subst1
                subjects480.appendleft(tmp487)
            subjects.appendleft(tmp479)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp490 = subjects.popleft()
            subjects491 = deque(tmp490._args)
            # State 137847
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 137848
                if len(subjects491) >= 1:
                    tmp493 = subjects491.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp493)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137849
                        if len(subjects491) == 0:
                            pass
                            # State 137850
                            if len(subjects) == 0:
                                pass
                                # 96: acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 96, subst2
                                # 94: acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 94, subst2
                    subjects491.appendleft(tmp493)
            if len(subjects491) >= 1 and isinstance(subjects491[0], Mul):
                tmp495 = subjects491.popleft()
                associative1 = tmp495
                associative_type1 = type(tmp495)
                subjects496 = deque(tmp495._args)
                matcher = CommutativeMatcher137852.get()
                tmp497 = subjects496
                subjects496 = []
                for s in tmp497:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp497, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 137853
                        if len(subjects491) == 0:
                            pass
                            # State 137854
                            if len(subjects) == 0:
                                pass
                                # 96: acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 96, subst1
                                # 94: acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 94, subst1
                subjects491.appendleft(tmp495)
            if len(subjects491) >= 1 and isinstance(subjects491[0], Add):
                tmp498 = subjects491.popleft()
                associative1 = tmp498
                associative_type1 = type(tmp498)
                subjects499 = deque(tmp498._args)
                matcher = CommutativeMatcher140144.get()
                tmp500 = subjects499
                subjects499 = []
                for s in tmp500:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp500, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 140150
                        if len(subjects491) == 0:
                            pass
                            # State 140151
                            if len(subjects) == 0:
                                pass
                                # 98: acosh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1275)
                                yield 98, subst1
                    if pattern_index == 1:
                        pass
                        # State 140518
                        if len(subjects491) == 0:
                            pass
                            # State 140519
                            if len(subjects) == 0:
                                pass
                                # 100: acosh(d*x**2 + 1) /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                                yield 100, subst1
                    if pattern_index == 2:
                        pass
                        # State 140565
                        if len(subjects491) == 0:
                            pass
                            # State 140566
                            if len(subjects) == 0:
                                pass
                                # 101: acosh(d*x**2 - 1) /; (cons_f2) and (cons_f3) and (cons_f29) and (cons_f1767)
                                yield 101, subst1
                    if pattern_index == 3:
                        pass
                        # State 140590
                        if len(subjects491) == 0:
                            pass
                            # State 140591
                            if len(subjects) == 0:
                                pass
                                # 102: acosh(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1766)
                                yield 102, subst1
                subjects491.appendleft(tmp498)
            subjects.appendleft(tmp490)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp501 = subjects.popleft()
            subjects502 = deque(tmp501._args)
            # State 142281
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142282
                if len(subjects502) >= 1:
                    tmp504 = subjects502.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp504)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142283
                        if len(subjects502) == 0:
                            pass
                            # State 142284
                            if len(subjects) == 0:
                                pass
                                # 105: atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                yield 105, subst2
                                # 103: atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 103, subst2
                    subjects502.appendleft(tmp504)
            if len(subjects502) >= 1 and isinstance(subjects502[0], Mul):
                tmp506 = subjects502.popleft()
                associative1 = tmp506
                associative_type1 = type(tmp506)
                subjects507 = deque(tmp506._args)
                matcher = CommutativeMatcher142286.get()
                tmp508 = subjects507
                subjects507 = []
                for s in tmp508:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp508, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142287
                        if len(subjects502) == 0:
                            pass
                            # State 142288
                            if len(subjects) == 0:
                                pass
                                # 105: atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                yield 105, subst1
                                # 103: atanh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 103, subst1
                subjects502.appendleft(tmp506)
            if len(subjects502) >= 1 and isinstance(subjects502[0], Add):
                tmp509 = subjects502.popleft()
                associative1 = tmp509
                associative_type1 = type(tmp509)
                subjects510 = deque(tmp509._args)
                matcher = CommutativeMatcher144736.get()
                tmp511 = subjects510
                subjects510 = []
                for s in tmp511:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp511, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144742
                        if len(subjects502) == 0:
                            pass
                            # State 144743
                            if len(subjects) == 0:
                                pass
                                # 107: atanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                yield 107, subst1
                                # 109: atanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                yield 109, subst1
                subjects502.appendleft(tmp509)
            subjects.appendleft(tmp501)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp512 = subjects.popleft()
            subjects513 = deque(tmp512._args)
            # State 142375
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142376
                if len(subjects513) >= 1:
                    tmp515 = subjects513.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp515)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142377
                        if len(subjects513) == 0:
                            pass
                            # State 142378
                            if len(subjects) == 0:
                                pass
                                # 104: acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 104, subst2
                                # 106: acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                yield 106, subst2
                    subjects513.appendleft(tmp515)
            if len(subjects513) >= 1 and isinstance(subjects513[0], Mul):
                tmp517 = subjects513.popleft()
                associative1 = tmp517
                associative_type1 = type(tmp517)
                subjects518 = deque(tmp517._args)
                matcher = CommutativeMatcher142380.get()
                tmp519 = subjects518
                subjects518 = []
                for s in tmp519:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp519, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142381
                        if len(subjects513) == 0:
                            pass
                            # State 142382
                            if len(subjects) == 0:
                                pass
                                # 104: acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8)
                                yield 104, subst1
                                # 106: acoth(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                yield 106, subst1
                subjects513.appendleft(tmp517)
            if len(subjects513) >= 1 and isinstance(subjects513[0], Add):
                tmp520 = subjects513.popleft()
                associative1 = tmp520
                associative_type1 = type(tmp520)
                subjects521 = deque(tmp520._args)
                matcher = CommutativeMatcher144832.get()
                tmp522 = subjects521
                subjects521 = []
                for s in tmp522:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp522, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144838
                        if len(subjects513) == 0:
                            pass
                            # State 144839
                            if len(subjects) == 0:
                                pass
                                # 108: acoth(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                yield 108, subst1
                                # 110: acoth(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                yield 110, subst1
                subjects513.appendleft(tmp520)
            subjects.appendleft(tmp512)
        if len(subjects) >= 1 and isinstance(subjects[0], asech):
            tmp523 = subjects.popleft()
            subjects524 = deque(tmp523._args)
            # State 148719
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 148720
                if len(subjects524) >= 1:
                    tmp526 = subjects524.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp526)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148721
                        if len(subjects524) == 0:
                            pass
                            # State 148722
                            if len(subjects) == 0:
                                pass
                                # 111: asech(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 111, subst2
                    subjects524.appendleft(tmp526)
            if len(subjects524) >= 1 and isinstance(subjects524[0], Mul):
                tmp528 = subjects524.popleft()
                associative1 = tmp528
                associative_type1 = type(tmp528)
                subjects529 = deque(tmp528._args)
                matcher = CommutativeMatcher148724.get()
                tmp530 = subjects529
                subjects529 = []
                for s in tmp530:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp530, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 148725
                        if len(subjects524) == 0:
                            pass
                            # State 148726
                            if len(subjects) == 0:
                                pass
                                # 111: asech(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 111, subst1
                subjects524.appendleft(tmp528)
            subjects.appendleft(tmp523)
        if len(subjects) >= 1 and isinstance(subjects[0], acsch):
            tmp531 = subjects.popleft()
            subjects532 = deque(tmp531._args)
            # State 148770
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 148771
                if len(subjects532) >= 1:
                    tmp534 = subjects532.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.0', tmp534)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148772
                        if len(subjects532) == 0:
                            pass
                            # State 148773
                            if len(subjects) == 0:
                                pass
                                # 112: acsch(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 112, subst2
                    subjects532.appendleft(tmp534)
            if len(subjects532) >= 1 and isinstance(subjects532[0], Mul):
                tmp536 = subjects532.popleft()
                associative1 = tmp536
                associative_type1 = type(tmp536)
                subjects537 = deque(tmp536._args)
                matcher = CommutativeMatcher148775.get()
                tmp538 = subjects537
                subjects537 = []
                for s in tmp538:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp538, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 148776
                        if len(subjects532) == 0:
                            pass
                            # State 148777
                            if len(subjects) == 0:
                                pass
                                # 112: acsch(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 112, subst1
                subjects532.appendleft(tmp536)
            subjects.appendleft(tmp531)
        return
        yield


from .generated_part009218 import *
from .generated_part009319 import *
from .generated_part009321 import *
from .generated_part009353 import *
from .generated_part009357 import *
from .generated_part009342 import *
from .generated_part009347 import *
from .generated_part009222 import *
from .generated_part009328 import *
from .generated_part009345 import *
from .generated_part009249 import *
from .generated_part009322 import *
from .generated_part009221 import *
from .generated_part009251 import *
from .generated_part009315 import *
from .generated_part009324 import *
from .generated_part009261 import *
from .generated_part009339 import *
from .generated_part009228 import *
from .generated_part009351 import *
from .generated_part009254 import *
from .generated_part009213 import *
from .generated_part009230 import *
from collections import deque
from .generated_part009224 import *
from .generated_part009240 import *
from .generated_part009316 import *
from .generated_part009331 import *
from .generated_part009233 import *
from .generated_part009354 import *
from matchpy.utils import VariableWithCount
from .generated_part009318 import *
from .generated_part009325 import *
from .generated_part009333 import *
from .generated_part009216 import *
from .generated_part009313 import *
from .generated_part009327 import *
from .generated_part009209 import *
from .generated_part009356 import *
from .generated_part009203 import *
from .generated_part009335 import *
from multiset import Multiset
from .generated_part009341 import *
from .generated_part009215 import *
from .generated_part009227 import *
from .generated_part009330 import *
from .generated_part009334 import *
from .generated_part009202 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part009338 import *
from .generated_part009219 import *
from .generated_part009348 import *
from .generated_part009212 import *
from .generated_part009231 import *
from .generated_part009248 import *
from .generated_part009252 import *
from .generated_part009225 import *
from .generated_part009269 import *
from .generated_part009312 import *
from .generated_part009336 import *
from .generated_part009344 import *
from .generated_part009350 import *
from .generated_part009210 import *