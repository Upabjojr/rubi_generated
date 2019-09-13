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

class CommutativeMatcher10176(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher10176._instance is None:
            CommutativeMatcher10176._instance = CommutativeMatcher10176()
        return CommutativeMatcher10176._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 10175
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 10177
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 10178
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10179
                            if len(subjects2) == 0:
                                pass
                                # State 10180
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects2.appendleft(tmp5)
                    if len(subjects2) >= 1 and subjects2[0] == -1:
                        tmp7 = subjects2.popleft()
                        # State 10674
                        if len(subjects2) == 0:
                            pass
                            # State 10675
                            if len(subjects) == 0:
                                pass
                                # 1: 1/x
                        subjects2.appendleft(tmp7)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp8 = subjects2.popleft()
                subjects9 = deque(tmp8._args)
                # State 83060
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 83061
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83062
                        if len(subjects9) >= 1:
                            tmp12 = subjects9.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.0', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83063
                                if len(subjects9) == 0:
                                    pass
                                    # State 83064
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp14 = subjects2.popleft()
                                        # State 83065
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83066
                                            if len(subjects) == 0:
                                                pass
                                                # 7: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp14)
                            subjects9.appendleft(tmp12)
                    if len(subjects9) >= 1 and isinstance(subjects9[0], Mul):
                        tmp15 = subjects9.popleft()
                        associative1 = tmp15
                        associative_type1 = type(tmp15)
                        subjects16 = deque(tmp15._args)
                        matcher = CommutativeMatcher83068.get()
                        tmp17 = subjects16
                        subjects16 = []
                        for s in tmp17:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp17, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83069
                                if len(subjects9) == 0:
                                    pass
                                    # State 83070
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp18 = subjects2.popleft()
                                        # State 83071
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83072
                                            if len(subjects) == 0:
                                                pass
                                                # 7: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp18)
                        subjects9.appendleft(tmp15)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 85489
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 85490
                        if len(subjects9) >= 1:
                            tmp21 = subjects9.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.3.1.0', tmp21)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 85491
                                if len(subjects9) == 0:
                                    pass
                                    # State 85492
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp23 = subjects2.popleft()
                                        # State 85493
                                        if len(subjects2) == 0:
                                            pass
                                            # State 85494
                                            if len(subjects) == 0:
                                                pass
                                                # 9: 1/tan(c + x*d)
                                        subjects2.appendleft(tmp23)
                            subjects9.appendleft(tmp21)
                    if len(subjects9) >= 1 and isinstance(subjects9[0], Mul):
                        tmp24 = subjects9.popleft()
                        associative1 = tmp24
                        associative_type1 = type(tmp24)
                        subjects25 = deque(tmp24._args)
                        matcher = CommutativeMatcher85496.get()
                        tmp26 = subjects25
                        subjects25 = []
                        for s in tmp26:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp26, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 85497
                                if len(subjects9) == 0:
                                    pass
                                    # State 85498
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp27 = subjects2.popleft()
                                        # State 85499
                                        if len(subjects2) == 0:
                                            pass
                                            # State 85500
                                            if len(subjects) == 0:
                                                pass
                                                # 9: 1/tan(c + x*d)
                                        subjects2.appendleft(tmp27)
                        subjects9.appendleft(tmp24)
                if len(subjects9) >= 1 and isinstance(subjects9[0], Add):
                    tmp28 = subjects9.popleft()
                    associative1 = tmp28
                    associative_type1 = type(tmp28)
                    subjects29 = deque(tmp28._args)
                    matcher = CommutativeMatcher83074.get()
                    tmp30 = subjects29
                    subjects29 = []
                    for s in tmp30:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp30, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 83080
                            if len(subjects9) == 0:
                                pass
                                # State 83081
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp31 = subjects2.popleft()
                                    # State 83082
                                    if len(subjects2) == 0:
                                        pass
                                        # State 83083
                                        if len(subjects) == 0:
                                            pass
                                            # 7: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp31)
                        if pattern_index == 1:
                            pass
                            # State 85504
                            if len(subjects9) == 0:
                                pass
                                # State 85505
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp32 = subjects2.popleft()
                                    # State 85506
                                    if len(subjects2) == 0:
                                        pass
                                        # State 85507
                                        if len(subjects) == 0:
                                            pass
                                            # 9: 1/tan(c + x*d)
                                    subjects2.appendleft(tmp32)
                    subjects9.appendleft(tmp28)
                subjects2.appendleft(tmp8)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp33 = subjects.popleft()
            subjects34 = deque(tmp33._args)
            # State 68058
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 68059
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68060
                    if len(subjects34) >= 1:
                        tmp37 = subjects34.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp37)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68061
                            if len(subjects34) == 0:
                                pass
                                # State 68062
                                if len(subjects) == 0:
                                    pass
                                    # 2: sin(c + x*d)
                        subjects34.appendleft(tmp37)
                if len(subjects34) >= 1 and isinstance(subjects34[0], Mul):
                    tmp39 = subjects34.popleft()
                    associative1 = tmp39
                    associative_type1 = type(tmp39)
                    subjects40 = deque(tmp39._args)
                    matcher = CommutativeMatcher68064.get()
                    tmp41 = subjects40
                    subjects40 = []
                    for s in tmp41:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp41, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 68065
                            if len(subjects34) == 0:
                                pass
                                # State 68066
                                if len(subjects) == 0:
                                    pass
                                    # 2: sin(c + x*d)
                    subjects34.appendleft(tmp39)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 71311
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 71312
                    if len(subjects34) >= 1:
                        tmp44 = subjects34.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp44)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 71313
                            if len(subjects34) == 0:
                                pass
                                # State 71314
                                if len(subjects) == 0:
                                    pass
                                    # 5: sin(e + x*f)
                        subjects34.appendleft(tmp44)
                if len(subjects34) >= 1 and isinstance(subjects34[0], Mul):
                    tmp46 = subjects34.popleft()
                    associative1 = tmp46
                    associative_type1 = type(tmp46)
                    subjects47 = deque(tmp46._args)
                    matcher = CommutativeMatcher71316.get()
                    tmp48 = subjects47
                    subjects47 = []
                    for s in tmp48:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp48, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 71317
                            if len(subjects34) == 0:
                                pass
                                # State 71318
                                if len(subjects) == 0:
                                    pass
                                    # 5: sin(e + x*f)
                    subjects34.appendleft(tmp46)
            if len(subjects34) >= 1 and isinstance(subjects34[0], Add):
                tmp49 = subjects34.popleft()
                associative1 = tmp49
                associative_type1 = type(tmp49)
                subjects50 = deque(tmp49._args)
                matcher = CommutativeMatcher68068.get()
                tmp51 = subjects50
                subjects50 = []
                for s in tmp51:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp51, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 68074
                        if len(subjects34) == 0:
                            pass
                            # State 68075
                            if len(subjects) == 0:
                                pass
                                # 2: sin(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 71322
                        if len(subjects34) == 0:
                            pass
                            # State 71323
                            if len(subjects) == 0:
                                pass
                                # 5: sin(e + x*f)
                subjects34.appendleft(tmp49)
            subjects.appendleft(tmp33)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp52 = subjects.popleft()
            subjects53 = deque(tmp52._args)
            # State 68279
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 68280
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68281
                    if len(subjects53) >= 1:
                        tmp56 = subjects53.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp56)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68282
                            if len(subjects53) == 0:
                                pass
                                # State 68283
                                if len(subjects) == 0:
                                    pass
                                    # 3: cos(c + x*d)
                        subjects53.appendleft(tmp56)
                if len(subjects53) >= 1 and isinstance(subjects53[0], Mul):
                    tmp58 = subjects53.popleft()
                    associative1 = tmp58
                    associative_type1 = type(tmp58)
                    subjects59 = deque(tmp58._args)
                    matcher = CommutativeMatcher68285.get()
                    tmp60 = subjects59
                    subjects59 = []
                    for s in tmp60:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp60, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 68286
                            if len(subjects53) == 0:
                                pass
                                # State 68287
                                if len(subjects) == 0:
                                    pass
                                    # 3: cos(c + x*d)
                    subjects53.appendleft(tmp58)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 68520
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68521
                    if len(subjects53) >= 1:
                        tmp63 = subjects53.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp63)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68522
                            if len(subjects53) == 0:
                                pass
                                # State 68523
                                if len(subjects) == 0:
                                    pass
                                    # 4: cos(e + x*f)
                        subjects53.appendleft(tmp63)
                if len(subjects53) >= 1 and isinstance(subjects53[0], Mul):
                    tmp65 = subjects53.popleft()
                    associative1 = tmp65
                    associative_type1 = type(tmp65)
                    subjects66 = deque(tmp65._args)
                    matcher = CommutativeMatcher68525.get()
                    tmp67 = subjects66
                    subjects66 = []
                    for s in tmp67:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp67, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 68526
                            if len(subjects53) == 0:
                                pass
                                # State 68527
                                if len(subjects) == 0:
                                    pass
                                    # 4: cos(e + x*f)
                    subjects53.appendleft(tmp65)
            if len(subjects53) >= 1 and isinstance(subjects53[0], Add):
                tmp68 = subjects53.popleft()
                associative1 = tmp68
                associative_type1 = type(tmp68)
                subjects69 = deque(tmp68._args)
                matcher = CommutativeMatcher68289.get()
                tmp70 = subjects69
                subjects69 = []
                for s in tmp70:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp70, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 68295
                        if len(subjects53) == 0:
                            pass
                            # State 68296
                            if len(subjects) == 0:
                                pass
                                # 3: cos(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 68531
                        if len(subjects53) == 0:
                            pass
                            # State 68532
                            if len(subjects) == 0:
                                pass
                                # 4: cos(e + x*f)
                subjects53.appendleft(tmp68)
            subjects.appendleft(tmp52)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp71 = subjects.popleft()
            subjects72 = deque(tmp71._args)
            # State 82873
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 82874
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 82875
                    if len(subjects72) >= 1:
                        tmp75 = subjects72.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp75)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 82876
                            if len(subjects72) == 0:
                                pass
                                # State 82877
                                if len(subjects) == 0:
                                    pass
                                    # 6: tan(e + x*f)
                        subjects72.appendleft(tmp75)
                if len(subjects72) >= 1 and isinstance(subjects72[0], Mul):
                    tmp77 = subjects72.popleft()
                    associative1 = tmp77
                    associative_type1 = type(tmp77)
                    subjects78 = deque(tmp77._args)
                    matcher = CommutativeMatcher82879.get()
                    tmp79 = subjects78
                    subjects78 = []
                    for s in tmp79:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp79, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 82880
                            if len(subjects72) == 0:
                                pass
                                # State 82881
                                if len(subjects) == 0:
                                    pass
                                    # 6: tan(e + x*f)
                    subjects72.appendleft(tmp77)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 85158
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 85159
                    if len(subjects72) >= 1:
                        tmp82 = subjects72.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp82)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 85160
                            if len(subjects72) == 0:
                                pass
                                # State 85161
                                if len(subjects) == 0:
                                    pass
                                    # 8: tan(c + x*d)
                        subjects72.appendleft(tmp82)
                if len(subjects72) >= 1 and isinstance(subjects72[0], Mul):
                    tmp84 = subjects72.popleft()
                    associative1 = tmp84
                    associative_type1 = type(tmp84)
                    subjects85 = deque(tmp84._args)
                    matcher = CommutativeMatcher85163.get()
                    tmp86 = subjects85
                    subjects85 = []
                    for s in tmp86:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp86, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 85164
                            if len(subjects72) == 0:
                                pass
                                # State 85165
                                if len(subjects) == 0:
                                    pass
                                    # 8: tan(c + x*d)
                    subjects72.appendleft(tmp84)
            if len(subjects72) >= 1 and isinstance(subjects72[0], Add):
                tmp87 = subjects72.popleft()
                associative1 = tmp87
                associative_type1 = type(tmp87)
                subjects88 = deque(tmp87._args)
                matcher = CommutativeMatcher82883.get()
                tmp89 = subjects88
                subjects88 = []
                for s in tmp89:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp89, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 82889
                        if len(subjects72) == 0:
                            pass
                            # State 82890
                            if len(subjects) == 0:
                                pass
                                # 6: tan(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 85169
                        if len(subjects72) == 0:
                            pass
                            # State 85170
                            if len(subjects) == 0:
                                pass
                                # 8: tan(c + x*d)
                subjects72.appendleft(tmp87)
            subjects.appendleft(tmp71)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
