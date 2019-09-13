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

class CommutativeMatcher61383(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.2.0_1', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({6: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, None), Mul)
]),
    8: (8, Multiset({7: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher61383._instance is None:
            CommutativeMatcher61383._instance = CommutativeMatcher61383()
        return CommutativeMatcher61383._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 61382
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 61384
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 61385
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61386
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61387
                            if len(subjects2) == 0:
                                pass
                                # State 61388
                                if len(subjects) == 0:
                                    pass
                                    # 0: sin(e + x*f)
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp7 = subjects2.popleft()
                    associative1 = tmp7
                    associative_type1 = type(tmp7)
                    subjects8 = deque(tmp7._args)
                    matcher = CommutativeMatcher61390.get()
                    tmp9 = subjects8
                    subjects8 = []
                    for s in tmp9:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp9, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 61391
                            if len(subjects2) == 0:
                                pass
                                # State 61392
                                if len(subjects) == 0:
                                    pass
                                    # 0: sin(e + x*f)
                    subjects2.appendleft(tmp7)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp10 = subjects2.popleft()
                associative1 = tmp10
                associative_type1 = type(tmp10)
                subjects11 = deque(tmp10._args)
                matcher = CommutativeMatcher61394.get()
                tmp12 = subjects11
                subjects11 = []
                for s in tmp12:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp12, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 61400
                        if len(subjects2) == 0:
                            pass
                            # State 61401
                            if len(subjects) == 0:
                                pass
                                # 0: sin(e + x*f)
                subjects2.appendleft(tmp10)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp13 = subjects.popleft()
            subjects14 = deque(tmp13._args)
            # State 61616
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 61617
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61618
                    if len(subjects14) >= 1:
                        tmp17 = subjects14.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp17)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61619
                            if len(subjects14) == 0:
                                pass
                                # State 61620
                                if len(subjects) == 0:
                                    pass
                                    # 1: cos(e + x*f)
                        subjects14.appendleft(tmp17)
                if len(subjects14) >= 1 and isinstance(subjects14[0], Mul):
                    tmp19 = subjects14.popleft()
                    associative1 = tmp19
                    associative_type1 = type(tmp19)
                    subjects20 = deque(tmp19._args)
                    matcher = CommutativeMatcher61622.get()
                    tmp21 = subjects20
                    subjects20 = []
                    for s in tmp21:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp21, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 61623
                            if len(subjects14) == 0:
                                pass
                                # State 61624
                                if len(subjects) == 0:
                                    pass
                                    # 1: cos(e + x*f)
                    subjects14.appendleft(tmp19)
            if len(subjects14) >= 1 and isinstance(subjects14[0], Add):
                tmp22 = subjects14.popleft()
                associative1 = tmp22
                associative_type1 = type(tmp22)
                subjects23 = deque(tmp22._args)
                matcher = CommutativeMatcher61626.get()
                tmp24 = subjects23
                subjects23 = []
                for s in tmp24:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp24, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 61632
                        if len(subjects14) == 0:
                            pass
                            # State 61633
                            if len(subjects) == 0:
                                pass
                                # 1: cos(e + x*f)
                subjects14.appendleft(tmp22)
            subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp25 = subjects.popleft()
            subjects26 = deque(tmp25._args)
            # State 76829
            if len(subjects26) >= 1 and isinstance(subjects26[0], cos):
                tmp27 = subjects26.popleft()
                subjects28 = deque(tmp27._args)
                # State 76830
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76831
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 76832
                        if len(subjects28) >= 1:
                            tmp31 = subjects28.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp31)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 76833
                                if len(subjects28) == 0:
                                    pass
                                    # State 76834
                                    if len(subjects26) >= 1 and subjects26[0] == -1:
                                        tmp33 = subjects26.popleft()
                                        # State 76835
                                        if len(subjects26) == 0:
                                            pass
                                            # State 76836
                                            if len(subjects) == 0:
                                                pass
                                                # 2: 1/cos(e + x*f)
                                        subjects26.appendleft(tmp33)
                            subjects28.appendleft(tmp31)
                    if len(subjects28) >= 1 and isinstance(subjects28[0], Mul):
                        tmp34 = subjects28.popleft()
                        associative1 = tmp34
                        associative_type1 = type(tmp34)
                        subjects35 = deque(tmp34._args)
                        matcher = CommutativeMatcher76838.get()
                        tmp36 = subjects35
                        subjects35 = []
                        for s in tmp36:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp36, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 76839
                                if len(subjects28) == 0:
                                    pass
                                    # State 76840
                                    if len(subjects26) >= 1 and subjects26[0] == -1:
                                        tmp37 = subjects26.popleft()
                                        # State 76841
                                        if len(subjects26) == 0:
                                            pass
                                            # State 76842
                                            if len(subjects) == 0:
                                                pass
                                                # 2: 1/cos(e + x*f)
                                        subjects26.appendleft(tmp37)
                        subjects28.appendleft(tmp34)
                if len(subjects28) >= 1 and isinstance(subjects28[0], Add):
                    tmp38 = subjects28.popleft()
                    associative1 = tmp38
                    associative_type1 = type(tmp38)
                    subjects39 = deque(tmp38._args)
                    matcher = CommutativeMatcher76844.get()
                    tmp40 = subjects39
                    subjects39 = []
                    for s in tmp40:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp40, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 76850
                            if len(subjects28) == 0:
                                pass
                                # State 76851
                                if len(subjects26) >= 1 and subjects26[0] == -1:
                                    tmp41 = subjects26.popleft()
                                    # State 76852
                                    if len(subjects26) == 0:
                                        pass
                                        # State 76853
                                        if len(subjects) == 0:
                                            pass
                                            # 2: 1/cos(e + x*f)
                                    subjects26.appendleft(tmp41)
                    subjects28.appendleft(tmp38)
                subjects26.appendleft(tmp27)
            if len(subjects26) >= 1 and isinstance(subjects26[0], sin):
                tmp42 = subjects26.popleft()
                subjects43 = deque(tmp42._args)
                # State 77110
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 77111
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 77112
                        if len(subjects43) >= 1:
                            tmp46 = subjects43.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp46)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 77113
                                if len(subjects43) == 0:
                                    pass
                                    # State 77114
                                    if len(subjects26) >= 1 and subjects26[0] == -1:
                                        tmp48 = subjects26.popleft()
                                        # State 77115
                                        if len(subjects26) == 0:
                                            pass
                                            # State 77116
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/sin(e + x*f)
                                        subjects26.appendleft(tmp48)
                            subjects43.appendleft(tmp46)
                    if len(subjects43) >= 1 and isinstance(subjects43[0], Mul):
                        tmp49 = subjects43.popleft()
                        associative1 = tmp49
                        associative_type1 = type(tmp49)
                        subjects50 = deque(tmp49._args)
                        matcher = CommutativeMatcher77118.get()
                        tmp51 = subjects50
                        subjects50 = []
                        for s in tmp51:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp51, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 77119
                                if len(subjects43) == 0:
                                    pass
                                    # State 77120
                                    if len(subjects26) >= 1 and subjects26[0] == -1:
                                        tmp52 = subjects26.popleft()
                                        # State 77121
                                        if len(subjects26) == 0:
                                            pass
                                            # State 77122
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/sin(e + x*f)
                                        subjects26.appendleft(tmp52)
                        subjects43.appendleft(tmp49)
                if len(subjects43) >= 1 and isinstance(subjects43[0], Add):
                    tmp53 = subjects43.popleft()
                    associative1 = tmp53
                    associative_type1 = type(tmp53)
                    subjects54 = deque(tmp53._args)
                    matcher = CommutativeMatcher77124.get()
                    tmp55 = subjects54
                    subjects54 = []
                    for s in tmp55:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp55, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 77130
                            if len(subjects43) == 0:
                                pass
                                # State 77131
                                if len(subjects26) >= 1 and subjects26[0] == -1:
                                    tmp56 = subjects26.popleft()
                                    # State 77132
                                    if len(subjects26) == 0:
                                        pass
                                        # State 77133
                                        if len(subjects) == 0:
                                            pass
                                            # 3: 1/sin(e + x*f)
                                    subjects26.appendleft(tmp56)
                    subjects43.appendleft(tmp53)
                subjects26.appendleft(tmp42)
            if len(subjects26) >= 1 and isinstance(subjects26[0], tan):
                tmp57 = subjects26.popleft()
                subjects58 = deque(tmp57._args)
                # State 80199
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80200
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80201
                        if len(subjects58) >= 1:
                            tmp61 = subjects58.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp61)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80202
                                if len(subjects58) == 0:
                                    pass
                                    # State 80203
                                    if len(subjects26) >= 1 and subjects26[0] == -1:
                                        tmp63 = subjects26.popleft()
                                        # State 80204
                                        if len(subjects26) == 0:
                                            pass
                                            # State 80205
                                            if len(subjects) == 0:
                                                pass
                                                # 5: 1/tan(e + x*f)
                                        subjects26.appendleft(tmp63)
                            subjects58.appendleft(tmp61)
                    if len(subjects58) >= 1 and isinstance(subjects58[0], Mul):
                        tmp64 = subjects58.popleft()
                        associative1 = tmp64
                        associative_type1 = type(tmp64)
                        subjects65 = deque(tmp64._args)
                        matcher = CommutativeMatcher80207.get()
                        tmp66 = subjects65
                        subjects65 = []
                        for s in tmp66:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp66, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80208
                                if len(subjects58) == 0:
                                    pass
                                    # State 80209
                                    if len(subjects26) >= 1 and subjects26[0] == -1:
                                        tmp67 = subjects26.popleft()
                                        # State 80210
                                        if len(subjects26) == 0:
                                            pass
                                            # State 80211
                                            if len(subjects) == 0:
                                                pass
                                                # 5: 1/tan(e + x*f)
                                        subjects26.appendleft(tmp67)
                        subjects58.appendleft(tmp64)
                if len(subjects58) >= 1 and isinstance(subjects58[0], Add):
                    tmp68 = subjects58.popleft()
                    associative1 = tmp68
                    associative_type1 = type(tmp68)
                    subjects69 = deque(tmp68._args)
                    matcher = CommutativeMatcher80213.get()
                    tmp70 = subjects69
                    subjects69 = []
                    for s in tmp70:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp70, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 80219
                            if len(subjects58) == 0:
                                pass
                                # State 80220
                                if len(subjects26) >= 1 and subjects26[0] == -1:
                                    tmp71 = subjects26.popleft()
                                    # State 80221
                                    if len(subjects26) == 0:
                                        pass
                                        # State 80222
                                        if len(subjects) == 0:
                                            pass
                                            # 5: 1/tan(e + x*f)
                                    subjects26.appendleft(tmp71)
                    subjects58.appendleft(tmp68)
                subjects26.appendleft(tmp57)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 150758
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 150759
                    if len(subjects26) >= 1:
                        tmp74 = subjects26.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp74)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 150760
                            if len(subjects26) >= 1:
                                tmp76 = subjects26.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.2', tmp76)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150761
                                    if len(subjects26) == 0:
                                        pass
                                        # State 150762
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (a + x*b)**n
                                subjects26.appendleft(tmp76)
                        subjects26.appendleft(tmp74)
                if len(subjects26) >= 1 and isinstance(subjects26[0], Mul):
                    tmp78 = subjects26.popleft()
                    associative1 = tmp78
                    associative_type1 = type(tmp78)
                    subjects79 = deque(tmp78._args)
                    matcher = CommutativeMatcher150764.get()
                    tmp80 = subjects79
                    subjects79 = []
                    for s in tmp80:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp80, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 150765
                            if len(subjects26) >= 1:
                                tmp81 = []
                                tmp81.append(subjects26.popleft())
                                while True:
                                    if len(tmp81) > 1:
                                        tmp82 = create_operation_expression(associative1, tmp81)
                                    elif len(tmp81) == 1:
                                        tmp82 = tmp81[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.2.2', tmp82)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 150766
                                        if len(subjects26) == 0:
                                            pass
                                            # State 150767
                                            if len(subjects) == 0:
                                                pass
                                                # 7: (a + x*b)**n
                                    if len(subjects26) == 0:
                                        break
                                    tmp81.append(subjects26.popleft())
                                subjects26.extendleft(reversed(tmp81))
                    subjects26.appendleft(tmp78)
            if len(subjects26) >= 1 and isinstance(subjects26[0], Add):
                tmp84 = subjects26.popleft()
                associative1 = tmp84
                associative_type1 = type(tmp84)
                subjects85 = deque(tmp84._args)
                matcher = CommutativeMatcher150769.get()
                tmp86 = subjects85
                subjects85 = []
                for s in tmp86:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp86, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 150775
                        if len(subjects26) >= 1:
                            tmp87 = []
                            tmp87.append(subjects26.popleft())
                            while True:
                                if len(tmp87) > 1:
                                    tmp88 = create_operation_expression(associative1, tmp87)
                                elif len(tmp87) == 1:
                                    tmp88 = tmp87[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2.2', tmp88)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150776
                                    if len(subjects26) == 0:
                                        pass
                                        # State 150777
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (a + x*b)**n
                                if len(subjects26) == 0:
                                    break
                                tmp87.append(subjects26.popleft())
                            subjects26.extendleft(reversed(tmp87))
                subjects26.appendleft(tmp84)
            subjects.appendleft(tmp25)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp90 = subjects.popleft()
            subjects91 = deque(tmp90._args)
            # State 79969
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 79970
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 79971
                    if len(subjects91) >= 1:
                        tmp94 = subjects91.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp94)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 79972
                            if len(subjects91) == 0:
                                pass
                                # State 79973
                                if len(subjects) == 0:
                                    pass
                                    # 4: tan(e + x*f)
                        subjects91.appendleft(tmp94)
                if len(subjects91) >= 1 and isinstance(subjects91[0], Mul):
                    tmp96 = subjects91.popleft()
                    associative1 = tmp96
                    associative_type1 = type(tmp96)
                    subjects97 = deque(tmp96._args)
                    matcher = CommutativeMatcher79975.get()
                    tmp98 = subjects97
                    subjects97 = []
                    for s in tmp98:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp98, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 79976
                            if len(subjects91) == 0:
                                pass
                                # State 79977
                                if len(subjects) == 0:
                                    pass
                                    # 4: tan(e + x*f)
                    subjects91.appendleft(tmp96)
            if len(subjects91) >= 1 and isinstance(subjects91[0], Add):
                tmp99 = subjects91.popleft()
                associative1 = tmp99
                associative_type1 = type(tmp99)
                subjects100 = deque(tmp99._args)
                matcher = CommutativeMatcher79979.get()
                tmp101 = subjects100
                subjects100 = []
                for s in tmp101:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp101, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 79985
                        if len(subjects91) == 0:
                            pass
                            # State 79986
                            if len(subjects) == 0:
                                pass
                                # 4: tan(e + x*f)
                subjects91.appendleft(tmp99)
            subjects.appendleft(tmp90)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 102471
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.2.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 102472
                if len(subjects) >= 1:
                    tmp104 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.1.1.0', tmp104)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102473
                        if len(subjects) == 0:
                            pass
                            # 6: c + x*d
                    subjects.appendleft(tmp104)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp106 = subjects.popleft()
                associative1 = tmp106
                associative_type1 = type(tmp106)
                subjects107 = deque(tmp106._args)
                matcher = CommutativeMatcher102475.get()
                tmp108 = subjects107
                subjects107 = []
                for s in tmp108:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp108, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 102476
                        if len(subjects) == 0:
                            pass
                            # 6: c + x*d
                subjects.appendleft(tmp106)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp109 = subjects.popleft()
            associative1 = tmp109
            associative_type1 = type(tmp109)
            subjects110 = deque(tmp109._args)
            matcher = CommutativeMatcher102478.get()
            tmp111 = subjects110
            subjects110 = []
            for s in tmp111:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp111, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 102484
                    if len(subjects) == 0:
                        pass
                        # 6: c + x*d
            subjects.appendleft(tmp109)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
