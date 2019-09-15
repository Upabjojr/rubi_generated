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


class CommutativeMatcher3238(CommutativeMatcher):
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
    3: (3, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.3.1.1.0', 1, 1, None), Mul)
]),
    8: (8, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.1.0', 1, 1, None), Mul)
]),
    9: (9, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.2.2.1.0', 1, 1, None), Mul)
]),
    10: (10, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
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
    21: (21, Multiset({14: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({15: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({16: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({17: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({18: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({19: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    27: (27, Multiset({20: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({21: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({22: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({23: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    31: (31, Multiset({24: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({25: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    33: (33, Multiset({26: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Mul)
]),
    35: (35, Multiset({27: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    36: (36, Multiset({28: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    37: (37, Multiset({29: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    38: (38, Multiset({30: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({31: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({32: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    41: (41, Multiset({33: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    42: (42, Multiset({34: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    43: (43, Multiset({35: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    44: (44, Multiset({36: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    45: (45, Multiset({37: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    46: (46, Multiset({38: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    47: (47, Multiset({39: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    48: (48, Multiset({40: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    49: (49, Multiset({41: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    50: (50, Multiset({42: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    51: (51, Multiset({43: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    52: (52, Multiset({44: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    53: (53, Multiset({}), [
      (VariableWithCount('i2.2.1.0_4', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_5', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher3238._instance is None:
            CommutativeMatcher3238._instance = CommutativeMatcher3238()
        return CommutativeMatcher3238._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3237
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 7819
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1_2', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7820
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7821
                            if len(subjects2) == 0:
                                pass
                                # State 7822
                                if len(subjects) == 0:
                                    pass
                                    # 0: w**n
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp7 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 9453
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 9454
                            if len(subjects2) == 0:
                                pass
                                # State 9455
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                                    yield 1, subst2
                        subjects2.appendleft(tmp9)
                subjects2.appendleft(tmp7)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10820
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp12 = subjects2.popleft()
                    subjects13 = deque(tmp12._args)
                    # State 10821
                    if len(subjects13) >= 1:
                        tmp14 = subjects13.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.0', tmp14)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10822
                            if len(subjects13) >= 1 and subjects13[0] == Integer(-1):
                                tmp16 = subjects13.popleft()
                                # State 10823
                                if len(subjects13) == 0:
                                    pass
                                    # State 10824
                                    if len(subjects2) >= 1:
                                        tmp17 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2', tmp17)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 10825
                                            if len(subjects2) == 0:
                                                pass
                                                # State 10826
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: (c/x)**n
                                                    yield 2, subst3
                                        subjects2.appendleft(tmp17)
                                subjects13.appendleft(tmp16)
                        subjects13.appendleft(tmp14)
                    subjects2.appendleft(tmp12)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp19 = subjects2.popleft()
                associative1 = tmp19
                associative_type1 = type(tmp19)
                subjects20 = deque(tmp19._args)
                matcher = CommutativeMatcher10828.get()
                tmp21 = subjects20
                subjects20 = []
                for s in tmp21:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp21, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10833
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
                                    subst2.try_add_variable('i2.2.1.2', tmp23)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10834
                                    if len(subjects2) == 0:
                                        pass
                                        # State 10835
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (c/x)**n
                                            yield 2, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp22.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp22))
                subjects2.appendleft(tmp19)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp25 = subjects2.popleft()
                subjects26 = deque(tmp25._args)
                # State 88871
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 88872
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88873
                        if len(subjects26) >= 1 and isinstance(subjects26[0], Pow):
                            tmp29 = subjects26.popleft()
                            subjects30 = deque(tmp29._args)
                            # State 88874
                            if len(subjects30) >= 1:
                                tmp31 = subjects30.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp31)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 88875
                                    if len(subjects30) >= 1:
                                        tmp33 = subjects30.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp33)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 88876
                                            if len(subjects30) == 0:
                                                pass
                                                # State 88877
                                                if len(subjects26) == 0:
                                                    pass
                                                    # State 88878
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp35 = subjects2.popleft()
                                                        # State 88879
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 88880
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 16: 1/tan(x**n*d + c)
                                                                yield 16, subst4
                                                        subjects2.appendleft(tmp35)
                                        subjects30.appendleft(tmp33)
                                subjects30.appendleft(tmp31)
                            subjects26.appendleft(tmp29)
                    if len(subjects26) >= 1 and isinstance(subjects26[0], Mul):
                        tmp36 = subjects26.popleft()
                        associative1 = tmp36
                        associative_type1 = type(tmp36)
                        subjects37 = deque(tmp36._args)
                        matcher = CommutativeMatcher88882.get()
                        tmp38 = subjects37
                        subjects37 = []
                        for s in tmp38:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp38, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 88887
                                if len(subjects26) == 0:
                                    pass
                                    # State 88888
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp39 = subjects2.popleft()
                                        # State 88889
                                        if len(subjects2) == 0:
                                            pass
                                            # State 88890
                                            if len(subjects) == 0:
                                                pass
                                                # 16: 1/tan(x**n*d + c)
                                                yield 16, subst2
                                        subjects2.appendleft(tmp39)
                        subjects26.appendleft(tmp36)
                if len(subjects26) >= 1:
                    tmp40 = subjects26.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp40)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89018
                        if len(subjects26) == 0:
                            pass
                            # State 89019
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp42 = subjects2.popleft()
                                # State 89020
                                if len(subjects2) == 0:
                                    pass
                                    # State 89021
                                    if len(subjects) == 0:
                                        pass
                                        # 18: 1/tan(v)
                                        yield 18, subst1
                                subjects2.appendleft(tmp42)
                    subjects26.appendleft(tmp40)
                if len(subjects26) >= 1 and isinstance(subjects26[0], Add):
                    tmp43 = subjects26.popleft()
                    associative1 = tmp43
                    associative_type1 = type(tmp43)
                    subjects44 = deque(tmp43._args)
                    matcher = CommutativeMatcher88892.get()
                    tmp45 = subjects44
                    subjects44 = []
                    for s in tmp45:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp45, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 88905
                            if len(subjects26) == 0:
                                pass
                                # State 88906
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp46 = subjects2.popleft()
                                    # State 88907
                                    if len(subjects2) == 0:
                                        pass
                                        # State 88908
                                        if len(subjects) == 0:
                                            pass
                                            # 16: 1/tan(x**n*d + c)
                                            yield 16, subst1
                                    subjects2.appendleft(tmp46)
                    subjects26.appendleft(tmp43)
                subjects2.appendleft(tmp25)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp47 = subjects2.popleft()
                subjects48 = deque(tmp47._args)
                # State 92658
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 92659
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 92660
                        if len(subjects48) >= 1:
                            tmp51 = subjects48.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp51)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 92661
                                if len(subjects48) == 0:
                                    pass
                                    # State 92662
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp53 = subjects2.popleft()
                                        # State 92663
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92664
                                            if len(subjects) == 0:
                                                pass
                                                # 19: 1/cos(e + x*f)
                                                yield 19, subst3
                                        subjects2.appendleft(tmp53)
                            subjects48.appendleft(tmp51)
                    if len(subjects48) >= 1 and isinstance(subjects48[0], Mul):
                        tmp54 = subjects48.popleft()
                        associative1 = tmp54
                        associative_type1 = type(tmp54)
                        subjects55 = deque(tmp54._args)
                        matcher = CommutativeMatcher92666.get()
                        tmp56 = subjects55
                        subjects55 = []
                        for s in tmp56:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp56, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 92667
                                if len(subjects48) == 0:
                                    pass
                                    # State 92668
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp57 = subjects2.popleft()
                                        # State 92669
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92670
                                            if len(subjects) == 0:
                                                pass
                                                # 19: 1/cos(e + x*f)
                                                yield 19, subst2
                                        subjects2.appendleft(tmp57)
                        subjects48.appendleft(tmp54)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 99040
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99041
                        if len(subjects48) >= 1 and isinstance(subjects48[0], Pow):
                            tmp60 = subjects48.popleft()
                            subjects61 = deque(tmp60._args)
                            # State 99042
                            if len(subjects61) >= 1:
                                tmp62 = subjects61.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp62)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 99043
                                    if len(subjects61) >= 1:
                                        tmp64 = subjects61.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp64)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99044
                                            if len(subjects61) == 0:
                                                pass
                                                # State 99045
                                                if len(subjects48) == 0:
                                                    pass
                                                    # State 99046
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp66 = subjects2.popleft()
                                                        # State 99047
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 99048
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 21: 1/cos(x**n*d + c)
                                                                yield 21, subst4
                                                        subjects2.appendleft(tmp66)
                                        subjects61.appendleft(tmp64)
                                subjects61.appendleft(tmp62)
                            subjects48.appendleft(tmp60)
                    if len(subjects48) >= 1 and isinstance(subjects48[0], Mul):
                        tmp67 = subjects48.popleft()
                        associative1 = tmp67
                        associative_type1 = type(tmp67)
                        subjects68 = deque(tmp67._args)
                        matcher = CommutativeMatcher99050.get()
                        tmp69 = subjects68
                        subjects68 = []
                        for s in tmp69:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp69, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 99055
                                if len(subjects48) == 0:
                                    pass
                                    # State 99056
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp70 = subjects2.popleft()
                                        # State 99057
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99058
                                            if len(subjects) == 0:
                                                pass
                                                # 21: 1/cos(x**n*d + c)
                                                yield 21, subst2
                                        subjects2.appendleft(tmp70)
                        subjects48.appendleft(tmp67)
                if len(subjects48) >= 1:
                    tmp71 = subjects48.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp71)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99433
                        if len(subjects48) == 0:
                            pass
                            # State 99434
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp73 = subjects2.popleft()
                                # State 99435
                                if len(subjects2) == 0:
                                    pass
                                    # State 99436
                                    if len(subjects) == 0:
                                        pass
                                        # 23: 1/cos(v)
                                        yield 23, subst1
                                subjects2.appendleft(tmp73)
                    subjects48.appendleft(tmp71)
                if len(subjects48) >= 1 and isinstance(subjects48[0], Add):
                    tmp74 = subjects48.popleft()
                    associative1 = tmp74
                    associative_type1 = type(tmp74)
                    subjects75 = deque(tmp74._args)
                    matcher = CommutativeMatcher92672.get()
                    tmp76 = subjects75
                    subjects75 = []
                    for s in tmp76:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp76, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 92678
                            if len(subjects48) == 0:
                                pass
                                # State 92679
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp77 = subjects2.popleft()
                                    # State 92680
                                    if len(subjects2) == 0:
                                        pass
                                        # State 92681
                                        if len(subjects) == 0:
                                            pass
                                            # 19: 1/cos(e + x*f)
                                            yield 19, subst1
                                    subjects2.appendleft(tmp77)
                        if pattern_index == 1:
                            pass
                            # State 99069
                            if len(subjects48) == 0:
                                pass
                                # State 99070
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp78 = subjects2.popleft()
                                    # State 99071
                                    if len(subjects2) == 0:
                                        pass
                                        # State 99072
                                        if len(subjects) == 0:
                                            pass
                                            # 21: 1/cos(x**n*d + c)
                                            yield 21, subst1
                                    subjects2.appendleft(tmp78)
                    subjects48.appendleft(tmp74)
                subjects2.appendleft(tmp47)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp79 = subjects2.popleft()
                subjects80 = deque(tmp79._args)
                # State 92731
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 92732
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 92733
                        if len(subjects80) >= 1:
                            tmp83 = subjects80.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp83)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 92734
                                if len(subjects80) == 0:
                                    pass
                                    # State 92735
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp85 = subjects2.popleft()
                                        # State 92736
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92737
                                            if len(subjects) == 0:
                                                pass
                                                # 20: 1/sin(e + x*f)
                                                yield 20, subst3
                                        subjects2.appendleft(tmp85)
                            subjects80.appendleft(tmp83)
                    if len(subjects80) >= 1 and isinstance(subjects80[0], Mul):
                        tmp86 = subjects80.popleft()
                        associative1 = tmp86
                        associative_type1 = type(tmp86)
                        subjects87 = deque(tmp86._args)
                        matcher = CommutativeMatcher92739.get()
                        tmp88 = subjects87
                        subjects87 = []
                        for s in tmp88:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp88, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 92740
                                if len(subjects80) == 0:
                                    pass
                                    # State 92741
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp89 = subjects2.popleft()
                                        # State 92742
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92743
                                            if len(subjects) == 0:
                                                pass
                                                # 20: 1/sin(e + x*f)
                                                yield 20, subst2
                                        subjects2.appendleft(tmp89)
                        subjects80.appendleft(tmp86)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 99317
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99318
                        if len(subjects80) >= 1 and isinstance(subjects80[0], Pow):
                            tmp92 = subjects80.popleft()
                            subjects93 = deque(tmp92._args)
                            # State 99319
                            if len(subjects93) >= 1:
                                tmp94 = subjects93.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp94)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 99320
                                    if len(subjects93) >= 1:
                                        tmp96 = subjects93.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp96)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 99321
                                            if len(subjects93) == 0:
                                                pass
                                                # State 99322
                                                if len(subjects80) == 0:
                                                    pass
                                                    # State 99323
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp98 = subjects2.popleft()
                                                        # State 99324
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 99325
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 22: 1/sin(x**n*d + c)
                                                                yield 22, subst4
                                                        subjects2.appendleft(tmp98)
                                        subjects93.appendleft(tmp96)
                                subjects93.appendleft(tmp94)
                            subjects80.appendleft(tmp92)
                    if len(subjects80) >= 1 and isinstance(subjects80[0], Mul):
                        tmp99 = subjects80.popleft()
                        associative1 = tmp99
                        associative_type1 = type(tmp99)
                        subjects100 = deque(tmp99._args)
                        matcher = CommutativeMatcher99327.get()
                        tmp101 = subjects100
                        subjects100 = []
                        for s in tmp101:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp101, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 99332
                                if len(subjects80) == 0:
                                    pass
                                    # State 99333
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp102 = subjects2.popleft()
                                        # State 99334
                                        if len(subjects2) == 0:
                                            pass
                                            # State 99335
                                            if len(subjects) == 0:
                                                pass
                                                # 22: 1/sin(x**n*d + c)
                                                yield 22, subst2
                                        subjects2.appendleft(tmp102)
                        subjects80.appendleft(tmp99)
                if len(subjects80) >= 1:
                    tmp103 = subjects80.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp103)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99471
                        if len(subjects80) == 0:
                            pass
                            # State 99472
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp105 = subjects2.popleft()
                                # State 99473
                                if len(subjects2) == 0:
                                    pass
                                    # State 99474
                                    if len(subjects) == 0:
                                        pass
                                        # 24: 1/sin(v)
                                        yield 24, subst1
                                subjects2.appendleft(tmp105)
                    subjects80.appendleft(tmp103)
                if len(subjects80) >= 1 and isinstance(subjects80[0], Add):
                    tmp106 = subjects80.popleft()
                    associative1 = tmp106
                    associative_type1 = type(tmp106)
                    subjects107 = deque(tmp106._args)
                    matcher = CommutativeMatcher92745.get()
                    tmp108 = subjects107
                    subjects107 = []
                    for s in tmp108:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp108, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 92751
                            if len(subjects80) == 0:
                                pass
                                # State 92752
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp109 = subjects2.popleft()
                                    # State 92753
                                    if len(subjects2) == 0:
                                        pass
                                        # State 92754
                                        if len(subjects) == 0:
                                            pass
                                            # 20: 1/sin(e + x*f)
                                            yield 20, subst1
                                    subjects2.appendleft(tmp109)
                        if pattern_index == 1:
                            pass
                            # State 99346
                            if len(subjects80) == 0:
                                pass
                                # State 99347
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp110 = subjects2.popleft()
                                    # State 99348
                                    if len(subjects2) == 0:
                                        pass
                                        # State 99349
                                        if len(subjects) == 0:
                                            pass
                                            # 22: 1/sin(x**n*d + c)
                                            yield 22, subst1
                                    subjects2.appendleft(tmp110)
                    subjects80.appendleft(tmp106)
                subjects2.appendleft(tmp79)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tanh):
                tmp111 = subjects2.popleft()
                subjects112 = deque(tmp111._args)
                # State 128422
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 128423
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128424
                        if len(subjects112) >= 1 and isinstance(subjects112[0], Pow):
                            tmp115 = subjects112.popleft()
                            subjects116 = deque(tmp115._args)
                            # State 128425
                            if len(subjects116) >= 1:
                                tmp117 = subjects116.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp117)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 128426
                                    if len(subjects116) >= 1:
                                        tmp119 = subjects116.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp119)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 128427
                                            if len(subjects116) == 0:
                                                pass
                                                # State 128428
                                                if len(subjects112) == 0:
                                                    pass
                                                    # State 128429
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp121 = subjects2.popleft()
                                                        # State 128430
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 128431
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 36: 1/tanh(x**n*d + c)
                                                                yield 36, subst4
                                                        subjects2.appendleft(tmp121)
                                        subjects116.appendleft(tmp119)
                                subjects116.appendleft(tmp117)
                            subjects112.appendleft(tmp115)
                    if len(subjects112) >= 1 and isinstance(subjects112[0], Mul):
                        tmp122 = subjects112.popleft()
                        associative1 = tmp122
                        associative_type1 = type(tmp122)
                        subjects123 = deque(tmp122._args)
                        matcher = CommutativeMatcher128433.get()
                        tmp124 = subjects123
                        subjects123 = []
                        for s in tmp124:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp124, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 128438
                                if len(subjects112) == 0:
                                    pass
                                    # State 128439
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp125 = subjects2.popleft()
                                        # State 128440
                                        if len(subjects2) == 0:
                                            pass
                                            # State 128441
                                            if len(subjects) == 0:
                                                pass
                                                # 36: 1/tanh(x**n*d + c)
                                                yield 36, subst2
                                        subjects2.appendleft(tmp125)
                        subjects112.appendleft(tmp122)
                if len(subjects112) >= 1:
                    tmp126 = subjects112.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp126)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128569
                        if len(subjects112) == 0:
                            pass
                            # State 128570
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp128 = subjects2.popleft()
                                # State 128571
                                if len(subjects2) == 0:
                                    pass
                                    # State 128572
                                    if len(subjects) == 0:
                                        pass
                                        # 38: 1/tanh(v)
                                        yield 38, subst1
                                subjects2.appendleft(tmp128)
                    subjects112.appendleft(tmp126)
                if len(subjects112) >= 1 and isinstance(subjects112[0], Add):
                    tmp129 = subjects112.popleft()
                    associative1 = tmp129
                    associative_type1 = type(tmp129)
                    subjects130 = deque(tmp129._args)
                    matcher = CommutativeMatcher128443.get()
                    tmp131 = subjects130
                    subjects130 = []
                    for s in tmp131:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp131, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 128456
                            if len(subjects112) == 0:
                                pass
                                # State 128457
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp132 = subjects2.popleft()
                                    # State 128458
                                    if len(subjects2) == 0:
                                        pass
                                        # State 128459
                                        if len(subjects) == 0:
                                            pass
                                            # 36: 1/tanh(x**n*d + c)
                                            yield 36, subst1
                                    subjects2.appendleft(tmp132)
                    subjects112.appendleft(tmp129)
                subjects2.appendleft(tmp111)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cosh):
                tmp133 = subjects2.popleft()
                subjects134 = deque(tmp133._args)
                # State 131366
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 131367
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131368
                        if len(subjects134) >= 1 and isinstance(subjects134[0], Pow):
                            tmp137 = subjects134.popleft()
                            subjects138 = deque(tmp137._args)
                            # State 131369
                            if len(subjects138) >= 1:
                                tmp139 = subjects138.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp139)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 131370
                                    if len(subjects138) >= 1:
                                        tmp141 = subjects138.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp141)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 131371
                                            if len(subjects138) == 0:
                                                pass
                                                # State 131372
                                                if len(subjects134) == 0:
                                                    pass
                                                    # State 131373
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp143 = subjects2.popleft()
                                                        # State 131374
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 131375
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 39: 1/cosh(x**n*d + c)
                                                                yield 39, subst4
                                                        subjects2.appendleft(tmp143)
                                        subjects138.appendleft(tmp141)
                                subjects138.appendleft(tmp139)
                            subjects134.appendleft(tmp137)
                    if len(subjects134) >= 1 and isinstance(subjects134[0], Mul):
                        tmp144 = subjects134.popleft()
                        associative1 = tmp144
                        associative_type1 = type(tmp144)
                        subjects145 = deque(tmp144._args)
                        matcher = CommutativeMatcher131377.get()
                        tmp146 = subjects145
                        subjects145 = []
                        for s in tmp146:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp146, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 131382
                                if len(subjects134) == 0:
                                    pass
                                    # State 131383
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp147 = subjects2.popleft()
                                        # State 131384
                                        if len(subjects2) == 0:
                                            pass
                                            # State 131385
                                            if len(subjects) == 0:
                                                pass
                                                # 39: 1/cosh(x**n*d + c)
                                                yield 39, subst2
                                        subjects2.appendleft(tmp147)
                        subjects134.appendleft(tmp144)
                if len(subjects134) >= 1:
                    tmp148 = subjects134.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp148)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131782
                        if len(subjects134) == 0:
                            pass
                            # State 131783
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp150 = subjects2.popleft()
                                # State 131784
                                if len(subjects2) == 0:
                                    pass
                                    # State 131785
                                    if len(subjects) == 0:
                                        pass
                                        # 41: 1/cosh(u)
                                        yield 41, subst1
                                subjects2.appendleft(tmp150)
                    subjects134.appendleft(tmp148)
                if len(subjects134) >= 1 and isinstance(subjects134[0], Add):
                    tmp151 = subjects134.popleft()
                    associative1 = tmp151
                    associative_type1 = type(tmp151)
                    subjects152 = deque(tmp151._args)
                    matcher = CommutativeMatcher131387.get()
                    tmp153 = subjects152
                    subjects152 = []
                    for s in tmp153:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp153, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 131400
                            if len(subjects134) == 0:
                                pass
                                # State 131401
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp154 = subjects2.popleft()
                                    # State 131402
                                    if len(subjects2) == 0:
                                        pass
                                        # State 131403
                                        if len(subjects) == 0:
                                            pass
                                            # 39: 1/cosh(x**n*d + c)
                                            yield 39, subst1
                                    subjects2.appendleft(tmp154)
                    subjects134.appendleft(tmp151)
                subjects2.appendleft(tmp133)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sinh):
                tmp155 = subjects2.popleft()
                subjects156 = deque(tmp155._args)
                # State 131661
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 131662
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131663
                        if len(subjects156) >= 1 and isinstance(subjects156[0], Pow):
                            tmp159 = subjects156.popleft()
                            subjects160 = deque(tmp159._args)
                            # State 131664
                            if len(subjects160) >= 1:
                                tmp161 = subjects160.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.0_1', tmp161)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 131665
                                    if len(subjects160) >= 1:
                                        tmp163 = subjects160.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.3.1.2', tmp163)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 131666
                                            if len(subjects160) == 0:
                                                pass
                                                # State 131667
                                                if len(subjects156) == 0:
                                                    pass
                                                    # State 131668
                                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                                        tmp165 = subjects2.popleft()
                                                        # State 131669
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 131670
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 40: 1/sinh(x**n*d + c)
                                                                yield 40, subst4
                                                        subjects2.appendleft(tmp165)
                                        subjects160.appendleft(tmp163)
                                subjects160.appendleft(tmp161)
                            subjects156.appendleft(tmp159)
                    if len(subjects156) >= 1 and isinstance(subjects156[0], Mul):
                        tmp166 = subjects156.popleft()
                        associative1 = tmp166
                        associative_type1 = type(tmp166)
                        subjects167 = deque(tmp166._args)
                        matcher = CommutativeMatcher131672.get()
                        tmp168 = subjects167
                        subjects167 = []
                        for s in tmp168:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp168, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 131677
                                if len(subjects156) == 0:
                                    pass
                                    # State 131678
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp169 = subjects2.popleft()
                                        # State 131679
                                        if len(subjects2) == 0:
                                            pass
                                            # State 131680
                                            if len(subjects) == 0:
                                                pass
                                                # 40: 1/sinh(x**n*d + c)
                                                yield 40, subst2
                                        subjects2.appendleft(tmp169)
                        subjects156.appendleft(tmp166)
                if len(subjects156) >= 1:
                    tmp170 = subjects156.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp170)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131829
                        if len(subjects156) == 0:
                            pass
                            # State 131830
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp172 = subjects2.popleft()
                                # State 131831
                                if len(subjects2) == 0:
                                    pass
                                    # State 131832
                                    if len(subjects) == 0:
                                        pass
                                        # 42: 1/sinh(u)
                                        yield 42, subst1
                                subjects2.appendleft(tmp172)
                    subjects156.appendleft(tmp170)
                if len(subjects156) >= 1 and isinstance(subjects156[0], Add):
                    tmp173 = subjects156.popleft()
                    associative1 = tmp173
                    associative_type1 = type(tmp173)
                    subjects174 = deque(tmp173._args)
                    matcher = CommutativeMatcher131682.get()
                    tmp175 = subjects174
                    subjects174 = []
                    for s in tmp175:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp175, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 131695
                            if len(subjects156) == 0:
                                pass
                                # State 131696
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp176 = subjects2.popleft()
                                    # State 131697
                                    if len(subjects2) == 0:
                                        pass
                                        # State 131698
                                        if len(subjects) == 0:
                                            pass
                                            # 40: 1/sinh(x**n*d + c)
                                            yield 40, subst1
                                    subjects2.appendleft(tmp176)
                    subjects156.appendleft(tmp173)
                subjects2.appendleft(tmp155)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp177 = subjects.popleft()
            subjects178 = deque(tmp177._args)
            # State 63073
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63074
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63075
                    if len(subjects178) >= 1:
                        tmp181 = subjects178.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp181)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63076
                            if len(subjects178) == 0:
                                pass
                                # State 63077
                                if len(subjects) == 0:
                                    pass
                                    # 3: sin(e + x*f)
                                    yield 3, subst3
                        subjects178.appendleft(tmp181)
                if len(subjects178) >= 1 and isinstance(subjects178[0], Mul):
                    tmp183 = subjects178.popleft()
                    associative1 = tmp183
                    associative_type1 = type(tmp183)
                    subjects184 = deque(tmp183._args)
                    matcher = CommutativeMatcher63079.get()
                    tmp185 = subjects184
                    subjects184 = []
                    for s in tmp185:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp185, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63080
                            if len(subjects178) == 0:
                                pass
                                # State 63081
                                if len(subjects) == 0:
                                    pass
                                    # 3: sin(e + x*f)
                                    yield 3, subst2
                    subjects178.appendleft(tmp183)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63329
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63330
                    if len(subjects178) >= 1:
                        tmp188 = subjects178.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp188)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63331
                            if len(subjects178) == 0:
                                pass
                                # State 63332
                                if len(subjects) == 0:
                                    pass
                                    # 5: sin(e + x*f)
                                    yield 5, subst3
                        subjects178.appendleft(tmp188)
                if len(subjects178) >= 1 and isinstance(subjects178[0], Mul):
                    tmp190 = subjects178.popleft()
                    associative1 = tmp190
                    associative_type1 = type(tmp190)
                    subjects191 = deque(tmp190._args)
                    matcher = CommutativeMatcher63334.get()
                    tmp192 = subjects191
                    subjects191 = []
                    for s in tmp192:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp192, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63335
                            if len(subjects178) == 0:
                                pass
                                # State 63336
                                if len(subjects) == 0:
                                    pass
                                    # 5: sin(e + x*f)
                                    yield 5, subst2
                    subjects178.appendleft(tmp190)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 74209
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 74210
                    if len(subjects178) >= 1 and isinstance(subjects178[0], Pow):
                        tmp195 = subjects178.popleft()
                        subjects196 = deque(tmp195._args)
                        # State 74211
                        if len(subjects196) >= 1:
                            tmp197 = subjects196.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp197)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74212
                                if len(subjects196) >= 1:
                                    tmp199 = subjects196.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp199)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 74213
                                        if len(subjects196) == 0:
                                            pass
                                            # State 74214
                                            if len(subjects178) == 0:
                                                pass
                                                # State 74215
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: sin(x**n*d + c)
                                                    yield 7, subst4
                                    subjects196.appendleft(tmp199)
                            subjects196.appendleft(tmp197)
                        if len(subjects196) >= 1:
                            tmp201 = subjects196.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp201)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74792
                                if len(subjects196) >= 1:
                                    tmp203 = subjects196.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp203)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 74793
                                        if len(subjects196) == 0:
                                            pass
                                            # State 74794
                                            if len(subjects178) == 0:
                                                pass
                                                # State 74795
                                                if len(subjects) == 0:
                                                    pass
                                                    # 9: sin(x**n*d + c)
                                                    yield 9, subst4
                                    subjects196.appendleft(tmp203)
                            subjects196.appendleft(tmp201)
                        if len(subjects196) >= 1:
                            tmp205 = subjects196.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp205)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75216
                                if len(subjects196) >= 1:
                                    tmp207 = subjects196.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp207)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 75217
                                        if len(subjects196) == 0:
                                            pass
                                            # State 75218
                                            if len(subjects178) == 0:
                                                pass
                                                # State 75219
                                                if len(subjects) == 0:
                                                    pass
                                                    # 11: sin(c + d*x**n)
                                                    yield 11, subst4
                                    subjects196.appendleft(tmp207)
                            subjects196.appendleft(tmp205)
                        subjects178.appendleft(tmp195)
                if len(subjects178) >= 1 and isinstance(subjects178[0], Mul):
                    tmp209 = subjects178.popleft()
                    associative1 = tmp209
                    associative_type1 = type(tmp209)
                    subjects210 = deque(tmp209._args)
                    matcher = CommutativeMatcher74217.get()
                    tmp211 = subjects210
                    subjects210 = []
                    for s in tmp211:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp211, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 74222
                            if len(subjects178) == 0:
                                pass
                                # State 74223
                                if len(subjects) == 0:
                                    pass
                                    # 7: sin(x**n*d + c)
                                    yield 7, subst2
                        if pattern_index == 1:
                            pass
                            # State 74799
                            if len(subjects178) == 0:
                                pass
                                # State 74800
                                if len(subjects) == 0:
                                    pass
                                    # 9: sin(x**n*d + c)
                                    yield 9, subst2
                        if pattern_index == 2:
                            pass
                            # State 75223
                            if len(subjects178) == 0:
                                pass
                                # State 75224
                                if len(subjects) == 0:
                                    pass
                                    # 11: sin(c + d*x**n)
                                    yield 11, subst2
                    subjects178.appendleft(tmp209)
            if len(subjects178) >= 1:
                tmp212 = subjects178.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp212)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75384
                    if len(subjects178) == 0:
                        pass
                        # State 75385
                        if len(subjects) == 0:
                            pass
                            # 13: sin(v)
                            yield 13, subst1
                subjects178.appendleft(tmp212)
            if len(subjects178) >= 1 and isinstance(subjects178[0], Add):
                tmp214 = subjects178.popleft()
                associative1 = tmp214
                associative_type1 = type(tmp214)
                subjects215 = deque(tmp214._args)
                matcher = CommutativeMatcher63083.get()
                tmp216 = subjects215
                subjects215 = []
                for s in tmp216:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp216, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 63089
                        if len(subjects178) == 0:
                            pass
                            # State 63090
                            if len(subjects) == 0:
                                pass
                                # 3: sin(e + x*f)
                                yield 3, subst1
                    if pattern_index == 1:
                        pass
                        # State 63340
                        if len(subjects178) == 0:
                            pass
                            # State 63341
                            if len(subjects) == 0:
                                pass
                                # 5: sin(e + x*f)
                                yield 5, subst1
                    if pattern_index == 2:
                        pass
                        # State 74234
                        if len(subjects178) == 0:
                            pass
                            # State 74235
                            if len(subjects) == 0:
                                pass
                                # 7: sin(x**n*d + c)
                                yield 7, subst1
                    if pattern_index == 3:
                        pass
                        # State 74808
                        if len(subjects178) == 0:
                            pass
                            # State 74809
                            if len(subjects) == 0:
                                pass
                                # 9: sin(x**n*d + c)
                                yield 9, subst1
                    if pattern_index == 4:
                        pass
                        # State 75232
                        if len(subjects178) == 0:
                            pass
                            # State 75233
                            if len(subjects) == 0:
                                pass
                                # 11: sin(c + d*x**n)
                                yield 11, subst1
                subjects178.appendleft(tmp214)
            subjects.appendleft(tmp177)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp217 = subjects.popleft()
            subjects218 = deque(tmp217._args)
            # State 63162
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63163
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63164
                    if len(subjects218) >= 1:
                        tmp221 = subjects218.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp221)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63165
                            if len(subjects218) == 0:
                                pass
                                # State 63166
                                if len(subjects) == 0:
                                    pass
                                    # 4: cos(e + x*f)
                                    yield 4, subst3
                        subjects218.appendleft(tmp221)
                if len(subjects218) >= 1 and isinstance(subjects218[0], Mul):
                    tmp223 = subjects218.popleft()
                    associative1 = tmp223
                    associative_type1 = type(tmp223)
                    subjects224 = deque(tmp223._args)
                    matcher = CommutativeMatcher63168.get()
                    tmp225 = subjects224
                    subjects224 = []
                    for s in tmp225:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp225, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63169
                            if len(subjects218) == 0:
                                pass
                                # State 63170
                                if len(subjects) == 0:
                                    pass
                                    # 4: cos(e + x*f)
                                    yield 4, subst2
                    subjects218.appendleft(tmp223)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63505
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63506
                    if len(subjects218) >= 1:
                        tmp228 = subjects218.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp228)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63507
                            if len(subjects218) == 0:
                                pass
                                # State 63508
                                if len(subjects) == 0:
                                    pass
                                    # 6: cos(e + x*f)
                                    yield 6, subst3
                        subjects218.appendleft(tmp228)
                if len(subjects218) >= 1 and isinstance(subjects218[0], Mul):
                    tmp230 = subjects218.popleft()
                    associative1 = tmp230
                    associative_type1 = type(tmp230)
                    subjects231 = deque(tmp230._args)
                    matcher = CommutativeMatcher63510.get()
                    tmp232 = subjects231
                    subjects231 = []
                    for s in tmp232:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp232, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63511
                            if len(subjects218) == 0:
                                pass
                                # State 63512
                                if len(subjects) == 0:
                                    pass
                                    # 6: cos(e + x*f)
                                    yield 6, subst2
                    subjects218.appendleft(tmp230)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 74438
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 74439
                    if len(subjects218) >= 1 and isinstance(subjects218[0], Pow):
                        tmp235 = subjects218.popleft()
                        subjects236 = deque(tmp235._args)
                        # State 74440
                        if len(subjects236) >= 1:
                            tmp237 = subjects236.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp237)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74441
                                if len(subjects236) >= 1:
                                    tmp239 = subjects236.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp239)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 74442
                                        if len(subjects236) == 0:
                                            pass
                                            # State 74443
                                            if len(subjects218) == 0:
                                                pass
                                                # State 74444
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: cos(x**n*d + c)
                                                    yield 8, subst4
                                    subjects236.appendleft(tmp239)
                            subjects236.appendleft(tmp237)
                        if len(subjects236) >= 1:
                            tmp241 = subjects236.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp241)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74955
                                if len(subjects236) >= 1:
                                    tmp243 = subjects236.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp243)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 74956
                                        if len(subjects236) == 0:
                                            pass
                                            # State 74957
                                            if len(subjects218) == 0:
                                                pass
                                                # State 74958
                                                if len(subjects) == 0:
                                                    pass
                                                    # 10: cos(x**n*d + c)
                                                    yield 10, subst4
                                    subjects236.appendleft(tmp243)
                            subjects236.appendleft(tmp241)
                        if len(subjects236) >= 1:
                            tmp245 = subjects236.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp245)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75342
                                if len(subjects236) >= 1:
                                    tmp247 = subjects236.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp247)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 75343
                                        if len(subjects236) == 0:
                                            pass
                                            # State 75344
                                            if len(subjects218) == 0:
                                                pass
                                                # State 75345
                                                if len(subjects) == 0:
                                                    pass
                                                    # 12: cos(c + d*x**n)
                                                    yield 12, subst4
                                    subjects236.appendleft(tmp247)
                            subjects236.appendleft(tmp245)
                        subjects218.appendleft(tmp235)
                if len(subjects218) >= 1 and isinstance(subjects218[0], Mul):
                    tmp249 = subjects218.popleft()
                    associative1 = tmp249
                    associative_type1 = type(tmp249)
                    subjects250 = deque(tmp249._args)
                    matcher = CommutativeMatcher74446.get()
                    tmp251 = subjects250
                    subjects250 = []
                    for s in tmp251:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp251, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 74451
                            if len(subjects218) == 0:
                                pass
                                # State 74452
                                if len(subjects) == 0:
                                    pass
                                    # 8: cos(x**n*d + c)
                                    yield 8, subst2
                        if pattern_index == 1:
                            pass
                            # State 74962
                            if len(subjects218) == 0:
                                pass
                                # State 74963
                                if len(subjects) == 0:
                                    pass
                                    # 10: cos(x**n*d + c)
                                    yield 10, subst2
                        if pattern_index == 2:
                            pass
                            # State 75349
                            if len(subjects218) == 0:
                                pass
                                # State 75350
                                if len(subjects) == 0:
                                    pass
                                    # 12: cos(c + d*x**n)
                                    yield 12, subst2
                    subjects218.appendleft(tmp249)
            if len(subjects218) >= 1:
                tmp252 = subjects218.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp252)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75410
                    if len(subjects218) == 0:
                        pass
                        # State 75411
                        if len(subjects) == 0:
                            pass
                            # 14: cos(v)
                            yield 14, subst1
                subjects218.appendleft(tmp252)
            if len(subjects218) >= 1 and isinstance(subjects218[0], Add):
                tmp254 = subjects218.popleft()
                associative1 = tmp254
                associative_type1 = type(tmp254)
                subjects255 = deque(tmp254._args)
                matcher = CommutativeMatcher63172.get()
                tmp256 = subjects255
                subjects255 = []
                for s in tmp256:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp256, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 63178
                        if len(subjects218) == 0:
                            pass
                            # State 63179
                            if len(subjects) == 0:
                                pass
                                # 4: cos(e + x*f)
                                yield 4, subst1
                    if pattern_index == 1:
                        pass
                        # State 63516
                        if len(subjects218) == 0:
                            pass
                            # State 63517
                            if len(subjects) == 0:
                                pass
                                # 6: cos(e + x*f)
                                yield 6, subst1
                    if pattern_index == 2:
                        pass
                        # State 74463
                        if len(subjects218) == 0:
                            pass
                            # State 74464
                            if len(subjects) == 0:
                                pass
                                # 8: cos(x**n*d + c)
                                yield 8, subst1
                    if pattern_index == 3:
                        pass
                        # State 74971
                        if len(subjects218) == 0:
                            pass
                            # State 74972
                            if len(subjects) == 0:
                                pass
                                # 10: cos(x**n*d + c)
                                yield 10, subst1
                    if pattern_index == 4:
                        pass
                        # State 75358
                        if len(subjects218) == 0:
                            pass
                            # State 75359
                            if len(subjects) == 0:
                                pass
                                # 12: cos(c + d*x**n)
                                yield 12, subst1
                subjects218.appendleft(tmp254)
            subjects.appendleft(tmp217)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp257 = subjects.popleft()
            subjects258 = deque(tmp257._args)
            # State 88607
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 88608
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 88609
                    if len(subjects258) >= 1 and isinstance(subjects258[0], Pow):
                        tmp261 = subjects258.popleft()
                        subjects262 = deque(tmp261._args)
                        # State 88610
                        if len(subjects262) >= 1:
                            tmp263 = subjects262.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp263)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 88611
                                if len(subjects262) >= 1:
                                    tmp265 = subjects262.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp265)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 88612
                                        if len(subjects262) == 0:
                                            pass
                                            # State 88613
                                            if len(subjects258) == 0:
                                                pass
                                                # State 88614
                                                if len(subjects) == 0:
                                                    pass
                                                    # 15: tan(x**n*d + c)
                                                    yield 15, subst4
                                    subjects262.appendleft(tmp265)
                            subjects262.appendleft(tmp263)
                        subjects258.appendleft(tmp261)
                if len(subjects258) >= 1 and isinstance(subjects258[0], Mul):
                    tmp267 = subjects258.popleft()
                    associative1 = tmp267
                    associative_type1 = type(tmp267)
                    subjects268 = deque(tmp267._args)
                    matcher = CommutativeMatcher88616.get()
                    tmp269 = subjects268
                    subjects268 = []
                    for s in tmp269:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp269, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 88621
                            if len(subjects258) == 0:
                                pass
                                # State 88622
                                if len(subjects) == 0:
                                    pass
                                    # 15: tan(x**n*d + c)
                                    yield 15, subst2
                    subjects258.appendleft(tmp267)
            if len(subjects258) >= 1:
                tmp270 = subjects258.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp270)
                except ValueError:
                    pass
                else:
                    pass
                    # State 88982
                    if len(subjects258) == 0:
                        pass
                        # State 88983
                        if len(subjects) == 0:
                            pass
                            # 17: tan(v)
                            yield 17, subst1
                subjects258.appendleft(tmp270)
            if len(subjects258) >= 1 and isinstance(subjects258[0], Add):
                tmp272 = subjects258.popleft()
                associative1 = tmp272
                associative_type1 = type(tmp272)
                subjects273 = deque(tmp272._args)
                matcher = CommutativeMatcher88624.get()
                tmp274 = subjects273
                subjects273 = []
                for s in tmp274:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp274, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 88637
                        if len(subjects258) == 0:
                            pass
                            # State 88638
                            if len(subjects) == 0:
                                pass
                                # 15: tan(x**n*d + c)
                                yield 15, subst1
                subjects258.appendleft(tmp272)
            subjects.appendleft(tmp257)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp275 = subjects.popleft()
            subjects276 = deque(tmp275._args)
            # State 108407
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108408
                if len(subjects276) >= 1:
                    tmp278 = subjects276.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp278)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108409
                        if len(subjects276) == 0:
                            pass
                            # State 108410
                            if len(subjects) == 0:
                                pass
                                # 25: asin(x*c)
                                yield 25, subst2
                    subjects276.appendleft(tmp278)
            if len(subjects276) >= 1 and isinstance(subjects276[0], Mul):
                tmp280 = subjects276.popleft()
                associative1 = tmp280
                associative_type1 = type(tmp280)
                subjects281 = deque(tmp280._args)
                matcher = CommutativeMatcher108412.get()
                tmp282 = subjects281
                subjects281 = []
                for s in tmp282:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp282, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108413
                        if len(subjects276) == 0:
                            pass
                            # State 108414
                            if len(subjects) == 0:
                                pass
                                # 25: asin(x*c)
                                yield 25, subst1
                subjects276.appendleft(tmp280)
            subjects.appendleft(tmp275)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp283 = subjects.popleft()
            subjects284 = deque(tmp283._args)
            # State 108482
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108483
                if len(subjects284) >= 1:
                    tmp286 = subjects284.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp286)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108484
                        if len(subjects284) == 0:
                            pass
                            # State 108485
                            if len(subjects) == 0:
                                pass
                                # 26: acos(x*c)
                                yield 26, subst2
                    subjects284.appendleft(tmp286)
            if len(subjects284) >= 1 and isinstance(subjects284[0], Mul):
                tmp288 = subjects284.popleft()
                associative1 = tmp288
                associative_type1 = type(tmp288)
                subjects289 = deque(tmp288._args)
                matcher = CommutativeMatcher108487.get()
                tmp290 = subjects289
                subjects289 = []
                for s in tmp290:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp290, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108488
                        if len(subjects284) == 0:
                            pass
                            # State 108489
                            if len(subjects) == 0:
                                pass
                                # 26: acos(x*c)
                                yield 26, subst1
                subjects284.appendleft(tmp288)
            subjects.appendleft(tmp283)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp291 = subjects.popleft()
            subjects292 = deque(tmp291._args)
            # State 124132
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 124133
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 124134
                    if len(subjects292) >= 1 and isinstance(subjects292[0], Pow):
                        tmp295 = subjects292.popleft()
                        subjects296 = deque(tmp295._args)
                        # State 124135
                        if len(subjects296) >= 1:
                            tmp297 = subjects296.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp297)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124136
                                if len(subjects296) >= 1:
                                    tmp299 = subjects296.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp299)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 124137
                                        if len(subjects296) == 0:
                                            pass
                                            # State 124138
                                            if len(subjects292) == 0:
                                                pass
                                                # State 124139
                                                if len(subjects) == 0:
                                                    pass
                                                    # 27: sinh(x**n*d + c)
                                                    yield 27, subst4
                                    subjects296.appendleft(tmp299)
                            subjects296.appendleft(tmp297)
                        if len(subjects296) >= 1:
                            tmp301 = subjects296.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp301)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124702
                                if len(subjects296) >= 1:
                                    tmp303 = subjects296.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp303)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 124703
                                        if len(subjects296) == 0:
                                            pass
                                            # State 124704
                                            if len(subjects292) == 0:
                                                pass
                                                # State 124705
                                                if len(subjects) == 0:
                                                    pass
                                                    # 29: sinh(x**n*d + c)
                                                    yield 29, subst4
                                    subjects296.appendleft(tmp303)
                            subjects296.appendleft(tmp301)
                        if len(subjects296) >= 1:
                            tmp305 = subjects296.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp305)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125126
                                if len(subjects296) >= 1:
                                    tmp307 = subjects296.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp307)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 125127
                                        if len(subjects296) == 0:
                                            pass
                                            # State 125128
                                            if len(subjects292) == 0:
                                                pass
                                                # State 125129
                                                if len(subjects) == 0:
                                                    pass
                                                    # 31: sinh(c + d*x**n)
                                                    yield 31, subst4
                                    subjects296.appendleft(tmp307)
                            subjects296.appendleft(tmp305)
                        subjects292.appendleft(tmp295)
                if len(subjects292) >= 1 and isinstance(subjects292[0], Mul):
                    tmp309 = subjects292.popleft()
                    associative1 = tmp309
                    associative_type1 = type(tmp309)
                    subjects310 = deque(tmp309._args)
                    matcher = CommutativeMatcher124141.get()
                    tmp311 = subjects310
                    subjects310 = []
                    for s in tmp311:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp311, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 124146
                            if len(subjects292) == 0:
                                pass
                                # State 124147
                                if len(subjects) == 0:
                                    pass
                                    # 27: sinh(x**n*d + c)
                                    yield 27, subst2
                        if pattern_index == 1:
                            pass
                            # State 124709
                            if len(subjects292) == 0:
                                pass
                                # State 124710
                                if len(subjects) == 0:
                                    pass
                                    # 29: sinh(x**n*d + c)
                                    yield 29, subst2
                        if pattern_index == 2:
                            pass
                            # State 125133
                            if len(subjects292) == 0:
                                pass
                                # State 125134
                                if len(subjects) == 0:
                                    pass
                                    # 31: sinh(c + d*x**n)
                                    yield 31, subst2
                    subjects292.appendleft(tmp309)
            if len(subjects292) >= 1:
                tmp312 = subjects292.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp312)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125294
                    if len(subjects292) == 0:
                        pass
                        # State 125295
                        if len(subjects) == 0:
                            pass
                            # 33: sinh(v)
                            yield 33, subst1
                subjects292.appendleft(tmp312)
            if len(subjects292) >= 1 and isinstance(subjects292[0], Add):
                tmp314 = subjects292.popleft()
                associative1 = tmp314
                associative_type1 = type(tmp314)
                subjects315 = deque(tmp314._args)
                matcher = CommutativeMatcher124149.get()
                tmp316 = subjects315
                subjects315 = []
                for s in tmp316:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp316, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 124162
                        if len(subjects292) == 0:
                            pass
                            # State 124163
                            if len(subjects) == 0:
                                pass
                                # 27: sinh(x**n*d + c)
                                yield 27, subst1
                    if pattern_index == 1:
                        pass
                        # State 124718
                        if len(subjects292) == 0:
                            pass
                            # State 124719
                            if len(subjects) == 0:
                                pass
                                # 29: sinh(x**n*d + c)
                                yield 29, subst1
                    if pattern_index == 2:
                        pass
                        # State 125142
                        if len(subjects292) == 0:
                            pass
                            # State 125143
                            if len(subjects) == 0:
                                pass
                                # 31: sinh(c + d*x**n)
                                yield 31, subst1
                subjects292.appendleft(tmp314)
            subjects.appendleft(tmp291)
        if len(subjects) >= 1 and isinstance(subjects[0], cosh):
            tmp317 = subjects.popleft()
            subjects318 = deque(tmp317._args)
            # State 124379
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 124380
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 124381
                    if len(subjects318) >= 1 and isinstance(subjects318[0], Pow):
                        tmp321 = subjects318.popleft()
                        subjects322 = deque(tmp321._args)
                        # State 124382
                        if len(subjects322) >= 1:
                            tmp323 = subjects322.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp323)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124383
                                if len(subjects322) >= 1:
                                    tmp325 = subjects322.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp325)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 124384
                                        if len(subjects322) == 0:
                                            pass
                                            # State 124385
                                            if len(subjects318) == 0:
                                                pass
                                                # State 124386
                                                if len(subjects) == 0:
                                                    pass
                                                    # 28: cosh(x**n*d + c)
                                                    yield 28, subst4
                                    subjects322.appendleft(tmp325)
                            subjects322.appendleft(tmp323)
                        if len(subjects322) >= 1:
                            tmp327 = subjects322.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp327)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124865
                                if len(subjects322) >= 1:
                                    tmp329 = subjects322.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp329)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 124866
                                        if len(subjects322) == 0:
                                            pass
                                            # State 124867
                                            if len(subjects318) == 0:
                                                pass
                                                # State 124868
                                                if len(subjects) == 0:
                                                    pass
                                                    # 30: cosh(x**n*d + c)
                                                    yield 30, subst4
                                    subjects322.appendleft(tmp329)
                            subjects322.appendleft(tmp327)
                        if len(subjects322) >= 1:
                            tmp331 = subjects322.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp331)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125252
                                if len(subjects322) >= 1:
                                    tmp333 = subjects322.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp333)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 125253
                                        if len(subjects322) == 0:
                                            pass
                                            # State 125254
                                            if len(subjects318) == 0:
                                                pass
                                                # State 125255
                                                if len(subjects) == 0:
                                                    pass
                                                    # 32: cosh(c + d*x**n)
                                                    yield 32, subst4
                                    subjects322.appendleft(tmp333)
                            subjects322.appendleft(tmp331)
                        subjects318.appendleft(tmp321)
                if len(subjects318) >= 1 and isinstance(subjects318[0], Mul):
                    tmp335 = subjects318.popleft()
                    associative1 = tmp335
                    associative_type1 = type(tmp335)
                    subjects336 = deque(tmp335._args)
                    matcher = CommutativeMatcher124388.get()
                    tmp337 = subjects336
                    subjects336 = []
                    for s in tmp337:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp337, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 124393
                            if len(subjects318) == 0:
                                pass
                                # State 124394
                                if len(subjects) == 0:
                                    pass
                                    # 28: cosh(x**n*d + c)
                                    yield 28, subst2
                        if pattern_index == 1:
                            pass
                            # State 124872
                            if len(subjects318) == 0:
                                pass
                                # State 124873
                                if len(subjects) == 0:
                                    pass
                                    # 30: cosh(x**n*d + c)
                                    yield 30, subst2
                        if pattern_index == 2:
                            pass
                            # State 125259
                            if len(subjects318) == 0:
                                pass
                                # State 125260
                                if len(subjects) == 0:
                                    pass
                                    # 32: cosh(c + d*x**n)
                                    yield 32, subst2
                    subjects318.appendleft(tmp335)
            if len(subjects318) >= 1:
                tmp338 = subjects318.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp338)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125320
                    if len(subjects318) == 0:
                        pass
                        # State 125321
                        if len(subjects) == 0:
                            pass
                            # 34: cosh(v)
                            yield 34, subst1
                subjects318.appendleft(tmp338)
            if len(subjects318) >= 1 and isinstance(subjects318[0], Add):
                tmp340 = subjects318.popleft()
                associative1 = tmp340
                associative_type1 = type(tmp340)
                subjects341 = deque(tmp340._args)
                matcher = CommutativeMatcher124396.get()
                tmp342 = subjects341
                subjects341 = []
                for s in tmp342:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp342, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 124409
                        if len(subjects318) == 0:
                            pass
                            # State 124410
                            if len(subjects) == 0:
                                pass
                                # 28: cosh(x**n*d + c)
                                yield 28, subst1
                    if pattern_index == 1:
                        pass
                        # State 124881
                        if len(subjects318) == 0:
                            pass
                            # State 124882
                            if len(subjects) == 0:
                                pass
                                # 30: cosh(x**n*d + c)
                                yield 30, subst1
                    if pattern_index == 2:
                        pass
                        # State 125268
                        if len(subjects318) == 0:
                            pass
                            # State 125269
                            if len(subjects) == 0:
                                pass
                                # 32: cosh(c + d*x**n)
                                yield 32, subst1
                subjects318.appendleft(tmp340)
            subjects.appendleft(tmp317)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp343 = subjects.popleft()
            subjects344 = deque(tmp343._args)
            # State 128145
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 128146
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 128147
                    if len(subjects344) >= 1 and isinstance(subjects344[0], Pow):
                        tmp347 = subjects344.popleft()
                        subjects348 = deque(tmp347._args)
                        # State 128148
                        if len(subjects348) >= 1:
                            tmp349 = subjects348.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0_1', tmp349)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 128149
                                if len(subjects348) >= 1:
                                    tmp351 = subjects348.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp351)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 128150
                                        if len(subjects348) == 0:
                                            pass
                                            # State 128151
                                            if len(subjects344) == 0:
                                                pass
                                                # State 128152
                                                if len(subjects) == 0:
                                                    pass
                                                    # 35: tanh(x**n*d + c)
                                                    yield 35, subst4
                                    subjects348.appendleft(tmp351)
                            subjects348.appendleft(tmp349)
                        subjects344.appendleft(tmp347)
                if len(subjects344) >= 1 and isinstance(subjects344[0], Mul):
                    tmp353 = subjects344.popleft()
                    associative1 = tmp353
                    associative_type1 = type(tmp353)
                    subjects354 = deque(tmp353._args)
                    matcher = CommutativeMatcher128154.get()
                    tmp355 = subjects354
                    subjects354 = []
                    for s in tmp355:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp355, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 128159
                            if len(subjects344) == 0:
                                pass
                                # State 128160
                                if len(subjects) == 0:
                                    pass
                                    # 35: tanh(x**n*d + c)
                                    yield 35, subst2
                    subjects344.appendleft(tmp353)
            if len(subjects344) >= 1:
                tmp356 = subjects344.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp356)
                except ValueError:
                    pass
                else:
                    pass
                    # State 128533
                    if len(subjects344) == 0:
                        pass
                        # State 128534
                        if len(subjects) == 0:
                            pass
                            # 37: tanh(v)
                            yield 37, subst1
                subjects344.appendleft(tmp356)
            if len(subjects344) >= 1 and isinstance(subjects344[0], Add):
                tmp358 = subjects344.popleft()
                associative1 = tmp358
                associative_type1 = type(tmp358)
                subjects359 = deque(tmp358._args)
                matcher = CommutativeMatcher128162.get()
                tmp360 = subjects359
                subjects359 = []
                for s in tmp360:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp360, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 128175
                        if len(subjects344) == 0:
                            pass
                            # State 128176
                            if len(subjects) == 0:
                                pass
                                # 35: tanh(x**n*d + c)
                                yield 35, subst1
                subjects344.appendleft(tmp358)
            subjects.appendleft(tmp343)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp361 = subjects.popleft()
            subjects362 = deque(tmp361._args)
            # State 138143
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138144
                if len(subjects362) >= 1:
                    tmp364 = subjects362.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp364)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138145
                        if len(subjects362) == 0:
                            pass
                            # State 138146
                            if len(subjects) == 0:
                                pass
                                # 43: asinh(x*c)
                                yield 43, subst2
                    subjects362.appendleft(tmp364)
            if len(subjects362) >= 1 and isinstance(subjects362[0], Mul):
                tmp366 = subjects362.popleft()
                associative1 = tmp366
                associative_type1 = type(tmp366)
                subjects367 = deque(tmp366._args)
                matcher = CommutativeMatcher138148.get()
                tmp368 = subjects367
                subjects367 = []
                for s in tmp368:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp368, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138149
                        if len(subjects362) == 0:
                            pass
                            # State 138150
                            if len(subjects) == 0:
                                pass
                                # 43: asinh(x*c)
                                yield 43, subst1
                subjects362.appendleft(tmp366)
            subjects.appendleft(tmp361)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp369 = subjects.popleft()
            subjects370 = deque(tmp369._args)
            # State 138218
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138219
                if len(subjects370) >= 1:
                    tmp372 = subjects370.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp372)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138220
                        if len(subjects370) == 0:
                            pass
                            # State 138221
                            if len(subjects) == 0:
                                pass
                                # 44: acosh(x*c)
                                yield 44, subst2
                    subjects370.appendleft(tmp372)
            if len(subjects370) >= 1 and isinstance(subjects370[0], Mul):
                tmp374 = subjects370.popleft()
                associative1 = tmp374
                associative_type1 = type(tmp374)
                subjects375 = deque(tmp374._args)
                matcher = CommutativeMatcher138223.get()
                tmp376 = subjects375
                subjects375 = []
                for s in tmp376:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp376, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138224
                        if len(subjects370) == 0:
                            pass
                            # State 138225
                            if len(subjects) == 0:
                                pass
                                # 44: acosh(x*c)
                                yield 44, subst1
                subjects370.appendleft(tmp374)
            subjects.appendleft(tmp369)
        return
        yield


from .generated_part006364 import *
from .generated_part006380 import *
from .generated_part006383 import *
from .generated_part006408 import *
from .generated_part006385 import *
from .generated_part006363 import *
from .generated_part006404 import *
from .generated_part006366 import *
from .generated_part006371 import *
from .generated_part006401 import *
from .generated_part006391 import *
from .generated_part006378 import *
from .generated_part006384 import *
from collections import deque
from .generated_part006374 import *
from .generated_part006388 import *
from .generated_part006402 import *
from matchpy.utils import VariableWithCount
from .generated_part006398 import *
from .generated_part006386 import *
from .generated_part006370 import *
from .generated_part006396 import *
from .generated_part006367 import *
from .generated_part006368 import *
from .generated_part006389 import *
from .generated_part006381 import *
from .generated_part006394 import *
from .generated_part006397 import *
from .generated_part006399 import *
from .generated_part006375 import *
from multiset import Multiset
from .generated_part006377 import *
from .generated_part006372 import *
from .generated_part006405 import *
from .generated_part006390 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part006362 import *
from .generated_part006393 import *
from .generated_part006407 import *