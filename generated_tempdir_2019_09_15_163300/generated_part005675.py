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


class CommutativeMatcher2381(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.1', 1, 1, None), Mul)
]),
    9: (9, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.2.1.1', 1, 1, None), Mul)
]),
    10: (10, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({13: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({14: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({15: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({16: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({17: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({18: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({19: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({20: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({21: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({22: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    27: (27, Multiset({23: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({24: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({25: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({26: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    31: (31, Multiset({27: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({28: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    33: (33, Multiset({29: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.4.1.1', 1, 1, None), Mul)
]),
    35: (35, Multiset({30: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    36: (36, Multiset({31: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    37: (37, Multiset({32: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    38: (38, Multiset({33: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({34: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({35: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    41: (41, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.4.1.0', 1, 1, None), Mul)
]),
    42: (42, Multiset({36: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    43: (43, Multiset({37: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    44: (44, Multiset({38: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    45: (45, Multiset({39: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    46: (46, Multiset({40: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    47: (47, Multiset({41: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    48: (48, Multiset({42: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    49: (49, Multiset({43: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    50: (50, Multiset({44: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    51: (51, Multiset({45: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    52: (52, Multiset({46: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    53: (53, Multiset({47: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    54: (54, Multiset({48: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    55: (55, Multiset({49: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    56: (56, Multiset({50: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    57: (57, Multiset({51: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    58: (58, Multiset({52: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    59: (59, Multiset({53: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    60: (60, Multiset({54: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    61: (61, Multiset({55: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    62: (62, Multiset({56: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    63: (63, Multiset({57: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    64: (64, Multiset({58: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    65: (65, Multiset({59: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    66: (66, Multiset({60: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    67: (67, Multiset({61: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    68: (68, Multiset({62: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    69: (69, Multiset({63: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    70: (70, Multiset({64: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    71: (71, Multiset({65: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    72: (72, Multiset({66: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    73: (73, Multiset({67: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    74: (74, Multiset({68: 1, 69: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    75: (75, Multiset({70: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    76: (76, Multiset({71: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    77: (77, Multiset({72: 1, 2: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 2
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher2381._instance is None:
            CommutativeMatcher2381._instance = CommutativeMatcher2381()
        return CommutativeMatcher2381._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2380
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2382
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2383
                    if len(subjects) == 0:
                        pass
                        # 0: x**n
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 15233
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 15234
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 15235
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.4.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 15236
                            if len(subjects6) >= 1:
                                tmp10 = subjects6.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.4.0', tmp10)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 15237
                                    if len(subjects6) == 0:
                                        pass
                                        # State 15238
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (F**(v*g))**n
                                            yield 6, subst4
                                subjects6.appendleft(tmp10)
                        if len(subjects6) >= 1 and isinstance(subjects6[0], Mul):
                            tmp12 = subjects6.popleft()
                            associative1 = tmp12
                            associative_type1 = type(tmp12)
                            subjects13 = deque(tmp12._args)
                            matcher = CommutativeMatcher15240.get()
                            tmp14 = subjects13
                            subjects13 = []
                            for s in tmp14:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp14, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 15241
                                    if len(subjects6) == 0:
                                        pass
                                        # State 15242
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (F**(v*g))**n
                                            yield 6, subst3
                            subjects6.appendleft(tmp12)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 16022
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp16 = subjects.popleft()
                subjects17 = deque(tmp16._args)
                # State 16023
                if len(subjects17) >= 1:
                    tmp18 = subjects17.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2', tmp18)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 16024
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 16025
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 16026
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.4.1.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 16027
                                    if len(subjects17) >= 1:
                                        tmp23 = subjects17.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.4.1.1.0', tmp23)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 16028
                                            if len(subjects17) == 0:
                                                pass
                                                # State 16029
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (F**(g*(e + x*f)))**n
                                                    yield 7, subst6
                                        subjects17.appendleft(tmp23)
                                if len(subjects17) >= 1 and isinstance(subjects17[0], Mul):
                                    tmp25 = subjects17.popleft()
                                    associative1 = tmp25
                                    associative_type1 = type(tmp25)
                                    subjects26 = deque(tmp25._args)
                                    matcher = CommutativeMatcher16031.get()
                                    tmp27 = subjects26
                                    subjects26 = []
                                    for s in tmp27:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp27, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 16032
                                            if len(subjects17) == 0:
                                                pass
                                                # State 16033
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (F**(g*(e + x*f)))**n
                                                    yield 7, subst5
                                    subjects17.appendleft(tmp25)
                            if len(subjects17) >= 1 and isinstance(subjects17[0], Add):
                                tmp28 = subjects17.popleft()
                                associative1 = tmp28
                                associative_type1 = type(tmp28)
                                subjects29 = deque(tmp28._args)
                                matcher = CommutativeMatcher16035.get()
                                tmp30 = subjects29
                                subjects29 = []
                                for s in tmp30:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp30, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 16041
                                        if len(subjects17) == 0:
                                            pass
                                            # State 16042
                                            if len(subjects) == 0:
                                                pass
                                                # 7: (F**(g*(e + x*f)))**n
                                                yield 7, subst4
                                subjects17.appendleft(tmp28)
                        if len(subjects17) >= 1 and isinstance(subjects17[0], Mul):
                            tmp31 = subjects17.popleft()
                            associative1 = tmp31
                            associative_type1 = type(tmp31)
                            subjects32 = deque(tmp31._args)
                            matcher = CommutativeMatcher16044.get()
                            tmp33 = subjects32
                            subjects32 = []
                            for s in tmp33:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp33, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 16059
                                    if len(subjects17) == 0:
                                        pass
                                        # State 16060
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (F**(g*(e + x*f)))**n
                                            yield 7, subst3
                            subjects17.appendleft(tmp31)
                    subjects17.appendleft(tmp18)
                subjects.appendleft(tmp16)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 151995
            if len(subjects) >= 1:
                tmp35 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1_1', tmp35)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151996
                    if len(subjects) == 0:
                        pass
                        # 72: w**n2
                        yield 72, subst2
                subjects.appendleft(tmp35)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp37 = subjects.popleft()
            subjects38 = deque(tmp37._args)
            # State 2384
            if len(subjects38) >= 1:
                tmp39 = subjects38.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp39)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2385
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2386
                        if len(subjects38) == 0:
                            pass
                            # State 2387
                            if len(subjects) == 0:
                                pass
                                # 0: x**n
                                yield 0, subst2
                    if len(subjects38) >= 1:
                        tmp42 = subjects38.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp42)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2386
                            if len(subjects38) == 0:
                                pass
                                # State 2387
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects38.appendleft(tmp42)
                    if len(subjects38) >= 1:
                        tmp44 = subjects38.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp44)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 6397
                            if len(subjects38) == 0:
                                pass
                                # State 6398
                                if len(subjects) == 0:
                                    pass
                                    # 2: x**j
                                    yield 2, subst2
                        subjects38.appendleft(tmp44)
                    if len(subjects38) >= 1 and subjects38[0] == Integer(2):
                        tmp46 = subjects38.popleft()
                        # State 5104
                        if len(subjects38) == 0:
                            pass
                            # State 5105
                            if len(subjects) == 0:
                                pass
                                # 1: x**2
                                yield 1, subst1
                        subjects38.appendleft(tmp46)
                    if len(subjects38) >= 1 and isinstance(subjects38[0], Mul):
                        tmp47 = subjects38.popleft()
                        associative1 = tmp47
                        associative_type1 = type(tmp47)
                        subjects48 = deque(tmp47._args)
                        matcher = CommutativeMatcher151235.get()
                        tmp49 = subjects48
                        subjects48 = []
                        for s in tmp49:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp49, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 151273
                                if len(subjects38) == 0:
                                    pass
                                    # State 151274
                                    if len(subjects) == 0:
                                        pass
                                        # 70: F**(c*sqrt(d + x*e)/sqrt(f + x*g))
                                        yield 70, subst2
                            if pattern_index == 1:
                                pass
                                # State 151432
                                if len(subjects38) == 0:
                                    pass
                                    # State 151433
                                    if len(subjects) == 0:
                                        pass
                                        # 71: F**(c*sqrt(x*e + 1)/sqrt(x*g + 1))
                                        yield 71, subst2
                        subjects38.appendleft(tmp47)
                subjects38.appendleft(tmp39)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10206
                if len(subjects38) >= 1 and isinstance(subjects38[0], Pow):
                    tmp51 = subjects38.popleft()
                    subjects52 = deque(tmp51._args)
                    # State 10207
                    if len(subjects52) >= 1:
                        tmp53 = subjects52.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1', tmp53)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10208
                            if len(subjects52) >= 1:
                                tmp55 = subjects52.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', tmp55)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10209
                                    if len(subjects52) == 0:
                                        pass
                                        # State 10210
                                        if len(subjects38) >= 1:
                                            tmp57 = subjects38.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2', tmp57)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 10211
                                                if len(subjects38) == 0:
                                                    pass
                                                    # State 10212
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (c*x**n)**q
                                                        yield 3, subst4
                                            subjects38.appendleft(tmp57)
                                subjects52.appendleft(tmp55)
                            if len(subjects52) >= 1 and subjects52[0] == Integer(-1):
                                tmp59 = subjects52.popleft()
                                # State 10694
                                if len(subjects52) == 0:
                                    pass
                                    # State 10695
                                    if len(subjects38) >= 1:
                                        tmp60 = subjects38.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', tmp60)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 10696
                                            if len(subjects38) == 0:
                                                pass
                                                # State 10697
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (c/x)**n
                                                    yield 4, subst3
                                        subjects38.appendleft(tmp60)
                                subjects52.appendleft(tmp59)
                        subjects52.appendleft(tmp53)
                    subjects38.appendleft(tmp51)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 150905
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 150906
                    if len(subjects38) >= 1:
                        tmp64 = subjects38.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp64)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 150907
                            if len(subjects38) >= 1 and subjects38[0] == Rational(1, 2):
                                tmp66 = subjects38.popleft()
                                # State 150908
                                if len(subjects38) == 0:
                                    pass
                                    # State 150909
                                    if len(subjects) == 0:
                                        pass
                                        # 68: sqrt(d + x*d)
                                        yield 68, subst3
                                subjects38.appendleft(tmp66)
                        subjects38.appendleft(tmp64)
                if len(subjects38) >= 1 and isinstance(subjects38[0], Mul):
                    tmp67 = subjects38.popleft()
                    associative1 = tmp67
                    associative_type1 = type(tmp67)
                    subjects68 = deque(tmp67._args)
                    matcher = CommutativeMatcher150911.get()
                    tmp69 = subjects68
                    subjects68 = []
                    for s in tmp69:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp69, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 150912
                            if len(subjects38) >= 1 and subjects38[0] == Rational(1, 2):
                                tmp70 = subjects38.popleft()
                                # State 150913
                                if len(subjects38) == 0:
                                    pass
                                    # State 150914
                                    if len(subjects) == 0:
                                        pass
                                        # 68: sqrt(d + x*d)
                                        yield 68, subst2
                                subjects38.appendleft(tmp70)
                    subjects38.appendleft(tmp67)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 150918
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 150919
                    if len(subjects38) >= 1:
                        tmp73 = subjects38.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp73)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 150920
                            if len(subjects38) >= 1 and subjects38[0] == Rational(-1, 2):
                                tmp75 = subjects38.popleft()
                                # State 150921
                                if len(subjects38) == 0:
                                    pass
                                    # State 150922
                                    if len(subjects) == 0:
                                        pass
                                        # 69: 1/sqrt(f + x*g)
                                        yield 69, subst3
                                subjects38.appendleft(tmp75)
                        subjects38.appendleft(tmp73)
                if len(subjects38) >= 1 and isinstance(subjects38[0], Mul):
                    tmp76 = subjects38.popleft()
                    associative1 = tmp76
                    associative_type1 = type(tmp76)
                    subjects77 = deque(tmp76._args)
                    matcher = CommutativeMatcher150924.get()
                    tmp78 = subjects77
                    subjects77 = []
                    for s in tmp78:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp78, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 150925
                            if len(subjects38) >= 1 and subjects38[0] == Rational(-1, 2):
                                tmp79 = subjects38.popleft()
                                # State 150926
                                if len(subjects38) == 0:
                                    pass
                                    # State 150927
                                    if len(subjects) == 0:
                                        pass
                                        # 69: 1/sqrt(f + x*g)
                                        yield 69, subst2
                                subjects38.appendleft(tmp79)
                    subjects38.appendleft(tmp76)
            if len(subjects38) >= 1:
                tmp80 = subjects38.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1_1', tmp80)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151997
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151998
                        if len(subjects38) == 0:
                            pass
                            # State 151999
                            if len(subjects) == 0:
                                pass
                                # 72: w**n2
                                yield 72, subst2
                    if len(subjects38) >= 1:
                        tmp83 = subjects38.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp83)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151998
                            if len(subjects38) == 0:
                                pass
                                # State 151999
                                if len(subjects) == 0:
                                    pass
                                    # 72: w**n2
                                    yield 72, subst2
                        subjects38.appendleft(tmp83)
                subjects38.appendleft(tmp80)
            if len(subjects38) >= 1 and isinstance(subjects38[0], Mul):
                tmp85 = subjects38.popleft()
                associative1 = tmp85
                associative_type1 = type(tmp85)
                subjects86 = deque(tmp85._args)
                matcher = CommutativeMatcher10214.get()
                tmp87 = subjects86
                subjects86 = []
                for s in tmp87:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp87, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10219
                        if len(subjects38) >= 1:
                            tmp88 = []
                            tmp88.append(subjects38.popleft())
                            while True:
                                if len(tmp88) > 1:
                                    tmp89 = create_operation_expression(associative1, tmp88)
                                elif len(tmp88) == 1:
                                    tmp89 = tmp88[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp89)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10220
                                    if len(subjects38) == 0:
                                        pass
                                        # State 10221
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (c*x**n)**q
                                            yield 3, subst2
                                if len(subjects38) == 0:
                                    break
                                tmp88.append(subjects38.popleft())
                            subjects38.extendleft(reversed(tmp88))
                    if pattern_index == 1:
                        pass
                        # State 10700
                        if len(subjects38) >= 1:
                            tmp91 = []
                            tmp91.append(subjects38.popleft())
                            while True:
                                if len(tmp91) > 1:
                                    tmp92 = create_operation_expression(associative1, tmp91)
                                elif len(tmp91) == 1:
                                    tmp92 = tmp91[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp92)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10701
                                    if len(subjects38) == 0:
                                        pass
                                        # State 10702
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (c/x)**n
                                            yield 4, subst2
                                if len(subjects38) == 0:
                                    break
                                tmp91.append(subjects38.popleft())
                            subjects38.extendleft(reversed(tmp91))
                subjects38.appendleft(tmp85)
            if len(subjects38) >= 1 and isinstance(subjects38[0], Add):
                tmp94 = subjects38.popleft()
                associative1 = tmp94
                associative_type1 = type(tmp94)
                subjects95 = deque(tmp94._args)
                matcher = CommutativeMatcher11753.get()
                tmp96 = subjects95
                subjects95 = []
                for s in tmp96:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp96, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 11759
                        if len(subjects38) >= 1:
                            tmp97 = []
                            tmp97.append(subjects38.popleft())
                            while True:
                                if len(tmp97) > 1:
                                    tmp98 = create_operation_expression(associative1, tmp97)
                                elif len(tmp97) == 1:
                                    tmp98 = tmp97[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp98)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 11760
                                    if len(subjects38) == 0:
                                        pass
                                        # State 11761
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (c + x*d)**n
                                            yield 5, subst2
                                if len(subjects38) == 0:
                                    break
                                tmp97.append(subjects38.popleft())
                            subjects38.extendleft(reversed(tmp97))
                    if pattern_index == 1:
                        pass
                        # State 150915
                        if len(subjects38) >= 1 and subjects38[0] == Rational(1, 2):
                            tmp100 = subjects38.popleft()
                            # State 150916
                            if len(subjects38) == 0:
                                pass
                                # State 150917
                                if len(subjects) == 0:
                                    pass
                                    # 68: sqrt(d + x*d)
                                    yield 68, subst1
                            subjects38.appendleft(tmp100)
                    if pattern_index == 2:
                        pass
                        # State 150931
                        if len(subjects38) >= 1 and subjects38[0] == Rational(-1, 2):
                            tmp101 = subjects38.popleft()
                            # State 150932
                            if len(subjects38) == 0:
                                pass
                                # State 150933
                                if len(subjects) == 0:
                                    pass
                                    # 69: 1/sqrt(f + x*g)
                                    yield 69, subst1
                            subjects38.appendleft(tmp101)
                subjects38.appendleft(tmp94)
            if len(subjects38) >= 1 and isinstance(subjects38[0], Pow):
                tmp102 = subjects38.popleft()
                subjects103 = deque(tmp102._args)
                # State 15243
                if len(subjects103) >= 1:
                    tmp104 = subjects103.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp104)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 15244
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.4.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 15245
                            if len(subjects103) >= 1:
                                tmp107 = subjects103.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.4.0', tmp107)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 15246
                                    if len(subjects103) == 0:
                                        pass
                                        # State 15247
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.4', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 15248
                                            if len(subjects38) == 0:
                                                pass
                                                # State 15249
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (F**(v*g))**n
                                                    yield 6, subst4
                                        if len(subjects38) >= 1:
                                            tmp110 = subjects38.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.4', tmp110)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 15248
                                                if len(subjects38) == 0:
                                                    pass
                                                    # State 15249
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (F**(v*g))**n
                                                        yield 6, subst4
                                            subjects38.appendleft(tmp110)
                                subjects103.appendleft(tmp107)
                        if len(subjects103) >= 1 and isinstance(subjects103[0], Mul):
                            tmp112 = subjects103.popleft()
                            associative1 = tmp112
                            associative_type1 = type(tmp112)
                            subjects113 = deque(tmp112._args)
                            matcher = CommutativeMatcher15251.get()
                            tmp114 = subjects113
                            subjects113 = []
                            for s in tmp114:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp114, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 15252
                                    if len(subjects103) == 0:
                                        pass
                                        # State 15253
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.4', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 15254
                                            if len(subjects38) == 0:
                                                pass
                                                # State 15255
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (F**(v*g))**n
                                                    yield 6, subst3
                                        if len(subjects38) >= 1:
                                            tmp116 = subjects38.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.4', tmp116)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 15254
                                                if len(subjects38) == 0:
                                                    pass
                                                    # State 15255
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (F**(v*g))**n
                                                        yield 6, subst3
                                            subjects38.appendleft(tmp116)
                            subjects103.appendleft(tmp112)
                    subjects103.appendleft(tmp104)
                if len(subjects103) >= 1:
                    tmp118 = subjects103.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2', tmp118)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 16061
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 16062
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 16063
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.4.1.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 16064
                                    if len(subjects103) >= 1:
                                        tmp123 = subjects103.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.4.1.1.0', tmp123)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 16065
                                            if len(subjects103) == 0:
                                                pass
                                                # State 16066
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16067
                                                    if len(subjects38) == 0:
                                                        pass
                                                        # State 16068
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 7: (F**(g*(e + x*f)))**n
                                                            yield 7, subst6
                                                if len(subjects38) >= 1:
                                                    tmp126 = subjects38.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.4', tmp126)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 16067
                                                        if len(subjects38) == 0:
                                                            pass
                                                            # State 16068
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 7: (F**(g*(e + x*f)))**n
                                                                yield 7, subst6
                                                    subjects38.appendleft(tmp126)
                                        subjects103.appendleft(tmp123)
                                if len(subjects103) >= 1 and isinstance(subjects103[0], Mul):
                                    tmp128 = subjects103.popleft()
                                    associative1 = tmp128
                                    associative_type1 = type(tmp128)
                                    subjects129 = deque(tmp128._args)
                                    matcher = CommutativeMatcher16070.get()
                                    tmp130 = subjects129
                                    subjects129 = []
                                    for s in tmp130:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp130, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 16071
                                            if len(subjects103) == 0:
                                                pass
                                                # State 16072
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16073
                                                    if len(subjects38) == 0:
                                                        pass
                                                        # State 16074
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 7: (F**(g*(e + x*f)))**n
                                                            yield 7, subst5
                                                if len(subjects38) >= 1:
                                                    tmp132 = subjects38.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.4', tmp132)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 16073
                                                        if len(subjects38) == 0:
                                                            pass
                                                            # State 16074
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 7: (F**(g*(e + x*f)))**n
                                                                yield 7, subst5
                                                    subjects38.appendleft(tmp132)
                                    subjects103.appendleft(tmp128)
                            if len(subjects103) >= 1 and isinstance(subjects103[0], Add):
                                tmp134 = subjects103.popleft()
                                associative1 = tmp134
                                associative_type1 = type(tmp134)
                                subjects135 = deque(tmp134._args)
                                matcher = CommutativeMatcher16076.get()
                                tmp136 = subjects135
                                subjects135 = []
                                for s in tmp136:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp136, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 16082
                                        if len(subjects103) == 0:
                                            pass
                                            # State 16083
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.4', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 16084
                                                if len(subjects38) == 0:
                                                    pass
                                                    # State 16085
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: (F**(g*(e + x*f)))**n
                                                        yield 7, subst4
                                            if len(subjects38) >= 1:
                                                tmp138 = subjects38.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.4', tmp138)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16084
                                                    if len(subjects38) == 0:
                                                        pass
                                                        # State 16085
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 7: (F**(g*(e + x*f)))**n
                                                            yield 7, subst4
                                                subjects38.appendleft(tmp138)
                                subjects103.appendleft(tmp134)
                        if len(subjects103) >= 1 and isinstance(subjects103[0], Mul):
                            tmp140 = subjects103.popleft()
                            associative1 = tmp140
                            associative_type1 = type(tmp140)
                            subjects141 = deque(tmp140._args)
                            matcher = CommutativeMatcher16087.get()
                            tmp142 = subjects141
                            subjects141 = []
                            for s in tmp142:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp142, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 16102
                                    if len(subjects103) == 0:
                                        pass
                                        # State 16103
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.4', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 16104
                                            if len(subjects38) == 0:
                                                pass
                                                # State 16105
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (F**(g*(e + x*f)))**n
                                                    yield 7, subst3
                                        if len(subjects38) >= 1:
                                            tmp144 = subjects38.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.4', tmp144)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 16104
                                                if len(subjects38) == 0:
                                                    pass
                                                    # State 16105
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: (F**(g*(e + x*f)))**n
                                                        yield 7, subst3
                                            subjects38.appendleft(tmp144)
                            subjects103.appendleft(tmp140)
                    subjects103.appendleft(tmp118)
                subjects38.appendleft(tmp102)
            if len(subjects38) >= 1 and isinstance(subjects38[0], tan):
                tmp146 = subjects38.popleft()
                subjects147 = deque(tmp146._args)
                # State 79232
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 79233
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 79234
                        if len(subjects147) >= 1:
                            tmp150 = subjects147.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp150)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 79235
                                if len(subjects147) == 0:
                                    pass
                                    # State 79236
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp152 = subjects38.popleft()
                                        # State 79237
                                        if len(subjects38) == 0:
                                            pass
                                            # State 79238
                                            if len(subjects) == 0:
                                                pass
                                                # 25: 1/tan(e + x*f)
                                                yield 25, subst3
                                        subjects38.appendleft(tmp152)
                            subjects147.appendleft(tmp150)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88303
                        if len(subjects147) >= 1 and isinstance(subjects147[0], Pow):
                            tmp154 = subjects147.popleft()
                            subjects155 = deque(tmp154._args)
                            # State 88304
                            if len(subjects155) >= 1:
                                tmp156 = subjects155.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.3.1.1', tmp156)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 88305
                                    if len(subjects155) >= 1:
                                        tmp158 = subjects155.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp158)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 88306
                                            if len(subjects155) == 0:
                                                pass
                                                # State 88307
                                                if len(subjects147) == 0:
                                                    pass
                                                    # State 88308
                                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                                        tmp160 = subjects38.popleft()
                                                        # State 88309
                                                        if len(subjects38) == 0:
                                                            pass
                                                            # State 88310
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 29: 1/tan(c + d*x**n)
                                                                yield 29, subst4
                                                        subjects38.appendleft(tmp160)
                                        subjects155.appendleft(tmp158)
                                subjects155.appendleft(tmp156)
                            subjects147.appendleft(tmp154)
                    if len(subjects147) >= 1 and isinstance(subjects147[0], Mul):
                        tmp161 = subjects147.popleft()
                        associative1 = tmp161
                        associative_type1 = type(tmp161)
                        subjects162 = deque(tmp161._args)
                        matcher = CommutativeMatcher79240.get()
                        tmp163 = subjects162
                        subjects162 = []
                        for s in tmp163:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp163, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 79241
                                if len(subjects147) == 0:
                                    pass
                                    # State 79242
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp164 = subjects38.popleft()
                                        # State 79243
                                        if len(subjects38) == 0:
                                            pass
                                            # State 79244
                                            if len(subjects) == 0:
                                                pass
                                                # 25: 1/tan(e + x*f)
                                                yield 25, subst2
                                        subjects38.appendleft(tmp164)
                            if pattern_index == 1:
                                pass
                                # State 88315
                                if len(subjects147) == 0:
                                    pass
                                    # State 88316
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp165 = subjects38.popleft()
                                        # State 88317
                                        if len(subjects38) == 0:
                                            pass
                                            # State 88318
                                            if len(subjects) == 0:
                                                pass
                                                # 29: 1/tan(c + d*x**n)
                                                yield 29, subst2
                                        subjects38.appendleft(tmp165)
                        subjects147.appendleft(tmp161)
                if len(subjects147) >= 1:
                    tmp166 = subjects147.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp166)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 86989
                        if len(subjects147) == 0:
                            pass
                            # State 86990
                            if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                tmp168 = subjects38.popleft()
                                # State 86991
                                if len(subjects38) == 0:
                                    pass
                                    # State 86992
                                    if len(subjects) == 0:
                                        pass
                                        # 27: 1/tan(v)
                                        yield 27, subst1
                                subjects38.appendleft(tmp168)
                    subjects147.appendleft(tmp166)
                if len(subjects147) >= 1 and isinstance(subjects147[0], Add):
                    tmp169 = subjects147.popleft()
                    associative1 = tmp169
                    associative_type1 = type(tmp169)
                    subjects170 = deque(tmp169._args)
                    matcher = CommutativeMatcher79246.get()
                    tmp171 = subjects170
                    subjects170 = []
                    for s in tmp171:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp171, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 79252
                            if len(subjects147) == 0:
                                pass
                                # State 79253
                                if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                    tmp172 = subjects38.popleft()
                                    # State 79254
                                    if len(subjects38) == 0:
                                        pass
                                        # State 79255
                                        if len(subjects) == 0:
                                            pass
                                            # 25: 1/tan(e + x*f)
                                            yield 25, subst1
                                    subjects38.appendleft(tmp172)
                        if pattern_index == 1:
                            pass
                            # State 88329
                            if len(subjects147) == 0:
                                pass
                                # State 88330
                                if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                    tmp173 = subjects38.popleft()
                                    # State 88331
                                    if len(subjects38) == 0:
                                        pass
                                        # State 88332
                                        if len(subjects) == 0:
                                            pass
                                            # 29: 1/tan(c + d*x**n)
                                            yield 29, subst1
                                    subjects38.appendleft(tmp173)
                    subjects147.appendleft(tmp169)
                subjects38.appendleft(tmp146)
            if len(subjects38) >= 1 and isinstance(subjects38[0], cos):
                tmp174 = subjects38.popleft()
                subjects175 = deque(tmp174._args)
                # State 93144
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 93145
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 93146
                        if len(subjects175) >= 1:
                            tmp178 = subjects175.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp178)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 93147
                                if len(subjects175) == 0:
                                    pass
                                    # State 93148
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp180 = subjects38.popleft()
                                        # State 93149
                                        if len(subjects38) == 0:
                                            pass
                                            # State 93150
                                            if len(subjects) == 0:
                                                pass
                                                # 30: 1/cos(e + x*f)
                                                yield 30, subst3
                                        subjects38.appendleft(tmp180)
                            subjects175.appendleft(tmp178)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98489
                        if len(subjects175) >= 1 and isinstance(subjects175[0], Pow):
                            tmp182 = subjects175.popleft()
                            subjects183 = deque(tmp182._args)
                            # State 98490
                            if len(subjects183) >= 1:
                                tmp184 = subjects183.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.3.1.1', tmp184)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 98491
                                    if len(subjects183) >= 1:
                                        tmp186 = subjects183.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp186)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 98492
                                            if len(subjects183) == 0:
                                                pass
                                                # State 98493
                                                if len(subjects175) == 0:
                                                    pass
                                                    # State 98494
                                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                                        tmp188 = subjects38.popleft()
                                                        # State 98495
                                                        if len(subjects38) == 0:
                                                            pass
                                                            # State 98496
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 34: 1/cos(c + d*x**n)
                                                                yield 34, subst4
                                                        subjects38.appendleft(tmp188)
                                        subjects183.appendleft(tmp186)
                                subjects183.appendleft(tmp184)
                            subjects175.appendleft(tmp182)
                    if len(subjects175) >= 1 and isinstance(subjects175[0], Mul):
                        tmp189 = subjects175.popleft()
                        associative1 = tmp189
                        associative_type1 = type(tmp189)
                        subjects190 = deque(tmp189._args)
                        matcher = CommutativeMatcher93152.get()
                        tmp191 = subjects190
                        subjects190 = []
                        for s in tmp191:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp191, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 93153
                                if len(subjects175) == 0:
                                    pass
                                    # State 93154
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp192 = subjects38.popleft()
                                        # State 93155
                                        if len(subjects38) == 0:
                                            pass
                                            # State 93156
                                            if len(subjects) == 0:
                                                pass
                                                # 30: 1/cos(e + x*f)
                                                yield 30, subst2
                                        subjects38.appendleft(tmp192)
                            if pattern_index == 1:
                                pass
                                # State 98501
                                if len(subjects175) == 0:
                                    pass
                                    # State 98502
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp193 = subjects38.popleft()
                                        # State 98503
                                        if len(subjects38) == 0:
                                            pass
                                            # State 98504
                                            if len(subjects) == 0:
                                                pass
                                                # 34: 1/cos(c + d*x**n)
                                                yield 34, subst2
                                        subjects38.appendleft(tmp193)
                        subjects175.appendleft(tmp189)
                if len(subjects175) >= 1:
                    tmp194 = subjects175.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp194)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 97343
                        if len(subjects175) == 0:
                            pass
                            # State 97344
                            if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                tmp196 = subjects38.popleft()
                                # State 97345
                                if len(subjects38) == 0:
                                    pass
                                    # State 97346
                                    if len(subjects) == 0:
                                        pass
                                        # 32: 1/cos(v)
                                        yield 32, subst1
                                subjects38.appendleft(tmp196)
                    subjects175.appendleft(tmp194)
                if len(subjects175) >= 1 and isinstance(subjects175[0], Add):
                    tmp197 = subjects175.popleft()
                    associative1 = tmp197
                    associative_type1 = type(tmp197)
                    subjects198 = deque(tmp197._args)
                    matcher = CommutativeMatcher93158.get()
                    tmp199 = subjects198
                    subjects198 = []
                    for s in tmp199:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp199, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 93164
                            if len(subjects175) == 0:
                                pass
                                # State 93165
                                if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                    tmp200 = subjects38.popleft()
                                    # State 93166
                                    if len(subjects38) == 0:
                                        pass
                                        # State 93167
                                        if len(subjects) == 0:
                                            pass
                                            # 30: 1/cos(e + x*f)
                                            yield 30, subst1
                                    subjects38.appendleft(tmp200)
                        if pattern_index == 1:
                            pass
                            # State 98515
                            if len(subjects175) == 0:
                                pass
                                # State 98516
                                if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                    tmp201 = subjects38.popleft()
                                    # State 98517
                                    if len(subjects38) == 0:
                                        pass
                                        # State 98518
                                        if len(subjects) == 0:
                                            pass
                                            # 34: 1/cos(c + d*x**n)
                                            yield 34, subst1
                                    subjects38.appendleft(tmp201)
                    subjects175.appendleft(tmp197)
                subjects38.appendleft(tmp174)
            if len(subjects38) >= 1 and isinstance(subjects38[0], sin):
                tmp202 = subjects38.popleft()
                subjects203 = deque(tmp202._args)
                # State 93330
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 93331
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 93332
                        if len(subjects203) >= 1:
                            tmp206 = subjects203.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp206)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 93333
                                if len(subjects203) == 0:
                                    pass
                                    # State 93334
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp208 = subjects38.popleft()
                                        # State 93335
                                        if len(subjects38) == 0:
                                            pass
                                            # State 93336
                                            if len(subjects) == 0:
                                                pass
                                                # 31: 1/sin(e + x*f)
                                                yield 31, subst3
                                        subjects38.appendleft(tmp208)
                            subjects203.appendleft(tmp206)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98748
                        if len(subjects203) >= 1 and isinstance(subjects203[0], Pow):
                            tmp210 = subjects203.popleft()
                            subjects211 = deque(tmp210._args)
                            # State 98749
                            if len(subjects211) >= 1:
                                tmp212 = subjects211.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.3.1.1', tmp212)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 98750
                                    if len(subjects211) >= 1:
                                        tmp214 = subjects211.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp214)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 98751
                                            if len(subjects211) == 0:
                                                pass
                                                # State 98752
                                                if len(subjects203) == 0:
                                                    pass
                                                    # State 98753
                                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                                        tmp216 = subjects38.popleft()
                                                        # State 98754
                                                        if len(subjects38) == 0:
                                                            pass
                                                            # State 98755
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 35: 1/sin(c + d*x**n)
                                                                yield 35, subst4
                                                        subjects38.appendleft(tmp216)
                                        subjects211.appendleft(tmp214)
                                subjects211.appendleft(tmp212)
                            subjects203.appendleft(tmp210)
                    if len(subjects203) >= 1 and isinstance(subjects203[0], Mul):
                        tmp217 = subjects203.popleft()
                        associative1 = tmp217
                        associative_type1 = type(tmp217)
                        subjects218 = deque(tmp217._args)
                        matcher = CommutativeMatcher93338.get()
                        tmp219 = subjects218
                        subjects218 = []
                        for s in tmp219:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp219, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 93339
                                if len(subjects203) == 0:
                                    pass
                                    # State 93340
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp220 = subjects38.popleft()
                                        # State 93341
                                        if len(subjects38) == 0:
                                            pass
                                            # State 93342
                                            if len(subjects) == 0:
                                                pass
                                                # 31: 1/sin(e + x*f)
                                                yield 31, subst2
                                        subjects38.appendleft(tmp220)
                            if pattern_index == 1:
                                pass
                                # State 98760
                                if len(subjects203) == 0:
                                    pass
                                    # State 98761
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp221 = subjects38.popleft()
                                        # State 98762
                                        if len(subjects38) == 0:
                                            pass
                                            # State 98763
                                            if len(subjects) == 0:
                                                pass
                                                # 35: 1/sin(c + d*x**n)
                                                yield 35, subst2
                                        subjects38.appendleft(tmp221)
                        subjects203.appendleft(tmp217)
                if len(subjects203) >= 1:
                    tmp222 = subjects203.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp222)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 97390
                        if len(subjects203) == 0:
                            pass
                            # State 97391
                            if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                tmp224 = subjects38.popleft()
                                # State 97392
                                if len(subjects38) == 0:
                                    pass
                                    # State 97393
                                    if len(subjects) == 0:
                                        pass
                                        # 33: 1/sin(v)
                                        yield 33, subst1
                                subjects38.appendleft(tmp224)
                    subjects203.appendleft(tmp222)
                if len(subjects203) >= 1 and isinstance(subjects203[0], Add):
                    tmp225 = subjects203.popleft()
                    associative1 = tmp225
                    associative_type1 = type(tmp225)
                    subjects226 = deque(tmp225._args)
                    matcher = CommutativeMatcher93344.get()
                    tmp227 = subjects226
                    subjects226 = []
                    for s in tmp227:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp227, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 93350
                            if len(subjects203) == 0:
                                pass
                                # State 93351
                                if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                    tmp228 = subjects38.popleft()
                                    # State 93352
                                    if len(subjects38) == 0:
                                        pass
                                        # State 93353
                                        if len(subjects) == 0:
                                            pass
                                            # 31: 1/sin(e + x*f)
                                            yield 31, subst1
                                    subjects38.appendleft(tmp228)
                        if pattern_index == 1:
                            pass
                            # State 98774
                            if len(subjects203) == 0:
                                pass
                                # State 98775
                                if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                    tmp229 = subjects38.popleft()
                                    # State 98776
                                    if len(subjects38) == 0:
                                        pass
                                        # State 98777
                                        if len(subjects) == 0:
                                            pass
                                            # 35: 1/sin(c + d*x**n)
                                            yield 35, subst1
                                    subjects38.appendleft(tmp229)
                    subjects203.appendleft(tmp225)
                subjects38.appendleft(tmp202)
            if len(subjects38) >= 1 and isinstance(subjects38[0], tanh):
                tmp230 = subjects38.popleft()
                subjects231 = deque(tmp230._args)
                # State 126313
                if len(subjects231) >= 1:
                    tmp232 = subjects231.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp232)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 126314
                        if len(subjects231) == 0:
                            pass
                            # State 126315
                            if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                tmp234 = subjects38.popleft()
                                # State 126316
                                if len(subjects38) == 0:
                                    pass
                                    # State 126317
                                    if len(subjects) == 0:
                                        pass
                                        # 52: 1/tanh(v)
                                        yield 52, subst1
                                subjects38.appendleft(tmp234)
                    subjects231.appendleft(tmp232)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 126502
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 126503
                        if len(subjects231) >= 1:
                            tmp237 = subjects231.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp237)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 126504
                                if len(subjects231) == 0:
                                    pass
                                    # State 126505
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp239 = subjects38.popleft()
                                        # State 126506
                                        if len(subjects38) == 0:
                                            pass
                                            # State 126507
                                            if len(subjects) == 0:
                                                pass
                                                # 53: 1/tanh(e + x*f)
                                                yield 53, subst3
                                        subjects38.appendleft(tmp239)
                            subjects231.appendleft(tmp237)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 127840
                        if len(subjects231) >= 1 and isinstance(subjects231[0], Pow):
                            tmp241 = subjects231.popleft()
                            subjects242 = deque(tmp241._args)
                            # State 127841
                            if len(subjects242) >= 1:
                                tmp243 = subjects242.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.3.1.1', tmp243)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 127842
                                    if len(subjects242) >= 1:
                                        tmp245 = subjects242.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp245)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 127843
                                            if len(subjects242) == 0:
                                                pass
                                                # State 127844
                                                if len(subjects231) == 0:
                                                    pass
                                                    # State 127845
                                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                                        tmp247 = subjects38.popleft()
                                                        # State 127846
                                                        if len(subjects38) == 0:
                                                            pass
                                                            # State 127847
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 55: 1/tanh(c + d*x**n)
                                                                yield 55, subst4
                                                        subjects38.appendleft(tmp247)
                                        subjects242.appendleft(tmp245)
                                subjects242.appendleft(tmp243)
                            subjects231.appendleft(tmp241)
                    if len(subjects231) >= 1 and isinstance(subjects231[0], Mul):
                        tmp248 = subjects231.popleft()
                        associative1 = tmp248
                        associative_type1 = type(tmp248)
                        subjects249 = deque(tmp248._args)
                        matcher = CommutativeMatcher126509.get()
                        tmp250 = subjects249
                        subjects249 = []
                        for s in tmp250:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp250, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 126510
                                if len(subjects231) == 0:
                                    pass
                                    # State 126511
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp251 = subjects38.popleft()
                                        # State 126512
                                        if len(subjects38) == 0:
                                            pass
                                            # State 126513
                                            if len(subjects) == 0:
                                                pass
                                                # 53: 1/tanh(e + x*f)
                                                yield 53, subst2
                                        subjects38.appendleft(tmp251)
                            if pattern_index == 1:
                                pass
                                # State 127852
                                if len(subjects231) == 0:
                                    pass
                                    # State 127853
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp252 = subjects38.popleft()
                                        # State 127854
                                        if len(subjects38) == 0:
                                            pass
                                            # State 127855
                                            if len(subjects) == 0:
                                                pass
                                                # 55: 1/tanh(c + d*x**n)
                                                yield 55, subst2
                                        subjects38.appendleft(tmp252)
                        subjects231.appendleft(tmp248)
                if len(subjects231) >= 1 and isinstance(subjects231[0], Add):
                    tmp253 = subjects231.popleft()
                    associative1 = tmp253
                    associative_type1 = type(tmp253)
                    subjects254 = deque(tmp253._args)
                    matcher = CommutativeMatcher126515.get()
                    tmp255 = subjects254
                    subjects254 = []
                    for s in tmp255:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp255, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 126521
                            if len(subjects231) == 0:
                                pass
                                # State 126522
                                if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                    tmp256 = subjects38.popleft()
                                    # State 126523
                                    if len(subjects38) == 0:
                                        pass
                                        # State 126524
                                        if len(subjects) == 0:
                                            pass
                                            # 53: 1/tanh(e + x*f)
                                            yield 53, subst1
                                    subjects38.appendleft(tmp256)
                        if pattern_index == 1:
                            pass
                            # State 127866
                            if len(subjects231) == 0:
                                pass
                                # State 127867
                                if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                    tmp257 = subjects38.popleft()
                                    # State 127868
                                    if len(subjects38) == 0:
                                        pass
                                        # State 127869
                                        if len(subjects) == 0:
                                            pass
                                            # 55: 1/tanh(c + d*x**n)
                                            yield 55, subst1
                                    subjects38.appendleft(tmp257)
                    subjects231.appendleft(tmp253)
                subjects38.appendleft(tmp230)
            if len(subjects38) >= 1 and isinstance(subjects38[0], cosh):
                tmp258 = subjects38.popleft()
                subjects259 = deque(tmp258._args)
                # State 130762
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 130763
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130764
                        if len(subjects259) >= 1 and isinstance(subjects259[0], Pow):
                            tmp262 = subjects259.popleft()
                            subjects263 = deque(tmp262._args)
                            # State 130765
                            if len(subjects263) >= 1:
                                tmp264 = subjects263.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.3.1.1', tmp264)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 130766
                                    if len(subjects263) >= 1:
                                        tmp266 = subjects263.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp266)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 130767
                                            if len(subjects263) == 0:
                                                pass
                                                # State 130768
                                                if len(subjects259) == 0:
                                                    pass
                                                    # State 130769
                                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                                        tmp268 = subjects38.popleft()
                                                        # State 130770
                                                        if len(subjects38) == 0:
                                                            pass
                                                            # State 130771
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 56: 1/cosh(c + d*x**n)
                                                                yield 56, subst4
                                                        subjects38.appendleft(tmp268)
                                        subjects263.appendleft(tmp266)
                                subjects263.appendleft(tmp264)
                            subjects259.appendleft(tmp262)
                    if len(subjects259) >= 1 and isinstance(subjects259[0], Mul):
                        tmp269 = subjects259.popleft()
                        associative1 = tmp269
                        associative_type1 = type(tmp269)
                        subjects270 = deque(tmp269._args)
                        matcher = CommutativeMatcher130773.get()
                        tmp271 = subjects270
                        subjects270 = []
                        for s in tmp271:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp271, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 130778
                                if len(subjects259) == 0:
                                    pass
                                    # State 130779
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp272 = subjects38.popleft()
                                        # State 130780
                                        if len(subjects38) == 0:
                                            pass
                                            # State 130781
                                            if len(subjects) == 0:
                                                pass
                                                # 56: 1/cosh(c + d*x**n)
                                                yield 56, subst2
                                        subjects38.appendleft(tmp272)
                        subjects259.appendleft(tmp269)
                if len(subjects259) >= 1 and isinstance(subjects259[0], Add):
                    tmp273 = subjects259.popleft()
                    associative1 = tmp273
                    associative_type1 = type(tmp273)
                    subjects274 = deque(tmp273._args)
                    matcher = CommutativeMatcher130783.get()
                    tmp275 = subjects274
                    subjects274 = []
                    for s in tmp275:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp275, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 130796
                            if len(subjects259) == 0:
                                pass
                                # State 130797
                                if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                    tmp276 = subjects38.popleft()
                                    # State 130798
                                    if len(subjects38) == 0:
                                        pass
                                        # State 130799
                                        if len(subjects) == 0:
                                            pass
                                            # 56: 1/cosh(c + d*x**n)
                                            yield 56, subst1
                                    subjects38.appendleft(tmp276)
                    subjects259.appendleft(tmp273)
                subjects38.appendleft(tmp258)
            if len(subjects38) >= 1 and isinstance(subjects38[0], sinh):
                tmp277 = subjects38.popleft()
                subjects278 = deque(tmp277._args)
                # State 131053
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 131054
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131055
                        if len(subjects278) >= 1 and isinstance(subjects278[0], Pow):
                            tmp281 = subjects278.popleft()
                            subjects282 = deque(tmp281._args)
                            # State 131056
                            if len(subjects282) >= 1:
                                tmp283 = subjects282.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.3.1.1', tmp283)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 131057
                                    if len(subjects282) >= 1:
                                        tmp285 = subjects282.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp285)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 131058
                                            if len(subjects282) == 0:
                                                pass
                                                # State 131059
                                                if len(subjects278) == 0:
                                                    pass
                                                    # State 131060
                                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                                        tmp287 = subjects38.popleft()
                                                        # State 131061
                                                        if len(subjects38) == 0:
                                                            pass
                                                            # State 131062
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 57: 1/sinh(c + d*x**n)
                                                                yield 57, subst4
                                                        subjects38.appendleft(tmp287)
                                        subjects282.appendleft(tmp285)
                                subjects282.appendleft(tmp283)
                            subjects278.appendleft(tmp281)
                    if len(subjects278) >= 1 and isinstance(subjects278[0], Mul):
                        tmp288 = subjects278.popleft()
                        associative1 = tmp288
                        associative_type1 = type(tmp288)
                        subjects289 = deque(tmp288._args)
                        matcher = CommutativeMatcher131064.get()
                        tmp290 = subjects289
                        subjects289 = []
                        for s in tmp290:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp290, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 131069
                                if len(subjects278) == 0:
                                    pass
                                    # State 131070
                                    if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                        tmp291 = subjects38.popleft()
                                        # State 131071
                                        if len(subjects38) == 0:
                                            pass
                                            # State 131072
                                            if len(subjects) == 0:
                                                pass
                                                # 57: 1/sinh(c + d*x**n)
                                                yield 57, subst2
                                        subjects38.appendleft(tmp291)
                        subjects278.appendleft(tmp288)
                if len(subjects278) >= 1 and isinstance(subjects278[0], Add):
                    tmp292 = subjects278.popleft()
                    associative1 = tmp292
                    associative_type1 = type(tmp292)
                    subjects293 = deque(tmp292._args)
                    matcher = CommutativeMatcher131074.get()
                    tmp294 = subjects293
                    subjects293 = []
                    for s in tmp294:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp294, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 131087
                            if len(subjects278) == 0:
                                pass
                                # State 131088
                                if len(subjects38) >= 1 and subjects38[0] == Integer(-1):
                                    tmp295 = subjects38.popleft()
                                    # State 131089
                                    if len(subjects38) == 0:
                                        pass
                                        # State 131090
                                        if len(subjects) == 0:
                                            pass
                                            # 57: 1/sinh(c + d*x**n)
                                            yield 57, subst1
                                    subjects38.appendleft(tmp295)
                    subjects278.appendleft(tmp292)
                subjects38.appendleft(tmp277)
            subjects.appendleft(tmp37)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp296 = subjects.popleft()
            subjects297 = deque(tmp296._args)
            # State 21097
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 21098
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 21099
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 21100
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21101
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 21102
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21103
                                    if len(subjects297) >= 1:
                                        tmp304 = subjects297.popleft()
                                        subst7 = Substitution(subst6)
                                        try:
                                            subst7.try_add_variable('i2.2.1.2.2.2.1.0', tmp304)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21104
                                            if len(subjects297) == 0:
                                                pass
                                                # State 21105
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: log(c*(d*(e + x*f)**p)**q)
                                                    yield 8, subst7
                                        subjects297.appendleft(tmp304)
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35129
                                    if len(subjects297) >= 1 and isinstance(subjects297[0], Pow):
                                        tmp307 = subjects297.popleft()
                                        subjects308 = deque(tmp307._args)
                                        # State 35130
                                        if len(subjects308) >= 1:
                                            tmp309 = subjects308.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2.2.1.1', tmp309)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35131
                                                if len(subjects308) >= 1:
                                                    tmp311 = subjects308.popleft()
                                                    subst8 = Substitution(subst7)
                                                    try:
                                                        subst8.try_add_variable('i2.2.1.2.2.2.1.2', tmp311)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35132
                                                        if len(subjects308) == 0:
                                                            pass
                                                            # State 35133
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 35134
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                    yield 13, subst8
                                                    subjects308.appendleft(tmp311)
                                            subjects308.appendleft(tmp309)
                                        subjects297.appendleft(tmp307)
                                if len(subjects297) >= 1 and isinstance(subjects297[0], Mul):
                                    tmp313 = subjects297.popleft()
                                    associative1 = tmp313
                                    associative_type1 = type(tmp313)
                                    subjects314 = deque(tmp313._args)
                                    matcher = CommutativeMatcher21107.get()
                                    tmp315 = subjects314
                                    subjects314 = []
                                    for s in tmp315:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp315, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 21108
                                            if len(subjects297) == 0:
                                                pass
                                                # State 21109
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: log(c*(d*(e + x*f)**p)**q)
                                                    yield 8, subst6
                                        if pattern_index == 1:
                                            pass
                                            # State 35139
                                            if len(subjects297) == 0:
                                                pass
                                                # State 35140
                                                if len(subjects) == 0:
                                                    pass
                                                    # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                    yield 13, subst6
                                    subjects297.appendleft(tmp313)
                            if len(subjects297) >= 1:
                                tmp316 = subjects297.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.1', tmp316)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45651
                                    if len(subjects297) == 0:
                                        pass
                                        # State 45652
                                        if len(subjects) == 0:
                                            pass
                                            # 15: log(c*(d*v**p)**q)
                                            yield 15, subst5
                                subjects297.appendleft(tmp316)
                            if len(subjects297) >= 1 and isinstance(subjects297[0], Add):
                                tmp318 = subjects297.popleft()
                                associative1 = tmp318
                                associative_type1 = type(tmp318)
                                subjects319 = deque(tmp318._args)
                                matcher = CommutativeMatcher21111.get()
                                tmp320 = subjects319
                                subjects319 = []
                                for s in tmp320:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp320, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 21117
                                        if len(subjects297) == 0:
                                            pass
                                            # State 21118
                                            if len(subjects) == 0:
                                                pass
                                                # 8: log(c*(d*(e + x*f)**p)**q)
                                                yield 8, subst5
                                    if pattern_index == 1:
                                        pass
                                        # State 29407
                                        if len(subjects297) == 0:
                                            pass
                                            # State 29408
                                            if len(subjects) == 0:
                                                pass
                                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                yield 11, subst5
                                    if pattern_index == 2:
                                        pass
                                        # State 35141
                                        if len(subjects297) == 0:
                                            pass
                                            # State 35142
                                            if len(subjects) == 0:
                                                pass
                                                # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                yield 13, subst5
                                    if pattern_index == 3:
                                        pass
                                        # State 44379
                                        if len(subjects297) == 0:
                                            pass
                                            # State 44380
                                            if len(subjects) == 0:
                                                pass
                                                # 14: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                yield 14, subst5
                                subjects297.appendleft(tmp318)
                            if len(subjects297) >= 1 and isinstance(subjects297[0], Mul):
                                tmp321 = subjects297.popleft()
                                associative1 = tmp321
                                associative_type1 = type(tmp321)
                                subjects322 = deque(tmp321._args)
                                matcher = CommutativeMatcher32356.get()
                                tmp323 = subjects322
                                subjects322 = []
                                for s in tmp323:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp323, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 32380
                                        if len(subjects297) == 0:
                                            pass
                                            # State 32381
                                            if len(subjects) == 0:
                                                pass
                                                # 12: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                yield 12, subst5
                                subjects297.appendleft(tmp321)
                        if len(subjects297) >= 1 and isinstance(subjects297[0], Pow):
                            tmp324 = subjects297.popleft()
                            subjects325 = deque(tmp324._args)
                            # State 21119
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 21120
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21121
                                    if len(subjects325) >= 1:
                                        tmp328 = subjects325.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp328)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21122
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21123
                                                if len(subjects325) == 0:
                                                    pass
                                                    # State 21124
                                                    if len(subjects297) == 0:
                                                        pass
                                                        # State 21125
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 8: log(c*(d*(e + x*f)**p)**q)
                                                            yield 8, subst7
                                            if len(subjects325) >= 1:
                                                tmp331 = subjects325.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.2.2.2', tmp331)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21123
                                                    if len(subjects325) == 0:
                                                        pass
                                                        # State 21124
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 21125
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + x*f)**p)**q)
                                                                yield 8, subst7
                                                subjects325.appendleft(tmp331)
                                        subjects325.appendleft(tmp328)
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35143
                                    if len(subjects325) >= 1 and isinstance(subjects325[0], Pow):
                                        tmp334 = subjects325.popleft()
                                        subjects335 = deque(tmp334._args)
                                        # State 35144
                                        if len(subjects335) >= 1:
                                            tmp336 = subjects335.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.1', tmp336)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35145
                                                if len(subjects335) >= 1:
                                                    tmp338 = subjects335.popleft()
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2.2.1.2', tmp338)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35146
                                                        if len(subjects335) == 0:
                                                            pass
                                                            # State 35147
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i2.2.1.2.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 35148
                                                                if len(subjects325) == 0:
                                                                    pass
                                                                    # State 35149
                                                                    if len(subjects297) == 0:
                                                                        pass
                                                                        # State 35150
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                            yield 13, subst8
                                                            if len(subjects325) >= 1:
                                                                tmp341 = subjects325.popleft()
                                                                subst8 = Substitution(subst7)
                                                                try:
                                                                    subst8.try_add_variable('i2.2.1.2.2.2', tmp341)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 35148
                                                                    if len(subjects325) == 0:
                                                                        pass
                                                                        # State 35149
                                                                        if len(subjects297) == 0:
                                                                            pass
                                                                            # State 35150
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                                yield 13, subst8
                                                                subjects325.appendleft(tmp341)
                                                    subjects335.appendleft(tmp338)
                                            subjects335.appendleft(tmp336)
                                        subjects325.appendleft(tmp334)
                                if len(subjects325) >= 1 and isinstance(subjects325[0], Mul):
                                    tmp343 = subjects325.popleft()
                                    associative1 = tmp343
                                    associative_type1 = type(tmp343)
                                    subjects344 = deque(tmp343._args)
                                    matcher = CommutativeMatcher21127.get()
                                    tmp345 = subjects344
                                    subjects344 = []
                                    for s in tmp345:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp345, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 21128
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21129
                                                if len(subjects325) == 0:
                                                    pass
                                                    # State 21130
                                                    if len(subjects297) == 0:
                                                        pass
                                                        # State 21131
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 8: log(c*(d*(e + x*f)**p)**q)
                                                            yield 8, subst6
                                            if len(subjects325) >= 1:
                                                tmp347 = []
                                                tmp347.append(subjects325.popleft())
                                                while True:
                                                    if len(tmp347) > 1:
                                                        tmp348 = create_operation_expression(associative1, tmp347)
                                                    elif len(tmp347) == 1:
                                                        tmp348 = tmp347[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', tmp348)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 21129
                                                        if len(subjects325) == 0:
                                                            pass
                                                            # State 21130
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 21131
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 8, subst6
                                                    if len(subjects325) == 0:
                                                        break
                                                    tmp347.append(subjects325.popleft())
                                                subjects325.extendleft(reversed(tmp347))
                                        if pattern_index == 1:
                                            pass
                                            # State 35155
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35156
                                                if len(subjects325) == 0:
                                                    pass
                                                    # State 35157
                                                    if len(subjects297) == 0:
                                                        pass
                                                        # State 35158
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                            yield 13, subst6
                                            if len(subjects325) >= 1:
                                                tmp351 = []
                                                tmp351.append(subjects325.popleft())
                                                while True:
                                                    if len(tmp351) > 1:
                                                        tmp352 = create_operation_expression(associative1, tmp351)
                                                    elif len(tmp351) == 1:
                                                        tmp352 = tmp351[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', tmp352)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35156
                                                        if len(subjects325) == 0:
                                                            pass
                                                            # State 35157
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 35158
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                    yield 13, subst6
                                                    if len(subjects325) == 0:
                                                        break
                                                    tmp351.append(subjects325.popleft())
                                                subjects325.extendleft(reversed(tmp351))
                                    subjects325.appendleft(tmp343)
                            if len(subjects325) >= 1:
                                tmp354 = subjects325.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.1', tmp354)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25711
                                    if len(subjects325) >= 1:
                                        tmp356 = subjects325.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp356)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25712
                                            if len(subjects325) == 0:
                                                pass
                                                # State 25713
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 25714
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 9: log(c*(d*v**p)**q)
                                                        yield 9, subst5
                                        subjects325.appendleft(tmp356)
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45653
                                        if len(subjects325) == 0:
                                            pass
                                            # State 45654
                                            if len(subjects297) == 0:
                                                pass
                                                # State 45655
                                                if len(subjects) == 0:
                                                    pass
                                                    # 15: log(c*(d*v**p)**q)
                                                    yield 15, subst5
                                    if len(subjects325) >= 1:
                                        tmp359 = subjects325.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp359)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45653
                                            if len(subjects325) == 0:
                                                pass
                                                # State 45654
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 45655
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 15: log(c*(d*v**p)**q)
                                                        yield 15, subst5
                                        subjects325.appendleft(tmp359)
                                subjects325.appendleft(tmp354)
                            if len(subjects325) >= 1 and isinstance(subjects325[0], Add):
                                tmp361 = subjects325.popleft()
                                associative1 = tmp361
                                associative_type1 = type(tmp361)
                                subjects362 = deque(tmp361._args)
                                matcher = CommutativeMatcher21133.get()
                                tmp363 = subjects362
                                subjects362 = []
                                for s in tmp363:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp363, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 21139
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21140
                                            if len(subjects325) == 0:
                                                pass
                                                # State 21141
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 21142
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 8: log(c*(d*(e + x*f)**p)**q)
                                                        yield 8, subst5
                                        if len(subjects325) >= 1:
                                            tmp365 = []
                                            tmp365.append(subjects325.popleft())
                                            while True:
                                                if len(tmp365) > 1:
                                                    tmp366 = create_operation_expression(associative1, tmp365)
                                                elif len(tmp365) == 1:
                                                    tmp366 = tmp365[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp366)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21140
                                                    if len(subjects325) == 0:
                                                        pass
                                                        # State 21141
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 21142
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + x*f)**p)**q)
                                                                yield 8, subst5
                                                if len(subjects325) == 0:
                                                    break
                                                tmp365.append(subjects325.popleft())
                                            subjects325.extendleft(reversed(tmp365))
                                    if pattern_index == 1:
                                        pass
                                        # State 29419
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 29420
                                            if len(subjects325) == 0:
                                                pass
                                                # State 29421
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 29422
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                        yield 11, subst5
                                        if len(subjects325) >= 1:
                                            tmp369 = []
                                            tmp369.append(subjects325.popleft())
                                            while True:
                                                if len(tmp369) > 1:
                                                    tmp370 = create_operation_expression(associative1, tmp369)
                                                elif len(tmp369) == 1:
                                                    tmp370 = tmp369[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp370)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 29420
                                                    if len(subjects325) == 0:
                                                        pass
                                                        # State 29421
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 29422
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                yield 11, subst5
                                                if len(subjects325) == 0:
                                                    break
                                                tmp369.append(subjects325.popleft())
                                            subjects325.extendleft(reversed(tmp369))
                                    if pattern_index == 2:
                                        pass
                                        # State 35159
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35160
                                            if len(subjects325) == 0:
                                                pass
                                                # State 35161
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 35162
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                        yield 13, subst5
                                        if len(subjects325) >= 1:
                                            tmp373 = []
                                            tmp373.append(subjects325.popleft())
                                            while True:
                                                if len(tmp373) > 1:
                                                    tmp374 = create_operation_expression(associative1, tmp373)
                                                elif len(tmp373) == 1:
                                                    tmp374 = tmp373[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp374)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 35160
                                                    if len(subjects325) == 0:
                                                        pass
                                                        # State 35161
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 35162
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                yield 13, subst5
                                                if len(subjects325) == 0:
                                                    break
                                                tmp373.append(subjects325.popleft())
                                            subjects325.extendleft(reversed(tmp373))
                                    if pattern_index == 3:
                                        pass
                                        # State 44388
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44389
                                            if len(subjects325) == 0:
                                                pass
                                                # State 44390
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 44391
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 14: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                        yield 14, subst5
                                        if len(subjects325) >= 1:
                                            tmp377 = []
                                            tmp377.append(subjects325.popleft())
                                            while True:
                                                if len(tmp377) > 1:
                                                    tmp378 = create_operation_expression(associative1, tmp377)
                                                elif len(tmp377) == 1:
                                                    tmp378 = tmp377[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp378)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 44389
                                                    if len(subjects325) == 0:
                                                        pass
                                                        # State 44390
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 44391
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 14: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                                yield 14, subst5
                                                if len(subjects325) == 0:
                                                    break
                                                tmp377.append(subjects325.popleft())
                                            subjects325.extendleft(reversed(tmp377))
                                subjects325.appendleft(tmp361)
                            if len(subjects325) >= 1 and isinstance(subjects325[0], Mul):
                                tmp380 = subjects325.popleft()
                                associative1 = tmp380
                                associative_type1 = type(tmp380)
                                subjects381 = deque(tmp380._args)
                                matcher = CommutativeMatcher32383.get()
                                tmp382 = subjects381
                                subjects381 = []
                                for s in tmp382:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp382, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 32407
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 32408
                                            if len(subjects325) == 0:
                                                pass
                                                # State 32409
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 32410
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 12: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                        yield 12, subst5
                                        if len(subjects325) >= 1:
                                            tmp384 = []
                                            tmp384.append(subjects325.popleft())
                                            while True:
                                                if len(tmp384) > 1:
                                                    tmp385 = create_operation_expression(associative1, tmp384)
                                                elif len(tmp384) == 1:
                                                    tmp385 = tmp384[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp385)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 32408
                                                    if len(subjects325) == 0:
                                                        pass
                                                        # State 32409
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 32410
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 12: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                                yield 12, subst5
                                                if len(subjects325) == 0:
                                                    break
                                                tmp384.append(subjects325.popleft())
                                            subjects325.extendleft(reversed(tmp384))
                                subjects325.appendleft(tmp380)
                            subjects297.appendleft(tmp324)
                    if len(subjects297) >= 1:
                        tmp387 = subjects297.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1', tmp387)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53282
                            if len(subjects297) == 0:
                                pass
                                # State 53283
                                if len(subjects) == 0:
                                    pass
                                    # 17: log(c*RFx**p)
                                    yield 17, subst3
                        subjects297.appendleft(tmp387)
                    if len(subjects297) >= 1 and isinstance(subjects297[0], Mul):
                        tmp389 = subjects297.popleft()
                        associative1 = tmp389
                        associative_type1 = type(tmp389)
                        subjects390 = deque(tmp389._args)
                        matcher = CommutativeMatcher21144.get()
                        tmp391 = subjects390
                        subjects390 = []
                        for s in tmp391:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp391, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 21181
                                if len(subjects297) == 0:
                                    pass
                                    # State 21182
                                    if len(subjects) == 0:
                                        pass
                                        # 8: log(c*(d*(e + x*f)**p)**q)
                                        yield 8, subst3
                            if pattern_index == 1:
                                pass
                                # State 25718
                                if len(subjects297) == 0:
                                    pass
                                    # State 25719
                                    if len(subjects) == 0:
                                        pass
                                        # 9: log(c*(d*v**p)**q)
                                        yield 9, subst3
                            if pattern_index == 2:
                                pass
                                # State 29447
                                if len(subjects297) == 0:
                                    pass
                                    # State 29448
                                    if len(subjects) == 0:
                                        pass
                                        # 11: log(c*(d*(e + f*x**m)**p)**q)
                                        yield 11, subst3
                            if pattern_index == 3:
                                pass
                                # State 32465
                                if len(subjects297) == 0:
                                    pass
                                    # State 32466
                                    if len(subjects) == 0:
                                        pass
                                        # 12: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                        yield 12, subst3
                            if pattern_index == 4:
                                pass
                                # State 35191
                                if len(subjects297) == 0:
                                    pass
                                    # State 35192
                                    if len(subjects) == 0:
                                        pass
                                        # 13: log(c*(d*(e + f*x**m)**p)**q)
                                        yield 13, subst3
                            if pattern_index == 5:
                                pass
                                # State 44410
                                if len(subjects297) == 0:
                                    pass
                                    # State 44411
                                    if len(subjects) == 0:
                                        pass
                                        # 14: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                        yield 14, subst3
                            if pattern_index == 6:
                                pass
                                # State 45659
                                if len(subjects297) == 0:
                                    pass
                                    # State 45660
                                    if len(subjects) == 0:
                                        pass
                                        # 15: log(c*(d*v**p)**q)
                                        yield 15, subst3
                        subjects297.appendleft(tmp389)
                    if len(subjects297) >= 1 and isinstance(subjects297[0], Add):
                        tmp392 = subjects297.popleft()
                        associative1 = tmp392
                        associative_type1 = type(tmp392)
                        subjects393 = deque(tmp392._args)
                        matcher = CommutativeMatcher50884.get()
                        tmp394 = subjects393
                        subjects393 = []
                        for s in tmp394:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp394, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 50897
                                if len(subjects297) == 0:
                                    pass
                                    # State 50898
                                    if len(subjects) == 0:
                                        pass
                                        # 16: log(c*(d + e*x**2)**p)
                                        yield 16, subst3
                        subjects297.appendleft(tmp392)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 26175
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 26176
                        if len(subjects297) >= 1:
                            tmp397 = subjects297.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.1.1.0', tmp397)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 26177
                                if len(subjects297) == 0:
                                    pass
                                    # State 26178
                                    if len(subjects) == 0:
                                        pass
                                        # 10: log(c*(e + x*f))
                                        yield 10, subst4
                            subjects297.appendleft(tmp397)
                    if len(subjects297) >= 1 and isinstance(subjects297[0], Mul):
                        tmp399 = subjects297.popleft()
                        associative1 = tmp399
                        associative_type1 = type(tmp399)
                        subjects400 = deque(tmp399._args)
                        matcher = CommutativeMatcher26180.get()
                        tmp401 = subjects400
                        subjects400 = []
                        for s in tmp401:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp401, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 26181
                                if len(subjects297) == 0:
                                    pass
                                    # State 26182
                                    if len(subjects) == 0:
                                        pass
                                        # 10: log(c*(e + x*f))
                                        yield 10, subst3
                        subjects297.appendleft(tmp399)
                if len(subjects297) >= 1 and isinstance(subjects297[0], Pow):
                    tmp402 = subjects297.popleft()
                    subjects403 = deque(tmp402._args)
                    # State 21183
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 21184
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21185
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 21186
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21187
                                    if len(subjects403) >= 1:
                                        tmp408 = subjects403.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp408)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21188
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21189
                                                if len(subjects403) == 0:
                                                    pass
                                                    # State 21190
                                                    if len(subjects297) == 0:
                                                        pass
                                                        # State 21191
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 8: log(c*(d*(e + x*f)**p)**q)
                                                            yield 8, subst7
                                            if len(subjects403) >= 1:
                                                tmp411 = subjects403.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.2.2', tmp411)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21189
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 21190
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 21191
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + x*f)**p)**q)
                                                                yield 8, subst7
                                                subjects403.appendleft(tmp411)
                                        subjects403.appendleft(tmp408)
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35193
                                    if len(subjects403) >= 1 and isinstance(subjects403[0], Pow):
                                        tmp414 = subjects403.popleft()
                                        subjects415 = deque(tmp414._args)
                                        # State 35194
                                        if len(subjects415) >= 1:
                                            tmp416 = subjects415.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.1', tmp416)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35195
                                                if len(subjects415) >= 1:
                                                    tmp418 = subjects415.popleft()
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2.2.1.2', tmp418)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35196
                                                        if len(subjects415) == 0:
                                                            pass
                                                            # State 35197
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 35198
                                                                if len(subjects403) == 0:
                                                                    pass
                                                                    # State 35199
                                                                    if len(subjects297) == 0:
                                                                        pass
                                                                        # State 35200
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                            yield 13, subst8
                                                            if len(subjects403) >= 1:
                                                                tmp421 = subjects403.popleft()
                                                                subst8 = Substitution(subst7)
                                                                try:
                                                                    subst8.try_add_variable('i2.2.1.2.2', tmp421)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 35198
                                                                    if len(subjects403) == 0:
                                                                        pass
                                                                        # State 35199
                                                                        if len(subjects297) == 0:
                                                                            pass
                                                                            # State 35200
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                                yield 13, subst8
                                                                subjects403.appendleft(tmp421)
                                                    subjects415.appendleft(tmp418)
                                            subjects415.appendleft(tmp416)
                                        subjects403.appendleft(tmp414)
                                if len(subjects403) >= 1 and isinstance(subjects403[0], Mul):
                                    tmp423 = subjects403.popleft()
                                    associative1 = tmp423
                                    associative_type1 = type(tmp423)
                                    subjects424 = deque(tmp423._args)
                                    matcher = CommutativeMatcher21193.get()
                                    tmp425 = subjects424
                                    subjects424 = []
                                    for s in tmp425:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp425, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 21194
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21195
                                                if len(subjects403) == 0:
                                                    pass
                                                    # State 21196
                                                    if len(subjects297) == 0:
                                                        pass
                                                        # State 21197
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 8: log(c*(d*(e + x*f)**p)**q)
                                                            yield 8, subst6
                                            if len(subjects403) >= 1:
                                                tmp427 = []
                                                tmp427.append(subjects403.popleft())
                                                while True:
                                                    if len(tmp427) > 1:
                                                        tmp428 = create_operation_expression(associative1, tmp427)
                                                    elif len(tmp427) == 1:
                                                        tmp428 = tmp427[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp428)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 21195
                                                        if len(subjects403) == 0:
                                                            pass
                                                            # State 21196
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 21197
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 8, subst6
                                                    if len(subjects403) == 0:
                                                        break
                                                    tmp427.append(subjects403.popleft())
                                                subjects403.extendleft(reversed(tmp427))
                                        if pattern_index == 1:
                                            pass
                                            # State 35205
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35206
                                                if len(subjects403) == 0:
                                                    pass
                                                    # State 35207
                                                    if len(subjects297) == 0:
                                                        pass
                                                        # State 35208
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                            yield 13, subst6
                                            if len(subjects403) >= 1:
                                                tmp431 = []
                                                tmp431.append(subjects403.popleft())
                                                while True:
                                                    if len(tmp431) > 1:
                                                        tmp432 = create_operation_expression(associative1, tmp431)
                                                    elif len(tmp431) == 1:
                                                        tmp432 = tmp431[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp432)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35206
                                                        if len(subjects403) == 0:
                                                            pass
                                                            # State 35207
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 35208
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                    yield 13, subst6
                                                    if len(subjects403) == 0:
                                                        break
                                                    tmp431.append(subjects403.popleft())
                                                subjects403.extendleft(reversed(tmp431))
                                    subjects403.appendleft(tmp423)
                            if len(subjects403) >= 1:
                                tmp434 = subjects403.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.1', tmp434)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45661
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45662
                                        if len(subjects403) == 0:
                                            pass
                                            # State 45663
                                            if len(subjects297) == 0:
                                                pass
                                                # State 45664
                                                if len(subjects) == 0:
                                                    pass
                                                    # 15: log(c*(d*v**p)**q)
                                                    yield 15, subst5
                                    if len(subjects403) >= 1:
                                        tmp437 = subjects403.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', tmp437)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45662
                                            if len(subjects403) == 0:
                                                pass
                                                # State 45663
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 45664
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 15: log(c*(d*v**p)**q)
                                                        yield 15, subst5
                                        subjects403.appendleft(tmp437)
                                subjects403.appendleft(tmp434)
                            if len(subjects403) >= 1 and isinstance(subjects403[0], Add):
                                tmp439 = subjects403.popleft()
                                associative1 = tmp439
                                associative_type1 = type(tmp439)
                                subjects440 = deque(tmp439._args)
                                matcher = CommutativeMatcher21199.get()
                                tmp441 = subjects440
                                subjects440 = []
                                for s in tmp441:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp441, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 21205
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21206
                                            if len(subjects403) == 0:
                                                pass
                                                # State 21207
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 21208
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 8: log(c*(d*(e + x*f)**p)**q)
                                                        yield 8, subst5
                                        if len(subjects403) >= 1:
                                            tmp443 = []
                                            tmp443.append(subjects403.popleft())
                                            while True:
                                                if len(tmp443) > 1:
                                                    tmp444 = create_operation_expression(associative1, tmp443)
                                                elif len(tmp443) == 1:
                                                    tmp444 = tmp443[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp444)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21206
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 21207
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 21208
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + x*f)**p)**q)
                                                                yield 8, subst5
                                                if len(subjects403) == 0:
                                                    break
                                                tmp443.append(subjects403.popleft())
                                            subjects403.extendleft(reversed(tmp443))
                                    if pattern_index == 1:
                                        pass
                                        # State 29459
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 29460
                                            if len(subjects403) == 0:
                                                pass
                                                # State 29461
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 29462
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                        yield 11, subst5
                                        if len(subjects403) >= 1:
                                            tmp447 = []
                                            tmp447.append(subjects403.popleft())
                                            while True:
                                                if len(tmp447) > 1:
                                                    tmp448 = create_operation_expression(associative1, tmp447)
                                                elif len(tmp447) == 1:
                                                    tmp448 = tmp447[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp448)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 29460
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 29461
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 29462
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                yield 11, subst5
                                                if len(subjects403) == 0:
                                                    break
                                                tmp447.append(subjects403.popleft())
                                            subjects403.extendleft(reversed(tmp447))
                                    if pattern_index == 2:
                                        pass
                                        # State 35209
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35210
                                            if len(subjects403) == 0:
                                                pass
                                                # State 35211
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 35212
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                        yield 13, subst5
                                        if len(subjects403) >= 1:
                                            tmp451 = []
                                            tmp451.append(subjects403.popleft())
                                            while True:
                                                if len(tmp451) > 1:
                                                    tmp452 = create_operation_expression(associative1, tmp451)
                                                elif len(tmp451) == 1:
                                                    tmp452 = tmp451[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp452)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 35210
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 35211
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 35212
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                yield 13, subst5
                                                if len(subjects403) == 0:
                                                    break
                                                tmp451.append(subjects403.popleft())
                                            subjects403.extendleft(reversed(tmp451))
                                    if pattern_index == 3:
                                        pass
                                        # State 44419
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44420
                                            if len(subjects403) == 0:
                                                pass
                                                # State 44421
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 44422
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 14: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                        yield 14, subst5
                                        if len(subjects403) >= 1:
                                            tmp455 = []
                                            tmp455.append(subjects403.popleft())
                                            while True:
                                                if len(tmp455) > 1:
                                                    tmp456 = create_operation_expression(associative1, tmp455)
                                                elif len(tmp455) == 1:
                                                    tmp456 = tmp455[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp456)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 44420
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 44421
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 44422
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 14: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                                yield 14, subst5
                                                if len(subjects403) == 0:
                                                    break
                                                tmp455.append(subjects403.popleft())
                                            subjects403.extendleft(reversed(tmp455))
                                subjects403.appendleft(tmp439)
                            if len(subjects403) >= 1 and isinstance(subjects403[0], Mul):
                                tmp458 = subjects403.popleft()
                                associative1 = tmp458
                                associative_type1 = type(tmp458)
                                subjects459 = deque(tmp458._args)
                                matcher = CommutativeMatcher32468.get()
                                tmp460 = subjects459
                                subjects459 = []
                                for s in tmp460:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp460, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 32492
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 32493
                                            if len(subjects403) == 0:
                                                pass
                                                # State 32494
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 32495
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 12: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                        yield 12, subst5
                                        if len(subjects403) >= 1:
                                            tmp462 = []
                                            tmp462.append(subjects403.popleft())
                                            while True:
                                                if len(tmp462) > 1:
                                                    tmp463 = create_operation_expression(associative1, tmp462)
                                                elif len(tmp462) == 1:
                                                    tmp463 = tmp462[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp463)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 32493
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 32494
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 32495
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 12: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                                yield 12, subst5
                                                if len(subjects403) == 0:
                                                    break
                                                tmp462.append(subjects403.popleft())
                                            subjects403.extendleft(reversed(tmp462))
                                subjects403.appendleft(tmp458)
                        if len(subjects403) >= 1 and isinstance(subjects403[0], Pow):
                            tmp465 = subjects403.popleft()
                            subjects466 = deque(tmp465._args)
                            # State 21209
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 21210
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21211
                                    if len(subjects466) >= 1:
                                        tmp469 = subjects466.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp469)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21212
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21213
                                                if len(subjects466) == 0:
                                                    pass
                                                    # State 21214
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 21215
                                                        if len(subjects403) == 0:
                                                            pass
                                                            # State 21216
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 21217
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 8, subst7
                                                    if len(subjects403) >= 1:
                                                        tmp473 = subjects403.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', tmp473)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 21215
                                                            if len(subjects403) == 0:
                                                                pass
                                                                # State 21216
                                                                if len(subjects297) == 0:
                                                                    pass
                                                                    # State 21217
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 8: log(c*(d*(e + x*f)**p)**q)
                                                                        yield 8, subst7
                                                        subjects403.appendleft(tmp473)
                                            if len(subjects466) >= 1:
                                                tmp475 = subjects466.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2.2', tmp475)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21213
                                                    if len(subjects466) == 0:
                                                        pass
                                                        # State 21214
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 21215
                                                            if len(subjects403) == 0:
                                                                pass
                                                                # State 21216
                                                                if len(subjects297) == 0:
                                                                    pass
                                                                    # State 21217
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 8: log(c*(d*(e + x*f)**p)**q)
                                                                        yield 8, subst7
                                                        if len(subjects403) >= 1:
                                                            tmp478 = subjects403.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2', tmp478)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 21215
                                                                if len(subjects403) == 0:
                                                                    pass
                                                                    # State 21216
                                                                    if len(subjects297) == 0:
                                                                        pass
                                                                        # State 21217
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 8: log(c*(d*(e + x*f)**p)**q)
                                                                            yield 8, subst7
                                                            subjects403.appendleft(tmp478)
                                                subjects466.appendleft(tmp475)
                                        subjects466.appendleft(tmp469)
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35213
                                    if len(subjects466) >= 1 and isinstance(subjects466[0], Pow):
                                        tmp481 = subjects466.popleft()
                                        subjects482 = deque(tmp481._args)
                                        # State 35214
                                        if len(subjects482) >= 1:
                                            tmp483 = subjects482.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2.1.1', tmp483)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35215
                                                if len(subjects482) >= 1:
                                                    tmp485 = subjects482.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2.1.2', tmp485)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35216
                                                        if len(subjects482) == 0:
                                                            pass
                                                            # State 35217
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 35218
                                                                if len(subjects466) == 0:
                                                                    pass
                                                                    # State 35219
                                                                    subst8 = Substitution(subst7)
                                                                    try:
                                                                        subst8.try_add_variable('i2.2.1.2.2', 1)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 35220
                                                                        if len(subjects403) == 0:
                                                                            pass
                                                                            # State 35221
                                                                            if len(subjects297) == 0:
                                                                                pass
                                                                                # State 35222
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                                    yield 13, subst8
                                                                    if len(subjects403) >= 1:
                                                                        tmp489 = subjects403.popleft()
                                                                        subst8 = Substitution(subst7)
                                                                        try:
                                                                            subst8.try_add_variable('i2.2.1.2.2', tmp489)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            # State 35220
                                                                            if len(subjects403) == 0:
                                                                                pass
                                                                                # State 35221
                                                                                if len(subjects297) == 0:
                                                                                    pass
                                                                                    # State 35222
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                                        yield 13, subst8
                                                                        subjects403.appendleft(tmp489)
                                                            if len(subjects466) >= 1:
                                                                tmp491 = subjects466.popleft()
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2.2', tmp491)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 35218
                                                                    if len(subjects466) == 0:
                                                                        pass
                                                                        # State 35219
                                                                        subst8 = Substitution(subst7)
                                                                        try:
                                                                            subst8.try_add_variable('i2.2.1.2.2', 1)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            # State 35220
                                                                            if len(subjects403) == 0:
                                                                                pass
                                                                                # State 35221
                                                                                if len(subjects297) == 0:
                                                                                    pass
                                                                                    # State 35222
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                                        yield 13, subst8
                                                                        if len(subjects403) >= 1:
                                                                            tmp494 = subjects403.popleft()
                                                                            subst8 = Substitution(subst7)
                                                                            try:
                                                                                subst8.try_add_variable('i2.2.1.2.2', tmp494)
                                                                            except ValueError:
                                                                                pass
                                                                            else:
                                                                                pass
                                                                                # State 35220
                                                                                if len(subjects403) == 0:
                                                                                    pass
                                                                                    # State 35221
                                                                                    if len(subjects297) == 0:
                                                                                        pass
                                                                                        # State 35222
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                                            yield 13, subst8
                                                                            subjects403.appendleft(tmp494)
                                                                subjects466.appendleft(tmp491)
                                                    subjects482.appendleft(tmp485)
                                            subjects482.appendleft(tmp483)
                                        subjects466.appendleft(tmp481)
                                if len(subjects466) >= 1 and isinstance(subjects466[0], Mul):
                                    tmp496 = subjects466.popleft()
                                    associative1 = tmp496
                                    associative_type1 = type(tmp496)
                                    subjects497 = deque(tmp496._args)
                                    matcher = CommutativeMatcher21219.get()
                                    tmp498 = subjects497
                                    subjects497 = []
                                    for s in tmp498:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp498, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 21220
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21221
                                                if len(subjects466) == 0:
                                                    pass
                                                    # State 21222
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 21223
                                                        if len(subjects403) == 0:
                                                            pass
                                                            # State 21224
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 21225
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 8, subst6
                                                    if len(subjects403) >= 1:
                                                        tmp501 = subjects403.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp501)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 21223
                                                            if len(subjects403) == 0:
                                                                pass
                                                                # State 21224
                                                                if len(subjects297) == 0:
                                                                    pass
                                                                    # State 21225
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 8: log(c*(d*(e + x*f)**p)**q)
                                                                        yield 8, subst6
                                                        subjects403.appendleft(tmp501)
                                            if len(subjects466) >= 1:
                                                tmp503 = []
                                                tmp503.append(subjects466.popleft())
                                                while True:
                                                    if len(tmp503) > 1:
                                                        tmp504 = create_operation_expression(associative1, tmp503)
                                                    elif len(tmp503) == 1:
                                                        tmp504 = tmp503[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2.2', tmp504)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 21221
                                                        if len(subjects466) == 0:
                                                            pass
                                                            # State 21222
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 21223
                                                                if len(subjects403) == 0:
                                                                    pass
                                                                    # State 21224
                                                                    if len(subjects297) == 0:
                                                                        pass
                                                                        # State 21225
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 8: log(c*(d*(e + x*f)**p)**q)
                                                                            yield 8, subst6
                                                            if len(subjects403) >= 1:
                                                                tmp507 = subjects403.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2.1.2.2', tmp507)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 21223
                                                                    if len(subjects403) == 0:
                                                                        pass
                                                                        # State 21224
                                                                        if len(subjects297) == 0:
                                                                            pass
                                                                            # State 21225
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 8: log(c*(d*(e + x*f)**p)**q)
                                                                                yield 8, subst6
                                                                subjects403.appendleft(tmp507)
                                                    if len(subjects466) == 0:
                                                        break
                                                    tmp503.append(subjects466.popleft())
                                                subjects466.extendleft(reversed(tmp503))
                                        if pattern_index == 1:
                                            pass
                                            # State 35227
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35228
                                                if len(subjects466) == 0:
                                                    pass
                                                    # State 35229
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35230
                                                        if len(subjects403) == 0:
                                                            pass
                                                            # State 35231
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 35232
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                    yield 13, subst6
                                                    if len(subjects403) >= 1:
                                                        tmp511 = subjects403.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp511)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35230
                                                            if len(subjects403) == 0:
                                                                pass
                                                                # State 35231
                                                                if len(subjects297) == 0:
                                                                    pass
                                                                    # State 35232
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                        yield 13, subst6
                                                        subjects403.appendleft(tmp511)
                                            if len(subjects466) >= 1:
                                                tmp513 = []
                                                tmp513.append(subjects466.popleft())
                                                while True:
                                                    if len(tmp513) > 1:
                                                        tmp514 = create_operation_expression(associative1, tmp513)
                                                    elif len(tmp513) == 1:
                                                        tmp514 = tmp513[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2.2', tmp514)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35228
                                                        if len(subjects466) == 0:
                                                            pass
                                                            # State 35229
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 35230
                                                                if len(subjects403) == 0:
                                                                    pass
                                                                    # State 35231
                                                                    if len(subjects297) == 0:
                                                                        pass
                                                                        # State 35232
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                            yield 13, subst6
                                                            if len(subjects403) >= 1:
                                                                tmp517 = subjects403.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2.1.2.2', tmp517)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 35230
                                                                    if len(subjects403) == 0:
                                                                        pass
                                                                        # State 35231
                                                                        if len(subjects297) == 0:
                                                                            pass
                                                                            # State 35232
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                                yield 13, subst6
                                                                subjects403.appendleft(tmp517)
                                                    if len(subjects466) == 0:
                                                        break
                                                    tmp513.append(subjects466.popleft())
                                                subjects466.extendleft(reversed(tmp513))
                                    subjects466.appendleft(tmp496)
                            if len(subjects466) >= 1:
                                tmp519 = subjects466.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.1', tmp519)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25720
                                    if len(subjects466) >= 1:
                                        tmp521 = subjects466.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp521)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25721
                                            if len(subjects466) == 0:
                                                pass
                                                # State 25722
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 25723
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 25724
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 25725
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 9: log(c*(d*v**p)**q)
                                                                yield 9, subst5
                                                if len(subjects403) >= 1:
                                                    tmp524 = subjects403.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp524)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 25723
                                                        if len(subjects403) == 0:
                                                            pass
                                                            # State 25724
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 25725
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 9: log(c*(d*v**p)**q)
                                                                    yield 9, subst5
                                                    subjects403.appendleft(tmp524)
                                        subjects466.appendleft(tmp521)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45665
                                        if len(subjects466) == 0:
                                            pass
                                            # State 45666
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45667
                                                if len(subjects403) == 0:
                                                    pass
                                                    # State 45668
                                                    if len(subjects297) == 0:
                                                        pass
                                                        # State 45669
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 15: log(c*(d*v**p)**q)
                                                            yield 15, subst5
                                            if len(subjects403) >= 1:
                                                tmp528 = subjects403.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp528)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 45667
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 45668
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 45669
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 15: log(c*(d*v**p)**q)
                                                                yield 15, subst5
                                                subjects403.appendleft(tmp528)
                                    if len(subjects466) >= 1:
                                        tmp530 = subjects466.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp530)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45665
                                            if len(subjects466) == 0:
                                                pass
                                                # State 45666
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 45667
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 45668
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 45669
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 15: log(c*(d*v**p)**q)
                                                                yield 15, subst5
                                                if len(subjects403) >= 1:
                                                    tmp533 = subjects403.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp533)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 45667
                                                        if len(subjects403) == 0:
                                                            pass
                                                            # State 45668
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 45669
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 15: log(c*(d*v**p)**q)
                                                                    yield 15, subst5
                                                    subjects403.appendleft(tmp533)
                                        subjects466.appendleft(tmp530)
                                subjects466.appendleft(tmp519)
                            if len(subjects466) >= 1 and isinstance(subjects466[0], Add):
                                tmp535 = subjects466.popleft()
                                associative1 = tmp535
                                associative_type1 = type(tmp535)
                                subjects536 = deque(tmp535._args)
                                matcher = CommutativeMatcher21227.get()
                                tmp537 = subjects536
                                subjects536 = []
                                for s in tmp537:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp537, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 21233
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21234
                                            if len(subjects466) == 0:
                                                pass
                                                # State 21235
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21236
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 21237
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 21238
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 8: log(c*(d*(e + x*f)**p)**q)
                                                                yield 8, subst5
                                                if len(subjects403) >= 1:
                                                    tmp540 = subjects403.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp540)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 21236
                                                        if len(subjects403) == 0:
                                                            pass
                                                            # State 21237
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 21238
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 8: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 8, subst5
                                                    subjects403.appendleft(tmp540)
                                        if len(subjects466) >= 1:
                                            tmp542 = []
                                            tmp542.append(subjects466.popleft())
                                            while True:
                                                if len(tmp542) > 1:
                                                    tmp543 = create_operation_expression(associative1, tmp542)
                                                elif len(tmp542) == 1:
                                                    tmp543 = tmp542[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp543)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21234
                                                    if len(subjects466) == 0:
                                                        pass
                                                        # State 21235
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 21236
                                                            if len(subjects403) == 0:
                                                                pass
                                                                # State 21237
                                                                if len(subjects297) == 0:
                                                                    pass
                                                                    # State 21238
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 8: log(c*(d*(e + x*f)**p)**q)
                                                                        yield 8, subst5
                                                        if len(subjects403) >= 1:
                                                            tmp546 = subjects403.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp546)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 21236
                                                                if len(subjects403) == 0:
                                                                    pass
                                                                    # State 21237
                                                                    if len(subjects297) == 0:
                                                                        pass
                                                                        # State 21238
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 8: log(c*(d*(e + x*f)**p)**q)
                                                                            yield 8, subst5
                                                            subjects403.appendleft(tmp546)
                                                if len(subjects466) == 0:
                                                    break
                                                tmp542.append(subjects466.popleft())
                                            subjects466.extendleft(reversed(tmp542))
                                    if pattern_index == 1:
                                        pass
                                        # State 29473
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 29474
                                            if len(subjects466) == 0:
                                                pass
                                                # State 29475
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 29476
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 29477
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 29478
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                yield 11, subst5
                                                if len(subjects403) >= 1:
                                                    tmp550 = subjects403.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp550)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 29476
                                                        if len(subjects403) == 0:
                                                            pass
                                                            # State 29477
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 29478
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                    yield 11, subst5
                                                    subjects403.appendleft(tmp550)
                                        if len(subjects466) >= 1:
                                            tmp552 = []
                                            tmp552.append(subjects466.popleft())
                                            while True:
                                                if len(tmp552) > 1:
                                                    tmp553 = create_operation_expression(associative1, tmp552)
                                                elif len(tmp552) == 1:
                                                    tmp553 = tmp552[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp553)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 29474
                                                    if len(subjects466) == 0:
                                                        pass
                                                        # State 29475
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 29476
                                                            if len(subjects403) == 0:
                                                                pass
                                                                # State 29477
                                                                if len(subjects297) == 0:
                                                                    pass
                                                                    # State 29478
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                        yield 11, subst5
                                                        if len(subjects403) >= 1:
                                                            tmp556 = subjects403.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp556)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 29476
                                                                if len(subjects403) == 0:
                                                                    pass
                                                                    # State 29477
                                                                    if len(subjects297) == 0:
                                                                        pass
                                                                        # State 29478
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                            yield 11, subst5
                                                            subjects403.appendleft(tmp556)
                                                if len(subjects466) == 0:
                                                    break
                                                tmp552.append(subjects466.popleft())
                                            subjects466.extendleft(reversed(tmp552))
                                    if pattern_index == 2:
                                        pass
                                        # State 35233
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35234
                                            if len(subjects466) == 0:
                                                pass
                                                # State 35235
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 35236
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 35237
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 35238
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                yield 13, subst5
                                                if len(subjects403) >= 1:
                                                    tmp560 = subjects403.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp560)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35236
                                                        if len(subjects403) == 0:
                                                            pass
                                                            # State 35237
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 35238
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                    yield 13, subst5
                                                    subjects403.appendleft(tmp560)
                                        if len(subjects466) >= 1:
                                            tmp562 = []
                                            tmp562.append(subjects466.popleft())
                                            while True:
                                                if len(tmp562) > 1:
                                                    tmp563 = create_operation_expression(associative1, tmp562)
                                                elif len(tmp562) == 1:
                                                    tmp563 = tmp562[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp563)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 35234
                                                    if len(subjects466) == 0:
                                                        pass
                                                        # State 35235
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35236
                                                            if len(subjects403) == 0:
                                                                pass
                                                                # State 35237
                                                                if len(subjects297) == 0:
                                                                    pass
                                                                    # State 35238
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                        yield 13, subst5
                                                        if len(subjects403) >= 1:
                                                            tmp566 = subjects403.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp566)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 35236
                                                                if len(subjects403) == 0:
                                                                    pass
                                                                    # State 35237
                                                                    if len(subjects297) == 0:
                                                                        pass
                                                                        # State 35238
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                                            yield 13, subst5
                                                            subjects403.appendleft(tmp566)
                                                if len(subjects466) == 0:
                                                    break
                                                tmp562.append(subjects466.popleft())
                                            subjects466.extendleft(reversed(tmp562))
                                    if pattern_index == 3:
                                        pass
                                        # State 44430
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44431
                                            if len(subjects466) == 0:
                                                pass
                                                # State 44432
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 44433
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 44434
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 44435
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 14: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                                yield 14, subst5
                                                if len(subjects403) >= 1:
                                                    tmp570 = subjects403.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp570)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 44433
                                                        if len(subjects403) == 0:
                                                            pass
                                                            # State 44434
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 44435
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 14: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                                    yield 14, subst5
                                                    subjects403.appendleft(tmp570)
                                        if len(subjects466) >= 1:
                                            tmp572 = []
                                            tmp572.append(subjects466.popleft())
                                            while True:
                                                if len(tmp572) > 1:
                                                    tmp573 = create_operation_expression(associative1, tmp572)
                                                elif len(tmp572) == 1:
                                                    tmp573 = tmp572[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp573)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 44431
                                                    if len(subjects466) == 0:
                                                        pass
                                                        # State 44432
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 44433
                                                            if len(subjects403) == 0:
                                                                pass
                                                                # State 44434
                                                                if len(subjects297) == 0:
                                                                    pass
                                                                    # State 44435
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 14: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                                        yield 14, subst5
                                                        if len(subjects403) >= 1:
                                                            tmp576 = subjects403.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp576)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 44433
                                                                if len(subjects403) == 0:
                                                                    pass
                                                                    # State 44434
                                                                    if len(subjects297) == 0:
                                                                        pass
                                                                        # State 44435
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 14: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                                            yield 14, subst5
                                                            subjects403.appendleft(tmp576)
                                                if len(subjects466) == 0:
                                                    break
                                                tmp572.append(subjects466.popleft())
                                            subjects466.extendleft(reversed(tmp572))
                                subjects466.appendleft(tmp535)
                            if len(subjects466) >= 1 and isinstance(subjects466[0], Mul):
                                tmp578 = subjects466.popleft()
                                associative1 = tmp578
                                associative_type1 = type(tmp578)
                                subjects579 = deque(tmp578._args)
                                matcher = CommutativeMatcher32497.get()
                                tmp580 = subjects579
                                subjects579 = []
                                for s in tmp580:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp580, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 32521
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 32522
                                            if len(subjects466) == 0:
                                                pass
                                                # State 32523
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 32524
                                                    if len(subjects403) == 0:
                                                        pass
                                                        # State 32525
                                                        if len(subjects297) == 0:
                                                            pass
                                                            # State 32526
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 12: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                                yield 12, subst5
                                                if len(subjects403) >= 1:
                                                    tmp583 = subjects403.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp583)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 32524
                                                        if len(subjects403) == 0:
                                                            pass
                                                            # State 32525
                                                            if len(subjects297) == 0:
                                                                pass
                                                                # State 32526
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 12: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                                    yield 12, subst5
                                                    subjects403.appendleft(tmp583)
                                        if len(subjects466) >= 1:
                                            tmp585 = []
                                            tmp585.append(subjects466.popleft())
                                            while True:
                                                if len(tmp585) > 1:
                                                    tmp586 = create_operation_expression(associative1, tmp585)
                                                elif len(tmp585) == 1:
                                                    tmp586 = tmp585[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp586)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 32522
                                                    if len(subjects466) == 0:
                                                        pass
                                                        # State 32523
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 32524
                                                            if len(subjects403) == 0:
                                                                pass
                                                                # State 32525
                                                                if len(subjects297) == 0:
                                                                    pass
                                                                    # State 32526
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 12: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                                        yield 12, subst5
                                                        if len(subjects403) >= 1:
                                                            tmp589 = subjects403.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp589)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 32524
                                                                if len(subjects403) == 0:
                                                                    pass
                                                                    # State 32525
                                                                    if len(subjects297) == 0:
                                                                        pass
                                                                        # State 32526
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 12: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                                            yield 12, subst5
                                                            subjects403.appendleft(tmp589)
                                                if len(subjects466) == 0:
                                                    break
                                                tmp585.append(subjects466.popleft())
                                            subjects466.extendleft(reversed(tmp585))
                                subjects466.appendleft(tmp578)
                            subjects403.appendleft(tmp465)
                    if len(subjects403) >= 1:
                        tmp591 = subjects403.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1', tmp591)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53284
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53285
                                if len(subjects403) == 0:
                                    pass
                                    # State 53286
                                    if len(subjects297) == 0:
                                        pass
                                        # State 53287
                                        if len(subjects) == 0:
                                            pass
                                            # 17: log(c*RFx**p)
                                            yield 17, subst3
                            if len(subjects403) >= 1:
                                tmp594 = subjects403.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', tmp594)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53285
                                    if len(subjects403) == 0:
                                        pass
                                        # State 53286
                                        if len(subjects297) == 0:
                                            pass
                                            # State 53287
                                            if len(subjects) == 0:
                                                pass
                                                # 17: log(c*RFx**p)
                                                yield 17, subst3
                                subjects403.appendleft(tmp594)
                        subjects403.appendleft(tmp591)
                    if len(subjects403) >= 1 and isinstance(subjects403[0], Mul):
                        tmp596 = subjects403.popleft()
                        associative1 = tmp596
                        associative_type1 = type(tmp596)
                        subjects597 = deque(tmp596._args)
                        matcher = CommutativeMatcher21240.get()
                        tmp598 = subjects597
                        subjects597 = []
                        for s in tmp598:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp598, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 21277
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21278
                                    if len(subjects403) == 0:
                                        pass
                                        # State 21279
                                        if len(subjects297) == 0:
                                            pass
                                            # State 21280
                                            if len(subjects) == 0:
                                                pass
                                                # 8: log(c*(d*(e + x*f)**p)**q)
                                                yield 8, subst3
                                if len(subjects403) >= 1:
                                    tmp600 = []
                                    tmp600.append(subjects403.popleft())
                                    while True:
                                        if len(tmp600) > 1:
                                            tmp601 = create_operation_expression(associative1, tmp600)
                                        elif len(tmp600) == 1:
                                            tmp601 = tmp600[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp601)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21278
                                            if len(subjects403) == 0:
                                                pass
                                                # State 21279
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 21280
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 8: log(c*(d*(e + x*f)**p)**q)
                                                        yield 8, subst3
                                        if len(subjects403) == 0:
                                            break
                                        tmp600.append(subjects403.popleft())
                                    subjects403.extendleft(reversed(tmp600))
                            if pattern_index == 1:
                                pass
                                # State 25729
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25730
                                    if len(subjects403) == 0:
                                        pass
                                        # State 25731
                                        if len(subjects297) == 0:
                                            pass
                                            # State 25732
                                            if len(subjects) == 0:
                                                pass
                                                # 9: log(c*(d*v**p)**q)
                                                yield 9, subst3
                                if len(subjects403) >= 1:
                                    tmp604 = []
                                    tmp604.append(subjects403.popleft())
                                    while True:
                                        if len(tmp604) > 1:
                                            tmp605 = create_operation_expression(associative1, tmp604)
                                        elif len(tmp604) == 1:
                                            tmp605 = tmp604[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp605)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25730
                                            if len(subjects403) == 0:
                                                pass
                                                # State 25731
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 25732
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 9: log(c*(d*v**p)**q)
                                                        yield 9, subst3
                                        if len(subjects403) == 0:
                                            break
                                        tmp604.append(subjects403.popleft())
                                    subjects403.extendleft(reversed(tmp604))
                            if pattern_index == 2:
                                pass
                                # State 29503
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 29504
                                    if len(subjects403) == 0:
                                        pass
                                        # State 29505
                                        if len(subjects297) == 0:
                                            pass
                                            # State 29506
                                            if len(subjects) == 0:
                                                pass
                                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                yield 11, subst3
                                if len(subjects403) >= 1:
                                    tmp608 = []
                                    tmp608.append(subjects403.popleft())
                                    while True:
                                        if len(tmp608) > 1:
                                            tmp609 = create_operation_expression(associative1, tmp608)
                                        elif len(tmp608) == 1:
                                            tmp609 = tmp608[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp609)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 29504
                                            if len(subjects403) == 0:
                                                pass
                                                # State 29505
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 29506
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                        yield 11, subst3
                                        if len(subjects403) == 0:
                                            break
                                        tmp608.append(subjects403.popleft())
                                    subjects403.extendleft(reversed(tmp608))
                            if pattern_index == 3:
                                pass
                                # State 32581
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 32582
                                    if len(subjects403) == 0:
                                        pass
                                        # State 32583
                                        if len(subjects297) == 0:
                                            pass
                                            # State 32584
                                            if len(subjects) == 0:
                                                pass
                                                # 12: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                yield 12, subst3
                                if len(subjects403) >= 1:
                                    tmp612 = []
                                    tmp612.append(subjects403.popleft())
                                    while True:
                                        if len(tmp612) > 1:
                                            tmp613 = create_operation_expression(associative1, tmp612)
                                        elif len(tmp612) == 1:
                                            tmp613 = tmp612[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp613)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 32582
                                            if len(subjects403) == 0:
                                                pass
                                                # State 32583
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 32584
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 12: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                        yield 12, subst3
                                        if len(subjects403) == 0:
                                            break
                                        tmp612.append(subjects403.popleft())
                                    subjects403.extendleft(reversed(tmp612))
                            if pattern_index == 4:
                                pass
                                # State 35267
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35268
                                    if len(subjects403) == 0:
                                        pass
                                        # State 35269
                                        if len(subjects297) == 0:
                                            pass
                                            # State 35270
                                            if len(subjects) == 0:
                                                pass
                                                # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                yield 13, subst3
                                if len(subjects403) >= 1:
                                    tmp616 = []
                                    tmp616.append(subjects403.popleft())
                                    while True:
                                        if len(tmp616) > 1:
                                            tmp617 = create_operation_expression(associative1, tmp616)
                                        elif len(tmp616) == 1:
                                            tmp617 = tmp616[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp617)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35268
                                            if len(subjects403) == 0:
                                                pass
                                                # State 35269
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 35270
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 13: log(c*(d*(e + f*x**m)**p)**q)
                                                        yield 13, subst3
                                        if len(subjects403) == 0:
                                            break
                                        tmp616.append(subjects403.popleft())
                                    subjects403.extendleft(reversed(tmp616))
                            if pattern_index == 5:
                                pass
                                # State 44454
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44455
                                    if len(subjects403) == 0:
                                        pass
                                        # State 44456
                                        if len(subjects297) == 0:
                                            pass
                                            # State 44457
                                            if len(subjects) == 0:
                                                pass
                                                # 14: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                yield 14, subst3
                                if len(subjects403) >= 1:
                                    tmp620 = []
                                    tmp620.append(subjects403.popleft())
                                    while True:
                                        if len(tmp620) > 1:
                                            tmp621 = create_operation_expression(associative1, tmp620)
                                        elif len(tmp620) == 1:
                                            tmp621 = tmp620[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp621)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44455
                                            if len(subjects403) == 0:
                                                pass
                                                # State 44456
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 44457
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 14: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                        yield 14, subst3
                                        if len(subjects403) == 0:
                                            break
                                        tmp620.append(subjects403.popleft())
                                    subjects403.extendleft(reversed(tmp620))
                            if pattern_index == 6:
                                pass
                                # State 45673
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45674
                                    if len(subjects403) == 0:
                                        pass
                                        # State 45675
                                        if len(subjects297) == 0:
                                            pass
                                            # State 45676
                                            if len(subjects) == 0:
                                                pass
                                                # 15: log(c*(d*v**p)**q)
                                                yield 15, subst3
                                if len(subjects403) >= 1:
                                    tmp624 = []
                                    tmp624.append(subjects403.popleft())
                                    while True:
                                        if len(tmp624) > 1:
                                            tmp625 = create_operation_expression(associative1, tmp624)
                                        elif len(tmp624) == 1:
                                            tmp625 = tmp624[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp625)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45674
                                            if len(subjects403) == 0:
                                                pass
                                                # State 45675
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 45676
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 15: log(c*(d*v**p)**q)
                                                        yield 15, subst3
                                        if len(subjects403) == 0:
                                            break
                                        tmp624.append(subjects403.popleft())
                                    subjects403.extendleft(reversed(tmp624))
                        subjects403.appendleft(tmp596)
                    if len(subjects403) >= 1 and isinstance(subjects403[0], Add):
                        tmp627 = subjects403.popleft()
                        associative1 = tmp627
                        associative_type1 = type(tmp627)
                        subjects628 = deque(tmp627._args)
                        matcher = CommutativeMatcher50900.get()
                        tmp629 = subjects628
                        subjects628 = []
                        for s in tmp629:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp629, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 50913
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 50914
                                    if len(subjects403) == 0:
                                        pass
                                        # State 50915
                                        if len(subjects297) == 0:
                                            pass
                                            # State 50916
                                            if len(subjects) == 0:
                                                pass
                                                # 16: log(c*(d + e*x**2)**p)
                                                yield 16, subst3
                                if len(subjects403) >= 1:
                                    tmp631 = []
                                    tmp631.append(subjects403.popleft())
                                    while True:
                                        if len(tmp631) > 1:
                                            tmp632 = create_operation_expression(associative1, tmp631)
                                        elif len(tmp631) == 1:
                                            tmp632 = tmp631[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp632)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 50914
                                            if len(subjects403) == 0:
                                                pass
                                                # State 50915
                                                if len(subjects297) == 0:
                                                    pass
                                                    # State 50916
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 16: log(c*(d + e*x**2)**p)
                                                        yield 16, subst3
                                        if len(subjects403) == 0:
                                            break
                                        tmp631.append(subjects403.popleft())
                                    subjects403.extendleft(reversed(tmp631))
                        subjects403.appendleft(tmp627)
                    subjects297.appendleft(tmp402)
                if len(subjects297) >= 1 and isinstance(subjects297[0], Add):
                    tmp634 = subjects297.popleft()
                    associative1 = tmp634
                    associative_type1 = type(tmp634)
                    subjects635 = deque(tmp634._args)
                    matcher = CommutativeMatcher26184.get()
                    tmp636 = subjects635
                    subjects635 = []
                    for s in tmp636:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp636, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 26190
                            if len(subjects297) == 0:
                                pass
                                # State 26191
                                if len(subjects) == 0:
                                    pass
                                    # 10: log(c*(e + x*f))
                                    yield 10, subst2
                    subjects297.appendleft(tmp634)
            if len(subjects297) >= 1 and isinstance(subjects297[0], Mul):
                tmp637 = subjects297.popleft()
                associative1 = tmp637
                associative_type1 = type(tmp637)
                subjects638 = deque(tmp637._args)
                matcher = CommutativeMatcher21282.get()
                tmp639 = subjects638
                subjects638 = []
                for s in tmp639:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp639, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 21451
                        if len(subjects297) == 0:
                            pass
                            # State 21452
                            if len(subjects) == 0:
                                pass
                                # 8: log(c*(d*(e + x*f)**p)**q)
                                yield 8, subst1
                    if pattern_index == 1:
                        pass
                        # State 25751
                        if len(subjects297) == 0:
                            pass
                            # State 25752
                            if len(subjects) == 0:
                                pass
                                # 9: log(c*(d*v**p)**q)
                                yield 9, subst1
                    if pattern_index == 2:
                        pass
                        # State 26206
                        if len(subjects297) == 0:
                            pass
                            # State 26207
                            if len(subjects) == 0:
                                pass
                                # 10: log(c*(e + x*f))
                                yield 10, subst1
                    if pattern_index == 3:
                        pass
                        # State 29611
                        if len(subjects297) == 0:
                            pass
                            # State 29612
                            if len(subjects) == 0:
                                pass
                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                yield 11, subst1
                    if pattern_index == 4:
                        pass
                        # State 32809
                        if len(subjects297) == 0:
                            pass
                            # State 32810
                            if len(subjects) == 0:
                                pass
                                # 12: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                yield 12, subst1
                    if pattern_index == 5:
                        pass
                        # State 35399
                        if len(subjects297) == 0:
                            pass
                            # State 35400
                            if len(subjects) == 0:
                                pass
                                # 13: log(c*(d*(e + f*x**m)**p)**q)
                                yield 13, subst1
                    if pattern_index == 6:
                        pass
                        # State 44538
                        if len(subjects297) == 0:
                            pass
                            # State 44539
                            if len(subjects) == 0:
                                pass
                                # 14: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                yield 14, subst1
                    if pattern_index == 7:
                        pass
                        # State 45697
                        if len(subjects297) == 0:
                            pass
                            # State 45698
                            if len(subjects) == 0:
                                pass
                                # 15: log(c*(d*v**p)**q)
                                yield 15, subst1
                    if pattern_index == 8:
                        pass
                        # State 50949
                        if len(subjects297) == 0:
                            pass
                            # State 50950
                            if len(subjects) == 0:
                                pass
                                # 16: log(c*(d + e*x**2)**p)
                                yield 16, subst1
                    if pattern_index == 9:
                        pass
                        # State 53292
                        if len(subjects297) == 0:
                            pass
                            # State 53293
                            if len(subjects) == 0:
                                pass
                                # 17: log(c*RFx**p)
                                yield 17, subst1
                subjects297.appendleft(tmp637)
            subjects.appendleft(tmp296)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp640 = subjects.popleft()
            subjects641 = deque(tmp640._args)
            # State 59949
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 59950
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59951
                    if len(subjects641) >= 1:
                        tmp644 = subjects641.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp644)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 59952
                            if len(subjects641) == 0:
                                pass
                                # State 59953
                                if len(subjects) == 0:
                                    pass
                                    # 18: sin(c + x*d)
                                    yield 18, subst3
                        subjects641.appendleft(tmp644)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 73761
                    if len(subjects641) >= 1 and isinstance(subjects641[0], Pow):
                        tmp647 = subjects641.popleft()
                        subjects648 = deque(tmp647._args)
                        # State 73762
                        if len(subjects648) >= 1:
                            tmp649 = subjects648.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp649)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 73763
                                if len(subjects648) >= 1:
                                    tmp651 = subjects648.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp651)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 73764
                                        if len(subjects648) == 0:
                                            pass
                                            # State 73765
                                            if len(subjects641) == 0:
                                                pass
                                                # State 73766
                                                if len(subjects) == 0:
                                                    pass
                                                    # 22: sin(c + d*x**n)
                                                    yield 22, subst4
                                    subjects648.appendleft(tmp651)
                            subjects648.appendleft(tmp649)
                        subjects641.appendleft(tmp647)
                if len(subjects641) >= 1 and isinstance(subjects641[0], Mul):
                    tmp653 = subjects641.popleft()
                    associative1 = tmp653
                    associative_type1 = type(tmp653)
                    subjects654 = deque(tmp653._args)
                    matcher = CommutativeMatcher59955.get()
                    tmp655 = subjects654
                    subjects654 = []
                    for s in tmp655:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp655, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 59956
                            if len(subjects641) == 0:
                                pass
                                # State 59957
                                if len(subjects) == 0:
                                    pass
                                    # 18: sin(c + x*d)
                                    yield 18, subst2
                        if pattern_index == 1:
                            pass
                            # State 73771
                            if len(subjects641) == 0:
                                pass
                                # State 73772
                                if len(subjects) == 0:
                                    pass
                                    # 22: sin(c + d*x**n)
                                    yield 22, subst2
                    subjects641.appendleft(tmp653)
            if len(subjects641) >= 1:
                tmp656 = subjects641.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp656)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72292
                    if len(subjects641) == 0:
                        pass
                        # State 72293
                        if len(subjects) == 0:
                            pass
                            # 20: sin(v)
                            yield 20, subst1
                subjects641.appendleft(tmp656)
            if len(subjects641) >= 1 and isinstance(subjects641[0], Add):
                tmp658 = subjects641.popleft()
                associative1 = tmp658
                associative_type1 = type(tmp658)
                subjects659 = deque(tmp658._args)
                matcher = CommutativeMatcher59959.get()
                tmp660 = subjects659
                subjects659 = []
                for s in tmp660:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp660, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 59965
                        if len(subjects641) == 0:
                            pass
                            # State 59966
                            if len(subjects) == 0:
                                pass
                                # 18: sin(c + x*d)
                                yield 18, subst1
                    if pattern_index == 1:
                        pass
                        # State 73783
                        if len(subjects641) == 0:
                            pass
                            # State 73784
                            if len(subjects) == 0:
                                pass
                                # 22: sin(c + d*x**n)
                                yield 22, subst1
                subjects641.appendleft(tmp658)
            subjects.appendleft(tmp640)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp661 = subjects.popleft()
            subjects662 = deque(tmp661._args)
            # State 60065
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 60066
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 60067
                    if len(subjects662) >= 1:
                        tmp665 = subjects662.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp665)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 60068
                            if len(subjects662) == 0:
                                pass
                                # State 60069
                                if len(subjects) == 0:
                                    pass
                                    # 19: cos(c + x*d)
                                    yield 19, subst3
                        subjects662.appendleft(tmp665)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 73973
                    if len(subjects662) >= 1 and isinstance(subjects662[0], Pow):
                        tmp668 = subjects662.popleft()
                        subjects669 = deque(tmp668._args)
                        # State 73974
                        if len(subjects669) >= 1:
                            tmp670 = subjects669.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp670)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 73975
                                if len(subjects669) >= 1:
                                    tmp672 = subjects669.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp672)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 73976
                                        if len(subjects669) == 0:
                                            pass
                                            # State 73977
                                            if len(subjects662) == 0:
                                                pass
                                                # State 73978
                                                if len(subjects) == 0:
                                                    pass
                                                    # 23: cos(c + d*x**n)
                                                    yield 23, subst4
                                    subjects669.appendleft(tmp672)
                            subjects669.appendleft(tmp670)
                        subjects662.appendleft(tmp668)
                if len(subjects662) >= 1 and isinstance(subjects662[0], Mul):
                    tmp674 = subjects662.popleft()
                    associative1 = tmp674
                    associative_type1 = type(tmp674)
                    subjects675 = deque(tmp674._args)
                    matcher = CommutativeMatcher60071.get()
                    tmp676 = subjects675
                    subjects675 = []
                    for s in tmp676:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp676, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 60072
                            if len(subjects662) == 0:
                                pass
                                # State 60073
                                if len(subjects) == 0:
                                    pass
                                    # 19: cos(c + x*d)
                                    yield 19, subst2
                        if pattern_index == 1:
                            pass
                            # State 73983
                            if len(subjects662) == 0:
                                pass
                                # State 73984
                                if len(subjects) == 0:
                                    pass
                                    # 23: cos(c + d*x**n)
                                    yield 23, subst2
                    subjects662.appendleft(tmp674)
            if len(subjects662) >= 1:
                tmp677 = subjects662.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp677)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72323
                    if len(subjects662) == 0:
                        pass
                        # State 72324
                        if len(subjects) == 0:
                            pass
                            # 21: cos(v)
                            yield 21, subst1
                subjects662.appendleft(tmp677)
            if len(subjects662) >= 1 and isinstance(subjects662[0], Add):
                tmp679 = subjects662.popleft()
                associative1 = tmp679
                associative_type1 = type(tmp679)
                subjects680 = deque(tmp679._args)
                matcher = CommutativeMatcher60075.get()
                tmp681 = subjects680
                subjects680 = []
                for s in tmp681:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp681, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 60081
                        if len(subjects662) == 0:
                            pass
                            # State 60082
                            if len(subjects) == 0:
                                pass
                                # 19: cos(c + x*d)
                                yield 19, subst1
                    if pattern_index == 1:
                        pass
                        # State 73995
                        if len(subjects662) == 0:
                            pass
                            # State 73996
                            if len(subjects) == 0:
                                pass
                                # 23: cos(c + d*x**n)
                                yield 23, subst1
                subjects662.appendleft(tmp679)
            subjects.appendleft(tmp661)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp682 = subjects.popleft()
            subjects683 = deque(tmp682._args)
            # State 79175
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 79176
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 79177
                    if len(subjects683) >= 1:
                        tmp686 = subjects683.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp686)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 79178
                            if len(subjects683) == 0:
                                pass
                                # State 79179
                                if len(subjects) == 0:
                                    pass
                                    # 24: tan(c + x*d)
                                    yield 24, subst3
                        subjects683.appendleft(tmp686)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 88064
                    if len(subjects683) >= 1 and isinstance(subjects683[0], Pow):
                        tmp689 = subjects683.popleft()
                        subjects690 = deque(tmp689._args)
                        # State 88065
                        if len(subjects690) >= 1:
                            tmp691 = subjects690.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp691)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 88066
                                if len(subjects690) >= 1:
                                    tmp693 = subjects690.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp693)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 88067
                                        if len(subjects690) == 0:
                                            pass
                                            # State 88068
                                            if len(subjects683) == 0:
                                                pass
                                                # State 88069
                                                if len(subjects) == 0:
                                                    pass
                                                    # 28: tan(c + d*x**n)
                                                    yield 28, subst4
                                    subjects690.appendleft(tmp693)
                            subjects690.appendleft(tmp691)
                        subjects683.appendleft(tmp689)
                if len(subjects683) >= 1 and isinstance(subjects683[0], Mul):
                    tmp695 = subjects683.popleft()
                    associative1 = tmp695
                    associative_type1 = type(tmp695)
                    subjects696 = deque(tmp695._args)
                    matcher = CommutativeMatcher79181.get()
                    tmp697 = subjects696
                    subjects696 = []
                    for s in tmp697:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp697, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 79182
                            if len(subjects683) == 0:
                                pass
                                # State 79183
                                if len(subjects) == 0:
                                    pass
                                    # 24: tan(c + x*d)
                                    yield 24, subst2
                        if pattern_index == 1:
                            pass
                            # State 88074
                            if len(subjects683) == 0:
                                pass
                                # State 88075
                                if len(subjects) == 0:
                                    pass
                                    # 28: tan(c + d*x**n)
                                    yield 28, subst2
                    subjects683.appendleft(tmp695)
            if len(subjects683) >= 1:
                tmp698 = subjects683.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp698)
                except ValueError:
                    pass
                else:
                    pass
                    # State 86948
                    if len(subjects683) == 0:
                        pass
                        # State 86949
                        if len(subjects) == 0:
                            pass
                            # 26: tan(v)
                            yield 26, subst1
                subjects683.appendleft(tmp698)
            if len(subjects683) >= 1 and isinstance(subjects683[0], Add):
                tmp700 = subjects683.popleft()
                associative1 = tmp700
                associative_type1 = type(tmp700)
                subjects701 = deque(tmp700._args)
                matcher = CommutativeMatcher79185.get()
                tmp702 = subjects701
                subjects701 = []
                for s in tmp702:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp702, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 79191
                        if len(subjects683) == 0:
                            pass
                            # State 79192
                            if len(subjects) == 0:
                                pass
                                # 24: tan(c + x*d)
                                yield 24, subst1
                    if pattern_index == 1:
                        pass
                        # State 88086
                        if len(subjects683) == 0:
                            pass
                            # State 88087
                            if len(subjects) == 0:
                                pass
                                # 28: tan(c + d*x**n)
                                yield 28, subst1
                subjects683.appendleft(tmp700)
            subjects.appendleft(tmp682)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp703 = subjects.popleft()
            subjects704 = deque(tmp703._args)
            # State 108242
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108243
                if len(subjects704) >= 1:
                    tmp706 = subjects704.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp706)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108244
                        if len(subjects704) == 0:
                            pass
                            # State 108245
                            if len(subjects) == 0:
                                pass
                                # 36: asin(x*c)
                                yield 36, subst2
                    subjects704.appendleft(tmp706)
            if len(subjects704) >= 1 and isinstance(subjects704[0], Mul):
                tmp708 = subjects704.popleft()
                associative1 = tmp708
                associative_type1 = type(tmp708)
                subjects709 = deque(tmp708._args)
                matcher = CommutativeMatcher108247.get()
                tmp710 = subjects709
                subjects709 = []
                for s in tmp710:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp710, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108248
                        if len(subjects704) == 0:
                            pass
                            # State 108249
                            if len(subjects) == 0:
                                pass
                                # 36: asin(x*c)
                                yield 36, subst1
                subjects704.appendleft(tmp708)
            if len(subjects704) >= 1 and isinstance(subjects704[0], Add):
                tmp711 = subjects704.popleft()
                associative1 = tmp711
                associative_type1 = type(tmp711)
                subjects712 = deque(tmp711._args)
                matcher = CommutativeMatcher110497.get()
                tmp713 = subjects712
                subjects712 = []
                for s in tmp713:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp713, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110503
                        if len(subjects704) == 0:
                            pass
                            # State 110504
                            if len(subjects) == 0:
                                pass
                                # 38: asin(c + x*d)
                                yield 38, subst1
                subjects704.appendleft(tmp711)
            subjects.appendleft(tmp703)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp714 = subjects.popleft()
            subjects715 = deque(tmp714._args)
            # State 108326
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108327
                if len(subjects715) >= 1:
                    tmp717 = subjects715.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp717)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108328
                        if len(subjects715) == 0:
                            pass
                            # State 108329
                            if len(subjects) == 0:
                                pass
                                # 37: acos(x*c)
                                yield 37, subst2
                    subjects715.appendleft(tmp717)
            if len(subjects715) >= 1 and isinstance(subjects715[0], Mul):
                tmp719 = subjects715.popleft()
                associative1 = tmp719
                associative_type1 = type(tmp719)
                subjects720 = deque(tmp719._args)
                matcher = CommutativeMatcher108331.get()
                tmp721 = subjects720
                subjects720 = []
                for s in tmp721:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp721, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108332
                        if len(subjects715) == 0:
                            pass
                            # State 108333
                            if len(subjects) == 0:
                                pass
                                # 37: acos(x*c)
                                yield 37, subst1
                subjects715.appendleft(tmp719)
            if len(subjects715) >= 1 and isinstance(subjects715[0], Add):
                tmp722 = subjects715.popleft()
                associative1 = tmp722
                associative_type1 = type(tmp722)
                subjects723 = deque(tmp722._args)
                matcher = CommutativeMatcher110584.get()
                tmp724 = subjects723
                subjects723 = []
                for s in tmp724:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp724, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110590
                        if len(subjects715) == 0:
                            pass
                            # State 110591
                            if len(subjects) == 0:
                                pass
                                # 39: acos(c + x*d)
                                yield 39, subst1
                subjects715.appendleft(tmp722)
            subjects.appendleft(tmp714)
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp725 = subjects.popleft()
            subjects726 = deque(tmp725._args)
            # State 112861
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 112862
                if len(subjects726) >= 1:
                    tmp728 = subjects726.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp728)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112863
                        if len(subjects726) == 0:
                            pass
                            # State 112864
                            if len(subjects) == 0:
                                pass
                                # 40: atan(x*c)
                                yield 40, subst2
                    subjects726.appendleft(tmp728)
            if len(subjects726) >= 1 and isinstance(subjects726[0], Mul):
                tmp730 = subjects726.popleft()
                associative1 = tmp730
                associative_type1 = type(tmp730)
                subjects731 = deque(tmp730._args)
                matcher = CommutativeMatcher112866.get()
                tmp732 = subjects731
                subjects731 = []
                for s in tmp732:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp732, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 112867
                        if len(subjects726) == 0:
                            pass
                            # State 112868
                            if len(subjects) == 0:
                                pass
                                # 40: atan(x*c)
                                yield 40, subst1
                subjects726.appendleft(tmp730)
            if len(subjects726) >= 1 and isinstance(subjects726[0], Add):
                tmp733 = subjects726.popleft()
                associative1 = tmp733
                associative_type1 = type(tmp733)
                subjects734 = deque(tmp733._args)
                matcher = CommutativeMatcher115727.get()
                tmp735 = subjects734
                subjects734 = []
                for s in tmp735:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp735, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115733
                        if len(subjects726) == 0:
                            pass
                            # State 115734
                            if len(subjects) == 0:
                                pass
                                # 42: atan(c + x*d)
                                yield 42, subst1
                subjects726.appendleft(tmp733)
            subjects.appendleft(tmp725)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp736 = subjects.popleft()
            subjects737 = deque(tmp736._args)
            # State 112942
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 112943
                if len(subjects737) >= 1:
                    tmp739 = subjects737.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp739)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112944
                        if len(subjects737) == 0:
                            pass
                            # State 112945
                            if len(subjects) == 0:
                                pass
                                # 41: acot(x*c)
                                yield 41, subst2
                    subjects737.appendleft(tmp739)
            if len(subjects737) >= 1 and isinstance(subjects737[0], Mul):
                tmp741 = subjects737.popleft()
                associative1 = tmp741
                associative_type1 = type(tmp741)
                subjects742 = deque(tmp741._args)
                matcher = CommutativeMatcher112947.get()
                tmp743 = subjects742
                subjects742 = []
                for s in tmp743:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp743, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 112948
                        if len(subjects737) == 0:
                            pass
                            # State 112949
                            if len(subjects) == 0:
                                pass
                                # 41: acot(x*c)
                                yield 41, subst1
                subjects737.appendleft(tmp741)
            if len(subjects737) >= 1 and isinstance(subjects737[0], Add):
                tmp744 = subjects737.popleft()
                associative1 = tmp744
                associative_type1 = type(tmp744)
                subjects745 = deque(tmp744._args)
                matcher = CommutativeMatcher115814.get()
                tmp746 = subjects745
                subjects745 = []
                for s in tmp746:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp746, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115820
                        if len(subjects737) == 0:
                            pass
                            # State 115821
                            if len(subjects) == 0:
                                pass
                                # 43: acot(c + x*d)
                                yield 43, subst1
                subjects737.appendleft(tmp744)
            subjects.appendleft(tmp736)
        if len(subjects) >= 1 and isinstance(subjects[0], asec):
            tmp747 = subjects.popleft()
            subjects748 = deque(tmp747._args)
            # State 119723
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119724
                if len(subjects748) >= 1:
                    tmp750 = subjects748.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp750)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119725
                        if len(subjects748) == 0:
                            pass
                            # State 119726
                            if len(subjects) == 0:
                                pass
                                # 44: asec(x*c)
                                yield 44, subst2
                    subjects748.appendleft(tmp750)
            if len(subjects748) >= 1 and isinstance(subjects748[0], Mul):
                tmp752 = subjects748.popleft()
                associative1 = tmp752
                associative_type1 = type(tmp752)
                subjects753 = deque(tmp752._args)
                matcher = CommutativeMatcher119728.get()
                tmp754 = subjects753
                subjects753 = []
                for s in tmp754:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp754, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119729
                        if len(subjects748) == 0:
                            pass
                            # State 119730
                            if len(subjects) == 0:
                                pass
                                # 44: asec(x*c)
                                yield 44, subst1
                subjects748.appendleft(tmp752)
            subjects.appendleft(tmp747)
        if len(subjects) >= 1 and isinstance(subjects[0], acsc):
            tmp755 = subjects.popleft()
            subjects756 = deque(tmp755._args)
            # State 119769
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119770
                if len(subjects756) >= 1:
                    tmp758 = subjects756.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp758)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119771
                        if len(subjects756) == 0:
                            pass
                            # State 119772
                            if len(subjects) == 0:
                                pass
                                # 45: acsc(x*c)
                                yield 45, subst2
                    subjects756.appendleft(tmp758)
            if len(subjects756) >= 1 and isinstance(subjects756[0], Mul):
                tmp760 = subjects756.popleft()
                associative1 = tmp760
                associative_type1 = type(tmp760)
                subjects761 = deque(tmp760._args)
                matcher = CommutativeMatcher119774.get()
                tmp762 = subjects761
                subjects761 = []
                for s in tmp762:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp762, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119775
                        if len(subjects756) == 0:
                            pass
                            # State 119776
                            if len(subjects) == 0:
                                pass
                                # 45: acsc(x*c)
                                yield 45, subst1
                subjects756.appendleft(tmp760)
            subjects.appendleft(tmp755)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp763 = subjects.popleft()
            subjects764 = deque(tmp763._args)
            # State 122055
            if len(subjects764) >= 1:
                tmp765 = subjects764.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp765)
                except ValueError:
                    pass
                else:
                    pass
                    # State 122056
                    if len(subjects764) == 0:
                        pass
                        # State 122057
                        if len(subjects) == 0:
                            pass
                            # 46: sinh(v)
                            yield 46, subst1
                subjects764.appendleft(tmp765)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 123668
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 123669
                    if len(subjects764) >= 1 and isinstance(subjects764[0], Pow):
                        tmp769 = subjects764.popleft()
                        subjects770 = deque(tmp769._args)
                        # State 123670
                        if len(subjects770) >= 1:
                            tmp771 = subjects770.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp771)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 123671
                                if len(subjects770) >= 1:
                                    tmp773 = subjects770.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp773)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 123672
                                        if len(subjects770) == 0:
                                            pass
                                            # State 123673
                                            if len(subjects764) == 0:
                                                pass
                                                # State 123674
                                                if len(subjects) == 0:
                                                    pass
                                                    # 49: sinh(c + d*x**n)
                                                    yield 49, subst4
                                    subjects770.appendleft(tmp773)
                            subjects770.appendleft(tmp771)
                        subjects764.appendleft(tmp769)
                if len(subjects764) >= 1 and isinstance(subjects764[0], Mul):
                    tmp775 = subjects764.popleft()
                    associative1 = tmp775
                    associative_type1 = type(tmp775)
                    subjects776 = deque(tmp775._args)
                    matcher = CommutativeMatcher123676.get()
                    tmp777 = subjects776
                    subjects776 = []
                    for s in tmp777:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp777, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 123681
                            if len(subjects764) == 0:
                                pass
                                # State 123682
                                if len(subjects) == 0:
                                    pass
                                    # 49: sinh(c + d*x**n)
                                    yield 49, subst2
                    subjects764.appendleft(tmp775)
            if len(subjects764) >= 1 and isinstance(subjects764[0], Add):
                tmp778 = subjects764.popleft()
                associative1 = tmp778
                associative_type1 = type(tmp778)
                subjects779 = deque(tmp778._args)
                matcher = CommutativeMatcher123684.get()
                tmp780 = subjects779
                subjects779 = []
                for s in tmp780:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp780, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 123697
                        if len(subjects764) == 0:
                            pass
                            # State 123698
                            if len(subjects) == 0:
                                pass
                                # 49: sinh(c + d*x**n)
                                yield 49, subst1
                subjects764.appendleft(tmp778)
            subjects.appendleft(tmp763)
        if len(subjects) >= 1 and isinstance(subjects[0], cosh):
            tmp781 = subjects.popleft()
            subjects782 = deque(tmp781._args)
            # State 122091
            if len(subjects782) >= 1:
                tmp783 = subjects782.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp783)
                except ValueError:
                    pass
                else:
                    pass
                    # State 122092
                    if len(subjects782) == 0:
                        pass
                        # State 122093
                        if len(subjects) == 0:
                            pass
                            # 47: cosh(v)
                            yield 47, subst1
                subjects782.appendleft(tmp783)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 122256
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122257
                    if len(subjects782) >= 1:
                        tmp787 = subjects782.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp787)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 122258
                            if len(subjects782) == 0:
                                pass
                                # State 122259
                                if len(subjects) == 0:
                                    pass
                                    # 48: cosh(e + x*d)
                                    yield 48, subst3
                        subjects782.appendleft(tmp787)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 123891
                    if len(subjects782) >= 1 and isinstance(subjects782[0], Pow):
                        tmp790 = subjects782.popleft()
                        subjects791 = deque(tmp790._args)
                        # State 123892
                        if len(subjects791) >= 1:
                            tmp792 = subjects791.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp792)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 123893
                                if len(subjects791) >= 1:
                                    tmp794 = subjects791.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp794)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 123894
                                        if len(subjects791) == 0:
                                            pass
                                            # State 123895
                                            if len(subjects782) == 0:
                                                pass
                                                # State 123896
                                                if len(subjects) == 0:
                                                    pass
                                                    # 50: cosh(c + d*x**n)
                                                    yield 50, subst4
                                    subjects791.appendleft(tmp794)
                            subjects791.appendleft(tmp792)
                        subjects782.appendleft(tmp790)
                if len(subjects782) >= 1 and isinstance(subjects782[0], Mul):
                    tmp796 = subjects782.popleft()
                    associative1 = tmp796
                    associative_type1 = type(tmp796)
                    subjects797 = deque(tmp796._args)
                    matcher = CommutativeMatcher122261.get()
                    tmp798 = subjects797
                    subjects797 = []
                    for s in tmp798:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp798, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122262
                            if len(subjects782) == 0:
                                pass
                                # State 122263
                                if len(subjects) == 0:
                                    pass
                                    # 48: cosh(e + x*d)
                                    yield 48, subst2
                        if pattern_index == 1:
                            pass
                            # State 123901
                            if len(subjects782) == 0:
                                pass
                                # State 123902
                                if len(subjects) == 0:
                                    pass
                                    # 50: cosh(c + d*x**n)
                                    yield 50, subst2
                    subjects782.appendleft(tmp796)
            if len(subjects782) >= 1 and isinstance(subjects782[0], Add):
                tmp799 = subjects782.popleft()
                associative1 = tmp799
                associative_type1 = type(tmp799)
                subjects800 = deque(tmp799._args)
                matcher = CommutativeMatcher122265.get()
                tmp801 = subjects800
                subjects800 = []
                for s in tmp801:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp801, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 122271
                        if len(subjects782) == 0:
                            pass
                            # State 122272
                            if len(subjects) == 0:
                                pass
                                # 48: cosh(e + x*d)
                                yield 48, subst1
                    if pattern_index == 1:
                        pass
                        # State 123913
                        if len(subjects782) == 0:
                            pass
                            # State 123914
                            if len(subjects) == 0:
                                pass
                                # 50: cosh(c + d*x**n)
                                yield 50, subst1
                subjects782.appendleft(tmp799)
            subjects.appendleft(tmp781)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp802 = subjects.popleft()
            subjects803 = deque(tmp802._args)
            # State 126268
            if len(subjects803) >= 1:
                tmp804 = subjects803.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp804)
                except ValueError:
                    pass
                else:
                    pass
                    # State 126269
                    if len(subjects803) == 0:
                        pass
                        # State 126270
                        if len(subjects) == 0:
                            pass
                            # 51: tanh(v)
                            yield 51, subst1
                subjects803.appendleft(tmp804)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 127594
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 127595
                    if len(subjects803) >= 1 and isinstance(subjects803[0], Pow):
                        tmp808 = subjects803.popleft()
                        subjects809 = deque(tmp808._args)
                        # State 127596
                        if len(subjects809) >= 1:
                            tmp810 = subjects809.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp810)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 127597
                                if len(subjects809) >= 1:
                                    tmp812 = subjects809.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp812)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 127598
                                        if len(subjects809) == 0:
                                            pass
                                            # State 127599
                                            if len(subjects803) == 0:
                                                pass
                                                # State 127600
                                                if len(subjects) == 0:
                                                    pass
                                                    # 54: tanh(c + d*x**n)
                                                    yield 54, subst4
                                    subjects809.appendleft(tmp812)
                            subjects809.appendleft(tmp810)
                        subjects803.appendleft(tmp808)
                if len(subjects803) >= 1 and isinstance(subjects803[0], Mul):
                    tmp814 = subjects803.popleft()
                    associative1 = tmp814
                    associative_type1 = type(tmp814)
                    subjects815 = deque(tmp814._args)
                    matcher = CommutativeMatcher127602.get()
                    tmp816 = subjects815
                    subjects815 = []
                    for s in tmp816:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp816, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 127607
                            if len(subjects803) == 0:
                                pass
                                # State 127608
                                if len(subjects) == 0:
                                    pass
                                    # 54: tanh(c + d*x**n)
                                    yield 54, subst2
                    subjects803.appendleft(tmp814)
            if len(subjects803) >= 1 and isinstance(subjects803[0], Add):
                tmp817 = subjects803.popleft()
                associative1 = tmp817
                associative_type1 = type(tmp817)
                subjects818 = deque(tmp817._args)
                matcher = CommutativeMatcher127610.get()
                tmp819 = subjects818
                subjects818 = []
                for s in tmp819:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp819, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 127623
                        if len(subjects803) == 0:
                            pass
                            # State 127624
                            if len(subjects) == 0:
                                pass
                                # 54: tanh(c + d*x**n)
                                yield 54, subst1
                subjects803.appendleft(tmp817)
            subjects.appendleft(tmp802)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp820 = subjects.popleft()
            subjects821 = deque(tmp820._args)
            # State 137981
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 137982
                if len(subjects821) >= 1:
                    tmp823 = subjects821.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp823)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137983
                        if len(subjects821) == 0:
                            pass
                            # State 137984
                            if len(subjects) == 0:
                                pass
                                # 58: asinh(x*c)
                                yield 58, subst2
                    subjects821.appendleft(tmp823)
            if len(subjects821) >= 1 and isinstance(subjects821[0], Mul):
                tmp825 = subjects821.popleft()
                associative1 = tmp825
                associative_type1 = type(tmp825)
                subjects826 = deque(tmp825._args)
                matcher = CommutativeMatcher137986.get()
                tmp827 = subjects826
                subjects826 = []
                for s in tmp827:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp827, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 137987
                        if len(subjects821) == 0:
                            pass
                            # State 137988
                            if len(subjects) == 0:
                                pass
                                # 58: asinh(x*c)
                                yield 58, subst1
                subjects821.appendleft(tmp825)
            if len(subjects821) >= 1 and isinstance(subjects821[0], Add):
                tmp828 = subjects821.popleft()
                associative1 = tmp828
                associative_type1 = type(tmp828)
                subjects829 = deque(tmp828._args)
                matcher = CommutativeMatcher140232.get()
                tmp830 = subjects829
                subjects829 = []
                for s in tmp830:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp830, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 140238
                        if len(subjects821) == 0:
                            pass
                            # State 140239
                            if len(subjects) == 0:
                                pass
                                # 60: asinh(c + x*d)
                                yield 60, subst1
                subjects821.appendleft(tmp828)
            subjects.appendleft(tmp820)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp831 = subjects.popleft()
            subjects832 = deque(tmp831._args)
            # State 138062
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138063
                if len(subjects832) >= 1:
                    tmp834 = subjects832.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp834)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138064
                        if len(subjects832) == 0:
                            pass
                            # State 138065
                            if len(subjects) == 0:
                                pass
                                # 59: acosh(x*c)
                                yield 59, subst2
                    subjects832.appendleft(tmp834)
            if len(subjects832) >= 1 and isinstance(subjects832[0], Mul):
                tmp836 = subjects832.popleft()
                associative1 = tmp836
                associative_type1 = type(tmp836)
                subjects837 = deque(tmp836._args)
                matcher = CommutativeMatcher138067.get()
                tmp838 = subjects837
                subjects837 = []
                for s in tmp838:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp838, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138068
                        if len(subjects832) == 0:
                            pass
                            # State 138069
                            if len(subjects) == 0:
                                pass
                                # 59: acosh(x*c)
                                yield 59, subst1
                subjects832.appendleft(tmp836)
            if len(subjects832) >= 1 and isinstance(subjects832[0], Add):
                tmp839 = subjects832.popleft()
                associative1 = tmp839
                associative_type1 = type(tmp839)
                subjects840 = deque(tmp839._args)
                matcher = CommutativeMatcher140319.get()
                tmp841 = subjects840
                subjects840 = []
                for s in tmp841:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp841, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 140325
                        if len(subjects832) == 0:
                            pass
                            # State 140326
                            if len(subjects) == 0:
                                pass
                                # 61: acosh(c + x*d)
                                yield 61, subst1
                subjects832.appendleft(tmp839)
            subjects.appendleft(tmp831)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp842 = subjects.popleft()
            subjects843 = deque(tmp842._args)
            # State 142493
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142494
                if len(subjects843) >= 1:
                    tmp845 = subjects843.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp845)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142495
                        if len(subjects843) == 0:
                            pass
                            # State 142496
                            if len(subjects) == 0:
                                pass
                                # 62: atanh(x*c)
                                yield 62, subst2
                    subjects843.appendleft(tmp845)
            if len(subjects843) >= 1 and isinstance(subjects843[0], Mul):
                tmp847 = subjects843.popleft()
                associative1 = tmp847
                associative_type1 = type(tmp847)
                subjects848 = deque(tmp847._args)
                matcher = CommutativeMatcher142498.get()
                tmp849 = subjects848
                subjects848 = []
                for s in tmp849:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp849, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142499
                        if len(subjects843) == 0:
                            pass
                            # State 142500
                            if len(subjects) == 0:
                                pass
                                # 62: atanh(x*c)
                                yield 62, subst1
                subjects843.appendleft(tmp847)
            if len(subjects843) >= 1 and isinstance(subjects843[0], Add):
                tmp850 = subjects843.popleft()
                associative1 = tmp850
                associative_type1 = type(tmp850)
                subjects851 = deque(tmp850._args)
                matcher = CommutativeMatcher144952.get()
                tmp852 = subjects851
                subjects851 = []
                for s in tmp852:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp852, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144958
                        if len(subjects843) == 0:
                            pass
                            # State 144959
                            if len(subjects) == 0:
                                pass
                                # 64: atanh(c + x*d)
                                yield 64, subst1
                subjects843.appendleft(tmp850)
            subjects.appendleft(tmp842)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp853 = subjects.popleft()
            subjects854 = deque(tmp853._args)
            # State 142574
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142575
                if len(subjects854) >= 1:
                    tmp856 = subjects854.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp856)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142576
                        if len(subjects854) == 0:
                            pass
                            # State 142577
                            if len(subjects) == 0:
                                pass
                                # 63: acoth(x*c)
                                yield 63, subst2
                    subjects854.appendleft(tmp856)
            if len(subjects854) >= 1 and isinstance(subjects854[0], Mul):
                tmp858 = subjects854.popleft()
                associative1 = tmp858
                associative_type1 = type(tmp858)
                subjects859 = deque(tmp858._args)
                matcher = CommutativeMatcher142579.get()
                tmp860 = subjects859
                subjects859 = []
                for s in tmp860:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp860, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142580
                        if len(subjects854) == 0:
                            pass
                            # State 142581
                            if len(subjects) == 0:
                                pass
                                # 63: acoth(x*c)
                                yield 63, subst1
                subjects854.appendleft(tmp858)
            if len(subjects854) >= 1 and isinstance(subjects854[0], Add):
                tmp861 = subjects854.popleft()
                associative1 = tmp861
                associative_type1 = type(tmp861)
                subjects862 = deque(tmp861._args)
                matcher = CommutativeMatcher145039.get()
                tmp863 = subjects862
                subjects862 = []
                for s in tmp863:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp863, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 145045
                        if len(subjects854) == 0:
                            pass
                            # State 145046
                            if len(subjects) == 0:
                                pass
                                # 65: acoth(c + x*d)
                                yield 65, subst1
                subjects854.appendleft(tmp861)
            subjects.appendleft(tmp853)
        if len(subjects) >= 1 and isinstance(subjects[0], asech):
            tmp864 = subjects.popleft()
            subjects865 = deque(tmp864._args)
            # State 148899
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 148900
                if len(subjects865) >= 1:
                    tmp867 = subjects865.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp867)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148901
                        if len(subjects865) == 0:
                            pass
                            # State 148902
                            if len(subjects) == 0:
                                pass
                                # 66: asech(x*c)
                                yield 66, subst2
                    subjects865.appendleft(tmp867)
            if len(subjects865) >= 1 and isinstance(subjects865[0], Mul):
                tmp869 = subjects865.popleft()
                associative1 = tmp869
                associative_type1 = type(tmp869)
                subjects870 = deque(tmp869._args)
                matcher = CommutativeMatcher148904.get()
                tmp871 = subjects870
                subjects870 = []
                for s in tmp871:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp871, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 148905
                        if len(subjects865) == 0:
                            pass
                            # State 148906
                            if len(subjects) == 0:
                                pass
                                # 66: asech(x*c)
                                yield 66, subst1
                subjects865.appendleft(tmp869)
            subjects.appendleft(tmp864)
        if len(subjects) >= 1 and isinstance(subjects[0], acsch):
            tmp872 = subjects.popleft()
            subjects873 = deque(tmp872._args)
            # State 148945
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 148946
                if len(subjects873) >= 1:
                    tmp875 = subjects873.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp875)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148947
                        if len(subjects873) == 0:
                            pass
                            # State 148948
                            if len(subjects) == 0:
                                pass
                                # 67: acsch(x*c)
                                yield 67, subst2
                    subjects873.appendleft(tmp875)
            if len(subjects873) >= 1 and isinstance(subjects873[0], Mul):
                tmp877 = subjects873.popleft()
                associative1 = tmp877
                associative_type1 = type(tmp877)
                subjects878 = deque(tmp877._args)
                matcher = CommutativeMatcher148950.get()
                tmp879 = subjects878
                subjects878 = []
                for s in tmp879:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp879, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 148951
                        if len(subjects873) == 0:
                            pass
                            # State 148952
                            if len(subjects) == 0:
                                pass
                                # 67: acsch(x*c)
                                yield 67, subst1
                subjects873.appendleft(tmp877)
            subjects.appendleft(tmp872)
        return
        yield


from .generated_part005708 import *
from .generated_part005696 import *
from .generated_part005876 import *
from .generated_part005720 import *
from .generated_part005695 import *
from .generated_part005718 import *
from .generated_part005873 import *
from collections import deque
from .generated_part005751 import *
from matchpy.utils import VariableWithCount
from .generated_part005726 import *
from .generated_part005691 import *
from .generated_part005709 import *
from .generated_part005680 import *
from .generated_part005702 import *
from .generated_part005721 import *
from .generated_part005867 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part005715 import *
from .generated_part005853 import *
from .generated_part005874 import *
from .generated_part005749 import *
from .generated_part005851 import *
from .generated_part005717 import *
from .generated_part005854 import *
from .generated_part005862 import *
from .generated_part005692 import *
from .generated_part005842 import *
from .generated_part005870 import *
from .generated_part005729 import *
from .generated_part005871 import *
from .generated_part005880 import *
from .generated_part005838 import *
from .generated_part005856 import *
from .generated_part005684 import *
from .generated_part005859 import *
from .generated_part005712 import *
from multiset import Multiset
from .generated_part005689 import *
from .generated_part005865 import *
from .generated_part005678 import *
from .generated_part005690 import *
from .generated_part005757 import *
from .generated_part005861 import *
from .generated_part005777 import *
from .generated_part005723 import *
from .generated_part005847 import *
from .generated_part005698 import *
from .generated_part005775 import *
from .generated_part005848 import *
from .generated_part005677 import *
from .generated_part005868 import *
from .generated_part005845 import *
from .generated_part005858 import *
from .generated_part005714 import *
from .generated_part005711 import *
from .generated_part005706 import *
from .generated_part005748 import *
from .generated_part005676 import *
from .generated_part005773 import *
from .generated_part005732 import *
from .generated_part005841 import *
from .generated_part005754 import *
from .generated_part005745 import *
from .generated_part005864 import *
from .generated_part005844 import *
from .generated_part005727 import *
from .generated_part005747 import *
from .generated_part005694 import *
from .generated_part005755 import *
from .generated_part005877 import *
from .generated_part005836 import *
from .generated_part005839 import *
from .generated_part005703 import *
from .generated_part005760 import *
from .generated_part005835 import *
from .generated_part005879 import *
from .generated_part005705 import *
from .generated_part005850 import *
from .generated_part005857 import *