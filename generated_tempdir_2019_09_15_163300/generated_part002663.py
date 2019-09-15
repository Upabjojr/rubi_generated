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


class CommutativeMatcher2359(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.2.1.1', 1, 1, None), Mul)
]),
    7: (7, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({13: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({14: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({15: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({16: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({17: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({18: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({19: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({20: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({21: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({22: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({23: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({24: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    27: (27, Multiset({25: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({26: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.4.1.1', 1, 1, None), Mul)
]),
    30: (30, Multiset({27: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    31: (31, Multiset({28: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({29: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    33: (33, Multiset({30: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({31: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({32: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    36: (36, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.4.1.0', 1, 1, None), Mul)
]),
    37: (37, Multiset({33: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    38: (38, Multiset({34: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({35: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({36: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    41: (41, Multiset({37: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    42: (42, Multiset({38: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    43: (43, Multiset({39: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    44: (44, Multiset({40: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    45: (45, Multiset({41: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    46: (46, Multiset({42: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    47: (47, Multiset({43: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    48: (48, Multiset({44: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    49: (49, Multiset({45: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    50: (50, Multiset({46: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    51: (51, Multiset({47: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    52: (52, Multiset({48: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    53: (53, Multiset({49: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    54: (54, Multiset({50: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    55: (55, Multiset({51: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    56: (56, Multiset({52: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    57: (57, Multiset({53: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    58: (58, Multiset({54: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    59: (59, Multiset({55: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    60: (60, Multiset({56: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    61: (61, Multiset({57: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    62: (62, Multiset({58: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    63: (63, Multiset({59: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    64: (64, Multiset({60: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    65: (65, Multiset({61: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    66: (66, Multiset({62: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    67: (67, Multiset({63: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    68: (68, Multiset({64: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    69: (69, Multiset({65: 1, 66: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    70: (70, Multiset({67: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    71: (71, Multiset({68: 1}), [
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
        if CommutativeMatcher2359._instance is None:
            CommutativeMatcher2359._instance = CommutativeMatcher2359()
        return CommutativeMatcher2359._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2358
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2360
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2361
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
            # State 15148
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 15149
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 15150
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.4.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 15151
                            if len(subjects6) >= 1:
                                tmp10 = subjects6.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.4.0', tmp10)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 15152
                                    if len(subjects6) == 0:
                                        pass
                                        # State 15153
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (F**(v*g))**n
                                            yield 5, subst4
                                subjects6.appendleft(tmp10)
                        if len(subjects6) >= 1 and isinstance(subjects6[0], Mul):
                            tmp12 = subjects6.popleft()
                            associative1 = tmp12
                            associative_type1 = type(tmp12)
                            subjects13 = deque(tmp12._args)
                            matcher = CommutativeMatcher15155.get()
                            tmp14 = subjects13
                            subjects13 = []
                            for s in tmp14:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp14, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 15156
                                    if len(subjects6) == 0:
                                        pass
                                        # State 15157
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (F**(v*g))**n
                                            yield 5, subst3
                            subjects6.appendleft(tmp12)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp15 = subjects.popleft()
            subjects16 = deque(tmp15._args)
            # State 2362
            if len(subjects16) >= 1:
                tmp17 = subjects16.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2363
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2364
                        if len(subjects16) == 0:
                            pass
                            # State 2365
                            if len(subjects) == 0:
                                pass
                                # 0: x**n
                                yield 0, subst2
                    if len(subjects16) >= 1:
                        tmp20 = subjects16.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp20)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2364
                            if len(subjects16) == 0:
                                pass
                                # State 2365
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects16.appendleft(tmp20)
                    if len(subjects16) >= 1:
                        tmp22 = subjects16.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp22)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 6389
                            if len(subjects16) == 0:
                                pass
                                # State 6390
                                if len(subjects) == 0:
                                    pass
                                    # 2: x**j
                                    yield 2, subst2
                        subjects16.appendleft(tmp22)
                    if len(subjects16) >= 1 and subjects16[0] == Integer(2):
                        tmp24 = subjects16.popleft()
                        # State 5096
                        if len(subjects16) == 0:
                            pass
                            # State 5097
                            if len(subjects) == 0:
                                pass
                                # 1: x**2
                                yield 1, subst1
                        subjects16.appendleft(tmp24)
                    if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                        tmp25 = subjects16.popleft()
                        associative1 = tmp25
                        associative_type1 = type(tmp25)
                        subjects26 = deque(tmp25._args)
                        matcher = CommutativeMatcher151070.get()
                        tmp27 = subjects26
                        subjects26 = []
                        for s in tmp27:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp27, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 151108
                                if len(subjects16) == 0:
                                    pass
                                    # State 151109
                                    if len(subjects) == 0:
                                        pass
                                        # 67: F**(c*sqrt(d + x*e)/sqrt(f + x*g))
                                        yield 67, subst2
                            if pattern_index == 1:
                                pass
                                # State 151391
                                if len(subjects16) == 0:
                                    pass
                                    # State 151392
                                    if len(subjects) == 0:
                                        pass
                                        # 68: F**(c*sqrt(x*e + 1)/sqrt(x*g + 1))
                                        yield 68, subst2
                        subjects16.appendleft(tmp25)
                subjects16.appendleft(tmp17)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10135
                if len(subjects16) >= 1 and isinstance(subjects16[0], Pow):
                    tmp29 = subjects16.popleft()
                    subjects30 = deque(tmp29._args)
                    # State 10136
                    if len(subjects30) >= 1:
                        tmp31 = subjects30.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1', tmp31)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10137
                            if len(subjects30) >= 1:
                                tmp33 = subjects30.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', tmp33)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10138
                                    if len(subjects30) == 0:
                                        pass
                                        # State 10139
                                        if len(subjects16) >= 1:
                                            tmp35 = subjects16.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2', tmp35)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 10140
                                                if len(subjects16) == 0:
                                                    pass
                                                    # State 10141
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (c*x**n)**q
                                                        yield 3, subst4
                                            subjects16.appendleft(tmp35)
                                subjects30.appendleft(tmp33)
                            if len(subjects30) >= 1 and subjects30[0] == Integer(-1):
                                tmp37 = subjects30.popleft()
                                # State 10651
                                if len(subjects30) == 0:
                                    pass
                                    # State 10652
                                    if len(subjects16) >= 1:
                                        tmp38 = subjects16.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', tmp38)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 10653
                                            if len(subjects16) == 0:
                                                pass
                                                # State 10654
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (c/x)**n
                                                    yield 4, subst3
                                        subjects16.appendleft(tmp38)
                                subjects30.appendleft(tmp37)
                        subjects30.appendleft(tmp31)
                    subjects16.appendleft(tmp29)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 150838
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 150839
                    if len(subjects16) >= 1:
                        tmp42 = subjects16.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp42)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 150840
                            if len(subjects16) >= 1 and subjects16[0] == Rational(1, 2):
                                tmp44 = subjects16.popleft()
                                # State 150841
                                if len(subjects16) == 0:
                                    pass
                                    # State 150842
                                    if len(subjects) == 0:
                                        pass
                                        # 65: sqrt(d + x*d)
                                        yield 65, subst3
                                subjects16.appendleft(tmp44)
                        subjects16.appendleft(tmp42)
                if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                    tmp45 = subjects16.popleft()
                    associative1 = tmp45
                    associative_type1 = type(tmp45)
                    subjects46 = deque(tmp45._args)
                    matcher = CommutativeMatcher150844.get()
                    tmp47 = subjects46
                    subjects46 = []
                    for s in tmp47:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp47, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 150845
                            if len(subjects16) >= 1 and subjects16[0] == Rational(1, 2):
                                tmp48 = subjects16.popleft()
                                # State 150846
                                if len(subjects16) == 0:
                                    pass
                                    # State 150847
                                    if len(subjects) == 0:
                                        pass
                                        # 65: sqrt(d + x*d)
                                        yield 65, subst2
                                subjects16.appendleft(tmp48)
                    subjects16.appendleft(tmp45)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 150858
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 150859
                    if len(subjects16) >= 1:
                        tmp51 = subjects16.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp51)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 150860
                            if len(subjects16) >= 1 and subjects16[0] == Rational(-1, 2):
                                tmp53 = subjects16.popleft()
                                # State 150861
                                if len(subjects16) == 0:
                                    pass
                                    # State 150862
                                    if len(subjects) == 0:
                                        pass
                                        # 66: 1/sqrt(f + x*g)
                                        yield 66, subst3
                                subjects16.appendleft(tmp53)
                        subjects16.appendleft(tmp51)
                if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                    tmp54 = subjects16.popleft()
                    associative1 = tmp54
                    associative_type1 = type(tmp54)
                    subjects55 = deque(tmp54._args)
                    matcher = CommutativeMatcher150864.get()
                    tmp56 = subjects55
                    subjects55 = []
                    for s in tmp56:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp56, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 150865
                            if len(subjects16) >= 1 and subjects16[0] == Rational(-1, 2):
                                tmp57 = subjects16.popleft()
                                # State 150866
                                if len(subjects16) == 0:
                                    pass
                                    # State 150867
                                    if len(subjects) == 0:
                                        pass
                                        # 66: 1/sqrt(f + x*g)
                                        yield 66, subst2
                                subjects16.appendleft(tmp57)
                    subjects16.appendleft(tmp54)
            if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                tmp58 = subjects16.popleft()
                associative1 = tmp58
                associative_type1 = type(tmp58)
                subjects59 = deque(tmp58._args)
                matcher = CommutativeMatcher10143.get()
                tmp60 = subjects59
                subjects59 = []
                for s in tmp60:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp60, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10148
                        if len(subjects16) >= 1:
                            tmp61 = []
                            tmp61.append(subjects16.popleft())
                            while True:
                                if len(tmp61) > 1:
                                    tmp62 = create_operation_expression(associative1, tmp61)
                                elif len(tmp61) == 1:
                                    tmp62 = tmp61[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp62)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10149
                                    if len(subjects16) == 0:
                                        pass
                                        # State 10150
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (c*x**n)**q
                                            yield 3, subst2
                                if len(subjects16) == 0:
                                    break
                                tmp61.append(subjects16.popleft())
                            subjects16.extendleft(reversed(tmp61))
                    if pattern_index == 1:
                        pass
                        # State 10657
                        if len(subjects16) >= 1:
                            tmp64 = []
                            tmp64.append(subjects16.popleft())
                            while True:
                                if len(tmp64) > 1:
                                    tmp65 = create_operation_expression(associative1, tmp64)
                                elif len(tmp64) == 1:
                                    tmp65 = tmp64[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp65)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10658
                                    if len(subjects16) == 0:
                                        pass
                                        # State 10659
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (c/x)**n
                                            yield 4, subst2
                                if len(subjects16) == 0:
                                    break
                                tmp64.append(subjects16.popleft())
                            subjects16.extendleft(reversed(tmp64))
                subjects16.appendleft(tmp58)
            if len(subjects16) >= 1 and isinstance(subjects16[0], Pow):
                tmp67 = subjects16.popleft()
                subjects68 = deque(tmp67._args)
                # State 15158
                if len(subjects68) >= 1:
                    tmp69 = subjects68.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp69)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 15159
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.4.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 15160
                            if len(subjects68) >= 1:
                                tmp72 = subjects68.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.4.0', tmp72)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 15161
                                    if len(subjects68) == 0:
                                        pass
                                        # State 15162
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.4', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 15163
                                            if len(subjects16) == 0:
                                                pass
                                                # State 15164
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (F**(v*g))**n
                                                    yield 5, subst4
                                        if len(subjects16) >= 1:
                                            tmp75 = subjects16.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.4', tmp75)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 15163
                                                if len(subjects16) == 0:
                                                    pass
                                                    # State 15164
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (F**(v*g))**n
                                                        yield 5, subst4
                                            subjects16.appendleft(tmp75)
                                subjects68.appendleft(tmp72)
                        if len(subjects68) >= 1 and isinstance(subjects68[0], Mul):
                            tmp77 = subjects68.popleft()
                            associative1 = tmp77
                            associative_type1 = type(tmp77)
                            subjects78 = deque(tmp77._args)
                            matcher = CommutativeMatcher15166.get()
                            tmp79 = subjects78
                            subjects78 = []
                            for s in tmp79:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp79, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 15167
                                    if len(subjects68) == 0:
                                        pass
                                        # State 15168
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.4', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 15169
                                            if len(subjects16) == 0:
                                                pass
                                                # State 15170
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (F**(v*g))**n
                                                    yield 5, subst3
                                        if len(subjects16) >= 1:
                                            tmp81 = subjects16.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.4', tmp81)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 15169
                                                if len(subjects16) == 0:
                                                    pass
                                                    # State 15170
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (F**(v*g))**n
                                                        yield 5, subst3
                                            subjects16.appendleft(tmp81)
                            subjects68.appendleft(tmp77)
                    subjects68.appendleft(tmp69)
                subjects16.appendleft(tmp67)
            if len(subjects16) >= 1 and isinstance(subjects16[0], tan):
                tmp83 = subjects16.popleft()
                subjects84 = deque(tmp83._args)
                # State 81305
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 81306
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 81307
                        if len(subjects84) >= 1:
                            tmp87 = subjects84.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp87)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 81308
                                if len(subjects84) == 0:
                                    pass
                                    # State 81309
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp89 = subjects16.popleft()
                                        # State 81310
                                        if len(subjects16) == 0:
                                            pass
                                            # State 81311
                                            if len(subjects) == 0:
                                                pass
                                                # 22: 1/tan(e + x*f)
                                                yield 22, subst3
                                        subjects16.appendleft(tmp89)
                            subjects84.appendleft(tmp87)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88174
                        if len(subjects84) >= 1 and isinstance(subjects84[0], Pow):
                            tmp91 = subjects84.popleft()
                            subjects92 = deque(tmp91._args)
                            # State 88175
                            if len(subjects92) >= 1:
                                tmp93 = subjects92.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.3.1.1', tmp93)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 88176
                                    if len(subjects92) >= 1:
                                        tmp95 = subjects92.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp95)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 88177
                                            if len(subjects92) == 0:
                                                pass
                                                # State 88178
                                                if len(subjects84) == 0:
                                                    pass
                                                    # State 88179
                                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                                        tmp97 = subjects16.popleft()
                                                        # State 88180
                                                        if len(subjects16) == 0:
                                                            pass
                                                            # State 88181
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 26: 1/tan(c + d*x**n)
                                                                yield 26, subst4
                                                        subjects16.appendleft(tmp97)
                                        subjects92.appendleft(tmp95)
                                subjects92.appendleft(tmp93)
                            subjects84.appendleft(tmp91)
                    if len(subjects84) >= 1 and isinstance(subjects84[0], Mul):
                        tmp98 = subjects84.popleft()
                        associative1 = tmp98
                        associative_type1 = type(tmp98)
                        subjects99 = deque(tmp98._args)
                        matcher = CommutativeMatcher81313.get()
                        tmp100 = subjects99
                        subjects99 = []
                        for s in tmp100:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp100, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 81314
                                if len(subjects84) == 0:
                                    pass
                                    # State 81315
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp101 = subjects16.popleft()
                                        # State 81316
                                        if len(subjects16) == 0:
                                            pass
                                            # State 81317
                                            if len(subjects) == 0:
                                                pass
                                                # 22: 1/tan(e + x*f)
                                                yield 22, subst2
                                        subjects16.appendleft(tmp101)
                            if pattern_index == 1:
                                pass
                                # State 88186
                                if len(subjects84) == 0:
                                    pass
                                    # State 88187
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp102 = subjects16.popleft()
                                        # State 88188
                                        if len(subjects16) == 0:
                                            pass
                                            # State 88189
                                            if len(subjects) == 0:
                                                pass
                                                # 26: 1/tan(c + d*x**n)
                                                yield 26, subst2
                                        subjects16.appendleft(tmp102)
                        subjects84.appendleft(tmp98)
                if len(subjects84) >= 1:
                    tmp103 = subjects84.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp103)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 86968
                        if len(subjects84) == 0:
                            pass
                            # State 86969
                            if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                tmp105 = subjects16.popleft()
                                # State 86970
                                if len(subjects16) == 0:
                                    pass
                                    # State 86971
                                    if len(subjects) == 0:
                                        pass
                                        # 24: 1/tan(v)
                                        yield 24, subst1
                                subjects16.appendleft(tmp105)
                    subjects84.appendleft(tmp103)
                if len(subjects84) >= 1 and isinstance(subjects84[0], Add):
                    tmp106 = subjects84.popleft()
                    associative1 = tmp106
                    associative_type1 = type(tmp106)
                    subjects107 = deque(tmp106._args)
                    matcher = CommutativeMatcher81319.get()
                    tmp108 = subjects107
                    subjects107 = []
                    for s in tmp108:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp108, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 81325
                            if len(subjects84) == 0:
                                pass
                                # State 81326
                                if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                    tmp109 = subjects16.popleft()
                                    # State 81327
                                    if len(subjects16) == 0:
                                        pass
                                        # State 81328
                                        if len(subjects) == 0:
                                            pass
                                            # 22: 1/tan(e + x*f)
                                            yield 22, subst1
                                    subjects16.appendleft(tmp109)
                        if pattern_index == 1:
                            pass
                            # State 88200
                            if len(subjects84) == 0:
                                pass
                                # State 88201
                                if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                    tmp110 = subjects16.popleft()
                                    # State 88202
                                    if len(subjects16) == 0:
                                        pass
                                        # State 88203
                                        if len(subjects) == 0:
                                            pass
                                            # 26: 1/tan(c + d*x**n)
                                            yield 26, subst1
                                    subjects16.appendleft(tmp110)
                    subjects84.appendleft(tmp106)
                subjects16.appendleft(tmp83)
            if len(subjects16) >= 1 and isinstance(subjects16[0], cos):
                tmp111 = subjects16.popleft()
                subjects112 = deque(tmp111._args)
                # State 93088
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 93089
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 93090
                        if len(subjects112) >= 1:
                            tmp115 = subjects112.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp115)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 93091
                                if len(subjects112) == 0:
                                    pass
                                    # State 93092
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp117 = subjects16.popleft()
                                        # State 93093
                                        if len(subjects16) == 0:
                                            pass
                                            # State 93094
                                            if len(subjects) == 0:
                                                pass
                                                # 27: 1/cos(e + x*f)
                                                yield 27, subst3
                                        subjects16.appendleft(tmp117)
                            subjects112.appendleft(tmp115)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98360
                        if len(subjects112) >= 1 and isinstance(subjects112[0], Pow):
                            tmp119 = subjects112.popleft()
                            subjects120 = deque(tmp119._args)
                            # State 98361
                            if len(subjects120) >= 1:
                                tmp121 = subjects120.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.3.1.1', tmp121)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 98362
                                    if len(subjects120) >= 1:
                                        tmp123 = subjects120.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp123)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 98363
                                            if len(subjects120) == 0:
                                                pass
                                                # State 98364
                                                if len(subjects112) == 0:
                                                    pass
                                                    # State 98365
                                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                                        tmp125 = subjects16.popleft()
                                                        # State 98366
                                                        if len(subjects16) == 0:
                                                            pass
                                                            # State 98367
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 31: 1/cos(c + d*x**n)
                                                                yield 31, subst4
                                                        subjects16.appendleft(tmp125)
                                        subjects120.appendleft(tmp123)
                                subjects120.appendleft(tmp121)
                            subjects112.appendleft(tmp119)
                    if len(subjects112) >= 1 and isinstance(subjects112[0], Mul):
                        tmp126 = subjects112.popleft()
                        associative1 = tmp126
                        associative_type1 = type(tmp126)
                        subjects127 = deque(tmp126._args)
                        matcher = CommutativeMatcher93096.get()
                        tmp128 = subjects127
                        subjects127 = []
                        for s in tmp128:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp128, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 93097
                                if len(subjects112) == 0:
                                    pass
                                    # State 93098
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp129 = subjects16.popleft()
                                        # State 93099
                                        if len(subjects16) == 0:
                                            pass
                                            # State 93100
                                            if len(subjects) == 0:
                                                pass
                                                # 27: 1/cos(e + x*f)
                                                yield 27, subst2
                                        subjects16.appendleft(tmp129)
                            if pattern_index == 1:
                                pass
                                # State 98372
                                if len(subjects112) == 0:
                                    pass
                                    # State 98373
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp130 = subjects16.popleft()
                                        # State 98374
                                        if len(subjects16) == 0:
                                            pass
                                            # State 98375
                                            if len(subjects) == 0:
                                                pass
                                                # 31: 1/cos(c + d*x**n)
                                                yield 31, subst2
                                        subjects16.appendleft(tmp130)
                        subjects112.appendleft(tmp126)
                if len(subjects112) >= 1:
                    tmp131 = subjects112.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp131)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 97322
                        if len(subjects112) == 0:
                            pass
                            # State 97323
                            if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                tmp133 = subjects16.popleft()
                                # State 97324
                                if len(subjects16) == 0:
                                    pass
                                    # State 97325
                                    if len(subjects) == 0:
                                        pass
                                        # 29: 1/cos(v)
                                        yield 29, subst1
                                subjects16.appendleft(tmp133)
                    subjects112.appendleft(tmp131)
                if len(subjects112) >= 1 and isinstance(subjects112[0], Add):
                    tmp134 = subjects112.popleft()
                    associative1 = tmp134
                    associative_type1 = type(tmp134)
                    subjects135 = deque(tmp134._args)
                    matcher = CommutativeMatcher93102.get()
                    tmp136 = subjects135
                    subjects135 = []
                    for s in tmp136:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp136, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 93108
                            if len(subjects112) == 0:
                                pass
                                # State 93109
                                if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                    tmp137 = subjects16.popleft()
                                    # State 93110
                                    if len(subjects16) == 0:
                                        pass
                                        # State 93111
                                        if len(subjects) == 0:
                                            pass
                                            # 27: 1/cos(e + x*f)
                                            yield 27, subst1
                                    subjects16.appendleft(tmp137)
                        if pattern_index == 1:
                            pass
                            # State 98386
                            if len(subjects112) == 0:
                                pass
                                # State 98387
                                if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                    tmp138 = subjects16.popleft()
                                    # State 98388
                                    if len(subjects16) == 0:
                                        pass
                                        # State 98389
                                        if len(subjects) == 0:
                                            pass
                                            # 31: 1/cos(c + d*x**n)
                                            yield 31, subst1
                                    subjects16.appendleft(tmp138)
                    subjects112.appendleft(tmp134)
                subjects16.appendleft(tmp111)
            if len(subjects16) >= 1 and isinstance(subjects16[0], sin):
                tmp139 = subjects16.popleft()
                subjects140 = deque(tmp139._args)
                # State 93274
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 93275
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 93276
                        if len(subjects140) >= 1:
                            tmp143 = subjects140.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp143)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 93277
                                if len(subjects140) == 0:
                                    pass
                                    # State 93278
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp145 = subjects16.popleft()
                                        # State 93279
                                        if len(subjects16) == 0:
                                            pass
                                            # State 93280
                                            if len(subjects) == 0:
                                                pass
                                                # 28: 1/sin(e + x*f)
                                                yield 28, subst3
                                        subjects16.appendleft(tmp145)
                            subjects140.appendleft(tmp143)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98619
                        if len(subjects140) >= 1 and isinstance(subjects140[0], Pow):
                            tmp147 = subjects140.popleft()
                            subjects148 = deque(tmp147._args)
                            # State 98620
                            if len(subjects148) >= 1:
                                tmp149 = subjects148.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.3.1.1', tmp149)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 98621
                                    if len(subjects148) >= 1:
                                        tmp151 = subjects148.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp151)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 98622
                                            if len(subjects148) == 0:
                                                pass
                                                # State 98623
                                                if len(subjects140) == 0:
                                                    pass
                                                    # State 98624
                                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                                        tmp153 = subjects16.popleft()
                                                        # State 98625
                                                        if len(subjects16) == 0:
                                                            pass
                                                            # State 98626
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 32: 1/sin(c + d*x**n)
                                                                yield 32, subst4
                                                        subjects16.appendleft(tmp153)
                                        subjects148.appendleft(tmp151)
                                subjects148.appendleft(tmp149)
                            subjects140.appendleft(tmp147)
                    if len(subjects140) >= 1 and isinstance(subjects140[0], Mul):
                        tmp154 = subjects140.popleft()
                        associative1 = tmp154
                        associative_type1 = type(tmp154)
                        subjects155 = deque(tmp154._args)
                        matcher = CommutativeMatcher93282.get()
                        tmp156 = subjects155
                        subjects155 = []
                        for s in tmp156:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp156, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 93283
                                if len(subjects140) == 0:
                                    pass
                                    # State 93284
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp157 = subjects16.popleft()
                                        # State 93285
                                        if len(subjects16) == 0:
                                            pass
                                            # State 93286
                                            if len(subjects) == 0:
                                                pass
                                                # 28: 1/sin(e + x*f)
                                                yield 28, subst2
                                        subjects16.appendleft(tmp157)
                            if pattern_index == 1:
                                pass
                                # State 98631
                                if len(subjects140) == 0:
                                    pass
                                    # State 98632
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp158 = subjects16.popleft()
                                        # State 98633
                                        if len(subjects16) == 0:
                                            pass
                                            # State 98634
                                            if len(subjects) == 0:
                                                pass
                                                # 32: 1/sin(c + d*x**n)
                                                yield 32, subst2
                                        subjects16.appendleft(tmp158)
                        subjects140.appendleft(tmp154)
                if len(subjects140) >= 1:
                    tmp159 = subjects140.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp159)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 97369
                        if len(subjects140) == 0:
                            pass
                            # State 97370
                            if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                tmp161 = subjects16.popleft()
                                # State 97371
                                if len(subjects16) == 0:
                                    pass
                                    # State 97372
                                    if len(subjects) == 0:
                                        pass
                                        # 30: 1/sin(v)
                                        yield 30, subst1
                                subjects16.appendleft(tmp161)
                    subjects140.appendleft(tmp159)
                if len(subjects140) >= 1 and isinstance(subjects140[0], Add):
                    tmp162 = subjects140.popleft()
                    associative1 = tmp162
                    associative_type1 = type(tmp162)
                    subjects163 = deque(tmp162._args)
                    matcher = CommutativeMatcher93288.get()
                    tmp164 = subjects163
                    subjects163 = []
                    for s in tmp164:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp164, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 93294
                            if len(subjects140) == 0:
                                pass
                                # State 93295
                                if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                    tmp165 = subjects16.popleft()
                                    # State 93296
                                    if len(subjects16) == 0:
                                        pass
                                        # State 93297
                                        if len(subjects) == 0:
                                            pass
                                            # 28: 1/sin(e + x*f)
                                            yield 28, subst1
                                    subjects16.appendleft(tmp165)
                        if pattern_index == 1:
                            pass
                            # State 98645
                            if len(subjects140) == 0:
                                pass
                                # State 98646
                                if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                    tmp166 = subjects16.popleft()
                                    # State 98647
                                    if len(subjects16) == 0:
                                        pass
                                        # State 98648
                                        if len(subjects) == 0:
                                            pass
                                            # 32: 1/sin(c + d*x**n)
                                            yield 32, subst1
                                    subjects16.appendleft(tmp166)
                    subjects140.appendleft(tmp162)
                subjects16.appendleft(tmp139)
            if len(subjects16) >= 1 and isinstance(subjects16[0], tanh):
                tmp167 = subjects16.popleft()
                subjects168 = deque(tmp167._args)
                # State 126290
                if len(subjects168) >= 1:
                    tmp169 = subjects168.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp169)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 126291
                        if len(subjects168) == 0:
                            pass
                            # State 126292
                            if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                tmp171 = subjects16.popleft()
                                # State 126293
                                if len(subjects16) == 0:
                                    pass
                                    # State 126294
                                    if len(subjects) == 0:
                                        pass
                                        # 49: 1/tanh(v)
                                        yield 49, subst1
                                subjects16.appendleft(tmp171)
                    subjects168.appendleft(tmp169)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 126448
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 126449
                        if len(subjects168) >= 1:
                            tmp174 = subjects168.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp174)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 126450
                                if len(subjects168) == 0:
                                    pass
                                    # State 126451
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp176 = subjects16.popleft()
                                        # State 126452
                                        if len(subjects16) == 0:
                                            pass
                                            # State 126453
                                            if len(subjects) == 0:
                                                pass
                                                # 50: 1/tanh(e + x*f)
                                                yield 50, subst3
                                        subjects16.appendleft(tmp176)
                            subjects168.appendleft(tmp174)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 127711
                        if len(subjects168) >= 1 and isinstance(subjects168[0], Pow):
                            tmp178 = subjects168.popleft()
                            subjects179 = deque(tmp178._args)
                            # State 127712
                            if len(subjects179) >= 1:
                                tmp180 = subjects179.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.3.1.1', tmp180)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 127713
                                    if len(subjects179) >= 1:
                                        tmp182 = subjects179.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp182)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 127714
                                            if len(subjects179) == 0:
                                                pass
                                                # State 127715
                                                if len(subjects168) == 0:
                                                    pass
                                                    # State 127716
                                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                                        tmp184 = subjects16.popleft()
                                                        # State 127717
                                                        if len(subjects16) == 0:
                                                            pass
                                                            # State 127718
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 52: 1/tanh(c + d*x**n)
                                                                yield 52, subst4
                                                        subjects16.appendleft(tmp184)
                                        subjects179.appendleft(tmp182)
                                subjects179.appendleft(tmp180)
                            subjects168.appendleft(tmp178)
                    if len(subjects168) >= 1 and isinstance(subjects168[0], Mul):
                        tmp185 = subjects168.popleft()
                        associative1 = tmp185
                        associative_type1 = type(tmp185)
                        subjects186 = deque(tmp185._args)
                        matcher = CommutativeMatcher126455.get()
                        tmp187 = subjects186
                        subjects186 = []
                        for s in tmp187:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp187, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 126456
                                if len(subjects168) == 0:
                                    pass
                                    # State 126457
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp188 = subjects16.popleft()
                                        # State 126458
                                        if len(subjects16) == 0:
                                            pass
                                            # State 126459
                                            if len(subjects) == 0:
                                                pass
                                                # 50: 1/tanh(e + x*f)
                                                yield 50, subst2
                                        subjects16.appendleft(tmp188)
                            if pattern_index == 1:
                                pass
                                # State 127723
                                if len(subjects168) == 0:
                                    pass
                                    # State 127724
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp189 = subjects16.popleft()
                                        # State 127725
                                        if len(subjects16) == 0:
                                            pass
                                            # State 127726
                                            if len(subjects) == 0:
                                                pass
                                                # 52: 1/tanh(c + d*x**n)
                                                yield 52, subst2
                                        subjects16.appendleft(tmp189)
                        subjects168.appendleft(tmp185)
                if len(subjects168) >= 1 and isinstance(subjects168[0], Add):
                    tmp190 = subjects168.popleft()
                    associative1 = tmp190
                    associative_type1 = type(tmp190)
                    subjects191 = deque(tmp190._args)
                    matcher = CommutativeMatcher126461.get()
                    tmp192 = subjects191
                    subjects191 = []
                    for s in tmp192:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp192, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 126467
                            if len(subjects168) == 0:
                                pass
                                # State 126468
                                if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                    tmp193 = subjects16.popleft()
                                    # State 126469
                                    if len(subjects16) == 0:
                                        pass
                                        # State 126470
                                        if len(subjects) == 0:
                                            pass
                                            # 50: 1/tanh(e + x*f)
                                            yield 50, subst1
                                    subjects16.appendleft(tmp193)
                        if pattern_index == 1:
                            pass
                            # State 127737
                            if len(subjects168) == 0:
                                pass
                                # State 127738
                                if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                    tmp194 = subjects16.popleft()
                                    # State 127739
                                    if len(subjects16) == 0:
                                        pass
                                        # State 127740
                                        if len(subjects) == 0:
                                            pass
                                            # 52: 1/tanh(c + d*x**n)
                                            yield 52, subst1
                                    subjects16.appendleft(tmp194)
                    subjects168.appendleft(tmp190)
                subjects16.appendleft(tmp167)
            if len(subjects16) >= 1 and isinstance(subjects16[0], cosh):
                tmp195 = subjects16.popleft()
                subjects196 = deque(tmp195._args)
                # State 130617
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 130618
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130619
                        if len(subjects196) >= 1 and isinstance(subjects196[0], Pow):
                            tmp199 = subjects196.popleft()
                            subjects200 = deque(tmp199._args)
                            # State 130620
                            if len(subjects200) >= 1:
                                tmp201 = subjects200.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.3.1.1', tmp201)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 130621
                                    if len(subjects200) >= 1:
                                        tmp203 = subjects200.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp203)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 130622
                                            if len(subjects200) == 0:
                                                pass
                                                # State 130623
                                                if len(subjects196) == 0:
                                                    pass
                                                    # State 130624
                                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                                        tmp205 = subjects16.popleft()
                                                        # State 130625
                                                        if len(subjects16) == 0:
                                                            pass
                                                            # State 130626
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 53: 1/cosh(c + d*x**n)
                                                                yield 53, subst4
                                                        subjects16.appendleft(tmp205)
                                        subjects200.appendleft(tmp203)
                                subjects200.appendleft(tmp201)
                            subjects196.appendleft(tmp199)
                    if len(subjects196) >= 1 and isinstance(subjects196[0], Mul):
                        tmp206 = subjects196.popleft()
                        associative1 = tmp206
                        associative_type1 = type(tmp206)
                        subjects207 = deque(tmp206._args)
                        matcher = CommutativeMatcher130628.get()
                        tmp208 = subjects207
                        subjects207 = []
                        for s in tmp208:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp208, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 130633
                                if len(subjects196) == 0:
                                    pass
                                    # State 130634
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp209 = subjects16.popleft()
                                        # State 130635
                                        if len(subjects16) == 0:
                                            pass
                                            # State 130636
                                            if len(subjects) == 0:
                                                pass
                                                # 53: 1/cosh(c + d*x**n)
                                                yield 53, subst2
                                        subjects16.appendleft(tmp209)
                        subjects196.appendleft(tmp206)
                if len(subjects196) >= 1 and isinstance(subjects196[0], Add):
                    tmp210 = subjects196.popleft()
                    associative1 = tmp210
                    associative_type1 = type(tmp210)
                    subjects211 = deque(tmp210._args)
                    matcher = CommutativeMatcher130638.get()
                    tmp212 = subjects211
                    subjects211 = []
                    for s in tmp212:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp212, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 130651
                            if len(subjects196) == 0:
                                pass
                                # State 130652
                                if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                    tmp213 = subjects16.popleft()
                                    # State 130653
                                    if len(subjects16) == 0:
                                        pass
                                        # State 130654
                                        if len(subjects) == 0:
                                            pass
                                            # 53: 1/cosh(c + d*x**n)
                                            yield 53, subst1
                                    subjects16.appendleft(tmp213)
                    subjects196.appendleft(tmp210)
                subjects16.appendleft(tmp195)
            if len(subjects16) >= 1 and isinstance(subjects16[0], sinh):
                tmp214 = subjects16.popleft()
                subjects215 = deque(tmp214._args)
                # State 130908
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 130909
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130910
                        if len(subjects215) >= 1 and isinstance(subjects215[0], Pow):
                            tmp218 = subjects215.popleft()
                            subjects219 = deque(tmp218._args)
                            # State 130911
                            if len(subjects219) >= 1:
                                tmp220 = subjects219.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.3.1.1', tmp220)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 130912
                                    if len(subjects219) >= 1:
                                        tmp222 = subjects219.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp222)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 130913
                                            if len(subjects219) == 0:
                                                pass
                                                # State 130914
                                                if len(subjects215) == 0:
                                                    pass
                                                    # State 130915
                                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                                        tmp224 = subjects16.popleft()
                                                        # State 130916
                                                        if len(subjects16) == 0:
                                                            pass
                                                            # State 130917
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 54: 1/sinh(c + d*x**n)
                                                                yield 54, subst4
                                                        subjects16.appendleft(tmp224)
                                        subjects219.appendleft(tmp222)
                                subjects219.appendleft(tmp220)
                            subjects215.appendleft(tmp218)
                    if len(subjects215) >= 1 and isinstance(subjects215[0], Mul):
                        tmp225 = subjects215.popleft()
                        associative1 = tmp225
                        associative_type1 = type(tmp225)
                        subjects226 = deque(tmp225._args)
                        matcher = CommutativeMatcher130919.get()
                        tmp227 = subjects226
                        subjects226 = []
                        for s in tmp227:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp227, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 130924
                                if len(subjects215) == 0:
                                    pass
                                    # State 130925
                                    if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                        tmp228 = subjects16.popleft()
                                        # State 130926
                                        if len(subjects16) == 0:
                                            pass
                                            # State 130927
                                            if len(subjects) == 0:
                                                pass
                                                # 54: 1/sinh(c + d*x**n)
                                                yield 54, subst2
                                        subjects16.appendleft(tmp228)
                        subjects215.appendleft(tmp225)
                if len(subjects215) >= 1 and isinstance(subjects215[0], Add):
                    tmp229 = subjects215.popleft()
                    associative1 = tmp229
                    associative_type1 = type(tmp229)
                    subjects230 = deque(tmp229._args)
                    matcher = CommutativeMatcher130929.get()
                    tmp231 = subjects230
                    subjects230 = []
                    for s in tmp231:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp231, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 130942
                            if len(subjects215) == 0:
                                pass
                                # State 130943
                                if len(subjects16) >= 1 and subjects16[0] == Integer(-1):
                                    tmp232 = subjects16.popleft()
                                    # State 130944
                                    if len(subjects16) == 0:
                                        pass
                                        # State 130945
                                        if len(subjects) == 0:
                                            pass
                                            # 54: 1/sinh(c + d*x**n)
                                            yield 54, subst1
                                    subjects16.appendleft(tmp232)
                    subjects215.appendleft(tmp229)
                subjects16.appendleft(tmp214)
            if len(subjects16) >= 1 and isinstance(subjects16[0], Add):
                tmp233 = subjects16.popleft()
                associative1 = tmp233
                associative_type1 = type(tmp233)
                subjects234 = deque(tmp233._args)
                matcher = CommutativeMatcher150849.get()
                tmp235 = subjects234
                subjects234 = []
                for s in tmp235:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp235, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 150855
                        if len(subjects16) >= 1 and subjects16[0] == Rational(1, 2):
                            tmp236 = subjects16.popleft()
                            # State 150856
                            if len(subjects16) == 0:
                                pass
                                # State 150857
                                if len(subjects) == 0:
                                    pass
                                    # 65: sqrt(d + x*d)
                                    yield 65, subst1
                            subjects16.appendleft(tmp236)
                    if pattern_index == 1:
                        pass
                        # State 150871
                        if len(subjects16) >= 1 and subjects16[0] == Rational(-1, 2):
                            tmp237 = subjects16.popleft()
                            # State 150872
                            if len(subjects16) == 0:
                                pass
                                # State 150873
                                if len(subjects) == 0:
                                    pass
                                    # 66: 1/sqrt(f + x*g)
                                    yield 66, subst1
                            subjects16.appendleft(tmp237)
                subjects16.appendleft(tmp233)
            subjects.appendleft(tmp15)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp238 = subjects.popleft()
            subjects239 = deque(tmp238._args)
            # State 22542
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 22543
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 22544
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 22545
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 22546
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 22547
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22548
                                    if len(subjects239) >= 1:
                                        tmp246 = subjects239.popleft()
                                        subst7 = Substitution(subst6)
                                        try:
                                            subst7.try_add_variable('i2.2.1.2.2.2.1.0', tmp246)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22549
                                            if len(subjects239) == 0:
                                                pass
                                                # State 22550
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: log(c*(d*(e + x*f)**p)**q)
                                                    yield 6, subst7
                                        subjects239.appendleft(tmp246)
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 34008
                                    if len(subjects239) >= 1 and isinstance(subjects239[0], Pow):
                                        tmp249 = subjects239.popleft()
                                        subjects250 = deque(tmp249._args)
                                        # State 34009
                                        if len(subjects250) >= 1:
                                            tmp251 = subjects250.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2.2.1.1', tmp251)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34010
                                                if len(subjects250) >= 1:
                                                    tmp253 = subjects250.popleft()
                                                    subst8 = Substitution(subst7)
                                                    try:
                                                        subst8.try_add_variable('i2.2.1.2.2.2.1.2', tmp253)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34011
                                                        if len(subjects250) == 0:
                                                            pass
                                                            # State 34012
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 34013
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                    yield 11, subst8
                                                    subjects250.appendleft(tmp253)
                                            subjects250.appendleft(tmp251)
                                        subjects239.appendleft(tmp249)
                                if len(subjects239) >= 1 and isinstance(subjects239[0], Mul):
                                    tmp255 = subjects239.popleft()
                                    associative1 = tmp255
                                    associative_type1 = type(tmp255)
                                    subjects256 = deque(tmp255._args)
                                    matcher = CommutativeMatcher22552.get()
                                    tmp257 = subjects256
                                    subjects256 = []
                                    for s in tmp257:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp257, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 22553
                                            if len(subjects239) == 0:
                                                pass
                                                # State 22554
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: log(c*(d*(e + x*f)**p)**q)
                                                    yield 6, subst6
                                        if pattern_index == 1:
                                            pass
                                            # State 34018
                                            if len(subjects239) == 0:
                                                pass
                                                # State 34019
                                                if len(subjects) == 0:
                                                    pass
                                                    # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                    yield 11, subst6
                                    subjects239.appendleft(tmp255)
                            if len(subjects239) >= 1:
                                tmp258 = subjects239.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.1', tmp258)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45442
                                    if len(subjects239) == 0:
                                        pass
                                        # State 45443
                                        if len(subjects) == 0:
                                            pass
                                            # 13: log(c*(d*v**p)**q)
                                            yield 13, subst5
                                subjects239.appendleft(tmp258)
                            if len(subjects239) >= 1 and isinstance(subjects239[0], Add):
                                tmp260 = subjects239.popleft()
                                associative1 = tmp260
                                associative_type1 = type(tmp260)
                                subjects261 = deque(tmp260._args)
                                matcher = CommutativeMatcher22556.get()
                                tmp262 = subjects261
                                subjects261 = []
                                for s in tmp262:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp262, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 22562
                                        if len(subjects239) == 0:
                                            pass
                                            # State 22563
                                            if len(subjects) == 0:
                                                pass
                                                # 6: log(c*(d*(e + x*f)**p)**q)
                                                yield 6, subst5
                                    if pattern_index == 1:
                                        pass
                                        # State 28526
                                        if len(subjects239) == 0:
                                            pass
                                            # State 28527
                                            if len(subjects) == 0:
                                                pass
                                                # 9: log(c*(d*(e + f*x**m)**p)**q)
                                                yield 9, subst5
                                    if pattern_index == 2:
                                        pass
                                        # State 34020
                                        if len(subjects239) == 0:
                                            pass
                                            # State 34021
                                            if len(subjects) == 0:
                                                pass
                                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                yield 11, subst5
                                    if pattern_index == 3:
                                        pass
                                        # State 43690
                                        if len(subjects239) == 0:
                                            pass
                                            # State 43691
                                            if len(subjects) == 0:
                                                pass
                                                # 12: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                yield 12, subst5
                                subjects239.appendleft(tmp260)
                            if len(subjects239) >= 1 and isinstance(subjects239[0], Mul):
                                tmp263 = subjects239.popleft()
                                associative1 = tmp263
                                associative_type1 = type(tmp263)
                                subjects264 = deque(tmp263._args)
                                matcher = CommutativeMatcher30515.get()
                                tmp265 = subjects264
                                subjects264 = []
                                for s in tmp265:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp265, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 30539
                                        if len(subjects239) == 0:
                                            pass
                                            # State 30540
                                            if len(subjects) == 0:
                                                pass
                                                # 10: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                yield 10, subst5
                                subjects239.appendleft(tmp263)
                        if len(subjects239) >= 1 and isinstance(subjects239[0], Pow):
                            tmp266 = subjects239.popleft()
                            subjects267 = deque(tmp266._args)
                            # State 22564
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 22565
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22566
                                    if len(subjects267) >= 1:
                                        tmp270 = subjects267.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp270)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22567
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22568
                                                if len(subjects267) == 0:
                                                    pass
                                                    # State 22569
                                                    if len(subjects239) == 0:
                                                        pass
                                                        # State 22570
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: log(c*(d*(e + x*f)**p)**q)
                                                            yield 6, subst7
                                            if len(subjects267) >= 1:
                                                tmp273 = subjects267.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.2.2.2', tmp273)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22568
                                                    if len(subjects267) == 0:
                                                        pass
                                                        # State 22569
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 22570
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: log(c*(d*(e + x*f)**p)**q)
                                                                yield 6, subst7
                                                subjects267.appendleft(tmp273)
                                        subjects267.appendleft(tmp270)
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 34022
                                    if len(subjects267) >= 1 and isinstance(subjects267[0], Pow):
                                        tmp276 = subjects267.popleft()
                                        subjects277 = deque(tmp276._args)
                                        # State 34023
                                        if len(subjects277) >= 1:
                                            tmp278 = subjects277.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.1', tmp278)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34024
                                                if len(subjects277) >= 1:
                                                    tmp280 = subjects277.popleft()
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2.2.1.2', tmp280)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34025
                                                        if len(subjects277) == 0:
                                                            pass
                                                            # State 34026
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i2.2.1.2.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 34027
                                                                if len(subjects267) == 0:
                                                                    pass
                                                                    # State 34028
                                                                    if len(subjects239) == 0:
                                                                        pass
                                                                        # State 34029
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                            yield 11, subst8
                                                            if len(subjects267) >= 1:
                                                                tmp283 = subjects267.popleft()
                                                                subst8 = Substitution(subst7)
                                                                try:
                                                                    subst8.try_add_variable('i2.2.1.2.2.2', tmp283)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 34027
                                                                    if len(subjects267) == 0:
                                                                        pass
                                                                        # State 34028
                                                                        if len(subjects239) == 0:
                                                                            pass
                                                                            # State 34029
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                                yield 11, subst8
                                                                subjects267.appendleft(tmp283)
                                                    subjects277.appendleft(tmp280)
                                            subjects277.appendleft(tmp278)
                                        subjects267.appendleft(tmp276)
                                if len(subjects267) >= 1 and isinstance(subjects267[0], Mul):
                                    tmp285 = subjects267.popleft()
                                    associative1 = tmp285
                                    associative_type1 = type(tmp285)
                                    subjects286 = deque(tmp285._args)
                                    matcher = CommutativeMatcher22572.get()
                                    tmp287 = subjects286
                                    subjects286 = []
                                    for s in tmp287:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp287, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 22573
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22574
                                                if len(subjects267) == 0:
                                                    pass
                                                    # State 22575
                                                    if len(subjects239) == 0:
                                                        pass
                                                        # State 22576
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: log(c*(d*(e + x*f)**p)**q)
                                                            yield 6, subst6
                                            if len(subjects267) >= 1:
                                                tmp289 = []
                                                tmp289.append(subjects267.popleft())
                                                while True:
                                                    if len(tmp289) > 1:
                                                        tmp290 = create_operation_expression(associative1, tmp289)
                                                    elif len(tmp289) == 1:
                                                        tmp290 = tmp289[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', tmp290)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 22574
                                                        if len(subjects267) == 0:
                                                            pass
                                                            # State 22575
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 22576
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 6, subst6
                                                    if len(subjects267) == 0:
                                                        break
                                                    tmp289.append(subjects267.popleft())
                                                subjects267.extendleft(reversed(tmp289))
                                        if pattern_index == 1:
                                            pass
                                            # State 34034
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34035
                                                if len(subjects267) == 0:
                                                    pass
                                                    # State 34036
                                                    if len(subjects239) == 0:
                                                        pass
                                                        # State 34037
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                            yield 11, subst6
                                            if len(subjects267) >= 1:
                                                tmp293 = []
                                                tmp293.append(subjects267.popleft())
                                                while True:
                                                    if len(tmp293) > 1:
                                                        tmp294 = create_operation_expression(associative1, tmp293)
                                                    elif len(tmp293) == 1:
                                                        tmp294 = tmp293[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', tmp294)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34035
                                                        if len(subjects267) == 0:
                                                            pass
                                                            # State 34036
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 34037
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                    yield 11, subst6
                                                    if len(subjects267) == 0:
                                                        break
                                                    tmp293.append(subjects267.popleft())
                                                subjects267.extendleft(reversed(tmp293))
                                    subjects267.appendleft(tmp285)
                            if len(subjects267) >= 1:
                                tmp296 = subjects267.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.1', tmp296)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25530
                                    if len(subjects267) >= 1:
                                        tmp298 = subjects267.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp298)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25531
                                            if len(subjects267) == 0:
                                                pass
                                                # State 25532
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 25533
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: log(c*(d*v**p)**q)
                                                        yield 7, subst5
                                        subjects267.appendleft(tmp298)
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45444
                                        if len(subjects267) == 0:
                                            pass
                                            # State 45445
                                            if len(subjects239) == 0:
                                                pass
                                                # State 45446
                                                if len(subjects) == 0:
                                                    pass
                                                    # 13: log(c*(d*v**p)**q)
                                                    yield 13, subst5
                                    if len(subjects267) >= 1:
                                        tmp301 = subjects267.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp301)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45444
                                            if len(subjects267) == 0:
                                                pass
                                                # State 45445
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 45446
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 13: log(c*(d*v**p)**q)
                                                        yield 13, subst5
                                        subjects267.appendleft(tmp301)
                                subjects267.appendleft(tmp296)
                            if len(subjects267) >= 1 and isinstance(subjects267[0], Add):
                                tmp303 = subjects267.popleft()
                                associative1 = tmp303
                                associative_type1 = type(tmp303)
                                subjects304 = deque(tmp303._args)
                                matcher = CommutativeMatcher22578.get()
                                tmp305 = subjects304
                                subjects304 = []
                                for s in tmp305:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp305, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 22584
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22585
                                            if len(subjects267) == 0:
                                                pass
                                                # State 22586
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 22587
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: log(c*(d*(e + x*f)**p)**q)
                                                        yield 6, subst5
                                        if len(subjects267) >= 1:
                                            tmp307 = []
                                            tmp307.append(subjects267.popleft())
                                            while True:
                                                if len(tmp307) > 1:
                                                    tmp308 = create_operation_expression(associative1, tmp307)
                                                elif len(tmp307) == 1:
                                                    tmp308 = tmp307[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp308)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22585
                                                    if len(subjects267) == 0:
                                                        pass
                                                        # State 22586
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 22587
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: log(c*(d*(e + x*f)**p)**q)
                                                                yield 6, subst5
                                                if len(subjects267) == 0:
                                                    break
                                                tmp307.append(subjects267.popleft())
                                            subjects267.extendleft(reversed(tmp307))
                                    if pattern_index == 1:
                                        pass
                                        # State 28538
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28539
                                            if len(subjects267) == 0:
                                                pass
                                                # State 28540
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 28541
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 9: log(c*(d*(e + f*x**m)**p)**q)
                                                        yield 9, subst5
                                        if len(subjects267) >= 1:
                                            tmp311 = []
                                            tmp311.append(subjects267.popleft())
                                            while True:
                                                if len(tmp311) > 1:
                                                    tmp312 = create_operation_expression(associative1, tmp311)
                                                elif len(tmp311) == 1:
                                                    tmp312 = tmp311[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp312)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28539
                                                    if len(subjects267) == 0:
                                                        pass
                                                        # State 28540
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 28541
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 9: log(c*(d*(e + f*x**m)**p)**q)
                                                                yield 9, subst5
                                                if len(subjects267) == 0:
                                                    break
                                                tmp311.append(subjects267.popleft())
                                            subjects267.extendleft(reversed(tmp311))
                                    if pattern_index == 2:
                                        pass
                                        # State 34038
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 34039
                                            if len(subjects267) == 0:
                                                pass
                                                # State 34040
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 34041
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                        yield 11, subst5
                                        if len(subjects267) >= 1:
                                            tmp315 = []
                                            tmp315.append(subjects267.popleft())
                                            while True:
                                                if len(tmp315) > 1:
                                                    tmp316 = create_operation_expression(associative1, tmp315)
                                                elif len(tmp315) == 1:
                                                    tmp316 = tmp315[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp316)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 34039
                                                    if len(subjects267) == 0:
                                                        pass
                                                        # State 34040
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 34041
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                yield 11, subst5
                                                if len(subjects267) == 0:
                                                    break
                                                tmp315.append(subjects267.popleft())
                                            subjects267.extendleft(reversed(tmp315))
                                    if pattern_index == 3:
                                        pass
                                        # State 43699
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43700
                                            if len(subjects267) == 0:
                                                pass
                                                # State 43701
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 43702
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 12: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                        yield 12, subst5
                                        if len(subjects267) >= 1:
                                            tmp319 = []
                                            tmp319.append(subjects267.popleft())
                                            while True:
                                                if len(tmp319) > 1:
                                                    tmp320 = create_operation_expression(associative1, tmp319)
                                                elif len(tmp319) == 1:
                                                    tmp320 = tmp319[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp320)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 43700
                                                    if len(subjects267) == 0:
                                                        pass
                                                        # State 43701
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 43702
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 12: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                                yield 12, subst5
                                                if len(subjects267) == 0:
                                                    break
                                                tmp319.append(subjects267.popleft())
                                            subjects267.extendleft(reversed(tmp319))
                                subjects267.appendleft(tmp303)
                            if len(subjects267) >= 1 and isinstance(subjects267[0], Mul):
                                tmp322 = subjects267.popleft()
                                associative1 = tmp322
                                associative_type1 = type(tmp322)
                                subjects323 = deque(tmp322._args)
                                matcher = CommutativeMatcher30542.get()
                                tmp324 = subjects323
                                subjects323 = []
                                for s in tmp324:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp324, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 30566
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 30567
                                            if len(subjects267) == 0:
                                                pass
                                                # State 30568
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 30569
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 10: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                        yield 10, subst5
                                        if len(subjects267) >= 1:
                                            tmp326 = []
                                            tmp326.append(subjects267.popleft())
                                            while True:
                                                if len(tmp326) > 1:
                                                    tmp327 = create_operation_expression(associative1, tmp326)
                                                elif len(tmp326) == 1:
                                                    tmp327 = tmp326[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp327)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 30567
                                                    if len(subjects267) == 0:
                                                        pass
                                                        # State 30568
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 30569
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 10: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                                yield 10, subst5
                                                if len(subjects267) == 0:
                                                    break
                                                tmp326.append(subjects267.popleft())
                                            subjects267.extendleft(reversed(tmp326))
                                subjects267.appendleft(tmp322)
                            subjects239.appendleft(tmp266)
                    if len(subjects239) >= 1:
                        tmp329 = subjects239.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1', tmp329)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53225
                            if len(subjects239) == 0:
                                pass
                                # State 53226
                                if len(subjects) == 0:
                                    pass
                                    # 14: log(c*RFx**p)
                                    yield 14, subst3
                        subjects239.appendleft(tmp329)
                    if len(subjects239) >= 1 and isinstance(subjects239[0], Mul):
                        tmp331 = subjects239.popleft()
                        associative1 = tmp331
                        associative_type1 = type(tmp331)
                        subjects332 = deque(tmp331._args)
                        matcher = CommutativeMatcher22589.get()
                        tmp333 = subjects332
                        subjects332 = []
                        for s in tmp333:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp333, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 22626
                                if len(subjects239) == 0:
                                    pass
                                    # State 22627
                                    if len(subjects) == 0:
                                        pass
                                        # 6: log(c*(d*(e + x*f)**p)**q)
                                        yield 6, subst3
                            if pattern_index == 1:
                                pass
                                # State 25537
                                if len(subjects239) == 0:
                                    pass
                                    # State 25538
                                    if len(subjects) == 0:
                                        pass
                                        # 7: log(c*(d*v**p)**q)
                                        yield 7, subst3
                            if pattern_index == 2:
                                pass
                                # State 28566
                                if len(subjects239) == 0:
                                    pass
                                    # State 28567
                                    if len(subjects) == 0:
                                        pass
                                        # 9: log(c*(d*(e + f*x**m)**p)**q)
                                        yield 9, subst3
                            if pattern_index == 3:
                                pass
                                # State 30624
                                if len(subjects239) == 0:
                                    pass
                                    # State 30625
                                    if len(subjects) == 0:
                                        pass
                                        # 10: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                        yield 10, subst3
                            if pattern_index == 4:
                                pass
                                # State 34070
                                if len(subjects239) == 0:
                                    pass
                                    # State 34071
                                    if len(subjects) == 0:
                                        pass
                                        # 11: log(c*(d*(e + f*x**m)**p)**q)
                                        yield 11, subst3
                            if pattern_index == 5:
                                pass
                                # State 43721
                                if len(subjects239) == 0:
                                    pass
                                    # State 43722
                                    if len(subjects) == 0:
                                        pass
                                        # 12: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                        yield 12, subst3
                            if pattern_index == 6:
                                pass
                                # State 45450
                                if len(subjects239) == 0:
                                    pass
                                    # State 45451
                                    if len(subjects) == 0:
                                        pass
                                        # 13: log(c*(d*v**p)**q)
                                        yield 13, subst3
                        subjects239.appendleft(tmp331)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 26032
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 26033
                        if len(subjects239) >= 1:
                            tmp336 = subjects239.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.1.1.0', tmp336)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 26034
                                if len(subjects239) == 0:
                                    pass
                                    # State 26035
                                    if len(subjects) == 0:
                                        pass
                                        # 8: log(c*(e + x*f))
                                        yield 8, subst4
                            subjects239.appendleft(tmp336)
                    if len(subjects239) >= 1 and isinstance(subjects239[0], Mul):
                        tmp338 = subjects239.popleft()
                        associative1 = tmp338
                        associative_type1 = type(tmp338)
                        subjects339 = deque(tmp338._args)
                        matcher = CommutativeMatcher26037.get()
                        tmp340 = subjects339
                        subjects339 = []
                        for s in tmp340:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp340, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 26038
                                if len(subjects239) == 0:
                                    pass
                                    # State 26039
                                    if len(subjects) == 0:
                                        pass
                                        # 8: log(c*(e + x*f))
                                        yield 8, subst3
                        subjects239.appendleft(tmp338)
                if len(subjects239) >= 1 and isinstance(subjects239[0], Pow):
                    tmp341 = subjects239.popleft()
                    subjects342 = deque(tmp341._args)
                    # State 22628
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 22629
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 22630
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 22631
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22632
                                    if len(subjects342) >= 1:
                                        tmp347 = subjects342.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp347)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22633
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22634
                                                if len(subjects342) == 0:
                                                    pass
                                                    # State 22635
                                                    if len(subjects239) == 0:
                                                        pass
                                                        # State 22636
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: log(c*(d*(e + x*f)**p)**q)
                                                            yield 6, subst7
                                            if len(subjects342) >= 1:
                                                tmp350 = subjects342.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.2.2', tmp350)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22634
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 22635
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 22636
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: log(c*(d*(e + x*f)**p)**q)
                                                                yield 6, subst7
                                                subjects342.appendleft(tmp350)
                                        subjects342.appendleft(tmp347)
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 34072
                                    if len(subjects342) >= 1 and isinstance(subjects342[0], Pow):
                                        tmp353 = subjects342.popleft()
                                        subjects354 = deque(tmp353._args)
                                        # State 34073
                                        if len(subjects354) >= 1:
                                            tmp355 = subjects354.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.1', tmp355)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34074
                                                if len(subjects354) >= 1:
                                                    tmp357 = subjects354.popleft()
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2.2.1.2', tmp357)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34075
                                                        if len(subjects354) == 0:
                                                            pass
                                                            # State 34076
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 34077
                                                                if len(subjects342) == 0:
                                                                    pass
                                                                    # State 34078
                                                                    if len(subjects239) == 0:
                                                                        pass
                                                                        # State 34079
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                            yield 11, subst8
                                                            if len(subjects342) >= 1:
                                                                tmp360 = subjects342.popleft()
                                                                subst8 = Substitution(subst7)
                                                                try:
                                                                    subst8.try_add_variable('i2.2.1.2.2', tmp360)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 34077
                                                                    if len(subjects342) == 0:
                                                                        pass
                                                                        # State 34078
                                                                        if len(subjects239) == 0:
                                                                            pass
                                                                            # State 34079
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                                yield 11, subst8
                                                                subjects342.appendleft(tmp360)
                                                    subjects354.appendleft(tmp357)
                                            subjects354.appendleft(tmp355)
                                        subjects342.appendleft(tmp353)
                                if len(subjects342) >= 1 and isinstance(subjects342[0], Mul):
                                    tmp362 = subjects342.popleft()
                                    associative1 = tmp362
                                    associative_type1 = type(tmp362)
                                    subjects363 = deque(tmp362._args)
                                    matcher = CommutativeMatcher22638.get()
                                    tmp364 = subjects363
                                    subjects363 = []
                                    for s in tmp364:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp364, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 22639
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22640
                                                if len(subjects342) == 0:
                                                    pass
                                                    # State 22641
                                                    if len(subjects239) == 0:
                                                        pass
                                                        # State 22642
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: log(c*(d*(e + x*f)**p)**q)
                                                            yield 6, subst6
                                            if len(subjects342) >= 1:
                                                tmp366 = []
                                                tmp366.append(subjects342.popleft())
                                                while True:
                                                    if len(tmp366) > 1:
                                                        tmp367 = create_operation_expression(associative1, tmp366)
                                                    elif len(tmp366) == 1:
                                                        tmp367 = tmp366[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp367)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 22640
                                                        if len(subjects342) == 0:
                                                            pass
                                                            # State 22641
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 22642
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 6, subst6
                                                    if len(subjects342) == 0:
                                                        break
                                                    tmp366.append(subjects342.popleft())
                                                subjects342.extendleft(reversed(tmp366))
                                        if pattern_index == 1:
                                            pass
                                            # State 34084
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34085
                                                if len(subjects342) == 0:
                                                    pass
                                                    # State 34086
                                                    if len(subjects239) == 0:
                                                        pass
                                                        # State 34087
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                            yield 11, subst6
                                            if len(subjects342) >= 1:
                                                tmp370 = []
                                                tmp370.append(subjects342.popleft())
                                                while True:
                                                    if len(tmp370) > 1:
                                                        tmp371 = create_operation_expression(associative1, tmp370)
                                                    elif len(tmp370) == 1:
                                                        tmp371 = tmp370[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp371)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34085
                                                        if len(subjects342) == 0:
                                                            pass
                                                            # State 34086
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 34087
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                    yield 11, subst6
                                                    if len(subjects342) == 0:
                                                        break
                                                    tmp370.append(subjects342.popleft())
                                                subjects342.extendleft(reversed(tmp370))
                                    subjects342.appendleft(tmp362)
                            if len(subjects342) >= 1:
                                tmp373 = subjects342.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.1', tmp373)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45452
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45453
                                        if len(subjects342) == 0:
                                            pass
                                            # State 45454
                                            if len(subjects239) == 0:
                                                pass
                                                # State 45455
                                                if len(subjects) == 0:
                                                    pass
                                                    # 13: log(c*(d*v**p)**q)
                                                    yield 13, subst5
                                    if len(subjects342) >= 1:
                                        tmp376 = subjects342.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', tmp376)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45453
                                            if len(subjects342) == 0:
                                                pass
                                                # State 45454
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 45455
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 13: log(c*(d*v**p)**q)
                                                        yield 13, subst5
                                        subjects342.appendleft(tmp376)
                                subjects342.appendleft(tmp373)
                            if len(subjects342) >= 1 and isinstance(subjects342[0], Add):
                                tmp378 = subjects342.popleft()
                                associative1 = tmp378
                                associative_type1 = type(tmp378)
                                subjects379 = deque(tmp378._args)
                                matcher = CommutativeMatcher22644.get()
                                tmp380 = subjects379
                                subjects379 = []
                                for s in tmp380:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp380, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 22650
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22651
                                            if len(subjects342) == 0:
                                                pass
                                                # State 22652
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 22653
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: log(c*(d*(e + x*f)**p)**q)
                                                        yield 6, subst5
                                        if len(subjects342) >= 1:
                                            tmp382 = []
                                            tmp382.append(subjects342.popleft())
                                            while True:
                                                if len(tmp382) > 1:
                                                    tmp383 = create_operation_expression(associative1, tmp382)
                                                elif len(tmp382) == 1:
                                                    tmp383 = tmp382[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp383)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22651
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 22652
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 22653
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: log(c*(d*(e + x*f)**p)**q)
                                                                yield 6, subst5
                                                if len(subjects342) == 0:
                                                    break
                                                tmp382.append(subjects342.popleft())
                                            subjects342.extendleft(reversed(tmp382))
                                    if pattern_index == 1:
                                        pass
                                        # State 28578
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28579
                                            if len(subjects342) == 0:
                                                pass
                                                # State 28580
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 28581
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 9: log(c*(d*(e + f*x**m)**p)**q)
                                                        yield 9, subst5
                                        if len(subjects342) >= 1:
                                            tmp386 = []
                                            tmp386.append(subjects342.popleft())
                                            while True:
                                                if len(tmp386) > 1:
                                                    tmp387 = create_operation_expression(associative1, tmp386)
                                                elif len(tmp386) == 1:
                                                    tmp387 = tmp386[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp387)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28579
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 28580
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 28581
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 9: log(c*(d*(e + f*x**m)**p)**q)
                                                                yield 9, subst5
                                                if len(subjects342) == 0:
                                                    break
                                                tmp386.append(subjects342.popleft())
                                            subjects342.extendleft(reversed(tmp386))
                                    if pattern_index == 2:
                                        pass
                                        # State 34088
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 34089
                                            if len(subjects342) == 0:
                                                pass
                                                # State 34090
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 34091
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                        yield 11, subst5
                                        if len(subjects342) >= 1:
                                            tmp390 = []
                                            tmp390.append(subjects342.popleft())
                                            while True:
                                                if len(tmp390) > 1:
                                                    tmp391 = create_operation_expression(associative1, tmp390)
                                                elif len(tmp390) == 1:
                                                    tmp391 = tmp390[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp391)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 34089
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 34090
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 34091
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                yield 11, subst5
                                                if len(subjects342) == 0:
                                                    break
                                                tmp390.append(subjects342.popleft())
                                            subjects342.extendleft(reversed(tmp390))
                                    if pattern_index == 3:
                                        pass
                                        # State 43730
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43731
                                            if len(subjects342) == 0:
                                                pass
                                                # State 43732
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 43733
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 12: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                        yield 12, subst5
                                        if len(subjects342) >= 1:
                                            tmp394 = []
                                            tmp394.append(subjects342.popleft())
                                            while True:
                                                if len(tmp394) > 1:
                                                    tmp395 = create_operation_expression(associative1, tmp394)
                                                elif len(tmp394) == 1:
                                                    tmp395 = tmp394[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp395)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 43731
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 43732
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 43733
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 12: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                                yield 12, subst5
                                                if len(subjects342) == 0:
                                                    break
                                                tmp394.append(subjects342.popleft())
                                            subjects342.extendleft(reversed(tmp394))
                                subjects342.appendleft(tmp378)
                            if len(subjects342) >= 1 and isinstance(subjects342[0], Mul):
                                tmp397 = subjects342.popleft()
                                associative1 = tmp397
                                associative_type1 = type(tmp397)
                                subjects398 = deque(tmp397._args)
                                matcher = CommutativeMatcher30627.get()
                                tmp399 = subjects398
                                subjects398 = []
                                for s in tmp399:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp399, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 30651
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 30652
                                            if len(subjects342) == 0:
                                                pass
                                                # State 30653
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 30654
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 10: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                        yield 10, subst5
                                        if len(subjects342) >= 1:
                                            tmp401 = []
                                            tmp401.append(subjects342.popleft())
                                            while True:
                                                if len(tmp401) > 1:
                                                    tmp402 = create_operation_expression(associative1, tmp401)
                                                elif len(tmp401) == 1:
                                                    tmp402 = tmp401[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp402)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 30652
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 30653
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 30654
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 10: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                                yield 10, subst5
                                                if len(subjects342) == 0:
                                                    break
                                                tmp401.append(subjects342.popleft())
                                            subjects342.extendleft(reversed(tmp401))
                                subjects342.appendleft(tmp397)
                        if len(subjects342) >= 1 and isinstance(subjects342[0], Pow):
                            tmp404 = subjects342.popleft()
                            subjects405 = deque(tmp404._args)
                            # State 22654
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 22655
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22656
                                    if len(subjects405) >= 1:
                                        tmp408 = subjects405.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp408)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22657
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22658
                                                if len(subjects405) == 0:
                                                    pass
                                                    # State 22659
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 22660
                                                        if len(subjects342) == 0:
                                                            pass
                                                            # State 22661
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 22662
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 6, subst7
                                                    if len(subjects342) >= 1:
                                                        tmp412 = subjects342.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', tmp412)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 22660
                                                            if len(subjects342) == 0:
                                                                pass
                                                                # State 22661
                                                                if len(subjects239) == 0:
                                                                    pass
                                                                    # State 22662
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 6: log(c*(d*(e + x*f)**p)**q)
                                                                        yield 6, subst7
                                                        subjects342.appendleft(tmp412)
                                            if len(subjects405) >= 1:
                                                tmp414 = subjects405.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2.2', tmp414)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22658
                                                    if len(subjects405) == 0:
                                                        pass
                                                        # State 22659
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 22660
                                                            if len(subjects342) == 0:
                                                                pass
                                                                # State 22661
                                                                if len(subjects239) == 0:
                                                                    pass
                                                                    # State 22662
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 6: log(c*(d*(e + x*f)**p)**q)
                                                                        yield 6, subst7
                                                        if len(subjects342) >= 1:
                                                            tmp417 = subjects342.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2', tmp417)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 22660
                                                                if len(subjects342) == 0:
                                                                    pass
                                                                    # State 22661
                                                                    if len(subjects239) == 0:
                                                                        pass
                                                                        # State 22662
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 6: log(c*(d*(e + x*f)**p)**q)
                                                                            yield 6, subst7
                                                            subjects342.appendleft(tmp417)
                                                subjects405.appendleft(tmp414)
                                        subjects405.appendleft(tmp408)
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 34092
                                    if len(subjects405) >= 1 and isinstance(subjects405[0], Pow):
                                        tmp420 = subjects405.popleft()
                                        subjects421 = deque(tmp420._args)
                                        # State 34093
                                        if len(subjects421) >= 1:
                                            tmp422 = subjects421.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2.1.1', tmp422)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34094
                                                if len(subjects421) >= 1:
                                                    tmp424 = subjects421.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2.1.2', tmp424)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34095
                                                        if len(subjects421) == 0:
                                                            pass
                                                            # State 34096
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 34097
                                                                if len(subjects405) == 0:
                                                                    pass
                                                                    # State 34098
                                                                    subst8 = Substitution(subst7)
                                                                    try:
                                                                        subst8.try_add_variable('i2.2.1.2.2', 1)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 34099
                                                                        if len(subjects342) == 0:
                                                                            pass
                                                                            # State 34100
                                                                            if len(subjects239) == 0:
                                                                                pass
                                                                                # State 34101
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                                    yield 11, subst8
                                                                    if len(subjects342) >= 1:
                                                                        tmp428 = subjects342.popleft()
                                                                        subst8 = Substitution(subst7)
                                                                        try:
                                                                            subst8.try_add_variable('i2.2.1.2.2', tmp428)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            # State 34099
                                                                            if len(subjects342) == 0:
                                                                                pass
                                                                                # State 34100
                                                                                if len(subjects239) == 0:
                                                                                    pass
                                                                                    # State 34101
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                                        yield 11, subst8
                                                                        subjects342.appendleft(tmp428)
                                                            if len(subjects405) >= 1:
                                                                tmp430 = subjects405.popleft()
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2.2', tmp430)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 34097
                                                                    if len(subjects405) == 0:
                                                                        pass
                                                                        # State 34098
                                                                        subst8 = Substitution(subst7)
                                                                        try:
                                                                            subst8.try_add_variable('i2.2.1.2.2', 1)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            # State 34099
                                                                            if len(subjects342) == 0:
                                                                                pass
                                                                                # State 34100
                                                                                if len(subjects239) == 0:
                                                                                    pass
                                                                                    # State 34101
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                                        yield 11, subst8
                                                                        if len(subjects342) >= 1:
                                                                            tmp433 = subjects342.popleft()
                                                                            subst8 = Substitution(subst7)
                                                                            try:
                                                                                subst8.try_add_variable('i2.2.1.2.2', tmp433)
                                                                            except ValueError:
                                                                                pass
                                                                            else:
                                                                                pass
                                                                                # State 34099
                                                                                if len(subjects342) == 0:
                                                                                    pass
                                                                                    # State 34100
                                                                                    if len(subjects239) == 0:
                                                                                        pass
                                                                                        # State 34101
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                                            yield 11, subst8
                                                                            subjects342.appendleft(tmp433)
                                                                subjects405.appendleft(tmp430)
                                                    subjects421.appendleft(tmp424)
                                            subjects421.appendleft(tmp422)
                                        subjects405.appendleft(tmp420)
                                if len(subjects405) >= 1 and isinstance(subjects405[0], Mul):
                                    tmp435 = subjects405.popleft()
                                    associative1 = tmp435
                                    associative_type1 = type(tmp435)
                                    subjects436 = deque(tmp435._args)
                                    matcher = CommutativeMatcher22664.get()
                                    tmp437 = subjects436
                                    subjects436 = []
                                    for s in tmp437:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp437, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 22665
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22666
                                                if len(subjects405) == 0:
                                                    pass
                                                    # State 22667
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 22668
                                                        if len(subjects342) == 0:
                                                            pass
                                                            # State 22669
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 22670
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 6, subst6
                                                    if len(subjects342) >= 1:
                                                        tmp440 = subjects342.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp440)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 22668
                                                            if len(subjects342) == 0:
                                                                pass
                                                                # State 22669
                                                                if len(subjects239) == 0:
                                                                    pass
                                                                    # State 22670
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 6: log(c*(d*(e + x*f)**p)**q)
                                                                        yield 6, subst6
                                                        subjects342.appendleft(tmp440)
                                            if len(subjects405) >= 1:
                                                tmp442 = []
                                                tmp442.append(subjects405.popleft())
                                                while True:
                                                    if len(tmp442) > 1:
                                                        tmp443 = create_operation_expression(associative1, tmp442)
                                                    elif len(tmp442) == 1:
                                                        tmp443 = tmp442[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2.2', tmp443)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 22666
                                                        if len(subjects405) == 0:
                                                            pass
                                                            # State 22667
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 22668
                                                                if len(subjects342) == 0:
                                                                    pass
                                                                    # State 22669
                                                                    if len(subjects239) == 0:
                                                                        pass
                                                                        # State 22670
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 6: log(c*(d*(e + x*f)**p)**q)
                                                                            yield 6, subst6
                                                            if len(subjects342) >= 1:
                                                                tmp446 = subjects342.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2.1.2.2', tmp446)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 22668
                                                                    if len(subjects342) == 0:
                                                                        pass
                                                                        # State 22669
                                                                        if len(subjects239) == 0:
                                                                            pass
                                                                            # State 22670
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 6: log(c*(d*(e + x*f)**p)**q)
                                                                                yield 6, subst6
                                                                subjects342.appendleft(tmp446)
                                                    if len(subjects405) == 0:
                                                        break
                                                    tmp442.append(subjects405.popleft())
                                                subjects405.extendleft(reversed(tmp442))
                                        if pattern_index == 1:
                                            pass
                                            # State 34106
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34107
                                                if len(subjects405) == 0:
                                                    pass
                                                    # State 34108
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34109
                                                        if len(subjects342) == 0:
                                                            pass
                                                            # State 34110
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 34111
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                    yield 11, subst6
                                                    if len(subjects342) >= 1:
                                                        tmp450 = subjects342.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp450)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 34109
                                                            if len(subjects342) == 0:
                                                                pass
                                                                # State 34110
                                                                if len(subjects239) == 0:
                                                                    pass
                                                                    # State 34111
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                        yield 11, subst6
                                                        subjects342.appendleft(tmp450)
                                            if len(subjects405) >= 1:
                                                tmp452 = []
                                                tmp452.append(subjects405.popleft())
                                                while True:
                                                    if len(tmp452) > 1:
                                                        tmp453 = create_operation_expression(associative1, tmp452)
                                                    elif len(tmp452) == 1:
                                                        tmp453 = tmp452[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2.2', tmp453)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34107
                                                        if len(subjects405) == 0:
                                                            pass
                                                            # State 34108
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 34109
                                                                if len(subjects342) == 0:
                                                                    pass
                                                                    # State 34110
                                                                    if len(subjects239) == 0:
                                                                        pass
                                                                        # State 34111
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                            yield 11, subst6
                                                            if len(subjects342) >= 1:
                                                                tmp456 = subjects342.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2.1.2.2', tmp456)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 34109
                                                                    if len(subjects342) == 0:
                                                                        pass
                                                                        # State 34110
                                                                        if len(subjects239) == 0:
                                                                            pass
                                                                            # State 34111
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                                yield 11, subst6
                                                                subjects342.appendleft(tmp456)
                                                    if len(subjects405) == 0:
                                                        break
                                                    tmp452.append(subjects405.popleft())
                                                subjects405.extendleft(reversed(tmp452))
                                    subjects405.appendleft(tmp435)
                            if len(subjects405) >= 1:
                                tmp458 = subjects405.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.1', tmp458)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25539
                                    if len(subjects405) >= 1:
                                        tmp460 = subjects405.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp460)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25540
                                            if len(subjects405) == 0:
                                                pass
                                                # State 25541
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 25542
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 25543
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 25544
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 7: log(c*(d*v**p)**q)
                                                                yield 7, subst5
                                                if len(subjects342) >= 1:
                                                    tmp463 = subjects342.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp463)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 25542
                                                        if len(subjects342) == 0:
                                                            pass
                                                            # State 25543
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 25544
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 7: log(c*(d*v**p)**q)
                                                                    yield 7, subst5
                                                    subjects342.appendleft(tmp463)
                                        subjects405.appendleft(tmp460)
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45456
                                        if len(subjects405) == 0:
                                            pass
                                            # State 45457
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45458
                                                if len(subjects342) == 0:
                                                    pass
                                                    # State 45459
                                                    if len(subjects239) == 0:
                                                        pass
                                                        # State 45460
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 13: log(c*(d*v**p)**q)
                                                            yield 13, subst5
                                            if len(subjects342) >= 1:
                                                tmp467 = subjects342.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp467)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 45458
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 45459
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 45460
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 13: log(c*(d*v**p)**q)
                                                                yield 13, subst5
                                                subjects342.appendleft(tmp467)
                                    if len(subjects405) >= 1:
                                        tmp469 = subjects405.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp469)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45456
                                            if len(subjects405) == 0:
                                                pass
                                                # State 45457
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 45458
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 45459
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 45460
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 13: log(c*(d*v**p)**q)
                                                                yield 13, subst5
                                                if len(subjects342) >= 1:
                                                    tmp472 = subjects342.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp472)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 45458
                                                        if len(subjects342) == 0:
                                                            pass
                                                            # State 45459
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 45460
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 13: log(c*(d*v**p)**q)
                                                                    yield 13, subst5
                                                    subjects342.appendleft(tmp472)
                                        subjects405.appendleft(tmp469)
                                subjects405.appendleft(tmp458)
                            if len(subjects405) >= 1 and isinstance(subjects405[0], Add):
                                tmp474 = subjects405.popleft()
                                associative1 = tmp474
                                associative_type1 = type(tmp474)
                                subjects475 = deque(tmp474._args)
                                matcher = CommutativeMatcher22672.get()
                                tmp476 = subjects475
                                subjects475 = []
                                for s in tmp476:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp476, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 22678
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22679
                                            if len(subjects405) == 0:
                                                pass
                                                # State 22680
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22681
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 22682
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 22683
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: log(c*(d*(e + x*f)**p)**q)
                                                                yield 6, subst5
                                                if len(subjects342) >= 1:
                                                    tmp479 = subjects342.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp479)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 22681
                                                        if len(subjects342) == 0:
                                                            pass
                                                            # State 22682
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 22683
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: log(c*(d*(e + x*f)**p)**q)
                                                                    yield 6, subst5
                                                    subjects342.appendleft(tmp479)
                                        if len(subjects405) >= 1:
                                            tmp481 = []
                                            tmp481.append(subjects405.popleft())
                                            while True:
                                                if len(tmp481) > 1:
                                                    tmp482 = create_operation_expression(associative1, tmp481)
                                                elif len(tmp481) == 1:
                                                    tmp482 = tmp481[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp482)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22679
                                                    if len(subjects405) == 0:
                                                        pass
                                                        # State 22680
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 22681
                                                            if len(subjects342) == 0:
                                                                pass
                                                                # State 22682
                                                                if len(subjects239) == 0:
                                                                    pass
                                                                    # State 22683
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 6: log(c*(d*(e + x*f)**p)**q)
                                                                        yield 6, subst5
                                                        if len(subjects342) >= 1:
                                                            tmp485 = subjects342.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp485)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 22681
                                                                if len(subjects342) == 0:
                                                                    pass
                                                                    # State 22682
                                                                    if len(subjects239) == 0:
                                                                        pass
                                                                        # State 22683
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 6: log(c*(d*(e + x*f)**p)**q)
                                                                            yield 6, subst5
                                                            subjects342.appendleft(tmp485)
                                                if len(subjects405) == 0:
                                                    break
                                                tmp481.append(subjects405.popleft())
                                            subjects405.extendleft(reversed(tmp481))
                                    if pattern_index == 1:
                                        pass
                                        # State 28592
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28593
                                            if len(subjects405) == 0:
                                                pass
                                                # State 28594
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28595
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 28596
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 28597
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 9: log(c*(d*(e + f*x**m)**p)**q)
                                                                yield 9, subst5
                                                if len(subjects342) >= 1:
                                                    tmp489 = subjects342.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp489)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 28595
                                                        if len(subjects342) == 0:
                                                            pass
                                                            # State 28596
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 28597
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 9: log(c*(d*(e + f*x**m)**p)**q)
                                                                    yield 9, subst5
                                                    subjects342.appendleft(tmp489)
                                        if len(subjects405) >= 1:
                                            tmp491 = []
                                            tmp491.append(subjects405.popleft())
                                            while True:
                                                if len(tmp491) > 1:
                                                    tmp492 = create_operation_expression(associative1, tmp491)
                                                elif len(tmp491) == 1:
                                                    tmp492 = tmp491[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp492)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28593
                                                    if len(subjects405) == 0:
                                                        pass
                                                        # State 28594
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 28595
                                                            if len(subjects342) == 0:
                                                                pass
                                                                # State 28596
                                                                if len(subjects239) == 0:
                                                                    pass
                                                                    # State 28597
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 9: log(c*(d*(e + f*x**m)**p)**q)
                                                                        yield 9, subst5
                                                        if len(subjects342) >= 1:
                                                            tmp495 = subjects342.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp495)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 28595
                                                                if len(subjects342) == 0:
                                                                    pass
                                                                    # State 28596
                                                                    if len(subjects239) == 0:
                                                                        pass
                                                                        # State 28597
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 9: log(c*(d*(e + f*x**m)**p)**q)
                                                                            yield 9, subst5
                                                            subjects342.appendleft(tmp495)
                                                if len(subjects405) == 0:
                                                    break
                                                tmp491.append(subjects405.popleft())
                                            subjects405.extendleft(reversed(tmp491))
                                    if pattern_index == 2:
                                        pass
                                        # State 34112
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 34113
                                            if len(subjects405) == 0:
                                                pass
                                                # State 34114
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 34115
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 34116
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 34117
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                yield 11, subst5
                                                if len(subjects342) >= 1:
                                                    tmp499 = subjects342.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp499)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34115
                                                        if len(subjects342) == 0:
                                                            pass
                                                            # State 34116
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 34117
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                    yield 11, subst5
                                                    subjects342.appendleft(tmp499)
                                        if len(subjects405) >= 1:
                                            tmp501 = []
                                            tmp501.append(subjects405.popleft())
                                            while True:
                                                if len(tmp501) > 1:
                                                    tmp502 = create_operation_expression(associative1, tmp501)
                                                elif len(tmp501) == 1:
                                                    tmp502 = tmp501[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp502)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 34113
                                                    if len(subjects405) == 0:
                                                        pass
                                                        # State 34114
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 34115
                                                            if len(subjects342) == 0:
                                                                pass
                                                                # State 34116
                                                                if len(subjects239) == 0:
                                                                    pass
                                                                    # State 34117
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                        yield 11, subst5
                                                        if len(subjects342) >= 1:
                                                            tmp505 = subjects342.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp505)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 34115
                                                                if len(subjects342) == 0:
                                                                    pass
                                                                    # State 34116
                                                                    if len(subjects239) == 0:
                                                                        pass
                                                                        # State 34117
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                                            yield 11, subst5
                                                            subjects342.appendleft(tmp505)
                                                if len(subjects405) == 0:
                                                    break
                                                tmp501.append(subjects405.popleft())
                                            subjects405.extendleft(reversed(tmp501))
                                    if pattern_index == 3:
                                        pass
                                        # State 43741
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43742
                                            if len(subjects405) == 0:
                                                pass
                                                # State 43743
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 43744
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 43745
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 43746
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 12: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                                yield 12, subst5
                                                if len(subjects342) >= 1:
                                                    tmp509 = subjects342.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp509)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 43744
                                                        if len(subjects342) == 0:
                                                            pass
                                                            # State 43745
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 43746
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 12: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                                    yield 12, subst5
                                                    subjects342.appendleft(tmp509)
                                        if len(subjects405) >= 1:
                                            tmp511 = []
                                            tmp511.append(subjects405.popleft())
                                            while True:
                                                if len(tmp511) > 1:
                                                    tmp512 = create_operation_expression(associative1, tmp511)
                                                elif len(tmp511) == 1:
                                                    tmp512 = tmp511[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp512)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 43742
                                                    if len(subjects405) == 0:
                                                        pass
                                                        # State 43743
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 43744
                                                            if len(subjects342) == 0:
                                                                pass
                                                                # State 43745
                                                                if len(subjects239) == 0:
                                                                    pass
                                                                    # State 43746
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 12: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                                        yield 12, subst5
                                                        if len(subjects342) >= 1:
                                                            tmp515 = subjects342.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp515)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 43744
                                                                if len(subjects342) == 0:
                                                                    pass
                                                                    # State 43745
                                                                    if len(subjects239) == 0:
                                                                        pass
                                                                        # State 43746
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 12: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                                            yield 12, subst5
                                                            subjects342.appendleft(tmp515)
                                                if len(subjects405) == 0:
                                                    break
                                                tmp511.append(subjects405.popleft())
                                            subjects405.extendleft(reversed(tmp511))
                                subjects405.appendleft(tmp474)
                            if len(subjects405) >= 1 and isinstance(subjects405[0], Mul):
                                tmp517 = subjects405.popleft()
                                associative1 = tmp517
                                associative_type1 = type(tmp517)
                                subjects518 = deque(tmp517._args)
                                matcher = CommutativeMatcher30656.get()
                                tmp519 = subjects518
                                subjects518 = []
                                for s in tmp519:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp519, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 30680
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 30681
                                            if len(subjects405) == 0:
                                                pass
                                                # State 30682
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 30683
                                                    if len(subjects342) == 0:
                                                        pass
                                                        # State 30684
                                                        if len(subjects239) == 0:
                                                            pass
                                                            # State 30685
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 10: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                                yield 10, subst5
                                                if len(subjects342) >= 1:
                                                    tmp522 = subjects342.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp522)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 30683
                                                        if len(subjects342) == 0:
                                                            pass
                                                            # State 30684
                                                            if len(subjects239) == 0:
                                                                pass
                                                                # State 30685
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 10: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                                    yield 10, subst5
                                                    subjects342.appendleft(tmp522)
                                        if len(subjects405) >= 1:
                                            tmp524 = []
                                            tmp524.append(subjects405.popleft())
                                            while True:
                                                if len(tmp524) > 1:
                                                    tmp525 = create_operation_expression(associative1, tmp524)
                                                elif len(tmp524) == 1:
                                                    tmp525 = tmp524[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp525)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 30681
                                                    if len(subjects405) == 0:
                                                        pass
                                                        # State 30682
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 30683
                                                            if len(subjects342) == 0:
                                                                pass
                                                                # State 30684
                                                                if len(subjects239) == 0:
                                                                    pass
                                                                    # State 30685
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 10: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                                        yield 10, subst5
                                                        if len(subjects342) >= 1:
                                                            tmp528 = subjects342.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp528)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 30683
                                                                if len(subjects342) == 0:
                                                                    pass
                                                                    # State 30684
                                                                    if len(subjects239) == 0:
                                                                        pass
                                                                        # State 30685
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 10: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                                            yield 10, subst5
                                                            subjects342.appendleft(tmp528)
                                                if len(subjects405) == 0:
                                                    break
                                                tmp524.append(subjects405.popleft())
                                            subjects405.extendleft(reversed(tmp524))
                                subjects405.appendleft(tmp517)
                            subjects342.appendleft(tmp404)
                    if len(subjects342) >= 1:
                        tmp530 = subjects342.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1', tmp530)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53227
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53228
                                if len(subjects342) == 0:
                                    pass
                                    # State 53229
                                    if len(subjects239) == 0:
                                        pass
                                        # State 53230
                                        if len(subjects) == 0:
                                            pass
                                            # 14: log(c*RFx**p)
                                            yield 14, subst3
                            if len(subjects342) >= 1:
                                tmp533 = subjects342.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', tmp533)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53228
                                    if len(subjects342) == 0:
                                        pass
                                        # State 53229
                                        if len(subjects239) == 0:
                                            pass
                                            # State 53230
                                            if len(subjects) == 0:
                                                pass
                                                # 14: log(c*RFx**p)
                                                yield 14, subst3
                                subjects342.appendleft(tmp533)
                        subjects342.appendleft(tmp530)
                    if len(subjects342) >= 1 and isinstance(subjects342[0], Mul):
                        tmp535 = subjects342.popleft()
                        associative1 = tmp535
                        associative_type1 = type(tmp535)
                        subjects536 = deque(tmp535._args)
                        matcher = CommutativeMatcher22685.get()
                        tmp537 = subjects536
                        subjects536 = []
                        for s in tmp537:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp537, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 22722
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22723
                                    if len(subjects342) == 0:
                                        pass
                                        # State 22724
                                        if len(subjects239) == 0:
                                            pass
                                            # State 22725
                                            if len(subjects) == 0:
                                                pass
                                                # 6: log(c*(d*(e + x*f)**p)**q)
                                                yield 6, subst3
                                if len(subjects342) >= 1:
                                    tmp539 = []
                                    tmp539.append(subjects342.popleft())
                                    while True:
                                        if len(tmp539) > 1:
                                            tmp540 = create_operation_expression(associative1, tmp539)
                                        elif len(tmp539) == 1:
                                            tmp540 = tmp539[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp540)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22723
                                            if len(subjects342) == 0:
                                                pass
                                                # State 22724
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 22725
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: log(c*(d*(e + x*f)**p)**q)
                                                        yield 6, subst3
                                        if len(subjects342) == 0:
                                            break
                                        tmp539.append(subjects342.popleft())
                                    subjects342.extendleft(reversed(tmp539))
                            if pattern_index == 1:
                                pass
                                # State 25548
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25549
                                    if len(subjects342) == 0:
                                        pass
                                        # State 25550
                                        if len(subjects239) == 0:
                                            pass
                                            # State 25551
                                            if len(subjects) == 0:
                                                pass
                                                # 7: log(c*(d*v**p)**q)
                                                yield 7, subst3
                                if len(subjects342) >= 1:
                                    tmp543 = []
                                    tmp543.append(subjects342.popleft())
                                    while True:
                                        if len(tmp543) > 1:
                                            tmp544 = create_operation_expression(associative1, tmp543)
                                        elif len(tmp543) == 1:
                                            tmp544 = tmp543[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp544)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25549
                                            if len(subjects342) == 0:
                                                pass
                                                # State 25550
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 25551
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: log(c*(d*v**p)**q)
                                                        yield 7, subst3
                                        if len(subjects342) == 0:
                                            break
                                        tmp543.append(subjects342.popleft())
                                    subjects342.extendleft(reversed(tmp543))
                            if pattern_index == 2:
                                pass
                                # State 28622
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28623
                                    if len(subjects342) == 0:
                                        pass
                                        # State 28624
                                        if len(subjects239) == 0:
                                            pass
                                            # State 28625
                                            if len(subjects) == 0:
                                                pass
                                                # 9: log(c*(d*(e + f*x**m)**p)**q)
                                                yield 9, subst3
                                if len(subjects342) >= 1:
                                    tmp547 = []
                                    tmp547.append(subjects342.popleft())
                                    while True:
                                        if len(tmp547) > 1:
                                            tmp548 = create_operation_expression(associative1, tmp547)
                                        elif len(tmp547) == 1:
                                            tmp548 = tmp547[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp548)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28623
                                            if len(subjects342) == 0:
                                                pass
                                                # State 28624
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 28625
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 9: log(c*(d*(e + f*x**m)**p)**q)
                                                        yield 9, subst3
                                        if len(subjects342) == 0:
                                            break
                                        tmp547.append(subjects342.popleft())
                                    subjects342.extendleft(reversed(tmp547))
                            if pattern_index == 3:
                                pass
                                # State 30740
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 30741
                                    if len(subjects342) == 0:
                                        pass
                                        # State 30742
                                        if len(subjects239) == 0:
                                            pass
                                            # State 30743
                                            if len(subjects) == 0:
                                                pass
                                                # 10: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                yield 10, subst3
                                if len(subjects342) >= 1:
                                    tmp551 = []
                                    tmp551.append(subjects342.popleft())
                                    while True:
                                        if len(tmp551) > 1:
                                            tmp552 = create_operation_expression(associative1, tmp551)
                                        elif len(tmp551) == 1:
                                            tmp552 = tmp551[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp552)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 30741
                                            if len(subjects342) == 0:
                                                pass
                                                # State 30742
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 30743
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 10: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                                        yield 10, subst3
                                        if len(subjects342) == 0:
                                            break
                                        tmp551.append(subjects342.popleft())
                                    subjects342.extendleft(reversed(tmp551))
                            if pattern_index == 4:
                                pass
                                # State 34146
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 34147
                                    if len(subjects342) == 0:
                                        pass
                                        # State 34148
                                        if len(subjects239) == 0:
                                            pass
                                            # State 34149
                                            if len(subjects) == 0:
                                                pass
                                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                yield 11, subst3
                                if len(subjects342) >= 1:
                                    tmp555 = []
                                    tmp555.append(subjects342.popleft())
                                    while True:
                                        if len(tmp555) > 1:
                                            tmp556 = create_operation_expression(associative1, tmp555)
                                        elif len(tmp555) == 1:
                                            tmp556 = tmp555[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp556)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 34147
                                            if len(subjects342) == 0:
                                                pass
                                                # State 34148
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 34149
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 11: log(c*(d*(e + f*x**m)**p)**q)
                                                        yield 11, subst3
                                        if len(subjects342) == 0:
                                            break
                                        tmp555.append(subjects342.popleft())
                                    subjects342.extendleft(reversed(tmp555))
                            if pattern_index == 5:
                                pass
                                # State 43765
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 43766
                                    if len(subjects342) == 0:
                                        pass
                                        # State 43767
                                        if len(subjects239) == 0:
                                            pass
                                            # State 43768
                                            if len(subjects) == 0:
                                                pass
                                                # 12: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                yield 12, subst3
                                if len(subjects342) >= 1:
                                    tmp559 = []
                                    tmp559.append(subjects342.popleft())
                                    while True:
                                        if len(tmp559) > 1:
                                            tmp560 = create_operation_expression(associative1, tmp559)
                                        elif len(tmp559) == 1:
                                            tmp560 = tmp559[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp560)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43766
                                            if len(subjects342) == 0:
                                                pass
                                                # State 43767
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 43768
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 12: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                        yield 12, subst3
                                        if len(subjects342) == 0:
                                            break
                                        tmp559.append(subjects342.popleft())
                                    subjects342.extendleft(reversed(tmp559))
                            if pattern_index == 6:
                                pass
                                # State 45464
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45465
                                    if len(subjects342) == 0:
                                        pass
                                        # State 45466
                                        if len(subjects239) == 0:
                                            pass
                                            # State 45467
                                            if len(subjects) == 0:
                                                pass
                                                # 13: log(c*(d*v**p)**q)
                                                yield 13, subst3
                                if len(subjects342) >= 1:
                                    tmp563 = []
                                    tmp563.append(subjects342.popleft())
                                    while True:
                                        if len(tmp563) > 1:
                                            tmp564 = create_operation_expression(associative1, tmp563)
                                        elif len(tmp563) == 1:
                                            tmp564 = tmp563[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp564)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45465
                                            if len(subjects342) == 0:
                                                pass
                                                # State 45466
                                                if len(subjects239) == 0:
                                                    pass
                                                    # State 45467
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 13: log(c*(d*v**p)**q)
                                                        yield 13, subst3
                                        if len(subjects342) == 0:
                                            break
                                        tmp563.append(subjects342.popleft())
                                    subjects342.extendleft(reversed(tmp563))
                        subjects342.appendleft(tmp535)
                    subjects239.appendleft(tmp341)
                if len(subjects239) >= 1 and isinstance(subjects239[0], Add):
                    tmp566 = subjects239.popleft()
                    associative1 = tmp566
                    associative_type1 = type(tmp566)
                    subjects567 = deque(tmp566._args)
                    matcher = CommutativeMatcher26041.get()
                    tmp568 = subjects567
                    subjects567 = []
                    for s in tmp568:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp568, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 26047
                            if len(subjects239) == 0:
                                pass
                                # State 26048
                                if len(subjects) == 0:
                                    pass
                                    # 8: log(c*(e + x*f))
                                    yield 8, subst2
                    subjects239.appendleft(tmp566)
            if len(subjects239) >= 1 and isinstance(subjects239[0], Mul):
                tmp569 = subjects239.popleft()
                associative1 = tmp569
                associative_type1 = type(tmp569)
                subjects570 = deque(tmp569._args)
                matcher = CommutativeMatcher22727.get()
                tmp571 = subjects570
                subjects570 = []
                for s in tmp571:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp571, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 22896
                        if len(subjects239) == 0:
                            pass
                            # State 22897
                            if len(subjects) == 0:
                                pass
                                # 6: log(c*(d*(e + x*f)**p)**q)
                                yield 6, subst1
                    if pattern_index == 1:
                        pass
                        # State 25570
                        if len(subjects239) == 0:
                            pass
                            # State 25571
                            if len(subjects) == 0:
                                pass
                                # 7: log(c*(d*v**p)**q)
                                yield 7, subst1
                    if pattern_index == 2:
                        pass
                        # State 26063
                        if len(subjects239) == 0:
                            pass
                            # State 26064
                            if len(subjects) == 0:
                                pass
                                # 8: log(c*(e + x*f))
                                yield 8, subst1
                    if pattern_index == 3:
                        pass
                        # State 28730
                        if len(subjects239) == 0:
                            pass
                            # State 28731
                            if len(subjects) == 0:
                                pass
                                # 9: log(c*(d*(e + f*x**m)**p)**q)
                                yield 9, subst1
                    if pattern_index == 4:
                        pass
                        # State 30968
                        if len(subjects239) == 0:
                            pass
                            # State 30969
                            if len(subjects) == 0:
                                pass
                                # 10: log(c*(d*(x**m*(f + e*x**r))**p)**q)
                                yield 10, subst1
                    if pattern_index == 5:
                        pass
                        # State 34278
                        if len(subjects239) == 0:
                            pass
                            # State 34279
                            if len(subjects) == 0:
                                pass
                                # 11: log(c*(d*(e + f*x**m)**p)**q)
                                yield 11, subst1
                    if pattern_index == 6:
                        pass
                        # State 43849
                        if len(subjects239) == 0:
                            pass
                            # State 43850
                            if len(subjects) == 0:
                                pass
                                # 12: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                yield 12, subst1
                    if pattern_index == 7:
                        pass
                        # State 45488
                        if len(subjects239) == 0:
                            pass
                            # State 45489
                            if len(subjects) == 0:
                                pass
                                # 13: log(c*(d*v**p)**q)
                                yield 13, subst1
                    if pattern_index == 8:
                        pass
                        # State 53235
                        if len(subjects239) == 0:
                            pass
                            # State 53236
                            if len(subjects) == 0:
                                pass
                                # 14: log(c*RFx**p)
                                yield 14, subst1
                subjects239.appendleft(tmp569)
            subjects.appendleft(tmp238)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp572 = subjects.popleft()
            subjects573 = deque(tmp572._args)
            # State 64958
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 64959
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 64960
                    if len(subjects573) >= 1:
                        tmp576 = subjects573.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp576)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 64961
                            if len(subjects573) == 0:
                                pass
                                # State 64962
                                if len(subjects) == 0:
                                    pass
                                    # 15: sin(c + x*d)
                                    yield 15, subst3
                        subjects573.appendleft(tmp576)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 73656
                    if len(subjects573) >= 1 and isinstance(subjects573[0], Pow):
                        tmp579 = subjects573.popleft()
                        subjects580 = deque(tmp579._args)
                        # State 73657
                        if len(subjects580) >= 1:
                            tmp581 = subjects580.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp581)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 73658
                                if len(subjects580) >= 1:
                                    tmp583 = subjects580.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp583)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 73659
                                        if len(subjects580) == 0:
                                            pass
                                            # State 73660
                                            if len(subjects573) == 0:
                                                pass
                                                # State 73661
                                                if len(subjects) == 0:
                                                    pass
                                                    # 19: sin(c + d*x**n)
                                                    yield 19, subst4
                                    subjects580.appendleft(tmp583)
                            subjects580.appendleft(tmp581)
                        subjects573.appendleft(tmp579)
                if len(subjects573) >= 1 and isinstance(subjects573[0], Mul):
                    tmp585 = subjects573.popleft()
                    associative1 = tmp585
                    associative_type1 = type(tmp585)
                    subjects586 = deque(tmp585._args)
                    matcher = CommutativeMatcher64964.get()
                    tmp587 = subjects586
                    subjects586 = []
                    for s in tmp587:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp587, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 64965
                            if len(subjects573) == 0:
                                pass
                                # State 64966
                                if len(subjects) == 0:
                                    pass
                                    # 15: sin(c + x*d)
                                    yield 15, subst2
                        if pattern_index == 1:
                            pass
                            # State 73666
                            if len(subjects573) == 0:
                                pass
                                # State 73667
                                if len(subjects) == 0:
                                    pass
                                    # 19: sin(c + d*x**n)
                                    yield 19, subst2
                    subjects573.appendleft(tmp585)
            if len(subjects573) >= 1:
                tmp588 = subjects573.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp588)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72279
                    if len(subjects573) == 0:
                        pass
                        # State 72280
                        if len(subjects) == 0:
                            pass
                            # 17: sin(v)
                            yield 17, subst1
                subjects573.appendleft(tmp588)
            if len(subjects573) >= 1 and isinstance(subjects573[0], Add):
                tmp590 = subjects573.popleft()
                associative1 = tmp590
                associative_type1 = type(tmp590)
                subjects591 = deque(tmp590._args)
                matcher = CommutativeMatcher64968.get()
                tmp592 = subjects591
                subjects591 = []
                for s in tmp592:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp592, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 64974
                        if len(subjects573) == 0:
                            pass
                            # State 64975
                            if len(subjects) == 0:
                                pass
                                # 15: sin(c + x*d)
                                yield 15, subst1
                    if pattern_index == 1:
                        pass
                        # State 73678
                        if len(subjects573) == 0:
                            pass
                            # State 73679
                            if len(subjects) == 0:
                                pass
                                # 19: sin(c + d*x**n)
                                yield 19, subst1
                subjects573.appendleft(tmp590)
            subjects.appendleft(tmp572)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp593 = subjects.popleft()
            subjects594 = deque(tmp593._args)
            # State 65051
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 65052
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65053
                    if len(subjects594) >= 1:
                        tmp597 = subjects594.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp597)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 65054
                            if len(subjects594) == 0:
                                pass
                                # State 65055
                                if len(subjects) == 0:
                                    pass
                                    # 16: cos(c + x*d)
                                    yield 16, subst3
                        subjects594.appendleft(tmp597)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 73868
                    if len(subjects594) >= 1 and isinstance(subjects594[0], Pow):
                        tmp600 = subjects594.popleft()
                        subjects601 = deque(tmp600._args)
                        # State 73869
                        if len(subjects601) >= 1:
                            tmp602 = subjects601.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp602)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 73870
                                if len(subjects601) >= 1:
                                    tmp604 = subjects601.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp604)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 73871
                                        if len(subjects601) == 0:
                                            pass
                                            # State 73872
                                            if len(subjects594) == 0:
                                                pass
                                                # State 73873
                                                if len(subjects) == 0:
                                                    pass
                                                    # 20: cos(c + d*x**n)
                                                    yield 20, subst4
                                    subjects601.appendleft(tmp604)
                            subjects601.appendleft(tmp602)
                        subjects594.appendleft(tmp600)
                if len(subjects594) >= 1 and isinstance(subjects594[0], Mul):
                    tmp606 = subjects594.popleft()
                    associative1 = tmp606
                    associative_type1 = type(tmp606)
                    subjects607 = deque(tmp606._args)
                    matcher = CommutativeMatcher65057.get()
                    tmp608 = subjects607
                    subjects607 = []
                    for s in tmp608:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp608, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 65058
                            if len(subjects594) == 0:
                                pass
                                # State 65059
                                if len(subjects) == 0:
                                    pass
                                    # 16: cos(c + x*d)
                                    yield 16, subst2
                        if pattern_index == 1:
                            pass
                            # State 73878
                            if len(subjects594) == 0:
                                pass
                                # State 73879
                                if len(subjects) == 0:
                                    pass
                                    # 20: cos(c + d*x**n)
                                    yield 20, subst2
                    subjects594.appendleft(tmp606)
            if len(subjects594) >= 1:
                tmp609 = subjects594.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp609)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72310
                    if len(subjects594) == 0:
                        pass
                        # State 72311
                        if len(subjects) == 0:
                            pass
                            # 18: cos(v)
                            yield 18, subst1
                subjects594.appendleft(tmp609)
            if len(subjects594) >= 1 and isinstance(subjects594[0], Add):
                tmp611 = subjects594.popleft()
                associative1 = tmp611
                associative_type1 = type(tmp611)
                subjects612 = deque(tmp611._args)
                matcher = CommutativeMatcher65061.get()
                tmp613 = subjects612
                subjects612 = []
                for s in tmp613:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp613, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 65067
                        if len(subjects594) == 0:
                            pass
                            # State 65068
                            if len(subjects) == 0:
                                pass
                                # 16: cos(c + x*d)
                                yield 16, subst1
                    if pattern_index == 1:
                        pass
                        # State 73890
                        if len(subjects594) == 0:
                            pass
                            # State 73891
                            if len(subjects) == 0:
                                pass
                                # 20: cos(c + d*x**n)
                                yield 20, subst1
                subjects594.appendleft(tmp611)
            subjects.appendleft(tmp593)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp614 = subjects.popleft()
            subjects615 = deque(tmp614._args)
            # State 81248
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 81249
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 81250
                    if len(subjects615) >= 1:
                        tmp618 = subjects615.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp618)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 81251
                            if len(subjects615) == 0:
                                pass
                                # State 81252
                                if len(subjects) == 0:
                                    pass
                                    # 21: tan(c + x*d)
                                    yield 21, subst3
                        subjects615.appendleft(tmp618)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 87959
                    if len(subjects615) >= 1 and isinstance(subjects615[0], Pow):
                        tmp621 = subjects615.popleft()
                        subjects622 = deque(tmp621._args)
                        # State 87960
                        if len(subjects622) >= 1:
                            tmp623 = subjects622.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp623)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 87961
                                if len(subjects622) >= 1:
                                    tmp625 = subjects622.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp625)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 87962
                                        if len(subjects622) == 0:
                                            pass
                                            # State 87963
                                            if len(subjects615) == 0:
                                                pass
                                                # State 87964
                                                if len(subjects) == 0:
                                                    pass
                                                    # 25: tan(c + d*x**n)
                                                    yield 25, subst4
                                    subjects622.appendleft(tmp625)
                            subjects622.appendleft(tmp623)
                        subjects615.appendleft(tmp621)
                if len(subjects615) >= 1 and isinstance(subjects615[0], Mul):
                    tmp627 = subjects615.popleft()
                    associative1 = tmp627
                    associative_type1 = type(tmp627)
                    subjects628 = deque(tmp627._args)
                    matcher = CommutativeMatcher81254.get()
                    tmp629 = subjects628
                    subjects628 = []
                    for s in tmp629:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp629, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 81255
                            if len(subjects615) == 0:
                                pass
                                # State 81256
                                if len(subjects) == 0:
                                    pass
                                    # 21: tan(c + x*d)
                                    yield 21, subst2
                        if pattern_index == 1:
                            pass
                            # State 87969
                            if len(subjects615) == 0:
                                pass
                                # State 87970
                                if len(subjects) == 0:
                                    pass
                                    # 25: tan(c + d*x**n)
                                    yield 25, subst2
                    subjects615.appendleft(tmp627)
            if len(subjects615) >= 1:
                tmp630 = subjects615.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp630)
                except ValueError:
                    pass
                else:
                    pass
                    # State 86935
                    if len(subjects615) == 0:
                        pass
                        # State 86936
                        if len(subjects) == 0:
                            pass
                            # 23: tan(v)
                            yield 23, subst1
                subjects615.appendleft(tmp630)
            if len(subjects615) >= 1 and isinstance(subjects615[0], Add):
                tmp632 = subjects615.popleft()
                associative1 = tmp632
                associative_type1 = type(tmp632)
                subjects633 = deque(tmp632._args)
                matcher = CommutativeMatcher81258.get()
                tmp634 = subjects633
                subjects633 = []
                for s in tmp634:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp634, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 81264
                        if len(subjects615) == 0:
                            pass
                            # State 81265
                            if len(subjects) == 0:
                                pass
                                # 21: tan(c + x*d)
                                yield 21, subst1
                    if pattern_index == 1:
                        pass
                        # State 87981
                        if len(subjects615) == 0:
                            pass
                            # State 87982
                            if len(subjects) == 0:
                                pass
                                # 25: tan(c + d*x**n)
                                yield 25, subst1
                subjects615.appendleft(tmp632)
            subjects.appendleft(tmp614)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp635 = subjects.popleft()
            subjects636 = deque(tmp635._args)
            # State 108203
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108204
                if len(subjects636) >= 1:
                    tmp638 = subjects636.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp638)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108205
                        if len(subjects636) == 0:
                            pass
                            # State 108206
                            if len(subjects) == 0:
                                pass
                                # 33: asin(x*c)
                                yield 33, subst2
                    subjects636.appendleft(tmp638)
            if len(subjects636) >= 1 and isinstance(subjects636[0], Mul):
                tmp640 = subjects636.popleft()
                associative1 = tmp640
                associative_type1 = type(tmp640)
                subjects641 = deque(tmp640._args)
                matcher = CommutativeMatcher108208.get()
                tmp642 = subjects641
                subjects641 = []
                for s in tmp642:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp642, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108209
                        if len(subjects636) == 0:
                            pass
                            # State 108210
                            if len(subjects) == 0:
                                pass
                                # 33: asin(x*c)
                                yield 33, subst1
                subjects636.appendleft(tmp640)
            if len(subjects636) >= 1 and isinstance(subjects636[0], Add):
                tmp643 = subjects636.popleft()
                associative1 = tmp643
                associative_type1 = type(tmp643)
                subjects644 = deque(tmp643._args)
                matcher = CommutativeMatcher110456.get()
                tmp645 = subjects644
                subjects644 = []
                for s in tmp645:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp645, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110462
                        if len(subjects636) == 0:
                            pass
                            # State 110463
                            if len(subjects) == 0:
                                pass
                                # 35: asin(c + x*d)
                                yield 35, subst1
                subjects636.appendleft(tmp643)
            subjects.appendleft(tmp635)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp646 = subjects.popleft()
            subjects647 = deque(tmp646._args)
            # State 108287
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108288
                if len(subjects647) >= 1:
                    tmp649 = subjects647.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp649)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108289
                        if len(subjects647) == 0:
                            pass
                            # State 108290
                            if len(subjects) == 0:
                                pass
                                # 34: acos(x*c)
                                yield 34, subst2
                    subjects647.appendleft(tmp649)
            if len(subjects647) >= 1 and isinstance(subjects647[0], Mul):
                tmp651 = subjects647.popleft()
                associative1 = tmp651
                associative_type1 = type(tmp651)
                subjects652 = deque(tmp651._args)
                matcher = CommutativeMatcher108292.get()
                tmp653 = subjects652
                subjects652 = []
                for s in tmp653:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp653, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108293
                        if len(subjects647) == 0:
                            pass
                            # State 108294
                            if len(subjects) == 0:
                                pass
                                # 34: acos(x*c)
                                yield 34, subst1
                subjects647.appendleft(tmp651)
            if len(subjects647) >= 1 and isinstance(subjects647[0], Add):
                tmp654 = subjects647.popleft()
                associative1 = tmp654
                associative_type1 = type(tmp654)
                subjects655 = deque(tmp654._args)
                matcher = CommutativeMatcher110543.get()
                tmp656 = subjects655
                subjects655 = []
                for s in tmp656:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp656, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110549
                        if len(subjects647) == 0:
                            pass
                            # State 110550
                            if len(subjects) == 0:
                                pass
                                # 36: acos(c + x*d)
                                yield 36, subst1
                subjects647.appendleft(tmp654)
            subjects.appendleft(tmp646)
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp657 = subjects.popleft()
            subjects658 = deque(tmp657._args)
            # State 112822
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 112823
                if len(subjects658) >= 1:
                    tmp660 = subjects658.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp660)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112824
                        if len(subjects658) == 0:
                            pass
                            # State 112825
                            if len(subjects) == 0:
                                pass
                                # 37: atan(x*c)
                                yield 37, subst2
                    subjects658.appendleft(tmp660)
            if len(subjects658) >= 1 and isinstance(subjects658[0], Mul):
                tmp662 = subjects658.popleft()
                associative1 = tmp662
                associative_type1 = type(tmp662)
                subjects663 = deque(tmp662._args)
                matcher = CommutativeMatcher112827.get()
                tmp664 = subjects663
                subjects663 = []
                for s in tmp664:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp664, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 112828
                        if len(subjects658) == 0:
                            pass
                            # State 112829
                            if len(subjects) == 0:
                                pass
                                # 37: atan(x*c)
                                yield 37, subst1
                subjects658.appendleft(tmp662)
            if len(subjects658) >= 1 and isinstance(subjects658[0], Add):
                tmp665 = subjects658.popleft()
                associative1 = tmp665
                associative_type1 = type(tmp665)
                subjects666 = deque(tmp665._args)
                matcher = CommutativeMatcher115686.get()
                tmp667 = subjects666
                subjects666 = []
                for s in tmp667:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp667, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115692
                        if len(subjects658) == 0:
                            pass
                            # State 115693
                            if len(subjects) == 0:
                                pass
                                # 39: atan(c + x*d)
                                yield 39, subst1
                subjects658.appendleft(tmp665)
            subjects.appendleft(tmp657)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp668 = subjects.popleft()
            subjects669 = deque(tmp668._args)
            # State 112903
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 112904
                if len(subjects669) >= 1:
                    tmp671 = subjects669.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp671)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112905
                        if len(subjects669) == 0:
                            pass
                            # State 112906
                            if len(subjects) == 0:
                                pass
                                # 38: acot(x*c)
                                yield 38, subst2
                    subjects669.appendleft(tmp671)
            if len(subjects669) >= 1 and isinstance(subjects669[0], Mul):
                tmp673 = subjects669.popleft()
                associative1 = tmp673
                associative_type1 = type(tmp673)
                subjects674 = deque(tmp673._args)
                matcher = CommutativeMatcher112908.get()
                tmp675 = subjects674
                subjects674 = []
                for s in tmp675:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp675, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 112909
                        if len(subjects669) == 0:
                            pass
                            # State 112910
                            if len(subjects) == 0:
                                pass
                                # 38: acot(x*c)
                                yield 38, subst1
                subjects669.appendleft(tmp673)
            if len(subjects669) >= 1 and isinstance(subjects669[0], Add):
                tmp676 = subjects669.popleft()
                associative1 = tmp676
                associative_type1 = type(tmp676)
                subjects677 = deque(tmp676._args)
                matcher = CommutativeMatcher115773.get()
                tmp678 = subjects677
                subjects677 = []
                for s in tmp678:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp678, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115779
                        if len(subjects669) == 0:
                            pass
                            # State 115780
                            if len(subjects) == 0:
                                pass
                                # 40: acot(c + x*d)
                                yield 40, subst1
                subjects669.appendleft(tmp676)
            subjects.appendleft(tmp668)
        if len(subjects) >= 1 and isinstance(subjects[0], asec):
            tmp679 = subjects.popleft()
            subjects680 = deque(tmp679._args)
            # State 119811
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119812
                if len(subjects680) >= 1:
                    tmp682 = subjects680.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp682)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119813
                        if len(subjects680) == 0:
                            pass
                            # State 119814
                            if len(subjects) == 0:
                                pass
                                # 41: asec(x*c)
                                yield 41, subst2
                    subjects680.appendleft(tmp682)
            if len(subjects680) >= 1 and isinstance(subjects680[0], Mul):
                tmp684 = subjects680.popleft()
                associative1 = tmp684
                associative_type1 = type(tmp684)
                subjects685 = deque(tmp684._args)
                matcher = CommutativeMatcher119816.get()
                tmp686 = subjects685
                subjects685 = []
                for s in tmp686:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp686, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119817
                        if len(subjects680) == 0:
                            pass
                            # State 119818
                            if len(subjects) == 0:
                                pass
                                # 41: asec(x*c)
                                yield 41, subst1
                subjects680.appendleft(tmp684)
            subjects.appendleft(tmp679)
        if len(subjects) >= 1 and isinstance(subjects[0], acsc):
            tmp687 = subjects.popleft()
            subjects688 = deque(tmp687._args)
            # State 119857
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119858
                if len(subjects688) >= 1:
                    tmp690 = subjects688.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp690)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119859
                        if len(subjects688) == 0:
                            pass
                            # State 119860
                            if len(subjects) == 0:
                                pass
                                # 42: acsc(x*c)
                                yield 42, subst2
                    subjects688.appendleft(tmp690)
            if len(subjects688) >= 1 and isinstance(subjects688[0], Mul):
                tmp692 = subjects688.popleft()
                associative1 = tmp692
                associative_type1 = type(tmp692)
                subjects693 = deque(tmp692._args)
                matcher = CommutativeMatcher119862.get()
                tmp694 = subjects693
                subjects693 = []
                for s in tmp694:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp694, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119863
                        if len(subjects688) == 0:
                            pass
                            # State 119864
                            if len(subjects) == 0:
                                pass
                                # 42: acsc(x*c)
                                yield 42, subst1
                subjects688.appendleft(tmp692)
            subjects.appendleft(tmp687)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp695 = subjects.popleft()
            subjects696 = deque(tmp695._args)
            # State 122038
            if len(subjects696) >= 1:
                tmp697 = subjects696.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp697)
                except ValueError:
                    pass
                else:
                    pass
                    # State 122039
                    if len(subjects696) == 0:
                        pass
                        # State 122040
                        if len(subjects) == 0:
                            pass
                            # 43: sinh(v)
                            yield 43, subst1
                subjects696.appendleft(tmp697)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 123535
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 123536
                    if len(subjects696) >= 1 and isinstance(subjects696[0], Pow):
                        tmp701 = subjects696.popleft()
                        subjects702 = deque(tmp701._args)
                        # State 123537
                        if len(subjects702) >= 1:
                            tmp703 = subjects702.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp703)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 123538
                                if len(subjects702) >= 1:
                                    tmp705 = subjects702.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp705)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 123539
                                        if len(subjects702) == 0:
                                            pass
                                            # State 123540
                                            if len(subjects696) == 0:
                                                pass
                                                # State 123541
                                                if len(subjects) == 0:
                                                    pass
                                                    # 46: sinh(c + d*x**n)
                                                    yield 46, subst4
                                    subjects702.appendleft(tmp705)
                            subjects702.appendleft(tmp703)
                        subjects696.appendleft(tmp701)
                if len(subjects696) >= 1 and isinstance(subjects696[0], Mul):
                    tmp707 = subjects696.popleft()
                    associative1 = tmp707
                    associative_type1 = type(tmp707)
                    subjects708 = deque(tmp707._args)
                    matcher = CommutativeMatcher123543.get()
                    tmp709 = subjects708
                    subjects708 = []
                    for s in tmp709:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp709, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 123548
                            if len(subjects696) == 0:
                                pass
                                # State 123549
                                if len(subjects) == 0:
                                    pass
                                    # 46: sinh(c + d*x**n)
                                    yield 46, subst2
                    subjects696.appendleft(tmp707)
            if len(subjects696) >= 1 and isinstance(subjects696[0], Add):
                tmp710 = subjects696.popleft()
                associative1 = tmp710
                associative_type1 = type(tmp710)
                subjects711 = deque(tmp710._args)
                matcher = CommutativeMatcher123551.get()
                tmp712 = subjects711
                subjects711 = []
                for s in tmp712:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp712, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 123564
                        if len(subjects696) == 0:
                            pass
                            # State 123565
                            if len(subjects) == 0:
                                pass
                                # 46: sinh(c + d*x**n)
                                yield 46, subst1
                subjects696.appendleft(tmp710)
            subjects.appendleft(tmp695)
        if len(subjects) >= 1 and isinstance(subjects[0], cosh):
            tmp713 = subjects.popleft()
            subjects714 = deque(tmp713._args)
            # State 122076
            if len(subjects714) >= 1:
                tmp715 = subjects714.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp715)
                except ValueError:
                    pass
                else:
                    pass
                    # State 122077
                    if len(subjects714) == 0:
                        pass
                        # State 122078
                        if len(subjects) == 0:
                            pass
                            # 44: cosh(v)
                            yield 44, subst1
                subjects714.appendleft(tmp715)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 122214
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122215
                    if len(subjects714) >= 1:
                        tmp719 = subjects714.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp719)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 122216
                            if len(subjects714) == 0:
                                pass
                                # State 122217
                                if len(subjects) == 0:
                                    pass
                                    # 45: cosh(e + x*d)
                                    yield 45, subst3
                        subjects714.appendleft(tmp719)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 123786
                    if len(subjects714) >= 1 and isinstance(subjects714[0], Pow):
                        tmp722 = subjects714.popleft()
                        subjects723 = deque(tmp722._args)
                        # State 123787
                        if len(subjects723) >= 1:
                            tmp724 = subjects723.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp724)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 123788
                                if len(subjects723) >= 1:
                                    tmp726 = subjects723.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp726)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 123789
                                        if len(subjects723) == 0:
                                            pass
                                            # State 123790
                                            if len(subjects714) == 0:
                                                pass
                                                # State 123791
                                                if len(subjects) == 0:
                                                    pass
                                                    # 47: cosh(c + d*x**n)
                                                    yield 47, subst4
                                    subjects723.appendleft(tmp726)
                            subjects723.appendleft(tmp724)
                        subjects714.appendleft(tmp722)
                if len(subjects714) >= 1 and isinstance(subjects714[0], Mul):
                    tmp728 = subjects714.popleft()
                    associative1 = tmp728
                    associative_type1 = type(tmp728)
                    subjects729 = deque(tmp728._args)
                    matcher = CommutativeMatcher122219.get()
                    tmp730 = subjects729
                    subjects729 = []
                    for s in tmp730:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp730, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122220
                            if len(subjects714) == 0:
                                pass
                                # State 122221
                                if len(subjects) == 0:
                                    pass
                                    # 45: cosh(e + x*d)
                                    yield 45, subst2
                        if pattern_index == 1:
                            pass
                            # State 123796
                            if len(subjects714) == 0:
                                pass
                                # State 123797
                                if len(subjects) == 0:
                                    pass
                                    # 47: cosh(c + d*x**n)
                                    yield 47, subst2
                    subjects714.appendleft(tmp728)
            if len(subjects714) >= 1 and isinstance(subjects714[0], Add):
                tmp731 = subjects714.popleft()
                associative1 = tmp731
                associative_type1 = type(tmp731)
                subjects732 = deque(tmp731._args)
                matcher = CommutativeMatcher122223.get()
                tmp733 = subjects732
                subjects732 = []
                for s in tmp733:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp733, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 122229
                        if len(subjects714) == 0:
                            pass
                            # State 122230
                            if len(subjects) == 0:
                                pass
                                # 45: cosh(e + x*d)
                                yield 45, subst1
                    if pattern_index == 1:
                        pass
                        # State 123808
                        if len(subjects714) == 0:
                            pass
                            # State 123809
                            if len(subjects) == 0:
                                pass
                                # 47: cosh(c + d*x**n)
                                yield 47, subst1
                subjects714.appendleft(tmp731)
            subjects.appendleft(tmp713)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp734 = subjects.popleft()
            subjects735 = deque(tmp734._args)
            # State 126251
            if len(subjects735) >= 1:
                tmp736 = subjects735.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp736)
                except ValueError:
                    pass
                else:
                    pass
                    # State 126252
                    if len(subjects735) == 0:
                        pass
                        # State 126253
                        if len(subjects) == 0:
                            pass
                            # 48: tanh(v)
                            yield 48, subst1
                subjects735.appendleft(tmp736)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 127461
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 127462
                    if len(subjects735) >= 1 and isinstance(subjects735[0], Pow):
                        tmp740 = subjects735.popleft()
                        subjects741 = deque(tmp740._args)
                        # State 127463
                        if len(subjects741) >= 1:
                            tmp742 = subjects741.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp742)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 127464
                                if len(subjects741) >= 1:
                                    tmp744 = subjects741.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp744)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 127465
                                        if len(subjects741) == 0:
                                            pass
                                            # State 127466
                                            if len(subjects735) == 0:
                                                pass
                                                # State 127467
                                                if len(subjects) == 0:
                                                    pass
                                                    # 51: tanh(c + d*x**n)
                                                    yield 51, subst4
                                    subjects741.appendleft(tmp744)
                            subjects741.appendleft(tmp742)
                        subjects735.appendleft(tmp740)
                if len(subjects735) >= 1 and isinstance(subjects735[0], Mul):
                    tmp746 = subjects735.popleft()
                    associative1 = tmp746
                    associative_type1 = type(tmp746)
                    subjects747 = deque(tmp746._args)
                    matcher = CommutativeMatcher127469.get()
                    tmp748 = subjects747
                    subjects747 = []
                    for s in tmp748:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp748, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 127474
                            if len(subjects735) == 0:
                                pass
                                # State 127475
                                if len(subjects) == 0:
                                    pass
                                    # 51: tanh(c + d*x**n)
                                    yield 51, subst2
                    subjects735.appendleft(tmp746)
            if len(subjects735) >= 1 and isinstance(subjects735[0], Add):
                tmp749 = subjects735.popleft()
                associative1 = tmp749
                associative_type1 = type(tmp749)
                subjects750 = deque(tmp749._args)
                matcher = CommutativeMatcher127477.get()
                tmp751 = subjects750
                subjects750 = []
                for s in tmp751:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp751, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 127490
                        if len(subjects735) == 0:
                            pass
                            # State 127491
                            if len(subjects) == 0:
                                pass
                                # 51: tanh(c + d*x**n)
                                yield 51, subst1
                subjects735.appendleft(tmp749)
            subjects.appendleft(tmp734)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp752 = subjects.popleft()
            subjects753 = deque(tmp752._args)
            # State 137942
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 137943
                if len(subjects753) >= 1:
                    tmp755 = subjects753.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp755)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137944
                        if len(subjects753) == 0:
                            pass
                            # State 137945
                            if len(subjects) == 0:
                                pass
                                # 55: asinh(x*c)
                                yield 55, subst2
                    subjects753.appendleft(tmp755)
            if len(subjects753) >= 1 and isinstance(subjects753[0], Mul):
                tmp757 = subjects753.popleft()
                associative1 = tmp757
                associative_type1 = type(tmp757)
                subjects758 = deque(tmp757._args)
                matcher = CommutativeMatcher137947.get()
                tmp759 = subjects758
                subjects758 = []
                for s in tmp759:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp759, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 137948
                        if len(subjects753) == 0:
                            pass
                            # State 137949
                            if len(subjects) == 0:
                                pass
                                # 55: asinh(x*c)
                                yield 55, subst1
                subjects753.appendleft(tmp757)
            if len(subjects753) >= 1 and isinstance(subjects753[0], Add):
                tmp760 = subjects753.popleft()
                associative1 = tmp760
                associative_type1 = type(tmp760)
                subjects761 = deque(tmp760._args)
                matcher = CommutativeMatcher140191.get()
                tmp762 = subjects761
                subjects761 = []
                for s in tmp762:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp762, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 140197
                        if len(subjects753) == 0:
                            pass
                            # State 140198
                            if len(subjects) == 0:
                                pass
                                # 57: asinh(c + x*d)
                                yield 57, subst1
                subjects753.appendleft(tmp760)
            subjects.appendleft(tmp752)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp763 = subjects.popleft()
            subjects764 = deque(tmp763._args)
            # State 138023
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138024
                if len(subjects764) >= 1:
                    tmp766 = subjects764.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp766)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138025
                        if len(subjects764) == 0:
                            pass
                            # State 138026
                            if len(subjects) == 0:
                                pass
                                # 56: acosh(x*c)
                                yield 56, subst2
                    subjects764.appendleft(tmp766)
            if len(subjects764) >= 1 and isinstance(subjects764[0], Mul):
                tmp768 = subjects764.popleft()
                associative1 = tmp768
                associative_type1 = type(tmp768)
                subjects769 = deque(tmp768._args)
                matcher = CommutativeMatcher138028.get()
                tmp770 = subjects769
                subjects769 = []
                for s in tmp770:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp770, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138029
                        if len(subjects764) == 0:
                            pass
                            # State 138030
                            if len(subjects) == 0:
                                pass
                                # 56: acosh(x*c)
                                yield 56, subst1
                subjects764.appendleft(tmp768)
            if len(subjects764) >= 1 and isinstance(subjects764[0], Add):
                tmp771 = subjects764.popleft()
                associative1 = tmp771
                associative_type1 = type(tmp771)
                subjects772 = deque(tmp771._args)
                matcher = CommutativeMatcher140278.get()
                tmp773 = subjects772
                subjects772 = []
                for s in tmp773:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp773, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 140284
                        if len(subjects764) == 0:
                            pass
                            # State 140285
                            if len(subjects) == 0:
                                pass
                                # 58: acosh(c + x*d)
                                yield 58, subst1
                subjects764.appendleft(tmp771)
            subjects.appendleft(tmp763)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp774 = subjects.popleft()
            subjects775 = deque(tmp774._args)
            # State 142454
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142455
                if len(subjects775) >= 1:
                    tmp777 = subjects775.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp777)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142456
                        if len(subjects775) == 0:
                            pass
                            # State 142457
                            if len(subjects) == 0:
                                pass
                                # 59: atanh(x*c)
                                yield 59, subst2
                    subjects775.appendleft(tmp777)
            if len(subjects775) >= 1 and isinstance(subjects775[0], Mul):
                tmp779 = subjects775.popleft()
                associative1 = tmp779
                associative_type1 = type(tmp779)
                subjects780 = deque(tmp779._args)
                matcher = CommutativeMatcher142459.get()
                tmp781 = subjects780
                subjects780 = []
                for s in tmp781:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp781, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142460
                        if len(subjects775) == 0:
                            pass
                            # State 142461
                            if len(subjects) == 0:
                                pass
                                # 59: atanh(x*c)
                                yield 59, subst1
                subjects775.appendleft(tmp779)
            if len(subjects775) >= 1 and isinstance(subjects775[0], Add):
                tmp782 = subjects775.popleft()
                associative1 = tmp782
                associative_type1 = type(tmp782)
                subjects783 = deque(tmp782._args)
                matcher = CommutativeMatcher144911.get()
                tmp784 = subjects783
                subjects783 = []
                for s in tmp784:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp784, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144917
                        if len(subjects775) == 0:
                            pass
                            # State 144918
                            if len(subjects) == 0:
                                pass
                                # 61: atanh(c + x*d)
                                yield 61, subst1
                subjects775.appendleft(tmp782)
            subjects.appendleft(tmp774)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp785 = subjects.popleft()
            subjects786 = deque(tmp785._args)
            # State 142535
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142536
                if len(subjects786) >= 1:
                    tmp788 = subjects786.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp788)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142537
                        if len(subjects786) == 0:
                            pass
                            # State 142538
                            if len(subjects) == 0:
                                pass
                                # 60: acoth(x*c)
                                yield 60, subst2
                    subjects786.appendleft(tmp788)
            if len(subjects786) >= 1 and isinstance(subjects786[0], Mul):
                tmp790 = subjects786.popleft()
                associative1 = tmp790
                associative_type1 = type(tmp790)
                subjects791 = deque(tmp790._args)
                matcher = CommutativeMatcher142540.get()
                tmp792 = subjects791
                subjects791 = []
                for s in tmp792:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp792, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142541
                        if len(subjects786) == 0:
                            pass
                            # State 142542
                            if len(subjects) == 0:
                                pass
                                # 60: acoth(x*c)
                                yield 60, subst1
                subjects786.appendleft(tmp790)
            if len(subjects786) >= 1 and isinstance(subjects786[0], Add):
                tmp793 = subjects786.popleft()
                associative1 = tmp793
                associative_type1 = type(tmp793)
                subjects794 = deque(tmp793._args)
                matcher = CommutativeMatcher144998.get()
                tmp795 = subjects794
                subjects794 = []
                for s in tmp795:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp795, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 145004
                        if len(subjects786) == 0:
                            pass
                            # State 145005
                            if len(subjects) == 0:
                                pass
                                # 62: acoth(c + x*d)
                                yield 62, subst1
                subjects786.appendleft(tmp793)
            subjects.appendleft(tmp785)
        if len(subjects) >= 1 and isinstance(subjects[0], asech):
            tmp796 = subjects.popleft()
            subjects797 = deque(tmp796._args)
            # State 148987
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 148988
                if len(subjects797) >= 1:
                    tmp799 = subjects797.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp799)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148989
                        if len(subjects797) == 0:
                            pass
                            # State 148990
                            if len(subjects) == 0:
                                pass
                                # 63: asech(x*c)
                                yield 63, subst2
                    subjects797.appendleft(tmp799)
            if len(subjects797) >= 1 and isinstance(subjects797[0], Mul):
                tmp801 = subjects797.popleft()
                associative1 = tmp801
                associative_type1 = type(tmp801)
                subjects802 = deque(tmp801._args)
                matcher = CommutativeMatcher148992.get()
                tmp803 = subjects802
                subjects802 = []
                for s in tmp803:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp803, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 148993
                        if len(subjects797) == 0:
                            pass
                            # State 148994
                            if len(subjects) == 0:
                                pass
                                # 63: asech(x*c)
                                yield 63, subst1
                subjects797.appendleft(tmp801)
            subjects.appendleft(tmp796)
        if len(subjects) >= 1 and isinstance(subjects[0], acsch):
            tmp804 = subjects.popleft()
            subjects805 = deque(tmp804._args)
            # State 149033
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 149034
                if len(subjects805) >= 1:
                    tmp807 = subjects805.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp807)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 149035
                        if len(subjects805) == 0:
                            pass
                            # State 149036
                            if len(subjects) == 0:
                                pass
                                # 64: acsch(x*c)
                                yield 64, subst2
                    subjects805.appendleft(tmp807)
            if len(subjects805) >= 1 and isinstance(subjects805[0], Mul):
                tmp809 = subjects805.popleft()
                associative1 = tmp809
                associative_type1 = type(tmp809)
                subjects810 = deque(tmp809._args)
                matcher = CommutativeMatcher149038.get()
                tmp811 = subjects810
                subjects810 = []
                for s in tmp811:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp811, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 149039
                        if len(subjects805) == 0:
                            pass
                            # State 149040
                            if len(subjects) == 0:
                                pass
                                # 64: acsch(x*c)
                                yield 64, subst1
                subjects805.appendleft(tmp809)
            subjects.appendleft(tmp804)
        return
        yield


from .generated_part002700 import *
from .generated_part002834 import *
from .generated_part002675 import *
from .generated_part002822 import *
from .generated_part002692 import *
from .generated_part002845 import *
from .generated_part002697 import *
from .generated_part002729 import *
from .generated_part002745 import *
from .generated_part002830 import *
from .generated_part002681 import *
from .generated_part002673 import *
from .generated_part002732 import *
from .generated_part002678 import *
from .generated_part002686 import *
from .generated_part002727 import *
from .generated_part002814 import *
from .generated_part002664 import *
from .generated_part002670 import *
from .generated_part002833 import *
from .generated_part002842 import *
from .generated_part002846 import *
from .generated_part002807 import *
from .generated_part002810 import *
from .generated_part002816 import *
from .generated_part002820 import *
from .generated_part002823 import *
from .generated_part002828 import *
from .generated_part002837 import *
from .generated_part002694 import *
from collections import deque
from .generated_part002723 import *
from .generated_part002840 import *
from .generated_part002825 import *
from .generated_part002677 import *
from .generated_part002721 import *
from .generated_part002687 import *
from .generated_part002703 import *
from matchpy.utils import VariableWithCount
from .generated_part002808 import *
from .generated_part002719 import *
from .generated_part002747 import *
from .generated_part002804 import *
from .generated_part002811 import *
from .generated_part002701 import *
from .generated_part002689 import *
from .generated_part002836 import *
from .generated_part002817 import *
from .generated_part002831 import *
from .generated_part002695 import *
from .generated_part002802 import *
from .generated_part002824 import *
from .generated_part002720 import *
from .generated_part002671 import *
from .generated_part002801 import *
from .generated_part002813 import *
from multiset import Multiset
from .generated_part002672 import *
from .generated_part002827 import *
from .generated_part002726 import *
from .generated_part002665 import *
from .generated_part002706 import *
from .generated_part002690 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part002683 import *
from .generated_part002805 import *
from .generated_part002839 import *
from .generated_part002684 import *
from .generated_part002843 import *
from .generated_part002680 import *
from .generated_part002674 import *
from .generated_part002819 import *