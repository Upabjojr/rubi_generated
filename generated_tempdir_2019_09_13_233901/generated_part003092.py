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

class CommutativeMatcher3056(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.3.1.1.0', 1, 1, None), Mul)
]),
    8: (8, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.4.1.1.0', 1, 1, None), Mul)
]),
    9: (9, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.4.1.1.0', 1, 1, None), Mul)
]),
    10: (10, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.2.2.1.0', 1, 1, None), Mul)
]),
    12: (12, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({13: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.2.1.0', 1, 1, None), Mul)
]),
    22: (22, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul)
]),
    23: (23, Multiset({14: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({15: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({16: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({17: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    27: (27, Multiset({18: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({19: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({20: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({21: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    31: (31, Multiset({22: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.3.1.0', 1, 1, None), Mul)
]),
    33: (33, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.3.1.0', 1, 1, None), Mul)
]),
    34: (34, Multiset({23: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({24: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    36: (36, Multiset({25: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    37: (37, Multiset({26: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    38: (38, Multiset({27: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({28: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Mul)
]),
    41: (41, Multiset({29: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    42: (42, Multiset({30: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    43: (43, Multiset({31: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    44: (44, Multiset({32: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    45: (45, Multiset({33: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    46: (46, Multiset({34: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    47: (47, Multiset({35: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    48: (48, Multiset({36: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    49: (49, Multiset({37: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    50: (50, Multiset({38: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    51: (51, Multiset({39: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    52: (52, Multiset({40: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    53: (53, Multiset({41: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    54: (54, Multiset({42: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    55: (55, Multiset({43: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    56: (56, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher3056._instance is None:
            CommutativeMatcher3056._instance = CommutativeMatcher3056()
        return CommutativeMatcher3056._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3055
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 5569
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 5570
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp5 = subjects2.popleft()
                        # State 5571
                        if len(subjects2) == 0:
                            pass
                            # State 5572
                            if len(subjects) == 0:
                                pass
                                # 0: x**2
                        subjects2.appendleft(tmp5)
                    if len(subjects2) >= 1:
                        tmp6 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp6)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7107
                            if len(subjects2) == 0:
                                pass
                                # State 7108
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**j
                        subjects2.appendleft(tmp6)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7845
                        if len(subjects2) == 0:
                            pass
                            # State 7846
                            if len(subjects) == 0:
                                pass
                                # 3: x**n
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7845
                            if len(subjects2) == 0:
                                pass
                                # State 7846
                                if len(subjects) == 0:
                                    pass
                                    # 3: x**n
                        subjects2.appendleft(tmp9)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp11 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1_1', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7763
                    if len(subjects2) >= 1:
                        tmp13 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp13)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7764
                            if len(subjects2) == 0:
                                pass
                                # State 7765
                                if len(subjects) == 0:
                                    pass
                                    # 2: v**n
                        subjects2.appendleft(tmp13)
                subjects2.appendleft(tmp11)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                tmp15 = subjects2.popleft()
                subjects16 = deque(tmp15._args)
                # State 16258
                if len(subjects16) >= 1:
                    tmp17 = subjects16.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp17)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 16259
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 16260
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 16261
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.4.1.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 16262
                                    if len(subjects16) >= 1:
                                        tmp22 = subjects16.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.3.1.1.0', tmp22)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 16263
                                            if len(subjects16) == 0:
                                                pass
                                                # State 16264
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16265
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 16266
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (F**(g*(e + f*x)))**n
                                                if len(subjects2) >= 1:
                                                    tmp25 = subjects2.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.4', tmp25)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 16265
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 16266
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (F**(g*(e + f*x)))**n
                                                    subjects2.appendleft(tmp25)
                                        subjects16.appendleft(tmp22)
                                if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                                    tmp27 = subjects16.popleft()
                                    associative1 = tmp27
                                    associative_type1 = type(tmp27)
                                    subjects28 = deque(tmp27._args)
                                    matcher = CommutativeMatcher16268.get()
                                    tmp29 = subjects28
                                    subjects28 = []
                                    for s in tmp29:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp29, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 16269
                                            if len(subjects16) == 0:
                                                pass
                                                # State 16270
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16271
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 16272
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (F**(g*(e + f*x)))**n
                                                if len(subjects2) >= 1:
                                                    tmp31 = subjects2.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.4', tmp31)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 16271
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 16272
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (F**(g*(e + f*x)))**n
                                                    subjects2.appendleft(tmp31)
                                    subjects16.appendleft(tmp27)
                            if len(subjects16) >= 1 and isinstance(subjects16[0], Add):
                                tmp33 = subjects16.popleft()
                                associative1 = tmp33
                                associative_type1 = type(tmp33)
                                subjects34 = deque(tmp33._args)
                                matcher = CommutativeMatcher16274.get()
                                tmp35 = subjects34
                                subjects34 = []
                                for s in tmp35:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp35, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 16280
                                        if len(subjects16) == 0:
                                            pass
                                            # State 16281
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.4', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 16282
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 16283
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (F**(g*(e + f*x)))**n
                                            if len(subjects2) >= 1:
                                                tmp37 = subjects2.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.4', tmp37)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16282
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 16283
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (F**(g*(e + f*x)))**n
                                                subjects2.appendleft(tmp37)
                                subjects16.appendleft(tmp33)
                        if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                            tmp39 = subjects16.popleft()
                            associative1 = tmp39
                            associative_type1 = type(tmp39)
                            subjects40 = deque(tmp39._args)
                            matcher = CommutativeMatcher16285.get()
                            tmp41 = subjects40
                            subjects40 = []
                            for s in tmp41:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp41, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 16300
                                    if len(subjects16) == 0:
                                        pass
                                        # State 16301
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.4', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 16302
                                            if len(subjects2) == 0:
                                                pass
                                                # State 16303
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (F**(g*(e + f*x)))**n
                                        if len(subjects2) >= 1:
                                            tmp43 = subjects2.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.4', tmp43)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 16302
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 16303
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (F**(g*(e + f*x)))**n
                                            subjects2.appendleft(tmp43)
                            subjects16.appendleft(tmp39)
                    subjects16.appendleft(tmp17)
                subjects2.appendleft(tmp15)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp45 = subjects2.popleft()
                subjects46 = deque(tmp45._args)
                # State 63753
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63754
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 63755
                        if len(subjects46) >= 1:
                            tmp49 = subjects46.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp49)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 63756
                                if len(subjects46) == 0:
                                    pass
                                    # State 63757
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp51 = subjects2.popleft()
                                        # State 63758
                                        if len(subjects2) == 0:
                                            pass
                                            # State 63759
                                            if len(subjects) == 0:
                                                pass
                                                # 12: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp51)
                            subjects46.appendleft(tmp49)
                    if len(subjects46) >= 1 and isinstance(subjects46[0], Mul):
                        tmp52 = subjects46.popleft()
                        associative1 = tmp52
                        associative_type1 = type(tmp52)
                        subjects53 = deque(tmp52._args)
                        matcher = CommutativeMatcher63761.get()
                        tmp54 = subjects53
                        subjects53 = []
                        for s in tmp54:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp54, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 63762
                                if len(subjects46) == 0:
                                    pass
                                    # State 63763
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp55 = subjects2.popleft()
                                        # State 63764
                                        if len(subjects2) == 0:
                                            pass
                                            # State 63765
                                            if len(subjects) == 0:
                                                pass
                                                # 12: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp55)
                        subjects46.appendleft(tmp52)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 91047
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91048
                        if len(subjects46) >= 1:
                            tmp58 = subjects46.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp58)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 91049
                                if len(subjects46) == 0:
                                    pass
                                    # State 91050
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp60 = subjects2.popleft()
                                        # State 91051
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91052
                                            if len(subjects) == 0:
                                                pass
                                                # 24: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp60)
                            subjects46.appendleft(tmp58)
                    if len(subjects46) >= 1 and isinstance(subjects46[0], Mul):
                        tmp61 = subjects46.popleft()
                        associative1 = tmp61
                        associative_type1 = type(tmp61)
                        subjects62 = deque(tmp61._args)
                        matcher = CommutativeMatcher91054.get()
                        tmp63 = subjects62
                        subjects62 = []
                        for s in tmp63:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp63, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 91055
                                if len(subjects46) == 0:
                                    pass
                                    # State 91056
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp64 = subjects2.popleft()
                                        # State 91057
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91058
                                            if len(subjects) == 0:
                                                pass
                                                # 24: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp64)
                        subjects46.appendleft(tmp61)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 92007
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 92008
                        if len(subjects46) >= 1:
                            tmp67 = subjects46.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp67)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 92009
                                if len(subjects46) == 0:
                                    pass
                                    # State 92010
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp69 = subjects2.popleft()
                                        # State 92011
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92012
                                            if len(subjects) == 0:
                                                pass
                                                # 26: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp69)
                            subjects46.appendleft(tmp67)
                    if len(subjects46) >= 1 and isinstance(subjects46[0], Mul):
                        tmp70 = subjects46.popleft()
                        associative1 = tmp70
                        associative_type1 = type(tmp70)
                        subjects71 = deque(tmp70._args)
                        matcher = CommutativeMatcher92014.get()
                        tmp72 = subjects71
                        subjects71 = []
                        for s in tmp72:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp72, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 92015
                                if len(subjects46) == 0:
                                    pass
                                    # State 92016
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp73 = subjects2.popleft()
                                        # State 92017
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92018
                                            if len(subjects) == 0:
                                                pass
                                                # 26: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp73)
                        subjects46.appendleft(tmp70)
                if len(subjects46) >= 1 and isinstance(subjects46[0], Add):
                    tmp74 = subjects46.popleft()
                    associative1 = tmp74
                    associative_type1 = type(tmp74)
                    subjects75 = deque(tmp74._args)
                    matcher = CommutativeMatcher63767.get()
                    tmp76 = subjects75
                    subjects75 = []
                    for s in tmp76:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp76, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63773
                            if len(subjects46) == 0:
                                pass
                                # State 63774
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp77 = subjects2.popleft()
                                    # State 63775
                                    if len(subjects2) == 0:
                                        pass
                                        # State 63776
                                        if len(subjects) == 0:
                                            pass
                                            # 12: 1/sin(e + x*f)
                                    subjects2.appendleft(tmp77)
                        if pattern_index == 1:
                            pass
                            # State 91062
                            if len(subjects46) == 0:
                                pass
                                # State 91063
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp78 = subjects2.popleft()
                                    # State 91064
                                    if len(subjects2) == 0:
                                        pass
                                        # State 91065
                                        if len(subjects) == 0:
                                            pass
                                            # 24: 1/sin(e + x*f)
                                    subjects2.appendleft(tmp78)
                        if pattern_index == 2:
                            pass
                            # State 92022
                            if len(subjects46) == 0:
                                pass
                                # State 92023
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp79 = subjects2.popleft()
                                    # State 92024
                                    if len(subjects2) == 0:
                                        pass
                                        # State 92025
                                        if len(subjects) == 0:
                                            pass
                                            # 26: 1/sin(e + x*f)
                                    subjects2.appendleft(tmp79)
                    subjects46.appendleft(tmp74)
                subjects2.appendleft(tmp45)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp80 = subjects2.popleft()
                subjects81 = deque(tmp80._args)
                # State 64032
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 64033
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 64034
                        if len(subjects81) >= 1:
                            tmp84 = subjects81.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp84)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 64035
                                if len(subjects81) == 0:
                                    pass
                                    # State 64036
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp86 = subjects2.popleft()
                                        # State 64037
                                        if len(subjects2) == 0:
                                            pass
                                            # State 64038
                                            if len(subjects) == 0:
                                                pass
                                                # 13: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp86)
                            subjects81.appendleft(tmp84)
                    if len(subjects81) >= 1 and isinstance(subjects81[0], Mul):
                        tmp87 = subjects81.popleft()
                        associative1 = tmp87
                        associative_type1 = type(tmp87)
                        subjects88 = deque(tmp87._args)
                        matcher = CommutativeMatcher64040.get()
                        tmp89 = subjects88
                        subjects88 = []
                        for s in tmp89:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp89, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 64041
                                if len(subjects81) == 0:
                                    pass
                                    # State 64042
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp90 = subjects2.popleft()
                                        # State 64043
                                        if len(subjects2) == 0:
                                            pass
                                            # State 64044
                                            if len(subjects) == 0:
                                                pass
                                                # 13: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp90)
                        subjects81.appendleft(tmp87)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 91826
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91827
                        if len(subjects81) >= 1:
                            tmp93 = subjects81.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp93)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 91828
                                if len(subjects81) == 0:
                                    pass
                                    # State 91829
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp95 = subjects2.popleft()
                                        # State 91830
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91831
                                            if len(subjects) == 0:
                                                pass
                                                # 25: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp95)
                            subjects81.appendleft(tmp93)
                    if len(subjects81) >= 1 and isinstance(subjects81[0], Mul):
                        tmp96 = subjects81.popleft()
                        associative1 = tmp96
                        associative_type1 = type(tmp96)
                        subjects97 = deque(tmp96._args)
                        matcher = CommutativeMatcher91833.get()
                        tmp98 = subjects97
                        subjects97 = []
                        for s in tmp98:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp98, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 91834
                                if len(subjects81) == 0:
                                    pass
                                    # State 91835
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp99 = subjects2.popleft()
                                        # State 91836
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91837
                                            if len(subjects) == 0:
                                                pass
                                                # 25: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp99)
                        subjects81.appendleft(tmp96)
                if len(subjects81) >= 1 and isinstance(subjects81[0], Add):
                    tmp100 = subjects81.popleft()
                    associative1 = tmp100
                    associative_type1 = type(tmp100)
                    subjects101 = deque(tmp100._args)
                    matcher = CommutativeMatcher64046.get()
                    tmp102 = subjects101
                    subjects101 = []
                    for s in tmp102:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp102, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 64052
                            if len(subjects81) == 0:
                                pass
                                # State 64053
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp103 = subjects2.popleft()
                                    # State 64054
                                    if len(subjects2) == 0:
                                        pass
                                        # State 64055
                                        if len(subjects) == 0:
                                            pass
                                            # 13: 1/cos(e + x*f)
                                    subjects2.appendleft(tmp103)
                        if pattern_index == 1:
                            pass
                            # State 91841
                            if len(subjects81) == 0:
                                pass
                                # State 91842
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp104 = subjects2.popleft()
                                    # State 91843
                                    if len(subjects2) == 0:
                                        pass
                                        # State 91844
                                        if len(subjects) == 0:
                                            pass
                                            # 25: 1/cos(e + x*f)
                                    subjects2.appendleft(tmp104)
                    subjects81.appendleft(tmp100)
                subjects2.appendleft(tmp80)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp105 = subjects2.popleft()
                subjects106 = deque(tmp105._args)
                # State 78541
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78542
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 78543
                        if len(subjects106) >= 1:
                            tmp109 = subjects106.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp109)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 78544
                                if len(subjects106) == 0:
                                    pass
                                    # State 78545
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp111 = subjects2.popleft()
                                        # State 78546
                                        if len(subjects2) == 0:
                                            pass
                                            # State 78547
                                            if len(subjects) == 0:
                                                pass
                                                # 16: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp111)
                            subjects106.appendleft(tmp109)
                    if len(subjects106) >= 1 and isinstance(subjects106[0], Mul):
                        tmp112 = subjects106.popleft()
                        associative1 = tmp112
                        associative_type1 = type(tmp112)
                        subjects113 = deque(tmp112._args)
                        matcher = CommutativeMatcher78549.get()
                        tmp114 = subjects113
                        subjects113 = []
                        for s in tmp114:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp114, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 78550
                                if len(subjects106) == 0:
                                    pass
                                    # State 78551
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp115 = subjects2.popleft()
                                        # State 78552
                                        if len(subjects2) == 0:
                                            pass
                                            # State 78553
                                            if len(subjects) == 0:
                                                pass
                                                # 16: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp115)
                        subjects106.appendleft(tmp112)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 79865
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 79866
                        if len(subjects106) >= 1:
                            tmp118 = subjects106.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp118)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 79867
                                if len(subjects106) == 0:
                                    pass
                                    # State 79868
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp120 = subjects2.popleft()
                                        # State 79869
                                        if len(subjects2) == 0:
                                            pass
                                            # State 79870
                                            if len(subjects) == 0:
                                                pass
                                                # 17: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp120)
                            subjects106.appendleft(tmp118)
                    if len(subjects106) >= 1 and isinstance(subjects106[0], Mul):
                        tmp121 = subjects106.popleft()
                        associative1 = tmp121
                        associative_type1 = type(tmp121)
                        subjects122 = deque(tmp121._args)
                        matcher = CommutativeMatcher79872.get()
                        tmp123 = subjects122
                        subjects122 = []
                        for s in tmp123:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp123, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 79873
                                if len(subjects106) == 0:
                                    pass
                                    # State 79874
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp124 = subjects2.popleft()
                                        # State 79875
                                        if len(subjects2) == 0:
                                            pass
                                            # State 79876
                                            if len(subjects) == 0:
                                                pass
                                                # 17: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp124)
                        subjects106.appendleft(tmp121)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80307
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80308
                        if len(subjects106) >= 1:
                            tmp127 = subjects106.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp127)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80309
                                if len(subjects106) == 0:
                                    pass
                                    # State 80310
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp129 = subjects2.popleft()
                                        # State 80311
                                        if len(subjects2) == 0:
                                            pass
                                            # State 80312
                                            if len(subjects) == 0:
                                                pass
                                                # 19: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp129)
                            subjects106.appendleft(tmp127)
                    if len(subjects106) >= 1 and isinstance(subjects106[0], Mul):
                        tmp130 = subjects106.popleft()
                        associative1 = tmp130
                        associative_type1 = type(tmp130)
                        subjects131 = deque(tmp130._args)
                        matcher = CommutativeMatcher80314.get()
                        tmp132 = subjects131
                        subjects131 = []
                        for s in tmp132:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp132, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80315
                                if len(subjects106) == 0:
                                    pass
                                    # State 80316
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp133 = subjects2.popleft()
                                        # State 80317
                                        if len(subjects2) == 0:
                                            pass
                                            # State 80318
                                            if len(subjects) == 0:
                                                pass
                                                # 19: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp133)
                        subjects106.appendleft(tmp130)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80755
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80756
                        if len(subjects106) >= 1:
                            tmp136 = subjects106.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.4.1.0', tmp136)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80757
                                if len(subjects106) == 0:
                                    pass
                                    # State 80758
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp138 = subjects2.popleft()
                                        # State 80759
                                        if len(subjects2) == 0:
                                            pass
                                            # State 80760
                                            if len(subjects) == 0:
                                                pass
                                                # 20: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp138)
                            subjects106.appendleft(tmp136)
                    if len(subjects106) >= 1 and isinstance(subjects106[0], Mul):
                        tmp139 = subjects106.popleft()
                        associative1 = tmp139
                        associative_type1 = type(tmp139)
                        subjects140 = deque(tmp139._args)
                        matcher = CommutativeMatcher80762.get()
                        tmp141 = subjects140
                        subjects140 = []
                        for s in tmp141:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp141, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80763
                                if len(subjects106) == 0:
                                    pass
                                    # State 80764
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp142 = subjects2.popleft()
                                        # State 80765
                                        if len(subjects2) == 0:
                                            pass
                                            # State 80766
                                            if len(subjects) == 0:
                                                pass
                                                # 20: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp142)
                        subjects106.appendleft(tmp139)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 81858
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 81859
                        if len(subjects106) >= 1:
                            tmp145 = subjects106.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp145)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 81860
                                if len(subjects106) == 0:
                                    pass
                                    # State 81861
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp147 = subjects2.popleft()
                                        # State 81862
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81863
                                            if len(subjects) == 0:
                                                pass
                                                # 22: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp147)
                            subjects106.appendleft(tmp145)
                    if len(subjects106) >= 1 and isinstance(subjects106[0], Mul):
                        tmp148 = subjects106.popleft()
                        associative1 = tmp148
                        associative_type1 = type(tmp148)
                        subjects149 = deque(tmp148._args)
                        matcher = CommutativeMatcher81865.get()
                        tmp150 = subjects149
                        subjects149 = []
                        for s in tmp150:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp150, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 81866
                                if len(subjects106) == 0:
                                    pass
                                    # State 81867
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp151 = subjects2.popleft()
                                        # State 81868
                                        if len(subjects2) == 0:
                                            pass
                                            # State 81869
                                            if len(subjects) == 0:
                                                pass
                                                # 22: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp151)
                        subjects106.appendleft(tmp148)
                if len(subjects106) >= 1 and isinstance(subjects106[0], Add):
                    tmp152 = subjects106.popleft()
                    associative1 = tmp152
                    associative_type1 = type(tmp152)
                    subjects153 = deque(tmp152._args)
                    matcher = CommutativeMatcher78555.get()
                    tmp154 = subjects153
                    subjects153 = []
                    for s in tmp154:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp154, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 78561
                            if len(subjects106) == 0:
                                pass
                                # State 78562
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp155 = subjects2.popleft()
                                    # State 78563
                                    if len(subjects2) == 0:
                                        pass
                                        # State 78564
                                        if len(subjects) == 0:
                                            pass
                                            # 16: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp155)
                        if pattern_index == 1:
                            pass
                            # State 79880
                            if len(subjects106) == 0:
                                pass
                                # State 79881
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp156 = subjects2.popleft()
                                    # State 79882
                                    if len(subjects2) == 0:
                                        pass
                                        # State 79883
                                        if len(subjects) == 0:
                                            pass
                                            # 17: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp156)
                        if pattern_index == 2:
                            pass
                            # State 80322
                            if len(subjects106) == 0:
                                pass
                                # State 80323
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp157 = subjects2.popleft()
                                    # State 80324
                                    if len(subjects2) == 0:
                                        pass
                                        # State 80325
                                        if len(subjects) == 0:
                                            pass
                                            # 19: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp157)
                        if pattern_index == 3:
                            pass
                            # State 80770
                            if len(subjects106) == 0:
                                pass
                                # State 80771
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp158 = subjects2.popleft()
                                    # State 80772
                                    if len(subjects2) == 0:
                                        pass
                                        # State 80773
                                        if len(subjects) == 0:
                                            pass
                                            # 20: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp158)
                        if pattern_index == 4:
                            pass
                            # State 81873
                            if len(subjects106) == 0:
                                pass
                                # State 81874
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp159 = subjects2.popleft()
                                    # State 81875
                                    if len(subjects2) == 0:
                                        pass
                                        # State 81876
                                        if len(subjects) == 0:
                                            pass
                                            # 22: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp159)
                    subjects106.appendleft(tmp152)
                subjects2.appendleft(tmp105)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 7843
            if len(subjects) >= 1:
                tmp161 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp161)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7844
                    if len(subjects) == 0:
                        pass
                        # 3: x**n
                subjects.appendleft(tmp161)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 16219
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp164 = subjects.popleft()
                subjects165 = deque(tmp164._args)
                # State 16220
                if len(subjects165) >= 1:
                    tmp166 = subjects165.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', tmp166)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 16221
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 16222
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 16223
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.4.1.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 16224
                                    if len(subjects165) >= 1:
                                        tmp171 = subjects165.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.3.1.1.0', tmp171)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 16225
                                            if len(subjects165) == 0:
                                                pass
                                                # State 16226
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (F**(g*(e + f*x)))**n
                                        subjects165.appendleft(tmp171)
                                if len(subjects165) >= 1 and isinstance(subjects165[0], Mul):
                                    tmp173 = subjects165.popleft()
                                    associative1 = tmp173
                                    associative_type1 = type(tmp173)
                                    subjects174 = deque(tmp173._args)
                                    matcher = CommutativeMatcher16228.get()
                                    tmp175 = subjects174
                                    subjects174 = []
                                    for s in tmp175:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp175, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 16229
                                            if len(subjects165) == 0:
                                                pass
                                                # State 16230
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (F**(g*(e + f*x)))**n
                                    subjects165.appendleft(tmp173)
                            if len(subjects165) >= 1 and isinstance(subjects165[0], Add):
                                tmp176 = subjects165.popleft()
                                associative1 = tmp176
                                associative_type1 = type(tmp176)
                                subjects177 = deque(tmp176._args)
                                matcher = CommutativeMatcher16232.get()
                                tmp178 = subjects177
                                subjects177 = []
                                for s in tmp178:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp178, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 16238
                                        if len(subjects165) == 0:
                                            pass
                                            # State 16239
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (F**(g*(e + f*x)))**n
                                subjects165.appendleft(tmp176)
                        if len(subjects165) >= 1 and isinstance(subjects165[0], Mul):
                            tmp179 = subjects165.popleft()
                            associative1 = tmp179
                            associative_type1 = type(tmp179)
                            subjects180 = deque(tmp179._args)
                            matcher = CommutativeMatcher16241.get()
                            tmp181 = subjects180
                            subjects180 = []
                            for s in tmp181:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp181, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 16256
                                    if len(subjects165) == 0:
                                        pass
                                        # State 16257
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (F**(g*(e + f*x)))**n
                            subjects165.appendleft(tmp179)
                    subjects165.appendleft(tmp166)
                subjects.appendleft(tmp164)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp182 = subjects.popleft()
            subjects183 = deque(tmp182._args)
            # State 36538
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 36539
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 36540
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 36541
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 36542
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 36543
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 36544
                                    if len(subjects183) >= 1 and isinstance(subjects183[0], Pow):
                                        tmp190 = subjects183.popleft()
                                        subjects191 = deque(tmp190._args)
                                        # State 36545
                                        if len(subjects191) >= 1:
                                            tmp192 = subjects191.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.1', tmp192)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 36546
                                                if len(subjects191) >= 1:
                                                    tmp194 = subjects191.popleft()
                                                    subst8 = Substitution(subst7)
                                                    try:
                                                        subst8.try_add_variable('i2.2.1.2', tmp194)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 36547
                                                        if len(subjects191) == 0:
                                                            pass
                                                            # State 36548
                                                            if len(subjects183) == 0:
                                                                pass
                                                                # State 36549
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                    subjects191.appendleft(tmp194)
                                            subjects191.appendleft(tmp192)
                                        subjects183.appendleft(tmp190)
                                if len(subjects183) >= 1 and isinstance(subjects183[0], Mul):
                                    tmp196 = subjects183.popleft()
                                    associative1 = tmp196
                                    associative_type1 = type(tmp196)
                                    subjects197 = deque(tmp196._args)
                                    matcher = CommutativeMatcher36551.get()
                                    tmp198 = subjects197
                                    subjects197 = []
                                    for s in tmp198:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp198, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 36556
                                            if len(subjects183) == 0:
                                                pass
                                                # State 36557
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                    subjects183.appendleft(tmp196)
                            if len(subjects183) >= 1 and isinstance(subjects183[0], Add):
                                tmp199 = subjects183.popleft()
                                associative1 = tmp199
                                associative_type1 = type(tmp199)
                                subjects200 = deque(tmp199._args)
                                matcher = CommutativeMatcher36559.get()
                                tmp201 = subjects200
                                subjects200 = []
                                for s in tmp201:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp201, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 36572
                                        if len(subjects183) == 0:
                                            pass
                                            # State 36573
                                            if len(subjects) == 0:
                                                pass
                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                subjects183.appendleft(tmp199)
                        if len(subjects183) >= 1 and isinstance(subjects183[0], Pow):
                            tmp202 = subjects183.popleft()
                            subjects203 = deque(tmp202._args)
                            # State 36574
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 36575
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 36576
                                    if len(subjects203) >= 1 and isinstance(subjects203[0], Pow):
                                        tmp206 = subjects203.popleft()
                                        subjects207 = deque(tmp206._args)
                                        # State 36577
                                        if len(subjects207) >= 1:
                                            tmp208 = subjects207.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.1', tmp208)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 36578
                                                if len(subjects207) >= 1:
                                                    tmp210 = subjects207.popleft()
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2', tmp210)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 36579
                                                        if len(subjects207) == 0:
                                                            pass
                                                            # State 36580
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i2.2.1.2.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 36581
                                                                if len(subjects203) == 0:
                                                                    pass
                                                                    # State 36582
                                                                    if len(subjects183) == 0:
                                                                        pass
                                                                        # State 36583
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                            if len(subjects203) >= 1:
                                                                tmp213 = subjects203.popleft()
                                                                subst8 = Substitution(subst7)
                                                                try:
                                                                    subst8.try_add_variable('i2.2.1.2.2.2', tmp213)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 36581
                                                                    if len(subjects203) == 0:
                                                                        pass
                                                                        # State 36582
                                                                        if len(subjects183) == 0:
                                                                            pass
                                                                            # State 36583
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                subjects203.appendleft(tmp213)
                                                    subjects207.appendleft(tmp210)
                                            subjects207.appendleft(tmp208)
                                        subjects203.appendleft(tmp206)
                                if len(subjects203) >= 1 and isinstance(subjects203[0], Mul):
                                    tmp215 = subjects203.popleft()
                                    associative1 = tmp215
                                    associative_type1 = type(tmp215)
                                    subjects216 = deque(tmp215._args)
                                    matcher = CommutativeMatcher36585.get()
                                    tmp217 = subjects216
                                    subjects216 = []
                                    for s in tmp217:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp217, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 36590
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 36591
                                                if len(subjects203) == 0:
                                                    pass
                                                    # State 36592
                                                    if len(subjects183) == 0:
                                                        pass
                                                        # State 36593
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                            if len(subjects203) >= 1:
                                                tmp219 = []
                                                tmp219.append(subjects203.popleft())
                                                while True:
                                                    if len(tmp219) > 1:
                                                        tmp220 = create_operation_expression(associative1, tmp219)
                                                    elif len(tmp219) == 1:
                                                        tmp220 = tmp219[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', tmp220)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 36591
                                                        if len(subjects203) == 0:
                                                            pass
                                                            # State 36592
                                                            if len(subjects183) == 0:
                                                                pass
                                                                # State 36593
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                    if len(subjects203) == 0:
                                                        break
                                                    tmp219.append(subjects203.popleft())
                                                subjects203.extendleft(reversed(tmp219))
                                    subjects203.appendleft(tmp215)
                            if len(subjects203) >= 1 and isinstance(subjects203[0], Add):
                                tmp222 = subjects203.popleft()
                                associative1 = tmp222
                                associative_type1 = type(tmp222)
                                subjects223 = deque(tmp222._args)
                                matcher = CommutativeMatcher36595.get()
                                tmp224 = subjects223
                                subjects223 = []
                                for s in tmp224:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp224, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 36608
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 36609
                                            if len(subjects203) == 0:
                                                pass
                                                # State 36610
                                                if len(subjects183) == 0:
                                                    pass
                                                    # State 36611
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                        if len(subjects203) >= 1:
                                            tmp226 = []
                                            tmp226.append(subjects203.popleft())
                                            while True:
                                                if len(tmp226) > 1:
                                                    tmp227 = create_operation_expression(associative1, tmp226)
                                                elif len(tmp226) == 1:
                                                    tmp227 = tmp226[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp227)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 36609
                                                    if len(subjects203) == 0:
                                                        pass
                                                        # State 36610
                                                        if len(subjects183) == 0:
                                                            pass
                                                            # State 36611
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                if len(subjects203) == 0:
                                                    break
                                                tmp226.append(subjects203.popleft())
                                            subjects203.extendleft(reversed(tmp226))
                                subjects203.appendleft(tmp222)
                            subjects183.appendleft(tmp202)
                    if len(subjects183) >= 1 and isinstance(subjects183[0], Mul):
                        tmp229 = subjects183.popleft()
                        associative1 = tmp229
                        associative_type1 = type(tmp229)
                        subjects230 = deque(tmp229._args)
                        matcher = CommutativeMatcher36613.get()
                        tmp231 = subjects230
                        subjects230 = []
                        for s in tmp231:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp231, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 36678
                                if len(subjects183) == 0:
                                    pass
                                    # State 36679
                                    if len(subjects) == 0:
                                        pass
                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                        subjects183.appendleft(tmp229)
                if len(subjects183) >= 1 and isinstance(subjects183[0], Pow):
                    tmp232 = subjects183.popleft()
                    subjects233 = deque(tmp232._args)
                    # State 36680
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 36681
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 36682
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 36683
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 36684
                                    if len(subjects233) >= 1 and isinstance(subjects233[0], Pow):
                                        tmp238 = subjects233.popleft()
                                        subjects239 = deque(tmp238._args)
                                        # State 36685
                                        if len(subjects239) >= 1:
                                            tmp240 = subjects239.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.1', tmp240)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 36686
                                                if len(subjects239) >= 1:
                                                    tmp242 = subjects239.popleft()
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2', tmp242)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 36687
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 36688
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 36689
                                                                if len(subjects233) == 0:
                                                                    pass
                                                                    # State 36690
                                                                    if len(subjects183) == 0:
                                                                        pass
                                                                        # State 36691
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                            if len(subjects233) >= 1:
                                                                tmp245 = subjects233.popleft()
                                                                subst8 = Substitution(subst7)
                                                                try:
                                                                    subst8.try_add_variable('i2.2.1.2.2', tmp245)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 36689
                                                                    if len(subjects233) == 0:
                                                                        pass
                                                                        # State 36690
                                                                        if len(subjects183) == 0:
                                                                            pass
                                                                            # State 36691
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                subjects233.appendleft(tmp245)
                                                    subjects239.appendleft(tmp242)
                                            subjects239.appendleft(tmp240)
                                        subjects233.appendleft(tmp238)
                                if len(subjects233) >= 1 and isinstance(subjects233[0], Mul):
                                    tmp247 = subjects233.popleft()
                                    associative1 = tmp247
                                    associative_type1 = type(tmp247)
                                    subjects248 = deque(tmp247._args)
                                    matcher = CommutativeMatcher36693.get()
                                    tmp249 = subjects248
                                    subjects248 = []
                                    for s in tmp249:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp249, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 36698
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 36699
                                                if len(subjects233) == 0:
                                                    pass
                                                    # State 36700
                                                    if len(subjects183) == 0:
                                                        pass
                                                        # State 36701
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                            if len(subjects233) >= 1:
                                                tmp251 = []
                                                tmp251.append(subjects233.popleft())
                                                while True:
                                                    if len(tmp251) > 1:
                                                        tmp252 = create_operation_expression(associative1, tmp251)
                                                    elif len(tmp251) == 1:
                                                        tmp252 = tmp251[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp252)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 36699
                                                        if len(subjects233) == 0:
                                                            pass
                                                            # State 36700
                                                            if len(subjects183) == 0:
                                                                pass
                                                                # State 36701
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                    if len(subjects233) == 0:
                                                        break
                                                    tmp251.append(subjects233.popleft())
                                                subjects233.extendleft(reversed(tmp251))
                                    subjects233.appendleft(tmp247)
                            if len(subjects233) >= 1 and isinstance(subjects233[0], Add):
                                tmp254 = subjects233.popleft()
                                associative1 = tmp254
                                associative_type1 = type(tmp254)
                                subjects255 = deque(tmp254._args)
                                matcher = CommutativeMatcher36703.get()
                                tmp256 = subjects255
                                subjects255 = []
                                for s in tmp256:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp256, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 36716
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 36717
                                            if len(subjects233) == 0:
                                                pass
                                                # State 36718
                                                if len(subjects183) == 0:
                                                    pass
                                                    # State 36719
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                        if len(subjects233) >= 1:
                                            tmp258 = []
                                            tmp258.append(subjects233.popleft())
                                            while True:
                                                if len(tmp258) > 1:
                                                    tmp259 = create_operation_expression(associative1, tmp258)
                                                elif len(tmp258) == 1:
                                                    tmp259 = tmp258[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp259)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 36717
                                                    if len(subjects233) == 0:
                                                        pass
                                                        # State 36718
                                                        if len(subjects183) == 0:
                                                            pass
                                                            # State 36719
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                if len(subjects233) == 0:
                                                    break
                                                tmp258.append(subjects233.popleft())
                                            subjects233.extendleft(reversed(tmp258))
                                subjects233.appendleft(tmp254)
                        if len(subjects233) >= 1 and isinstance(subjects233[0], Pow):
                            tmp261 = subjects233.popleft()
                            subjects262 = deque(tmp261._args)
                            # State 36720
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 36721
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 36722
                                    if len(subjects262) >= 1 and isinstance(subjects262[0], Pow):
                                        tmp265 = subjects262.popleft()
                                        subjects266 = deque(tmp265._args)
                                        # State 36723
                                        if len(subjects266) >= 1:
                                            tmp267 = subjects266.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.1', tmp267)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 36724
                                                if len(subjects266) >= 1:
                                                    tmp269 = subjects266.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2', tmp269)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 36725
                                                        if len(subjects266) == 0:
                                                            pass
                                                            # State 36726
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 36727
                                                                if len(subjects262) == 0:
                                                                    pass
                                                                    # State 36728
                                                                    subst8 = Substitution(subst7)
                                                                    try:
                                                                        subst8.try_add_variable('i2.2.1.2.2', 1)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 36729
                                                                        if len(subjects233) == 0:
                                                                            pass
                                                                            # State 36730
                                                                            if len(subjects183) == 0:
                                                                                pass
                                                                                # State 36731
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                    if len(subjects233) >= 1:
                                                                        tmp273 = subjects233.popleft()
                                                                        subst8 = Substitution(subst7)
                                                                        try:
                                                                            subst8.try_add_variable('i2.2.1.2.2', tmp273)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            # State 36729
                                                                            if len(subjects233) == 0:
                                                                                pass
                                                                                # State 36730
                                                                                if len(subjects183) == 0:
                                                                                    pass
                                                                                    # State 36731
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                        subjects233.appendleft(tmp273)
                                                            if len(subjects262) >= 1:
                                                                tmp275 = subjects262.popleft()
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2.2', tmp275)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 36727
                                                                    if len(subjects262) == 0:
                                                                        pass
                                                                        # State 36728
                                                                        subst8 = Substitution(subst7)
                                                                        try:
                                                                            subst8.try_add_variable('i2.2.1.2.2', 1)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            # State 36729
                                                                            if len(subjects233) == 0:
                                                                                pass
                                                                                # State 36730
                                                                                if len(subjects183) == 0:
                                                                                    pass
                                                                                    # State 36731
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                        if len(subjects233) >= 1:
                                                                            tmp278 = subjects233.popleft()
                                                                            subst8 = Substitution(subst7)
                                                                            try:
                                                                                subst8.try_add_variable('i2.2.1.2.2', tmp278)
                                                                            except ValueError:
                                                                                pass
                                                                            else:
                                                                                pass
                                                                                # State 36729
                                                                                if len(subjects233) == 0:
                                                                                    pass
                                                                                    # State 36730
                                                                                    if len(subjects183) == 0:
                                                                                        pass
                                                                                        # State 36731
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                            subjects233.appendleft(tmp278)
                                                                subjects262.appendleft(tmp275)
                                                    subjects266.appendleft(tmp269)
                                            subjects266.appendleft(tmp267)
                                        subjects262.appendleft(tmp265)
                                if len(subjects262) >= 1 and isinstance(subjects262[0], Mul):
                                    tmp280 = subjects262.popleft()
                                    associative1 = tmp280
                                    associative_type1 = type(tmp280)
                                    subjects281 = deque(tmp280._args)
                                    matcher = CommutativeMatcher36733.get()
                                    tmp282 = subjects281
                                    subjects281 = []
                                    for s in tmp282:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp282, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 36738
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 36739
                                                if len(subjects262) == 0:
                                                    pass
                                                    # State 36740
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 36741
                                                        if len(subjects233) == 0:
                                                            pass
                                                            # State 36742
                                                            if len(subjects183) == 0:
                                                                pass
                                                                # State 36743
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                    if len(subjects233) >= 1:
                                                        tmp285 = subjects233.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp285)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 36741
                                                            if len(subjects233) == 0:
                                                                pass
                                                                # State 36742
                                                                if len(subjects183) == 0:
                                                                    pass
                                                                    # State 36743
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                        subjects233.appendleft(tmp285)
                                            if len(subjects262) >= 1:
                                                tmp287 = []
                                                tmp287.append(subjects262.popleft())
                                                while True:
                                                    if len(tmp287) > 1:
                                                        tmp288 = create_operation_expression(associative1, tmp287)
                                                    elif len(tmp287) == 1:
                                                        tmp288 = tmp287[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2.2', tmp288)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 36739
                                                        if len(subjects262) == 0:
                                                            pass
                                                            # State 36740
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 36741
                                                                if len(subjects233) == 0:
                                                                    pass
                                                                    # State 36742
                                                                    if len(subjects183) == 0:
                                                                        pass
                                                                        # State 36743
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                            if len(subjects233) >= 1:
                                                                tmp291 = subjects233.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2.1.2.2', tmp291)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 36741
                                                                    if len(subjects233) == 0:
                                                                        pass
                                                                        # State 36742
                                                                        if len(subjects183) == 0:
                                                                            pass
                                                                            # State 36743
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                subjects233.appendleft(tmp291)
                                                    if len(subjects262) == 0:
                                                        break
                                                    tmp287.append(subjects262.popleft())
                                                subjects262.extendleft(reversed(tmp287))
                                    subjects262.appendleft(tmp280)
                            if len(subjects262) >= 1 and isinstance(subjects262[0], Add):
                                tmp293 = subjects262.popleft()
                                associative1 = tmp293
                                associative_type1 = type(tmp293)
                                subjects294 = deque(tmp293._args)
                                matcher = CommutativeMatcher36745.get()
                                tmp295 = subjects294
                                subjects294 = []
                                for s in tmp295:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp295, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 36758
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 36759
                                            if len(subjects262) == 0:
                                                pass
                                                # State 36760
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 36761
                                                    if len(subjects233) == 0:
                                                        pass
                                                        # State 36762
                                                        if len(subjects183) == 0:
                                                            pass
                                                            # State 36763
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                if len(subjects233) >= 1:
                                                    tmp298 = subjects233.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp298)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 36761
                                                        if len(subjects233) == 0:
                                                            pass
                                                            # State 36762
                                                            if len(subjects183) == 0:
                                                                pass
                                                                # State 36763
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                    subjects233.appendleft(tmp298)
                                        if len(subjects262) >= 1:
                                            tmp300 = []
                                            tmp300.append(subjects262.popleft())
                                            while True:
                                                if len(tmp300) > 1:
                                                    tmp301 = create_operation_expression(associative1, tmp300)
                                                elif len(tmp300) == 1:
                                                    tmp301 = tmp300[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp301)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 36759
                                                    if len(subjects262) == 0:
                                                        pass
                                                        # State 36760
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 36761
                                                            if len(subjects233) == 0:
                                                                pass
                                                                # State 36762
                                                                if len(subjects183) == 0:
                                                                    pass
                                                                    # State 36763
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                        if len(subjects233) >= 1:
                                                            tmp304 = subjects233.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp304)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 36761
                                                                if len(subjects233) == 0:
                                                                    pass
                                                                    # State 36762
                                                                    if len(subjects183) == 0:
                                                                        pass
                                                                        # State 36763
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                            subjects233.appendleft(tmp304)
                                                if len(subjects262) == 0:
                                                    break
                                                tmp300.append(subjects262.popleft())
                                            subjects262.extendleft(reversed(tmp300))
                                subjects262.appendleft(tmp293)
                            subjects233.appendleft(tmp261)
                    if len(subjects233) >= 1 and isinstance(subjects233[0], Mul):
                        tmp306 = subjects233.popleft()
                        associative1 = tmp306
                        associative_type1 = type(tmp306)
                        subjects307 = deque(tmp306._args)
                        matcher = CommutativeMatcher36765.get()
                        tmp308 = subjects307
                        subjects307 = []
                        for s in tmp308:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp308, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 36830
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 36831
                                    if len(subjects233) == 0:
                                        pass
                                        # State 36832
                                        if len(subjects183) == 0:
                                            pass
                                            # State 36833
                                            if len(subjects) == 0:
                                                pass
                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                if len(subjects233) >= 1:
                                    tmp310 = []
                                    tmp310.append(subjects233.popleft())
                                    while True:
                                        if len(tmp310) > 1:
                                            tmp311 = create_operation_expression(associative1, tmp310)
                                        elif len(tmp310) == 1:
                                            tmp311 = tmp310[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp311)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 36831
                                            if len(subjects233) == 0:
                                                pass
                                                # State 36832
                                                if len(subjects183) == 0:
                                                    pass
                                                    # State 36833
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                        if len(subjects233) == 0:
                                            break
                                        tmp310.append(subjects233.popleft())
                                    subjects233.extendleft(reversed(tmp310))
                        subjects233.appendleft(tmp306)
                    subjects183.appendleft(tmp232)
            if len(subjects183) >= 1 and isinstance(subjects183[0], Mul):
                tmp313 = subjects183.popleft()
                associative1 = tmp313
                associative_type1 = type(tmp313)
                subjects314 = deque(tmp313._args)
                matcher = CommutativeMatcher36835.get()
                tmp315 = subjects314
                subjects314 = []
                for s in tmp315:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp315, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 37116
                        if len(subjects183) == 0:
                            pass
                            # State 37117
                            if len(subjects) == 0:
                                pass
                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                subjects183.appendleft(tmp313)
            subjects.appendleft(tmp182)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp316 = subjects.popleft()
            subjects317 = deque(tmp316._args)
            # State 60831
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 60832
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 60833
                    if len(subjects317) >= 1:
                        tmp320 = subjects317.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp320)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 60834
                            if len(subjects317) == 0:
                                pass
                                # State 60835
                                if len(subjects) == 0:
                                    pass
                                    # 6: sin(c + x*d)
                        subjects317.appendleft(tmp320)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 72357
                    if len(subjects317) >= 1:
                        tmp323 = subjects317.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp323)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 72358
                            if len(subjects317) == 0:
                                pass
                                # State 72359
                                if len(subjects) == 0:
                                    pass
                                    # 14: sin(x*f + e)
                        subjects317.appendleft(tmp323)
                if len(subjects317) >= 1 and isinstance(subjects317[0], Mul):
                    tmp325 = subjects317.popleft()
                    associative1 = tmp325
                    associative_type1 = type(tmp325)
                    subjects326 = deque(tmp325._args)
                    matcher = CommutativeMatcher60837.get()
                    tmp327 = subjects326
                    subjects326 = []
                    for s in tmp327:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp327, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 60838
                            if len(subjects317) == 0:
                                pass
                                # State 60839
                                if len(subjects) == 0:
                                    pass
                                    # 6: sin(c + x*d)
                        if pattern_index == 1:
                            pass
                            # State 72360
                            if len(subjects317) == 0:
                                pass
                                # State 72361
                                if len(subjects) == 0:
                                    pass
                                    # 14: sin(x*f + e)
                    subjects317.appendleft(tmp325)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 61476
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61477
                    if len(subjects317) >= 1:
                        tmp330 = subjects317.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp330)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61478
                            if len(subjects317) == 0:
                                pass
                                # State 61479
                                if len(subjects) == 0:
                                    pass
                                    # 8: sin(e + x*f)
                        subjects317.appendleft(tmp330)
                if len(subjects317) >= 1 and isinstance(subjects317[0], Mul):
                    tmp332 = subjects317.popleft()
                    associative1 = tmp332
                    associative_type1 = type(tmp332)
                    subjects333 = deque(tmp332._args)
                    matcher = CommutativeMatcher61481.get()
                    tmp334 = subjects333
                    subjects333 = []
                    for s in tmp334:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp334, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 61482
                            if len(subjects317) == 0:
                                pass
                                # State 61483
                                if len(subjects) == 0:
                                    pass
                                    # 8: sin(e + x*f)
                    subjects317.appendleft(tmp332)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63202
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63203
                    if len(subjects317) >= 1:
                        tmp337 = subjects317.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp337)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63204
                            if len(subjects317) == 0:
                                pass
                                # State 63205
                                if len(subjects) == 0:
                                    pass
                                    # 10: sin(e + x*f)
                        subjects317.appendleft(tmp337)
                if len(subjects317) >= 1 and isinstance(subjects317[0], Mul):
                    tmp339 = subjects317.popleft()
                    associative1 = tmp339
                    associative_type1 = type(tmp339)
                    subjects340 = deque(tmp339._args)
                    matcher = CommutativeMatcher63207.get()
                    tmp341 = subjects340
                    subjects340 = []
                    for s in tmp341:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp341, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63208
                            if len(subjects317) == 0:
                                pass
                                # State 63209
                                if len(subjects) == 0:
                                    pass
                                    # 10: sin(e + x*f)
                    subjects317.appendleft(tmp339)
            if len(subjects317) >= 1 and isinstance(subjects317[0], Add):
                tmp342 = subjects317.popleft()
                associative1 = tmp342
                associative_type1 = type(tmp342)
                subjects343 = deque(tmp342._args)
                matcher = CommutativeMatcher60841.get()
                tmp344 = subjects343
                subjects343 = []
                for s in tmp344:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp344, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 60847
                        if len(subjects317) == 0:
                            pass
                            # State 60848
                            if len(subjects) == 0:
                                pass
                                # 6: sin(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 61487
                        if len(subjects317) == 0:
                            pass
                            # State 61488
                            if len(subjects) == 0:
                                pass
                                # 8: sin(e + x*f)
                    if pattern_index == 2:
                        pass
                        # State 63213
                        if len(subjects317) == 0:
                            pass
                            # State 63214
                            if len(subjects) == 0:
                                pass
                                # 10: sin(e + x*f)
                    if pattern_index == 3:
                        pass
                        # State 72365
                        if len(subjects317) == 0:
                            pass
                            # State 72366
                            if len(subjects) == 0:
                                pass
                                # 14: sin(x*f + e)
                subjects317.appendleft(tmp342)
            subjects.appendleft(tmp316)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp345 = subjects.popleft()
            subjects346 = deque(tmp345._args)
            # State 60882
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 60883
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 60884
                    if len(subjects346) >= 1:
                        tmp349 = subjects346.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp349)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 60885
                            if len(subjects346) == 0:
                                pass
                                # State 60886
                                if len(subjects) == 0:
                                    pass
                                    # 7: cos(c + x*d)
                        subjects346.appendleft(tmp349)
                if len(subjects346) >= 1 and isinstance(subjects346[0], Mul):
                    tmp351 = subjects346.popleft()
                    associative1 = tmp351
                    associative_type1 = type(tmp351)
                    subjects352 = deque(tmp351._args)
                    matcher = CommutativeMatcher60888.get()
                    tmp353 = subjects352
                    subjects352 = []
                    for s in tmp353:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp353, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 60889
                            if len(subjects346) == 0:
                                pass
                                # State 60890
                                if len(subjects) == 0:
                                    pass
                                    # 7: cos(c + x*d)
                    subjects346.appendleft(tmp351)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 61705
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61706
                    if len(subjects346) >= 1:
                        tmp356 = subjects346.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp356)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61707
                            if len(subjects346) == 0:
                                pass
                                # State 61708
                                if len(subjects) == 0:
                                    pass
                                    # 9: cos(e + x*f)
                        subjects346.appendleft(tmp356)
                if len(subjects346) >= 1 and isinstance(subjects346[0], Mul):
                    tmp358 = subjects346.popleft()
                    associative1 = tmp358
                    associative_type1 = type(tmp358)
                    subjects359 = deque(tmp358._args)
                    matcher = CommutativeMatcher61710.get()
                    tmp360 = subjects359
                    subjects359 = []
                    for s in tmp360:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp360, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 61711
                            if len(subjects346) == 0:
                                pass
                                # State 61712
                                if len(subjects) == 0:
                                    pass
                                    # 9: cos(e + x*f)
                    subjects346.appendleft(tmp358)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63378
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63379
                    if len(subjects346) >= 1:
                        tmp363 = subjects346.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp363)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63380
                            if len(subjects346) == 0:
                                pass
                                # State 63381
                                if len(subjects) == 0:
                                    pass
                                    # 11: cos(e + x*f)
                        subjects346.appendleft(tmp363)
                if len(subjects346) >= 1 and isinstance(subjects346[0], Mul):
                    tmp365 = subjects346.popleft()
                    associative1 = tmp365
                    associative_type1 = type(tmp365)
                    subjects366 = deque(tmp365._args)
                    matcher = CommutativeMatcher63383.get()
                    tmp367 = subjects366
                    subjects366 = []
                    for s in tmp367:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp367, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63384
                            if len(subjects346) == 0:
                                pass
                                # State 63385
                                if len(subjects) == 0:
                                    pass
                                    # 11: cos(e + x*f)
                    subjects346.appendleft(tmp365)
            if len(subjects346) >= 1 and isinstance(subjects346[0], Add):
                tmp368 = subjects346.popleft()
                associative1 = tmp368
                associative_type1 = type(tmp368)
                subjects369 = deque(tmp368._args)
                matcher = CommutativeMatcher60892.get()
                tmp370 = subjects369
                subjects369 = []
                for s in tmp370:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp370, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 60898
                        if len(subjects346) == 0:
                            pass
                            # State 60899
                            if len(subjects) == 0:
                                pass
                                # 7: cos(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 61716
                        if len(subjects346) == 0:
                            pass
                            # State 61717
                            if len(subjects) == 0:
                                pass
                                # 9: cos(e + x*f)
                    if pattern_index == 2:
                        pass
                        # State 63389
                        if len(subjects346) == 0:
                            pass
                            # State 63390
                            if len(subjects) == 0:
                                pass
                                # 11: cos(e + x*f)
                subjects346.appendleft(tmp368)
            subjects.appendleft(tmp345)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp371 = subjects.popleft()
            subjects372 = deque(tmp371._args)
            # State 78446
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 78447
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78448
                    if len(subjects372) >= 1:
                        tmp375 = subjects372.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp375)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 78449
                            if len(subjects372) == 0:
                                pass
                                # State 78450
                                if len(subjects) == 0:
                                    pass
                                    # 15: tan(e + x*f)
                        subjects372.appendleft(tmp375)
                if len(subjects372) >= 1 and isinstance(subjects372[0], Mul):
                    tmp377 = subjects372.popleft()
                    associative1 = tmp377
                    associative_type1 = type(tmp377)
                    subjects378 = deque(tmp377._args)
                    matcher = CommutativeMatcher78452.get()
                    tmp379 = subjects378
                    subjects378 = []
                    for s in tmp379:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp379, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 78453
                            if len(subjects372) == 0:
                                pass
                                # State 78454
                                if len(subjects) == 0:
                                    pass
                                    # 15: tan(e + x*f)
                    subjects372.appendleft(tmp377)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 80053
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80054
                    if len(subjects372) >= 1:
                        tmp382 = subjects372.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp382)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 80055
                            if len(subjects372) == 0:
                                pass
                                # State 80056
                                if len(subjects) == 0:
                                    pass
                                    # 18: tan(e + x*f)
                        subjects372.appendleft(tmp382)
                if len(subjects372) >= 1 and isinstance(subjects372[0], Mul):
                    tmp384 = subjects372.popleft()
                    associative1 = tmp384
                    associative_type1 = type(tmp384)
                    subjects385 = deque(tmp384._args)
                    matcher = CommutativeMatcher80058.get()
                    tmp386 = subjects385
                    subjects385 = []
                    for s in tmp386:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp386, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 80059
                            if len(subjects372) == 0:
                                pass
                                # State 80060
                                if len(subjects) == 0:
                                    pass
                                    # 18: tan(e + x*f)
                    subjects372.appendleft(tmp384)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 81806
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 81807
                    if len(subjects372) >= 1:
                        tmp389 = subjects372.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp389)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 81808
                            if len(subjects372) == 0:
                                pass
                                # State 81809
                                if len(subjects) == 0:
                                    pass
                                    # 21: tan(c + x*d)
                        subjects372.appendleft(tmp389)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 87029
                    if len(subjects372) >= 1:
                        tmp392 = subjects372.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp392)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 87030
                            if len(subjects372) == 0:
                                pass
                                # State 87031
                                if len(subjects) == 0:
                                    pass
                                    # 23: tan(x*f + e)
                        subjects372.appendleft(tmp392)
                if len(subjects372) >= 1 and isinstance(subjects372[0], Mul):
                    tmp394 = subjects372.popleft()
                    associative1 = tmp394
                    associative_type1 = type(tmp394)
                    subjects395 = deque(tmp394._args)
                    matcher = CommutativeMatcher81811.get()
                    tmp396 = subjects395
                    subjects395 = []
                    for s in tmp396:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp396, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 81812
                            if len(subjects372) == 0:
                                pass
                                # State 81813
                                if len(subjects) == 0:
                                    pass
                                    # 21: tan(c + x*d)
                        if pattern_index == 1:
                            pass
                            # State 87032
                            if len(subjects372) == 0:
                                pass
                                # State 87033
                                if len(subjects) == 0:
                                    pass
                                    # 23: tan(x*f + e)
                    subjects372.appendleft(tmp394)
            if len(subjects372) >= 1 and isinstance(subjects372[0], Add):
                tmp397 = subjects372.popleft()
                associative1 = tmp397
                associative_type1 = type(tmp397)
                subjects398 = deque(tmp397._args)
                matcher = CommutativeMatcher78456.get()
                tmp399 = subjects398
                subjects398 = []
                for s in tmp399:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp399, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 78462
                        if len(subjects372) == 0:
                            pass
                            # State 78463
                            if len(subjects) == 0:
                                pass
                                # 15: tan(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 80064
                        if len(subjects372) == 0:
                            pass
                            # State 80065
                            if len(subjects) == 0:
                                pass
                                # 18: tan(e + x*f)
                    if pattern_index == 2:
                        pass
                        # State 81817
                        if len(subjects372) == 0:
                            pass
                            # State 81818
                            if len(subjects) == 0:
                                pass
                                # 21: tan(c + x*d)
                    if pattern_index == 3:
                        pass
                        # State 87037
                        if len(subjects372) == 0:
                            pass
                            # State 87038
                            if len(subjects) == 0:
                                pass
                                # 23: tan(x*f + e)
                subjects372.appendleft(tmp397)
            subjects.appendleft(tmp371)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp400 = subjects.popleft()
            subjects401 = deque(tmp400._args)
            # State 108825
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108826
                if len(subjects401) >= 1:
                    tmp403 = subjects401.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp403)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108827
                        if len(subjects401) == 0:
                            pass
                            # State 108828
                            if len(subjects) == 0:
                                pass
                                # 27: asin(x*c)
                    subjects401.appendleft(tmp403)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109847
                if len(subjects401) >= 1:
                    tmp406 = subjects401.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp406)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109848
                        if len(subjects401) == 0:
                            pass
                            # State 109849
                            if len(subjects) == 0:
                                pass
                                # 29: asin(c*x)
                    subjects401.appendleft(tmp406)
            if len(subjects401) >= 1 and isinstance(subjects401[0], Mul):
                tmp408 = subjects401.popleft()
                associative1 = tmp408
                associative_type1 = type(tmp408)
                subjects409 = deque(tmp408._args)
                matcher = CommutativeMatcher108830.get()
                tmp410 = subjects409
                subjects409 = []
                for s in tmp410:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp410, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108831
                        if len(subjects401) == 0:
                            pass
                            # State 108832
                            if len(subjects) == 0:
                                pass
                                # 27: asin(x*c)
                    if pattern_index == 1:
                        pass
                        # State 109850
                        if len(subjects401) == 0:
                            pass
                            # State 109851
                            if len(subjects) == 0:
                                pass
                                # 29: asin(c*x)
                subjects401.appendleft(tmp408)
            subjects.appendleft(tmp400)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp411 = subjects.popleft()
            subjects412 = deque(tmp411._args)
            # State 108867
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108868
                if len(subjects412) >= 1:
                    tmp414 = subjects412.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp414)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108869
                        if len(subjects412) == 0:
                            pass
                            # State 108870
                            if len(subjects) == 0:
                                pass
                                # 28: acos(x*c)
                    subjects412.appendleft(tmp414)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109903
                if len(subjects412) >= 1:
                    tmp417 = subjects412.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp417)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109904
                        if len(subjects412) == 0:
                            pass
                            # State 109905
                            if len(subjects) == 0:
                                pass
                                # 30: acos(c*x)
                    subjects412.appendleft(tmp417)
            if len(subjects412) >= 1 and isinstance(subjects412[0], Mul):
                tmp419 = subjects412.popleft()
                associative1 = tmp419
                associative_type1 = type(tmp419)
                subjects420 = deque(tmp419._args)
                matcher = CommutativeMatcher108872.get()
                tmp421 = subjects420
                subjects420 = []
                for s in tmp421:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp421, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108873
                        if len(subjects412) == 0:
                            pass
                            # State 108874
                            if len(subjects) == 0:
                                pass
                                # 28: acos(x*c)
                    if pattern_index == 1:
                        pass
                        # State 109906
                        if len(subjects412) == 0:
                            pass
                            # State 109907
                            if len(subjects) == 0:
                                pass
                                # 30: acos(c*x)
                subjects412.appendleft(tmp419)
            subjects.appendleft(tmp411)
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp422 = subjects.popleft()
            subjects423 = deque(tmp422._args)
            # State 113476
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113477
                if len(subjects423) >= 1:
                    tmp425 = subjects423.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp425)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113478
                        if len(subjects423) == 0:
                            pass
                            # State 113479
                            if len(subjects) == 0:
                                pass
                                # 31: atan(x*c)
                    subjects423.appendleft(tmp425)
            if len(subjects423) >= 1 and isinstance(subjects423[0], Mul):
                tmp427 = subjects423.popleft()
                associative1 = tmp427
                associative_type1 = type(tmp427)
                subjects428 = deque(tmp427._args)
                matcher = CommutativeMatcher113481.get()
                tmp429 = subjects428
                subjects428 = []
                for s in tmp429:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp429, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 113482
                        if len(subjects423) == 0:
                            pass
                            # State 113483
                            if len(subjects) == 0:
                                pass
                                # 31: atan(x*c)
                subjects423.appendleft(tmp427)
            subjects.appendleft(tmp422)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp430 = subjects.popleft()
            subjects431 = deque(tmp430._args)
            # State 113525
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113526
                if len(subjects431) >= 1:
                    tmp433 = subjects431.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp433)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113527
                        if len(subjects431) == 0:
                            pass
                            # State 113528
                            if len(subjects) == 0:
                                pass
                                # 32: acot(x*c)
                    subjects431.appendleft(tmp433)
            if len(subjects431) >= 1 and isinstance(subjects431[0], Mul):
                tmp435 = subjects431.popleft()
                associative1 = tmp435
                associative_type1 = type(tmp435)
                subjects436 = deque(tmp435._args)
                matcher = CommutativeMatcher113530.get()
                tmp437 = subjects436
                subjects436 = []
                for s in tmp437:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp437, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 113531
                        if len(subjects431) == 0:
                            pass
                            # State 113532
                            if len(subjects) == 0:
                                pass
                                # 32: acot(x*c)
                subjects431.appendleft(tmp435)
            subjects.appendleft(tmp430)
        if len(subjects) >= 1 and isinstance(subjects[0], asec):
            tmp438 = subjects.popleft()
            subjects439 = deque(tmp438._args)
            # State 119947
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119948
                if len(subjects439) >= 1:
                    tmp441 = subjects439.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp441)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119949
                        if len(subjects439) == 0:
                            pass
                            # State 119950
                            if len(subjects) == 0:
                                pass
                                # 33: asec(x*c)
                    subjects439.appendleft(tmp441)
            if len(subjects439) >= 1 and isinstance(subjects439[0], Mul):
                tmp443 = subjects439.popleft()
                associative1 = tmp443
                associative_type1 = type(tmp443)
                subjects444 = deque(tmp443._args)
                matcher = CommutativeMatcher119952.get()
                tmp445 = subjects444
                subjects444 = []
                for s in tmp445:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp445, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119953
                        if len(subjects439) == 0:
                            pass
                            # State 119954
                            if len(subjects) == 0:
                                pass
                                # 33: asec(x*c)
                subjects439.appendleft(tmp443)
            subjects.appendleft(tmp438)
        if len(subjects) >= 1 and isinstance(subjects[0], acsc):
            tmp446 = subjects.popleft()
            subjects447 = deque(tmp446._args)
            # State 120025
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 120026
                if len(subjects447) >= 1:
                    tmp449 = subjects447.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp449)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 120027
                        if len(subjects447) == 0:
                            pass
                            # State 120028
                            if len(subjects) == 0:
                                pass
                                # 34: acsc(x*c)
                    subjects447.appendleft(tmp449)
            if len(subjects447) >= 1 and isinstance(subjects447[0], Mul):
                tmp451 = subjects447.popleft()
                associative1 = tmp451
                associative_type1 = type(tmp451)
                subjects452 = deque(tmp451._args)
                matcher = CommutativeMatcher120030.get()
                tmp453 = subjects452
                subjects452 = []
                for s in tmp453:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp453, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 120031
                        if len(subjects447) == 0:
                            pass
                            # State 120032
                            if len(subjects) == 0:
                                pass
                                # 34: acsc(x*c)
                subjects447.appendleft(tmp451)
            subjects.appendleft(tmp446)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp454 = subjects.popleft()
            subjects455 = deque(tmp454._args)
            # State 122126
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 122127
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122128
                    if len(subjects455) >= 1:
                        tmp458 = subjects455.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp458)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 122129
                            if len(subjects455) == 0:
                                pass
                                # State 122130
                                if len(subjects) == 0:
                                    pass
                                    # 35: sinh(x*b + a)
                        subjects455.appendleft(tmp458)
                if len(subjects455) >= 1 and isinstance(subjects455[0], Mul):
                    tmp460 = subjects455.popleft()
                    associative1 = tmp460
                    associative_type1 = type(tmp460)
                    subjects461 = deque(tmp460._args)
                    matcher = CommutativeMatcher122132.get()
                    tmp462 = subjects461
                    subjects461 = []
                    for s in tmp462:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp462, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122133
                            if len(subjects455) == 0:
                                pass
                                # State 122134
                                if len(subjects) == 0:
                                    pass
                                    # 35: sinh(x*b + a)
                    subjects455.appendleft(tmp460)
            if len(subjects455) >= 1 and isinstance(subjects455[0], Add):
                tmp463 = subjects455.popleft()
                associative1 = tmp463
                associative_type1 = type(tmp463)
                subjects464 = deque(tmp463._args)
                matcher = CommutativeMatcher122136.get()
                tmp465 = subjects464
                subjects464 = []
                for s in tmp465:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp465, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 122142
                        if len(subjects455) == 0:
                            pass
                            # State 122143
                            if len(subjects) == 0:
                                pass
                                # 35: sinh(x*b + a)
                subjects455.appendleft(tmp463)
            subjects.appendleft(tmp454)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp466 = subjects.popleft()
            subjects467 = deque(tmp466._args)
            # State 126354
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 126355
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 126356
                    if len(subjects467) >= 1:
                        tmp470 = subjects467.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp470)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 126357
                            if len(subjects467) == 0:
                                pass
                                # State 126358
                                if len(subjects) == 0:
                                    pass
                                    # 36: tanh(x*b + a)
                        subjects467.appendleft(tmp470)
                if len(subjects467) >= 1 and isinstance(subjects467[0], Mul):
                    tmp472 = subjects467.popleft()
                    associative1 = tmp472
                    associative_type1 = type(tmp472)
                    subjects473 = deque(tmp472._args)
                    matcher = CommutativeMatcher126360.get()
                    tmp474 = subjects473
                    subjects473 = []
                    for s in tmp474:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp474, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 126361
                            if len(subjects467) == 0:
                                pass
                                # State 126362
                                if len(subjects) == 0:
                                    pass
                                    # 36: tanh(x*b + a)
                    subjects467.appendleft(tmp472)
            if len(subjects467) >= 1 and isinstance(subjects467[0], Add):
                tmp475 = subjects467.popleft()
                associative1 = tmp475
                associative_type1 = type(tmp475)
                subjects476 = deque(tmp475._args)
                matcher = CommutativeMatcher126364.get()
                tmp477 = subjects476
                subjects476 = []
                for s in tmp477:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp477, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 126370
                        if len(subjects467) == 0:
                            pass
                            # State 126371
                            if len(subjects) == 0:
                                pass
                                # 36: tanh(x*b + a)
                subjects467.appendleft(tmp475)
            subjects.appendleft(tmp466)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp478 = subjects.popleft()
            subjects479 = deque(tmp478._args)
            # State 138485
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138486
                if len(subjects479) >= 1:
                    tmp481 = subjects479.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp481)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138487
                        if len(subjects479) == 0:
                            pass
                            # State 138488
                            if len(subjects) == 0:
                                pass
                                # 37: acosh(x*c)
                    subjects479.appendleft(tmp481)
            if len(subjects479) >= 1 and isinstance(subjects479[0], Mul):
                tmp483 = subjects479.popleft()
                associative1 = tmp483
                associative_type1 = type(tmp483)
                subjects484 = deque(tmp483._args)
                matcher = CommutativeMatcher138490.get()
                tmp485 = subjects484
                subjects484 = []
                for s in tmp485:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp485, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138491
                        if len(subjects479) == 0:
                            pass
                            # State 138492
                            if len(subjects) == 0:
                                pass
                                # 37: acosh(x*c)
                subjects479.appendleft(tmp483)
            subjects.appendleft(tmp478)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp486 = subjects.popleft()
            subjects487 = deque(tmp486._args)
            # State 138568
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138569
                if len(subjects487) >= 1:
                    tmp489 = subjects487.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp489)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138570
                        if len(subjects487) == 0:
                            pass
                            # State 138571
                            if len(subjects) == 0:
                                pass
                                # 38: asinh(x*c)
                    subjects487.appendleft(tmp489)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139610
                if len(subjects487) >= 1:
                    tmp492 = subjects487.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp492)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139611
                        if len(subjects487) == 0:
                            pass
                            # State 139612
                            if len(subjects) == 0:
                                pass
                                # 39: asinh(c*x)
                    subjects487.appendleft(tmp492)
            if len(subjects487) >= 1 and isinstance(subjects487[0], Mul):
                tmp494 = subjects487.popleft()
                associative1 = tmp494
                associative_type1 = type(tmp494)
                subjects495 = deque(tmp494._args)
                matcher = CommutativeMatcher138573.get()
                tmp496 = subjects495
                subjects495 = []
                for s in tmp496:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp496, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138574
                        if len(subjects487) == 0:
                            pass
                            # State 138575
                            if len(subjects) == 0:
                                pass
                                # 38: asinh(x*c)
                    if pattern_index == 1:
                        pass
                        # State 139613
                        if len(subjects487) == 0:
                            pass
                            # State 139614
                            if len(subjects) == 0:
                                pass
                                # 39: asinh(c*x)
                subjects487.appendleft(tmp494)
            subjects.appendleft(tmp486)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp497 = subjects.popleft()
            subjects498 = deque(tmp497._args)
            # State 143101
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 143102
                if len(subjects498) >= 1:
                    tmp500 = subjects498.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp500)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143103
                        if len(subjects498) == 0:
                            pass
                            # State 143104
                            if len(subjects) == 0:
                                pass
                                # 40: atanh(x*c)
                    subjects498.appendleft(tmp500)
            if len(subjects498) >= 1 and isinstance(subjects498[0], Mul):
                tmp502 = subjects498.popleft()
                associative1 = tmp502
                associative_type1 = type(tmp502)
                subjects503 = deque(tmp502._args)
                matcher = CommutativeMatcher143106.get()
                tmp504 = subjects503
                subjects503 = []
                for s in tmp504:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp504, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 143107
                        if len(subjects498) == 0:
                            pass
                            # State 143108
                            if len(subjects) == 0:
                                pass
                                # 40: atanh(x*c)
                subjects498.appendleft(tmp502)
            subjects.appendleft(tmp497)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp505 = subjects.popleft()
            subjects506 = deque(tmp505._args)
            # State 143150
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 143151
                if len(subjects506) >= 1:
                    tmp508 = subjects506.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp508)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143152
                        if len(subjects506) == 0:
                            pass
                            # State 143153
                            if len(subjects) == 0:
                                pass
                                # 41: acoth(x*c)
                    subjects506.appendleft(tmp508)
            if len(subjects506) >= 1 and isinstance(subjects506[0], Mul):
                tmp510 = subjects506.popleft()
                associative1 = tmp510
                associative_type1 = type(tmp510)
                subjects511 = deque(tmp510._args)
                matcher = CommutativeMatcher143155.get()
                tmp512 = subjects511
                subjects511 = []
                for s in tmp512:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp512, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 143156
                        if len(subjects506) == 0:
                            pass
                            # State 143157
                            if len(subjects) == 0:
                                pass
                                # 41: acoth(x*c)
                subjects506.appendleft(tmp510)
            subjects.appendleft(tmp505)
        if len(subjects) >= 1 and isinstance(subjects[0], asech):
            tmp513 = subjects.popleft()
            subjects514 = deque(tmp513._args)
            # State 149123
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 149124
                if len(subjects514) >= 1:
                    tmp516 = subjects514.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp516)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 149125
                        if len(subjects514) == 0:
                            pass
                            # State 149126
                            if len(subjects) == 0:
                                pass
                                # 42: asech(x*c)
                    subjects514.appendleft(tmp516)
            if len(subjects514) >= 1 and isinstance(subjects514[0], Mul):
                tmp518 = subjects514.popleft()
                associative1 = tmp518
                associative_type1 = type(tmp518)
                subjects519 = deque(tmp518._args)
                matcher = CommutativeMatcher149128.get()
                tmp520 = subjects519
                subjects519 = []
                for s in tmp520:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp520, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 149129
                        if len(subjects514) == 0:
                            pass
                            # State 149130
                            if len(subjects) == 0:
                                pass
                                # 42: asech(x*c)
                subjects514.appendleft(tmp518)
            subjects.appendleft(tmp513)
        if len(subjects) >= 1 and isinstance(subjects[0], acsch):
            tmp521 = subjects.popleft()
            subjects522 = deque(tmp521._args)
            # State 149201
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 149202
                if len(subjects522) >= 1:
                    tmp524 = subjects522.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp524)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 149203
                        if len(subjects522) == 0:
                            pass
                            # State 149204
                            if len(subjects) == 0:
                                pass
                                # 43: acsch(x*c)
                    subjects522.appendleft(tmp524)
            if len(subjects522) >= 1 and isinstance(subjects522[0], Mul):
                tmp526 = subjects522.popleft()
                associative1 = tmp526
                associative_type1 = type(tmp526)
                subjects527 = deque(tmp526._args)
                matcher = CommutativeMatcher149206.get()
                tmp528 = subjects527
                subjects527 = []
                for s in tmp528:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp528, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 149207
                        if len(subjects522) == 0:
                            pass
                            # State 149208
                            if len(subjects) == 0:
                                pass
                                # 43: acsch(x*c)
                subjects522.appendleft(tmp526)
            subjects.appendleft(tmp521)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
