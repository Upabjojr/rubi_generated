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


class CommutativeMatcher115937(CommutativeMatcher):
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
        if CommutativeMatcher115937._instance is None:
            CommutativeMatcher115937._instance = CommutativeMatcher115937()
        return CommutativeMatcher115937._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 115936
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 115938
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 115939
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 115940
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 115941
                                if len(subjects3) == 0:
                                    pass
                                    # State 115942
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f1833)
                                        yield 0, subst3
                            subjects3.appendleft(tmp6)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 116173
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 116174
                                if len(subjects3) >= 1:
                                    tmp10 = subjects3.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.3.1.0', tmp10)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 116175
                                        if len(subjects3) == 0:
                                            pass
                                            # State 116176
                                            if len(subjects) == 0:
                                                pass
                                                # 1: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f127) and (cons_f1836)
                                                yield 1, subst5
                                    subjects3.appendleft(tmp10)
                            if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                                tmp12 = subjects3.popleft()
                                associative1 = tmp12
                                associative_type1 = type(tmp12)
                                subjects13 = deque(tmp12._args)
                                matcher = CommutativeMatcher116178.get()
                                tmp14 = subjects13
                                subjects13 = []
                                for s in tmp14:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp14, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 116179
                                        if len(subjects3) == 0:
                                            pass
                                            # State 116180
                                            if len(subjects) == 0:
                                                pass
                                                # 1: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f127) and (cons_f1836)
                                                yield 1, subst4
                                subjects3.appendleft(tmp12)
                        if len(subjects3) >= 1 and isinstance(subjects3[0], Add):
                            tmp15 = subjects3.popleft()
                            associative1 = tmp15
                            associative_type1 = type(tmp15)
                            subjects16 = deque(tmp15._args)
                            matcher = CommutativeMatcher116182.get()
                            tmp17 = subjects16
                            subjects16 = []
                            for s in tmp17:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp17, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 116188
                                    if len(subjects3) == 0:
                                        pass
                                        # State 116189
                                        if len(subjects) == 0:
                                            pass
                                            # 1: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f127) and (cons_f1836)
                                            yield 1, subst3
                            subjects3.appendleft(tmp15)
                    subjects3.appendleft(tmp4)
                if len(subjects3) >= 1 and isinstance(subjects3[0], tan):
                    tmp18 = subjects3.popleft()
                    subjects19 = deque(tmp18._args)
                    # State 117917
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 117918
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 117919
                            if len(subjects19) >= 1:
                                tmp22 = subjects19.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp22)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 117920
                                    if len(subjects19) == 0:
                                        pass
                                        # State 117921
                                        if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                            tmp24 = subjects3.popleft()
                                            # State 117922
                                            if len(subjects3) == 0:
                                                pass
                                                # State 117923
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1844)
                                                    yield 3, subst4
                                                    # 5: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1846)
                                                    yield 5, subst4
                                            subjects3.appendleft(tmp24)
                                subjects19.appendleft(tmp22)
                        if len(subjects19) >= 1 and isinstance(subjects19[0], Mul):
                            tmp25 = subjects19.popleft()
                            associative1 = tmp25
                            associative_type1 = type(tmp25)
                            subjects26 = deque(tmp25._args)
                            matcher = CommutativeMatcher117925.get()
                            tmp27 = subjects26
                            subjects26 = []
                            for s in tmp27:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp27, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 117926
                                    if len(subjects19) == 0:
                                        pass
                                        # State 117927
                                        if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                            tmp28 = subjects3.popleft()
                                            # State 117928
                                            if len(subjects3) == 0:
                                                pass
                                                # State 117929
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1844)
                                                    yield 3, subst3
                                                    # 5: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1846)
                                                    yield 5, subst3
                                            subjects3.appendleft(tmp28)
                            subjects19.appendleft(tmp25)
                    if len(subjects19) >= 1 and isinstance(subjects19[0], Add):
                        tmp29 = subjects19.popleft()
                        associative1 = tmp29
                        associative_type1 = type(tmp29)
                        subjects30 = deque(tmp29._args)
                        matcher = CommutativeMatcher117931.get()
                        tmp31 = subjects30
                        subjects30 = []
                        for s in tmp31:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp31, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 117937
                                if len(subjects19) == 0:
                                    pass
                                    # State 117938
                                    if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                        tmp32 = subjects3.popleft()
                                        # State 117939
                                        if len(subjects3) == 0:
                                            pass
                                            # State 117940
                                            if len(subjects) == 0:
                                                pass
                                                # 3: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1844)
                                                yield 3, subst2
                                                # 5: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1846)
                                                yield 5, subst2
                                        subjects3.appendleft(tmp32)
                        subjects19.appendleft(tmp29)
                    subjects3.appendleft(tmp18)
                if len(subjects3) >= 1 and isinstance(subjects3[0], tanh):
                    tmp33 = subjects3.popleft()
                    subjects34 = deque(tmp33._args)
                    # State 118981
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 118982
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 118983
                            if len(subjects34) >= 1:
                                tmp37 = subjects34.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp37)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 118984
                                    if len(subjects34) == 0:
                                        pass
                                        # State 118985
                                        if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                            tmp39 = subjects3.popleft()
                                            # State 118986
                                            if len(subjects3) == 0:
                                                pass
                                                # State 118987
                                                if len(subjects) == 0:
                                                    pass
                                                    # 9: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1848)
                                                    yield 9, subst4
                                                    # 7: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1847)
                                                    yield 7, subst4
                                            subjects3.appendleft(tmp39)
                                subjects34.appendleft(tmp37)
                        if len(subjects34) >= 1 and isinstance(subjects34[0], Mul):
                            tmp40 = subjects34.popleft()
                            associative1 = tmp40
                            associative_type1 = type(tmp40)
                            subjects41 = deque(tmp40._args)
                            matcher = CommutativeMatcher118989.get()
                            tmp42 = subjects41
                            subjects41 = []
                            for s in tmp42:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp42, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 118990
                                    if len(subjects34) == 0:
                                        pass
                                        # State 118991
                                        if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                            tmp43 = subjects3.popleft()
                                            # State 118992
                                            if len(subjects3) == 0:
                                                pass
                                                # State 118993
                                                if len(subjects) == 0:
                                                    pass
                                                    # 9: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1848)
                                                    yield 9, subst3
                                                    # 7: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1847)
                                                    yield 7, subst3
                                            subjects3.appendleft(tmp43)
                            subjects34.appendleft(tmp40)
                    if len(subjects34) >= 1 and isinstance(subjects34[0], Add):
                        tmp44 = subjects34.popleft()
                        associative1 = tmp44
                        associative_type1 = type(tmp44)
                        subjects45 = deque(tmp44._args)
                        matcher = CommutativeMatcher118995.get()
                        tmp46 = subjects45
                        subjects45 = []
                        for s in tmp46:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp46, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 119001
                                if len(subjects34) == 0:
                                    pass
                                    # State 119002
                                    if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                        tmp47 = subjects3.popleft()
                                        # State 119003
                                        if len(subjects3) == 0:
                                            pass
                                            # State 119004
                                            if len(subjects) == 0:
                                                pass
                                                # 9: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1848)
                                                yield 9, subst2
                                                # 7: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1847)
                                                yield 7, subst2
                                        subjects3.appendleft(tmp47)
                        subjects34.appendleft(tmp44)
                    subjects3.appendleft(tmp33)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp48 = subjects.popleft()
                subjects49 = deque(tmp48._args)
                # State 117701
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 117702
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 117703
                        if len(subjects49) >= 1:
                            tmp52 = subjects49.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1.0', tmp52)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 117704
                                if len(subjects49) == 0:
                                    pass
                                    # State 117705
                                    if len(subjects) == 0:
                                        pass
                                        # 2: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1843)
                                        yield 2, subst4
                                        # 4: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1845)
                                        yield 4, subst4
                            subjects49.appendleft(tmp52)
                    if len(subjects49) >= 1 and isinstance(subjects49[0], Mul):
                        tmp54 = subjects49.popleft()
                        associative1 = tmp54
                        associative_type1 = type(tmp54)
                        subjects55 = deque(tmp54._args)
                        matcher = CommutativeMatcher117707.get()
                        tmp56 = subjects55
                        subjects55 = []
                        for s in tmp56:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp56, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 117708
                                if len(subjects49) == 0:
                                    pass
                                    # State 117709
                                    if len(subjects) == 0:
                                        pass
                                        # 2: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1843)
                                        yield 2, subst3
                                        # 4: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1845)
                                        yield 4, subst3
                        subjects49.appendleft(tmp54)
                if len(subjects49) >= 1 and isinstance(subjects49[0], Add):
                    tmp57 = subjects49.popleft()
                    associative1 = tmp57
                    associative_type1 = type(tmp57)
                    subjects58 = deque(tmp57._args)
                    matcher = CommutativeMatcher117711.get()
                    tmp59 = subjects58
                    subjects58 = []
                    for s in tmp59:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp59, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 117717
                            if len(subjects49) == 0:
                                pass
                                # State 117718
                                if len(subjects) == 0:
                                    pass
                                    # 2: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1843)
                                    yield 2, subst2
                                    # 4: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1845)
                                    yield 4, subst2
                    subjects49.appendleft(tmp57)
                subjects.appendleft(tmp48)
            if len(subjects) >= 1 and isinstance(subjects[0], tanh):
                tmp60 = subjects.popleft()
                subjects61 = deque(tmp60._args)
                # State 118765
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 118766
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 118767
                        if len(subjects61) >= 1:
                            tmp64 = subjects61.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1.0', tmp64)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 118768
                                if len(subjects61) == 0:
                                    pass
                                    # State 118769
                                    if len(subjects) == 0:
                                        pass
                                        # 8: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1848)
                                        yield 8, subst4
                                        # 6: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1847)
                                        yield 6, subst4
                            subjects61.appendleft(tmp64)
                    if len(subjects61) >= 1 and isinstance(subjects61[0], Mul):
                        tmp66 = subjects61.popleft()
                        associative1 = tmp66
                        associative_type1 = type(tmp66)
                        subjects67 = deque(tmp66._args)
                        matcher = CommutativeMatcher118771.get()
                        tmp68 = subjects67
                        subjects67 = []
                        for s in tmp68:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp68, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 118772
                                if len(subjects61) == 0:
                                    pass
                                    # State 118773
                                    if len(subjects) == 0:
                                        pass
                                        # 8: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1848)
                                        yield 8, subst3
                                        # 6: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1847)
                                        yield 6, subst3
                        subjects61.appendleft(tmp66)
                if len(subjects61) >= 1 and isinstance(subjects61[0], Add):
                    tmp69 = subjects61.popleft()
                    associative1 = tmp69
                    associative_type1 = type(tmp69)
                    subjects70 = deque(tmp69._args)
                    matcher = CommutativeMatcher118775.get()
                    tmp71 = subjects70
                    subjects70 = []
                    for s in tmp71:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp71, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 118781
                            if len(subjects61) == 0:
                                pass
                                # State 118782
                                if len(subjects) == 0:
                                    pass
                                    # 8: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1848)
                                    yield 8, subst2
                                    # 6: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1847)
                                    yield 6, subst2
                    subjects61.appendleft(tmp69)
                subjects.appendleft(tmp60)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp72 = subjects.popleft()
            associative1 = tmp72
            associative_type1 = type(tmp72)
            subjects73 = deque(tmp72._args)
            matcher = CommutativeMatcher115944.get()
            tmp74 = subjects73
            subjects73 = []
            for s in tmp74:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp74, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 115949
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f1833)
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 116207
                    if len(subjects) == 0:
                        pass
                        # 1: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f127) and (cons_f1836)
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 117737
                    if len(subjects) == 0:
                        pass
                        # 2: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1843)
                        yield 2, subst1
                        # 4: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1845)
                        yield 4, subst1
                if pattern_index == 3:
                    pass
                    # State 117965
                    if len(subjects) == 0:
                        pass
                        # 3: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1844)
                        yield 3, subst1
                        # 5: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1846)
                        yield 5, subst1
                if pattern_index == 4:
                    pass
                    # State 118801
                    if len(subjects) == 0:
                        pass
                        # 8: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1848)
                        yield 8, subst1
                        # 6: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1847)
                        yield 6, subst1
                if pattern_index == 5:
                    pass
                    # State 119029
                    if len(subjects) == 0:
                        pass
                        # 9: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1848)
                        yield 9, subst1
                        # 7: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1847)
                        yield 7, subst1
            subjects.appendleft(tmp72)
        return
        yield


from .generated_part010396 import *
from .generated_part010390 import *
from .generated_part010404 import *
from .generated_part010389 import *
from .generated_part010401 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part010402 import *
from .generated_part010393 import *
from collections import deque
from .generated_part010398 import *
from .generated_part010395 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part010399 import *
from .generated_part010392 import *