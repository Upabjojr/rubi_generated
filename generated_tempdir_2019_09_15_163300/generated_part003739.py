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


class CommutativeMatcher3225(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    3: (3, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({4: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    7: (7, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    8: (8, Multiset({6: 1, 7: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    9: (9, Multiset({6: 1, 7: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    10: (10, Multiset({8: 1, 9: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    11: (11, Multiset({10: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    12: (12, Multiset({11: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    13: (13, Multiset({12: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    14: (14, Multiset({13: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    15: (15, Multiset({14: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    16: (16, Multiset({15: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    17: (17, Multiset({16: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    18: (18, Multiset({17: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    19: (19, Multiset({13: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    20: (20, Multiset({14: 1, 18: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    21: (21, Multiset({19: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    22: (22, Multiset({10: 1, 20: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    23: (23, Multiset({21: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    24: (24, Multiset({11: 1, 22: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    25: (25, Multiset({12: 1, 23: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    26: (26, Multiset({24: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    27: (27, Multiset({12: 1, 25: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    28: (28, Multiset({26: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    29: (29, Multiset({13: 1, 27: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    30: (30, Multiset({28: 1, 29: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    31: (31, Multiset({23: 1, 30: 1}), [
      (VariableWithCount('i2.2.0_4', 1, 1, S(0)), Add)
]),
    32: (32, Multiset({27: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    33: (33, Multiset({31: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    34: (34, Multiset({32: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    35: (35, Multiset({33: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    36: (36, Multiset({34: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    37: (37, Multiset({35: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    38: (38, Multiset({34: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    39: (39, Multiset({35: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    40: (40, Multiset({36: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    41: (41, Multiset({37: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    42: (42, Multiset({38: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    43: (43, Multiset({39: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    44: (44, Multiset({36: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    45: (45, Multiset({37: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    46: (46, Multiset({40: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    47: (47, Multiset({41: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    48: (48, Multiset({42: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    49: (49, Multiset({43: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    50: (50, Multiset({44: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    51: (51, Multiset({45: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    52: (52, Multiset({46: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    53: (53, Multiset({47: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    54: (54, Multiset({48: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    55: (55, Multiset({49: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, None), Add)
]),
    56: (56, Multiset({50: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    57: (57, Multiset({51: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    58: (58, Multiset({52: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    59: (59, Multiset({53: 1, 54: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    60: (60, Multiset({55: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    61: (61, Multiset({56: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    62: (62, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    63: (63, Multiset({5: 1}), [
      (VariableWithCount('i2.2.0_4', 1, 1, None), Add)
]),
    64: (64, Multiset({57: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    65: (65, Multiset({58: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
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
        if CommutativeMatcher3225._instance is None:
            CommutativeMatcher3225._instance = CommutativeMatcher3225()
        return CommutativeMatcher3225._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3224
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 3226
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 3227
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 5865
                    if len(subjects) == 0:
                        pass
                        # 9: e*x
                        yield 9, subst2
                subjects.appendleft(tmp4)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 7887
                if len(subjects) >= 1:
                    tmp7 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7888
                        if len(subjects) == 0:
                            pass
                            # 17: f2*x**n
                            yield 17, subst3
                    subjects.appendleft(tmp7)
            if len(subjects) >= 1:
                tmp9 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp9)
                except ValueError:
                    pass
                else:
                    pass
                    # State 110655
                    if len(subjects) == 0:
                        pass
                        # 54: B*x
                        yield 54, subst2
                subjects.appendleft(tmp9)
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 139438
                    if len(subjects) == 0:
                        pass
                        # 57: g*x
                        yield 57, subst2
                subjects.appendleft(tmp11)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp13 = subjects.popleft()
                subjects14 = deque(tmp13._args)
                # State 4597
                if len(subjects14) >= 1:
                    tmp15 = subjects14.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp15)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 4598
                        if len(subjects14) >= 1 and subjects14[0] == Integer(2):
                            tmp17 = subjects14.popleft()
                            # State 4599
                            if len(subjects14) == 0:
                                pass
                                # State 4600
                                if len(subjects) == 0:
                                    pass
                                    # 2: v**2*c
                                    yield 2, subst2
                            subjects14.appendleft(tmp17)
                    subjects14.appendleft(tmp15)
                if len(subjects14) >= 1:
                    tmp18 = subjects14.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp18)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7889
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7890
                            if len(subjects14) == 0:
                                pass
                                # State 7891
                                if len(subjects) == 0:
                                    pass
                                    # 17: f2*x**n
                                    yield 17, subst3
                        if len(subjects14) >= 1:
                            tmp21 = subjects14.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp21)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7890
                                if len(subjects14) == 0:
                                    pass
                                    # State 7891
                                    if len(subjects) == 0:
                                        pass
                                        # 17: f2*x**n
                                        yield 17, subst3
                            subjects14.appendleft(tmp21)
                        if len(subjects14) >= 1:
                            tmp23 = subjects14.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp23)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9074
                                if len(subjects14) == 0:
                                    pass
                                    # State 9075
                                    if len(subjects) == 0:
                                        pass
                                        # 18: c*x**n2
                                        yield 18, subst3
                            subjects14.appendleft(tmp23)
                    subjects14.appendleft(tmp18)
                if len(subjects14) >= 1:
                    tmp25 = subjects14.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp25)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9730
                        if len(subjects14) >= 1:
                            tmp27 = subjects14.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_2', tmp27)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9731
                                if len(subjects14) == 0:
                                    pass
                                    # State 9732
                                    if len(subjects) == 0:
                                        pass
                                        # 30: x**n2*c
                                        yield 30, subst3
                            subjects14.appendleft(tmp27)
                    subjects14.appendleft(tmp25)
                subjects.appendleft(tmp13)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 3351
            if len(subjects) >= 1:
                tmp30 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp30)
                except ValueError:
                    pass
                else:
                    pass
                    # State 3352
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst2
                subjects.appendleft(tmp30)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 7495
                if len(subjects) >= 1:
                    tmp33 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0_1', tmp33)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7496
                        if len(subjects) == 0:
                            pass
                            # 13: x**n*b
                            yield 13, subst3
                    subjects.appendleft(tmp33)
                if len(subjects) >= 1:
                    tmp35 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0', tmp35)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9312
                        if len(subjects) == 0:
                            pass
                            # 26: x**n2*c
                            yield 26, subst3
                    subjects.appendleft(tmp35)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 9145
                if len(subjects) >= 1:
                    tmp38 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1', tmp38)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9146
                        if len(subjects) == 0:
                            pass
                            # 20: c*x**n2
                            yield 20, subst3
                    subjects.appendleft(tmp38)
            if len(subjects) >= 1:
                tmp40 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.1.0', tmp40)
                except ValueError:
                    pass
                else:
                    pass
                    # State 16118
                    if len(subjects) == 0:
                        pass
                        # 32: d*x
                        yield 32, subst2
                subjects.appendleft(tmp40)
            if len(subjects) >= 1:
                tmp42 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.1.0', tmp42)
                except ValueError:
                    pass
                else:
                    pass
                    # State 16764
                    if len(subjects) == 0:
                        pass
                        # 33: d*x
                        yield 33, subst2
                subjects.appendleft(tmp42)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp44 = subjects.popleft()
                subjects45 = deque(tmp44._args)
                # State 7180
                if len(subjects45) >= 1:
                    tmp46 = subjects45.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp46)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7181
                        if len(subjects45) >= 1:
                            tmp48 = subjects45.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp48)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7182
                                if len(subjects45) == 0:
                                    pass
                                    # State 7183
                                    if len(subjects) == 0:
                                        pass
                                        # 11: x**n*b2
                                        yield 11, subst3
                            subjects45.appendleft(tmp48)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7497
                            if len(subjects45) == 0:
                                pass
                                # State 7498
                                if len(subjects) == 0:
                                    pass
                                    # 13: x**n*b
                                    yield 13, subst3
                        if len(subjects45) >= 1:
                            tmp51 = subjects45.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp51)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7497
                                if len(subjects45) == 0:
                                    pass
                                    # State 7498
                                    if len(subjects) == 0:
                                        pass
                                        # 13: x**n*b
                                        yield 13, subst3
                            subjects45.appendleft(tmp51)
                        if len(subjects45) >= 1:
                            tmp53 = subjects45.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp53)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9701
                                if len(subjects45) == 0:
                                    pass
                                    # State 9702
                                    if len(subjects) == 0:
                                        pass
                                        # 28: x**mn*b
                                        yield 28, subst3
                            subjects45.appendleft(tmp53)
                    subjects45.appendleft(tmp46)
                if len(subjects45) >= 1:
                    tmp55 = subjects45.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp55)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7194
                        if len(subjects45) >= 1:
                            tmp57 = subjects45.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp57)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7195
                                if len(subjects45) == 0:
                                    pass
                                    # State 7196
                                    if len(subjects) == 0:
                                        pass
                                        # 12: x**n*b2
                                        yield 12, subst3
                            subjects45.appendleft(tmp57)
                        if len(subjects45) >= 1:
                            tmp59 = subjects45.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp59)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9262
                                if len(subjects45) == 0:
                                    pass
                                    # State 9263
                                    if len(subjects) == 0:
                                        pass
                                        # 24: x**n2*c
                                        yield 24, subst3
                            subjects45.appendleft(tmp59)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9313
                            if len(subjects45) == 0:
                                pass
                                # State 9314
                                if len(subjects) == 0:
                                    pass
                                    # 26: x**n2*c
                                    yield 26, subst3
                        if len(subjects45) >= 1:
                            tmp62 = subjects45.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp62)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9313
                                if len(subjects45) == 0:
                                    pass
                                    # State 9314
                                    if len(subjects) == 0:
                                        pass
                                        # 26: x**n2*c
                                        yield 26, subst3
                            subjects45.appendleft(tmp62)
                    subjects45.appendleft(tmp55)
                if len(subjects45) >= 1:
                    tmp64 = subjects45.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1', tmp64)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9147
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9148
                            if len(subjects45) == 0:
                                pass
                                # State 9149
                                if len(subjects) == 0:
                                    pass
                                    # 20: c*x**n2
                                    yield 20, subst3
                        if len(subjects45) >= 1:
                            tmp67 = subjects45.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp67)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9148
                                if len(subjects45) == 0:
                                    pass
                                    # State 9149
                                    if len(subjects) == 0:
                                        pass
                                        # 20: c*x**n2
                                        yield 20, subst3
                            subjects45.appendleft(tmp67)
                    subjects45.appendleft(tmp64)
                if len(subjects45) >= 1 and isinstance(subjects45[0], sin):
                    tmp69 = subjects45.popleft()
                    subjects70 = deque(tmp69._args)
                    # State 63927
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 63928
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63929
                            if len(subjects70) >= 1:
                                tmp73 = subjects70.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.1.0', tmp73)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 63930
                                    if len(subjects70) == 0:
                                        pass
                                        # State 63931
                                        if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                            tmp75 = subjects45.popleft()
                                            # State 63932
                                            if len(subjects45) == 0:
                                                pass
                                                # State 63933
                                                if len(subjects) == 0:
                                                    pass
                                                    # 38: d/sin(e + x*f)
                                                    yield 38, subst4
                                            subjects45.appendleft(tmp75)
                                subjects70.appendleft(tmp73)
                        if len(subjects70) >= 1 and isinstance(subjects70[0], Mul):
                            tmp76 = subjects70.popleft()
                            associative1 = tmp76
                            associative_type1 = type(tmp76)
                            subjects77 = deque(tmp76._args)
                            matcher = CommutativeMatcher63935.get()
                            tmp78 = subjects77
                            subjects77 = []
                            for s in tmp78:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp78, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 63936
                                    if len(subjects70) == 0:
                                        pass
                                        # State 63937
                                        if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                            tmp79 = subjects45.popleft()
                                            # State 63938
                                            if len(subjects45) == 0:
                                                pass
                                                # State 63939
                                                if len(subjects) == 0:
                                                    pass
                                                    # 38: d/sin(e + x*f)
                                                    yield 38, subst3
                                            subjects45.appendleft(tmp79)
                            subjects70.appendleft(tmp76)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 92297
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 92298
                            if len(subjects70) >= 1:
                                tmp82 = subjects70.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.3.1.0', tmp82)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 92299
                                    if len(subjects70) == 0:
                                        pass
                                        # State 92300
                                        if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                            tmp84 = subjects45.popleft()
                                            # State 92301
                                            if len(subjects45) == 0:
                                                pass
                                                # State 92302
                                                if len(subjects) == 0:
                                                    pass
                                                    # 47: d/sin(e + x*f)
                                                    yield 47, subst4
                                            subjects45.appendleft(tmp84)
                                subjects70.appendleft(tmp82)
                        if len(subjects70) >= 1 and isinstance(subjects70[0], Mul):
                            tmp85 = subjects70.popleft()
                            associative1 = tmp85
                            associative_type1 = type(tmp85)
                            subjects86 = deque(tmp85._args)
                            matcher = CommutativeMatcher92304.get()
                            tmp87 = subjects86
                            subjects86 = []
                            for s in tmp87:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp87, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 92305
                                    if len(subjects70) == 0:
                                        pass
                                        # State 92306
                                        if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                            tmp88 = subjects45.popleft()
                                            # State 92307
                                            if len(subjects45) == 0:
                                                pass
                                                # State 92308
                                                if len(subjects) == 0:
                                                    pass
                                                    # 47: d/sin(e + x*f)
                                                    yield 47, subst3
                                            subjects45.appendleft(tmp88)
                            subjects70.appendleft(tmp85)
                    if len(subjects70) >= 1 and isinstance(subjects70[0], Add):
                        tmp89 = subjects70.popleft()
                        associative1 = tmp89
                        associative_type1 = type(tmp89)
                        subjects90 = deque(tmp89._args)
                        matcher = CommutativeMatcher63941.get()
                        tmp91 = subjects90
                        subjects90 = []
                        for s in tmp91:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp91, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 63947
                                if len(subjects70) == 0:
                                    pass
                                    # State 63948
                                    if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                        tmp92 = subjects45.popleft()
                                        # State 63949
                                        if len(subjects45) == 0:
                                            pass
                                            # State 63950
                                            if len(subjects) == 0:
                                                pass
                                                # 38: d/sin(e + x*f)
                                                yield 38, subst2
                                        subjects45.appendleft(tmp92)
                            if pattern_index == 1:
                                pass
                                # State 92312
                                if len(subjects70) == 0:
                                    pass
                                    # State 92313
                                    if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                        tmp93 = subjects45.popleft()
                                        # State 92314
                                        if len(subjects45) == 0:
                                            pass
                                            # State 92315
                                            if len(subjects) == 0:
                                                pass
                                                # 47: d/sin(e + x*f)
                                                yield 47, subst2
                                        subjects45.appendleft(tmp93)
                        subjects70.appendleft(tmp89)
                    subjects45.appendleft(tmp69)
                if len(subjects45) >= 1 and isinstance(subjects45[0], cos):
                    tmp94 = subjects45.popleft()
                    subjects95 = deque(tmp94._args)
                    # State 64206
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 64207
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 64208
                            if len(subjects95) >= 1:
                                tmp98 = subjects95.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.1.0', tmp98)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 64209
                                    if len(subjects95) == 0:
                                        pass
                                        # State 64210
                                        if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                            tmp100 = subjects45.popleft()
                                            # State 64211
                                            if len(subjects45) == 0:
                                                pass
                                                # State 64212
                                                if len(subjects) == 0:
                                                    pass
                                                    # 39: d/cos(e + x*f)
                                                    yield 39, subst4
                                            subjects45.appendleft(tmp100)
                                subjects95.appendleft(tmp98)
                        if len(subjects95) >= 1 and isinstance(subjects95[0], Mul):
                            tmp101 = subjects95.popleft()
                            associative1 = tmp101
                            associative_type1 = type(tmp101)
                            subjects102 = deque(tmp101._args)
                            matcher = CommutativeMatcher64214.get()
                            tmp103 = subjects102
                            subjects102 = []
                            for s in tmp103:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp103, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 64215
                                    if len(subjects95) == 0:
                                        pass
                                        # State 64216
                                        if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                            tmp104 = subjects45.popleft()
                                            # State 64217
                                            if len(subjects45) == 0:
                                                pass
                                                # State 64218
                                                if len(subjects) == 0:
                                                    pass
                                                    # 39: d/cos(e + x*f)
                                                    yield 39, subst3
                                            subjects45.appendleft(tmp104)
                            subjects95.appendleft(tmp101)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 92231
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 92232
                            if len(subjects95) >= 1:
                                tmp107 = subjects95.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.3.1.0', tmp107)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 92233
                                    if len(subjects95) == 0:
                                        pass
                                        # State 92234
                                        if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                            tmp109 = subjects45.popleft()
                                            # State 92235
                                            if len(subjects45) == 0:
                                                pass
                                                # State 92236
                                                if len(subjects) == 0:
                                                    pass
                                                    # 46: d/cos(e + x*f)
                                                    yield 46, subst4
                                            subjects45.appendleft(tmp109)
                                subjects95.appendleft(tmp107)
                        if len(subjects95) >= 1 and isinstance(subjects95[0], Mul):
                            tmp110 = subjects95.popleft()
                            associative1 = tmp110
                            associative_type1 = type(tmp110)
                            subjects111 = deque(tmp110._args)
                            matcher = CommutativeMatcher92238.get()
                            tmp112 = subjects111
                            subjects111 = []
                            for s in tmp112:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp112, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 92239
                                    if len(subjects95) == 0:
                                        pass
                                        # State 92240
                                        if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                            tmp113 = subjects45.popleft()
                                            # State 92241
                                            if len(subjects45) == 0:
                                                pass
                                                # State 92242
                                                if len(subjects) == 0:
                                                    pass
                                                    # 46: d/cos(e + x*f)
                                                    yield 46, subst3
                                            subjects45.appendleft(tmp113)
                            subjects95.appendleft(tmp110)
                    if len(subjects95) >= 1 and isinstance(subjects95[0], Add):
                        tmp114 = subjects95.popleft()
                        associative1 = tmp114
                        associative_type1 = type(tmp114)
                        subjects115 = deque(tmp114._args)
                        matcher = CommutativeMatcher64220.get()
                        tmp116 = subjects115
                        subjects115 = []
                        for s in tmp116:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp116, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 64226
                                if len(subjects95) == 0:
                                    pass
                                    # State 64227
                                    if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                        tmp117 = subjects45.popleft()
                                        # State 64228
                                        if len(subjects45) == 0:
                                            pass
                                            # State 64229
                                            if len(subjects) == 0:
                                                pass
                                                # 39: d/cos(e + x*f)
                                                yield 39, subst2
                                        subjects45.appendleft(tmp117)
                            if pattern_index == 1:
                                pass
                                # State 92246
                                if len(subjects95) == 0:
                                    pass
                                    # State 92247
                                    if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                        tmp118 = subjects45.popleft()
                                        # State 92248
                                        if len(subjects45) == 0:
                                            pass
                                            # State 92249
                                            if len(subjects) == 0:
                                                pass
                                                # 46: d/cos(e + x*f)
                                                yield 46, subst2
                                        subjects45.appendleft(tmp118)
                        subjects95.appendleft(tmp114)
                    subjects45.appendleft(tmp94)
                if len(subjects45) >= 1 and isinstance(subjects45[0], tan):
                    tmp119 = subjects45.popleft()
                    subjects120 = deque(tmp119._args)
                    # State 80565
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80566
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 80567
                            if len(subjects120) >= 1:
                                tmp123 = subjects120.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.1.0', tmp123)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 80568
                                    if len(subjects120) == 0:
                                        pass
                                        # State 80569
                                        if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                            tmp125 = subjects45.popleft()
                                            # State 80570
                                            if len(subjects45) == 0:
                                                pass
                                                # State 80571
                                                if len(subjects) == 0:
                                                    pass
                                                    # 43: d/tan(e + x*f)
                                                    yield 43, subst4
                                            subjects45.appendleft(tmp125)
                                subjects120.appendleft(tmp123)
                        if len(subjects120) >= 1 and isinstance(subjects120[0], Mul):
                            tmp126 = subjects120.popleft()
                            associative1 = tmp126
                            associative_type1 = type(tmp126)
                            subjects127 = deque(tmp126._args)
                            matcher = CommutativeMatcher80573.get()
                            tmp128 = subjects127
                            subjects127 = []
                            for s in tmp128:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp128, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 80574
                                    if len(subjects120) == 0:
                                        pass
                                        # State 80575
                                        if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                            tmp129 = subjects45.popleft()
                                            # State 80576
                                            if len(subjects45) == 0:
                                                pass
                                                # State 80577
                                                if len(subjects) == 0:
                                                    pass
                                                    # 43: d/tan(e + x*f)
                                                    yield 43, subst3
                                            subjects45.appendleft(tmp129)
                            subjects120.appendleft(tmp126)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80904
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 80905
                            if len(subjects120) >= 1:
                                tmp132 = subjects120.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.4.1.0', tmp132)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 80906
                                    if len(subjects120) == 0:
                                        pass
                                        # State 80907
                                        if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                            tmp134 = subjects45.popleft()
                                            # State 80908
                                            if len(subjects45) == 0:
                                                pass
                                                # State 80909
                                                if len(subjects) == 0:
                                                    pass
                                                    # 44: d/tan(e + x*f)
                                                    yield 44, subst4
                                            subjects45.appendleft(tmp134)
                                subjects120.appendleft(tmp132)
                        if len(subjects120) >= 1 and isinstance(subjects120[0], Mul):
                            tmp135 = subjects120.popleft()
                            associative1 = tmp135
                            associative_type1 = type(tmp135)
                            subjects136 = deque(tmp135._args)
                            matcher = CommutativeMatcher80911.get()
                            tmp137 = subjects136
                            subjects136 = []
                            for s in tmp137:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp137, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 80912
                                    if len(subjects120) == 0:
                                        pass
                                        # State 80913
                                        if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                            tmp138 = subjects45.popleft()
                                            # State 80914
                                            if len(subjects45) == 0:
                                                pass
                                                # State 80915
                                                if len(subjects) == 0:
                                                    pass
                                                    # 44: d/tan(e + x*f)
                                                    yield 44, subst3
                                            subjects45.appendleft(tmp138)
                            subjects120.appendleft(tmp135)
                    if len(subjects120) >= 1 and isinstance(subjects120[0], Add):
                        tmp139 = subjects120.popleft()
                        associative1 = tmp139
                        associative_type1 = type(tmp139)
                        subjects140 = deque(tmp139._args)
                        matcher = CommutativeMatcher80579.get()
                        tmp141 = subjects140
                        subjects140 = []
                        for s in tmp141:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp141, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80585
                                if len(subjects120) == 0:
                                    pass
                                    # State 80586
                                    if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                        tmp142 = subjects45.popleft()
                                        # State 80587
                                        if len(subjects45) == 0:
                                            pass
                                            # State 80588
                                            if len(subjects) == 0:
                                                pass
                                                # 43: d/tan(e + x*f)
                                                yield 43, subst2
                                        subjects45.appendleft(tmp142)
                            if pattern_index == 1:
                                pass
                                # State 80919
                                if len(subjects120) == 0:
                                    pass
                                    # State 80920
                                    if len(subjects45) >= 1 and subjects45[0] == Integer(-1):
                                        tmp143 = subjects45.popleft()
                                        # State 80921
                                        if len(subjects45) == 0:
                                            pass
                                            # State 80922
                                            if len(subjects) == 0:
                                                pass
                                                # 44: d/tan(e + x*f)
                                                yield 44, subst2
                                        subjects45.appendleft(tmp143)
                        subjects120.appendleft(tmp139)
                    subjects45.appendleft(tmp119)
                subjects.appendleft(tmp44)
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp144 = subjects.popleft()
                subjects145 = deque(tmp144._args)
                # State 62259
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 62260
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 62261
                        if len(subjects145) >= 1:
                            tmp148 = subjects145.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2.1.0', tmp148)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 62262
                                if len(subjects145) == 0:
                                    pass
                                    # State 62263
                                    if len(subjects) == 0:
                                        pass
                                        # 34: d*sin(e + x*f)
                                        yield 34, subst4
                            subjects145.appendleft(tmp148)
                    if len(subjects145) >= 1 and isinstance(subjects145[0], Mul):
                        tmp150 = subjects145.popleft()
                        associative1 = tmp150
                        associative_type1 = type(tmp150)
                        subjects151 = deque(tmp150._args)
                        matcher = CommutativeMatcher62265.get()
                        tmp152 = subjects151
                        subjects151 = []
                        for s in tmp152:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp152, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 62266
                                if len(subjects145) == 0:
                                    pass
                                    # State 62267
                                    if len(subjects) == 0:
                                        pass
                                        # 34: d*sin(e + x*f)
                                        yield 34, subst3
                        subjects145.appendleft(tmp150)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63282
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 63283
                        if len(subjects145) >= 1:
                            tmp155 = subjects145.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.3.1.0', tmp155)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 63284
                                if len(subjects145) == 0:
                                    pass
                                    # State 63285
                                    if len(subjects) == 0:
                                        pass
                                        # 36: d*sin(e + x*f)
                                        yield 36, subst4
                            subjects145.appendleft(tmp155)
                    if len(subjects145) >= 1 and isinstance(subjects145[0], Mul):
                        tmp157 = subjects145.popleft()
                        associative1 = tmp157
                        associative_type1 = type(tmp157)
                        subjects158 = deque(tmp157._args)
                        matcher = CommutativeMatcher63287.get()
                        tmp159 = subjects158
                        subjects158 = []
                        for s in tmp159:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp159, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 63288
                                if len(subjects145) == 0:
                                    pass
                                    # State 63289
                                    if len(subjects) == 0:
                                        pass
                                        # 36: d*sin(e + x*f)
                                        yield 36, subst3
                        subjects145.appendleft(tmp157)
                if len(subjects145) >= 1 and isinstance(subjects145[0], Add):
                    tmp160 = subjects145.popleft()
                    associative1 = tmp160
                    associative_type1 = type(tmp160)
                    subjects161 = deque(tmp160._args)
                    matcher = CommutativeMatcher62269.get()
                    tmp162 = subjects161
                    subjects161 = []
                    for s in tmp162:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp162, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 62275
                            if len(subjects145) == 0:
                                pass
                                # State 62276
                                if len(subjects) == 0:
                                    pass
                                    # 34: d*sin(e + x*f)
                                    yield 34, subst2
                        if pattern_index == 1:
                            pass
                            # State 63293
                            if len(subjects145) == 0:
                                pass
                                # State 63294
                                if len(subjects) == 0:
                                    pass
                                    # 36: d*sin(e + x*f)
                                    yield 36, subst2
                    subjects145.appendleft(tmp160)
                subjects.appendleft(tmp144)
            if len(subjects) >= 1 and isinstance(subjects[0], cos):
                tmp163 = subjects.popleft()
                subjects164 = deque(tmp163._args)
                # State 62317
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 62318
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 62319
                        if len(subjects164) >= 1:
                            tmp167 = subjects164.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2.1.0', tmp167)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 62320
                                if len(subjects164) == 0:
                                    pass
                                    # State 62321
                                    if len(subjects) == 0:
                                        pass
                                        # 35: d*cos(e + x*f)
                                        yield 35, subst4
                            subjects164.appendleft(tmp167)
                    if len(subjects164) >= 1 and isinstance(subjects164[0], Mul):
                        tmp169 = subjects164.popleft()
                        associative1 = tmp169
                        associative_type1 = type(tmp169)
                        subjects170 = deque(tmp169._args)
                        matcher = CommutativeMatcher62323.get()
                        tmp171 = subjects170
                        subjects170 = []
                        for s in tmp171:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp171, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 62324
                                if len(subjects164) == 0:
                                    pass
                                    # State 62325
                                    if len(subjects) == 0:
                                        pass
                                        # 35: d*cos(e + x*f)
                                        yield 35, subst3
                        subjects164.appendleft(tmp169)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63458
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 63459
                        if len(subjects164) >= 1:
                            tmp174 = subjects164.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.3.1.0', tmp174)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 63460
                                if len(subjects164) == 0:
                                    pass
                                    # State 63461
                                    if len(subjects) == 0:
                                        pass
                                        # 37: d*cos(e + x*f)
                                        yield 37, subst4
                            subjects164.appendleft(tmp174)
                    if len(subjects164) >= 1 and isinstance(subjects164[0], Mul):
                        tmp176 = subjects164.popleft()
                        associative1 = tmp176
                        associative_type1 = type(tmp176)
                        subjects177 = deque(tmp176._args)
                        matcher = CommutativeMatcher63463.get()
                        tmp178 = subjects177
                        subjects177 = []
                        for s in tmp178:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp178, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 63464
                                if len(subjects164) == 0:
                                    pass
                                    # State 63465
                                    if len(subjects) == 0:
                                        pass
                                        # 37: d*cos(e + x*f)
                                        yield 37, subst3
                        subjects164.appendleft(tmp176)
                if len(subjects164) >= 1 and isinstance(subjects164[0], Add):
                    tmp179 = subjects164.popleft()
                    associative1 = tmp179
                    associative_type1 = type(tmp179)
                    subjects180 = deque(tmp179._args)
                    matcher = CommutativeMatcher62327.get()
                    tmp181 = subjects180
                    subjects180 = []
                    for s in tmp181:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp181, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 62333
                            if len(subjects164) == 0:
                                pass
                                # State 62334
                                if len(subjects) == 0:
                                    pass
                                    # 35: d*cos(e + x*f)
                                    yield 35, subst2
                        if pattern_index == 1:
                            pass
                            # State 63469
                            if len(subjects164) == 0:
                                pass
                                # State 63470
                                if len(subjects) == 0:
                                    pass
                                    # 37: d*cos(e + x*f)
                                    yield 37, subst2
                    subjects164.appendleft(tmp179)
                subjects.appendleft(tmp163)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp182 = subjects.popleft()
                subjects183 = deque(tmp182._args)
                # State 80507
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80508
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80509
                        if len(subjects183) >= 1:
                            tmp186 = subjects183.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.3.1.0', tmp186)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80510
                                if len(subjects183) == 0:
                                    pass
                                    # State 80511
                                    if len(subjects) == 0:
                                        pass
                                        # 42: d*tan(e + x*f)
                                        yield 42, subst4
                            subjects183.appendleft(tmp186)
                    if len(subjects183) >= 1 and isinstance(subjects183[0], Mul):
                        tmp188 = subjects183.popleft()
                        associative1 = tmp188
                        associative_type1 = type(tmp188)
                        subjects189 = deque(tmp188._args)
                        matcher = CommutativeMatcher80513.get()
                        tmp190 = subjects189
                        subjects189 = []
                        for s in tmp190:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp190, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80514
                                if len(subjects183) == 0:
                                    pass
                                    # State 80515
                                    if len(subjects) == 0:
                                        pass
                                        # 42: d*tan(e + x*f)
                                        yield 42, subst3
                        subjects183.appendleft(tmp188)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80970
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80971
                        if len(subjects183) >= 1:
                            tmp193 = subjects183.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2.1.0', tmp193)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80972
                                if len(subjects183) == 0:
                                    pass
                                    # State 80973
                                    if len(subjects) == 0:
                                        pass
                                        # 45: d*tan(e + x*f)
                                        yield 45, subst4
                            subjects183.appendleft(tmp193)
                    if len(subjects183) >= 1 and isinstance(subjects183[0], Mul):
                        tmp195 = subjects183.popleft()
                        associative1 = tmp195
                        associative_type1 = type(tmp195)
                        subjects196 = deque(tmp195._args)
                        matcher = CommutativeMatcher80975.get()
                        tmp197 = subjects196
                        subjects196 = []
                        for s in tmp197:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp197, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80976
                                if len(subjects183) == 0:
                                    pass
                                    # State 80977
                                    if len(subjects) == 0:
                                        pass
                                        # 45: d*tan(e + x*f)
                                        yield 45, subst3
                        subjects183.appendleft(tmp195)
                if len(subjects183) >= 1 and isinstance(subjects183[0], Add):
                    tmp198 = subjects183.popleft()
                    associative1 = tmp198
                    associative_type1 = type(tmp198)
                    subjects199 = deque(tmp198._args)
                    matcher = CommutativeMatcher80517.get()
                    tmp200 = subjects199
                    subjects199 = []
                    for s in tmp200:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp200, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 80523
                            if len(subjects183) == 0:
                                pass
                                # State 80524
                                if len(subjects) == 0:
                                    pass
                                    # 42: d*tan(e + x*f)
                                    yield 42, subst2
                        if pattern_index == 1:
                            pass
                            # State 80981
                            if len(subjects183) == 0:
                                pass
                                # State 80982
                                if len(subjects) == 0:
                                    pass
                                    # 45: d*tan(e + x*f)
                                    yield 45, subst2
                    subjects183.appendleft(tmp198)
                subjects.appendleft(tmp182)
            if len(subjects) >= 1 and isinstance(subjects[0], asin):
                tmp201 = subjects.popleft()
                subjects202 = deque(tmp201._args)
                # State 109028
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 109029
                    if len(subjects202) >= 1:
                        tmp204 = subjects202.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.0', tmp204)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 109030
                            if len(subjects202) == 0:
                                pass
                                # State 109031
                                if len(subjects) == 0:
                                    pass
                                    # 50: b*asin(x*c)
                                    yield 50, subst3
                        subjects202.appendleft(tmp204)
                if len(subjects202) >= 1 and isinstance(subjects202[0], Mul):
                    tmp206 = subjects202.popleft()
                    associative1 = tmp206
                    associative_type1 = type(tmp206)
                    subjects207 = deque(tmp206._args)
                    matcher = CommutativeMatcher109033.get()
                    tmp208 = subjects207
                    subjects207 = []
                    for s in tmp208:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp208, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 109034
                            if len(subjects202) == 0:
                                pass
                                # State 109035
                                if len(subjects) == 0:
                                    pass
                                    # 50: b*asin(x*c)
                                    yield 50, subst2
                    subjects202.appendleft(tmp206)
                subjects.appendleft(tmp201)
            if len(subjects) >= 1 and isinstance(subjects[0], acos):
                tmp209 = subjects.popleft()
                subjects210 = deque(tmp209._args)
                # State 109097
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 109098
                    if len(subjects210) >= 1:
                        tmp212 = subjects210.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.0', tmp212)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 109099
                            if len(subjects210) == 0:
                                pass
                                # State 109100
                                if len(subjects) == 0:
                                    pass
                                    # 51: b*acos(x*c)
                                    yield 51, subst3
                        subjects210.appendleft(tmp212)
                if len(subjects210) >= 1 and isinstance(subjects210[0], Mul):
                    tmp214 = subjects210.popleft()
                    associative1 = tmp214
                    associative_type1 = type(tmp214)
                    subjects215 = deque(tmp214._args)
                    matcher = CommutativeMatcher109102.get()
                    tmp216 = subjects215
                    subjects215 = []
                    for s in tmp216:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp216, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 109103
                            if len(subjects210) == 0:
                                pass
                                # State 109104
                                if len(subjects) == 0:
                                    pass
                                    # 51: b*acos(x*c)
                                    yield 51, subst2
                    subjects210.appendleft(tmp214)
                subjects.appendleft(tmp209)
            if len(subjects) >= 1 and isinstance(subjects[0], acosh):
                tmp217 = subjects.popleft()
                subjects218 = deque(tmp217._args)
                # State 138787
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 138788
                    if len(subjects218) >= 1:
                        tmp220 = subjects218.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.0', tmp220)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 138789
                            if len(subjects218) == 0:
                                pass
                                # State 138790
                                if len(subjects) == 0:
                                    pass
                                    # 55: b*acosh(x*c)
                                    yield 55, subst3
                        subjects218.appendleft(tmp220)
                if len(subjects218) >= 1 and isinstance(subjects218[0], Mul):
                    tmp222 = subjects218.popleft()
                    associative1 = tmp222
                    associative_type1 = type(tmp222)
                    subjects223 = deque(tmp222._args)
                    matcher = CommutativeMatcher138792.get()
                    tmp224 = subjects223
                    subjects223 = []
                    for s in tmp224:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp224, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 138793
                            if len(subjects218) == 0:
                                pass
                                # State 138794
                                if len(subjects) == 0:
                                    pass
                                    # 55: b*acosh(x*c)
                                    yield 55, subst2
                    subjects218.appendleft(tmp222)
                subjects.appendleft(tmp217)
            if len(subjects) >= 1 and isinstance(subjects[0], asinh):
                tmp225 = subjects.popleft()
                subjects226 = deque(tmp225._args)
                # State 138856
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 138857
                    if len(subjects226) >= 1:
                        tmp228 = subjects226.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.0', tmp228)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 138858
                            if len(subjects226) == 0:
                                pass
                                # State 138859
                                if len(subjects) == 0:
                                    pass
                                    # 56: b*asinh(x*c)
                                    yield 56, subst3
                        subjects226.appendleft(tmp228)
                if len(subjects226) >= 1 and isinstance(subjects226[0], Mul):
                    tmp230 = subjects226.popleft()
                    associative1 = tmp230
                    associative_type1 = type(tmp230)
                    subjects231 = deque(tmp230._args)
                    matcher = CommutativeMatcher138861.get()
                    tmp232 = subjects231
                    subjects231 = []
                    for s in tmp232:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp232, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 138862
                            if len(subjects226) == 0:
                                pass
                                # State 138863
                                if len(subjects) == 0:
                                    pass
                                    # 56: b*asinh(x*c)
                                    yield 56, subst2
                    subjects226.appendleft(tmp230)
                subjects.appendleft(tmp225)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_4', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 4606
            if len(subjects) >= 1:
                tmp234 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp234)
                except ValueError:
                    pass
                else:
                    pass
                    # State 4607
                    if len(subjects) == 0:
                        pass
                        # 3: x*h
                        yield 3, subst2
                subjects.appendleft(tmp234)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp236 = subjects.popleft()
                subjects237 = deque(tmp236._args)
                # State 5495
                if len(subjects237) >= 1:
                    tmp238 = subjects237.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp238)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 5496
                        if len(subjects237) >= 1 and subjects237[0] == Integer(2):
                            tmp240 = subjects237.popleft()
                            # State 5497
                            if len(subjects237) == 0:
                                pass
                                # State 5498
                                if len(subjects) == 0:
                                    pass
                                    # 6: v**2*f
                                    yield 6, subst2
                            subjects237.appendleft(tmp240)
                    subjects237.appendleft(tmp238)
                subjects.appendleft(tmp236)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 4618
            if len(subjects) >= 1:
                tmp242 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp242)
                except ValueError:
                    pass
                else:
                    pass
                    # State 4619
                    if len(subjects) == 0:
                        pass
                        # 4: e*x
                        yield 4, subst2
                subjects.appendleft(tmp242)
            if len(subjects) >= 1:
                tmp244 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp244)
                except ValueError:
                    pass
                else:
                    pass
                    # State 4834
                    if len(subjects) == 0:
                        pass
                        # 5: x*g
                        yield 5, subst2
                subjects.appendleft(tmp244)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 7867
                if len(subjects) >= 1:
                    tmp247 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp247)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7868
                        if len(subjects) == 0:
                            pass
                            # 16: b2*x**n
                            yield 16, subst3
                    subjects.appendleft(tmp247)
                if len(subjects) >= 1:
                    tmp249 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0_1', tmp249)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9229
                        if len(subjects) == 0:
                            pass
                            # 22: x**n*f
                            yield 22, subst3
                    subjects.appendleft(tmp249)
                if len(subjects) >= 1:
                    tmp251 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0', tmp251)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9299
                        if len(subjects) == 0:
                            pass
                            # 25: x**n2*f1
                            yield 25, subst3
                    subjects.appendleft(tmp251)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 9669
                if len(subjects) >= 1:
                    tmp254 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0_1', tmp254)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9670
                        if len(subjects) == 0:
                            pass
                            # 27: x**n2*c
                            yield 27, subst3
                    subjects.appendleft(tmp254)
                if len(subjects) >= 1:
                    tmp256 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0', tmp256)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12243
                        if len(subjects) == 0:
                            pass
                            # 31: x**n*d
                            yield 31, subst3
                    subjects.appendleft(tmp256)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 9706
                if len(subjects) >= 1:
                    tmp259 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0_1', tmp259)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9707
                        if len(subjects) == 0:
                            pass
                            # 29: x**mn*c
                            yield 29, subst3
                    subjects.appendleft(tmp259)
            if len(subjects) >= 1:
                tmp261 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', tmp261)
                except ValueError:
                    pass
                else:
                    pass
                    # State 109607
                    if len(subjects) == 0:
                        pass
                        # 52: g*x
                        yield 52, subst2
                subjects.appendleft(tmp261)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp263 = subjects.popleft()
                subjects264 = deque(tmp263._args)
                # State 5857
                if len(subjects264) >= 1:
                    tmp265 = subjects264.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp265)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 5858
                        if len(subjects264) >= 1 and subjects264[0] == Integer(2):
                            tmp267 = subjects264.popleft()
                            # State 5859
                            if len(subjects264) == 0:
                                pass
                                # State 5860
                                if len(subjects) == 0:
                                    pass
                                    # 8: f*x**2
                                    yield 8, subst2
                            subjects264.appendleft(tmp267)
                        if len(subjects264) >= 1:
                            tmp268 = subjects264.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp268)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7601
                                if len(subjects264) == 0:
                                    pass
                                    # State 7602
                                    if len(subjects) == 0:
                                        pass
                                        # 14: f*x**j
                                        yield 14, subst3
                            subjects264.appendleft(tmp268)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7869
                            if len(subjects264) == 0:
                                pass
                                # State 7870
                                if len(subjects) == 0:
                                    pass
                                    # 16: b2*x**n
                                    yield 16, subst3
                        if len(subjects264) >= 1:
                            tmp271 = subjects264.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp271)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7869
                                if len(subjects264) == 0:
                                    pass
                                    # State 7870
                                    if len(subjects) == 0:
                                        pass
                                        # 16: b2*x**n
                                        yield 16, subst3
                            subjects264.appendleft(tmp271)
                        if len(subjects264) >= 1:
                            tmp273 = subjects264.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp273)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9085
                                if len(subjects264) == 0:
                                    pass
                                    # State 9086
                                    if len(subjects) == 0:
                                        pass
                                        # 19: c*x**n2
                                        yield 19, subst3
                            subjects264.appendleft(tmp273)
                    subjects264.appendleft(tmp265)
                if len(subjects264) >= 1:
                    tmp275 = subjects264.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1_2', tmp275)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7805
                        if len(subjects264) >= 1:
                            tmp277 = subjects264.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp277)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7806
                                if len(subjects264) == 0:
                                    pass
                                    # State 7807
                                    if len(subjects) == 0:
                                        pass
                                        # 15: f*w**n
                                        yield 15, subst3
                            subjects264.appendleft(tmp277)
                    subjects264.appendleft(tmp275)
                if len(subjects264) >= 1:
                    tmp279 = subjects264.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp279)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9230
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9231
                            if len(subjects264) == 0:
                                pass
                                # State 9232
                                if len(subjects) == 0:
                                    pass
                                    # 22: x**n*f
                                    yield 22, subst3
                        if len(subjects264) >= 1:
                            tmp282 = subjects264.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp282)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9231
                                if len(subjects264) == 0:
                                    pass
                                    # State 9232
                                    if len(subjects) == 0:
                                        pass
                                        # 22: x**n*f
                                        yield 22, subst3
                            subjects264.appendleft(tmp282)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9671
                            if len(subjects264) == 0:
                                pass
                                # State 9672
                                if len(subjects) == 0:
                                    pass
                                    # 27: x**n2*c
                                    yield 27, subst3
                        if len(subjects264) >= 1:
                            tmp285 = subjects264.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_2', tmp285)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9671
                                if len(subjects264) == 0:
                                    pass
                                    # State 9672
                                    if len(subjects) == 0:
                                        pass
                                        # 27: x**n2*c
                                        yield 27, subst3
                            subjects264.appendleft(tmp285)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9708
                            if len(subjects264) == 0:
                                pass
                                # State 9709
                                if len(subjects) == 0:
                                    pass
                                    # 29: x**mn*c
                                    yield 29, subst3
                        if len(subjects264) >= 1:
                            tmp288 = subjects264.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp288)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9708
                                if len(subjects264) == 0:
                                    pass
                                    # State 9709
                                    if len(subjects) == 0:
                                        pass
                                        # 29: x**mn*c
                                        yield 29, subst3
                            subjects264.appendleft(tmp288)
                    subjects264.appendleft(tmp279)
                if len(subjects264) >= 1:
                    tmp290 = subjects264.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp290)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9244
                        if len(subjects264) >= 1:
                            tmp292 = subjects264.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp292)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9245
                                if len(subjects264) == 0:
                                    pass
                                    # State 9246
                                    if len(subjects) == 0:
                                        pass
                                        # 23: x**n2*c
                                        yield 23, subst3
                            subjects264.appendleft(tmp292)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9300
                            if len(subjects264) == 0:
                                pass
                                # State 9301
                                if len(subjects) == 0:
                                    pass
                                    # 25: x**n2*f1
                                    yield 25, subst3
                        if len(subjects264) >= 1:
                            tmp295 = subjects264.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp295)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9300
                                if len(subjects264) == 0:
                                    pass
                                    # State 9301
                                    if len(subjects) == 0:
                                        pass
                                        # 25: x**n2*f1
                                        yield 25, subst3
                            subjects264.appendleft(tmp295)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 12244
                            if len(subjects264) == 0:
                                pass
                                # State 12245
                                if len(subjects) == 0:
                                    pass
                                    # 31: x**n*d
                                    yield 31, subst3
                        if len(subjects264) >= 1:
                            tmp298 = subjects264.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_2', tmp298)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 12244
                                if len(subjects264) == 0:
                                    pass
                                    # State 12245
                                    if len(subjects) == 0:
                                        pass
                                        # 31: x**n*d
                                        yield 31, subst3
                            subjects264.appendleft(tmp298)
                    subjects264.appendleft(tmp290)
                if len(subjects264) >= 1:
                    tmp300 = subjects264.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.0', tmp300)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 110648
                        if len(subjects264) >= 1 and subjects264[0] == Integer(2):
                            tmp302 = subjects264.popleft()
                            # State 110649
                            if len(subjects264) == 0:
                                pass
                                # State 110650
                                if len(subjects) == 0:
                                    pass
                                    # 53: C*x**2
                                    yield 53, subst2
                            subjects264.appendleft(tmp302)
                    subjects264.appendleft(tmp300)
                if len(subjects264) >= 1 and isinstance(subjects264[0], cos):
                    tmp303 = subjects264.popleft()
                    subjects304 = deque(tmp303._args)
                    # State 93174
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 93175
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 93176
                            if len(subjects304) >= 1:
                                tmp307 = subjects304.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.3.1.0', tmp307)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 93177
                                    if len(subjects304) == 0:
                                        pass
                                        # State 93178
                                        if len(subjects264) >= 1 and subjects264[0] == Integer(-1):
                                            tmp309 = subjects264.popleft()
                                            # State 93179
                                            if len(subjects264) == 0:
                                                pass
                                                # State 93180
                                                if len(subjects) == 0:
                                                    pass
                                                    # 48: d/cos(e + x*f)
                                                    yield 48, subst4
                                            subjects264.appendleft(tmp309)
                                subjects304.appendleft(tmp307)
                        if len(subjects304) >= 1 and isinstance(subjects304[0], Mul):
                            tmp310 = subjects304.popleft()
                            associative1 = tmp310
                            associative_type1 = type(tmp310)
                            subjects311 = deque(tmp310._args)
                            matcher = CommutativeMatcher93182.get()
                            tmp312 = subjects311
                            subjects311 = []
                            for s in tmp312:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp312, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 93183
                                    if len(subjects304) == 0:
                                        pass
                                        # State 93184
                                        if len(subjects264) >= 1 and subjects264[0] == Integer(-1):
                                            tmp313 = subjects264.popleft()
                                            # State 93185
                                            if len(subjects264) == 0:
                                                pass
                                                # State 93186
                                                if len(subjects) == 0:
                                                    pass
                                                    # 48: d/cos(e + x*f)
                                                    yield 48, subst3
                                            subjects264.appendleft(tmp313)
                            subjects304.appendleft(tmp310)
                    if len(subjects304) >= 1 and isinstance(subjects304[0], Add):
                        tmp314 = subjects304.popleft()
                        associative1 = tmp314
                        associative_type1 = type(tmp314)
                        subjects315 = deque(tmp314._args)
                        matcher = CommutativeMatcher93188.get()
                        tmp316 = subjects315
                        subjects315 = []
                        for s in tmp316:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp316, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 93194
                                if len(subjects304) == 0:
                                    pass
                                    # State 93195
                                    if len(subjects264) >= 1 and subjects264[0] == Integer(-1):
                                        tmp317 = subjects264.popleft()
                                        # State 93196
                                        if len(subjects264) == 0:
                                            pass
                                            # State 93197
                                            if len(subjects) == 0:
                                                pass
                                                # 48: d/cos(e + x*f)
                                                yield 48, subst2
                                        subjects264.appendleft(tmp317)
                        subjects304.appendleft(tmp314)
                    subjects264.appendleft(tmp303)
                if len(subjects264) >= 1 and isinstance(subjects264[0], sin):
                    tmp318 = subjects264.popleft()
                    subjects319 = deque(tmp318._args)
                    # State 93360
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 93361
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 93362
                            if len(subjects319) >= 1:
                                tmp322 = subjects319.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.3.1.0', tmp322)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 93363
                                    if len(subjects319) == 0:
                                        pass
                                        # State 93364
                                        if len(subjects264) >= 1 and subjects264[0] == Integer(-1):
                                            tmp324 = subjects264.popleft()
                                            # State 93365
                                            if len(subjects264) == 0:
                                                pass
                                                # State 93366
                                                if len(subjects) == 0:
                                                    pass
                                                    # 49: d/sin(e + x*f)
                                                    yield 49, subst4
                                            subjects264.appendleft(tmp324)
                                subjects319.appendleft(tmp322)
                        if len(subjects319) >= 1 and isinstance(subjects319[0], Mul):
                            tmp325 = subjects319.popleft()
                            associative1 = tmp325
                            associative_type1 = type(tmp325)
                            subjects326 = deque(tmp325._args)
                            matcher = CommutativeMatcher93368.get()
                            tmp327 = subjects326
                            subjects326 = []
                            for s in tmp327:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp327, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 93369
                                    if len(subjects319) == 0:
                                        pass
                                        # State 93370
                                        if len(subjects264) >= 1 and subjects264[0] == Integer(-1):
                                            tmp328 = subjects264.popleft()
                                            # State 93371
                                            if len(subjects264) == 0:
                                                pass
                                                # State 93372
                                                if len(subjects) == 0:
                                                    pass
                                                    # 49: d/sin(e + x*f)
                                                    yield 49, subst3
                                            subjects264.appendleft(tmp328)
                            subjects319.appendleft(tmp325)
                    if len(subjects319) >= 1 and isinstance(subjects319[0], Add):
                        tmp329 = subjects319.popleft()
                        associative1 = tmp329
                        associative_type1 = type(tmp329)
                        subjects330 = deque(tmp329._args)
                        matcher = CommutativeMatcher93374.get()
                        tmp331 = subjects330
                        subjects330 = []
                        for s in tmp331:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp331, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 93380
                                if len(subjects319) == 0:
                                    pass
                                    # State 93381
                                    if len(subjects264) >= 1 and subjects264[0] == Integer(-1):
                                        tmp332 = subjects264.popleft()
                                        # State 93382
                                        if len(subjects264) == 0:
                                            pass
                                            # State 93383
                                            if len(subjects) == 0:
                                                pass
                                                # 49: d/sin(e + x*f)
                                                yield 49, subst2
                                        subjects264.appendleft(tmp332)
                        subjects319.appendleft(tmp329)
                    subjects264.appendleft(tmp318)
                subjects.appendleft(tmp263)
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp333 = subjects.popleft()
                subjects334 = deque(tmp333._args)
                # State 65397
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65398
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 65399
                        if len(subjects334) >= 1:
                            tmp337 = subjects334.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.1.0', tmp337)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 65400
                                if len(subjects334) == 0:
                                    pass
                                    # State 65401
                                    if len(subjects) == 0:
                                        pass
                                        # 40: d*sin(c + x*d)
                                        yield 40, subst4
                            subjects334.appendleft(tmp337)
                    if len(subjects334) >= 1 and isinstance(subjects334[0], Mul):
                        tmp339 = subjects334.popleft()
                        associative1 = tmp339
                        associative_type1 = type(tmp339)
                        subjects340 = deque(tmp339._args)
                        matcher = CommutativeMatcher65403.get()
                        tmp341 = subjects340
                        subjects340 = []
                        for s in tmp341:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp341, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 65404
                                if len(subjects334) == 0:
                                    pass
                                    # State 65405
                                    if len(subjects) == 0:
                                        pass
                                        # 40: d*sin(c + x*d)
                                        yield 40, subst3
                        subjects334.appendleft(tmp339)
                if len(subjects334) >= 1 and isinstance(subjects334[0], Add):
                    tmp342 = subjects334.popleft()
                    associative1 = tmp342
                    associative_type1 = type(tmp342)
                    subjects343 = deque(tmp342._args)
                    matcher = CommutativeMatcher65407.get()
                    tmp344 = subjects343
                    subjects343 = []
                    for s in tmp344:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp344, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 65413
                            if len(subjects334) == 0:
                                pass
                                # State 65414
                                if len(subjects) == 0:
                                    pass
                                    # 40: d*sin(c + x*d)
                                    yield 40, subst2
                    subjects334.appendleft(tmp342)
                subjects.appendleft(tmp333)
            if len(subjects) >= 1 and isinstance(subjects[0], cos):
                tmp345 = subjects.popleft()
                subjects346 = deque(tmp345._args)
                # State 65455
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65456
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 65457
                        if len(subjects346) >= 1:
                            tmp349 = subjects346.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.1.0', tmp349)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 65458
                                if len(subjects346) == 0:
                                    pass
                                    # State 65459
                                    if len(subjects) == 0:
                                        pass
                                        # 41: d*cos(c + x*d)
                                        yield 41, subst4
                            subjects346.appendleft(tmp349)
                    if len(subjects346) >= 1 and isinstance(subjects346[0], Mul):
                        tmp351 = subjects346.popleft()
                        associative1 = tmp351
                        associative_type1 = type(tmp351)
                        subjects352 = deque(tmp351._args)
                        matcher = CommutativeMatcher65461.get()
                        tmp353 = subjects352
                        subjects352 = []
                        for s in tmp353:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp353, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 65462
                                if len(subjects346) == 0:
                                    pass
                                    # State 65463
                                    if len(subjects) == 0:
                                        pass
                                        # 41: d*cos(c + x*d)
                                        yield 41, subst3
                        subjects346.appendleft(tmp351)
                if len(subjects346) >= 1 and isinstance(subjects346[0], Add):
                    tmp354 = subjects346.popleft()
                    associative1 = tmp354
                    associative_type1 = type(tmp354)
                    subjects355 = deque(tmp354._args)
                    matcher = CommutativeMatcher65465.get()
                    tmp356 = subjects355
                    subjects355 = []
                    for s in tmp356:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp356, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 65471
                            if len(subjects346) == 0:
                                pass
                                # State 65472
                                if len(subjects) == 0:
                                    pass
                                    # 41: d*cos(c + x*d)
                                    yield 41, subst2
                    subjects346.appendleft(tmp354)
                subjects.appendleft(tmp345)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_5', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 5500
            if len(subjects) >= 1:
                tmp358 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp358)
                except ValueError:
                    pass
                else:
                    pass
                    # State 5501
                    if len(subjects) == 0:
                        pass
                        # 7: x*e
                        yield 7, subst2
                subjects.appendleft(tmp358)
            if len(subjects) >= 1:
                tmp360 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0_4', tmp360)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151680
                    if len(subjects) == 0:
                        pass
                        # 58: y*b
                        yield 58, subst2
                subjects.appendleft(tmp360)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 7126
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp363 = subjects.popleft()
                subjects364 = deque(tmp363._args)
                # State 7127
                if len(subjects364) >= 1:
                    tmp365 = subjects364.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1', tmp365)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7128
                        if len(subjects364) >= 1:
                            tmp367 = subjects364.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2', tmp367)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7129
                                if len(subjects364) == 0:
                                    pass
                                    # State 7130
                                    if len(subjects) == 0:
                                        pass
                                        # 10: d*x**n
                                        yield 10, subst3
                            subjects364.appendleft(tmp367)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9171
                            if len(subjects364) == 0:
                                pass
                                # State 9172
                                if len(subjects) == 0:
                                    pass
                                    # 21: c*x**n2
                                    yield 21, subst3
                        if len(subjects364) >= 1:
                            tmp370 = subjects364.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp370)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 9171
                                if len(subjects364) == 0:
                                    pass
                                    # State 9172
                                    if len(subjects) == 0:
                                        pass
                                        # 21: c*x**n2
                                        yield 21, subst3
                            subjects364.appendleft(tmp370)
                    subjects364.appendleft(tmp365)
                subjects.appendleft(tmp363)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 9169
                if len(subjects) >= 1:
                    tmp373 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1', tmp373)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 9170
                        if len(subjects) == 0:
                            pass
                            # 21: c*x**n2
                            yield 21, subst3
                    subjects.appendleft(tmp373)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp375 = subjects.popleft()
            associative1 = tmp375
            associative_type1 = type(tmp375)
            subjects376 = deque(tmp375._args)
            matcher = CommutativeMatcher3229.get()
            tmp377 = subjects376
            subjects376 = []
            for s in tmp377:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp377, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 3230
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 3353
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 4605
                    if len(subjects) == 0:
                        pass
                        # 2: v**2*c
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 4608
                    if len(subjects) == 0:
                        pass
                        # 3: x*h
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 4620
                    if len(subjects) == 0:
                        pass
                        # 4: e*x
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 4835
                    if len(subjects) == 0:
                        pass
                        # 5: x*g
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 5499
                    if len(subjects) == 0:
                        pass
                        # 6: v**2*f
                        yield 6, subst1
                if pattern_index == 7:
                    pass
                    # State 5502
                    if len(subjects) == 0:
                        pass
                        # 7: x*e
                        yield 7, subst1
                if pattern_index == 8:
                    pass
                    # State 5864
                    if len(subjects) == 0:
                        pass
                        # 8: f*x**2
                        yield 8, subst1
                if pattern_index == 9:
                    pass
                    # State 5866
                    if len(subjects) == 0:
                        pass
                        # 9: e*x
                        yield 9, subst1
                if pattern_index == 10:
                    pass
                    # State 7134
                    if len(subjects) == 0:
                        pass
                        # 10: d*x**n
                        yield 10, subst1
                if pattern_index == 11:
                    pass
                    # State 7187
                    if len(subjects) == 0:
                        pass
                        # 11: x**n*b2
                        yield 11, subst1
                if pattern_index == 12:
                    pass
                    # State 7200
                    if len(subjects) == 0:
                        pass
                        # 12: x**n*b2
                        yield 12, subst1
                if pattern_index == 13:
                    pass
                    # State 7503
                    if len(subjects) == 0:
                        pass
                        # 13: x**n*b
                        yield 13, subst1
                if pattern_index == 14:
                    pass
                    # State 7605
                    if len(subjects) == 0:
                        pass
                        # 14: f*x**j
                        yield 14, subst1
                if pattern_index == 15:
                    pass
                    # State 7811
                    if len(subjects) == 0:
                        pass
                        # 15: f*w**n
                        yield 15, subst1
                if pattern_index == 16:
                    pass
                    # State 7874
                    if len(subjects) == 0:
                        pass
                        # 16: b2*x**n
                        yield 16, subst1
                if pattern_index == 17:
                    pass
                    # State 7892
                    if len(subjects) == 0:
                        pass
                        # 17: f2*x**n
                        yield 17, subst1
                if pattern_index == 18:
                    pass
                    # State 9078
                    if len(subjects) == 0:
                        pass
                        # 18: c*x**n2
                        yield 18, subst1
                if pattern_index == 19:
                    pass
                    # State 9087
                    if len(subjects) == 0:
                        pass
                        # 19: c*x**n2
                        yield 19, subst1
                if pattern_index == 20:
                    pass
                    # State 9154
                    if len(subjects) == 0:
                        pass
                        # 20: c*x**n2
                        yield 20, subst1
                if pattern_index == 21:
                    pass
                    # State 9173
                    if len(subjects) == 0:
                        pass
                        # 21: c*x**n2
                        yield 21, subst1
                if pattern_index == 22:
                    pass
                    # State 9233
                    if len(subjects) == 0:
                        pass
                        # 22: x**n*f
                        yield 22, subst1
                if pattern_index == 23:
                    pass
                    # State 9249
                    if len(subjects) == 0:
                        pass
                        # 23: x**n2*c
                        yield 23, subst1
                if pattern_index == 24:
                    pass
                    # State 9264
                    if len(subjects) == 0:
                        pass
                        # 24: x**n2*c
                        yield 24, subst1
                if pattern_index == 25:
                    pass
                    # State 9305
                    if len(subjects) == 0:
                        pass
                        # 25: x**n2*f1
                        yield 25, subst1
                if pattern_index == 26:
                    pass
                    # State 9315
                    if len(subjects) == 0:
                        pass
                        # 26: x**n2*c
                        yield 26, subst1
                if pattern_index == 27:
                    pass
                    # State 9677
                    if len(subjects) == 0:
                        pass
                        # 27: x**n2*c
                        yield 27, subst1
                if pattern_index == 28:
                    pass
                    # State 9705
                    if len(subjects) == 0:
                        pass
                        # 28: x**mn*b
                        yield 28, subst1
                if pattern_index == 29:
                    pass
                    # State 9713
                    if len(subjects) == 0:
                        pass
                        # 29: x**mn*c
                        yield 29, subst1
                if pattern_index == 30:
                    pass
                    # State 9735
                    if len(subjects) == 0:
                        pass
                        # 30: x**n2*c
                        yield 30, subst1
                if pattern_index == 31:
                    pass
                    # State 12249
                    if len(subjects) == 0:
                        pass
                        # 31: x**n*d
                        yield 31, subst1
                if pattern_index == 32:
                    pass
                    # State 16119
                    if len(subjects) == 0:
                        pass
                        # 32: d*x
                        yield 32, subst1
                if pattern_index == 33:
                    pass
                    # State 16765
                    if len(subjects) == 0:
                        pass
                        # 33: d*x
                        yield 33, subst1
                if pattern_index == 34:
                    pass
                    # State 62295
                    if len(subjects) == 0:
                        pass
                        # 34: d*sin(e + x*f)
                        yield 34, subst1
                if pattern_index == 35:
                    pass
                    # State 62353
                    if len(subjects) == 0:
                        pass
                        # 35: d*cos(e + x*f)
                        yield 35, subst1
                if pattern_index == 36:
                    pass
                    # State 63308
                    if len(subjects) == 0:
                        pass
                        # 36: d*sin(e + x*f)
                        yield 36, subst1
                if pattern_index == 37:
                    pass
                    # State 63484
                    if len(subjects) == 0:
                        pass
                        # 37: d*cos(e + x*f)
                        yield 37, subst1
                if pattern_index == 38:
                    pass
                    # State 63975
                    if len(subjects) == 0:
                        pass
                        # 38: d/sin(e + x*f)
                        yield 38, subst1
                if pattern_index == 39:
                    pass
                    # State 64254
                    if len(subjects) == 0:
                        pass
                        # 39: d/cos(e + x*f)
                        yield 39, subst1
                if pattern_index == 40:
                    pass
                    # State 65428
                    if len(subjects) == 0:
                        pass
                        # 40: d*sin(c + x*d)
                        yield 40, subst1
                if pattern_index == 41:
                    pass
                    # State 65486
                    if len(subjects) == 0:
                        pass
                        # 41: d*cos(c + x*d)
                        yield 41, subst1
                if pattern_index == 42:
                    pass
                    # State 80543
                    if len(subjects) == 0:
                        pass
                        # 42: d*tan(e + x*f)
                        yield 42, subst1
                if pattern_index == 43:
                    pass
                    # State 80613
                    if len(subjects) == 0:
                        pass
                        # 43: d/tan(e + x*f)
                        yield 43, subst1
                if pattern_index == 44:
                    pass
                    # State 80942
                    if len(subjects) == 0:
                        pass
                        # 44: d/tan(e + x*f)
                        yield 44, subst1
                if pattern_index == 45:
                    pass
                    # State 80996
                    if len(subjects) == 0:
                        pass
                        # 45: d*tan(e + x*f)
                        yield 45, subst1
                if pattern_index == 46:
                    pass
                    # State 92269
                    if len(subjects) == 0:
                        pass
                        # 46: d/cos(e + x*f)
                        yield 46, subst1
                if pattern_index == 47:
                    pass
                    # State 92335
                    if len(subjects) == 0:
                        pass
                        # 47: d/sin(e + x*f)
                        yield 47, subst1
                if pattern_index == 48:
                    pass
                    # State 93217
                    if len(subjects) == 0:
                        pass
                        # 48: d/cos(e + x*f)
                        yield 48, subst1
                if pattern_index == 49:
                    pass
                    # State 93403
                    if len(subjects) == 0:
                        pass
                        # 49: d/sin(e + x*f)
                        yield 49, subst1
                if pattern_index == 50:
                    pass
                    # State 109044
                    if len(subjects) == 0:
                        pass
                        # 50: b*asin(x*c)
                        yield 50, subst1
                if pattern_index == 51:
                    pass
                    # State 109113
                    if len(subjects) == 0:
                        pass
                        # 51: b*acos(x*c)
                        yield 51, subst1
                if pattern_index == 52:
                    pass
                    # State 109608
                    if len(subjects) == 0:
                        pass
                        # 52: g*x
                        yield 52, subst1
                if pattern_index == 53:
                    pass
                    # State 110654
                    if len(subjects) == 0:
                        pass
                        # 53: C*x**2
                        yield 53, subst1
                if pattern_index == 54:
                    pass
                    # State 110656
                    if len(subjects) == 0:
                        pass
                        # 54: B*x
                        yield 54, subst1
                if pattern_index == 55:
                    pass
                    # State 138803
                    if len(subjects) == 0:
                        pass
                        # 55: b*acosh(x*c)
                        yield 55, subst1
                if pattern_index == 56:
                    pass
                    # State 138872
                    if len(subjects) == 0:
                        pass
                        # 56: b*asinh(x*c)
                        yield 56, subst1
                if pattern_index == 57:
                    pass
                    # State 139439
                    if len(subjects) == 0:
                        pass
                        # 57: g*x
                        yield 57, subst1
                if pattern_index == 58:
                    pass
                    # State 151681
                    if len(subjects) == 0:
                        pass
                        # 58: y*b
                        yield 58, subst1
            subjects.appendleft(tmp375)
        return
        yield


from .generated_part003750 import *
from .generated_part003756 import *
from .generated_part003742 import *
from .generated_part003754 import *
from .generated_part003741 import *
from .generated_part003761 import *
from .generated_part003762 import *
from .generated_part003769 import *
from .generated_part003752 import *
from .generated_part003744 import *
from .generated_part003777 import *
from .generated_part003746 import *
from .generated_part003767 import *
from collections import deque
from .generated_part003753 import *
from .generated_part003768 import *
from .generated_part003758 import *
from matchpy.utils import VariableWithCount
from .generated_part003774 import *
from .generated_part003748 import *
from .generated_part003766 import *
from .generated_part003760 import *
from .generated_part003775 import *
from .generated_part003757 import *
from .generated_part003740 import *
from multiset import Multiset
from .generated_part003778 import *
from .generated_part003749 import *
from .generated_part003764 import *
from .generated_part003765 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part003771 import *
from .generated_part003745 import *
from .generated_part003780 import *
from .generated_part003772 import *