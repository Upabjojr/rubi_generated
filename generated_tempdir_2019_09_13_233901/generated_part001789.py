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

class CommutativeMatcher10160(CommutativeMatcher):
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
        if CommutativeMatcher10160._instance is None:
            CommutativeMatcher10160._instance = CommutativeMatcher10160()
        return CommutativeMatcher10160._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 10159
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 10161
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 10162
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10163
                            if len(subjects2) == 0:
                                pass
                                # State 10164
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects2.appendleft(tmp5)
                    if len(subjects2) >= 1 and subjects2[0] == -1:
                        tmp7 = subjects2.popleft()
                        # State 10665
                        if len(subjects2) == 0:
                            pass
                            # State 10666
                            if len(subjects) == 0:
                                pass
                                # 1: 1/x
                        subjects2.appendleft(tmp7)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp8 = subjects2.popleft()
                subjects9 = deque(tmp8._args)
                # State 83003
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 83004
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83005
                        if len(subjects9) >= 1:
                            tmp12 = subjects9.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.0', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83006
                                if len(subjects9) == 0:
                                    pass
                                    # State 83007
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp14 = subjects2.popleft()
                                        # State 83008
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83009
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
                        matcher = CommutativeMatcher83011.get()
                        tmp17 = subjects16
                        subjects16 = []
                        for s in tmp17:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp17, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83012
                                if len(subjects9) == 0:
                                    pass
                                    # State 83013
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp18 = subjects2.popleft()
                                        # State 83014
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83015
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
                    # State 85391
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 85392
                        if len(subjects9) >= 1:
                            tmp21 = subjects9.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.3.1.0', tmp21)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 85393
                                if len(subjects9) == 0:
                                    pass
                                    # State 85394
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp23 = subjects2.popleft()
                                        # State 85395
                                        if len(subjects2) == 0:
                                            pass
                                            # State 85396
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
                        matcher = CommutativeMatcher85398.get()
                        tmp26 = subjects25
                        subjects25 = []
                        for s in tmp26:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp26, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 85399
                                if len(subjects9) == 0:
                                    pass
                                    # State 85400
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp27 = subjects2.popleft()
                                        # State 85401
                                        if len(subjects2) == 0:
                                            pass
                                            # State 85402
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
                    matcher = CommutativeMatcher83017.get()
                    tmp30 = subjects29
                    subjects29 = []
                    for s in tmp30:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp30, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 83023
                            if len(subjects9) == 0:
                                pass
                                # State 83024
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp31 = subjects2.popleft()
                                    # State 83025
                                    if len(subjects2) == 0:
                                        pass
                                        # State 83026
                                        if len(subjects) == 0:
                                            pass
                                            # 7: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp31)
                        if pattern_index == 1:
                            pass
                            # State 85406
                            if len(subjects9) == 0:
                                pass
                                # State 85407
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp32 = subjects2.popleft()
                                    # State 85408
                                    if len(subjects2) == 0:
                                        pass
                                        # State 85409
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
            # State 68013
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 68014
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68015
                    if len(subjects34) >= 1:
                        tmp37 = subjects34.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp37)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68016
                            if len(subjects34) == 0:
                                pass
                                # State 68017
                                if len(subjects) == 0:
                                    pass
                                    # 2: sin(c + x*d)
                        subjects34.appendleft(tmp37)
                if len(subjects34) >= 1 and isinstance(subjects34[0], Mul):
                    tmp39 = subjects34.popleft()
                    associative1 = tmp39
                    associative_type1 = type(tmp39)
                    subjects40 = deque(tmp39._args)
                    matcher = CommutativeMatcher68019.get()
                    tmp41 = subjects40
                    subjects40 = []
                    for s in tmp41:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp41, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 68020
                            if len(subjects34) == 0:
                                pass
                                # State 68021
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
                # State 71276
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 71277
                    if len(subjects34) >= 1:
                        tmp44 = subjects34.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp44)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 71278
                            if len(subjects34) == 0:
                                pass
                                # State 71279
                                if len(subjects) == 0:
                                    pass
                                    # 5: sin(e + x*f)
                        subjects34.appendleft(tmp44)
                if len(subjects34) >= 1 and isinstance(subjects34[0], Mul):
                    tmp46 = subjects34.popleft()
                    associative1 = tmp46
                    associative_type1 = type(tmp46)
                    subjects47 = deque(tmp46._args)
                    matcher = CommutativeMatcher71281.get()
                    tmp48 = subjects47
                    subjects47 = []
                    for s in tmp48:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp48, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 71282
                            if len(subjects34) == 0:
                                pass
                                # State 71283
                                if len(subjects) == 0:
                                    pass
                                    # 5: sin(e + x*f)
                    subjects34.appendleft(tmp46)
            if len(subjects34) >= 1 and isinstance(subjects34[0], Add):
                tmp49 = subjects34.popleft()
                associative1 = tmp49
                associative_type1 = type(tmp49)
                subjects50 = deque(tmp49._args)
                matcher = CommutativeMatcher68023.get()
                tmp51 = subjects50
                subjects50 = []
                for s in tmp51:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp51, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 68029
                        if len(subjects34) == 0:
                            pass
                            # State 68030
                            if len(subjects) == 0:
                                pass
                                # 2: sin(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 71287
                        if len(subjects34) == 0:
                            pass
                            # State 71288
                            if len(subjects) == 0:
                                pass
                                # 5: sin(e + x*f)
                subjects34.appendleft(tmp49)
            subjects.appendleft(tmp33)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp52 = subjects.popleft()
            subjects53 = deque(tmp52._args)
            # State 68234
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 68235
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68236
                    if len(subjects53) >= 1:
                        tmp56 = subjects53.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp56)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68237
                            if len(subjects53) == 0:
                                pass
                                # State 68238
                                if len(subjects) == 0:
                                    pass
                                    # 3: cos(c + x*d)
                        subjects53.appendleft(tmp56)
                if len(subjects53) >= 1 and isinstance(subjects53[0], Mul):
                    tmp58 = subjects53.popleft()
                    associative1 = tmp58
                    associative_type1 = type(tmp58)
                    subjects59 = deque(tmp58._args)
                    matcher = CommutativeMatcher68240.get()
                    tmp60 = subjects59
                    subjects59 = []
                    for s in tmp60:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp60, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 68241
                            if len(subjects53) == 0:
                                pass
                                # State 68242
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
                # State 68485
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68486
                    if len(subjects53) >= 1:
                        tmp63 = subjects53.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp63)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68487
                            if len(subjects53) == 0:
                                pass
                                # State 68488
                                if len(subjects) == 0:
                                    pass
                                    # 4: cos(e + x*f)
                        subjects53.appendleft(tmp63)
                if len(subjects53) >= 1 and isinstance(subjects53[0], Mul):
                    tmp65 = subjects53.popleft()
                    associative1 = tmp65
                    associative_type1 = type(tmp65)
                    subjects66 = deque(tmp65._args)
                    matcher = CommutativeMatcher68490.get()
                    tmp67 = subjects66
                    subjects66 = []
                    for s in tmp67:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp67, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 68491
                            if len(subjects53) == 0:
                                pass
                                # State 68492
                                if len(subjects) == 0:
                                    pass
                                    # 4: cos(e + x*f)
                    subjects53.appendleft(tmp65)
            if len(subjects53) >= 1 and isinstance(subjects53[0], Add):
                tmp68 = subjects53.popleft()
                associative1 = tmp68
                associative_type1 = type(tmp68)
                subjects69 = deque(tmp68._args)
                matcher = CommutativeMatcher68244.get()
                tmp70 = subjects69
                subjects69 = []
                for s in tmp70:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp70, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 68250
                        if len(subjects53) == 0:
                            pass
                            # State 68251
                            if len(subjects) == 0:
                                pass
                                # 3: cos(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 68496
                        if len(subjects53) == 0:
                            pass
                            # State 68497
                            if len(subjects) == 0:
                                pass
                                # 4: cos(e + x*f)
                subjects53.appendleft(tmp68)
            subjects.appendleft(tmp52)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp71 = subjects.popleft()
            subjects72 = deque(tmp71._args)
            # State 82828
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 82829
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 82830
                    if len(subjects72) >= 1:
                        tmp75 = subjects72.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp75)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 82831
                            if len(subjects72) == 0:
                                pass
                                # State 82832
                                if len(subjects) == 0:
                                    pass
                                    # 6: tan(e + x*f)
                        subjects72.appendleft(tmp75)
                if len(subjects72) >= 1 and isinstance(subjects72[0], Mul):
                    tmp77 = subjects72.popleft()
                    associative1 = tmp77
                    associative_type1 = type(tmp77)
                    subjects78 = deque(tmp77._args)
                    matcher = CommutativeMatcher82834.get()
                    tmp79 = subjects78
                    subjects78 = []
                    for s in tmp79:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp79, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 82835
                            if len(subjects72) == 0:
                                pass
                                # State 82836
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
                # State 85086
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 85087
                    if len(subjects72) >= 1:
                        tmp82 = subjects72.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp82)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 85088
                            if len(subjects72) == 0:
                                pass
                                # State 85089
                                if len(subjects) == 0:
                                    pass
                                    # 8: tan(c + x*d)
                        subjects72.appendleft(tmp82)
                if len(subjects72) >= 1 and isinstance(subjects72[0], Mul):
                    tmp84 = subjects72.popleft()
                    associative1 = tmp84
                    associative_type1 = type(tmp84)
                    subjects85 = deque(tmp84._args)
                    matcher = CommutativeMatcher85091.get()
                    tmp86 = subjects85
                    subjects85 = []
                    for s in tmp86:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp86, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 85092
                            if len(subjects72) == 0:
                                pass
                                # State 85093
                                if len(subjects) == 0:
                                    pass
                                    # 8: tan(c + x*d)
                    subjects72.appendleft(tmp84)
            if len(subjects72) >= 1 and isinstance(subjects72[0], Add):
                tmp87 = subjects72.popleft()
                associative1 = tmp87
                associative_type1 = type(tmp87)
                subjects88 = deque(tmp87._args)
                matcher = CommutativeMatcher82838.get()
                tmp89 = subjects88
                subjects88 = []
                for s in tmp89:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp89, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 82844
                        if len(subjects72) == 0:
                            pass
                            # State 82845
                            if len(subjects) == 0:
                                pass
                                # 6: tan(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 85097
                        if len(subjects72) == 0:
                            pass
                            # State 85098
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
