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

class CommutativeMatcher114708(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher114708._instance is None:
            CommutativeMatcher114708._instance = CommutativeMatcher114708()
        return CommutativeMatcher114708._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 114707
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 114709
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 114710
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp4 = subjects2.popleft()
                    subjects5 = deque(tmp4._args)
                    # State 114711
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114712
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 114713
                            if len(subjects5) >= 1:
                                tmp8 = subjects5.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2.1.0', tmp8)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 114714
                                    if len(subjects5) >= 1 and subjects5[0] == -1:
                                        tmp10 = subjects5.popleft()
                                        # State 114715
                                        if len(subjects5) == 0:
                                            pass
                                            # State 114716
                                            if len(subjects2) == 0:
                                                pass
                                                # State 114717
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: atan(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                        subjects5.appendleft(tmp10)
                                subjects5.appendleft(tmp8)
                        if len(subjects5) >= 1 and isinstance(subjects5[0], Mul):
                            tmp11 = subjects5.popleft()
                            associative1 = tmp11
                            associative_type1 = type(tmp11)
                            subjects12 = deque(tmp11._args)
                            matcher = CommutativeMatcher114719.get()
                            tmp13 = subjects12
                            subjects12 = []
                            for s in tmp13:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp13, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 114720
                                    if len(subjects5) >= 1 and subjects5[0] == -1:
                                        tmp14 = subjects5.popleft()
                                        # State 114721
                                        if len(subjects5) == 0:
                                            pass
                                            # State 114722
                                            if len(subjects2) == 0:
                                                pass
                                                # State 114723
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: atan(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                        subjects5.appendleft(tmp14)
                            subjects5.appendleft(tmp11)
                    if len(subjects5) >= 1 and isinstance(subjects5[0], Add):
                        tmp15 = subjects5.popleft()
                        associative1 = tmp15
                        associative_type1 = type(tmp15)
                        subjects16 = deque(tmp15._args)
                        matcher = CommutativeMatcher114725.get()
                        tmp17 = subjects16
                        subjects16 = []
                        for s in tmp17:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp17, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 114731
                                if len(subjects5) >= 1 and subjects5[0] == -1:
                                    tmp18 = subjects5.popleft()
                                    # State 114732
                                    if len(subjects5) == 0:
                                        pass
                                        # State 114733
                                        if len(subjects2) == 0:
                                            pass
                                            # State 114734
                                            if len(subjects) == 0:
                                                pass
                                                # 0: atan(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    subjects5.appendleft(tmp18)
                        subjects5.appendleft(tmp15)
                    subjects2.appendleft(tmp4)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp19 = subjects2.popleft()
                associative1 = tmp19
                associative_type1 = type(tmp19)
                subjects20 = deque(tmp19._args)
                matcher = CommutativeMatcher114736.get()
                tmp21 = subjects20
                subjects20 = []
                for s in tmp21:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp21, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 114758
                        if len(subjects2) == 0:
                            pass
                            # State 114759
                            if len(subjects) == 0:
                                pass
                                # 0: atan(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                subjects2.appendleft(tmp19)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp22 = subjects.popleft()
            subjects23 = deque(tmp22._args)
            # State 114867
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 114868
                if len(subjects23) >= 1:
                    tmp25 = subjects23.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.0', tmp25)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114869
                        if len(subjects23) == 0:
                            pass
                            # State 114870
                            if len(subjects) == 0:
                                pass
                                # 1: acot(x*a) /; (cons_f2)
                    subjects23.appendleft(tmp25)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 115043
                if len(subjects23) >= 1 and isinstance(subjects23[0], Add):
                    tmp28 = subjects23.popleft()
                    associative1 = tmp28
                    associative_type1 = type(tmp28)
                    subjects29 = deque(tmp28._args)
                    matcher = CommutativeMatcher115045.get()
                    tmp30 = subjects29
                    subjects29 = []
                    for s in tmp30:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp30, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 115051
                            if len(subjects23) == 0:
                                pass
                                # State 115052
                                if len(subjects) == 0:
                                    pass
                                    # 2: acot(c*(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects23.appendleft(tmp28)
                if len(subjects23) >= 1 and isinstance(subjects23[0], Pow):
                    tmp31 = subjects23.popleft()
                    subjects32 = deque(tmp31._args)
                    # State 115298
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 115299
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 115300
                            if len(subjects32) >= 1:
                                tmp35 = subjects32.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2.1.0', tmp35)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 115301
                                    if len(subjects32) >= 1 and subjects32[0] == -1:
                                        tmp37 = subjects32.popleft()
                                        # State 115302
                                        if len(subjects32) == 0:
                                            pass
                                            # State 115303
                                            if len(subjects23) == 0:
                                                pass
                                                # State 115304
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: acot(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                        subjects32.appendleft(tmp37)
                                subjects32.appendleft(tmp35)
                        if len(subjects32) >= 1 and isinstance(subjects32[0], Mul):
                            tmp38 = subjects32.popleft()
                            associative1 = tmp38
                            associative_type1 = type(tmp38)
                            subjects39 = deque(tmp38._args)
                            matcher = CommutativeMatcher115306.get()
                            tmp40 = subjects39
                            subjects39 = []
                            for s in tmp40:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp40, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 115307
                                    if len(subjects32) >= 1 and subjects32[0] == -1:
                                        tmp41 = subjects32.popleft()
                                        # State 115308
                                        if len(subjects32) == 0:
                                            pass
                                            # State 115309
                                            if len(subjects23) == 0:
                                                pass
                                                # State 115310
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: acot(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                        subjects32.appendleft(tmp41)
                            subjects32.appendleft(tmp38)
                    if len(subjects32) >= 1 and isinstance(subjects32[0], Add):
                        tmp42 = subjects32.popleft()
                        associative1 = tmp42
                        associative_type1 = type(tmp42)
                        subjects43 = deque(tmp42._args)
                        matcher = CommutativeMatcher115312.get()
                        tmp44 = subjects43
                        subjects43 = []
                        for s in tmp44:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp44, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 115318
                                if len(subjects32) >= 1 and subjects32[0] == -1:
                                    tmp45 = subjects32.popleft()
                                    # State 115319
                                    if len(subjects32) == 0:
                                        pass
                                        # State 115320
                                        if len(subjects23) == 0:
                                            pass
                                            # State 115321
                                            if len(subjects) == 0:
                                                pass
                                                # 3: acot(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    subjects32.appendleft(tmp45)
                        subjects32.appendleft(tmp42)
                    subjects23.appendleft(tmp31)
            if len(subjects23) >= 1 and isinstance(subjects23[0], Mul):
                tmp46 = subjects23.popleft()
                associative1 = tmp46
                associative_type1 = type(tmp46)
                subjects47 = deque(tmp46._args)
                matcher = CommutativeMatcher114872.get()
                tmp48 = subjects47
                subjects47 = []
                for s in tmp48:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp48, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 114873
                        if len(subjects23) == 0:
                            pass
                            # State 114874
                            if len(subjects) == 0:
                                pass
                                # 1: acot(x*a) /; (cons_f2)
                    if pattern_index == 1:
                        pass
                        # State 115061
                        if len(subjects23) == 0:
                            pass
                            # State 115062
                            if len(subjects) == 0:
                                pass
                                # 2: acot(c*(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8)
                    if pattern_index == 2:
                        pass
                        # State 115343
                        if len(subjects23) == 0:
                            pass
                            # State 115344
                            if len(subjects) == 0:
                                pass
                                # 3: acot(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                subjects23.appendleft(tmp46)
            subjects.appendleft(tmp22)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp49 = subjects.popleft()
            subjects50 = deque(tmp49._args)
            # State 144003
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 144004
                if len(subjects50) >= 1 and isinstance(subjects50[0], Pow):
                    tmp52 = subjects50.popleft()
                    subjects53 = deque(tmp52._args)
                    # State 144005
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 144006
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 144007
                            if len(subjects53) >= 1:
                                tmp56 = subjects53.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2.1.0', tmp56)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 144008
                                    if len(subjects53) >= 1 and subjects53[0] == -1:
                                        tmp58 = subjects53.popleft()
                                        # State 144009
                                        if len(subjects53) == 0:
                                            pass
                                            # State 144010
                                            if len(subjects50) == 0:
                                                pass
                                                # State 144011
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: atanh(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                        subjects53.appendleft(tmp58)
                                subjects53.appendleft(tmp56)
                        if len(subjects53) >= 1 and isinstance(subjects53[0], Mul):
                            tmp59 = subjects53.popleft()
                            associative1 = tmp59
                            associative_type1 = type(tmp59)
                            subjects60 = deque(tmp59._args)
                            matcher = CommutativeMatcher144013.get()
                            tmp61 = subjects60
                            subjects60 = []
                            for s in tmp61:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp61, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 144014
                                    if len(subjects53) >= 1 and subjects53[0] == -1:
                                        tmp62 = subjects53.popleft()
                                        # State 144015
                                        if len(subjects53) == 0:
                                            pass
                                            # State 144016
                                            if len(subjects50) == 0:
                                                pass
                                                # State 144017
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: atanh(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                        subjects53.appendleft(tmp62)
                            subjects53.appendleft(tmp59)
                    if len(subjects53) >= 1 and isinstance(subjects53[0], Add):
                        tmp63 = subjects53.popleft()
                        associative1 = tmp63
                        associative_type1 = type(tmp63)
                        subjects64 = deque(tmp63._args)
                        matcher = CommutativeMatcher144019.get()
                        tmp65 = subjects64
                        subjects64 = []
                        for s in tmp65:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp65, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 144025
                                if len(subjects53) >= 1 and subjects53[0] == -1:
                                    tmp66 = subjects53.popleft()
                                    # State 144026
                                    if len(subjects53) == 0:
                                        pass
                                        # State 144027
                                        if len(subjects50) == 0:
                                            pass
                                            # State 144028
                                            if len(subjects) == 0:
                                                pass
                                                # 4: atanh(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    subjects53.appendleft(tmp66)
                        subjects53.appendleft(tmp63)
                    subjects50.appendleft(tmp52)
            if len(subjects50) >= 1 and isinstance(subjects50[0], Mul):
                tmp67 = subjects50.popleft()
                associative1 = tmp67
                associative_type1 = type(tmp67)
                subjects68 = deque(tmp67._args)
                matcher = CommutativeMatcher144030.get()
                tmp69 = subjects68
                subjects68 = []
                for s in tmp69:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp69, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144052
                        if len(subjects50) == 0:
                            pass
                            # State 144053
                            if len(subjects) == 0:
                                pass
                                # 4: atanh(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                subjects50.appendleft(tmp67)
            subjects.appendleft(tmp49)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp70 = subjects.popleft()
            subjects71 = deque(tmp70._args)
            # State 144161
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 144162
                if len(subjects71) >= 1:
                    tmp73 = subjects71.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.0', tmp73)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 144163
                        if len(subjects71) == 0:
                            pass
                            # State 144164
                            if len(subjects) == 0:
                                pass
                                # 5: acoth(x*a) /; (cons_f2)
                    subjects71.appendleft(tmp73)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 144337
                if len(subjects71) >= 1 and isinstance(subjects71[0], Add):
                    tmp76 = subjects71.popleft()
                    associative1 = tmp76
                    associative_type1 = type(tmp76)
                    subjects77 = deque(tmp76._args)
                    matcher = CommutativeMatcher144339.get()
                    tmp78 = subjects77
                    subjects77 = []
                    for s in tmp78:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp78, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 144345
                            if len(subjects71) == 0:
                                pass
                                # State 144346
                                if len(subjects) == 0:
                                    pass
                                    # 6: acoth(c*(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8)
                    subjects71.appendleft(tmp76)
                if len(subjects71) >= 1 and isinstance(subjects71[0], Pow):
                    tmp79 = subjects71.popleft()
                    subjects80 = deque(tmp79._args)
                    # State 144523
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 144524
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 144525
                            if len(subjects80) >= 1:
                                tmp83 = subjects80.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2.1.0', tmp83)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 144526
                                    if len(subjects80) >= 1 and subjects80[0] == -1:
                                        tmp85 = subjects80.popleft()
                                        # State 144527
                                        if len(subjects80) == 0:
                                            pass
                                            # State 144528
                                            if len(subjects71) == 0:
                                                pass
                                                # State 144529
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: acoth(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                        subjects80.appendleft(tmp85)
                                subjects80.appendleft(tmp83)
                        if len(subjects80) >= 1 and isinstance(subjects80[0], Mul):
                            tmp86 = subjects80.popleft()
                            associative1 = tmp86
                            associative_type1 = type(tmp86)
                            subjects87 = deque(tmp86._args)
                            matcher = CommutativeMatcher144531.get()
                            tmp88 = subjects87
                            subjects87 = []
                            for s in tmp88:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp88, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 144532
                                    if len(subjects80) >= 1 and subjects80[0] == -1:
                                        tmp89 = subjects80.popleft()
                                        # State 144533
                                        if len(subjects80) == 0:
                                            pass
                                            # State 144534
                                            if len(subjects71) == 0:
                                                pass
                                                # State 144535
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: acoth(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                        subjects80.appendleft(tmp89)
                            subjects80.appendleft(tmp86)
                    if len(subjects80) >= 1 and isinstance(subjects80[0], Add):
                        tmp90 = subjects80.popleft()
                        associative1 = tmp90
                        associative_type1 = type(tmp90)
                        subjects91 = deque(tmp90._args)
                        matcher = CommutativeMatcher144537.get()
                        tmp92 = subjects91
                        subjects91 = []
                        for s in tmp92:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp92, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 144543
                                if len(subjects80) >= 1 and subjects80[0] == -1:
                                    tmp93 = subjects80.popleft()
                                    # State 144544
                                    if len(subjects80) == 0:
                                        pass
                                        # State 144545
                                        if len(subjects71) == 0:
                                            pass
                                            # State 144546
                                            if len(subjects) == 0:
                                                pass
                                                # 7: acoth(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    subjects80.appendleft(tmp93)
                        subjects80.appendleft(tmp90)
                    subjects71.appendleft(tmp79)
            if len(subjects71) >= 1 and isinstance(subjects71[0], Mul):
                tmp94 = subjects71.popleft()
                associative1 = tmp94
                associative_type1 = type(tmp94)
                subjects95 = deque(tmp94._args)
                matcher = CommutativeMatcher144166.get()
                tmp96 = subjects95
                subjects95 = []
                for s in tmp96:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp96, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144167
                        if len(subjects71) == 0:
                            pass
                            # State 144168
                            if len(subjects) == 0:
                                pass
                                # 5: acoth(x*a) /; (cons_f2)
                    if pattern_index == 1:
                        pass
                        # State 144355
                        if len(subjects71) == 0:
                            pass
                            # State 144356
                            if len(subjects) == 0:
                                pass
                                # 6: acoth(c*(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8)
                    if pattern_index == 2:
                        pass
                        # State 144568
                        if len(subjects71) == 0:
                            pass
                            # State 144569
                            if len(subjects) == 0:
                                pass
                                # 7: acoth(c/(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                subjects71.appendleft(tmp94)
            subjects.appendleft(tmp70)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
