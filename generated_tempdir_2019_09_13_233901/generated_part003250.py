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

class CommutativeMatcher3316(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    3: (3, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.1.0', 1, 1, None), Mul)
]),
    5: (5, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.2.2.1.0', 1, 1, None), Mul)
]),
    6: (6, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({13: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({14: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({15: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({16: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({17: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({18: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({19: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({20: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({21: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    27: (27, Multiset({22: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({23: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({24: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({25: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    31: (31, Multiset({26: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({27: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    33: (33, Multiset({28: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({29: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
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
    41: (41, Multiset({36: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher3316._instance is None:
            CommutativeMatcher3316._instance = CommutativeMatcher3316()
        return CommutativeMatcher3316._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3315
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 10748
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10749
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp4 = subjects2.popleft()
                    subjects5 = deque(tmp4._args)
                    # State 10750
                    if len(subjects5) >= 1:
                        tmp6 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.0', tmp6)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10751
                            if len(subjects5) >= 1 and subjects5[0] == -1:
                                tmp8 = subjects5.popleft()
                                # State 10752
                                if len(subjects5) == 0:
                                    pass
                                    # State 10753
                                    if len(subjects2) >= 1:
                                        tmp9 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', tmp9)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 10754
                                            if len(subjects2) == 0:
                                                pass
                                                # State 10755
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (c/x)**n
                                        subjects2.appendleft(tmp9)
                                subjects5.appendleft(tmp8)
                        subjects5.appendleft(tmp6)
                    subjects2.appendleft(tmp4)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp11 = subjects2.popleft()
                associative1 = tmp11
                associative_type1 = type(tmp11)
                subjects12 = deque(tmp11._args)
                matcher = CommutativeMatcher10757.get()
                tmp13 = subjects12
                subjects12 = []
                for s in tmp13:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp13, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10762
                        if len(subjects2) >= 1:
                            tmp14 = []
                            tmp14.append(subjects2.popleft())
                            while True:
                                if len(tmp14) > 1:
                                    tmp15 = create_operation_expression(associative1, tmp14)
                                elif len(tmp14) == 1:
                                    tmp15 = tmp14[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp15)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10763
                                    if len(subjects2) == 0:
                                        pass
                                        # State 10764
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (c/x)**n
                                if len(subjects2) == 0:
                                    break
                                tmp14.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp14))
                subjects2.appendleft(tmp11)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp17 = subjects2.popleft()
                subjects18 = deque(tmp17._args)
                # State 88723
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 88724
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88725
                        if len(subjects18) >= 1 and isinstance(subjects18[0], Pow):
                            tmp21 = subjects18.popleft()
                            subjects22 = deque(tmp21._args)
                            # State 88726
                            if len(subjects22) >= 1:
                                tmp23 = subjects22.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp23)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 88727
                                    if len(subjects22) >= 1:
                                        tmp25 = subjects22.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp25)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 88728
                                            if len(subjects22) == 0:
                                                pass
                                                # State 88729
                                                if len(subjects18) == 0:
                                                    pass
                                                    # State 88730
                                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                                        tmp27 = subjects2.popleft()
                                                        # State 88731
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 88732
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 10: 1/tan(x**n*d + c)
                                                        subjects2.appendleft(tmp27)
                                        subjects22.appendleft(tmp25)
                                subjects22.appendleft(tmp23)
                            subjects18.appendleft(tmp21)
                    if len(subjects18) >= 1 and isinstance(subjects18[0], Mul):
                        tmp28 = subjects18.popleft()
                        associative1 = tmp28
                        associative_type1 = type(tmp28)
                        subjects29 = deque(tmp28._args)
                        matcher = CommutativeMatcher88734.get()
                        tmp30 = subjects29
                        subjects29 = []
                        for s in tmp30:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp30, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 88739
                                if len(subjects18) == 0:
                                    pass
                                    # State 88740
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp31 = subjects2.popleft()
                                        # State 88741
                                        if len(subjects2) == 0:
                                            pass
                                            # State 88742
                                            if len(subjects) == 0:
                                                pass
                                                # 10: 1/tan(x**n*d + c)
                                        subjects2.appendleft(tmp31)
                        subjects18.appendleft(tmp28)
                if len(subjects18) >= 1:
                    tmp32 = subjects18.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp32)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88997
                        if len(subjects18) == 0:
                            pass
                            # State 88998
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp34 = subjects2.popleft()
                                # State 88999
                                if len(subjects2) == 0:
                                    pass
                                    # State 89000
                                    if len(subjects) == 0:
                                        pass
                                        # 12: 1/tan(v)
                                subjects2.appendleft(tmp34)
                    subjects18.appendleft(tmp32)
                if len(subjects18) >= 1 and isinstance(subjects18[0], Add):
                    tmp35 = subjects18.popleft()
                    associative1 = tmp35
                    associative_type1 = type(tmp35)
                    subjects36 = deque(tmp35._args)
                    matcher = CommutativeMatcher88744.get()
                    tmp37 = subjects36
                    subjects36 = []
                    for s in tmp37:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp37, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 88757
                            if len(subjects18) == 0:
                                pass
                                # State 88758
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp38 = subjects2.popleft()
                                    # State 88759
                                    if len(subjects2) == 0:
                                        pass
                                        # State 88760
                                        if len(subjects) == 0:
                                            pass
                                            # 10: 1/tan(x**n*d + c)
                                    subjects2.appendleft(tmp38)
                    subjects18.appendleft(tmp35)
                subjects2.appendleft(tmp17)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp39 = subjects2.popleft()
                subjects40 = deque(tmp39._args)
                # State 98892
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 98893
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98894
                        if len(subjects40) >= 1 and isinstance(subjects40[0], Pow):
                            tmp43 = subjects40.popleft()
                            subjects44 = deque(tmp43._args)
                            # State 98895
                            if len(subjects44) >= 1:
                                tmp45 = subjects44.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp45)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 98896
                                    if len(subjects44) >= 1:
                                        tmp47 = subjects44.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp47)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 98897
                                            if len(subjects44) == 0:
                                                pass
                                                # State 98898
                                                if len(subjects40) == 0:
                                                    pass
                                                    # State 98899
                                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                                        tmp49 = subjects2.popleft()
                                                        # State 98900
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 98901
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 13: 1/cos(x**n*d + c)
                                                        subjects2.appendleft(tmp49)
                                        subjects44.appendleft(tmp47)
                                subjects44.appendleft(tmp45)
                            subjects40.appendleft(tmp43)
                    if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                        tmp50 = subjects40.popleft()
                        associative1 = tmp50
                        associative_type1 = type(tmp50)
                        subjects51 = deque(tmp50._args)
                        matcher = CommutativeMatcher98903.get()
                        tmp52 = subjects51
                        subjects51 = []
                        for s in tmp52:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp52, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 98908
                                if len(subjects40) == 0:
                                    pass
                                    # State 98909
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp53 = subjects2.popleft()
                                        # State 98910
                                        if len(subjects2) == 0:
                                            pass
                                            # State 98911
                                            if len(subjects) == 0:
                                                pass
                                                # 13: 1/cos(x**n*d + c)
                                        subjects2.appendleft(tmp53)
                        subjects40.appendleft(tmp50)
                if len(subjects40) >= 1:
                    tmp54 = subjects40.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp54)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99412
                        if len(subjects40) == 0:
                            pass
                            # State 99413
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp56 = subjects2.popleft()
                                # State 99414
                                if len(subjects2) == 0:
                                    pass
                                    # State 99415
                                    if len(subjects) == 0:
                                        pass
                                        # 15: 1/cos(v)
                                subjects2.appendleft(tmp56)
                    subjects40.appendleft(tmp54)
                if len(subjects40) >= 1 and isinstance(subjects40[0], Add):
                    tmp57 = subjects40.popleft()
                    associative1 = tmp57
                    associative_type1 = type(tmp57)
                    subjects58 = deque(tmp57._args)
                    matcher = CommutativeMatcher98913.get()
                    tmp59 = subjects58
                    subjects58 = []
                    for s in tmp59:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp59, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 98926
                            if len(subjects40) == 0:
                                pass
                                # State 98927
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp60 = subjects2.popleft()
                                    # State 98928
                                    if len(subjects2) == 0:
                                        pass
                                        # State 98929
                                        if len(subjects) == 0:
                                            pass
                                            # 13: 1/cos(x**n*d + c)
                                    subjects2.appendleft(tmp60)
                    subjects40.appendleft(tmp57)
                subjects2.appendleft(tmp39)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp61 = subjects2.popleft()
                subjects62 = deque(tmp61._args)
                # State 99169
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 99170
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99171
                        if len(subjects62) >= 1 and isinstance(subjects62[0], Pow):
                            tmp65 = subjects62.popleft()
                            subjects66 = deque(tmp65._args)
                            # State 99172
                            if len(subjects66) >= 1:
                                tmp67 = subjects66.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp67)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 99173
                                    if len(subjects66) >= 1:
                                        tmp69 = subjects66.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp69)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99174
                                            if len(subjects66) == 0:
                                                pass
                                                # State 99175
                                                if len(subjects62) == 0:
                                                    pass
                                                    # State 99176
                                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                                        tmp71 = subjects2.popleft()
                                                        # State 99177
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 99178
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 14: 1/sin(x**n*d + c)
                                                        subjects2.appendleft(tmp71)
                                        subjects66.appendleft(tmp69)
                                subjects66.appendleft(tmp67)
                            subjects62.appendleft(tmp65)
                    if len(subjects62) >= 1 and isinstance(subjects62[0], Mul):
                        tmp72 = subjects62.popleft()
                        associative1 = tmp72
                        associative_type1 = type(tmp72)
                        subjects73 = deque(tmp72._args)
                        matcher = CommutativeMatcher99180.get()
                        tmp74 = subjects73
                        subjects73 = []
                        for s in tmp74:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp74, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 99185
                                if len(subjects62) == 0:
                                    pass
                                    # State 99186
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp75 = subjects2.popleft()
                                        # State 99187
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99188
                                            if len(subjects) == 0:
                                                pass
                                                # 14: 1/sin(x**n*d + c)
                                        subjects2.appendleft(tmp75)
                        subjects62.appendleft(tmp72)
                if len(subjects62) >= 1:
                    tmp76 = subjects62.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp76)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99450
                        if len(subjects62) == 0:
                            pass
                            # State 99451
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp78 = subjects2.popleft()
                                # State 99452
                                if len(subjects2) == 0:
                                    pass
                                    # State 99453
                                    if len(subjects) == 0:
                                        pass
                                        # 16: 1/sin(v)
                                subjects2.appendleft(tmp78)
                    subjects62.appendleft(tmp76)
                if len(subjects62) >= 1 and isinstance(subjects62[0], Add):
                    tmp79 = subjects62.popleft()
                    associative1 = tmp79
                    associative_type1 = type(tmp79)
                    subjects80 = deque(tmp79._args)
                    matcher = CommutativeMatcher99190.get()
                    tmp81 = subjects80
                    subjects80 = []
                    for s in tmp81:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp81, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 99203
                            if len(subjects62) == 0:
                                pass
                                # State 99204
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp82 = subjects2.popleft()
                                    # State 99205
                                    if len(subjects2) == 0:
                                        pass
                                        # State 99206
                                        if len(subjects) == 0:
                                            pass
                                            # 14: 1/sin(x**n*d + c)
                                    subjects2.appendleft(tmp82)
                    subjects62.appendleft(tmp79)
                subjects2.appendleft(tmp61)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tanh):
                tmp83 = subjects2.popleft()
                subjects84 = deque(tmp83._args)
                # State 128261
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 128262
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128263
                        if len(subjects84) >= 1 and isinstance(subjects84[0], Pow):
                            tmp87 = subjects84.popleft()
                            subjects88 = deque(tmp87._args)
                            # State 128264
                            if len(subjects88) >= 1:
                                tmp89 = subjects88.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp89)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 128265
                                    if len(subjects88) >= 1:
                                        tmp91 = subjects88.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp91)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 128266
                                            if len(subjects88) == 0:
                                                pass
                                                # State 128267
                                                if len(subjects84) == 0:
                                                    pass
                                                    # State 128268
                                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                                        tmp93 = subjects2.popleft()
                                                        # State 128269
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 128270
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: 1/tanh(x**n*d + c)
                                                        subjects2.appendleft(tmp93)
                                        subjects88.appendleft(tmp91)
                                subjects88.appendleft(tmp89)
                            subjects84.appendleft(tmp87)
                    if len(subjects84) >= 1 and isinstance(subjects84[0], Mul):
                        tmp94 = subjects84.popleft()
                        associative1 = tmp94
                        associative_type1 = type(tmp94)
                        subjects95 = deque(tmp94._args)
                        matcher = CommutativeMatcher128272.get()
                        tmp96 = subjects95
                        subjects95 = []
                        for s in tmp96:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp96, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 128277
                                if len(subjects84) == 0:
                                    pass
                                    # State 128278
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp97 = subjects2.popleft()
                                        # State 128279
                                        if len(subjects2) == 0:
                                            pass
                                            # State 128280
                                            if len(subjects) == 0:
                                                pass
                                                # 28: 1/tanh(x**n*d + c)
                                        subjects2.appendleft(tmp97)
                        subjects84.appendleft(tmp94)
                if len(subjects84) >= 1:
                    tmp98 = subjects84.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp98)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128548
                        if len(subjects84) == 0:
                            pass
                            # State 128549
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp100 = subjects2.popleft()
                                # State 128550
                                if len(subjects2) == 0:
                                    pass
                                    # State 128551
                                    if len(subjects) == 0:
                                        pass
                                        # 30: 1/tanh(v)
                                subjects2.appendleft(tmp100)
                    subjects84.appendleft(tmp98)
                if len(subjects84) >= 1 and isinstance(subjects84[0], Add):
                    tmp101 = subjects84.popleft()
                    associative1 = tmp101
                    associative_type1 = type(tmp101)
                    subjects102 = deque(tmp101._args)
                    matcher = CommutativeMatcher128282.get()
                    tmp103 = subjects102
                    subjects102 = []
                    for s in tmp103:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp103, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 128295
                            if len(subjects84) == 0:
                                pass
                                # State 128296
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp104 = subjects2.popleft()
                                    # State 128297
                                    if len(subjects2) == 0:
                                        pass
                                        # State 128298
                                        if len(subjects) == 0:
                                            pass
                                            # 28: 1/tanh(x**n*d + c)
                                    subjects2.appendleft(tmp104)
                    subjects84.appendleft(tmp101)
                subjects2.appendleft(tmp83)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cosh):
                tmp105 = subjects2.popleft()
                subjects106 = deque(tmp105._args)
                # State 131205
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 131206
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131207
                        if len(subjects106) >= 1 and isinstance(subjects106[0], Pow):
                            tmp109 = subjects106.popleft()
                            subjects110 = deque(tmp109._args)
                            # State 131208
                            if len(subjects110) >= 1:
                                tmp111 = subjects110.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp111)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 131209
                                    if len(subjects110) >= 1:
                                        tmp113 = subjects110.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp113)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 131210
                                            if len(subjects110) == 0:
                                                pass
                                                # State 131211
                                                if len(subjects106) == 0:
                                                    pass
                                                    # State 131212
                                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                                        tmp115 = subjects2.popleft()
                                                        # State 131213
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 131214
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 31: 1/cosh(x**n*d + c)
                                                        subjects2.appendleft(tmp115)
                                        subjects110.appendleft(tmp113)
                                subjects110.appendleft(tmp111)
                            subjects106.appendleft(tmp109)
                    if len(subjects106) >= 1 and isinstance(subjects106[0], Mul):
                        tmp116 = subjects106.popleft()
                        associative1 = tmp116
                        associative_type1 = type(tmp116)
                        subjects117 = deque(tmp116._args)
                        matcher = CommutativeMatcher131216.get()
                        tmp118 = subjects117
                        subjects117 = []
                        for s in tmp118:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp118, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 131221
                                if len(subjects106) == 0:
                                    pass
                                    # State 131222
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp119 = subjects2.popleft()
                                        # State 131223
                                        if len(subjects2) == 0:
                                            pass
                                            # State 131224
                                            if len(subjects) == 0:
                                                pass
                                                # 31: 1/cosh(x**n*d + c)
                                        subjects2.appendleft(tmp119)
                        subjects106.appendleft(tmp116)
                if len(subjects106) >= 1:
                    tmp120 = subjects106.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp120)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131761
                        if len(subjects106) == 0:
                            pass
                            # State 131762
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp122 = subjects2.popleft()
                                # State 131763
                                if len(subjects2) == 0:
                                    pass
                                    # State 131764
                                    if len(subjects) == 0:
                                        pass
                                        # 33: 1/cosh(u)
                                subjects2.appendleft(tmp122)
                    subjects106.appendleft(tmp120)
                if len(subjects106) >= 1 and isinstance(subjects106[0], Add):
                    tmp123 = subjects106.popleft()
                    associative1 = tmp123
                    associative_type1 = type(tmp123)
                    subjects124 = deque(tmp123._args)
                    matcher = CommutativeMatcher131226.get()
                    tmp125 = subjects124
                    subjects124 = []
                    for s in tmp125:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp125, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 131239
                            if len(subjects106) == 0:
                                pass
                                # State 131240
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp126 = subjects2.popleft()
                                    # State 131241
                                    if len(subjects2) == 0:
                                        pass
                                        # State 131242
                                        if len(subjects) == 0:
                                            pass
                                            # 31: 1/cosh(x**n*d + c)
                                    subjects2.appendleft(tmp126)
                    subjects106.appendleft(tmp123)
                subjects2.appendleft(tmp105)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sinh):
                tmp127 = subjects2.popleft()
                subjects128 = deque(tmp127._args)
                # State 131500
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 131501
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131502
                        if len(subjects128) >= 1 and isinstance(subjects128[0], Pow):
                            tmp131 = subjects128.popleft()
                            subjects132 = deque(tmp131._args)
                            # State 131503
                            if len(subjects132) >= 1:
                                tmp133 = subjects132.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp133)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 131504
                                    if len(subjects132) >= 1:
                                        tmp135 = subjects132.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp135)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 131505
                                            if len(subjects132) == 0:
                                                pass
                                                # State 131506
                                                if len(subjects128) == 0:
                                                    pass
                                                    # State 131507
                                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                                        tmp137 = subjects2.popleft()
                                                        # State 131508
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 131509
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 32: 1/sinh(x**n*d + c)
                                                        subjects2.appendleft(tmp137)
                                        subjects132.appendleft(tmp135)
                                subjects132.appendleft(tmp133)
                            subjects128.appendleft(tmp131)
                    if len(subjects128) >= 1 and isinstance(subjects128[0], Mul):
                        tmp138 = subjects128.popleft()
                        associative1 = tmp138
                        associative_type1 = type(tmp138)
                        subjects139 = deque(tmp138._args)
                        matcher = CommutativeMatcher131511.get()
                        tmp140 = subjects139
                        subjects139 = []
                        for s in tmp140:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp140, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 131516
                                if len(subjects128) == 0:
                                    pass
                                    # State 131517
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp141 = subjects2.popleft()
                                        # State 131518
                                        if len(subjects2) == 0:
                                            pass
                                            # State 131519
                                            if len(subjects) == 0:
                                                pass
                                                # 32: 1/sinh(x**n*d + c)
                                        subjects2.appendleft(tmp141)
                        subjects128.appendleft(tmp138)
                if len(subjects128) >= 1:
                    tmp142 = subjects128.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp142)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131808
                        if len(subjects128) == 0:
                            pass
                            # State 131809
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp144 = subjects2.popleft()
                                # State 131810
                                if len(subjects2) == 0:
                                    pass
                                    # State 131811
                                    if len(subjects) == 0:
                                        pass
                                        # 34: 1/sinh(u)
                                subjects2.appendleft(tmp144)
                    subjects128.appendleft(tmp142)
                if len(subjects128) >= 1 and isinstance(subjects128[0], Add):
                    tmp145 = subjects128.popleft()
                    associative1 = tmp145
                    associative_type1 = type(tmp145)
                    subjects146 = deque(tmp145._args)
                    matcher = CommutativeMatcher131521.get()
                    tmp147 = subjects146
                    subjects146 = []
                    for s in tmp147:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp147, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 131534
                            if len(subjects128) == 0:
                                pass
                                # State 131535
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp148 = subjects2.popleft()
                                    # State 131536
                                    if len(subjects2) == 0:
                                        pass
                                        # State 131537
                                        if len(subjects) == 0:
                                            pass
                                            # 32: 1/sinh(x**n*d + c)
                                    subjects2.appendleft(tmp148)
                    subjects128.appendleft(tmp145)
                subjects2.appendleft(tmp127)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp149 = subjects.popleft()
            subjects150 = deque(tmp149._args)
            # State 74087
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 74088
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 74089
                    if len(subjects150) >= 1 and isinstance(subjects150[0], Pow):
                        tmp153 = subjects150.popleft()
                        subjects154 = deque(tmp153._args)
                        # State 74090
                        if len(subjects154) >= 1:
                            tmp155 = subjects154.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp155)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74091
                                if len(subjects154) >= 1:
                                    tmp157 = subjects154.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp157)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 74092
                                        if len(subjects154) == 0:
                                            pass
                                            # State 74093
                                            if len(subjects150) == 0:
                                                pass
                                                # State 74094
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: sin(x**n*d + c)
                                    subjects154.appendleft(tmp157)
                            subjects154.appendleft(tmp155)
                        if len(subjects154) >= 1:
                            tmp159 = subjects154.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp159)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74711
                                if len(subjects154) >= 1:
                                    tmp161 = subjects154.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp161)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 74712
                                        if len(subjects154) == 0:
                                            pass
                                            # State 74713
                                            if len(subjects150) == 0:
                                                pass
                                                # State 74714
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: sin(x**n*d + c)
                                    subjects154.appendleft(tmp161)
                            subjects154.appendleft(tmp159)
                        if len(subjects154) >= 1:
                            tmp163 = subjects154.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp163)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75135
                                if len(subjects154) >= 1:
                                    tmp165 = subjects154.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp165)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 75136
                                        if len(subjects154) == 0:
                                            pass
                                            # State 75137
                                            if len(subjects150) == 0:
                                                pass
                                                # State 75138
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: sin(c + d*x**n)
                                    subjects154.appendleft(tmp165)
                            subjects154.appendleft(tmp163)
                        subjects150.appendleft(tmp153)
                if len(subjects150) >= 1 and isinstance(subjects150[0], Mul):
                    tmp167 = subjects150.popleft()
                    associative1 = tmp167
                    associative_type1 = type(tmp167)
                    subjects168 = deque(tmp167._args)
                    matcher = CommutativeMatcher74096.get()
                    tmp169 = subjects168
                    subjects168 = []
                    for s in tmp169:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp169, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 74101
                            if len(subjects150) == 0:
                                pass
                                # State 74102
                                if len(subjects) == 0:
                                    pass
                                    # 1: sin(x**n*d + c)
                        if pattern_index == 1:
                            pass
                            # State 74718
                            if len(subjects150) == 0:
                                pass
                                # State 74719
                                if len(subjects) == 0:
                                    pass
                                    # 3: sin(x**n*d + c)
                        if pattern_index == 2:
                            pass
                            # State 75142
                            if len(subjects150) == 0:
                                pass
                                # State 75143
                                if len(subjects) == 0:
                                    pass
                                    # 5: sin(c + d*x**n)
                    subjects150.appendleft(tmp167)
            if len(subjects150) >= 1:
                tmp170 = subjects150.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp170)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75371
                    if len(subjects150) == 0:
                        pass
                        # State 75372
                        if len(subjects) == 0:
                            pass
                            # 7: sin(v)
                subjects150.appendleft(tmp170)
            if len(subjects150) >= 1 and isinstance(subjects150[0], Add):
                tmp172 = subjects150.popleft()
                associative1 = tmp172
                associative_type1 = type(tmp172)
                subjects173 = deque(tmp172._args)
                matcher = CommutativeMatcher74104.get()
                tmp174 = subjects173
                subjects173 = []
                for s in tmp174:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp174, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 74117
                        if len(subjects150) == 0:
                            pass
                            # State 74118
                            if len(subjects) == 0:
                                pass
                                # 1: sin(x**n*d + c)
                    if pattern_index == 1:
                        pass
                        # State 74727
                        if len(subjects150) == 0:
                            pass
                            # State 74728
                            if len(subjects) == 0:
                                pass
                                # 3: sin(x**n*d + c)
                    if pattern_index == 2:
                        pass
                        # State 75151
                        if len(subjects150) == 0:
                            pass
                            # State 75152
                            if len(subjects) == 0:
                                pass
                                # 5: sin(c + d*x**n)
                subjects150.appendleft(tmp172)
            subjects.appendleft(tmp149)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp175 = subjects.popleft()
            subjects176 = deque(tmp175._args)
            # State 74314
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 74315
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 74316
                    if len(subjects176) >= 1 and isinstance(subjects176[0], Pow):
                        tmp179 = subjects176.popleft()
                        subjects180 = deque(tmp179._args)
                        # State 74317
                        if len(subjects180) >= 1:
                            tmp181 = subjects180.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp181)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74318
                                if len(subjects180) >= 1:
                                    tmp183 = subjects180.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp183)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 74319
                                        if len(subjects180) == 0:
                                            pass
                                            # State 74320
                                            if len(subjects176) == 0:
                                                pass
                                                # State 74321
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: cos(x**n*d + c)
                                    subjects180.appendleft(tmp183)
                            subjects180.appendleft(tmp181)
                        if len(subjects180) >= 1:
                            tmp185 = subjects180.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp185)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74874
                                if len(subjects180) >= 1:
                                    tmp187 = subjects180.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp187)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 74875
                                        if len(subjects180) == 0:
                                            pass
                                            # State 74876
                                            if len(subjects176) == 0:
                                                pass
                                                # State 74877
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: cos(x**n*d + c)
                                    subjects180.appendleft(tmp187)
                            subjects180.appendleft(tmp185)
                        if len(subjects180) >= 1:
                            tmp189 = subjects180.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp189)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75261
                                if len(subjects180) >= 1:
                                    tmp191 = subjects180.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp191)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 75262
                                        if len(subjects180) == 0:
                                            pass
                                            # State 75263
                                            if len(subjects176) == 0:
                                                pass
                                                # State 75264
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: cos(c + d*x**n)
                                    subjects180.appendleft(tmp191)
                            subjects180.appendleft(tmp189)
                        subjects176.appendleft(tmp179)
                if len(subjects176) >= 1 and isinstance(subjects176[0], Mul):
                    tmp193 = subjects176.popleft()
                    associative1 = tmp193
                    associative_type1 = type(tmp193)
                    subjects194 = deque(tmp193._args)
                    matcher = CommutativeMatcher74323.get()
                    tmp195 = subjects194
                    subjects194 = []
                    for s in tmp195:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp195, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 74328
                            if len(subjects176) == 0:
                                pass
                                # State 74329
                                if len(subjects) == 0:
                                    pass
                                    # 2: cos(x**n*d + c)
                        if pattern_index == 1:
                            pass
                            # State 74881
                            if len(subjects176) == 0:
                                pass
                                # State 74882
                                if len(subjects) == 0:
                                    pass
                                    # 4: cos(x**n*d + c)
                        if pattern_index == 2:
                            pass
                            # State 75268
                            if len(subjects176) == 0:
                                pass
                                # State 75269
                                if len(subjects) == 0:
                                    pass
                                    # 6: cos(c + d*x**n)
                    subjects176.appendleft(tmp193)
            if len(subjects176) >= 1:
                tmp196 = subjects176.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp196)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75397
                    if len(subjects176) == 0:
                        pass
                        # State 75398
                        if len(subjects) == 0:
                            pass
                            # 8: cos(v)
                subjects176.appendleft(tmp196)
            if len(subjects176) >= 1 and isinstance(subjects176[0], Add):
                tmp198 = subjects176.popleft()
                associative1 = tmp198
                associative_type1 = type(tmp198)
                subjects199 = deque(tmp198._args)
                matcher = CommutativeMatcher74331.get()
                tmp200 = subjects199
                subjects199 = []
                for s in tmp200:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp200, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 74344
                        if len(subjects176) == 0:
                            pass
                            # State 74345
                            if len(subjects) == 0:
                                pass
                                # 2: cos(x**n*d + c)
                    if pattern_index == 1:
                        pass
                        # State 74890
                        if len(subjects176) == 0:
                            pass
                            # State 74891
                            if len(subjects) == 0:
                                pass
                                # 4: cos(x**n*d + c)
                    if pattern_index == 2:
                        pass
                        # State 75277
                        if len(subjects176) == 0:
                            pass
                            # State 75278
                            if len(subjects) == 0:
                                pass
                                # 6: cos(c + d*x**n)
                subjects176.appendleft(tmp198)
            subjects.appendleft(tmp175)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp201 = subjects.popleft()
            subjects202 = deque(tmp201._args)
            # State 88485
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 88486
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 88487
                    if len(subjects202) >= 1 and isinstance(subjects202[0], Pow):
                        tmp205 = subjects202.popleft()
                        subjects206 = deque(tmp205._args)
                        # State 88488
                        if len(subjects206) >= 1:
                            tmp207 = subjects206.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp207)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 88489
                                if len(subjects206) >= 1:
                                    tmp209 = subjects206.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp209)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 88490
                                        if len(subjects206) == 0:
                                            pass
                                            # State 88491
                                            if len(subjects202) == 0:
                                                pass
                                                # State 88492
                                                if len(subjects) == 0:
                                                    pass
                                                    # 9: tan(x**n*d + c)
                                    subjects206.appendleft(tmp209)
                            subjects206.appendleft(tmp207)
                        subjects202.appendleft(tmp205)
                if len(subjects202) >= 1 and isinstance(subjects202[0], Mul):
                    tmp211 = subjects202.popleft()
                    associative1 = tmp211
                    associative_type1 = type(tmp211)
                    subjects212 = deque(tmp211._args)
                    matcher = CommutativeMatcher88494.get()
                    tmp213 = subjects212
                    subjects212 = []
                    for s in tmp213:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp213, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 88499
                            if len(subjects202) == 0:
                                pass
                                # State 88500
                                if len(subjects) == 0:
                                    pass
                                    # 9: tan(x**n*d + c)
                    subjects202.appendleft(tmp211)
            if len(subjects202) >= 1:
                tmp214 = subjects202.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp214)
                except ValueError:
                    pass
                else:
                    pass
                    # State 88969
                    if len(subjects202) == 0:
                        pass
                        # State 88970
                        if len(subjects) == 0:
                            pass
                            # 11: tan(v)
                subjects202.appendleft(tmp214)
            if len(subjects202) >= 1 and isinstance(subjects202[0], Add):
                tmp216 = subjects202.popleft()
                associative1 = tmp216
                associative_type1 = type(tmp216)
                subjects217 = deque(tmp216._args)
                matcher = CommutativeMatcher88502.get()
                tmp218 = subjects217
                subjects217 = []
                for s in tmp218:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp218, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 88515
                        if len(subjects202) == 0:
                            pass
                            # State 88516
                            if len(subjects) == 0:
                                pass
                                # 9: tan(x**n*d + c)
                subjects202.appendleft(tmp216)
            subjects.appendleft(tmp201)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp219 = subjects.popleft()
            subjects220 = deque(tmp219._args)
            # State 108368
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108369
                if len(subjects220) >= 1:
                    tmp222 = subjects220.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp222)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108370
                        if len(subjects220) == 0:
                            pass
                            # State 108371
                            if len(subjects) == 0:
                                pass
                                # 17: asin(x*c)
                    subjects220.appendleft(tmp222)
            if len(subjects220) >= 1 and isinstance(subjects220[0], Mul):
                tmp224 = subjects220.popleft()
                associative1 = tmp224
                associative_type1 = type(tmp224)
                subjects225 = deque(tmp224._args)
                matcher = CommutativeMatcher108373.get()
                tmp226 = subjects225
                subjects225 = []
                for s in tmp226:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp226, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108374
                        if len(subjects220) == 0:
                            pass
                            # State 108375
                            if len(subjects) == 0:
                                pass
                                # 17: asin(x*c)
                subjects220.appendleft(tmp224)
            subjects.appendleft(tmp219)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp227 = subjects.popleft()
            subjects228 = deque(tmp227._args)
            # State 108443
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108444
                if len(subjects228) >= 1:
                    tmp230 = subjects228.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp230)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108445
                        if len(subjects228) == 0:
                            pass
                            # State 108446
                            if len(subjects) == 0:
                                pass
                                # 18: acos(x*c)
                    subjects228.appendleft(tmp230)
            if len(subjects228) >= 1 and isinstance(subjects228[0], Mul):
                tmp232 = subjects228.popleft()
                associative1 = tmp232
                associative_type1 = type(tmp232)
                subjects233 = deque(tmp232._args)
                matcher = CommutativeMatcher108448.get()
                tmp234 = subjects233
                subjects233 = []
                for s in tmp234:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp234, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108449
                        if len(subjects228) == 0:
                            pass
                            # State 108450
                            if len(subjects) == 0:
                                pass
                                # 18: acos(x*c)
                subjects228.appendleft(tmp232)
            subjects.appendleft(tmp227)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp235 = subjects.popleft()
            subjects236 = deque(tmp235._args)
            # State 124005
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 124006
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 124007
                    if len(subjects236) >= 1 and isinstance(subjects236[0], Pow):
                        tmp239 = subjects236.popleft()
                        subjects240 = deque(tmp239._args)
                        # State 124008
                        if len(subjects240) >= 1:
                            tmp241 = subjects240.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp241)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124009
                                if len(subjects240) >= 1:
                                    tmp243 = subjects240.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp243)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 124010
                                        if len(subjects240) == 0:
                                            pass
                                            # State 124011
                                            if len(subjects236) == 0:
                                                pass
                                                # State 124012
                                                if len(subjects) == 0:
                                                    pass
                                                    # 19: sinh(x**n*d + c)
                                    subjects240.appendleft(tmp243)
                            subjects240.appendleft(tmp241)
                        if len(subjects240) >= 1:
                            tmp245 = subjects240.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp245)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124621
                                if len(subjects240) >= 1:
                                    tmp247 = subjects240.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp247)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 124622
                                        if len(subjects240) == 0:
                                            pass
                                            # State 124623
                                            if len(subjects236) == 0:
                                                pass
                                                # State 124624
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: sinh(x**n*d + c)
                                    subjects240.appendleft(tmp247)
                            subjects240.appendleft(tmp245)
                        if len(subjects240) >= 1:
                            tmp249 = subjects240.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp249)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125045
                                if len(subjects240) >= 1:
                                    tmp251 = subjects240.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp251)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 125046
                                        if len(subjects240) == 0:
                                            pass
                                            # State 125047
                                            if len(subjects236) == 0:
                                                pass
                                                # State 125048
                                                if len(subjects) == 0:
                                                    pass
                                                    # 23: sinh(c + d*x**n)
                                    subjects240.appendleft(tmp251)
                            subjects240.appendleft(tmp249)
                        subjects236.appendleft(tmp239)
                if len(subjects236) >= 1 and isinstance(subjects236[0], Mul):
                    tmp253 = subjects236.popleft()
                    associative1 = tmp253
                    associative_type1 = type(tmp253)
                    subjects254 = deque(tmp253._args)
                    matcher = CommutativeMatcher124014.get()
                    tmp255 = subjects254
                    subjects254 = []
                    for s in tmp255:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp255, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 124019
                            if len(subjects236) == 0:
                                pass
                                # State 124020
                                if len(subjects) == 0:
                                    pass
                                    # 19: sinh(x**n*d + c)
                        if pattern_index == 1:
                            pass
                            # State 124628
                            if len(subjects236) == 0:
                                pass
                                # State 124629
                                if len(subjects) == 0:
                                    pass
                                    # 21: sinh(x**n*d + c)
                        if pattern_index == 2:
                            pass
                            # State 125052
                            if len(subjects236) == 0:
                                pass
                                # State 125053
                                if len(subjects) == 0:
                                    pass
                                    # 23: sinh(c + d*x**n)
                    subjects236.appendleft(tmp253)
            if len(subjects236) >= 1:
                tmp256 = subjects236.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp256)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125281
                    if len(subjects236) == 0:
                        pass
                        # State 125282
                        if len(subjects) == 0:
                            pass
                            # 25: sinh(v)
                subjects236.appendleft(tmp256)
            if len(subjects236) >= 1 and isinstance(subjects236[0], Add):
                tmp258 = subjects236.popleft()
                associative1 = tmp258
                associative_type1 = type(tmp258)
                subjects259 = deque(tmp258._args)
                matcher = CommutativeMatcher124022.get()
                tmp260 = subjects259
                subjects259 = []
                for s in tmp260:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp260, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 124035
                        if len(subjects236) == 0:
                            pass
                            # State 124036
                            if len(subjects) == 0:
                                pass
                                # 19: sinh(x**n*d + c)
                    if pattern_index == 1:
                        pass
                        # State 124637
                        if len(subjects236) == 0:
                            pass
                            # State 124638
                            if len(subjects) == 0:
                                pass
                                # 21: sinh(x**n*d + c)
                    if pattern_index == 2:
                        pass
                        # State 125061
                        if len(subjects236) == 0:
                            pass
                            # State 125062
                            if len(subjects) == 0:
                                pass
                                # 23: sinh(c + d*x**n)
                subjects236.appendleft(tmp258)
            subjects.appendleft(tmp235)
        if len(subjects) >= 1 and isinstance(subjects[0], cosh):
            tmp261 = subjects.popleft()
            subjects262 = deque(tmp261._args)
            # State 124242
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 124243
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 124244
                    if len(subjects262) >= 1 and isinstance(subjects262[0], Pow):
                        tmp265 = subjects262.popleft()
                        subjects266 = deque(tmp265._args)
                        # State 124245
                        if len(subjects266) >= 1:
                            tmp267 = subjects266.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp267)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124246
                                if len(subjects266) >= 1:
                                    tmp269 = subjects266.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp269)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 124247
                                        if len(subjects266) == 0:
                                            pass
                                            # State 124248
                                            if len(subjects262) == 0:
                                                pass
                                                # State 124249
                                                if len(subjects) == 0:
                                                    pass
                                                    # 20: cosh(x**n*d + c)
                                    subjects266.appendleft(tmp269)
                            subjects266.appendleft(tmp267)
                        if len(subjects266) >= 1:
                            tmp271 = subjects266.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp271)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124784
                                if len(subjects266) >= 1:
                                    tmp273 = subjects266.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp273)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 124785
                                        if len(subjects266) == 0:
                                            pass
                                            # State 124786
                                            if len(subjects262) == 0:
                                                pass
                                                # State 124787
                                                if len(subjects) == 0:
                                                    pass
                                                    # 22: cosh(x**n*d + c)
                                    subjects266.appendleft(tmp273)
                            subjects266.appendleft(tmp271)
                        if len(subjects266) >= 1:
                            tmp275 = subjects266.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp275)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125171
                                if len(subjects266) >= 1:
                                    tmp277 = subjects266.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp277)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 125172
                                        if len(subjects266) == 0:
                                            pass
                                            # State 125173
                                            if len(subjects262) == 0:
                                                pass
                                                # State 125174
                                                if len(subjects) == 0:
                                                    pass
                                                    # 24: cosh(c + d*x**n)
                                    subjects266.appendleft(tmp277)
                            subjects266.appendleft(tmp275)
                        subjects262.appendleft(tmp265)
                if len(subjects262) >= 1 and isinstance(subjects262[0], Mul):
                    tmp279 = subjects262.popleft()
                    associative1 = tmp279
                    associative_type1 = type(tmp279)
                    subjects280 = deque(tmp279._args)
                    matcher = CommutativeMatcher124251.get()
                    tmp281 = subjects280
                    subjects280 = []
                    for s in tmp281:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp281, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 124256
                            if len(subjects262) == 0:
                                pass
                                # State 124257
                                if len(subjects) == 0:
                                    pass
                                    # 20: cosh(x**n*d + c)
                        if pattern_index == 1:
                            pass
                            # State 124791
                            if len(subjects262) == 0:
                                pass
                                # State 124792
                                if len(subjects) == 0:
                                    pass
                                    # 22: cosh(x**n*d + c)
                        if pattern_index == 2:
                            pass
                            # State 125178
                            if len(subjects262) == 0:
                                pass
                                # State 125179
                                if len(subjects) == 0:
                                    pass
                                    # 24: cosh(c + d*x**n)
                    subjects262.appendleft(tmp279)
            if len(subjects262) >= 1:
                tmp282 = subjects262.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp282)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125307
                    if len(subjects262) == 0:
                        pass
                        # State 125308
                        if len(subjects) == 0:
                            pass
                            # 26: cosh(v)
                subjects262.appendleft(tmp282)
            if len(subjects262) >= 1 and isinstance(subjects262[0], Add):
                tmp284 = subjects262.popleft()
                associative1 = tmp284
                associative_type1 = type(tmp284)
                subjects285 = deque(tmp284._args)
                matcher = CommutativeMatcher124259.get()
                tmp286 = subjects285
                subjects285 = []
                for s in tmp286:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp286, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 124272
                        if len(subjects262) == 0:
                            pass
                            # State 124273
                            if len(subjects) == 0:
                                pass
                                # 20: cosh(x**n*d + c)
                    if pattern_index == 1:
                        pass
                        # State 124800
                        if len(subjects262) == 0:
                            pass
                            # State 124801
                            if len(subjects) == 0:
                                pass
                                # 22: cosh(x**n*d + c)
                    if pattern_index == 2:
                        pass
                        # State 125187
                        if len(subjects262) == 0:
                            pass
                            # State 125188
                            if len(subjects) == 0:
                                pass
                                # 24: cosh(c + d*x**n)
                subjects262.appendleft(tmp284)
            subjects.appendleft(tmp261)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp287 = subjects.popleft()
            subjects288 = deque(tmp287._args)
            # State 128018
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 128019
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 128020
                    if len(subjects288) >= 1 and isinstance(subjects288[0], Pow):
                        tmp291 = subjects288.popleft()
                        subjects292 = deque(tmp291._args)
                        # State 128021
                        if len(subjects292) >= 1:
                            tmp293 = subjects292.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp293)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 128022
                                if len(subjects292) >= 1:
                                    tmp295 = subjects292.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp295)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 128023
                                        if len(subjects292) == 0:
                                            pass
                                            # State 128024
                                            if len(subjects288) == 0:
                                                pass
                                                # State 128025
                                                if len(subjects) == 0:
                                                    pass
                                                    # 27: tanh(x**n*d + c)
                                    subjects292.appendleft(tmp295)
                            subjects292.appendleft(tmp293)
                        subjects288.appendleft(tmp291)
                if len(subjects288) >= 1 and isinstance(subjects288[0], Mul):
                    tmp297 = subjects288.popleft()
                    associative1 = tmp297
                    associative_type1 = type(tmp297)
                    subjects298 = deque(tmp297._args)
                    matcher = CommutativeMatcher128027.get()
                    tmp299 = subjects298
                    subjects298 = []
                    for s in tmp299:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp299, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 128032
                            if len(subjects288) == 0:
                                pass
                                # State 128033
                                if len(subjects) == 0:
                                    pass
                                    # 27: tanh(x**n*d + c)
                    subjects288.appendleft(tmp297)
            if len(subjects288) >= 1:
                tmp300 = subjects288.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp300)
                except ValueError:
                    pass
                else:
                    pass
                    # State 128520
                    if len(subjects288) == 0:
                        pass
                        # State 128521
                        if len(subjects) == 0:
                            pass
                            # 29: tanh(v)
                subjects288.appendleft(tmp300)
            if len(subjects288) >= 1 and isinstance(subjects288[0], Add):
                tmp302 = subjects288.popleft()
                associative1 = tmp302
                associative_type1 = type(tmp302)
                subjects303 = deque(tmp302._args)
                matcher = CommutativeMatcher128035.get()
                tmp304 = subjects303
                subjects303 = []
                for s in tmp304:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp304, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 128048
                        if len(subjects288) == 0:
                            pass
                            # State 128049
                            if len(subjects) == 0:
                                pass
                                # 27: tanh(x**n*d + c)
                subjects288.appendleft(tmp302)
            subjects.appendleft(tmp287)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp305 = subjects.popleft()
            subjects306 = deque(tmp305._args)
            # State 138104
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138105
                if len(subjects306) >= 1:
                    tmp308 = subjects306.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp308)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138106
                        if len(subjects306) == 0:
                            pass
                            # State 138107
                            if len(subjects) == 0:
                                pass
                                # 35: asinh(x*c)
                    subjects306.appendleft(tmp308)
            if len(subjects306) >= 1 and isinstance(subjects306[0], Mul):
                tmp310 = subjects306.popleft()
                associative1 = tmp310
                associative_type1 = type(tmp310)
                subjects311 = deque(tmp310._args)
                matcher = CommutativeMatcher138109.get()
                tmp312 = subjects311
                subjects311 = []
                for s in tmp312:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp312, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138110
                        if len(subjects306) == 0:
                            pass
                            # State 138111
                            if len(subjects) == 0:
                                pass
                                # 35: asinh(x*c)
                subjects306.appendleft(tmp310)
            subjects.appendleft(tmp305)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp313 = subjects.popleft()
            subjects314 = deque(tmp313._args)
            # State 138179
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138180
                if len(subjects314) >= 1:
                    tmp316 = subjects314.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp316)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138181
                        if len(subjects314) == 0:
                            pass
                            # State 138182
                            if len(subjects) == 0:
                                pass
                                # 36: acosh(x*c)
                    subjects314.appendleft(tmp316)
            if len(subjects314) >= 1 and isinstance(subjects314[0], Mul):
                tmp318 = subjects314.popleft()
                associative1 = tmp318
                associative_type1 = type(tmp318)
                subjects319 = deque(tmp318._args)
                matcher = CommutativeMatcher138184.get()
                tmp320 = subjects319
                subjects319 = []
                for s in tmp320:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp320, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138185
                        if len(subjects314) == 0:
                            pass
                            # State 138186
                            if len(subjects) == 0:
                                pass
                                # 36: acosh(x*c)
                subjects314.appendleft(tmp318)
            subjects.appendleft(tmp313)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
