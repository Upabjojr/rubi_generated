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

class CommutativeMatcher116149(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher116149._instance is None:
            CommutativeMatcher116149._instance = CommutativeMatcher116149()
        return CommutativeMatcher116149._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 116148
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 116150
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 116151
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 116152
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 116153
                            if len(subjects2) >= 1:
                                tmp7 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp7)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 116154
                                    if len(subjects2) == 0:
                                        pass
                                        # State 116155
                                        if len(subjects) == 0:
                                            pass
                                            # 0: F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f127) and (cons_f1836)
                                subjects2.appendleft(tmp7)
                        if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                            tmp9 = subjects2.popleft()
                            associative1 = tmp9
                            associative_type1 = type(tmp9)
                            subjects10 = deque(tmp9._args)
                            matcher = CommutativeMatcher116157.get()
                            tmp11 = subjects10
                            subjects10 = []
                            for s in tmp11:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp11, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 116158
                                    if len(subjects2) == 0:
                                        pass
                                        # State 116159
                                        if len(subjects) == 0:
                                            pass
                                            # 0: F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f127) and (cons_f1836)
                            subjects2.appendleft(tmp9)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                        tmp12 = subjects2.popleft()
                        associative1 = tmp12
                        associative_type1 = type(tmp12)
                        subjects13 = deque(tmp12._args)
                        matcher = CommutativeMatcher116161.get()
                        tmp14 = subjects13
                        subjects13 = []
                        for s in tmp14:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp14, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 116167
                                if len(subjects2) == 0:
                                    pass
                                    # State 116168
                                    if len(subjects) == 0:
                                        pass
                                        # 0: F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f127) and (cons_f1836)
                        subjects2.appendleft(tmp12)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp15 = subjects2.popleft()
                subjects16 = deque(tmp15._args)
                # State 117889
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 117890
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 117891
                        if len(subjects16) >= 1:
                            tmp19 = subjects16.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.3.1.0', tmp19)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 117892
                                if len(subjects16) == 0:
                                    pass
                                    # State 117893
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp21 = subjects2.popleft()
                                        # State 117894
                                        if len(subjects2) == 0:
                                            pass
                                            # State 117895
                                            if len(subjects) == 0:
                                                pass
                                                # 2: 1/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                        subjects2.appendleft(tmp21)
                            subjects16.appendleft(tmp19)
                    if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                        tmp22 = subjects16.popleft()
                        associative1 = tmp22
                        associative_type1 = type(tmp22)
                        subjects23 = deque(tmp22._args)
                        matcher = CommutativeMatcher117897.get()
                        tmp24 = subjects23
                        subjects23 = []
                        for s in tmp24:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp24, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 117898
                                if len(subjects16) == 0:
                                    pass
                                    # State 117899
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp25 = subjects2.popleft()
                                        # State 117900
                                        if len(subjects2) == 0:
                                            pass
                                            # State 117901
                                            if len(subjects) == 0:
                                                pass
                                                # 2: 1/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                        subjects2.appendleft(tmp25)
                        subjects16.appendleft(tmp22)
                if len(subjects16) >= 1 and isinstance(subjects16[0], Add):
                    tmp26 = subjects16.popleft()
                    associative1 = tmp26
                    associative_type1 = type(tmp26)
                    subjects27 = deque(tmp26._args)
                    matcher = CommutativeMatcher117903.get()
                    tmp28 = subjects27
                    subjects27 = []
                    for s in tmp28:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp28, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 117909
                            if len(subjects16) == 0:
                                pass
                                # State 117910
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp29 = subjects2.popleft()
                                    # State 117911
                                    if len(subjects2) == 0:
                                        pass
                                        # State 117912
                                        if len(subjects) == 0:
                                            pass
                                            # 2: 1/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                    subjects2.appendleft(tmp29)
                    subjects16.appendleft(tmp26)
                subjects2.appendleft(tmp15)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tanh):
                tmp30 = subjects2.popleft()
                subjects31 = deque(tmp30._args)
                # State 118953
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 118954
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 118955
                        if len(subjects31) >= 1:
                            tmp34 = subjects31.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.3.1.0', tmp34)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 118956
                                if len(subjects31) == 0:
                                    pass
                                    # State 118957
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp36 = subjects2.popleft()
                                        # State 118958
                                        if len(subjects2) == 0:
                                            pass
                                            # State 118959
                                            if len(subjects) == 0:
                                                pass
                                                # 4: 1/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                        subjects2.appendleft(tmp36)
                            subjects31.appendleft(tmp34)
                    if len(subjects31) >= 1 and isinstance(subjects31[0], Mul):
                        tmp37 = subjects31.popleft()
                        associative1 = tmp37
                        associative_type1 = type(tmp37)
                        subjects38 = deque(tmp37._args)
                        matcher = CommutativeMatcher118961.get()
                        tmp39 = subjects38
                        subjects38 = []
                        for s in tmp39:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp39, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 118962
                                if len(subjects31) == 0:
                                    pass
                                    # State 118963
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp40 = subjects2.popleft()
                                        # State 118964
                                        if len(subjects2) == 0:
                                            pass
                                            # State 118965
                                            if len(subjects) == 0:
                                                pass
                                                # 4: 1/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                        subjects2.appendleft(tmp40)
                        subjects31.appendleft(tmp37)
                if len(subjects31) >= 1 and isinstance(subjects31[0], Add):
                    tmp41 = subjects31.popleft()
                    associative1 = tmp41
                    associative_type1 = type(tmp41)
                    subjects42 = deque(tmp41._args)
                    matcher = CommutativeMatcher118967.get()
                    tmp43 = subjects42
                    subjects42 = []
                    for s in tmp43:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp43, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 118973
                            if len(subjects31) == 0:
                                pass
                                # State 118974
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp44 = subjects2.popleft()
                                    # State 118975
                                    if len(subjects2) == 0:
                                        pass
                                        # State 118976
                                        if len(subjects) == 0:
                                            pass
                                            # 4: 1/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                    subjects2.appendleft(tmp44)
                    subjects31.appendleft(tmp41)
                subjects2.appendleft(tmp30)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp45 = subjects.popleft()
            subjects46 = deque(tmp45._args)
            # State 117679
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 117680
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 117681
                    if len(subjects46) >= 1:
                        tmp49 = subjects46.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1.0', tmp49)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 117682
                            if len(subjects46) == 0:
                                pass
                                # State 117683
                                if len(subjects) == 0:
                                    pass
                                    # 1: tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                        subjects46.appendleft(tmp49)
                if len(subjects46) >= 1 and isinstance(subjects46[0], Mul):
                    tmp51 = subjects46.popleft()
                    associative1 = tmp51
                    associative_type1 = type(tmp51)
                    subjects52 = deque(tmp51._args)
                    matcher = CommutativeMatcher117685.get()
                    tmp53 = subjects52
                    subjects52 = []
                    for s in tmp53:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp53, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 117686
                            if len(subjects46) == 0:
                                pass
                                # State 117687
                                if len(subjects) == 0:
                                    pass
                                    # 1: tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                    subjects46.appendleft(tmp51)
            if len(subjects46) >= 1 and isinstance(subjects46[0], Add):
                tmp54 = subjects46.popleft()
                associative1 = tmp54
                associative_type1 = type(tmp54)
                subjects55 = deque(tmp54._args)
                matcher = CommutativeMatcher117689.get()
                tmp56 = subjects55
                subjects55 = []
                for s in tmp56:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp56, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 117695
                        if len(subjects46) == 0:
                            pass
                            # State 117696
                            if len(subjects) == 0:
                                pass
                                # 1: tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                subjects46.appendleft(tmp54)
            subjects.appendleft(tmp45)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp57 = subjects.popleft()
            subjects58 = deque(tmp57._args)
            # State 118743
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 118744
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 118745
                    if len(subjects58) >= 1:
                        tmp61 = subjects58.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1.0', tmp61)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 118746
                            if len(subjects58) == 0:
                                pass
                                # State 118747
                                if len(subjects) == 0:
                                    pass
                                    # 3: tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                        subjects58.appendleft(tmp61)
                if len(subjects58) >= 1 and isinstance(subjects58[0], Mul):
                    tmp63 = subjects58.popleft()
                    associative1 = tmp63
                    associative_type1 = type(tmp63)
                    subjects64 = deque(tmp63._args)
                    matcher = CommutativeMatcher118749.get()
                    tmp65 = subjects64
                    subjects64 = []
                    for s in tmp65:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp65, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 118750
                            if len(subjects58) == 0:
                                pass
                                # State 118751
                                if len(subjects) == 0:
                                    pass
                                    # 3: tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                    subjects58.appendleft(tmp63)
            if len(subjects58) >= 1 and isinstance(subjects58[0], Add):
                tmp66 = subjects58.popleft()
                associative1 = tmp66
                associative_type1 = type(tmp66)
                subjects67 = deque(tmp66._args)
                matcher = CommutativeMatcher118753.get()
                tmp68 = subjects67
                subjects67 = []
                for s in tmp68:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp68, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 118759
                        if len(subjects58) == 0:
                            pass
                            # State 118760
                            if len(subjects) == 0:
                                pass
                                # 3: tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                subjects58.appendleft(tmp66)
            subjects.appendleft(tmp57)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
