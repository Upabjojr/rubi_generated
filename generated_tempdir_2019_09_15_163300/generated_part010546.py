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


class CommutativeMatcher145156(CommutativeMatcher):
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
        if CommutativeMatcher145156._instance is None:
            CommutativeMatcher145156._instance = CommutativeMatcher145156()
        return CommutativeMatcher145156._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 145155
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 145157
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 145158
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 145159
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 145160
                                if len(subjects3) == 0:
                                    pass
                                    # State 145161
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
                            # State 145420
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.3.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 145421
                                if len(subjects3) >= 1:
                                    tmp10 = subjects3.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.1.3.1.0', tmp10)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 145422
                                        if len(subjects3) == 0:
                                            pass
                                            # State 145423
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
                                matcher = CommutativeMatcher145425.get()
                                tmp14 = subjects13
                                subjects13 = []
                                for s in tmp14:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp14, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 145426
                                        if len(subjects3) == 0:
                                            pass
                                            # State 145427
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
                            matcher = CommutativeMatcher145429.get()
                            tmp17 = subjects16
                            subjects16 = []
                            for s in tmp17:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp17, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 145435
                                    if len(subjects3) == 0:
                                        pass
                                        # State 145436
                                        if len(subjects) == 0:
                                            pass
                                            # 1: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f127) and (cons_f1836)
                                            yield 1, subst3
                            subjects3.appendleft(tmp15)
                    subjects3.appendleft(tmp4)
                if len(subjects3) >= 1 and isinstance(subjects3[0], tanh):
                    tmp18 = subjects3.popleft()
                    subjects19 = deque(tmp18._args)
                    # State 147112
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 147113
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 147114
                            if len(subjects19) >= 1:
                                tmp22 = subjects19.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp22)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 147115
                                    if len(subjects19) == 0:
                                        pass
                                        # State 147116
                                        if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                            tmp24 = subjects3.popleft()
                                            # State 147117
                                            if len(subjects3) == 0:
                                                pass
                                                # State 147118
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                                                    yield 3, subst4
                                                    # 5: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                                                    yield 5, subst4
                                            subjects3.appendleft(tmp24)
                                subjects19.appendleft(tmp22)
                        if len(subjects19) >= 1 and isinstance(subjects19[0], Mul):
                            tmp25 = subjects19.popleft()
                            associative1 = tmp25
                            associative_type1 = type(tmp25)
                            subjects26 = deque(tmp25._args)
                            matcher = CommutativeMatcher147120.get()
                            tmp27 = subjects26
                            subjects26 = []
                            for s in tmp27:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp27, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 147121
                                    if len(subjects19) == 0:
                                        pass
                                        # State 147122
                                        if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                            tmp28 = subjects3.popleft()
                                            # State 147123
                                            if len(subjects3) == 0:
                                                pass
                                                # State 147124
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                                                    yield 3, subst3
                                                    # 5: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                                                    yield 5, subst3
                                            subjects3.appendleft(tmp28)
                            subjects19.appendleft(tmp25)
                    if len(subjects19) >= 1 and isinstance(subjects19[0], Add):
                        tmp29 = subjects19.popleft()
                        associative1 = tmp29
                        associative_type1 = type(tmp29)
                        subjects30 = deque(tmp29._args)
                        matcher = CommutativeMatcher147126.get()
                        tmp31 = subjects30
                        subjects30 = []
                        for s in tmp31:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp31, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 147132
                                if len(subjects19) == 0:
                                    pass
                                    # State 147133
                                    if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                        tmp32 = subjects3.popleft()
                                        # State 147134
                                        if len(subjects3) == 0:
                                            pass
                                            # State 147135
                                            if len(subjects) == 0:
                                                pass
                                                # 3: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                                                yield 3, subst2
                                                # 5: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                                                yield 5, subst2
                                        subjects3.appendleft(tmp32)
                        subjects19.appendleft(tmp29)
                    subjects3.appendleft(tmp18)
                if len(subjects3) >= 1 and isinstance(subjects3[0], tan):
                    tmp33 = subjects3.popleft()
                    subjects34 = deque(tmp33._args)
                    # State 148176
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148177
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 148178
                            if len(subjects34) >= 1:
                                tmp37 = subjects34.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.3.1.0', tmp37)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 148179
                                    if len(subjects34) == 0:
                                        pass
                                        # State 148180
                                        if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                            tmp39 = subjects3.popleft()
                                            # State 148181
                                            if len(subjects3) == 0:
                                                pass
                                                # State 148182
                                                if len(subjects) == 0:
                                                    pass
                                                    # 9: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1950)
                                                    yield 9, subst4
                                                    # 7: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1948)
                                                    yield 7, subst4
                                            subjects3.appendleft(tmp39)
                                subjects34.appendleft(tmp37)
                        if len(subjects34) >= 1 and isinstance(subjects34[0], Mul):
                            tmp40 = subjects34.popleft()
                            associative1 = tmp40
                            associative_type1 = type(tmp40)
                            subjects41 = deque(tmp40._args)
                            matcher = CommutativeMatcher148184.get()
                            tmp42 = subjects41
                            subjects41 = []
                            for s in tmp42:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp42, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 148185
                                    if len(subjects34) == 0:
                                        pass
                                        # State 148186
                                        if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                            tmp43 = subjects3.popleft()
                                            # State 148187
                                            if len(subjects3) == 0:
                                                pass
                                                # State 148188
                                                if len(subjects) == 0:
                                                    pass
                                                    # 9: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1950)
                                                    yield 9, subst3
                                                    # 7: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1948)
                                                    yield 7, subst3
                                            subjects3.appendleft(tmp43)
                            subjects34.appendleft(tmp40)
                    if len(subjects34) >= 1 and isinstance(subjects34[0], Add):
                        tmp44 = subjects34.popleft()
                        associative1 = tmp44
                        associative_type1 = type(tmp44)
                        subjects45 = deque(tmp44._args)
                        matcher = CommutativeMatcher148190.get()
                        tmp46 = subjects45
                        subjects45 = []
                        for s in tmp46:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp46, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 148196
                                if len(subjects34) == 0:
                                    pass
                                    # State 148197
                                    if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                        tmp47 = subjects3.popleft()
                                        # State 148198
                                        if len(subjects3) == 0:
                                            pass
                                            # State 148199
                                            if len(subjects) == 0:
                                                pass
                                                # 9: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1950)
                                                yield 9, subst2
                                                # 7: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1948)
                                                yield 7, subst2
                                        subjects3.appendleft(tmp47)
                        subjects34.appendleft(tmp44)
                    subjects3.appendleft(tmp33)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], tanh):
                tmp48 = subjects.popleft()
                subjects49 = deque(tmp48._args)
                # State 146896
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 146897
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 146898
                        if len(subjects49) >= 1:
                            tmp52 = subjects49.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1.0', tmp52)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 146899
                                if len(subjects49) == 0:
                                    pass
                                    # State 146900
                                    if len(subjects) == 0:
                                        pass
                                        # 2: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                                        yield 2, subst4
                                        # 4: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                                        yield 4, subst4
                            subjects49.appendleft(tmp52)
                    if len(subjects49) >= 1 and isinstance(subjects49[0], Mul):
                        tmp54 = subjects49.popleft()
                        associative1 = tmp54
                        associative_type1 = type(tmp54)
                        subjects55 = deque(tmp54._args)
                        matcher = CommutativeMatcher146902.get()
                        tmp56 = subjects55
                        subjects55 = []
                        for s in tmp56:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp56, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 146903
                                if len(subjects49) == 0:
                                    pass
                                    # State 146904
                                    if len(subjects) == 0:
                                        pass
                                        # 2: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                                        yield 2, subst3
                                        # 4: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                                        yield 4, subst3
                        subjects49.appendleft(tmp54)
                if len(subjects49) >= 1 and isinstance(subjects49[0], Add):
                    tmp57 = subjects49.popleft()
                    associative1 = tmp57
                    associative_type1 = type(tmp57)
                    subjects58 = deque(tmp57._args)
                    matcher = CommutativeMatcher146906.get()
                    tmp59 = subjects58
                    subjects58 = []
                    for s in tmp59:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp59, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 146912
                            if len(subjects49) == 0:
                                pass
                                # State 146913
                                if len(subjects) == 0:
                                    pass
                                    # 2: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                                    yield 2, subst2
                                    # 4: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                                    yield 4, subst2
                    subjects49.appendleft(tmp57)
                subjects.appendleft(tmp48)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp60 = subjects.popleft()
                subjects61 = deque(tmp60._args)
                # State 147960
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 147961
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 147962
                        if len(subjects61) >= 1:
                            tmp64 = subjects61.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1.0', tmp64)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 147963
                                if len(subjects61) == 0:
                                    pass
                                    # State 147964
                                    if len(subjects) == 0:
                                        pass
                                        # 8: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1949)
                                        yield 8, subst4
                                        # 6: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1947)
                                        yield 6, subst4
                            subjects61.appendleft(tmp64)
                    if len(subjects61) >= 1 and isinstance(subjects61[0], Mul):
                        tmp66 = subjects61.popleft()
                        associative1 = tmp66
                        associative_type1 = type(tmp66)
                        subjects67 = deque(tmp66._args)
                        matcher = CommutativeMatcher147966.get()
                        tmp68 = subjects67
                        subjects67 = []
                        for s in tmp68:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp68, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 147967
                                if len(subjects61) == 0:
                                    pass
                                    # State 147968
                                    if len(subjects) == 0:
                                        pass
                                        # 8: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1949)
                                        yield 8, subst3
                                        # 6: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1947)
                                        yield 6, subst3
                        subjects61.appendleft(tmp66)
                if len(subjects61) >= 1 and isinstance(subjects61[0], Add):
                    tmp69 = subjects61.popleft()
                    associative1 = tmp69
                    associative_type1 = type(tmp69)
                    subjects70 = deque(tmp69._args)
                    matcher = CommutativeMatcher147970.get()
                    tmp71 = subjects70
                    subjects70 = []
                    for s in tmp71:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp71, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 147976
                            if len(subjects61) == 0:
                                pass
                                # State 147977
                                if len(subjects) == 0:
                                    pass
                                    # 8: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1949)
                                    yield 8, subst2
                                    # 6: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1947)
                                    yield 6, subst2
                    subjects61.appendleft(tmp69)
                subjects.appendleft(tmp60)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp72 = subjects.popleft()
            associative1 = tmp72
            associative_type1 = type(tmp72)
            subjects73 = deque(tmp72._args)
            matcher = CommutativeMatcher145163.get()
            tmp74 = subjects73
            subjects73 = []
            for s in tmp74:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp74, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 145168
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f1833)
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 145454
                    if len(subjects) == 0:
                        pass
                        # 1: b*F**(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f127) and (cons_f1836)
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 146932
                    if len(subjects) == 0:
                        pass
                        # 2: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                        yield 2, subst1
                        # 4: d*tanh(a + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                        yield 4, subst1
                if pattern_index == 3:
                    pass
                    # State 147160
                    if len(subjects) == 0:
                        pass
                        # 3: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1945)
                        yield 3, subst1
                        # 5: d/tanh(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1946)
                        yield 5, subst1
                if pattern_index == 4:
                    pass
                    # State 147996
                    if len(subjects) == 0:
                        pass
                        # 8: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1949)
                        yield 8, subst1
                        # 6: d*tan(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1947)
                        yield 6, subst1
                if pattern_index == 5:
                    pass
                    # State 148224
                    if len(subjects) == 0:
                        pass
                        # 9: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1950)
                        yield 9, subst1
                        # 7: d/tan(d + x*e) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1948)
                        yield 7, subst1
            subjects.appendleft(tmp72)
        return
        yield


from .generated_part010559 import *
from .generated_part010556 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part010551 import *
from .generated_part010550 import *
from .generated_part010557 import *
from collections import deque
from .generated_part010548 import *
from .generated_part010553 import *
from .generated_part010554 import *
from multiset import Multiset
from .generated_part010562 import *
from .generated_part010560 import *
from matchpy.utils import VariableWithCount
from .generated_part010547 import *