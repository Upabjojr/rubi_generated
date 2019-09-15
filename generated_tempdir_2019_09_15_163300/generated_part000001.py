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


class CommutativeMatcher2199(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    3: (3, Multiset({2: 1, 4: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({5: 1, 3: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({6: 1, 7: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({8: 1, 9: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    7: (7, Multiset({10: 1, 11: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    8: (8, Multiset({12: 1, 13: 1}), [
      
]),
    9: (9, Multiset({14: 1, 15: 1, 16: 1}), [
      
]),
    10: (10, Multiset({17: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    11: (11, Multiset({18: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    12: (12, Multiset({19: 1, 20: 1}), [
      
]),
    13: (13, Multiset({21: 1, 22: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    14: (14, Multiset({23: 1, 24: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    15: (15, Multiset({25: 1, 26: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    16: (16, Multiset({27: 1, 28: 1}), [
      
]),
    17: (17, Multiset({29: 1, 30: 1}), [
      
]),
    18: (18, Multiset({31: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    19: (19, Multiset({32: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    20: (20, Multiset({33: 1, 34: 1}), [
      
]),
    21: (21, Multiset({35: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    22: (22, Multiset({36: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher2199._instance is None:
            CommutativeMatcher2199._instance = CommutativeMatcher2199()
        return CommutativeMatcher2199._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2198
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2200
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2201
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2202
                        if len(subjects) == 0:
                            pass
                            # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                            yield 0, subst3
                            # 1: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                            yield 1, subst3
                            # 2: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                            yield 2, subst3
                            # 5: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                            yield 5, subst3
                            # 12: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                            yield 12, subst3
                            # 14: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                            yield 14, subst3
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 2203
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2204
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2205
                            if len(subjects6) == 0:
                                pass
                                # State 2206
                                if len(subjects) == 0:
                                    pass
                                    # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                    yield 0, subst3
                                    # 1: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                    yield 1, subst3
                                    # 2: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                    yield 2, subst3
                                    # 5: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                    yield 5, subst3
                                    # 12: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                    yield 12, subst3
                                    # 14: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                    yield 14, subst3
                        if len(subjects6) >= 1:
                            tmp10 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 2205
                                if len(subjects6) == 0:
                                    pass
                                    # State 2206
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                        yield 0, subst3
                                        # 1: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                        yield 1, subst3
                                        # 2: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                        yield 2, subst3
                                        # 5: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                        yield 5, subst3
                                        # 12: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                        yield 12, subst3
                                        # 14: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                        yield 14, subst3
                            subjects6.appendleft(tmp10)
                        if len(subjects6) >= 1:
                            tmp12 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 2746
                                if len(subjects6) == 0:
                                    pass
                                    # State 2747
                                    if len(subjects) == 0:
                                        pass
                                        # 10: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                        yield 10, subst3
                            subjects6.appendleft(tmp12)
                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                            tmp14 = subjects6.popleft()
                            # State 2703
                            if len(subjects6) == 0:
                                pass
                                # State 2704
                                if len(subjects) == 0:
                                    pass
                                    # 8: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                                    yield 8, subst2
                            subjects6.appendleft(tmp14)
                    subjects6.appendleft(tmp7)
                if len(subjects6) >= 1 and isinstance(subjects6[0], cos):
                    tmp15 = subjects6.popleft()
                    subjects16 = deque(tmp15._args)
                    # State 101671
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101672
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 101673
                            if len(subjects16) >= 1:
                                tmp19 = subjects16.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.3.1.0', tmp19)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 101674
                                    if len(subjects16) == 0:
                                        pass
                                        # State 101675
                                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                            tmp21 = subjects6.popleft()
                                            # State 101676
                                            if len(subjects6) == 0:
                                                pass
                                                # State 101677
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: b*cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                                                    yield 21, subst4
                                            subjects6.appendleft(tmp21)
                                        if len(subjects6) >= 1 and subjects6[0] == Integer(-2):
                                            tmp22 = subjects6.popleft()
                                            # State 101915
                                            if len(subjects6) == 0:
                                                pass
                                                # State 101916
                                                if len(subjects) == 0:
                                                    pass
                                                    # 23: c/cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                                    yield 23, subst4
                                            subjects6.appendleft(tmp22)
                                subjects16.appendleft(tmp19)
                        if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                            tmp23 = subjects16.popleft()
                            associative1 = tmp23
                            associative_type1 = type(tmp23)
                            subjects24 = deque(tmp23._args)
                            matcher = CommutativeMatcher101679.get()
                            tmp25 = subjects24
                            subjects24 = []
                            for s in tmp25:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp25, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 101680
                                    if len(subjects16) == 0:
                                        pass
                                        # State 101681
                                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                            tmp26 = subjects6.popleft()
                                            # State 101682
                                            if len(subjects6) == 0:
                                                pass
                                                # State 101683
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: b*cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                                                    yield 21, subst3
                                            subjects6.appendleft(tmp26)
                                        if len(subjects6) >= 1 and subjects6[0] == Integer(-2):
                                            tmp27 = subjects6.popleft()
                                            # State 101917
                                            if len(subjects6) == 0:
                                                pass
                                                # State 101918
                                                if len(subjects) == 0:
                                                    pass
                                                    # 23: c/cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                                    yield 23, subst3
                                            subjects6.appendleft(tmp27)
                            subjects16.appendleft(tmp23)
                    if len(subjects16) >= 1 and isinstance(subjects16[0], Add):
                        tmp28 = subjects16.popleft()
                        associative1 = tmp28
                        associative_type1 = type(tmp28)
                        subjects29 = deque(tmp28._args)
                        matcher = CommutativeMatcher101685.get()
                        tmp30 = subjects29
                        subjects29 = []
                        for s in tmp30:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp30, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 101691
                                if len(subjects16) == 0:
                                    pass
                                    # State 101692
                                    if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                                        tmp31 = subjects6.popleft()
                                        # State 101693
                                        if len(subjects6) == 0:
                                            pass
                                            # State 101694
                                            if len(subjects) == 0:
                                                pass
                                                # 21: b*cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                                                yield 21, subst2
                                        subjects6.appendleft(tmp31)
                                    if len(subjects6) >= 1 and subjects6[0] == Integer(-2):
                                        tmp32 = subjects6.popleft()
                                        # State 101919
                                        if len(subjects6) == 0:
                                            pass
                                            # State 101920
                                            if len(subjects) == 0:
                                                pass
                                                # 23: c/cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                                yield 23, subst2
                                        subjects6.appendleft(tmp32)
                        subjects16.appendleft(tmp28)
                    subjects6.appendleft(tmp15)
                if len(subjects6) >= 1 and isinstance(subjects6[0], sin):
                    tmp33 = subjects6.popleft()
                    subjects34 = deque(tmp33._args)
                    # State 102094
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102095
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102096
                            if len(subjects34) >= 1:
                                tmp37 = subjects34.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.3.1.0', tmp37)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102097
                                    if len(subjects34) == 0:
                                        pass
                                        # State 102098
                                        if len(subjects6) >= 1 and subjects6[0] == Integer(-2):
                                            tmp39 = subjects6.popleft()
                                            # State 102099
                                            if len(subjects6) == 0:
                                                pass
                                                # State 102100
                                                if len(subjects) == 0:
                                                    pass
                                                    # 25: c/sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                                    yield 25, subst4
                                            subjects6.appendleft(tmp39)
                                subjects34.appendleft(tmp37)
                        if len(subjects34) >= 1 and isinstance(subjects34[0], Mul):
                            tmp40 = subjects34.popleft()
                            associative1 = tmp40
                            associative_type1 = type(tmp40)
                            subjects41 = deque(tmp40._args)
                            matcher = CommutativeMatcher102102.get()
                            tmp42 = subjects41
                            subjects41 = []
                            for s in tmp42:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp42, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102103
                                    if len(subjects34) == 0:
                                        pass
                                        # State 102104
                                        if len(subjects6) >= 1 and subjects6[0] == Integer(-2):
                                            tmp43 = subjects6.popleft()
                                            # State 102105
                                            if len(subjects6) == 0:
                                                pass
                                                # State 102106
                                                if len(subjects) == 0:
                                                    pass
                                                    # 25: c/sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                                    yield 25, subst3
                                            subjects6.appendleft(tmp43)
                            subjects34.appendleft(tmp40)
                    if len(subjects34) >= 1 and isinstance(subjects34[0], Add):
                        tmp44 = subjects34.popleft()
                        associative1 = tmp44
                        associative_type1 = type(tmp44)
                        subjects45 = deque(tmp44._args)
                        matcher = CommutativeMatcher102108.get()
                        tmp46 = subjects45
                        subjects45 = []
                        for s in tmp46:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp46, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102114
                                if len(subjects34) == 0:
                                    pass
                                    # State 102115
                                    if len(subjects6) >= 1 and subjects6[0] == Integer(-2):
                                        tmp47 = subjects6.popleft()
                                        # State 102116
                                        if len(subjects6) == 0:
                                            pass
                                            # State 102117
                                            if len(subjects) == 0:
                                                pass
                                                # 25: c/sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                                yield 25, subst2
                                        subjects6.appendleft(tmp47)
                        subjects34.appendleft(tmp44)
                    subjects6.appendleft(tmp33)
                subjects.appendleft(tmp5)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp48 = subjects.popleft()
                subjects49 = deque(tmp48._args)
                # State 41288
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 41289
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 41290
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 41291
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.2.1.2.2.2', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 41292
                                if len(subjects49) >= 1 and isinstance(subjects49[0], Add):
                                    tmp54 = subjects49.popleft()
                                    associative1 = tmp54
                                    associative_type1 = type(tmp54)
                                    subjects55 = deque(tmp54._args)
                                    matcher = CommutativeMatcher41294.get()
                                    tmp56 = subjects55
                                    subjects55 = []
                                    for s in tmp56:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp56, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 41310
                                            if len(subjects49) == 0:
                                                pass
                                                # State 41311
                                                if len(subjects) == 0:
                                                    pass
                                                    # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                    yield 17, subst6
                                    subjects49.appendleft(tmp54)
                                if len(subjects49) >= 1:
                                    tmp57 = subjects49.popleft()
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.1', tmp57)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45015
                                        if len(subjects49) == 0:
                                            pass
                                            # State 45016
                                            if len(subjects) == 0:
                                                pass
                                                # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                yield 18, subst6
                                    subjects49.appendleft(tmp57)
                            if len(subjects49) >= 1 and isinstance(subjects49[0], Pow):
                                tmp59 = subjects49.popleft()
                                subjects60 = deque(tmp59._args)
                                # State 41312
                                if len(subjects60) >= 1 and isinstance(subjects60[0], Add):
                                    tmp61 = subjects60.popleft()
                                    associative1 = tmp61
                                    associative_type1 = type(tmp61)
                                    subjects62 = deque(tmp61._args)
                                    matcher = CommutativeMatcher41314.get()
                                    tmp63 = subjects62
                                    subjects62 = []
                                    for s in tmp63:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp63, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 41330
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 41331
                                                if len(subjects60) == 0:
                                                    pass
                                                    # State 41332
                                                    if len(subjects49) == 0:
                                                        pass
                                                        # State 41333
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                            yield 17, subst6
                                            if len(subjects60) >= 1:
                                                tmp65 = []
                                                tmp65.append(subjects60.popleft())
                                                while True:
                                                    if len(tmp65) > 1:
                                                        tmp66 = create_operation_expression(associative1, tmp65)
                                                    elif len(tmp65) == 1:
                                                        tmp66 = tmp65[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', tmp66)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 41331
                                                        if len(subjects60) == 0:
                                                            pass
                                                            # State 41332
                                                            if len(subjects49) == 0:
                                                                pass
                                                                # State 41333
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                    yield 17, subst6
                                                    if len(subjects60) == 0:
                                                        break
                                                    tmp65.append(subjects60.popleft())
                                                subjects60.extendleft(reversed(tmp65))
                                    subjects60.appendleft(tmp61)
                                if len(subjects60) >= 1:
                                    tmp68 = subjects60.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.1', tmp68)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45017
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45018
                                            if len(subjects60) == 0:
                                                pass
                                                # State 45019
                                                if len(subjects49) == 0:
                                                    pass
                                                    # State 45020
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                        yield 18, subst6
                                        if len(subjects60) >= 1:
                                            tmp71 = subjects60.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', tmp71)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45018
                                                if len(subjects60) == 0:
                                                    pass
                                                    # State 45019
                                                    if len(subjects49) == 0:
                                                        pass
                                                        # State 45020
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                            yield 18, subst6
                                            subjects60.appendleft(tmp71)
                                    subjects60.appendleft(tmp68)
                                subjects49.appendleft(tmp59)
                        if len(subjects49) >= 1 and isinstance(subjects49[0], Mul):
                            tmp73 = subjects49.popleft()
                            associative1 = tmp73
                            associative_type1 = type(tmp73)
                            subjects74 = deque(tmp73._args)
                            matcher = CommutativeMatcher41335.get()
                            tmp75 = subjects74
                            subjects74 = []
                            for s in tmp75:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp75, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 41376
                                    if len(subjects49) == 0:
                                        pass
                                        # State 41377
                                        if len(subjects) == 0:
                                            pass
                                            # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                            yield 17, subst4
                                if pattern_index == 1:
                                    pass
                                    # State 45025
                                    if len(subjects49) == 0:
                                        pass
                                        # State 45026
                                        if len(subjects) == 0:
                                            pass
                                            # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                            yield 18, subst4
                            subjects49.appendleft(tmp73)
                    if len(subjects49) >= 1 and isinstance(subjects49[0], Pow):
                        tmp76 = subjects49.popleft()
                        subjects77 = deque(tmp76._args)
                        # State 41378
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 41379
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 41380
                                if len(subjects77) >= 1 and isinstance(subjects77[0], Add):
                                    tmp80 = subjects77.popleft()
                                    associative1 = tmp80
                                    associative_type1 = type(tmp80)
                                    subjects81 = deque(tmp80._args)
                                    matcher = CommutativeMatcher41382.get()
                                    tmp82 = subjects81
                                    subjects81 = []
                                    for s in tmp82:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp82, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 41398
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 41399
                                                if len(subjects77) == 0:
                                                    pass
                                                    # State 41400
                                                    if len(subjects49) == 0:
                                                        pass
                                                        # State 41401
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                            yield 17, subst6
                                            if len(subjects77) >= 1:
                                                tmp84 = []
                                                tmp84.append(subjects77.popleft())
                                                while True:
                                                    if len(tmp84) > 1:
                                                        tmp85 = create_operation_expression(associative1, tmp84)
                                                    elif len(tmp84) == 1:
                                                        tmp85 = tmp84[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp85)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 41399
                                                        if len(subjects77) == 0:
                                                            pass
                                                            # State 41400
                                                            if len(subjects49) == 0:
                                                                pass
                                                                # State 41401
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                    yield 17, subst6
                                                    if len(subjects77) == 0:
                                                        break
                                                    tmp84.append(subjects77.popleft())
                                                subjects77.extendleft(reversed(tmp84))
                                    subjects77.appendleft(tmp80)
                                if len(subjects77) >= 1:
                                    tmp87 = subjects77.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.1', tmp87)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45027
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45028
                                            if len(subjects77) == 0:
                                                pass
                                                # State 45029
                                                if len(subjects49) == 0:
                                                    pass
                                                    # State 45030
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                        yield 18, subst6
                                        if len(subjects77) >= 1:
                                            tmp90 = subjects77.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', tmp90)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45028
                                                if len(subjects77) == 0:
                                                    pass
                                                    # State 45029
                                                    if len(subjects49) == 0:
                                                        pass
                                                        # State 45030
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                            yield 18, subst6
                                            subjects77.appendleft(tmp90)
                                    subjects77.appendleft(tmp87)
                            if len(subjects77) >= 1 and isinstance(subjects77[0], Pow):
                                tmp92 = subjects77.popleft()
                                subjects93 = deque(tmp92._args)
                                # State 41402
                                if len(subjects93) >= 1 and isinstance(subjects93[0], Add):
                                    tmp94 = subjects93.popleft()
                                    associative1 = tmp94
                                    associative_type1 = type(tmp94)
                                    subjects95 = deque(tmp94._args)
                                    matcher = CommutativeMatcher41404.get()
                                    tmp96 = subjects95
                                    subjects95 = []
                                    for s in tmp96:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp96, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 41420
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 41421
                                                if len(subjects93) == 0:
                                                    pass
                                                    # State 41422
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 41423
                                                        if len(subjects77) == 0:
                                                            pass
                                                            # State 41424
                                                            if len(subjects49) == 0:
                                                                pass
                                                                # State 41425
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                    yield 17, subst6
                                                    if len(subjects77) >= 1:
                                                        tmp99 = subjects77.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp99)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 41423
                                                            if len(subjects77) == 0:
                                                                pass
                                                                # State 41424
                                                                if len(subjects49) == 0:
                                                                    pass
                                                                    # State 41425
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                        yield 17, subst6
                                                        subjects77.appendleft(tmp99)
                                            if len(subjects93) >= 1:
                                                tmp101 = []
                                                tmp101.append(subjects93.popleft())
                                                while True:
                                                    if len(tmp101) > 1:
                                                        tmp102 = create_operation_expression(associative1, tmp101)
                                                    elif len(tmp101) == 1:
                                                        tmp102 = tmp101[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2.2', tmp102)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 41421
                                                        if len(subjects93) == 0:
                                                            pass
                                                            # State 41422
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 41423
                                                                if len(subjects77) == 0:
                                                                    pass
                                                                    # State 41424
                                                                    if len(subjects49) == 0:
                                                                        pass
                                                                        # State 41425
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                            yield 17, subst6
                                                            if len(subjects77) >= 1:
                                                                tmp105 = subjects77.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2.1.2.2', tmp105)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 41423
                                                                    if len(subjects77) == 0:
                                                                        pass
                                                                        # State 41424
                                                                        if len(subjects49) == 0:
                                                                            pass
                                                                            # State 41425
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                                yield 17, subst6
                                                                subjects77.appendleft(tmp105)
                                                    if len(subjects93) == 0:
                                                        break
                                                    tmp101.append(subjects93.popleft())
                                                subjects93.extendleft(reversed(tmp101))
                                    subjects93.appendleft(tmp94)
                                if len(subjects93) >= 1:
                                    tmp107 = subjects93.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.1', tmp107)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45031
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45032
                                            if len(subjects93) == 0:
                                                pass
                                                # State 45033
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 45034
                                                    if len(subjects77) == 0:
                                                        pass
                                                        # State 45035
                                                        if len(subjects49) == 0:
                                                            pass
                                                            # State 45036
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                                yield 18, subst6
                                                if len(subjects77) >= 1:
                                                    tmp111 = subjects77.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp111)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 45034
                                                        if len(subjects77) == 0:
                                                            pass
                                                            # State 45035
                                                            if len(subjects49) == 0:
                                                                pass
                                                                # State 45036
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                                    yield 18, subst6
                                                    subjects77.appendleft(tmp111)
                                        if len(subjects93) >= 1:
                                            tmp113 = subjects93.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', tmp113)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45032
                                                if len(subjects93) == 0:
                                                    pass
                                                    # State 45033
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 45034
                                                        if len(subjects77) == 0:
                                                            pass
                                                            # State 45035
                                                            if len(subjects49) == 0:
                                                                pass
                                                                # State 45036
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                                    yield 18, subst6
                                                    if len(subjects77) >= 1:
                                                        tmp116 = subjects77.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp116)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 45034
                                                            if len(subjects77) == 0:
                                                                pass
                                                                # State 45035
                                                                if len(subjects49) == 0:
                                                                    pass
                                                                    # State 45036
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                                        yield 18, subst6
                                                        subjects77.appendleft(tmp116)
                                            subjects93.appendleft(tmp113)
                                    subjects93.appendleft(tmp107)
                                subjects77.appendleft(tmp92)
                        if len(subjects77) >= 1 and isinstance(subjects77[0], Mul):
                            tmp118 = subjects77.popleft()
                            associative1 = tmp118
                            associative_type1 = type(tmp118)
                            subjects119 = deque(tmp118._args)
                            matcher = CommutativeMatcher41427.get()
                            tmp120 = subjects119
                            subjects119 = []
                            for s in tmp120:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp120, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 41468
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 41469
                                        if len(subjects77) == 0:
                                            pass
                                            # State 41470
                                            if len(subjects49) == 0:
                                                pass
                                                # State 41471
                                                if len(subjects) == 0:
                                                    pass
                                                    # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                    yield 17, subst4
                                    if len(subjects77) >= 1:
                                        tmp122 = []
                                        tmp122.append(subjects77.popleft())
                                        while True:
                                            if len(tmp122) > 1:
                                                tmp123 = create_operation_expression(associative1, tmp122)
                                            elif len(tmp122) == 1:
                                                tmp123 = tmp122[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp123)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 41469
                                                if len(subjects77) == 0:
                                                    pass
                                                    # State 41470
                                                    if len(subjects49) == 0:
                                                        pass
                                                        # State 41471
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                            yield 17, subst4
                                            if len(subjects77) == 0:
                                                break
                                            tmp122.append(subjects77.popleft())
                                        subjects77.extendleft(reversed(tmp122))
                                if pattern_index == 1:
                                    pass
                                    # State 45041
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45042
                                        if len(subjects77) == 0:
                                            pass
                                            # State 45043
                                            if len(subjects49) == 0:
                                                pass
                                                # State 45044
                                                if len(subjects) == 0:
                                                    pass
                                                    # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                    yield 18, subst4
                                    if len(subjects77) >= 1:
                                        tmp126 = []
                                        tmp126.append(subjects77.popleft())
                                        while True:
                                            if len(tmp126) > 1:
                                                tmp127 = create_operation_expression(associative1, tmp126)
                                            elif len(tmp126) == 1:
                                                tmp127 = tmp126[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp127)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45042
                                                if len(subjects77) == 0:
                                                    pass
                                                    # State 45043
                                                    if len(subjects49) == 0:
                                                        pass
                                                        # State 45044
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                            yield 18, subst4
                                            if len(subjects77) == 0:
                                                break
                                            tmp126.append(subjects77.popleft())
                                        subjects77.extendleft(reversed(tmp126))
                            subjects77.appendleft(tmp118)
                        subjects49.appendleft(tmp76)
                if len(subjects49) >= 1 and isinstance(subjects49[0], Mul):
                    tmp129 = subjects49.popleft()
                    associative1 = tmp129
                    associative_type1 = type(tmp129)
                    subjects130 = deque(tmp129._args)
                    matcher = CommutativeMatcher41473.get()
                    tmp131 = subjects130
                    subjects130 = []
                    for s in tmp131:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp131, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 41650
                            if len(subjects49) == 0:
                                pass
                                # State 41651
                                if len(subjects) == 0:
                                    pass
                                    # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                    yield 17, subst2
                        if pattern_index == 1:
                            pass
                            # State 45069
                            if len(subjects49) == 0:
                                pass
                                # State 45070
                                if len(subjects) == 0:
                                    pass
                                    # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                    yield 18, subst2
                    subjects49.appendleft(tmp129)
                subjects.appendleft(tmp48)
            if len(subjects) >= 1 and isinstance(subjects[0], cos):
                tmp132 = subjects.popleft()
                subjects133 = deque(tmp132._args)
                # State 103209
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 103210
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 103211
                        if len(subjects133) >= 1:
                            tmp136 = subjects133.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.1.0', tmp136)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 103212
                                if len(subjects133) == 0:
                                    pass
                                    # State 103213
                                    if len(subjects) == 0:
                                        pass
                                        # 27: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                        yield 27, subst4
                            subjects133.appendleft(tmp136)
                    if len(subjects133) >= 1 and isinstance(subjects133[0], Mul):
                        tmp138 = subjects133.popleft()
                        associative1 = tmp138
                        associative_type1 = type(tmp138)
                        subjects139 = deque(tmp138._args)
                        matcher = CommutativeMatcher103215.get()
                        tmp140 = subjects139
                        subjects139 = []
                        for s in tmp140:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp140, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 103216
                                if len(subjects133) == 0:
                                    pass
                                    # State 103217
                                    if len(subjects) == 0:
                                        pass
                                        # 27: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                        yield 27, subst3
                        subjects133.appendleft(tmp138)
                if len(subjects133) >= 1:
                    tmp141 = subjects133.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp141)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 107914
                        if len(subjects133) == 0:
                            pass
                            # State 107915
                            if len(subjects) == 0:
                                pass
                                # 29: a*cos(v) /; (cons_f2) and (cons_f1441)
                                yield 29, subst2
                    subjects133.appendleft(tmp141)
                if len(subjects133) >= 1 and isinstance(subjects133[0], Add):
                    tmp143 = subjects133.popleft()
                    associative1 = tmp143
                    associative_type1 = type(tmp143)
                    subjects144 = deque(tmp143._args)
                    matcher = CommutativeMatcher103219.get()
                    tmp145 = subjects144
                    subjects144 = []
                    for s in tmp145:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp145, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 103225
                            if len(subjects133) == 0:
                                pass
                                # State 103226
                                if len(subjects) == 0:
                                    pass
                                    # 27: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                    yield 27, subst2
                    subjects133.appendleft(tmp143)
                subjects.appendleft(tmp132)
            if len(subjects) >= 1 and isinstance(subjects[0], asin):
                tmp146 = subjects.popleft()
                subjects147 = deque(tmp146._args)
                # State 110083
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 110084
                    if len(subjects147) >= 1:
                        tmp149 = subjects147.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.0', tmp149)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 110085
                            if len(subjects147) == 0:
                                pass
                                # State 110086
                                if len(subjects) == 0:
                                    pass
                                    # 31: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 31, subst3
                        subjects147.appendleft(tmp149)
                if len(subjects147) >= 1 and isinstance(subjects147[0], Mul):
                    tmp151 = subjects147.popleft()
                    associative1 = tmp151
                    associative_type1 = type(tmp151)
                    subjects152 = deque(tmp151._args)
                    matcher = CommutativeMatcher110088.get()
                    tmp153 = subjects152
                    subjects152 = []
                    for s in tmp153:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp153, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 110089
                            if len(subjects147) == 0:
                                pass
                                # State 110090
                                if len(subjects) == 0:
                                    pass
                                    # 31: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 31, subst2
                    subjects147.appendleft(tmp151)
                subjects.appendleft(tmp146)
            if len(subjects) >= 1 and isinstance(subjects[0], acos):
                tmp154 = subjects.popleft()
                subjects155 = deque(tmp154._args)
                # State 110180
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 110181
                    if len(subjects155) >= 1:
                        tmp157 = subjects155.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.0', tmp157)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 110182
                            if len(subjects155) == 0:
                                pass
                                # State 110183
                                if len(subjects) == 0:
                                    pass
                                    # 32: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 32, subst3
                        subjects155.appendleft(tmp157)
                if len(subjects155) >= 1 and isinstance(subjects155[0], Mul):
                    tmp159 = subjects155.popleft()
                    associative1 = tmp159
                    associative_type1 = type(tmp159)
                    subjects160 = deque(tmp159._args)
                    matcher = CommutativeMatcher110185.get()
                    tmp161 = subjects160
                    subjects160 = []
                    for s in tmp161:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp161, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 110186
                            if len(subjects155) == 0:
                                pass
                                # State 110187
                                if len(subjects) == 0:
                                    pass
                                    # 32: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 32, subst2
                    subjects155.appendleft(tmp159)
                subjects.appendleft(tmp154)
            if len(subjects) >= 1 and isinstance(subjects[0], cosh):
                tmp162 = subjects.popleft()
                subjects163 = deque(tmp162._args)
                # State 137643
                if len(subjects163) >= 1:
                    tmp164 = subjects163.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp164)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137644
                        if len(subjects163) == 0:
                            pass
                            # State 137645
                            if len(subjects) == 0:
                                pass
                                # 33: a*cosh(v) /; (cons_f2) and (cons_f1267)
                                yield 33, subst2
                    subjects163.appendleft(tmp164)
                subjects.appendleft(tmp162)
            if len(subjects) >= 1 and isinstance(subjects[0], asinh):
                tmp166 = subjects.popleft()
                subjects167 = deque(tmp166._args)
                # State 139818
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 139819
                    if len(subjects167) >= 1:
                        tmp169 = subjects167.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.0', tmp169)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 139820
                            if len(subjects167) == 0:
                                pass
                                # State 139821
                                if len(subjects) == 0:
                                    pass
                                    # 35: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 35, subst3
                        subjects167.appendleft(tmp169)
                if len(subjects167) >= 1 and isinstance(subjects167[0], Mul):
                    tmp171 = subjects167.popleft()
                    associative1 = tmp171
                    associative_type1 = type(tmp171)
                    subjects172 = deque(tmp171._args)
                    matcher = CommutativeMatcher139823.get()
                    tmp173 = subjects172
                    subjects172 = []
                    for s in tmp173:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp173, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 139824
                            if len(subjects167) == 0:
                                pass
                                # State 139825
                                if len(subjects) == 0:
                                    pass
                                    # 35: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 35, subst2
                    subjects167.appendleft(tmp171)
                subjects.appendleft(tmp166)
            if len(subjects) >= 1 and isinstance(subjects[0], acosh):
                tmp174 = subjects.popleft()
                subjects175 = deque(tmp174._args)
                # State 139915
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 139916
                    if len(subjects175) >= 1:
                        tmp177 = subjects175.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.0', tmp177)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 139917
                            if len(subjects175) == 0:
                                pass
                                # State 139918
                                if len(subjects) == 0:
                                    pass
                                    # 36: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 36, subst3
                        subjects175.appendleft(tmp177)
                if len(subjects175) >= 1 and isinstance(subjects175[0], Mul):
                    tmp179 = subjects175.popleft()
                    associative1 = tmp179
                    associative_type1 = type(tmp179)
                    subjects180 = deque(tmp179._args)
                    matcher = CommutativeMatcher139920.get()
                    tmp181 = subjects180
                    subjects180 = []
                    for s in tmp181:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp181, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 139921
                            if len(subjects175) == 0:
                                pass
                                # State 139922
                                if len(subjects) == 0:
                                    pass
                                    # 36: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 36, subst2
                    subjects175.appendleft(tmp179)
                subjects.appendleft(tmp174)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2397
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2398
                if len(subjects) >= 1:
                    tmp184 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp184)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2399
                        if len(subjects) == 0:
                            pass
                            # 3: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                            yield 3, subst3
                            # 4: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                            yield 4, subst3
                            # 11: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                            yield 11, subst3
                            # 13: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                            yield 13, subst3
                            # 15: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                            yield 15, subst3
                    subjects.appendleft(tmp184)
            if len(subjects) >= 1:
                tmp186 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp186)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2486
                    if len(subjects) == 0:
                        pass
                        # 19: x*f /; (cons_f2)
                        yield 19, subst2
                        # 6: v*a /; (cons_f2) and (cons_f10)
                        yield 6, subst2
                subjects.appendleft(tmp186)
            if len(subjects) >= 1:
                tmp188 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp188)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2708
                    if len(subjects) == 0:
                        pass
                        # 9: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                        yield 9, subst2
                subjects.appendleft(tmp188)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp190 = subjects.popleft()
                subjects191 = deque(tmp190._args)
                # State 2400
                if len(subjects191) >= 1:
                    tmp192 = subjects191.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp192)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2401
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2402
                            if len(subjects191) == 0:
                                pass
                                # State 2403
                                if len(subjects) == 0:
                                    pass
                                    # 3: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                    yield 3, subst3
                                    # 4: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                    yield 4, subst3
                                    # 11: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                    yield 11, subst3
                                    # 13: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                    yield 13, subst3
                                    # 15: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                    yield 15, subst3
                        if len(subjects191) >= 1:
                            tmp195 = subjects191.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp195)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 2402
                                if len(subjects191) == 0:
                                    pass
                                    # State 2403
                                    if len(subjects) == 0:
                                        pass
                                        # 3: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                        yield 3, subst3
                                        # 4: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                        yield 4, subst3
                                        # 11: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                        yield 11, subst3
                                        # 13: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                        yield 13, subst3
                                        # 15: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                        yield 15, subst3
                            subjects191.appendleft(tmp195)
                    subjects191.appendleft(tmp192)
                if len(subjects191) >= 1 and isinstance(subjects191[0], sin):
                    tmp197 = subjects191.popleft()
                    subjects198 = deque(tmp197._args)
                    # State 101720
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101721
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 101722
                            if len(subjects198) >= 1:
                                tmp201 = subjects198.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.3.1.0', tmp201)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 101723
                                    if len(subjects198) == 0:
                                        pass
                                        # State 101724
                                        if len(subjects191) >= 1 and subjects191[0] == Integer(2):
                                            tmp203 = subjects191.popleft()
                                            # State 101725
                                            if len(subjects191) == 0:
                                                pass
                                                # State 101726
                                                if len(subjects) == 0:
                                                    pass
                                                    # 22: c*sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                                                    yield 22, subst4
                                            subjects191.appendleft(tmp203)
                                subjects198.appendleft(tmp201)
                        if len(subjects198) >= 1 and isinstance(subjects198[0], Mul):
                            tmp204 = subjects198.popleft()
                            associative1 = tmp204
                            associative_type1 = type(tmp204)
                            subjects205 = deque(tmp204._args)
                            matcher = CommutativeMatcher101728.get()
                            tmp206 = subjects205
                            subjects205 = []
                            for s in tmp206:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp206, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 101729
                                    if len(subjects198) == 0:
                                        pass
                                        # State 101730
                                        if len(subjects191) >= 1 and subjects191[0] == Integer(2):
                                            tmp207 = subjects191.popleft()
                                            # State 101731
                                            if len(subjects191) == 0:
                                                pass
                                                # State 101732
                                                if len(subjects) == 0:
                                                    pass
                                                    # 22: c*sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                                                    yield 22, subst3
                                            subjects191.appendleft(tmp207)
                            subjects198.appendleft(tmp204)
                    if len(subjects198) >= 1 and isinstance(subjects198[0], Add):
                        tmp208 = subjects198.popleft()
                        associative1 = tmp208
                        associative_type1 = type(tmp208)
                        subjects209 = deque(tmp208._args)
                        matcher = CommutativeMatcher101734.get()
                        tmp210 = subjects209
                        subjects209 = []
                        for s in tmp210:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp210, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 101740
                                if len(subjects198) == 0:
                                    pass
                                    # State 101741
                                    if len(subjects191) >= 1 and subjects191[0] == Integer(2):
                                        tmp211 = subjects191.popleft()
                                        # State 101742
                                        if len(subjects191) == 0:
                                            pass
                                            # State 101743
                                            if len(subjects) == 0:
                                                pass
                                                # 22: c*sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                                                yield 22, subst2
                                        subjects191.appendleft(tmp211)
                        subjects198.appendleft(tmp208)
                    subjects191.appendleft(tmp197)
                if len(subjects191) >= 1 and isinstance(subjects191[0], tan):
                    tmp212 = subjects191.popleft()
                    subjects213 = deque(tmp212._args)
                    # State 101928
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101929
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 101930
                            if len(subjects213) >= 1:
                                tmp216 = subjects213.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.3.1.0', tmp216)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 101931
                                    if len(subjects213) == 0:
                                        pass
                                        # State 101932
                                        if len(subjects191) >= 1 and subjects191[0] == Integer(2):
                                            tmp218 = subjects191.popleft()
                                            # State 101933
                                            if len(subjects191) == 0:
                                                pass
                                                # State 101934
                                                if len(subjects) == 0:
                                                    pass
                                                    # 24: b*tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                                    yield 24, subst4
                                            subjects191.appendleft(tmp218)
                                        if len(subjects191) >= 1 and subjects191[0] == Integer(-2):
                                            tmp219 = subjects191.popleft()
                                            # State 102125
                                            if len(subjects191) == 0:
                                                pass
                                                # State 102126
                                                if len(subjects) == 0:
                                                    pass
                                                    # 26: b/tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                                    yield 26, subst4
                                            subjects191.appendleft(tmp219)
                                subjects213.appendleft(tmp216)
                        if len(subjects213) >= 1 and isinstance(subjects213[0], Mul):
                            tmp220 = subjects213.popleft()
                            associative1 = tmp220
                            associative_type1 = type(tmp220)
                            subjects221 = deque(tmp220._args)
                            matcher = CommutativeMatcher101936.get()
                            tmp222 = subjects221
                            subjects221 = []
                            for s in tmp222:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp222, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 101937
                                    if len(subjects213) == 0:
                                        pass
                                        # State 101938
                                        if len(subjects191) >= 1 and subjects191[0] == Integer(2):
                                            tmp223 = subjects191.popleft()
                                            # State 101939
                                            if len(subjects191) == 0:
                                                pass
                                                # State 101940
                                                if len(subjects) == 0:
                                                    pass
                                                    # 24: b*tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                                    yield 24, subst3
                                            subjects191.appendleft(tmp223)
                                        if len(subjects191) >= 1 and subjects191[0] == Integer(-2):
                                            tmp224 = subjects191.popleft()
                                            # State 102127
                                            if len(subjects191) == 0:
                                                pass
                                                # State 102128
                                                if len(subjects) == 0:
                                                    pass
                                                    # 26: b/tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                                    yield 26, subst3
                                            subjects191.appendleft(tmp224)
                            subjects213.appendleft(tmp220)
                    if len(subjects213) >= 1 and isinstance(subjects213[0], Add):
                        tmp225 = subjects213.popleft()
                        associative1 = tmp225
                        associative_type1 = type(tmp225)
                        subjects226 = deque(tmp225._args)
                        matcher = CommutativeMatcher101942.get()
                        tmp227 = subjects226
                        subjects226 = []
                        for s in tmp227:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp227, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 101948
                                if len(subjects213) == 0:
                                    pass
                                    # State 101949
                                    if len(subjects191) >= 1 and subjects191[0] == Integer(2):
                                        tmp228 = subjects191.popleft()
                                        # State 101950
                                        if len(subjects191) == 0:
                                            pass
                                            # State 101951
                                            if len(subjects) == 0:
                                                pass
                                                # 24: b*tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                                yield 24, subst2
                                        subjects191.appendleft(tmp228)
                                    if len(subjects191) >= 1 and subjects191[0] == Integer(-2):
                                        tmp229 = subjects191.popleft()
                                        # State 102129
                                        if len(subjects191) == 0:
                                            pass
                                            # State 102130
                                            if len(subjects) == 0:
                                                pass
                                                # 26: b/tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                                yield 26, subst2
                                        subjects191.appendleft(tmp229)
                        subjects213.appendleft(tmp225)
                    subjects191.appendleft(tmp212)
                subjects.appendleft(tmp190)
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp230 = subjects.popleft()
                subjects231 = deque(tmp230._args)
                # State 103246
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 103247
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 103248
                        if len(subjects231) >= 1:
                            tmp234 = subjects231.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.1.0', tmp234)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 103249
                                if len(subjects231) == 0:
                                    pass
                                    # State 103250
                                    if len(subjects) == 0:
                                        pass
                                        # 28: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                        yield 28, subst4
                            subjects231.appendleft(tmp234)
                    if len(subjects231) >= 1 and isinstance(subjects231[0], Mul):
                        tmp236 = subjects231.popleft()
                        associative1 = tmp236
                        associative_type1 = type(tmp236)
                        subjects237 = deque(tmp236._args)
                        matcher = CommutativeMatcher103252.get()
                        tmp238 = subjects237
                        subjects237 = []
                        for s in tmp238:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp238, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 103253
                                if len(subjects231) == 0:
                                    pass
                                    # State 103254
                                    if len(subjects) == 0:
                                        pass
                                        # 28: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                        yield 28, subst3
                        subjects231.appendleft(tmp236)
                if len(subjects231) >= 1:
                    tmp239 = subjects231.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp239)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 107919
                        if len(subjects231) == 0:
                            pass
                            # State 107920
                            if len(subjects) == 0:
                                pass
                                # 30: b*sin(v) /; (cons_f3) and (cons_f1441)
                                yield 30, subst2
                    subjects231.appendleft(tmp239)
                if len(subjects231) >= 1 and isinstance(subjects231[0], Add):
                    tmp241 = subjects231.popleft()
                    associative1 = tmp241
                    associative_type1 = type(tmp241)
                    subjects242 = deque(tmp241._args)
                    matcher = CommutativeMatcher103256.get()
                    tmp243 = subjects242
                    subjects242 = []
                    for s in tmp243:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp243, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 103262
                            if len(subjects231) == 0:
                                pass
                                # State 103263
                                if len(subjects) == 0:
                                    pass
                                    # 28: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                                    yield 28, subst2
                    subjects231.appendleft(tmp241)
                subjects.appendleft(tmp230)
            if len(subjects) >= 1 and isinstance(subjects[0], sinh):
                tmp244 = subjects.popleft()
                subjects245 = deque(tmp244._args)
                # State 137650
                if len(subjects245) >= 1:
                    tmp246 = subjects245.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp246)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137651
                        if len(subjects245) == 0:
                            pass
                            # State 137652
                            if len(subjects) == 0:
                                pass
                                # 34: b*sinh(v) /; (cons_f3) and (cons_f1267)
                                yield 34, subst2
                    subjects245.appendleft(tmp246)
                subjects.appendleft(tmp244)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2488
            if len(subjects) >= 1:
                tmp249 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp249)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2489
                    if len(subjects) == 0:
                        pass
                        # 7: v*b /; (cons_f3) and (cons_f10)
                        yield 7, subst2
                subjects.appendleft(tmp249)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2796
                if len(subjects) >= 1:
                    tmp252 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp252)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2797
                        if len(subjects) == 0:
                            pass
                            # 16: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                            yield 16, subst3
                    subjects.appendleft(tmp252)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp254 = subjects.popleft()
                subjects255 = deque(tmp254._args)
                # State 2798
                if len(subjects255) >= 1:
                    tmp256 = subjects255.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp256)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2799
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2800
                            if len(subjects255) == 0:
                                pass
                                # State 2801
                                if len(subjects) == 0:
                                    pass
                                    # 16: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                    yield 16, subst3
                        if len(subjects255) >= 1:
                            tmp259 = subjects255.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_2', tmp259)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 2800
                                if len(subjects255) == 0:
                                    pass
                                    # State 2801
                                    if len(subjects) == 0:
                                        pass
                                        # 16: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                                        yield 16, subst3
                            subjects255.appendleft(tmp259)
                    subjects255.appendleft(tmp256)
                subjects.appendleft(tmp254)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp261 = subjects.popleft()
            associative1 = tmp261
            associative_type1 = type(tmp261)
            subjects262 = deque(tmp261._args)
            matcher = CommutativeMatcher2208.get()
            tmp263 = subjects262
            subjects262 = []
            for s in tmp263:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp263, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 2215
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                        yield 0, subst1
                        # 1: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                        yield 1, subst1
                        # 2: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                        yield 2, subst1
                        # 5: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                        yield 5, subst1
                        # 12: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                        yield 12, subst1
                        # 14: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                        yield 14, subst1
                if pattern_index == 1:
                    pass
                    # State 2408
                    if len(subjects) == 0:
                        pass
                        # 3: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                        yield 3, subst1
                        # 4: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                        yield 4, subst1
                        # 11: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 11, subst1
                        # 13: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                        yield 13, subst1
                        # 15: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                        yield 15, subst1
                if pattern_index == 2:
                    pass
                    # State 2487
                    if len(subjects) == 0:
                        pass
                        # 19: x*f /; (cons_f2)
                        yield 19, subst1
                        # 6: v*a /; (cons_f2) and (cons_f10)
                        yield 6, subst1
                if pattern_index == 3:
                    pass
                    # State 2490
                    if len(subjects) == 0:
                        pass
                        # 7: v*b /; (cons_f3) and (cons_f10)
                        yield 7, subst1
                if pattern_index == 4:
                    pass
                    # State 2707
                    if len(subjects) == 0:
                        pass
                        # 8: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                        yield 8, subst1
                if pattern_index == 5:
                    pass
                    # State 2709
                    if len(subjects) == 0:
                        pass
                        # 9: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                        yield 9, subst1
                if pattern_index == 6:
                    pass
                    # State 2750
                    if len(subjects) == 0:
                        pass
                        # 10: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                        yield 10, subst1
                if pattern_index == 7:
                    pass
                    # State 2806
                    if len(subjects) == 0:
                        pass
                        # 16: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                        yield 16, subst1
                if pattern_index == 8:
                    pass
                    # State 42016
                    if len(subjects) == 0:
                        pass
                        # 17: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                        yield 17, subst1
                if pattern_index == 9:
                    pass
                    # State 45127
                    if len(subjects) == 0:
                        pass
                        # 18: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                        yield 18, subst1
                if pattern_index == 10:
                    pass
                    # State 54178
                    if len(subjects) == 0:
                        pass
                        # 20: w*b*log(v)**n /; (cons_f3) and (cons_f4)
                        yield 20, subst1
                if pattern_index == 11:
                    pass
                    # State 101719
                    if len(subjects) == 0:
                        pass
                        # 21: b*cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                        yield 21, subst1
                if pattern_index == 12:
                    pass
                    # State 101768
                    if len(subjects) == 0:
                        pass
                        # 22: c*sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                        yield 22, subst1
                if pattern_index == 13:
                    pass
                    # State 101927
                    if len(subjects) == 0:
                        pass
                        # 23: c/cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                        yield 23, subst1
                if pattern_index == 14:
                    pass
                    # State 101976
                    if len(subjects) == 0:
                        pass
                        # 24: b*tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                        yield 24, subst1
                if pattern_index == 15:
                    pass
                    # State 102124
                    if len(subjects) == 0:
                        pass
                        # 25: c/sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                        yield 25, subst1
                if pattern_index == 16:
                    pass
                    # State 102137
                    if len(subjects) == 0:
                        pass
                        # 26: b/tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                        yield 26, subst1
                if pattern_index == 17:
                    pass
                    # State 103245
                    if len(subjects) == 0:
                        pass
                        # 27: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                        yield 27, subst1
                if pattern_index == 18:
                    pass
                    # State 103282
                    if len(subjects) == 0:
                        pass
                        # 28: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                        yield 28, subst1
                if pattern_index == 19:
                    pass
                    # State 107918
                    if len(subjects) == 0:
                        pass
                        # 29: a*cos(v) /; (cons_f2) and (cons_f1441)
                        yield 29, subst1
                if pattern_index == 20:
                    pass
                    # State 107923
                    if len(subjects) == 0:
                        pass
                        # 30: b*sin(v) /; (cons_f3) and (cons_f1441)
                        yield 30, subst1
                if pattern_index == 21:
                    pass
                    # State 110099
                    if len(subjects) == 0:
                        pass
                        # 31: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 31, subst1
                if pattern_index == 22:
                    pass
                    # State 110196
                    if len(subjects) == 0:
                        pass
                        # 32: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 32, subst1
                if pattern_index == 23:
                    pass
                    # State 137649
                    if len(subjects) == 0:
                        pass
                        # 33: a*cosh(v) /; (cons_f2) and (cons_f1267)
                        yield 33, subst1
                if pattern_index == 24:
                    pass
                    # State 137656
                    if len(subjects) == 0:
                        pass
                        # 34: b*sinh(v) /; (cons_f3) and (cons_f1267)
                        yield 34, subst1
                if pattern_index == 25:
                    pass
                    # State 139834
                    if len(subjects) == 0:
                        pass
                        # 35: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 35, subst1
                if pattern_index == 26:
                    pass
                    # State 139931
                    if len(subjects) == 0:
                        pass
                        # 36: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 36, subst1
            subjects.appendleft(tmp261)
        return
        yield


from .generated_part000052 import *
from .generated_part000051 import *
from .generated_part000006 import *
from .generated_part000008 import *
from .generated_part000061 import *
from .generated_part000010 import *
from .generated_part000058 import *
from .generated_part000026 import *
from collections import deque
from .generated_part000045 import *
from .generated_part000012 import *
from matchpy.utils import VariableWithCount
from .generated_part000053 import *
from .generated_part000003 import *
from .generated_part000059 import *
from .generated_part000017 import *
from multiset import Multiset
from .generated_part000056 import *
from .generated_part000021 import *
from .generated_part000019 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part000002 import *
from .generated_part000046 import *
from .generated_part000048 import *
from .generated_part000005 import *
from .generated_part000050 import *
from .generated_part000049 import *
from .generated_part000055 import *