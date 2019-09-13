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

class CommutativeMatcher145137(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher145137._instance is None:
            CommutativeMatcher145137._instance = CommutativeMatcher145137()
        return CommutativeMatcher145137._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 145136
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 145138
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 145139
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 145140
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 145141
                                if len(subjects3) == 0:
                                    pass
                                    # State 145142
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f1833)
                            subjects3.appendleft(tmp6)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 145326
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 145327
                                if len(subjects3) >= 1:
                                    tmp10 = subjects3.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.3.1.0', tmp10)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 145328
                                        if len(subjects3) == 0:
                                            pass
                                            # State 145329
                                            if len(subjects) == 0:
                                                pass
                                                # 1: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f127) and (cons_f1836)
                                    subjects3.appendleft(tmp10)
                            if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                                tmp12 = subjects3.popleft()
                                associative1 = tmp12
                                associative_type1 = type(tmp12)
                                subjects13 = deque(tmp12._args)
                                matcher = CommutativeMatcher145331.get()
                                tmp14 = subjects13
                                subjects13 = []
                                for s in tmp14:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp14, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 145332
                                        if len(subjects3) == 0:
                                            pass
                                            # State 145333
                                            if len(subjects) == 0:
                                                pass
                                                # 1: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f127) and (cons_f1836)
                                subjects3.appendleft(tmp12)
                        if len(subjects3) >= 1 and isinstance(subjects3[0], Add):
                            tmp15 = subjects3.popleft()
                            associative1 = tmp15
                            associative_type1 = type(tmp15)
                            subjects16 = deque(tmp15._args)
                            matcher = CommutativeMatcher145335.get()
                            tmp17 = subjects16
                            subjects16 = []
                            for s in tmp17:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp17, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 145341
                                    if len(subjects3) == 0:
                                        pass
                                        # State 145342
                                        if len(subjects) == 0:
                                            pass
                                            # 1: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f127) and (cons_f1836)
                            subjects3.appendleft(tmp15)
                    subjects3.appendleft(tmp4)
                if len(subjects3) >= 1 and isinstance(subjects3[0], tanh):
                    tmp18 = subjects3.popleft()
                    subjects19 = deque(tmp18._args)
                    # State 146998
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 146999
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 147000
                            if len(subjects19) >= 1:
                                tmp22 = subjects19.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp22)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 147001
                                    if len(subjects19) == 0:
                                        pass
                                        # State 147002
                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                            tmp24 = subjects3.popleft()
                                            # State 147003
                                            if len(subjects3) == 0:
                                                pass
                                                # State 147004
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                                                    # 5: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                                            subjects3.appendleft(tmp24)
                                subjects19.appendleft(tmp22)
                        if len(subjects19) >= 1 and isinstance(subjects19[0], Mul):
                            tmp25 = subjects19.popleft()
                            associative1 = tmp25
                            associative_type1 = type(tmp25)
                            subjects26 = deque(tmp25._args)
                            matcher = CommutativeMatcher147006.get()
                            tmp27 = subjects26
                            subjects26 = []
                            for s in tmp27:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp27, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 147007
                                    if len(subjects19) == 0:
                                        pass
                                        # State 147008
                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                            tmp28 = subjects3.popleft()
                                            # State 147009
                                            if len(subjects3) == 0:
                                                pass
                                                # State 147010
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                                                    # 5: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                                            subjects3.appendleft(tmp28)
                            subjects19.appendleft(tmp25)
                    if len(subjects19) >= 1 and isinstance(subjects19[0], Add):
                        tmp29 = subjects19.popleft()
                        associative1 = tmp29
                        associative_type1 = type(tmp29)
                        subjects30 = deque(tmp29._args)
                        matcher = CommutativeMatcher147012.get()
                        tmp31 = subjects30
                        subjects30 = []
                        for s in tmp31:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp31, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 147018
                                if len(subjects19) == 0:
                                    pass
                                    # State 147019
                                    if len(subjects3) >= 1 and subjects3[0] == -1:
                                        tmp32 = subjects3.popleft()
                                        # State 147020
                                        if len(subjects3) == 0:
                                            pass
                                            # State 147021
                                            if len(subjects) == 0:
                                                pass
                                                # 3: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                                                # 5: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                                        subjects3.appendleft(tmp32)
                        subjects19.appendleft(tmp29)
                    subjects3.appendleft(tmp18)
                if len(subjects3) >= 1 and isinstance(subjects3[0], tan):
                    tmp33 = subjects3.popleft()
                    subjects34 = deque(tmp33._args)
                    # State 148062
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148063
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 148064
                            if len(subjects34) >= 1:
                                tmp37 = subjects34.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp37)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 148065
                                    if len(subjects34) == 0:
                                        pass
                                        # State 148066
                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                            tmp39 = subjects3.popleft()
                                            # State 148067
                                            if len(subjects3) == 0:
                                                pass
                                                # State 148068
                                                if len(subjects) == 0:
                                                    pass
                                                    # 9: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1950)
                                                    # 7: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1948)
                                            subjects3.appendleft(tmp39)
                                subjects34.appendleft(tmp37)
                        if len(subjects34) >= 1 and isinstance(subjects34[0], Mul):
                            tmp40 = subjects34.popleft()
                            associative1 = tmp40
                            associative_type1 = type(tmp40)
                            subjects41 = deque(tmp40._args)
                            matcher = CommutativeMatcher148070.get()
                            tmp42 = subjects41
                            subjects41 = []
                            for s in tmp42:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp42, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 148071
                                    if len(subjects34) == 0:
                                        pass
                                        # State 148072
                                        if len(subjects3) >= 1 and subjects3[0] == -1:
                                            tmp43 = subjects3.popleft()
                                            # State 148073
                                            if len(subjects3) == 0:
                                                pass
                                                # State 148074
                                                if len(subjects) == 0:
                                                    pass
                                                    # 9: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1950)
                                                    # 7: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1948)
                                            subjects3.appendleft(tmp43)
                            subjects34.appendleft(tmp40)
                    if len(subjects34) >= 1 and isinstance(subjects34[0], Add):
                        tmp44 = subjects34.popleft()
                        associative1 = tmp44
                        associative_type1 = type(tmp44)
                        subjects45 = deque(tmp44._args)
                        matcher = CommutativeMatcher148076.get()
                        tmp46 = subjects45
                        subjects45 = []
                        for s in tmp46:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp46, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 148082
                                if len(subjects34) == 0:
                                    pass
                                    # State 148083
                                    if len(subjects3) >= 1 and subjects3[0] == -1:
                                        tmp47 = subjects3.popleft()
                                        # State 148084
                                        if len(subjects3) == 0:
                                            pass
                                            # State 148085
                                            if len(subjects) == 0:
                                                pass
                                                # 9: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1950)
                                                # 7: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1948)
                                        subjects3.appendleft(tmp47)
                        subjects34.appendleft(tmp44)
                    subjects3.appendleft(tmp33)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], tanh):
                tmp48 = subjects.popleft()
                subjects49 = deque(tmp48._args)
                # State 146806
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 146807
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 146808
                        if len(subjects49) >= 1:
                            tmp52 = subjects49.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1.0', tmp52)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 146809
                                if len(subjects49) == 0:
                                    pass
                                    # State 146810
                                    if len(subjects) == 0:
                                        pass
                                        # 2: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                                        # 4: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                            subjects49.appendleft(tmp52)
                    if len(subjects49) >= 1 and isinstance(subjects49[0], Mul):
                        tmp54 = subjects49.popleft()
                        associative1 = tmp54
                        associative_type1 = type(tmp54)
                        subjects55 = deque(tmp54._args)
                        matcher = CommutativeMatcher146812.get()
                        tmp56 = subjects55
                        subjects55 = []
                        for s in tmp56:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp56, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 146813
                                if len(subjects49) == 0:
                                    pass
                                    # State 146814
                                    if len(subjects) == 0:
                                        pass
                                        # 2: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                                        # 4: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                        subjects49.appendleft(tmp54)
                if len(subjects49) >= 1 and isinstance(subjects49[0], Add):
                    tmp57 = subjects49.popleft()
                    associative1 = tmp57
                    associative_type1 = type(tmp57)
                    subjects58 = deque(tmp57._args)
                    matcher = CommutativeMatcher146816.get()
                    tmp59 = subjects58
                    subjects58 = []
                    for s in tmp59:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp59, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 146822
                            if len(subjects49) == 0:
                                pass
                                # State 146823
                                if len(subjects) == 0:
                                    pass
                                    # 2: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                                    # 4: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                    subjects49.appendleft(tmp57)
                subjects.appendleft(tmp48)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp60 = subjects.popleft()
                subjects61 = deque(tmp60._args)
                # State 147870
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 147871
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 147872
                        if len(subjects61) >= 1:
                            tmp64 = subjects61.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1.0', tmp64)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 147873
                                if len(subjects61) == 0:
                                    pass
                                    # State 147874
                                    if len(subjects) == 0:
                                        pass
                                        # 8: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1949)
                                        # 6: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1947)
                            subjects61.appendleft(tmp64)
                    if len(subjects61) >= 1 and isinstance(subjects61[0], Mul):
                        tmp66 = subjects61.popleft()
                        associative1 = tmp66
                        associative_type1 = type(tmp66)
                        subjects67 = deque(tmp66._args)
                        matcher = CommutativeMatcher147876.get()
                        tmp68 = subjects67
                        subjects67 = []
                        for s in tmp68:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp68, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 147877
                                if len(subjects61) == 0:
                                    pass
                                    # State 147878
                                    if len(subjects) == 0:
                                        pass
                                        # 8: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1949)
                                        # 6: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1947)
                        subjects61.appendleft(tmp66)
                if len(subjects61) >= 1 and isinstance(subjects61[0], Add):
                    tmp69 = subjects61.popleft()
                    associative1 = tmp69
                    associative_type1 = type(tmp69)
                    subjects70 = deque(tmp69._args)
                    matcher = CommutativeMatcher147880.get()
                    tmp71 = subjects70
                    subjects70 = []
                    for s in tmp71:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp71, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 147886
                            if len(subjects61) == 0:
                                pass
                                # State 147887
                                if len(subjects) == 0:
                                    pass
                                    # 8: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1949)
                                    # 6: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1947)
                    subjects61.appendleft(tmp69)
                subjects.appendleft(tmp60)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp72 = subjects.popleft()
            associative1 = tmp72
            associative_type1 = type(tmp72)
            subjects73 = deque(tmp72._args)
            matcher = CommutativeMatcher145144.get()
            tmp74 = subjects73
            subjects73 = []
            for s in tmp74:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp74, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 145149
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f1833)
                if pattern_index == 1:
                    pass
                    # State 145360
                    if len(subjects) == 0:
                        pass
                        # 1: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f127) and (cons_f1836)
                if pattern_index == 2:
                    pass
                    # State 146842
                    if len(subjects) == 0:
                        pass
                        # 2: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                        # 4: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                if pattern_index == 3:
                    pass
                    # State 147046
                    if len(subjects) == 0:
                        pass
                        # 3: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                        # 5: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                if pattern_index == 4:
                    pass
                    # State 147906
                    if len(subjects) == 0:
                        pass
                        # 8: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1949)
                        # 6: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1947)
                if pattern_index == 5:
                    pass
                    # State 148110
                    if len(subjects) == 0:
                        pass
                        # 9: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1950)
                        # 7: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1948)
            subjects.appendleft(tmp72)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
