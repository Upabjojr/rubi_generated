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

class CommutativeMatcher2567(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.0_1', 1, 1, None), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.0_2', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1', 1, 1, None), Mul)
]),
    5: (5, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1', 1, 1, None), Mul)
]),
    7: (7, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({3: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({4: 1, 5: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({6: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1.2.1.1', 1, 1, None), Mul)
]),
    11: (11, Multiset({7: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({8: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({9: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({10: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({11: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({12: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({13: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({14: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({14: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({15: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({16: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({17: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({18: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({19: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({20: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({19: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul)
]),
    27: (27, Multiset({20: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul)
]),
    28: (28, Multiset({21: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({22: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({14: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Mul)
]),
    31: (31, Multiset({13: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul)
]),
    32: (32, Multiset({14: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul)
]),
    33: (33, Multiset({23: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({24: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({19: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    36: (36, Multiset({25: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    37: (37, Multiset({26: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    38: (38, Multiset({20: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({27: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({28: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    41: (41, Multiset({29: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    42: (42, Multiset({30: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    43: (43, Multiset({31: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    44: (44, Multiset({32: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    45: (45, Multiset({33: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    46: (46, Multiset({34: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    47: (47, Multiset({35: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    48: (48, Multiset({36: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    49: (49, Multiset({17: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    50: (50, Multiset({37: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    51: (51, Multiset({38: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    52: (52, Multiset({39: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    53: (53, Multiset({39: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(1)), Mul)
]),
    54: (54, Multiset({40: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    55: (55, Multiset({41: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    56: (56, Multiset({1: 1, 42: 1}), [
      
]),
    57: (57, Multiset({43: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    58: (58, Multiset({44: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    59: (59, Multiset({45: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    60: (60, Multiset({46: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    61: (61, Multiset({47: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    62: (62, Multiset({48: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    63: (63, Multiset({49: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    64: (64, Multiset({1: 1, 42: 1, 50: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    65: (65, Multiset({1: 1, 42: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 1
    anonymous_patterns = {8, 9, 10, 11, 12}

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher2567._instance is None:
            CommutativeMatcher2567._instance = CommutativeMatcher2567()
        return CommutativeMatcher2567._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2566
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 6470
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 6471
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 6472
                            if len(subjects2) == 0:
                                pass
                                # State 6473
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects2.appendleft(tmp5)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 6501
                        if len(subjects2) == 0:
                            pass
                            # State 6502
                            if len(subjects) == 0:
                                pass
                                # 1: x**n
                    if len(subjects2) >= 1:
                        tmp8 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp8)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 6501
                            if len(subjects2) == 0:
                                pass
                                # State 6502
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                        subjects2.appendleft(tmp8)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 14609
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 14610
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.3.1.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 14611
                                if len(subjects2) >= 1:
                                    tmp13 = subjects2.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.3.1.1.0', tmp13)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 14612
                                        if len(subjects2) == 0:
                                            pass
                                            # State 14613
                                            if len(subjects) == 0:
                                                pass
                                                # 7: F**(g*(e + x*f))
                                    subjects2.appendleft(tmp13)
                            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                                tmp15 = subjects2.popleft()
                                associative1 = tmp15
                                associative_type1 = type(tmp15)
                                subjects16 = deque(tmp15._args)
                                matcher = CommutativeMatcher14615.get()
                                tmp17 = subjects16
                                subjects16 = []
                                for s in tmp17:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp17, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 14616
                                        if len(subjects2) == 0:
                                            pass
                                            # State 14617
                                            if len(subjects) == 0:
                                                pass
                                                # 7: F**(g*(e + x*f))
                                subjects2.appendleft(tmp15)
                        if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                            tmp18 = subjects2.popleft()
                            associative1 = tmp18
                            associative_type1 = type(tmp18)
                            subjects19 = deque(tmp18._args)
                            matcher = CommutativeMatcher14619.get()
                            tmp20 = subjects19
                            subjects19 = []
                            for s in tmp20:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp20, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 14625
                                    if len(subjects2) == 0:
                                        pass
                                        # State 14626
                                        if len(subjects) == 0:
                                            pass
                                            # 7: F**(g*(e + x*f))
                            subjects2.appendleft(tmp18)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102318
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102319
                            if len(subjects2) >= 1:
                                tmp23 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.3.1.0', tmp23)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102320
                                    if len(subjects2) == 0:
                                        pass
                                        # State 102321
                                        if len(subjects) == 0:
                                            pass
                                            # 40: F**(e + x*f)
                                subjects2.appendleft(tmp23)
                        if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                            tmp25 = subjects2.popleft()
                            associative1 = tmp25
                            associative_type1 = type(tmp25)
                            subjects26 = deque(tmp25._args)
                            matcher = CommutativeMatcher102323.get()
                            tmp27 = subjects26
                            subjects26 = []
                            for s in tmp27:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp27, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102324
                                    if len(subjects2) == 0:
                                        pass
                                        # State 102325
                                        if len(subjects) == 0:
                                            pass
                                            # 40: F**(e + x*f)
                            subjects2.appendleft(tmp25)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                        tmp28 = subjects2.popleft()
                        associative1 = tmp28
                        associative_type1 = type(tmp28)
                        subjects29 = deque(tmp28._args)
                        matcher = CommutativeMatcher14628.get()
                        tmp30 = subjects29
                        subjects29 = []
                        for s in tmp30:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp30, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 14643
                                if len(subjects2) == 0:
                                    pass
                                    # State 14644
                                    if len(subjects) == 0:
                                        pass
                                        # 7: F**(g*(e + x*f))
                        subjects2.appendleft(tmp28)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                        tmp31 = subjects2.popleft()
                        associative1 = tmp31
                        associative_type1 = type(tmp31)
                        subjects32 = deque(tmp31._args)
                        matcher = CommutativeMatcher102327.get()
                        tmp33 = subjects32
                        subjects32 = []
                        for s in tmp33:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp33, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102333
                                if len(subjects2) == 0:
                                    pass
                                    # State 102334
                                    if len(subjects) == 0:
                                        pass
                                        # 40: F**(e + x*f)
                        subjects2.appendleft(tmp31)
                subjects2.appendleft(tmp3)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 61407
                if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                    tmp35 = subjects2.popleft()
                    subjects36 = deque(tmp35._args)
                    # State 61408
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 61409
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61410
                            if len(subjects36) >= 1:
                                tmp39 = subjects36.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.2.1.0', tmp39)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 61411
                                    if len(subjects36) == 0:
                                        pass
                                        # State 61412
                                        if len(subjects2) >= 1:
                                            tmp41 = subjects2.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.2', tmp41)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 61413
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 61414
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 21: (d*sin(e + x*f))**p
                                            subjects2.appendleft(tmp41)
                                subjects36.appendleft(tmp39)
                        if len(subjects36) >= 1 and isinstance(subjects36[0], Mul):
                            tmp43 = subjects36.popleft()
                            associative1 = tmp43
                            associative_type1 = type(tmp43)
                            subjects44 = deque(tmp43._args)
                            matcher = CommutativeMatcher61416.get()
                            tmp45 = subjects44
                            subjects44 = []
                            for s in tmp45:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp45, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 61417
                                    if len(subjects36) == 0:
                                        pass
                                        # State 61418
                                        if len(subjects2) >= 1:
                                            tmp46 = subjects2.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.2', tmp46)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 61419
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 61420
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 21: (d*sin(e + x*f))**p
                                            subjects2.appendleft(tmp46)
                            subjects36.appendleft(tmp43)
                    if len(subjects36) >= 1 and isinstance(subjects36[0], Add):
                        tmp48 = subjects36.popleft()
                        associative1 = tmp48
                        associative_type1 = type(tmp48)
                        subjects49 = deque(tmp48._args)
                        matcher = CommutativeMatcher61422.get()
                        tmp50 = subjects49
                        subjects49 = []
                        for s in tmp50:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp50, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 61428
                                if len(subjects36) == 0:
                                    pass
                                    # State 61429
                                    if len(subjects2) >= 1:
                                        tmp51 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.2', tmp51)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 61430
                                            if len(subjects2) == 0:
                                                pass
                                                # State 61431
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: (d*sin(e + x*f))**p
                                        subjects2.appendleft(tmp51)
                        subjects36.appendleft(tmp48)
                    subjects2.appendleft(tmp35)
                if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                    tmp53 = subjects2.popleft()
                    subjects54 = deque(tmp53._args)
                    # State 61639
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 61640
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61641
                            if len(subjects54) >= 1:
                                tmp57 = subjects54.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.2.1.0', tmp57)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 61642
                                    if len(subjects54) == 0:
                                        pass
                                        # State 61643
                                        if len(subjects2) >= 1:
                                            tmp59 = subjects2.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.2', tmp59)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 61644
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 61645
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 22: (d*cos(e + x*f))**p
                                            subjects2.appendleft(tmp59)
                                subjects54.appendleft(tmp57)
                        if len(subjects54) >= 1 and isinstance(subjects54[0], Mul):
                            tmp61 = subjects54.popleft()
                            associative1 = tmp61
                            associative_type1 = type(tmp61)
                            subjects62 = deque(tmp61._args)
                            matcher = CommutativeMatcher61647.get()
                            tmp63 = subjects62
                            subjects62 = []
                            for s in tmp63:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp63, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 61648
                                    if len(subjects54) == 0:
                                        pass
                                        # State 61649
                                        if len(subjects2) >= 1:
                                            tmp64 = subjects2.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.2', tmp64)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 61650
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 61651
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 22: (d*cos(e + x*f))**p
                                            subjects2.appendleft(tmp64)
                            subjects54.appendleft(tmp61)
                    if len(subjects54) >= 1 and isinstance(subjects54[0], Add):
                        tmp66 = subjects54.popleft()
                        associative1 = tmp66
                        associative_type1 = type(tmp66)
                        subjects67 = deque(tmp66._args)
                        matcher = CommutativeMatcher61653.get()
                        tmp68 = subjects67
                        subjects67 = []
                        for s in tmp68:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp68, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 61659
                                if len(subjects54) == 0:
                                    pass
                                    # State 61660
                                    if len(subjects2) >= 1:
                                        tmp69 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.2', tmp69)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 61661
                                            if len(subjects2) == 0:
                                                pass
                                                # State 61662
                                                if len(subjects) == 0:
                                                    pass
                                                    # 22: (d*cos(e + x*f))**p
                                        subjects2.appendleft(tmp69)
                        subjects54.appendleft(tmp66)
                    subjects2.appendleft(tmp53)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp71 = subjects2.popleft()
                    subjects72 = deque(tmp71._args)
                    # State 76859
                    if len(subjects72) >= 1 and isinstance(subjects72[0], cos):
                        tmp73 = subjects72.popleft()
                        subjects74 = deque(tmp73._args)
                        # State 76860
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2.3.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 76861
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 76862
                                if len(subjects74) >= 1:
                                    tmp77 = subjects74.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.2.3.1.0', tmp77)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 76863
                                        if len(subjects74) == 0:
                                            pass
                                            # State 76864
                                            if len(subjects72) >= 1 and subjects72[0] == -1:
                                                tmp79 = subjects72.popleft()
                                                # State 76865
                                                if len(subjects72) == 0:
                                                    pass
                                                    # State 76866
                                                    if len(subjects2) >= 1:
                                                        tmp80 = subjects2.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.2', tmp80)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 76867
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 76868
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 29: (d/cos(e + x*f))**p
                                                        subjects2.appendleft(tmp80)
                                                subjects72.appendleft(tmp79)
                                    subjects74.appendleft(tmp77)
                            if len(subjects74) >= 1 and isinstance(subjects74[0], Mul):
                                tmp82 = subjects74.popleft()
                                associative1 = tmp82
                                associative_type1 = type(tmp82)
                                subjects83 = deque(tmp82._args)
                                matcher = CommutativeMatcher76870.get()
                                tmp84 = subjects83
                                subjects83 = []
                                for s in tmp84:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp84, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 76871
                                        if len(subjects74) == 0:
                                            pass
                                            # State 76872
                                            if len(subjects72) >= 1 and subjects72[0] == -1:
                                                tmp85 = subjects72.popleft()
                                                # State 76873
                                                if len(subjects72) == 0:
                                                    pass
                                                    # State 76874
                                                    if len(subjects2) >= 1:
                                                        tmp86 = subjects2.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i2.2.2', tmp86)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 76875
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 76876
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 29: (d/cos(e + x*f))**p
                                                        subjects2.appendleft(tmp86)
                                                subjects72.appendleft(tmp85)
                                subjects74.appendleft(tmp82)
                        if len(subjects74) >= 1 and isinstance(subjects74[0], Add):
                            tmp88 = subjects74.popleft()
                            associative1 = tmp88
                            associative_type1 = type(tmp88)
                            subjects89 = deque(tmp88._args)
                            matcher = CommutativeMatcher76878.get()
                            tmp90 = subjects89
                            subjects89 = []
                            for s in tmp90:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp90, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 76884
                                    if len(subjects74) == 0:
                                        pass
                                        # State 76885
                                        if len(subjects72) >= 1 and subjects72[0] == -1:
                                            tmp91 = subjects72.popleft()
                                            # State 76886
                                            if len(subjects72) == 0:
                                                pass
                                                # State 76887
                                                if len(subjects2) >= 1:
                                                    tmp92 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.2', tmp92)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 76888
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 76889
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 29: (d/cos(e + x*f))**p
                                                    subjects2.appendleft(tmp92)
                                            subjects72.appendleft(tmp91)
                            subjects74.appendleft(tmp88)
                        subjects72.appendleft(tmp73)
                    if len(subjects72) >= 1 and isinstance(subjects72[0], sin):
                        tmp94 = subjects72.popleft()
                        subjects95 = deque(tmp94._args)
                        # State 77139
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2.3.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 77140
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 77141
                                if len(subjects95) >= 1:
                                    tmp98 = subjects95.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.2.3.1.0', tmp98)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 77142
                                        if len(subjects95) == 0:
                                            pass
                                            # State 77143
                                            if len(subjects72) >= 1 and subjects72[0] == -1:
                                                tmp100 = subjects72.popleft()
                                                # State 77144
                                                if len(subjects72) == 0:
                                                    pass
                                                    # State 77145
                                                    if len(subjects2) >= 1:
                                                        tmp101 = subjects2.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.2', tmp101)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 77146
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 77147
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 31: (d/sin(e + x*f))**p
                                                        subjects2.appendleft(tmp101)
                                                subjects72.appendleft(tmp100)
                                    subjects95.appendleft(tmp98)
                            if len(subjects95) >= 1 and isinstance(subjects95[0], Mul):
                                tmp103 = subjects95.popleft()
                                associative1 = tmp103
                                associative_type1 = type(tmp103)
                                subjects104 = deque(tmp103._args)
                                matcher = CommutativeMatcher77149.get()
                                tmp105 = subjects104
                                subjects104 = []
                                for s in tmp105:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp105, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 77150
                                        if len(subjects95) == 0:
                                            pass
                                            # State 77151
                                            if len(subjects72) >= 1 and subjects72[0] == -1:
                                                tmp106 = subjects72.popleft()
                                                # State 77152
                                                if len(subjects72) == 0:
                                                    pass
                                                    # State 77153
                                                    if len(subjects2) >= 1:
                                                        tmp107 = subjects2.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i2.2.2', tmp107)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 77154
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 77155
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 31: (d/sin(e + x*f))**p
                                                        subjects2.appendleft(tmp107)
                                                subjects72.appendleft(tmp106)
                                subjects95.appendleft(tmp103)
                        if len(subjects95) >= 1 and isinstance(subjects95[0], Add):
                            tmp109 = subjects95.popleft()
                            associative1 = tmp109
                            associative_type1 = type(tmp109)
                            subjects110 = deque(tmp109._args)
                            matcher = CommutativeMatcher77157.get()
                            tmp111 = subjects110
                            subjects110 = []
                            for s in tmp111:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp111, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 77163
                                    if len(subjects95) == 0:
                                        pass
                                        # State 77164
                                        if len(subjects72) >= 1 and subjects72[0] == -1:
                                            tmp112 = subjects72.popleft()
                                            # State 77165
                                            if len(subjects72) == 0:
                                                pass
                                                # State 77166
                                                if len(subjects2) >= 1:
                                                    tmp113 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.2', tmp113)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 77167
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 77168
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 31: (d/sin(e + x*f))**p
                                                    subjects2.appendleft(tmp113)
                                            subjects72.appendleft(tmp112)
                            subjects95.appendleft(tmp109)
                        subjects72.appendleft(tmp94)
                    if len(subjects72) >= 1 and isinstance(subjects72[0], tan):
                        tmp115 = subjects72.popleft()
                        subjects116 = deque(tmp115._args)
                        # State 80228
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2.3.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 80229
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80230
                                if len(subjects116) >= 1:
                                    tmp119 = subjects116.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.2.3.1.0', tmp119)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 80231
                                        if len(subjects116) == 0:
                                            pass
                                            # State 80232
                                            if len(subjects72) >= 1 and subjects72[0] == -1:
                                                tmp121 = subjects72.popleft()
                                                # State 80233
                                                if len(subjects72) == 0:
                                                    pass
                                                    # State 80234
                                                    if len(subjects2) >= 1:
                                                        tmp122 = subjects2.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.2', tmp122)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 80235
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 80236
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 34: (d/tan(e + x*f))**p
                                                        subjects2.appendleft(tmp122)
                                                subjects72.appendleft(tmp121)
                                    subjects116.appendleft(tmp119)
                            if len(subjects116) >= 1 and isinstance(subjects116[0], Mul):
                                tmp124 = subjects116.popleft()
                                associative1 = tmp124
                                associative_type1 = type(tmp124)
                                subjects125 = deque(tmp124._args)
                                matcher = CommutativeMatcher80238.get()
                                tmp126 = subjects125
                                subjects125 = []
                                for s in tmp126:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp126, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 80239
                                        if len(subjects116) == 0:
                                            pass
                                            # State 80240
                                            if len(subjects72) >= 1 and subjects72[0] == -1:
                                                tmp127 = subjects72.popleft()
                                                # State 80241
                                                if len(subjects72) == 0:
                                                    pass
                                                    # State 80242
                                                    if len(subjects2) >= 1:
                                                        tmp128 = subjects2.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i2.2.2', tmp128)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 80243
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 80244
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 34: (d/tan(e + x*f))**p
                                                        subjects2.appendleft(tmp128)
                                                subjects72.appendleft(tmp127)
                                subjects116.appendleft(tmp124)
                        if len(subjects116) >= 1 and isinstance(subjects116[0], Add):
                            tmp130 = subjects116.popleft()
                            associative1 = tmp130
                            associative_type1 = type(tmp130)
                            subjects131 = deque(tmp130._args)
                            matcher = CommutativeMatcher80246.get()
                            tmp132 = subjects131
                            subjects131 = []
                            for s in tmp132:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp132, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 80252
                                    if len(subjects116) == 0:
                                        pass
                                        # State 80253
                                        if len(subjects72) >= 1 and subjects72[0] == -1:
                                            tmp133 = subjects72.popleft()
                                            # State 80254
                                            if len(subjects72) == 0:
                                                pass
                                                # State 80255
                                                if len(subjects2) >= 1:
                                                    tmp134 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.2', tmp134)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 80256
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 80257
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 34: (d/tan(e + x*f))**p
                                                    subjects2.appendleft(tmp134)
                                            subjects72.appendleft(tmp133)
                            subjects116.appendleft(tmp130)
                        subjects72.appendleft(tmp115)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 150783
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 150784
                            if len(subjects72) >= 1:
                                tmp138 = subjects72.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.2.1.0', tmp138)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150785
                                    if len(subjects72) >= 1:
                                        tmp140 = subjects72.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.2.2', tmp140)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 150786
                                            if len(subjects72) == 0:
                                                pass
                                                # State 150787
                                                if len(subjects2) >= 1:
                                                    tmp142 = subjects2.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.2', tmp142)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 150788
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 150789
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 49: (d*(a + x*b)**n)**p
                                                    subjects2.appendleft(tmp142)
                                        subjects72.appendleft(tmp140)
                                subjects72.appendleft(tmp138)
                        if len(subjects72) >= 1 and isinstance(subjects72[0], Mul):
                            tmp144 = subjects72.popleft()
                            associative1 = tmp144
                            associative_type1 = type(tmp144)
                            subjects145 = deque(tmp144._args)
                            matcher = CommutativeMatcher150791.get()
                            tmp146 = subjects145
                            subjects145 = []
                            for s in tmp146:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp146, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 150792
                                    if len(subjects72) >= 1:
                                        tmp147 = []
                                        tmp147.append(subjects72.popleft())
                                        while True:
                                            if len(tmp147) > 1:
                                                tmp148 = create_operation_expression(associative1, tmp147)
                                            elif len(tmp147) == 1:
                                                tmp148 = tmp147[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.2.2', tmp148)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 150793
                                                if len(subjects72) == 0:
                                                    pass
                                                    # State 150794
                                                    if len(subjects2) >= 1:
                                                        tmp150 = subjects2.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.2', tmp150)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 150795
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 150796
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 49: (d*(a + x*b)**n)**p
                                                        subjects2.appendleft(tmp150)
                                            if len(subjects72) == 0:
                                                break
                                            tmp147.append(subjects72.popleft())
                                        subjects72.extendleft(reversed(tmp147))
                            subjects72.appendleft(tmp144)
                    if len(subjects72) >= 1 and isinstance(subjects72[0], Add):
                        tmp152 = subjects72.popleft()
                        associative1 = tmp152
                        associative_type1 = type(tmp152)
                        subjects153 = deque(tmp152._args)
                        matcher = CommutativeMatcher150798.get()
                        tmp154 = subjects153
                        subjects153 = []
                        for s in tmp154:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp154, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 150804
                                if len(subjects72) >= 1:
                                    tmp155 = []
                                    tmp155.append(subjects72.popleft())
                                    while True:
                                        if len(tmp155) > 1:
                                            tmp156 = create_operation_expression(associative1, tmp155)
                                        elif len(tmp155) == 1:
                                            tmp156 = tmp155[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.2.2', tmp156)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 150805
                                            if len(subjects72) == 0:
                                                pass
                                                # State 150806
                                                if len(subjects2) >= 1:
                                                    tmp158 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.2', tmp158)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 150807
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 150808
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 49: (d*(a + x*b)**n)**p
                                                    subjects2.appendleft(tmp158)
                                        if len(subjects72) == 0:
                                            break
                                        tmp155.append(subjects72.popleft())
                                    subjects72.extendleft(reversed(tmp155))
                        subjects72.appendleft(tmp152)
                    subjects2.appendleft(tmp71)
                if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                    tmp160 = subjects2.popleft()
                    subjects161 = deque(tmp160._args)
                    # State 79992
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 79993
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 79994
                            if len(subjects161) >= 1:
                                tmp164 = subjects161.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.2.1.0', tmp164)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 79995
                                    if len(subjects161) == 0:
                                        pass
                                        # State 79996
                                        if len(subjects2) >= 1:
                                            tmp166 = subjects2.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.2', tmp166)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 79997
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 79998
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 33: (d*tan(e + x*f))**p
                                            subjects2.appendleft(tmp166)
                                subjects161.appendleft(tmp164)
                        if len(subjects161) >= 1 and isinstance(subjects161[0], Mul):
                            tmp168 = subjects161.popleft()
                            associative1 = tmp168
                            associative_type1 = type(tmp168)
                            subjects169 = deque(tmp168._args)
                            matcher = CommutativeMatcher80000.get()
                            tmp170 = subjects169
                            subjects169 = []
                            for s in tmp170:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp170, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 80001
                                    if len(subjects161) == 0:
                                        pass
                                        # State 80002
                                        if len(subjects2) >= 1:
                                            tmp171 = subjects2.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.2', tmp171)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 80003
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 80004
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 33: (d*tan(e + x*f))**p
                                            subjects2.appendleft(tmp171)
                            subjects161.appendleft(tmp168)
                    if len(subjects161) >= 1 and isinstance(subjects161[0], Add):
                        tmp173 = subjects161.popleft()
                        associative1 = tmp173
                        associative_type1 = type(tmp173)
                        subjects174 = deque(tmp173._args)
                        matcher = CommutativeMatcher80006.get()
                        tmp175 = subjects174
                        subjects174 = []
                        for s in tmp175:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp175, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80012
                                if len(subjects161) == 0:
                                    pass
                                    # State 80013
                                    if len(subjects2) >= 1:
                                        tmp176 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.2', tmp176)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 80014
                                            if len(subjects2) == 0:
                                                pass
                                                # State 80015
                                                if len(subjects) == 0:
                                                    pass
                                                    # 33: (d*tan(e + x*f))**p
                                        subjects2.appendleft(tmp176)
                        subjects161.appendleft(tmp173)
                    subjects2.appendleft(tmp160)
            if len(subjects2) >= 1:
                tmp178 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1_1', tmp178)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103407
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 103408
                        if len(subjects2) == 0:
                            pass
                            # State 103409
                            if len(subjects) == 0:
                                pass
                                # 42: w**n
                    if len(subjects2) >= 1:
                        tmp181 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2_1', tmp181)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 103408
                            if len(subjects2) == 0:
                                pass
                                # State 103409
                                if len(subjects) == 0:
                                    pass
                                    # 42: w**n
                        subjects2.appendleft(tmp181)
                subjects2.appendleft(tmp178)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 150551
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 150552
                    if len(subjects2) >= 1:
                        tmp185 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp185)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 150553
                            if len(subjects2) >= 1:
                                tmp187 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2', tmp187)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150554
                                    if len(subjects2) == 0:
                                        pass
                                        # State 150555
                                        if len(subjects) == 0:
                                            pass
                                            # 47: (a + x*b)**n
                                subjects2.appendleft(tmp187)
                        subjects2.appendleft(tmp185)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp189 = subjects2.popleft()
                    associative1 = tmp189
                    associative_type1 = type(tmp189)
                    subjects190 = deque(tmp189._args)
                    matcher = CommutativeMatcher150557.get()
                    tmp191 = subjects190
                    subjects190 = []
                    for s in tmp191:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp191, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 150558
                            if len(subjects2) >= 1:
                                tmp192 = []
                                tmp192.append(subjects2.popleft())
                                while True:
                                    if len(tmp192) > 1:
                                        tmp193 = create_operation_expression(associative1, tmp192)
                                    elif len(tmp192) == 1:
                                        tmp193 = tmp192[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.2', tmp193)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 150559
                                        if len(subjects2) == 0:
                                            pass
                                            # State 150560
                                            if len(subjects) == 0:
                                                pass
                                                # 47: (a + x*b)**n
                                    if len(subjects2) == 0:
                                        break
                                    tmp192.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp192))
                    subjects2.appendleft(tmp189)
            if len(subjects2) >= 1:
                tmp195 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1_2', tmp195)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151908
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2_2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151909
                        if len(subjects2) == 0:
                            pass
                            # State 151910
                            if len(subjects) == 0:
                                pass
                                # 50: z**q
                    if len(subjects2) >= 1:
                        tmp198 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2_2', tmp198)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151909
                            if len(subjects2) == 0:
                                pass
                                # State 151910
                                if len(subjects) == 0:
                                    pass
                                    # 50: z**q
                        subjects2.appendleft(tmp198)
                subjects2.appendleft(tmp195)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp200 = subjects2.popleft()
                associative1 = tmp200
                associative_type1 = type(tmp200)
                subjects201 = deque(tmp200._args)
                matcher = CommutativeMatcher10332.get()
                tmp202 = subjects201
                subjects201 = []
                for s in tmp202:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp202, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10349
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10350
                            if len(subjects2) == 0:
                                pass
                                # State 10351
                                if len(subjects) == 0:
                                    pass
                                    # 2: (a + b*x**n)**r
                        if len(subjects2) >= 1:
                            tmp204 = []
                            tmp204.append(subjects2.popleft())
                            while True:
                                if len(tmp204) > 1:
                                    tmp205 = create_operation_expression(associative1, tmp204)
                                elif len(tmp204) == 1:
                                    tmp205 = tmp204[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp205)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10350
                                    if len(subjects2) == 0:
                                        pass
                                        # State 10351
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (a + b*x**n)**r
                                if len(subjects2) == 0:
                                    break
                                tmp204.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp204))
                        if len(subjects2) >= 1 and subjects2[0] == -1:
                            tmp207 = subjects2.popleft()
                            # State 10465
                            if len(subjects2) == 0:
                                pass
                                # State 10466
                                if len(subjects) == 0:
                                    pass
                                    # 4: 1/(a + b*x**n)
                            subjects2.appendleft(tmp207)
                    if pattern_index == 1:
                        pass
                        # State 10387
                        if len(subjects2) >= 1:
                            tmp208 = []
                            tmp208.append(subjects2.popleft())
                            while True:
                                if len(tmp208) > 1:
                                    tmp209 = create_operation_expression(associative1, tmp208)
                                elif len(tmp208) == 1:
                                    tmp209 = tmp208[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2_1', tmp209)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10388
                                    if len(subjects2) == 0:
                                        pass
                                        # State 10389
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (c + d*x**n)**s
                                if len(subjects2) == 0:
                                    break
                                tmp208.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp208))
                    if pattern_index == 2:
                        pass
                        # State 150563
                        if len(subjects2) >= 1:
                            tmp211 = []
                            tmp211.append(subjects2.popleft())
                            while True:
                                if len(tmp211) > 1:
                                    tmp212 = create_operation_expression(associative1, tmp211)
                                elif len(tmp211) == 1:
                                    tmp212 = tmp211[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp212)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150564
                                    if len(subjects2) == 0:
                                        pass
                                        # State 150565
                                        if len(subjects) == 0:
                                            pass
                                            # 47: (a + x*b)**n
                                if len(subjects2) == 0:
                                    break
                                tmp211.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp211))
                subjects2.appendleft(tmp200)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp214 = subjects2.popleft()
                subjects215 = deque(tmp214._args)
                # State 57426
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57427
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 57428
                        if len(subjects215) >= 1:
                            tmp218 = subjects215.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp218)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 57429
                                if len(subjects215) == 0:
                                    pass
                                    # State 57430
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp220 = subjects2.popleft()
                                        # State 57431
                                        if len(subjects2) == 0:
                                            pass
                                            # State 57432
                                            if len(subjects) == 0:
                                                pass
                                                # 15: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp220)
                                    if len(subjects2) >= 1:
                                        tmp221 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.3', tmp221)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 66160
                                            if len(subjects2) == 0:
                                                pass
                                                # State 66161
                                                if len(subjects) == 0:
                                                    pass
                                                    # 24: cos(e + x*f)**p
                                        subjects2.appendleft(tmp221)
                            subjects215.appendleft(tmp218)
                    if len(subjects215) >= 1 and isinstance(subjects215[0], Mul):
                        tmp223 = subjects215.popleft()
                        associative1 = tmp223
                        associative_type1 = type(tmp223)
                        subjects224 = deque(tmp223._args)
                        matcher = CommutativeMatcher57434.get()
                        tmp225 = subjects224
                        subjects224 = []
                        for s in tmp225:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp225, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 57435
                                if len(subjects215) == 0:
                                    pass
                                    # State 57436
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp226 = subjects2.popleft()
                                        # State 57437
                                        if len(subjects2) == 0:
                                            pass
                                            # State 57438
                                            if len(subjects) == 0:
                                                pass
                                                # 15: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp226)
                                    if len(subjects2) >= 1:
                                        tmp227 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.3', tmp227)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 66162
                                            if len(subjects2) == 0:
                                                pass
                                                # State 66163
                                                if len(subjects) == 0:
                                                    pass
                                                    # 24: cos(e + x*f)**p
                                        subjects2.appendleft(tmp227)
                        subjects215.appendleft(tmp223)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 89755
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89756
                        if len(subjects215) >= 1:
                            tmp231 = subjects215.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.0', tmp231)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 89757
                                if len(subjects215) == 0:
                                    pass
                                    # State 89758
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp233 = subjects2.popleft()
                                        # State 89759
                                        if len(subjects2) == 0:
                                            pass
                                            # State 89760
                                            if len(subjects) == 0:
                                                pass
                                                # 38: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp233)
                            subjects215.appendleft(tmp231)
                    if len(subjects215) >= 1 and isinstance(subjects215[0], Mul):
                        tmp234 = subjects215.popleft()
                        associative1 = tmp234
                        associative_type1 = type(tmp234)
                        subjects235 = deque(tmp234._args)
                        matcher = CommutativeMatcher89762.get()
                        tmp236 = subjects235
                        subjects235 = []
                        for s in tmp236:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp236, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 89763
                                if len(subjects215) == 0:
                                    pass
                                    # State 89764
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp237 = subjects2.popleft()
                                        # State 89765
                                        if len(subjects2) == 0:
                                            pass
                                            # State 89766
                                            if len(subjects) == 0:
                                                pass
                                                # 38: 1/cos(e + x*f)
                                        subjects2.appendleft(tmp237)
                        subjects215.appendleft(tmp234)
                if len(subjects215) >= 1 and isinstance(subjects215[0], Add):
                    tmp238 = subjects215.popleft()
                    associative1 = tmp238
                    associative_type1 = type(tmp238)
                    subjects239 = deque(tmp238._args)
                    matcher = CommutativeMatcher57440.get()
                    tmp240 = subjects239
                    subjects239 = []
                    for s in tmp240:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp240, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57446
                            if len(subjects215) == 0:
                                pass
                                # State 57447
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp241 = subjects2.popleft()
                                    # State 57448
                                    if len(subjects2) == 0:
                                        pass
                                        # State 57449
                                        if len(subjects) == 0:
                                            pass
                                            # 15: 1/cos(e + x*f)
                                    subjects2.appendleft(tmp241)
                                if len(subjects2) >= 1:
                                    tmp242 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.3', tmp242)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 66164
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66165
                                            if len(subjects) == 0:
                                                pass
                                                # 24: cos(e + x*f)**p
                                    subjects2.appendleft(tmp242)
                        if pattern_index == 1:
                            pass
                            # State 89770
                            if len(subjects215) == 0:
                                pass
                                # State 89771
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp244 = subjects2.popleft()
                                    # State 89772
                                    if len(subjects2) == 0:
                                        pass
                                        # State 89773
                                        if len(subjects) == 0:
                                            pass
                                            # 38: 1/cos(e + x*f)
                                    subjects2.appendleft(tmp244)
                    subjects215.appendleft(tmp238)
                subjects2.appendleft(tmp214)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp245 = subjects2.popleft()
                subjects246 = deque(tmp245._args)
                # State 57597
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57598
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 57599
                        if len(subjects246) >= 1:
                            tmp249 = subjects246.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp249)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 57600
                                if len(subjects246) == 0:
                                    pass
                                    # State 57601
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp251 = subjects2.popleft()
                                        # State 57602
                                        if len(subjects2) == 0:
                                            pass
                                            # State 57603
                                            if len(subjects) == 0:
                                                pass
                                                # 17: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp251)
                                    if len(subjects2) >= 1:
                                        tmp252 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.3', tmp252)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 66069
                                            if len(subjects2) == 0:
                                                pass
                                                # State 66070
                                                if len(subjects) == 0:
                                                    pass
                                                    # 23: sin(e + x*f)**p
                                        subjects2.appendleft(tmp252)
                            subjects246.appendleft(tmp249)
                    if len(subjects246) >= 1 and isinstance(subjects246[0], Mul):
                        tmp254 = subjects246.popleft()
                        associative1 = tmp254
                        associative_type1 = type(tmp254)
                        subjects255 = deque(tmp254._args)
                        matcher = CommutativeMatcher57605.get()
                        tmp256 = subjects255
                        subjects255 = []
                        for s in tmp256:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp256, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 57606
                                if len(subjects246) == 0:
                                    pass
                                    # State 57607
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp257 = subjects2.popleft()
                                        # State 57608
                                        if len(subjects2) == 0:
                                            pass
                                            # State 57609
                                            if len(subjects) == 0:
                                                pass
                                                # 17: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp257)
                                    if len(subjects2) >= 1:
                                        tmp258 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.3', tmp258)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 66071
                                            if len(subjects2) == 0:
                                                pass
                                                # State 66072
                                                if len(subjects) == 0:
                                                    pass
                                                    # 23: sin(e + x*f)**p
                                        subjects2.appendleft(tmp258)
                        subjects246.appendleft(tmp254)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 89705
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89706
                        if len(subjects246) >= 1:
                            tmp262 = subjects246.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.0', tmp262)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 89707
                                if len(subjects246) == 0:
                                    pass
                                    # State 89708
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp264 = subjects2.popleft()
                                        # State 89709
                                        if len(subjects2) == 0:
                                            pass
                                            # State 89710
                                            if len(subjects) == 0:
                                                pass
                                                # 37: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp264)
                            subjects246.appendleft(tmp262)
                    if len(subjects246) >= 1 and isinstance(subjects246[0], Mul):
                        tmp265 = subjects246.popleft()
                        associative1 = tmp265
                        associative_type1 = type(tmp265)
                        subjects266 = deque(tmp265._args)
                        matcher = CommutativeMatcher89712.get()
                        tmp267 = subjects266
                        subjects266 = []
                        for s in tmp267:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp267, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 89713
                                if len(subjects246) == 0:
                                    pass
                                    # State 89714
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp268 = subjects2.popleft()
                                        # State 89715
                                        if len(subjects2) == 0:
                                            pass
                                            # State 89716
                                            if len(subjects) == 0:
                                                pass
                                                # 37: 1/sin(e + x*f)
                                        subjects2.appendleft(tmp268)
                        subjects246.appendleft(tmp265)
                if len(subjects246) >= 1 and isinstance(subjects246[0], Add):
                    tmp269 = subjects246.popleft()
                    associative1 = tmp269
                    associative_type1 = type(tmp269)
                    subjects270 = deque(tmp269._args)
                    matcher = CommutativeMatcher57611.get()
                    tmp271 = subjects270
                    subjects270 = []
                    for s in tmp271:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp271, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57617
                            if len(subjects246) == 0:
                                pass
                                # State 57618
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp272 = subjects2.popleft()
                                    # State 57619
                                    if len(subjects2) == 0:
                                        pass
                                        # State 57620
                                        if len(subjects) == 0:
                                            pass
                                            # 17: 1/sin(e + x*f)
                                    subjects2.appendleft(tmp272)
                                if len(subjects2) >= 1:
                                    tmp273 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.3', tmp273)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 66073
                                        if len(subjects2) == 0:
                                            pass
                                            # State 66074
                                            if len(subjects) == 0:
                                                pass
                                                # 23: sin(e + x*f)**p
                                    subjects2.appendleft(tmp273)
                        if pattern_index == 1:
                            pass
                            # State 89720
                            if len(subjects246) == 0:
                                pass
                                # State 89721
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp275 = subjects2.popleft()
                                    # State 89722
                                    if len(subjects2) == 0:
                                        pass
                                        # State 89723
                                        if len(subjects) == 0:
                                            pass
                                            # 37: 1/sin(e + x*f)
                                    subjects2.appendleft(tmp275)
                    subjects246.appendleft(tmp269)
                subjects2.appendleft(tmp245)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp276 = subjects2.popleft()
                subjects277 = deque(tmp276._args)
                # State 59305
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59306
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 59307
                        if len(subjects277) >= 1:
                            tmp280 = subjects277.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp280)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 59308
                                if len(subjects277) == 0:
                                    pass
                                    # State 59309
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp282 = subjects2.popleft()
                                        # State 59310
                                        if len(subjects2) == 0:
                                            pass
                                            # State 59311
                                            if len(subjects) == 0:
                                                pass
                                                # 20: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp282)
                                    if len(subjects2) >= 1:
                                        tmp283 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.3', tmp283)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 80653
                                            if len(subjects2) == 0:
                                                pass
                                                # State 80654
                                                if len(subjects) == 0:
                                                    pass
                                                    # 35: tan(e + x*f)**q
                                        subjects2.appendleft(tmp283)
                            subjects277.appendleft(tmp280)
                    if len(subjects277) >= 1 and isinstance(subjects277[0], Mul):
                        tmp285 = subjects277.popleft()
                        associative1 = tmp285
                        associative_type1 = type(tmp285)
                        subjects286 = deque(tmp285._args)
                        matcher = CommutativeMatcher59313.get()
                        tmp287 = subjects286
                        subjects286 = []
                        for s in tmp287:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp287, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 59314
                                if len(subjects277) == 0:
                                    pass
                                    # State 59315
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp288 = subjects2.popleft()
                                        # State 59316
                                        if len(subjects2) == 0:
                                            pass
                                            # State 59317
                                            if len(subjects) == 0:
                                                pass
                                                # 20: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp288)
                                    if len(subjects2) >= 1:
                                        tmp289 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.3', tmp289)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 80655
                                            if len(subjects2) == 0:
                                                pass
                                                # State 80656
                                                if len(subjects) == 0:
                                                    pass
                                                    # 35: tan(e + x*f)**q
                                        subjects2.appendleft(tmp289)
                        subjects277.appendleft(tmp285)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76501
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 76502
                        if len(subjects277) >= 1:
                            tmp293 = subjects277.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.0', tmp293)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 76503
                                if len(subjects277) == 0:
                                    pass
                                    # State 76504
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp295 = subjects2.popleft()
                                        # State 76505
                                        if len(subjects2) == 0:
                                            pass
                                            # State 76506
                                            if len(subjects) == 0:
                                                pass
                                                # 28: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp295)
                            subjects277.appendleft(tmp293)
                    if len(subjects277) >= 1 and isinstance(subjects277[0], Mul):
                        tmp296 = subjects277.popleft()
                        associative1 = tmp296
                        associative_type1 = type(tmp296)
                        subjects297 = deque(tmp296._args)
                        matcher = CommutativeMatcher76508.get()
                        tmp298 = subjects297
                        subjects297 = []
                        for s in tmp298:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp298, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 76509
                                if len(subjects277) == 0:
                                    pass
                                    # State 76510
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp299 = subjects2.popleft()
                                        # State 76511
                                        if len(subjects2) == 0:
                                            pass
                                            # State 76512
                                            if len(subjects) == 0:
                                                pass
                                                # 28: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp299)
                        subjects277.appendleft(tmp296)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 77224
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 77225
                        if len(subjects277) >= 1:
                            tmp302 = subjects277.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp302)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 77226
                                if len(subjects277) == 0:
                                    pass
                                    # State 77227
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp304 = subjects2.popleft()
                                        # State 77228
                                        if len(subjects2) == 0:
                                            pass
                                            # State 77229
                                            if len(subjects) == 0:
                                                pass
                                                # 32: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp304)
                            subjects277.appendleft(tmp302)
                    if len(subjects277) >= 1 and isinstance(subjects277[0], Mul):
                        tmp305 = subjects277.popleft()
                        associative1 = tmp305
                        associative_type1 = type(tmp305)
                        subjects306 = deque(tmp305._args)
                        matcher = CommutativeMatcher77231.get()
                        tmp307 = subjects306
                        subjects306 = []
                        for s in tmp307:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp307, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 77232
                                if len(subjects277) == 0:
                                    pass
                                    # State 77233
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp308 = subjects2.popleft()
                                        # State 77234
                                        if len(subjects2) == 0:
                                            pass
                                            # State 77235
                                            if len(subjects) == 0:
                                                pass
                                                # 32: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp308)
                        subjects277.appendleft(tmp305)
                if len(subjects277) >= 1 and isinstance(subjects277[0], Add):
                    tmp309 = subjects277.popleft()
                    associative1 = tmp309
                    associative_type1 = type(tmp309)
                    subjects310 = deque(tmp309._args)
                    matcher = CommutativeMatcher59319.get()
                    tmp311 = subjects310
                    subjects310 = []
                    for s in tmp311:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp311, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 59325
                            if len(subjects277) == 0:
                                pass
                                # State 59326
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp312 = subjects2.popleft()
                                    # State 59327
                                    if len(subjects2) == 0:
                                        pass
                                        # State 59328
                                        if len(subjects) == 0:
                                            pass
                                            # 20: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp312)
                                if len(subjects2) >= 1:
                                    tmp313 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.3', tmp313)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 80657
                                        if len(subjects2) == 0:
                                            pass
                                            # State 80658
                                            if len(subjects) == 0:
                                                pass
                                                # 35: tan(e + x*f)**q
                                    subjects2.appendleft(tmp313)
                        if pattern_index == 1:
                            pass
                            # State 76516
                            if len(subjects277) == 0:
                                pass
                                # State 76517
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp315 = subjects2.popleft()
                                    # State 76518
                                    if len(subjects2) == 0:
                                        pass
                                        # State 76519
                                        if len(subjects) == 0:
                                            pass
                                            # 28: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp315)
                        if pattern_index == 2:
                            pass
                            # State 77239
                            if len(subjects277) == 0:
                                pass
                                # State 77240
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp316 = subjects2.popleft()
                                    # State 77241
                                    if len(subjects2) == 0:
                                        pass
                                        # State 77242
                                        if len(subjects) == 0:
                                            pass
                                            # 32: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp316)
                    subjects277.appendleft(tmp309)
                subjects2.appendleft(tmp276)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp317 = subjects2.popleft()
                associative1 = tmp317
                associative_type1 = type(tmp317)
                subjects318 = deque(tmp317._args)
                matcher = CommutativeMatcher61433.get()
                tmp319 = subjects318
                subjects318 = []
                for s in tmp319:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp319, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 61452
                        if len(subjects2) >= 1:
                            tmp320 = []
                            tmp320.append(subjects2.popleft())
                            while True:
                                if len(tmp320) > 1:
                                    tmp321 = create_operation_expression(associative1, tmp320)
                                elif len(tmp320) == 1:
                                    tmp321 = tmp320[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp321)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 61453
                                    if len(subjects2) == 0:
                                        pass
                                        # State 61454
                                        if len(subjects) == 0:
                                            pass
                                            # 21: (d*sin(e + x*f))**p
                                if len(subjects2) == 0:
                                    break
                                tmp320.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp320))
                    if pattern_index == 1:
                        pass
                        # State 61681
                        if len(subjects2) >= 1:
                            tmp323 = []
                            tmp323.append(subjects2.popleft())
                            while True:
                                if len(tmp323) > 1:
                                    tmp324 = create_operation_expression(associative1, tmp323)
                                elif len(tmp323) == 1:
                                    tmp324 = tmp323[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp324)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 61682
                                    if len(subjects2) == 0:
                                        pass
                                        # State 61683
                                        if len(subjects) == 0:
                                            pass
                                            # 22: (d*cos(e + x*f))**p
                                if len(subjects2) == 0:
                                    break
                                tmp323.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp323))
                    if pattern_index == 2:
                        pass
                        # State 76915
                        if len(subjects2) >= 1:
                            tmp326 = []
                            tmp326.append(subjects2.popleft())
                            while True:
                                if len(tmp326) > 1:
                                    tmp327 = create_operation_expression(associative1, tmp326)
                                elif len(tmp326) == 1:
                                    tmp327 = tmp326[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp327)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 76916
                                    if len(subjects2) == 0:
                                        pass
                                        # State 76917
                                        if len(subjects) == 0:
                                            pass
                                            # 29: (d/cos(e + x*f))**p
                                if len(subjects2) == 0:
                                    break
                                tmp326.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp326))
                    if pattern_index == 3:
                        pass
                        # State 77193
                        if len(subjects2) >= 1:
                            tmp329 = []
                            tmp329.append(subjects2.popleft())
                            while True:
                                if len(tmp329) > 1:
                                    tmp330 = create_operation_expression(associative1, tmp329)
                                elif len(tmp329) == 1:
                                    tmp330 = tmp329[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp330)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 77194
                                    if len(subjects2) == 0:
                                        pass
                                        # State 77195
                                        if len(subjects) == 0:
                                            pass
                                            # 31: (d/sin(e + x*f))**p
                                if len(subjects2) == 0:
                                    break
                                tmp329.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp329))
                    if pattern_index == 4:
                        pass
                        # State 80034
                        if len(subjects2) >= 1:
                            tmp332 = []
                            tmp332.append(subjects2.popleft())
                            while True:
                                if len(tmp332) > 1:
                                    tmp333 = create_operation_expression(associative1, tmp332)
                                elif len(tmp332) == 1:
                                    tmp333 = tmp332[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp333)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 80035
                                    if len(subjects2) == 0:
                                        pass
                                        # State 80036
                                        if len(subjects) == 0:
                                            pass
                                            # 33: (d*tan(e + x*f))**p
                                if len(subjects2) == 0:
                                    break
                                tmp332.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp332))
                    if pattern_index == 5:
                        pass
                        # State 80282
                        if len(subjects2) >= 1:
                            tmp335 = []
                            tmp335.append(subjects2.popleft())
                            while True:
                                if len(tmp335) > 1:
                                    tmp336 = create_operation_expression(associative1, tmp335)
                                elif len(tmp335) == 1:
                                    tmp336 = tmp335[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp336)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 80283
                                    if len(subjects2) == 0:
                                        pass
                                        # State 80284
                                        if len(subjects) == 0:
                                            pass
                                            # 34: (d/tan(e + x*f))**p
                                if len(subjects2) == 0:
                                    break
                                tmp335.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp335))
                    if pattern_index == 6:
                        pass
                        # State 102504
                        if len(subjects2) >= 1:
                            tmp338 = []
                            tmp338.append(subjects2.popleft())
                            while True:
                                if len(tmp338) > 1:
                                    tmp339 = create_operation_expression(associative1, tmp338)
                                elif len(tmp338) == 1:
                                    tmp339 = tmp338[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp339)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102505
                                    if len(subjects2) == 0:
                                        pass
                                        # State 102506
                                        if len(subjects) == 0:
                                            pass
                                            # 41: (F*b*(c + x*d))**p
                                if len(subjects2) == 0:
                                    break
                                tmp338.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp338))
                    if pattern_index == 7:
                        pass
                        # State 150592
                        if len(subjects2) >= 1:
                            tmp341 = []
                            tmp341.append(subjects2.popleft())
                            while True:
                                if len(tmp341) > 1:
                                    tmp342 = create_operation_expression(associative1, tmp341)
                                elif len(tmp341) == 1:
                                    tmp342 = tmp341[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp342)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150593
                                    if len(subjects2) == 0:
                                        pass
                                        # State 150594
                                        if len(subjects) == 0:
                                            pass
                                            # 48: (d*(a + x*b))**p
                                if len(subjects2) == 0:
                                    break
                                tmp341.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp341))
                    if pattern_index == 8:
                        pass
                        # State 150829
                        if len(subjects2) >= 1:
                            tmp344 = []
                            tmp344.append(subjects2.popleft())
                            while True:
                                if len(tmp344) > 1:
                                    tmp345 = create_operation_expression(associative1, tmp344)
                                elif len(tmp344) == 1:
                                    tmp345 = tmp344[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp345)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150830
                                    if len(subjects2) == 0:
                                        pass
                                        # State 150831
                                        if len(subjects) == 0:
                                            pass
                                            # 49: (d*(a + x*b)**n)**p
                                if len(subjects2) == 0:
                                    break
                                tmp344.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp344))
                subjects2.appendleft(tmp317)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                tmp347 = subjects2.popleft()
                subjects348 = deque(tmp347._args)
                # State 80702
                if len(subjects348) >= 1 and isinstance(subjects348[0], tan):
                    tmp349 = subjects348.popleft()
                    subjects350 = deque(tmp349._args)
                    # State 80703
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80704
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 80705
                            if len(subjects350) >= 1:
                                tmp353 = subjects350.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.4.1.0', tmp353)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 80706
                                    if len(subjects350) == 0:
                                        pass
                                        # State 80707
                                        if len(subjects348) >= 1 and subjects348[0] == -1:
                                            tmp355 = subjects348.popleft()
                                            # State 80708
                                            if len(subjects348) == 0:
                                                pass
                                                # State 80709
                                                if len(subjects2) >= 1:
                                                    tmp356 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.5', tmp356)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 80710
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 80711
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 36: (1/tan(e + x*f))**q
                                                    subjects2.appendleft(tmp356)
                                            subjects348.appendleft(tmp355)
                                subjects350.appendleft(tmp353)
                        if len(subjects350) >= 1 and isinstance(subjects350[0], Mul):
                            tmp358 = subjects350.popleft()
                            associative1 = tmp358
                            associative_type1 = type(tmp358)
                            subjects359 = deque(tmp358._args)
                            matcher = CommutativeMatcher80713.get()
                            tmp360 = subjects359
                            subjects359 = []
                            for s in tmp360:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp360, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 80714
                                    if len(subjects350) == 0:
                                        pass
                                        # State 80715
                                        if len(subjects348) >= 1 and subjects348[0] == -1:
                                            tmp361 = subjects348.popleft()
                                            # State 80716
                                            if len(subjects348) == 0:
                                                pass
                                                # State 80717
                                                if len(subjects2) >= 1:
                                                    tmp362 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.5', tmp362)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 80718
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 80719
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 36: (1/tan(e + x*f))**q
                                                    subjects2.appendleft(tmp362)
                                            subjects348.appendleft(tmp361)
                            subjects350.appendleft(tmp358)
                    if len(subjects350) >= 1 and isinstance(subjects350[0], Add):
                        tmp364 = subjects350.popleft()
                        associative1 = tmp364
                        associative_type1 = type(tmp364)
                        subjects365 = deque(tmp364._args)
                        matcher = CommutativeMatcher80721.get()
                        tmp366 = subjects365
                        subjects365 = []
                        for s in tmp366:
                            matcher.add_subject(s)
                        for pattern_index, subst1 in matcher.match(tmp366, subst0):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80727
                                if len(subjects350) == 0:
                                    pass
                                    # State 80728
                                    if len(subjects348) >= 1 and subjects348[0] == -1:
                                        tmp367 = subjects348.popleft()
                                        # State 80729
                                        if len(subjects348) == 0:
                                            pass
                                            # State 80730
                                            if len(subjects2) >= 1:
                                                tmp368 = subjects2.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.5', tmp368)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 80731
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 80732
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 36: (1/tan(e + x*f))**q
                                                subjects2.appendleft(tmp368)
                                        subjects348.appendleft(tmp367)
                        subjects350.appendleft(tmp364)
                    subjects348.appendleft(tmp349)
                subjects2.appendleft(tmp347)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tanh):
                tmp370 = subjects2.popleft()
                subjects371 = deque(tmp370._args)
                # State 125918
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 125919
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125920
                        if len(subjects371) >= 1:
                            tmp374 = subjects371.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp374)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125921
                                if len(subjects371) == 0:
                                    pass
                                    # State 125922
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp376 = subjects2.popleft()
                                        # State 125923
                                        if len(subjects2) == 0:
                                            pass
                                            # State 125924
                                            if len(subjects) == 0:
                                                pass
                                                # 46: 1/tanh(e + x*f)
                                        subjects2.appendleft(tmp376)
                            subjects371.appendleft(tmp374)
                    if len(subjects371) >= 1 and isinstance(subjects371[0], Mul):
                        tmp377 = subjects371.popleft()
                        associative1 = tmp377
                        associative_type1 = type(tmp377)
                        subjects378 = deque(tmp377._args)
                        matcher = CommutativeMatcher125926.get()
                        tmp379 = subjects378
                        subjects378 = []
                        for s in tmp379:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp379, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 125927
                                if len(subjects371) == 0:
                                    pass
                                    # State 125928
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp380 = subjects2.popleft()
                                        # State 125929
                                        if len(subjects2) == 0:
                                            pass
                                            # State 125930
                                            if len(subjects) == 0:
                                                pass
                                                # 46: 1/tanh(e + x*f)
                                        subjects2.appendleft(tmp380)
                        subjects371.appendleft(tmp377)
                if len(subjects371) >= 1 and isinstance(subjects371[0], Add):
                    tmp381 = subjects371.popleft()
                    associative1 = tmp381
                    associative_type1 = type(tmp381)
                    subjects382 = deque(tmp381._args)
                    matcher = CommutativeMatcher125932.get()
                    tmp383 = subjects382
                    subjects382 = []
                    for s in tmp383:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp383, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 125938
                            if len(subjects371) == 0:
                                pass
                                # State 125939
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp384 = subjects2.popleft()
                                    # State 125940
                                    if len(subjects2) == 0:
                                        pass
                                        # State 125941
                                        if len(subjects) == 0:
                                            pass
                                            # 46: 1/tanh(e + x*f)
                                    subjects2.appendleft(tmp384)
                    subjects371.appendleft(tmp381)
                subjects2.appendleft(tmp370)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 6499
            if len(subjects) >= 1:
                tmp386 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1', tmp386)
                except ValueError:
                    pass
                else:
                    pass
                    # State 6500
                    if len(subjects) == 0:
                        pass
                        # 1: x**n
                subjects.appendleft(tmp386)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp388 = subjects.popleft()
                associative1 = tmp388
                associative_type1 = type(tmp388)
                subjects389 = deque(tmp388._args)
                matcher = CommutativeMatcher10313.get()
                tmp390 = subjects389
                subjects389 = []
                for s in tmp390:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp390, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10330
                        if len(subjects) == 0:
                            pass
                            # 2: (a + b*x**n)**r
                subjects.appendleft(tmp388)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 10467
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10468
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.2.1.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 10469
                    if len(subjects) >= 1:
                        tmp394 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.2.1.1', tmp394)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10470
                            if len(subjects) == 0:
                                pass
                                # 5: a + b*x**n
                        subjects.appendleft(tmp394)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp396 = subjects.popleft()
                    subjects397 = deque(tmp396._args)
                    # State 10471
                    if len(subjects397) >= 1:
                        tmp398 = subjects397.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.1', tmp398)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10472
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 10473
                                if len(subjects397) == 0:
                                    pass
                                    # State 10474
                                    if len(subjects) == 0:
                                        pass
                                        # 5: a + b*x**n
                            if len(subjects397) >= 1:
                                tmp401 = subjects397.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.1.2', tmp401)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10473
                                    if len(subjects397) == 0:
                                        pass
                                        # State 10474
                                        if len(subjects) == 0:
                                            pass
                                            # 5: a + b*x**n
                                subjects397.appendleft(tmp401)
                        subjects397.appendleft(tmp398)
                    subjects.appendleft(tmp396)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp403 = subjects.popleft()
                associative1 = tmp403
                associative_type1 = type(tmp403)
                subjects404 = deque(tmp403._args)
                matcher = CommutativeMatcher10476.get()
                tmp405 = subjects404
                subjects404 = []
                for s in tmp405:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp405, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10483
                        if len(subjects) == 0:
                            pass
                            # 5: a + b*x**n
                subjects.appendleft(tmp403)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 103405
            if len(subjects) >= 1:
                tmp407 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1_1', tmp407)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103406
                    if len(subjects) == 0:
                        pass
                        # 42: w**n
                subjects.appendleft(tmp407)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 151906
            if len(subjects) >= 1:
                tmp410 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1_2', tmp410)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151907
                    if len(subjects) == 0:
                        pass
                        # 50: z**q
                subjects.appendleft(tmp410)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp412 = subjects.popleft()
            associative1 = tmp412
            associative_type1 = type(tmp412)
            subjects413 = deque(tmp412._args)
            matcher = CommutativeMatcher10485.get()
            tmp414 = subjects413
            subjects413 = []
            for s in tmp414:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp414, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 10502
                    if len(subjects) == 0:
                        pass
                        # 5: a + b*x**n
                if pattern_index == 1:
                    pass
                    # State 14191
                    if len(subjects) == 0:
                        pass
                        # 6: a*x + b*sqrt(c + d*x**2)
            subjects.appendleft(tmp412)
        if len(subjects) >= 1 and subjects[0] == LambertW(a + b*x):
            tmp415 = subjects.popleft()
            # State 56706
            if len(subjects) == 0:
                pass
                # 8: LambertW(a + b*x)
            subjects.appendleft(tmp415)
        if len(subjects) >= 1 and subjects[0] == LambertW(a*x**n):
            tmp416 = subjects.popleft()
            # State 56737
            if len(subjects) == 0:
                pass
                # 9: LambertW(a*x**n)
            subjects.appendleft(tmp416)
        if len(subjects) >= 1 and subjects[0] == LambertW(a*x):
            tmp417 = subjects.popleft()
            # State 56753
            if len(subjects) == 0:
                pass
                # 10: LambertW(a*x)
            subjects.appendleft(tmp417)
        if len(subjects) >= 1 and subjects[0] == LambertW(a*x**n):
            tmp418 = subjects.popleft()
            # State 56766
            if len(subjects) == 0:
                pass
                # 11: LambertW(a*x**n)
            subjects.appendleft(tmp418)
        if len(subjects) >= 1 and subjects[0] == LambertW(a + b*x):
            tmp419 = subjects.popleft()
            # State 56794
            if len(subjects) == 0:
                pass
                # 12: LambertW(a + b*x)
            subjects.appendleft(tmp419)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp420 = subjects.popleft()
            subjects421 = deque(tmp420._args)
            # State 57003
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 57004
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57005
                    if len(subjects421) >= 1:
                        tmp424 = subjects421.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp424)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 57006
                            if len(subjects421) == 0:
                                pass
                                # State 57007
                                if len(subjects) == 0:
                                    pass
                                    # 13: cos(e + x*f)
                        subjects421.appendleft(tmp424)
                if len(subjects421) >= 1 and isinstance(subjects421[0], Mul):
                    tmp426 = subjects421.popleft()
                    associative1 = tmp426
                    associative_type1 = type(tmp426)
                    subjects427 = deque(tmp426._args)
                    matcher = CommutativeMatcher57009.get()
                    tmp428 = subjects427
                    subjects427 = []
                    for s in tmp428:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp428, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57010
                            if len(subjects421) == 0:
                                pass
                                # State 57011
                                if len(subjects) == 0:
                                    pass
                                    # 13: cos(e + x*f)
                    subjects421.appendleft(tmp426)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 57685
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57686
                    if len(subjects421) >= 1:
                        tmp431 = subjects421.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp431)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 57687
                            if len(subjects421) == 0:
                                pass
                                # State 57688
                                if len(subjects) == 0:
                                    pass
                                    # 18: cos(e + x*f)
                        subjects421.appendleft(tmp431)
                if len(subjects421) >= 1 and isinstance(subjects421[0], Mul):
                    tmp433 = subjects421.popleft()
                    associative1 = tmp433
                    associative_type1 = type(tmp433)
                    subjects434 = deque(tmp433._args)
                    matcher = CommutativeMatcher57690.get()
                    tmp435 = subjects434
                    subjects434 = []
                    for s in tmp435:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp435, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57691
                            if len(subjects421) == 0:
                                pass
                                # State 57692
                                if len(subjects) == 0:
                                    pass
                                    # 18: cos(e + x*f)
                    subjects421.appendleft(tmp433)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 76160
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76161
                    if len(subjects421) >= 1:
                        tmp438 = subjects421.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp438)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 76162
                            if len(subjects421) == 0:
                                pass
                                # State 76163
                                if len(subjects) == 0:
                                    pass
                                    # 25: cos(e + x*f)
                        subjects421.appendleft(tmp438)
                if len(subjects421) >= 1 and isinstance(subjects421[0], Mul):
                    tmp440 = subjects421.popleft()
                    associative1 = tmp440
                    associative_type1 = type(tmp440)
                    subjects441 = deque(tmp440._args)
                    matcher = CommutativeMatcher76165.get()
                    tmp442 = subjects441
                    subjects441 = []
                    for s in tmp442:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp442, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 76166
                            if len(subjects421) == 0:
                                pass
                                # State 76167
                                if len(subjects) == 0:
                                    pass
                                    # 25: cos(e + x*f)
                    subjects421.appendleft(tmp440)
            if len(subjects421) >= 1 and isinstance(subjects421[0], Add):
                tmp443 = subjects421.popleft()
                associative1 = tmp443
                associative_type1 = type(tmp443)
                subjects444 = deque(tmp443._args)
                matcher = CommutativeMatcher57013.get()
                tmp445 = subjects444
                subjects444 = []
                for s in tmp445:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp445, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 57019
                        if len(subjects421) == 0:
                            pass
                            # State 57020
                            if len(subjects) == 0:
                                pass
                                # 13: cos(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 57696
                        if len(subjects421) == 0:
                            pass
                            # State 57697
                            if len(subjects) == 0:
                                pass
                                # 18: cos(e + x*f)
                    if pattern_index == 2:
                        pass
                        # State 76171
                        if len(subjects421) == 0:
                            pass
                            # State 76172
                            if len(subjects) == 0:
                                pass
                                # 25: cos(e + x*f)
                subjects421.appendleft(tmp443)
            subjects.appendleft(tmp420)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp446 = subjects.popleft()
            subjects447 = deque(tmp446._args)
            # State 57085
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 57086
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57087
                    if len(subjects447) >= 1:
                        tmp450 = subjects447.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp450)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 57088
                            if len(subjects447) == 0:
                                pass
                                # State 57089
                                if len(subjects) == 0:
                                    pass
                                    # 14: sin(e + x*f)
                        subjects447.appendleft(tmp450)
                if len(subjects447) >= 1 and isinstance(subjects447[0], Mul):
                    tmp452 = subjects447.popleft()
                    associative1 = tmp452
                    associative_type1 = type(tmp452)
                    subjects453 = deque(tmp452._args)
                    matcher = CommutativeMatcher57091.get()
                    tmp454 = subjects453
                    subjects453 = []
                    for s in tmp454:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp454, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57092
                            if len(subjects447) == 0:
                                pass
                                # State 57093
                                if len(subjects) == 0:
                                    pass
                                    # 14: sin(e + x*f)
                    subjects447.appendleft(tmp452)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 57499
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57500
                    if len(subjects447) >= 1:
                        tmp457 = subjects447.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp457)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 57501
                            if len(subjects447) == 0:
                                pass
                                # State 57502
                                if len(subjects) == 0:
                                    pass
                                    # 16: sin(e + x*f)
                        subjects447.appendleft(tmp457)
                if len(subjects447) >= 1 and isinstance(subjects447[0], Mul):
                    tmp459 = subjects447.popleft()
                    associative1 = tmp459
                    associative_type1 = type(tmp459)
                    subjects460 = deque(tmp459._args)
                    matcher = CommutativeMatcher57504.get()
                    tmp461 = subjects460
                    subjects460 = []
                    for s in tmp461:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp461, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57505
                            if len(subjects447) == 0:
                                pass
                                # State 57506
                                if len(subjects) == 0:
                                    pass
                                    # 16: sin(e + x*f)
                    subjects447.appendleft(tmp459)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 100952
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 100953
                    if len(subjects447) >= 1:
                        tmp464 = subjects447.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp464)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 100954
                            if len(subjects447) == 0:
                                pass
                                # State 100955
                                if len(subjects) == 0:
                                    pass
                                    # 39: sin(c + x*d)
                        subjects447.appendleft(tmp464)
                if len(subjects447) >= 1 and isinstance(subjects447[0], Mul):
                    tmp466 = subjects447.popleft()
                    associative1 = tmp466
                    associative_type1 = type(tmp466)
                    subjects467 = deque(tmp466._args)
                    matcher = CommutativeMatcher100957.get()
                    tmp468 = subjects467
                    subjects467 = []
                    for s in tmp468:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp468, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 100958
                            if len(subjects447) == 0:
                                pass
                                # State 100959
                                if len(subjects) == 0:
                                    pass
                                    # 39: sin(c + x*d)
                    subjects447.appendleft(tmp466)
            if len(subjects447) >= 1 and isinstance(subjects447[0], Add):
                tmp469 = subjects447.popleft()
                associative1 = tmp469
                associative_type1 = type(tmp469)
                subjects470 = deque(tmp469._args)
                matcher = CommutativeMatcher57095.get()
                tmp471 = subjects470
                subjects470 = []
                for s in tmp471:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp471, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 57101
                        if len(subjects447) == 0:
                            pass
                            # State 57102
                            if len(subjects) == 0:
                                pass
                                # 14: sin(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 57510
                        if len(subjects447) == 0:
                            pass
                            # State 57511
                            if len(subjects) == 0:
                                pass
                                # 16: sin(e + x*f)
                    if pattern_index == 2:
                        pass
                        # State 100963
                        if len(subjects447) == 0:
                            pass
                            # State 100964
                            if len(subjects) == 0:
                                pass
                                # 39: sin(c + x*d)
                subjects447.appendleft(tmp469)
            subjects.appendleft(tmp446)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp472 = subjects.popleft()
            subjects473 = deque(tmp472._args)
            # State 59202
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 59203
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59204
                    if len(subjects473) >= 1:
                        tmp476 = subjects473.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp476)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 59205
                            if len(subjects473) == 0:
                                pass
                                # State 59206
                                if len(subjects) == 0:
                                    pass
                                    # 19: tan(e + x*f)
                        subjects473.appendleft(tmp476)
                if len(subjects473) >= 1 and isinstance(subjects473[0], Mul):
                    tmp478 = subjects473.popleft()
                    associative1 = tmp478
                    associative_type1 = type(tmp478)
                    subjects479 = deque(tmp478._args)
                    matcher = CommutativeMatcher59208.get()
                    tmp480 = subjects479
                    subjects479 = []
                    for s in tmp480:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp480, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 59209
                            if len(subjects473) == 0:
                                pass
                                # State 59210
                                if len(subjects) == 0:
                                    pass
                                    # 19: tan(e + x*f)
                    subjects473.appendleft(tmp478)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 76210
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76211
                    if len(subjects473) >= 1:
                        tmp483 = subjects473.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp483)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 76212
                            if len(subjects473) == 0:
                                pass
                                # State 76213
                                if len(subjects) == 0:
                                    pass
                                    # 26: tan(e + x*f)
                        subjects473.appendleft(tmp483)
                if len(subjects473) >= 1 and isinstance(subjects473[0], Mul):
                    tmp485 = subjects473.popleft()
                    associative1 = tmp485
                    associative_type1 = type(tmp485)
                    subjects486 = deque(tmp485._args)
                    matcher = CommutativeMatcher76215.get()
                    tmp487 = subjects486
                    subjects486 = []
                    for s in tmp487:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp487, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 76216
                            if len(subjects473) == 0:
                                pass
                                # State 76217
                                if len(subjects) == 0:
                                    pass
                                    # 26: tan(e + x*f)
                    subjects473.appendleft(tmp485)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 76412
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76413
                    if len(subjects473) >= 1:
                        tmp490 = subjects473.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp490)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 76414
                            if len(subjects473) == 0:
                                pass
                                # State 76415
                                if len(subjects) == 0:
                                    pass
                                    # 27: tan(e + x*f)
                        subjects473.appendleft(tmp490)
                if len(subjects473) >= 1 and isinstance(subjects473[0], Mul):
                    tmp492 = subjects473.popleft()
                    associative1 = tmp492
                    associative_type1 = type(tmp492)
                    subjects493 = deque(tmp492._args)
                    matcher = CommutativeMatcher76417.get()
                    tmp494 = subjects493
                    subjects493 = []
                    for s in tmp494:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp494, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 76418
                            if len(subjects473) == 0:
                                pass
                                # State 76419
                                if len(subjects) == 0:
                                    pass
                                    # 27: tan(e + x*f)
                    subjects473.appendleft(tmp492)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 76940
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76941
                    if len(subjects473) >= 1:
                        tmp497 = subjects473.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.3.1.0', tmp497)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 76942
                            if len(subjects473) == 0:
                                pass
                                # State 76943
                                if len(subjects) == 0:
                                    pass
                                    # 30: tan(e + x*f)
                        subjects473.appendleft(tmp497)
                if len(subjects473) >= 1 and isinstance(subjects473[0], Mul):
                    tmp499 = subjects473.popleft()
                    associative1 = tmp499
                    associative_type1 = type(tmp499)
                    subjects500 = deque(tmp499._args)
                    matcher = CommutativeMatcher76945.get()
                    tmp501 = subjects500
                    subjects500 = []
                    for s in tmp501:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp501, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 76946
                            if len(subjects473) == 0:
                                pass
                                # State 76947
                                if len(subjects) == 0:
                                    pass
                                    # 30: tan(e + x*f)
                    subjects473.appendleft(tmp499)
            if len(subjects473) >= 1 and isinstance(subjects473[0], Add):
                tmp502 = subjects473.popleft()
                associative1 = tmp502
                associative_type1 = type(tmp502)
                subjects503 = deque(tmp502._args)
                matcher = CommutativeMatcher59212.get()
                tmp504 = subjects503
                subjects503 = []
                for s in tmp504:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp504, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 59218
                        if len(subjects473) == 0:
                            pass
                            # State 59219
                            if len(subjects) == 0:
                                pass
                                # 19: tan(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 76221
                        if len(subjects473) == 0:
                            pass
                            # State 76222
                            if len(subjects) == 0:
                                pass
                                # 26: tan(e + x*f)
                    if pattern_index == 2:
                        pass
                        # State 76423
                        if len(subjects473) == 0:
                            pass
                            # State 76424
                            if len(subjects) == 0:
                                pass
                                # 27: tan(e + x*f)
                    if pattern_index == 3:
                        pass
                        # State 76951
                        if len(subjects473) == 0:
                            pass
                            # State 76952
                            if len(subjects) == 0:
                                pass
                                # 30: tan(e + x*f)
                subjects473.appendleft(tmp502)
            subjects.appendleft(tmp472)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp505 = subjects.popleft()
            subjects506 = deque(tmp505._args)
            # State 121669
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 121670
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 121671
                    if len(subjects506) >= 1:
                        tmp509 = subjects506.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp509)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 121672
                            if len(subjects506) == 0:
                                pass
                                # State 121673
                                if len(subjects) == 0:
                                    pass
                                    # 43: sinh(e + x*f)
                        subjects506.appendleft(tmp509)
                if len(subjects506) >= 1 and isinstance(subjects506[0], Mul):
                    tmp511 = subjects506.popleft()
                    associative1 = tmp511
                    associative_type1 = type(tmp511)
                    subjects512 = deque(tmp511._args)
                    matcher = CommutativeMatcher121675.get()
                    tmp513 = subjects512
                    subjects512 = []
                    for s in tmp513:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp513, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 121676
                            if len(subjects506) == 0:
                                pass
                                # State 121677
                                if len(subjects) == 0:
                                    pass
                                    # 43: sinh(e + x*f)
                    subjects506.appendleft(tmp511)
            if len(subjects506) >= 1 and isinstance(subjects506[0], Add):
                tmp514 = subjects506.popleft()
                associative1 = tmp514
                associative_type1 = type(tmp514)
                subjects515 = deque(tmp514._args)
                matcher = CommutativeMatcher121679.get()
                tmp516 = subjects515
                subjects515 = []
                for s in tmp516:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp516, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 121685
                        if len(subjects506) == 0:
                            pass
                            # State 121686
                            if len(subjects) == 0:
                                pass
                                # 43: sinh(e + x*f)
                subjects506.appendleft(tmp514)
            subjects.appendleft(tmp505)
        if len(subjects) >= 1 and isinstance(subjects[0], cosh):
            tmp517 = subjects.popleft()
            subjects518 = deque(tmp517._args)
            # State 121717
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 121718
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 121719
                    if len(subjects518) >= 1:
                        tmp521 = subjects518.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp521)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 121720
                            if len(subjects518) == 0:
                                pass
                                # State 121721
                                if len(subjects) == 0:
                                    pass
                                    # 44: cosh(e + x*f)
                        subjects518.appendleft(tmp521)
                if len(subjects518) >= 1 and isinstance(subjects518[0], Mul):
                    tmp523 = subjects518.popleft()
                    associative1 = tmp523
                    associative_type1 = type(tmp523)
                    subjects524 = deque(tmp523._args)
                    matcher = CommutativeMatcher121723.get()
                    tmp525 = subjects524
                    subjects524 = []
                    for s in tmp525:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp525, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 121724
                            if len(subjects518) == 0:
                                pass
                                # State 121725
                                if len(subjects) == 0:
                                    pass
                                    # 44: cosh(e + x*f)
                    subjects518.appendleft(tmp523)
            if len(subjects518) >= 1 and isinstance(subjects518[0], Add):
                tmp526 = subjects518.popleft()
                associative1 = tmp526
                associative_type1 = type(tmp526)
                subjects527 = deque(tmp526._args)
                matcher = CommutativeMatcher121727.get()
                tmp528 = subjects527
                subjects527 = []
                for s in tmp528:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp528, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 121733
                        if len(subjects518) == 0:
                            pass
                            # State 121734
                            if len(subjects) == 0:
                                pass
                                # 44: cosh(e + x*f)
                subjects518.appendleft(tmp526)
            subjects.appendleft(tmp517)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp529 = subjects.popleft()
            subjects530 = deque(tmp529._args)
            # State 125864
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 125865
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 125866
                    if len(subjects530) >= 1:
                        tmp533 = subjects530.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp533)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 125867
                            if len(subjects530) == 0:
                                pass
                                # State 125868
                                if len(subjects) == 0:
                                    pass
                                    # 45: tanh(e + x*f)
                        subjects530.appendleft(tmp533)
                if len(subjects530) >= 1 and isinstance(subjects530[0], Mul):
                    tmp535 = subjects530.popleft()
                    associative1 = tmp535
                    associative_type1 = type(tmp535)
                    subjects536 = deque(tmp535._args)
                    matcher = CommutativeMatcher125870.get()
                    tmp537 = subjects536
                    subjects536 = []
                    for s in tmp537:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp537, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 125871
                            if len(subjects530) == 0:
                                pass
                                # State 125872
                                if len(subjects) == 0:
                                    pass
                                    # 45: tanh(e + x*f)
                    subjects530.appendleft(tmp535)
            if len(subjects530) >= 1 and isinstance(subjects530[0], Add):
                tmp538 = subjects530.popleft()
                associative1 = tmp538
                associative_type1 = type(tmp538)
                subjects539 = deque(tmp538._args)
                matcher = CommutativeMatcher125874.get()
                tmp540 = subjects539
                subjects539 = []
                for s in tmp540:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp540, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 125880
                        if len(subjects530) == 0:
                            pass
                            # State 125881
                            if len(subjects) == 0:
                                pass
                                # 45: tanh(e + x*f)
                subjects530.appendleft(tmp538)
            subjects.appendleft(tmp529)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
