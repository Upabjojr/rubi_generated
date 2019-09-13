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

class CommutativeMatcher61433(CommutativeMatcher):
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
        if CommutativeMatcher61433._instance is None:
            CommutativeMatcher61433._instance = CommutativeMatcher61433()
        return CommutativeMatcher61433._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 61432
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 61434
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 61435
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61436
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61437
                            if len(subjects2) == 0:
                                pass
                                # State 61438
                                if len(subjects) == 0:
                                    pass
                                    # 0: sin(e + x*f)
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp7 = subjects2.popleft()
                    associative1 = tmp7
                    associative_type1 = type(tmp7)
                    subjects8 = deque(tmp7._args)
                    matcher = CommutativeMatcher61440.get()
                    tmp9 = subjects8
                    subjects8 = []
                    for s in tmp9:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp9, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 61441
                            if len(subjects2) == 0:
                                pass
                                # State 61442
                                if len(subjects) == 0:
                                    pass
                                    # 0: sin(e + x*f)
                    subjects2.appendleft(tmp7)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp10 = subjects2.popleft()
                associative1 = tmp10
                associative_type1 = type(tmp10)
                subjects11 = deque(tmp10._args)
                matcher = CommutativeMatcher61444.get()
                tmp12 = subjects11
                subjects11 = []
                for s in tmp12:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp12, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 61450
                        if len(subjects2) == 0:
                            pass
                            # State 61451
                            if len(subjects) == 0:
                                pass
                                # 0: sin(e + x*f)
                subjects2.appendleft(tmp10)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp13 = subjects.popleft()
            subjects14 = deque(tmp13._args)
            # State 61663
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 61664
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61665
                    if len(subjects14) >= 1:
                        tmp17 = subjects14.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp17)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61666
                            if len(subjects14) == 0:
                                pass
                                # State 61667
                                if len(subjects) == 0:
                                    pass
                                    # 1: cos(e + x*f)
                        subjects14.appendleft(tmp17)
                if len(subjects14) >= 1 and isinstance(subjects14[0], Mul):
                    tmp19 = subjects14.popleft()
                    associative1 = tmp19
                    associative_type1 = type(tmp19)
                    subjects20 = deque(tmp19._args)
                    matcher = CommutativeMatcher61669.get()
                    tmp21 = subjects20
                    subjects20 = []
                    for s in tmp21:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp21, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 61670
                            if len(subjects14) == 0:
                                pass
                                # State 61671
                                if len(subjects) == 0:
                                    pass
                                    # 1: cos(e + x*f)
                    subjects14.appendleft(tmp19)
            if len(subjects14) >= 1 and isinstance(subjects14[0], Add):
                tmp22 = subjects14.popleft()
                associative1 = tmp22
                associative_type1 = type(tmp22)
                subjects23 = deque(tmp22._args)
                matcher = CommutativeMatcher61673.get()
                tmp24 = subjects23
                subjects23 = []
                for s in tmp24:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp24, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 61679
                        if len(subjects14) == 0:
                            pass
                            # State 61680
                            if len(subjects) == 0:
                                pass
                                # 1: cos(e + x*f)
                subjects14.appendleft(tmp22)
            subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp25 = subjects.popleft()
            subjects26 = deque(tmp25._args)
            # State 76890
            if len(subjects26) >= 1 and isinstance(subjects26[0], cos):
                tmp27 = subjects26.popleft()
                subjects28 = deque(tmp27._args)
                # State 76891
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76892
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 76893
                        if len(subjects28) >= 1:
                            tmp31 = subjects28.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp31)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 76894
                                if len(subjects28) == 0:
                                    pass
                                    # State 76895
                                    if len(subjects26) >= 1 and subjects26[0] == -1:
                                        tmp33 = subjects26.popleft()
                                        # State 76896
                                        if len(subjects26) == 0:
                                            pass
                                            # State 76897
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
                        matcher = CommutativeMatcher76899.get()
                        tmp36 = subjects35
                        subjects35 = []
                        for s in tmp36:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp36, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 76900
                                if len(subjects28) == 0:
                                    pass
                                    # State 76901
                                    if len(subjects26) >= 1 and subjects26[0] == -1:
                                        tmp37 = subjects26.popleft()
                                        # State 76902
                                        if len(subjects26) == 0:
                                            pass
                                            # State 76903
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
                    matcher = CommutativeMatcher76905.get()
                    tmp40 = subjects39
                    subjects39 = []
                    for s in tmp40:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp40, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 76911
                            if len(subjects28) == 0:
                                pass
                                # State 76912
                                if len(subjects26) >= 1 and subjects26[0] == -1:
                                    tmp41 = subjects26.popleft()
                                    # State 76913
                                    if len(subjects26) == 0:
                                        pass
                                        # State 76914
                                        if len(subjects) == 0:
                                            pass
                                            # 2: 1/cos(e + x*f)
                                    subjects26.appendleft(tmp41)
                    subjects28.appendleft(tmp38)
                subjects26.appendleft(tmp27)
            if len(subjects26) >= 1 and isinstance(subjects26[0], sin):
                tmp42 = subjects26.popleft()
                subjects43 = deque(tmp42._args)
                # State 77169
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 77170
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 77171
                        if len(subjects43) >= 1:
                            tmp46 = subjects43.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp46)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 77172
                                if len(subjects43) == 0:
                                    pass
                                    # State 77173
                                    if len(subjects26) >= 1 and subjects26[0] == -1:
                                        tmp48 = subjects26.popleft()
                                        # State 77174
                                        if len(subjects26) == 0:
                                            pass
                                            # State 77175
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
                        matcher = CommutativeMatcher77177.get()
                        tmp51 = subjects50
                        subjects50 = []
                        for s in tmp51:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp51, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 77178
                                if len(subjects43) == 0:
                                    pass
                                    # State 77179
                                    if len(subjects26) >= 1 and subjects26[0] == -1:
                                        tmp52 = subjects26.popleft()
                                        # State 77180
                                        if len(subjects26) == 0:
                                            pass
                                            # State 77181
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
                    matcher = CommutativeMatcher77183.get()
                    tmp55 = subjects54
                    subjects54 = []
                    for s in tmp55:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp55, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 77189
                            if len(subjects43) == 0:
                                pass
                                # State 77190
                                if len(subjects26) >= 1 and subjects26[0] == -1:
                                    tmp56 = subjects26.popleft()
                                    # State 77191
                                    if len(subjects26) == 0:
                                        pass
                                        # State 77192
                                        if len(subjects) == 0:
                                            pass
                                            # 3: 1/sin(e + x*f)
                                    subjects26.appendleft(tmp56)
                    subjects43.appendleft(tmp53)
                subjects26.appendleft(tmp42)
            if len(subjects26) >= 1 and isinstance(subjects26[0], tan):
                tmp57 = subjects26.popleft()
                subjects58 = deque(tmp57._args)
                # State 80258
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80259
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80260
                        if len(subjects58) >= 1:
                            tmp61 = subjects58.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp61)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80261
                                if len(subjects58) == 0:
                                    pass
                                    # State 80262
                                    if len(subjects26) >= 1 and subjects26[0] == -1:
                                        tmp63 = subjects26.popleft()
                                        # State 80263
                                        if len(subjects26) == 0:
                                            pass
                                            # State 80264
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
                        matcher = CommutativeMatcher80266.get()
                        tmp66 = subjects65
                        subjects65 = []
                        for s in tmp66:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp66, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80267
                                if len(subjects58) == 0:
                                    pass
                                    # State 80268
                                    if len(subjects26) >= 1 and subjects26[0] == -1:
                                        tmp67 = subjects26.popleft()
                                        # State 80269
                                        if len(subjects26) == 0:
                                            pass
                                            # State 80270
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
                    matcher = CommutativeMatcher80272.get()
                    tmp70 = subjects69
                    subjects69 = []
                    for s in tmp70:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp70, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 80278
                            if len(subjects58) == 0:
                                pass
                                # State 80279
                                if len(subjects26) >= 1 and subjects26[0] == -1:
                                    tmp71 = subjects26.popleft()
                                    # State 80280
                                    if len(subjects26) == 0:
                                        pass
                                        # State 80281
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
                # State 150809
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 150810
                    if len(subjects26) >= 1:
                        tmp74 = subjects26.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp74)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 150811
                            if len(subjects26) >= 1:
                                tmp76 = subjects26.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.2', tmp76)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150812
                                    if len(subjects26) == 0:
                                        pass
                                        # State 150813
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
                    matcher = CommutativeMatcher150815.get()
                    tmp80 = subjects79
                    subjects79 = []
                    for s in tmp80:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp80, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 150816
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
                                        # State 150817
                                        if len(subjects26) == 0:
                                            pass
                                            # State 150818
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
                matcher = CommutativeMatcher150820.get()
                tmp86 = subjects85
                subjects85 = []
                for s in tmp86:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp86, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 150826
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
                                    # State 150827
                                    if len(subjects26) == 0:
                                        pass
                                        # State 150828
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
            # State 80016
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 80017
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80018
                    if len(subjects91) >= 1:
                        tmp94 = subjects91.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp94)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 80019
                            if len(subjects91) == 0:
                                pass
                                # State 80020
                                if len(subjects) == 0:
                                    pass
                                    # 4: tan(e + x*f)
                        subjects91.appendleft(tmp94)
                if len(subjects91) >= 1 and isinstance(subjects91[0], Mul):
                    tmp96 = subjects91.popleft()
                    associative1 = tmp96
                    associative_type1 = type(tmp96)
                    subjects97 = deque(tmp96._args)
                    matcher = CommutativeMatcher80022.get()
                    tmp98 = subjects97
                    subjects97 = []
                    for s in tmp98:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp98, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 80023
                            if len(subjects91) == 0:
                                pass
                                # State 80024
                                if len(subjects) == 0:
                                    pass
                                    # 4: tan(e + x*f)
                    subjects91.appendleft(tmp96)
            if len(subjects91) >= 1 and isinstance(subjects91[0], Add):
                tmp99 = subjects91.popleft()
                associative1 = tmp99
                associative_type1 = type(tmp99)
                subjects100 = deque(tmp99._args)
                matcher = CommutativeMatcher80026.get()
                tmp101 = subjects100
                subjects100 = []
                for s in tmp101:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp101, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 80032
                        if len(subjects91) == 0:
                            pass
                            # State 80033
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
            # State 102490
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.2.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 102491
                if len(subjects) >= 1:
                    tmp104 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.2.1.1.0', tmp104)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102492
                        if len(subjects) == 0:
                            pass
                            # 6: c + x*d
                    subjects.appendleft(tmp104)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp106 = subjects.popleft()
                associative1 = tmp106
                associative_type1 = type(tmp106)
                subjects107 = deque(tmp106._args)
                matcher = CommutativeMatcher102494.get()
                tmp108 = subjects107
                subjects107 = []
                for s in tmp108:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp108, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 102495
                        if len(subjects) == 0:
                            pass
                            # 6: c + x*d
                subjects.appendleft(tmp106)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp109 = subjects.popleft()
            associative1 = tmp109
            associative_type1 = type(tmp109)
            subjects110 = deque(tmp109._args)
            matcher = CommutativeMatcher102497.get()
            tmp111 = subjects110
            subjects110 = []
            for s in tmp111:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp111, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 102503
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
