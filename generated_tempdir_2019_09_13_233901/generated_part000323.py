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

class CommutativeMatcher2221(CommutativeMatcher):
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
    10: (10, Multiset({17: 1, 18: 1}), [
      
]),
    11: (11, Multiset({19: 1, 20: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    12: (12, Multiset({21: 1, 22: 1}), [
      
]),
    13: (13, Multiset({23: 1, 21: 1}), [
      
]),
    14: (14, Multiset({24: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    15: (15, Multiset({25: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    16: (16, Multiset({26: 1, 27: 1}), [
      
]),
    17: (17, Multiset({28: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    18: (18, Multiset({29: 1, 30: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    19: (19, Multiset({31: 1, 32: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    20: (20, Multiset({33: 1, 34: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    21: (21, Multiset({35: 1, 36: 1}), [
      
]),
    22: (22, Multiset({37: 1, 38: 1}), [
      
]),
    23: (23, Multiset({39: 1, 40: 1}), [
      
]),
    24: (24, Multiset({41: 1, 42: 1}), [
      
]),
    25: (25, Multiset({43: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    26: (26, Multiset({44: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    27: (27, Multiset({45: 1, 46: 1}), [
      
]),
    28: (28, Multiset({47: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    29: (29, Multiset({48: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    30: (30, Multiset({49: 1, 50: 1}), [
      
]),
    31: (31, Multiset({51: 1, 52: 1}), [
      
]),
    32: (32, Multiset({53: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    33: (33, Multiset({54: 1, 55: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    34: (34, Multiset({56: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    35: (35, Multiset({57: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    36: (36, Multiset({58: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    37: (37, Multiset({59: 1, 60: 1}), [
      
]),
    38: (38, Multiset({61: 1, 62: 1}), [
      
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
        if CommutativeMatcher2221._instance is None:
            CommutativeMatcher2221._instance = CommutativeMatcher2221()
        return CommutativeMatcher2221._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2220
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2222
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2223
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2224
                        if len(subjects) == 0:
                            pass
                            # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                            # 1: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                            # 2: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                            # 5: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                            # 12: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                            # 14: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                            # 54: d*x**n /; (cons_f8) and (cons_f48) and (cons_f2011) and (With6955)
                            # 59: d*x**n /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f54) and (cons_f802) and (cons_f2033) and (With6981)
                    subjects.appendleft(tmp3)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.5', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 102513
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp6 = subjects.popleft()
                    subjects7 = deque(tmp6._args)
                    # State 102514
                    if len(subjects7) >= 1 and isinstance(subjects7[0], cos):
                        tmp8 = subjects7.popleft()
                        subjects9 = deque(tmp8._args)
                        # State 102515
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102516
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 102517
                                if len(subjects9) >= 1:
                                    tmp12 = subjects9.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.4.1.0', tmp12)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 102518
                                        if len(subjects9) == 0:
                                            pass
                                            # State 102519
                                            if len(subjects7) >= 1 and subjects7[0] == -1:
                                                tmp14 = subjects7.popleft()
                                                # State 102520
                                                if len(subjects7) == 0:
                                                    pass
                                                    # State 102521
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 35: b*(1/cos(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                subjects7.appendleft(tmp14)
                                    subjects9.appendleft(tmp12)
                            if len(subjects9) >= 1 and isinstance(subjects9[0], Mul):
                                tmp15 = subjects9.popleft()
                                associative1 = tmp15
                                associative_type1 = type(tmp15)
                                subjects16 = deque(tmp15._args)
                                matcher = CommutativeMatcher102523.get()
                                tmp17 = subjects16
                                subjects16 = []
                                for s in tmp17:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp17, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 102524
                                        if len(subjects9) == 0:
                                            pass
                                            # State 102525
                                            if len(subjects7) >= 1 and subjects7[0] == -1:
                                                tmp18 = subjects7.popleft()
                                                # State 102526
                                                if len(subjects7) == 0:
                                                    pass
                                                    # State 102527
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 35: b*(1/cos(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                subjects7.appendleft(tmp18)
                                subjects9.appendleft(tmp15)
                        if len(subjects9) >= 1 and isinstance(subjects9[0], Add):
                            tmp19 = subjects9.popleft()
                            associative1 = tmp19
                            associative_type1 = type(tmp19)
                            subjects20 = deque(tmp19._args)
                            matcher = CommutativeMatcher102529.get()
                            tmp21 = subjects20
                            subjects20 = []
                            for s in tmp21:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp21, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102535
                                    if len(subjects9) == 0:
                                        pass
                                        # State 102536
                                        if len(subjects7) >= 1 and subjects7[0] == -1:
                                            tmp22 = subjects7.popleft()
                                            # State 102537
                                            if len(subjects7) == 0:
                                                pass
                                                # State 102538
                                                if len(subjects) == 0:
                                                    pass
                                                    # 35: b*(1/cos(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                            subjects7.appendleft(tmp22)
                            subjects9.appendleft(tmp19)
                        subjects7.appendleft(tmp8)
                    if len(subjects7) >= 1 and isinstance(subjects7[0], sin):
                        tmp23 = subjects7.popleft()
                        subjects24 = deque(tmp23._args)
                        # State 102765
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102766
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 102767
                                if len(subjects24) >= 1:
                                    tmp27 = subjects24.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.4.1.0', tmp27)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 102768
                                        if len(subjects24) == 0:
                                            pass
                                            # State 102769
                                            if len(subjects7) >= 1 and subjects7[0] == -1:
                                                tmp29 = subjects7.popleft()
                                                # State 102770
                                                if len(subjects7) == 0:
                                                    pass
                                                    # State 102771
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 37: b*(1/sin(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                subjects7.appendleft(tmp29)
                                    subjects24.appendleft(tmp27)
                            if len(subjects24) >= 1 and isinstance(subjects24[0], Mul):
                                tmp30 = subjects24.popleft()
                                associative1 = tmp30
                                associative_type1 = type(tmp30)
                                subjects31 = deque(tmp30._args)
                                matcher = CommutativeMatcher102773.get()
                                tmp32 = subjects31
                                subjects31 = []
                                for s in tmp32:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp32, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 102774
                                        if len(subjects24) == 0:
                                            pass
                                            # State 102775
                                            if len(subjects7) >= 1 and subjects7[0] == -1:
                                                tmp33 = subjects7.popleft()
                                                # State 102776
                                                if len(subjects7) == 0:
                                                    pass
                                                    # State 102777
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 37: b*(1/sin(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                subjects7.appendleft(tmp33)
                                subjects24.appendleft(tmp30)
                        if len(subjects24) >= 1 and isinstance(subjects24[0], Add):
                            tmp34 = subjects24.popleft()
                            associative1 = tmp34
                            associative_type1 = type(tmp34)
                            subjects35 = deque(tmp34._args)
                            matcher = CommutativeMatcher102779.get()
                            tmp36 = subjects35
                            subjects35 = []
                            for s in tmp36:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp36, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102785
                                    if len(subjects24) == 0:
                                        pass
                                        # State 102786
                                        if len(subjects7) >= 1 and subjects7[0] == -1:
                                            tmp37 = subjects7.popleft()
                                            # State 102787
                                            if len(subjects7) == 0:
                                                pass
                                                # State 102788
                                                if len(subjects) == 0:
                                                    pass
                                                    # 37: b*(1/sin(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                            subjects7.appendleft(tmp37)
                            subjects24.appendleft(tmp34)
                        subjects7.appendleft(tmp23)
                    subjects.appendleft(tmp6)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp38 = subjects.popleft()
                subjects39 = deque(tmp38._args)
                # State 2225
                if len(subjects39) >= 1:
                    tmp40 = subjects39.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp40)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2226
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2227
                            if len(subjects39) == 0:
                                pass
                                # State 2228
                                if len(subjects) == 0:
                                    pass
                                    # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                    # 1: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                    # 2: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                    # 5: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                    # 12: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                    # 14: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                    # 54: d*x**n /; (cons_f8) and (cons_f48) and (cons_f2011) and (With6955)
                                    # 59: d*x**n /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f54) and (cons_f802) and (cons_f2033) and (With6981)
                        if len(subjects39) >= 1:
                            tmp43 = subjects39.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp43)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 2227
                                if len(subjects39) == 0:
                                    pass
                                    # State 2228
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                        # 1: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                                        # 2: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                        # 5: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                                        # 12: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                        # 14: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                                        # 54: d*x**n /; (cons_f8) and (cons_f48) and (cons_f2011) and (With6955)
                                        # 59: d*x**n /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f54) and (cons_f802) and (cons_f2033) and (With6981)
                            subjects39.appendleft(tmp43)
                        if len(subjects39) >= 1:
                            tmp45 = subjects39.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp45)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 2754
                                if len(subjects39) == 0:
                                    pass
                                    # State 2755
                                    if len(subjects) == 0:
                                        pass
                                        # 10: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                        # 21: d*x**j /; (cons_f1101) and (cons_f2) and (cons_f1156)
                                        # 53: d*x**n /; (cons_f3) and (cons_f4) and (cons_f1246) and (With6953)
                                        # 56: d*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f198) and (cons_f2031)
                                        # 57: d*x**n /; (cons_f3) and (cons_f198) and (cons_f842) and (cons_f2032)
                            subjects39.appendleft(tmp45)
                        if len(subjects39) >= 1 and subjects39[0] == 2:
                            tmp47 = subjects39.popleft()
                            # State 2713
                            if len(subjects39) == 0:
                                pass
                                # State 2714
                                if len(subjects) == 0:
                                    pass
                                    # 8: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                            subjects39.appendleft(tmp47)
                    subjects39.appendleft(tmp40)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 12665
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12666
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.1.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 12667
                            if len(subjects39) >= 1:
                                tmp51 = subjects39.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.1.1', tmp51)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 12668
                                    if len(subjects39) >= 1 and subjects39[0] == 1/2:
                                        tmp53 = subjects39.popleft()
                                        # State 12669
                                        if len(subjects39) == 0:
                                            pass
                                            # State 12670
                                            if len(subjects) == 0:
                                                pass
                                                # 17: c*sqrt(a + b*x**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1042) and (cons_f1043)
                                                # 51: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1038)
                                                # 49: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1039)
                                        subjects39.appendleft(tmp53)
                                subjects39.appendleft(tmp51)
                        if len(subjects39) >= 1 and isinstance(subjects39[0], Pow):
                            tmp54 = subjects39.popleft()
                            subjects55 = deque(tmp54._args)
                            # State 12671
                            if len(subjects55) >= 1:
                                tmp56 = subjects55.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.1.1', tmp56)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 12672
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.1.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 12673
                                        if len(subjects55) == 0:
                                            pass
                                            # State 12674
                                            if len(subjects39) >= 1 and subjects39[0] == 1/2:
                                                tmp59 = subjects39.popleft()
                                                # State 12675
                                                if len(subjects39) == 0:
                                                    pass
                                                    # State 12676
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 17: c*sqrt(a + b*x**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1042) and (cons_f1043)
                                                        # 51: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1038)
                                                        # 49: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1039)
                                                subjects39.appendleft(tmp59)
                                    if len(subjects55) >= 1:
                                        tmp60 = subjects55.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp60)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 12673
                                            if len(subjects55) == 0:
                                                pass
                                                # State 12674
                                                if len(subjects39) >= 1 and subjects39[0] == 1/2:
                                                    tmp62 = subjects39.popleft()
                                                    # State 12675
                                                    if len(subjects39) == 0:
                                                        pass
                                                        # State 12676
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 17: c*sqrt(a + b*x**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1042) and (cons_f1043)
                                                            # 51: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1038)
                                                            # 49: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1039)
                                                    subjects39.appendleft(tmp62)
                                        subjects55.appendleft(tmp60)
                                subjects55.appendleft(tmp56)
                            subjects39.appendleft(tmp54)
                    if len(subjects39) >= 1 and isinstance(subjects39[0], Mul):
                        tmp63 = subjects39.popleft()
                        associative1 = tmp63
                        associative_type1 = type(tmp63)
                        subjects64 = deque(tmp63._args)
                        matcher = CommutativeMatcher12678.get()
                        tmp65 = subjects64
                        subjects64 = []
                        for s in tmp65:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp65, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 12685
                                if len(subjects39) >= 1 and subjects39[0] == 1/2:
                                    tmp66 = subjects39.popleft()
                                    # State 12686
                                    if len(subjects39) == 0:
                                        pass
                                        # State 12687
                                        if len(subjects) == 0:
                                            pass
                                            # 17: c*sqrt(a + b*x**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1042) and (cons_f1043)
                                            # 51: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1038)
                                            # 49: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1039)
                                    subjects39.appendleft(tmp66)
                        subjects39.appendleft(tmp63)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 152034
                    if len(subjects39) >= 1 and isinstance(subjects39[0], Pow):
                        tmp68 = subjects39.popleft()
                        subjects69 = deque(tmp68._args)
                        # State 152035
                        if len(subjects69) >= 1:
                            tmp70 = subjects69.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1', tmp70)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 152036
                                if len(subjects69) >= 1:
                                    tmp72 = subjects69.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', tmp72)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 152037
                                        if len(subjects69) == 0:
                                            pass
                                            # State 152038
                                            if len(subjects39) >= 1 and subjects39[0] == 1/2:
                                                tmp74 = subjects39.popleft()
                                                # State 152039
                                                if len(subjects39) == 0:
                                                    pass
                                                    # State 152040
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 61: b*sqrt(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f19) and (cons_f4) and (cons_f1856)
                                                subjects39.appendleft(tmp74)
                                    subjects69.appendleft(tmp72)
                            subjects69.appendleft(tmp70)
                        subjects39.appendleft(tmp68)
                if len(subjects39) >= 1 and isinstance(subjects39[0], Add):
                    tmp75 = subjects39.popleft()
                    associative1 = tmp75
                    associative_type1 = type(tmp75)
                    subjects76 = deque(tmp75._args)
                    matcher = CommutativeMatcher12689.get()
                    tmp77 = subjects76
                    subjects76 = []
                    for s in tmp77:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp77, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 12706
                            if len(subjects39) >= 1 and subjects39[0] == 1/2:
                                tmp78 = subjects39.popleft()
                                # State 12707
                                if len(subjects39) == 0:
                                    pass
                                    # State 12708
                                    if len(subjects) == 0:
                                        pass
                                        # 17: c*sqrt(a + b*x**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1042) and (cons_f1043)
                                        # 51: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1038)
                                        # 49: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1039)
                                subjects39.appendleft(tmp78)
                        if pattern_index == 1:
                            pass
                            # State 14371
                            if len(subjects39) >= 1 and subjects39[0] == 1/2:
                                tmp79 = subjects39.popleft()
                                # State 14372
                                if len(subjects39) == 0:
                                    pass
                                    # State 14373
                                    if len(subjects) == 0:
                                        pass
                                        # 19: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f1074)
                                subjects39.appendleft(tmp79)
                    subjects39.appendleft(tmp75)
                if len(subjects39) >= 1 and isinstance(subjects39[0], cos):
                    tmp80 = subjects39.popleft()
                    subjects81 = deque(tmp80._args)
                    # State 101772
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101773
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 101774
                            if len(subjects81) >= 1:
                                tmp84 = subjects81.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.3.1.0', tmp84)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 101775
                                    if len(subjects81) == 0:
                                        pass
                                        # State 101776
                                        if len(subjects39) >= 1 and subjects39[0] == 2:
                                            tmp86 = subjects39.popleft()
                                            # State 101777
                                            if len(subjects39) == 0:
                                                pass
                                                # State 101778
                                                if len(subjects) == 0:
                                                    pass
                                                    # 29: b*cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                                            subjects39.appendleft(tmp86)
                                        if len(subjects39) >= 1 and subjects39[0] == -2:
                                            tmp87 = subjects39.popleft()
                                            # State 101980
                                            if len(subjects39) == 0:
                                                pass
                                                # State 101981
                                                if len(subjects) == 0:
                                                    pass
                                                    # 31: c/cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                            subjects39.appendleft(tmp87)
                                subjects81.appendleft(tmp84)
                        if len(subjects81) >= 1 and isinstance(subjects81[0], Mul):
                            tmp88 = subjects81.popleft()
                            associative1 = tmp88
                            associative_type1 = type(tmp88)
                            subjects89 = deque(tmp88._args)
                            matcher = CommutativeMatcher101780.get()
                            tmp90 = subjects89
                            subjects89 = []
                            for s in tmp90:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp90, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 101781
                                    if len(subjects81) == 0:
                                        pass
                                        # State 101782
                                        if len(subjects39) >= 1 and subjects39[0] == 2:
                                            tmp91 = subjects39.popleft()
                                            # State 101783
                                            if len(subjects39) == 0:
                                                pass
                                                # State 101784
                                                if len(subjects) == 0:
                                                    pass
                                                    # 29: b*cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                                            subjects39.appendleft(tmp91)
                                        if len(subjects39) >= 1 and subjects39[0] == -2:
                                            tmp92 = subjects39.popleft()
                                            # State 101982
                                            if len(subjects39) == 0:
                                                pass
                                                # State 101983
                                                if len(subjects) == 0:
                                                    pass
                                                    # 31: c/cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                            subjects39.appendleft(tmp92)
                            subjects81.appendleft(tmp88)
                    if len(subjects81) >= 1 and isinstance(subjects81[0], Add):
                        tmp93 = subjects81.popleft()
                        associative1 = tmp93
                        associative_type1 = type(tmp93)
                        subjects94 = deque(tmp93._args)
                        matcher = CommutativeMatcher101786.get()
                        tmp95 = subjects94
                        subjects94 = []
                        for s in tmp95:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp95, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 101792
                                if len(subjects81) == 0:
                                    pass
                                    # State 101793
                                    if len(subjects39) >= 1 and subjects39[0] == 2:
                                        tmp96 = subjects39.popleft()
                                        # State 101794
                                        if len(subjects39) == 0:
                                            pass
                                            # State 101795
                                            if len(subjects) == 0:
                                                pass
                                                # 29: b*cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                                        subjects39.appendleft(tmp96)
                                    if len(subjects39) >= 1 and subjects39[0] == -2:
                                        tmp97 = subjects39.popleft()
                                        # State 101984
                                        if len(subjects39) == 0:
                                            pass
                                            # State 101985
                                            if len(subjects) == 0:
                                                pass
                                                # 31: c/cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                        subjects39.appendleft(tmp97)
                        subjects81.appendleft(tmp93)
                    subjects39.appendleft(tmp80)
                if len(subjects39) >= 1 and isinstance(subjects39[0], sin):
                    tmp98 = subjects39.popleft()
                    subjects99 = deque(tmp98._args)
                    # State 102141
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102142
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102143
                            if len(subjects99) >= 1:
                                tmp102 = subjects99.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.3.1.0', tmp102)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102144
                                    if len(subjects99) == 0:
                                        pass
                                        # State 102145
                                        if len(subjects39) >= 1 and subjects39[0] == -2:
                                            tmp104 = subjects39.popleft()
                                            # State 102146
                                            if len(subjects39) == 0:
                                                pass
                                                # State 102147
                                                if len(subjects) == 0:
                                                    pass
                                                    # 33: c/sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                            subjects39.appendleft(tmp104)
                                subjects99.appendleft(tmp102)
                        if len(subjects99) >= 1 and isinstance(subjects99[0], Mul):
                            tmp105 = subjects99.popleft()
                            associative1 = tmp105
                            associative_type1 = type(tmp105)
                            subjects106 = deque(tmp105._args)
                            matcher = CommutativeMatcher102149.get()
                            tmp107 = subjects106
                            subjects106 = []
                            for s in tmp107:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp107, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102150
                                    if len(subjects99) == 0:
                                        pass
                                        # State 102151
                                        if len(subjects39) >= 1 and subjects39[0] == -2:
                                            tmp108 = subjects39.popleft()
                                            # State 102152
                                            if len(subjects39) == 0:
                                                pass
                                                # State 102153
                                                if len(subjects) == 0:
                                                    pass
                                                    # 33: c/sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                            subjects39.appendleft(tmp108)
                            subjects99.appendleft(tmp105)
                    if len(subjects99) >= 1 and isinstance(subjects99[0], Add):
                        tmp109 = subjects99.popleft()
                        associative1 = tmp109
                        associative_type1 = type(tmp109)
                        subjects110 = deque(tmp109._args)
                        matcher = CommutativeMatcher102155.get()
                        tmp111 = subjects110
                        subjects110 = []
                        for s in tmp111:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp111, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102161
                                if len(subjects99) == 0:
                                    pass
                                    # State 102162
                                    if len(subjects39) >= 1 and subjects39[0] == -2:
                                        tmp112 = subjects39.popleft()
                                        # State 102163
                                        if len(subjects39) == 0:
                                            pass
                                            # State 102164
                                            if len(subjects) == 0:
                                                pass
                                                # 33: c/sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                        subjects39.appendleft(tmp112)
                        subjects99.appendleft(tmp109)
                    subjects39.appendleft(tmp98)
                if len(subjects39) >= 1 and isinstance(subjects39[0], Pow):
                    tmp113 = subjects39.popleft()
                    subjects114 = deque(tmp113._args)
                    # State 102539
                    if len(subjects114) >= 1 and isinstance(subjects114[0], cos):
                        tmp115 = subjects114.popleft()
                        subjects116 = deque(tmp115._args)
                        # State 102540
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102541
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 102542
                                if len(subjects116) >= 1:
                                    tmp119 = subjects116.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.4.1.0', tmp119)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 102543
                                        if len(subjects116) == 0:
                                            pass
                                            # State 102544
                                            if len(subjects114) >= 1 and subjects114[0] == -1:
                                                tmp121 = subjects114.popleft()
                                                # State 102545
                                                if len(subjects114) == 0:
                                                    pass
                                                    # State 102546
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102547
                                                        if len(subjects39) == 0:
                                                            pass
                                                            # State 102548
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 35: b*(1/cos(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                    if len(subjects39) >= 1:
                                                        tmp123 = subjects39.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.5', tmp123)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 102547
                                                            if len(subjects39) == 0:
                                                                pass
                                                                # State 102548
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 35: b*(1/cos(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                        subjects39.appendleft(tmp123)
                                                subjects114.appendleft(tmp121)
                                    subjects116.appendleft(tmp119)
                            if len(subjects116) >= 1 and isinstance(subjects116[0], Mul):
                                tmp125 = subjects116.popleft()
                                associative1 = tmp125
                                associative_type1 = type(tmp125)
                                subjects126 = deque(tmp125._args)
                                matcher = CommutativeMatcher102550.get()
                                tmp127 = subjects126
                                subjects126 = []
                                for s in tmp127:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp127, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 102551
                                        if len(subjects116) == 0:
                                            pass
                                            # State 102552
                                            if len(subjects114) >= 1 and subjects114[0] == -1:
                                                tmp128 = subjects114.popleft()
                                                # State 102553
                                                if len(subjects114) == 0:
                                                    pass
                                                    # State 102554
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102555
                                                        if len(subjects39) == 0:
                                                            pass
                                                            # State 102556
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 35: b*(1/cos(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                    if len(subjects39) >= 1:
                                                        tmp130 = subjects39.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i2.2.1.5', tmp130)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 102555
                                                            if len(subjects39) == 0:
                                                                pass
                                                                # State 102556
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 35: b*(1/cos(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                        subjects39.appendleft(tmp130)
                                                subjects114.appendleft(tmp128)
                                subjects116.appendleft(tmp125)
                        if len(subjects116) >= 1 and isinstance(subjects116[0], Add):
                            tmp132 = subjects116.popleft()
                            associative1 = tmp132
                            associative_type1 = type(tmp132)
                            subjects133 = deque(tmp132._args)
                            matcher = CommutativeMatcher102558.get()
                            tmp134 = subjects133
                            subjects133 = []
                            for s in tmp134:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp134, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102564
                                    if len(subjects116) == 0:
                                        pass
                                        # State 102565
                                        if len(subjects114) >= 1 and subjects114[0] == -1:
                                            tmp135 = subjects114.popleft()
                                            # State 102566
                                            if len(subjects114) == 0:
                                                pass
                                                # State 102567
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 102568
                                                    if len(subjects39) == 0:
                                                        pass
                                                        # State 102569
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 35: b*(1/cos(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                if len(subjects39) >= 1:
                                                    tmp137 = subjects39.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.5', tmp137)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102568
                                                        if len(subjects39) == 0:
                                                            pass
                                                            # State 102569
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 35: b*(1/cos(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                    subjects39.appendleft(tmp137)
                                            subjects114.appendleft(tmp135)
                            subjects116.appendleft(tmp132)
                        subjects114.appendleft(tmp115)
                    if len(subjects114) >= 1 and isinstance(subjects114[0], sin):
                        tmp139 = subjects114.popleft()
                        subjects140 = deque(tmp139._args)
                        # State 102789
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102790
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 102791
                                if len(subjects140) >= 1:
                                    tmp143 = subjects140.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.4.1.0', tmp143)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 102792
                                        if len(subjects140) == 0:
                                            pass
                                            # State 102793
                                            if len(subjects114) >= 1 and subjects114[0] == -1:
                                                tmp145 = subjects114.popleft()
                                                # State 102794
                                                if len(subjects114) == 0:
                                                    pass
                                                    # State 102795
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102796
                                                        if len(subjects39) == 0:
                                                            pass
                                                            # State 102797
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 37: b*(1/sin(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                    if len(subjects39) >= 1:
                                                        tmp147 = subjects39.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.5', tmp147)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 102796
                                                            if len(subjects39) == 0:
                                                                pass
                                                                # State 102797
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 37: b*(1/sin(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                        subjects39.appendleft(tmp147)
                                                subjects114.appendleft(tmp145)
                                    subjects140.appendleft(tmp143)
                            if len(subjects140) >= 1 and isinstance(subjects140[0], Mul):
                                tmp149 = subjects140.popleft()
                                associative1 = tmp149
                                associative_type1 = type(tmp149)
                                subjects150 = deque(tmp149._args)
                                matcher = CommutativeMatcher102799.get()
                                tmp151 = subjects150
                                subjects150 = []
                                for s in tmp151:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp151, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 102800
                                        if len(subjects140) == 0:
                                            pass
                                            # State 102801
                                            if len(subjects114) >= 1 and subjects114[0] == -1:
                                                tmp152 = subjects114.popleft()
                                                # State 102802
                                                if len(subjects114) == 0:
                                                    pass
                                                    # State 102803
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102804
                                                        if len(subjects39) == 0:
                                                            pass
                                                            # State 102805
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 37: b*(1/sin(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                    if len(subjects39) >= 1:
                                                        tmp154 = subjects39.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i2.2.1.5', tmp154)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 102804
                                                            if len(subjects39) == 0:
                                                                pass
                                                                # State 102805
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 37: b*(1/sin(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                        subjects39.appendleft(tmp154)
                                                subjects114.appendleft(tmp152)
                                subjects140.appendleft(tmp149)
                        if len(subjects140) >= 1 and isinstance(subjects140[0], Add):
                            tmp156 = subjects140.popleft()
                            associative1 = tmp156
                            associative_type1 = type(tmp156)
                            subjects157 = deque(tmp156._args)
                            matcher = CommutativeMatcher102807.get()
                            tmp158 = subjects157
                            subjects157 = []
                            for s in tmp158:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp158, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102813
                                    if len(subjects140) == 0:
                                        pass
                                        # State 102814
                                        if len(subjects114) >= 1 and subjects114[0] == -1:
                                            tmp159 = subjects114.popleft()
                                            # State 102815
                                            if len(subjects114) == 0:
                                                pass
                                                # State 102816
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 102817
                                                    if len(subjects39) == 0:
                                                        pass
                                                        # State 102818
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 37: b*(1/sin(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                if len(subjects39) >= 1:
                                                    tmp161 = subjects39.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.5', tmp161)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102817
                                                        if len(subjects39) == 0:
                                                            pass
                                                            # State 102818
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 37: b*(1/sin(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                    subjects39.appendleft(tmp161)
                                            subjects114.appendleft(tmp159)
                            subjects140.appendleft(tmp156)
                        subjects114.appendleft(tmp139)
                    subjects39.appendleft(tmp113)
                if len(subjects39) >= 1 and isinstance(subjects39[0], Mul):
                    tmp163 = subjects39.popleft()
                    associative1 = tmp163
                    associative_type1 = type(tmp163)
                    subjects164 = deque(tmp163._args)
                    matcher = CommutativeMatcher152042.get()
                    tmp165 = subjects164
                    subjects164 = []
                    for s in tmp165:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp165, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 152047
                            if len(subjects39) >= 1 and subjects39[0] == 1/2:
                                tmp166 = subjects39.popleft()
                                # State 152048
                                if len(subjects39) == 0:
                                    pass
                                    # State 152049
                                    if len(subjects) == 0:
                                        pass
                                        # 61: b*sqrt(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f19) and (cons_f4) and (cons_f1856)
                                subjects39.appendleft(tmp166)
                    subjects39.appendleft(tmp163)
                subjects.appendleft(tmp38)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp167 = subjects.popleft()
                subjects168 = deque(tmp167._args)
                # State 42781
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 42782
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 42783
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 42784
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.2.1.2.2.2', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 42785
                                if len(subjects168) >= 1 and isinstance(subjects168[0], Add):
                                    tmp173 = subjects168.popleft()
                                    associative1 = tmp173
                                    associative_type1 = type(tmp173)
                                    subjects174 = deque(tmp173._args)
                                    matcher = CommutativeMatcher42787.get()
                                    tmp175 = subjects174
                                    subjects174 = []
                                    for s in tmp175:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp175, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 42803
                                            if len(subjects168) == 0:
                                                pass
                                                # State 42804
                                                if len(subjects) == 0:
                                                    pass
                                                    # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                        if pattern_index == 1:
                                            pass
                                            # State 54779
                                            if len(subjects168) == 0:
                                                pass
                                                # State 54780
                                                if len(subjects) == 0:
                                                    pass
                                                    # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                    subjects168.appendleft(tmp173)
                                if len(subjects168) >= 1:
                                    tmp176 = subjects168.popleft()
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.1', tmp176)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45276
                                        if len(subjects168) == 0:
                                            pass
                                            # State 45277
                                            if len(subjects) == 0:
                                                pass
                                                # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                    subjects168.appendleft(tmp176)
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54769
                                    subst7 = Substitution(subst6)
                                    try:
                                        subst7.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54770
                                        if len(subjects168) >= 1:
                                            tmp180 = subjects168.popleft()
                                            subst8 = Substitution(subst7)
                                            try:
                                                subst8.try_add_variable('i2.2.1.2.2.2.1.0', tmp180)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54771
                                                if len(subjects168) == 0:
                                                    pass
                                                    # State 54772
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                            subjects168.appendleft(tmp180)
                                    if len(subjects168) >= 1 and isinstance(subjects168[0], Mul):
                                        tmp182 = subjects168.popleft()
                                        associative1 = tmp182
                                        associative_type1 = type(tmp182)
                                        subjects183 = deque(tmp182._args)
                                        matcher = CommutativeMatcher54774.get()
                                        tmp184 = subjects183
                                        subjects183 = []
                                        for s in tmp184:
                                            matcher.add_subject(s)
                                        for pattern_index, subst7 in matcher.match(tmp184, subst6):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 54775
                                                if len(subjects168) == 0:
                                                    pass
                                                    # State 54776
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                        subjects168.appendleft(tmp182)
                            if len(subjects168) >= 1 and isinstance(subjects168[0], Pow):
                                tmp185 = subjects168.popleft()
                                subjects186 = deque(tmp185._args)
                                # State 42805
                                if len(subjects186) >= 1 and isinstance(subjects186[0], Add):
                                    tmp187 = subjects186.popleft()
                                    associative1 = tmp187
                                    associative_type1 = type(tmp187)
                                    subjects188 = deque(tmp187._args)
                                    matcher = CommutativeMatcher42807.get()
                                    tmp189 = subjects188
                                    subjects188 = []
                                    for s in tmp189:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp189, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 42823
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 42824
                                                if len(subjects186) == 0:
                                                    pass
                                                    # State 42825
                                                    if len(subjects168) == 0:
                                                        pass
                                                        # State 42826
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                            if len(subjects186) >= 1:
                                                tmp191 = []
                                                tmp191.append(subjects186.popleft())
                                                while True:
                                                    if len(tmp191) > 1:
                                                        tmp192 = create_operation_expression(associative1, tmp191)
                                                    elif len(tmp191) == 1:
                                                        tmp192 = tmp191[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', tmp192)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 42824
                                                        if len(subjects186) == 0:
                                                            pass
                                                            # State 42825
                                                            if len(subjects168) == 0:
                                                                pass
                                                                # State 42826
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                    if len(subjects186) == 0:
                                                        break
                                                    tmp191.append(subjects186.popleft())
                                                subjects186.extendleft(reversed(tmp191))
                                        if pattern_index == 1:
                                            pass
                                            # State 54795
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54796
                                                if len(subjects186) == 0:
                                                    pass
                                                    # State 54797
                                                    if len(subjects168) == 0:
                                                        pass
                                                        # State 54798
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                            if len(subjects186) >= 1:
                                                tmp195 = []
                                                tmp195.append(subjects186.popleft())
                                                while True:
                                                    if len(tmp195) > 1:
                                                        tmp196 = create_operation_expression(associative1, tmp195)
                                                    elif len(tmp195) == 1:
                                                        tmp196 = tmp195[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', tmp196)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54796
                                                        if len(subjects186) == 0:
                                                            pass
                                                            # State 54797
                                                            if len(subjects168) == 0:
                                                                pass
                                                                # State 54798
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                    if len(subjects186) == 0:
                                                        break
                                                    tmp195.append(subjects186.popleft())
                                                subjects186.extendleft(reversed(tmp195))
                                    subjects186.appendleft(tmp187)
                                if len(subjects186) >= 1:
                                    tmp198 = subjects186.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.1', tmp198)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45278
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45279
                                            if len(subjects186) == 0:
                                                pass
                                                # State 45280
                                                if len(subjects168) == 0:
                                                    pass
                                                    # State 45281
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                        if len(subjects186) >= 1:
                                            tmp201 = subjects186.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', tmp201)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45279
                                                if len(subjects186) == 0:
                                                    pass
                                                    # State 45280
                                                    if len(subjects168) == 0:
                                                        pass
                                                        # State 45281
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                            subjects186.appendleft(tmp201)
                                    subjects186.appendleft(tmp198)
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54781
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54782
                                        if len(subjects186) >= 1:
                                            tmp205 = subjects186.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2.2.1.0', tmp205)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54783
                                                subst8 = Substitution(subst7)
                                                try:
                                                    subst8.try_add_variable('i2.2.1.2.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54784
                                                    if len(subjects186) == 0:
                                                        pass
                                                        # State 54785
                                                        if len(subjects168) == 0:
                                                            pass
                                                            # State 54786
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                if len(subjects186) >= 1:
                                                    tmp208 = subjects186.popleft()
                                                    subst8 = Substitution(subst7)
                                                    try:
                                                        subst8.try_add_variable('i2.2.1.2.2.2', tmp208)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54784
                                                        if len(subjects186) == 0:
                                                            pass
                                                            # State 54785
                                                            if len(subjects168) == 0:
                                                                pass
                                                                # State 54786
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                    subjects186.appendleft(tmp208)
                                            subjects186.appendleft(tmp205)
                                    if len(subjects186) >= 1 and isinstance(subjects186[0], Mul):
                                        tmp210 = subjects186.popleft()
                                        associative1 = tmp210
                                        associative_type1 = type(tmp210)
                                        subjects211 = deque(tmp210._args)
                                        matcher = CommutativeMatcher54788.get()
                                        tmp212 = subjects211
                                        subjects211 = []
                                        for s in tmp212:
                                            matcher.add_subject(s)
                                        for pattern_index, subst6 in matcher.match(tmp212, subst5):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 54789
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54790
                                                    if len(subjects186) == 0:
                                                        pass
                                                        # State 54791
                                                        if len(subjects168) == 0:
                                                            pass
                                                            # State 54792
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                if len(subjects186) >= 1:
                                                    tmp214 = []
                                                    tmp214.append(subjects186.popleft())
                                                    while True:
                                                        if len(tmp214) > 1:
                                                            tmp215 = create_operation_expression(associative1, tmp214)
                                                        elif len(tmp214) == 1:
                                                            tmp215 = tmp214[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2.2', tmp215)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 54790
                                                            if len(subjects186) == 0:
                                                                pass
                                                                # State 54791
                                                                if len(subjects168) == 0:
                                                                    pass
                                                                    # State 54792
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                        if len(subjects186) == 0:
                                                            break
                                                        tmp214.append(subjects186.popleft())
                                                    subjects186.extendleft(reversed(tmp214))
                                        subjects186.appendleft(tmp210)
                                subjects168.appendleft(tmp185)
                        if len(subjects168) >= 1 and isinstance(subjects168[0], Mul):
                            tmp217 = subjects168.popleft()
                            associative1 = tmp217
                            associative_type1 = type(tmp217)
                            subjects218 = deque(tmp217._args)
                            matcher = CommutativeMatcher42828.get()
                            tmp219 = subjects218
                            subjects218 = []
                            for s in tmp219:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp219, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 42869
                                    if len(subjects168) == 0:
                                        pass
                                        # State 42870
                                        if len(subjects) == 0:
                                            pass
                                            # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                if pattern_index == 1:
                                    pass
                                    # State 45286
                                    if len(subjects168) == 0:
                                        pass
                                        # State 45287
                                        if len(subjects) == 0:
                                            pass
                                            # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                if pattern_index == 2:
                                    pass
                                    # State 54823
                                    if len(subjects168) == 0:
                                        pass
                                        # State 54824
                                        if len(subjects) == 0:
                                            pass
                                            # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                            subjects168.appendleft(tmp217)
                    if len(subjects168) >= 1 and isinstance(subjects168[0], Pow):
                        tmp220 = subjects168.popleft()
                        subjects221 = deque(tmp220._args)
                        # State 42871
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 42872
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 42873
                                if len(subjects221) >= 1 and isinstance(subjects221[0], Add):
                                    tmp224 = subjects221.popleft()
                                    associative1 = tmp224
                                    associative_type1 = type(tmp224)
                                    subjects225 = deque(tmp224._args)
                                    matcher = CommutativeMatcher42875.get()
                                    tmp226 = subjects225
                                    subjects225 = []
                                    for s in tmp226:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp226, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 42891
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 42892
                                                if len(subjects221) == 0:
                                                    pass
                                                    # State 42893
                                                    if len(subjects168) == 0:
                                                        pass
                                                        # State 42894
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                            if len(subjects221) >= 1:
                                                tmp228 = []
                                                tmp228.append(subjects221.popleft())
                                                while True:
                                                    if len(tmp228) > 1:
                                                        tmp229 = create_operation_expression(associative1, tmp228)
                                                    elif len(tmp228) == 1:
                                                        tmp229 = tmp228[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp229)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 42892
                                                        if len(subjects221) == 0:
                                                            pass
                                                            # State 42893
                                                            if len(subjects168) == 0:
                                                                pass
                                                                # State 42894
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                    if len(subjects221) == 0:
                                                        break
                                                    tmp228.append(subjects221.popleft())
                                                subjects221.extendleft(reversed(tmp228))
                                        if pattern_index == 1:
                                            pass
                                            # State 54839
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54840
                                                if len(subjects221) == 0:
                                                    pass
                                                    # State 54841
                                                    if len(subjects168) == 0:
                                                        pass
                                                        # State 54842
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                            if len(subjects221) >= 1:
                                                tmp232 = []
                                                tmp232.append(subjects221.popleft())
                                                while True:
                                                    if len(tmp232) > 1:
                                                        tmp233 = create_operation_expression(associative1, tmp232)
                                                    elif len(tmp232) == 1:
                                                        tmp233 = tmp232[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp233)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54840
                                                        if len(subjects221) == 0:
                                                            pass
                                                            # State 54841
                                                            if len(subjects168) == 0:
                                                                pass
                                                                # State 54842
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                    if len(subjects221) == 0:
                                                        break
                                                    tmp232.append(subjects221.popleft())
                                                subjects221.extendleft(reversed(tmp232))
                                    subjects221.appendleft(tmp224)
                                if len(subjects221) >= 1:
                                    tmp235 = subjects221.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.1', tmp235)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45288
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45289
                                            if len(subjects221) == 0:
                                                pass
                                                # State 45290
                                                if len(subjects168) == 0:
                                                    pass
                                                    # State 45291
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                        if len(subjects221) >= 1:
                                            tmp238 = subjects221.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', tmp238)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45289
                                                if len(subjects221) == 0:
                                                    pass
                                                    # State 45290
                                                    if len(subjects168) == 0:
                                                        pass
                                                        # State 45291
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                            subjects221.appendleft(tmp238)
                                    subjects221.appendleft(tmp235)
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54825
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54826
                                        if len(subjects221) >= 1:
                                            tmp242 = subjects221.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2.2.1.0', tmp242)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54827
                                                subst8 = Substitution(subst7)
                                                try:
                                                    subst8.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54828
                                                    if len(subjects221) == 0:
                                                        pass
                                                        # State 54829
                                                        if len(subjects168) == 0:
                                                            pass
                                                            # State 54830
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                if len(subjects221) >= 1:
                                                    tmp245 = subjects221.popleft()
                                                    subst8 = Substitution(subst7)
                                                    try:
                                                        subst8.try_add_variable('i2.2.1.2.2', tmp245)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54828
                                                        if len(subjects221) == 0:
                                                            pass
                                                            # State 54829
                                                            if len(subjects168) == 0:
                                                                pass
                                                                # State 54830
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                    subjects221.appendleft(tmp245)
                                            subjects221.appendleft(tmp242)
                                    if len(subjects221) >= 1 and isinstance(subjects221[0], Mul):
                                        tmp247 = subjects221.popleft()
                                        associative1 = tmp247
                                        associative_type1 = type(tmp247)
                                        subjects248 = deque(tmp247._args)
                                        matcher = CommutativeMatcher54832.get()
                                        tmp249 = subjects248
                                        subjects248 = []
                                        for s in tmp249:
                                            matcher.add_subject(s)
                                        for pattern_index, subst6 in matcher.match(tmp249, subst5):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 54833
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54834
                                                    if len(subjects221) == 0:
                                                        pass
                                                        # State 54835
                                                        if len(subjects168) == 0:
                                                            pass
                                                            # State 54836
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                if len(subjects221) >= 1:
                                                    tmp251 = []
                                                    tmp251.append(subjects221.popleft())
                                                    while True:
                                                        if len(tmp251) > 1:
                                                            tmp252 = create_operation_expression(associative1, tmp251)
                                                        elif len(tmp251) == 1:
                                                            tmp252 = tmp251[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', tmp252)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 54834
                                                            if len(subjects221) == 0:
                                                                pass
                                                                # State 54835
                                                                if len(subjects168) == 0:
                                                                    pass
                                                                    # State 54836
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                        if len(subjects221) == 0:
                                                            break
                                                        tmp251.append(subjects221.popleft())
                                                    subjects221.extendleft(reversed(tmp251))
                                        subjects221.appendleft(tmp247)
                            if len(subjects221) >= 1 and isinstance(subjects221[0], Pow):
                                tmp254 = subjects221.popleft()
                                subjects255 = deque(tmp254._args)
                                # State 42895
                                if len(subjects255) >= 1 and isinstance(subjects255[0], Add):
                                    tmp256 = subjects255.popleft()
                                    associative1 = tmp256
                                    associative_type1 = type(tmp256)
                                    subjects257 = deque(tmp256._args)
                                    matcher = CommutativeMatcher42897.get()
                                    tmp258 = subjects257
                                    subjects257 = []
                                    for s in tmp258:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp258, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 42913
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 42914
                                                if len(subjects255) == 0:
                                                    pass
                                                    # State 42915
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 42916
                                                        if len(subjects221) == 0:
                                                            pass
                                                            # State 42917
                                                            if len(subjects168) == 0:
                                                                pass
                                                                # State 42918
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                    if len(subjects221) >= 1:
                                                        tmp261 = subjects221.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp261)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 42916
                                                            if len(subjects221) == 0:
                                                                pass
                                                                # State 42917
                                                                if len(subjects168) == 0:
                                                                    pass
                                                                    # State 42918
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                        subjects221.appendleft(tmp261)
                                            if len(subjects255) >= 1:
                                                tmp263 = []
                                                tmp263.append(subjects255.popleft())
                                                while True:
                                                    if len(tmp263) > 1:
                                                        tmp264 = create_operation_expression(associative1, tmp263)
                                                    elif len(tmp263) == 1:
                                                        tmp264 = tmp263[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2.2', tmp264)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 42914
                                                        if len(subjects255) == 0:
                                                            pass
                                                            # State 42915
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 42916
                                                                if len(subjects221) == 0:
                                                                    pass
                                                                    # State 42917
                                                                    if len(subjects168) == 0:
                                                                        pass
                                                                        # State 42918
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                            if len(subjects221) >= 1:
                                                                tmp267 = subjects221.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2.1.2.2', tmp267)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 42916
                                                                    if len(subjects221) == 0:
                                                                        pass
                                                                        # State 42917
                                                                        if len(subjects168) == 0:
                                                                            pass
                                                                            # State 42918
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                subjects221.appendleft(tmp267)
                                                    if len(subjects255) == 0:
                                                        break
                                                    tmp263.append(subjects255.popleft())
                                                subjects255.extendleft(reversed(tmp263))
                                        if pattern_index == 1:
                                            pass
                                            # State 54861
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54862
                                                if len(subjects255) == 0:
                                                    pass
                                                    # State 54863
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54864
                                                        if len(subjects221) == 0:
                                                            pass
                                                            # State 54865
                                                            if len(subjects168) == 0:
                                                                pass
                                                                # State 54866
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                    if len(subjects221) >= 1:
                                                        tmp271 = subjects221.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp271)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 54864
                                                            if len(subjects221) == 0:
                                                                pass
                                                                # State 54865
                                                                if len(subjects168) == 0:
                                                                    pass
                                                                    # State 54866
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                        subjects221.appendleft(tmp271)
                                            if len(subjects255) >= 1:
                                                tmp273 = []
                                                tmp273.append(subjects255.popleft())
                                                while True:
                                                    if len(tmp273) > 1:
                                                        tmp274 = create_operation_expression(associative1, tmp273)
                                                    elif len(tmp273) == 1:
                                                        tmp274 = tmp273[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2.2', tmp274)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54862
                                                        if len(subjects255) == 0:
                                                            pass
                                                            # State 54863
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 54864
                                                                if len(subjects221) == 0:
                                                                    pass
                                                                    # State 54865
                                                                    if len(subjects168) == 0:
                                                                        pass
                                                                        # State 54866
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                            if len(subjects221) >= 1:
                                                                tmp277 = subjects221.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2.1.2.2', tmp277)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 54864
                                                                    if len(subjects221) == 0:
                                                                        pass
                                                                        # State 54865
                                                                        if len(subjects168) == 0:
                                                                            pass
                                                                            # State 54866
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                subjects221.appendleft(tmp277)
                                                    if len(subjects255) == 0:
                                                        break
                                                    tmp273.append(subjects255.popleft())
                                                subjects255.extendleft(reversed(tmp273))
                                    subjects255.appendleft(tmp256)
                                if len(subjects255) >= 1:
                                    tmp279 = subjects255.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.1', tmp279)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45292
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45293
                                            if len(subjects255) == 0:
                                                pass
                                                # State 45294
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 45295
                                                    if len(subjects221) == 0:
                                                        pass
                                                        # State 45296
                                                        if len(subjects168) == 0:
                                                            pass
                                                            # State 45297
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                if len(subjects221) >= 1:
                                                    tmp283 = subjects221.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp283)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 45295
                                                        if len(subjects221) == 0:
                                                            pass
                                                            # State 45296
                                                            if len(subjects168) == 0:
                                                                pass
                                                                # State 45297
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                    subjects221.appendleft(tmp283)
                                        if len(subjects255) >= 1:
                                            tmp285 = subjects255.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', tmp285)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45293
                                                if len(subjects255) == 0:
                                                    pass
                                                    # State 45294
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 45295
                                                        if len(subjects221) == 0:
                                                            pass
                                                            # State 45296
                                                            if len(subjects168) == 0:
                                                                pass
                                                                # State 45297
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                    if len(subjects221) >= 1:
                                                        tmp288 = subjects221.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp288)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 45295
                                                            if len(subjects221) == 0:
                                                                pass
                                                                # State 45296
                                                                if len(subjects168) == 0:
                                                                    pass
                                                                    # State 45297
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                        subjects221.appendleft(tmp288)
                                            subjects255.appendleft(tmp285)
                                    subjects255.appendleft(tmp279)
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54843
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54844
                                        if len(subjects255) >= 1:
                                            tmp292 = subjects255.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp292)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54845
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54846
                                                    if len(subjects255) == 0:
                                                        pass
                                                        # State 54847
                                                        subst8 = Substitution(subst7)
                                                        try:
                                                            subst8.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 54848
                                                            if len(subjects221) == 0:
                                                                pass
                                                                # State 54849
                                                                if len(subjects168) == 0:
                                                                    pass
                                                                    # State 54850
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                        if len(subjects221) >= 1:
                                                            tmp296 = subjects221.popleft()
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i2.2.1.2.2', tmp296)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 54848
                                                                if len(subjects221) == 0:
                                                                    pass
                                                                    # State 54849
                                                                    if len(subjects168) == 0:
                                                                        pass
                                                                        # State 54850
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                            subjects221.appendleft(tmp296)
                                                if len(subjects255) >= 1:
                                                    tmp298 = subjects255.popleft()
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2.2', tmp298)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54846
                                                        if len(subjects255) == 0:
                                                            pass
                                                            # State 54847
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 54848
                                                                if len(subjects221) == 0:
                                                                    pass
                                                                    # State 54849
                                                                    if len(subjects168) == 0:
                                                                        pass
                                                                        # State 54850
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                            if len(subjects221) >= 1:
                                                                tmp301 = subjects221.popleft()
                                                                subst8 = Substitution(subst7)
                                                                try:
                                                                    subst8.try_add_variable('i2.2.1.2.2', tmp301)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 54848
                                                                    if len(subjects221) == 0:
                                                                        pass
                                                                        # State 54849
                                                                        if len(subjects168) == 0:
                                                                            pass
                                                                            # State 54850
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                subjects221.appendleft(tmp301)
                                                    subjects255.appendleft(tmp298)
                                            subjects255.appendleft(tmp292)
                                    if len(subjects255) >= 1 and isinstance(subjects255[0], Mul):
                                        tmp303 = subjects255.popleft()
                                        associative1 = tmp303
                                        associative_type1 = type(tmp303)
                                        subjects304 = deque(tmp303._args)
                                        matcher = CommutativeMatcher54852.get()
                                        tmp305 = subjects304
                                        subjects304 = []
                                        for s in tmp305:
                                            matcher.add_subject(s)
                                        for pattern_index, subst5 in matcher.match(tmp305, subst4):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 54853
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54854
                                                    if len(subjects255) == 0:
                                                        pass
                                                        # State 54855
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 54856
                                                            if len(subjects221) == 0:
                                                                pass
                                                                # State 54857
                                                                if len(subjects168) == 0:
                                                                    pass
                                                                    # State 54858
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                        if len(subjects221) >= 1:
                                                            tmp308 = subjects221.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2', tmp308)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 54856
                                                                if len(subjects221) == 0:
                                                                    pass
                                                                    # State 54857
                                                                    if len(subjects168) == 0:
                                                                        pass
                                                                        # State 54858
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                            subjects221.appendleft(tmp308)
                                                if len(subjects255) >= 1:
                                                    tmp310 = []
                                                    tmp310.append(subjects255.popleft())
                                                    while True:
                                                        if len(tmp310) > 1:
                                                            tmp311 = create_operation_expression(associative1, tmp310)
                                                        elif len(tmp310) == 1:
                                                            tmp311 = tmp310[0]
                                                        else:
                                                            assert False, "Unreachable"
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp311)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 54854
                                                            if len(subjects255) == 0:
                                                                pass
                                                                # State 54855
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 54856
                                                                    if len(subjects221) == 0:
                                                                        pass
                                                                        # State 54857
                                                                        if len(subjects168) == 0:
                                                                            pass
                                                                            # State 54858
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                if len(subjects221) >= 1:
                                                                    tmp314 = subjects221.popleft()
                                                                    subst7 = Substitution(subst6)
                                                                    try:
                                                                        subst7.try_add_variable('i2.2.1.2.2', tmp314)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 54856
                                                                        if len(subjects221) == 0:
                                                                            pass
                                                                            # State 54857
                                                                            if len(subjects168) == 0:
                                                                                pass
                                                                                # State 54858
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                    subjects221.appendleft(tmp314)
                                                        if len(subjects255) == 0:
                                                            break
                                                        tmp310.append(subjects255.popleft())
                                                    subjects255.extendleft(reversed(tmp310))
                                        subjects255.appendleft(tmp303)
                                subjects221.appendleft(tmp254)
                        if len(subjects221) >= 1 and isinstance(subjects221[0], Mul):
                            tmp316 = subjects221.popleft()
                            associative1 = tmp316
                            associative_type1 = type(tmp316)
                            subjects317 = deque(tmp316._args)
                            matcher = CommutativeMatcher42920.get()
                            tmp318 = subjects317
                            subjects317 = []
                            for s in tmp318:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp318, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 42961
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 42962
                                        if len(subjects221) == 0:
                                            pass
                                            # State 42963
                                            if len(subjects168) == 0:
                                                pass
                                                # State 42964
                                                if len(subjects) == 0:
                                                    pass
                                                    # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                    if len(subjects221) >= 1:
                                        tmp320 = []
                                        tmp320.append(subjects221.popleft())
                                        while True:
                                            if len(tmp320) > 1:
                                                tmp321 = create_operation_expression(associative1, tmp320)
                                            elif len(tmp320) == 1:
                                                tmp321 = tmp320[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp321)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 42962
                                                if len(subjects221) == 0:
                                                    pass
                                                    # State 42963
                                                    if len(subjects168) == 0:
                                                        pass
                                                        # State 42964
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                            if len(subjects221) == 0:
                                                break
                                            tmp320.append(subjects221.popleft())
                                        subjects221.extendleft(reversed(tmp320))
                                if pattern_index == 1:
                                    pass
                                    # State 45302
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45303
                                        if len(subjects221) == 0:
                                            pass
                                            # State 45304
                                            if len(subjects168) == 0:
                                                pass
                                                # State 45305
                                                if len(subjects) == 0:
                                                    pass
                                                    # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                    if len(subjects221) >= 1:
                                        tmp324 = []
                                        tmp324.append(subjects221.popleft())
                                        while True:
                                            if len(tmp324) > 1:
                                                tmp325 = create_operation_expression(associative1, tmp324)
                                            elif len(tmp324) == 1:
                                                tmp325 = tmp324[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp325)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45303
                                                if len(subjects221) == 0:
                                                    pass
                                                    # State 45304
                                                    if len(subjects168) == 0:
                                                        pass
                                                        # State 45305
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                            if len(subjects221) == 0:
                                                break
                                            tmp324.append(subjects221.popleft())
                                        subjects221.extendleft(reversed(tmp324))
                                if pattern_index == 2:
                                    pass
                                    # State 54891
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54892
                                        if len(subjects221) == 0:
                                            pass
                                            # State 54893
                                            if len(subjects168) == 0:
                                                pass
                                                # State 54894
                                                if len(subjects) == 0:
                                                    pass
                                                    # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                    if len(subjects221) >= 1:
                                        tmp328 = []
                                        tmp328.append(subjects221.popleft())
                                        while True:
                                            if len(tmp328) > 1:
                                                tmp329 = create_operation_expression(associative1, tmp328)
                                            elif len(tmp328) == 1:
                                                tmp329 = tmp328[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp329)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54892
                                                if len(subjects221) == 0:
                                                    pass
                                                    # State 54893
                                                    if len(subjects168) == 0:
                                                        pass
                                                        # State 54894
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                            if len(subjects221) == 0:
                                                break
                                            tmp328.append(subjects221.popleft())
                                        subjects221.extendleft(reversed(tmp328))
                            subjects221.appendleft(tmp316)
                        subjects168.appendleft(tmp220)
                if len(subjects168) >= 1 and isinstance(subjects168[0], Mul):
                    tmp331 = subjects168.popleft()
                    associative1 = tmp331
                    associative_type1 = type(tmp331)
                    subjects332 = deque(tmp331._args)
                    matcher = CommutativeMatcher42966.get()
                    tmp333 = subjects332
                    subjects332 = []
                    for s in tmp333:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp333, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 43143
                            if len(subjects168) == 0:
                                pass
                                # State 43144
                                if len(subjects) == 0:
                                    pass
                                    # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                        if pattern_index == 1:
                            pass
                            # State 45330
                            if len(subjects168) == 0:
                                pass
                                # State 45331
                                if len(subjects) == 0:
                                    pass
                                    # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                        if pattern_index == 2:
                            pass
                            # State 55007
                            if len(subjects168) == 0:
                                pass
                                # State 55008
                                if len(subjects) == 0:
                                    pass
                                    # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                    subjects168.appendleft(tmp331)
                subjects.appendleft(tmp167)
            if len(subjects) >= 1 and isinstance(subjects[0], cos):
                tmp334 = subjects.popleft()
                subjects335 = deque(tmp334._args)
                # State 103286
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 103287
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 103288
                        if len(subjects335) >= 1:
                            tmp338 = subjects335.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.1.0', tmp338)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 103289
                                if len(subjects335) == 0:
                                    pass
                                    # State 103290
                                    if len(subjects) == 0:
                                        pass
                                        # 39: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                            subjects335.appendleft(tmp338)
                    if len(subjects335) >= 1 and isinstance(subjects335[0], Mul):
                        tmp340 = subjects335.popleft()
                        associative1 = tmp340
                        associative_type1 = type(tmp340)
                        subjects341 = deque(tmp340._args)
                        matcher = CommutativeMatcher103292.get()
                        tmp342 = subjects341
                        subjects341 = []
                        for s in tmp342:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp342, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 103293
                                if len(subjects335) == 0:
                                    pass
                                    # State 103294
                                    if len(subjects) == 0:
                                        pass
                                        # 39: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                        subjects335.appendleft(tmp340)
                if len(subjects335) >= 1:
                    tmp343 = subjects335.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp343)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 107927
                        if len(subjects335) == 0:
                            pass
                            # State 107928
                            if len(subjects) == 0:
                                pass
                                # 41: a*cos(v) /; (cons_f2) and (cons_f1441)
                    subjects335.appendleft(tmp343)
                if len(subjects335) >= 1 and isinstance(subjects335[0], Add):
                    tmp345 = subjects335.popleft()
                    associative1 = tmp345
                    associative_type1 = type(tmp345)
                    subjects346 = deque(tmp345._args)
                    matcher = CommutativeMatcher103296.get()
                    tmp347 = subjects346
                    subjects346 = []
                    for s in tmp347:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp347, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 103302
                            if len(subjects335) == 0:
                                pass
                                # State 103303
                                if len(subjects) == 0:
                                    pass
                                    # 39: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                    subjects335.appendleft(tmp345)
                subjects.appendleft(tmp334)
            if len(subjects) >= 1 and isinstance(subjects[0], asin):
                tmp348 = subjects.popleft()
                subjects349 = deque(tmp348._args)
                # State 110132
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 110133
                    if len(subjects349) >= 1:
                        tmp351 = subjects349.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.0', tmp351)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 110134
                            if len(subjects349) == 0:
                                pass
                                # State 110135
                                if len(subjects) == 0:
                                    pass
                                    # 43: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        subjects349.appendleft(tmp351)
                if len(subjects349) >= 1 and isinstance(subjects349[0], Mul):
                    tmp353 = subjects349.popleft()
                    associative1 = tmp353
                    associative_type1 = type(tmp353)
                    subjects354 = deque(tmp353._args)
                    matcher = CommutativeMatcher110137.get()
                    tmp355 = subjects354
                    subjects354 = []
                    for s in tmp355:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp355, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 110138
                            if len(subjects349) == 0:
                                pass
                                # State 110139
                                if len(subjects) == 0:
                                    pass
                                    # 43: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                    subjects349.appendleft(tmp353)
                subjects.appendleft(tmp348)
            if len(subjects) >= 1 and isinstance(subjects[0], acos):
                tmp356 = subjects.popleft()
                subjects357 = deque(tmp356._args)
                # State 110229
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 110230
                    if len(subjects357) >= 1:
                        tmp359 = subjects357.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.0', tmp359)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 110231
                            if len(subjects357) == 0:
                                pass
                                # State 110232
                                if len(subjects) == 0:
                                    pass
                                    # 44: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        subjects357.appendleft(tmp359)
                if len(subjects357) >= 1 and isinstance(subjects357[0], Mul):
                    tmp361 = subjects357.popleft()
                    associative1 = tmp361
                    associative_type1 = type(tmp361)
                    subjects362 = deque(tmp361._args)
                    matcher = CommutativeMatcher110234.get()
                    tmp363 = subjects362
                    subjects362 = []
                    for s in tmp363:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp363, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 110235
                            if len(subjects357) == 0:
                                pass
                                # State 110236
                                if len(subjects) == 0:
                                    pass
                                    # 44: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                    subjects357.appendleft(tmp361)
                subjects.appendleft(tmp356)
            if len(subjects) >= 1 and isinstance(subjects[0], cosh):
                tmp364 = subjects.popleft()
                subjects365 = deque(tmp364._args)
                # State 137660
                if len(subjects365) >= 1:
                    tmp366 = subjects365.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp366)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137661
                        if len(subjects365) == 0:
                            pass
                            # State 137662
                            if len(subjects) == 0:
                                pass
                                # 45: a*cosh(v) /; (cons_f2) and (cons_f1267)
                    subjects365.appendleft(tmp366)
                subjects.appendleft(tmp364)
            if len(subjects) >= 1 and isinstance(subjects[0], asinh):
                tmp368 = subjects.popleft()
                subjects369 = deque(tmp368._args)
                # State 139867
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 139868
                    if len(subjects369) >= 1:
                        tmp371 = subjects369.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.0', tmp371)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 139869
                            if len(subjects369) == 0:
                                pass
                                # State 139870
                                if len(subjects) == 0:
                                    pass
                                    # 47: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        subjects369.appendleft(tmp371)
                if len(subjects369) >= 1 and isinstance(subjects369[0], Mul):
                    tmp373 = subjects369.popleft()
                    associative1 = tmp373
                    associative_type1 = type(tmp373)
                    subjects374 = deque(tmp373._args)
                    matcher = CommutativeMatcher139872.get()
                    tmp375 = subjects374
                    subjects374 = []
                    for s in tmp375:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp375, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 139873
                            if len(subjects369) == 0:
                                pass
                                # State 139874
                                if len(subjects) == 0:
                                    pass
                                    # 47: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                    subjects369.appendleft(tmp373)
                subjects.appendleft(tmp368)
            if len(subjects) >= 1 and isinstance(subjects[0], acosh):
                tmp376 = subjects.popleft()
                subjects377 = deque(tmp376._args)
                # State 139964
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 139965
                    if len(subjects377) >= 1:
                        tmp379 = subjects377.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.0', tmp379)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 139966
                            if len(subjects377) == 0:
                                pass
                                # State 139967
                                if len(subjects) == 0:
                                    pass
                                    # 48: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        subjects377.appendleft(tmp379)
                if len(subjects377) >= 1 and isinstance(subjects377[0], Mul):
                    tmp381 = subjects377.popleft()
                    associative1 = tmp381
                    associative_type1 = type(tmp381)
                    subjects382 = deque(tmp381._args)
                    matcher = CommutativeMatcher139969.get()
                    tmp383 = subjects382
                    subjects382 = []
                    for s in tmp383:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp383, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 139970
                            if len(subjects377) == 0:
                                pass
                                # State 139971
                                if len(subjects) == 0:
                                    pass
                                    # 48: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                    subjects377.appendleft(tmp381)
                subjects.appendleft(tmp376)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2412
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2413
                if len(subjects) >= 1:
                    tmp386 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp386)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2414
                        if len(subjects) == 0:
                            pass
                            # 3: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                            # 4: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                            # 11: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                            # 13: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                            # 15: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                            # 60: b*x**s /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f54) and (cons_f802) and (cons_f2033) and (With6981)
                    subjects.appendleft(tmp386)
            if len(subjects) >= 1:
                tmp388 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp388)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2494
                    if len(subjects) == 0:
                        pass
                        # 26: x*f /; (cons_f2)
                        # 6: v*a /; (cons_f2) and (cons_f10)
                subjects.appendleft(tmp388)
            if len(subjects) >= 1:
                tmp390 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp390)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2718
                    if len(subjects) == 0:
                        pass
                        # 9: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                subjects.appendleft(tmp390)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 12754
                if len(subjects) >= 1:
                    tmp393 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1', tmp393)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12755
                        if len(subjects) == 0:
                            pass
                            # 18: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1042) and (cons_f1043)
                    subjects.appendleft(tmp393)
                if len(subjects) >= 1:
                    tmp395 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1', tmp395)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 152067
                        if len(subjects) == 0:
                            pass
                            # 62: a*x**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f19) and (cons_f4) and (cons_f1856)
                    subjects.appendleft(tmp395)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.5', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 102628
                if len(subjects) >= 1 and isinstance(subjects[0], tan):
                    tmp398 = subjects.popleft()
                    subjects399 = deque(tmp398._args)
                    # State 102629
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102630
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102631
                            if len(subjects399) >= 1:
                                tmp402 = subjects399.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.4.1.0', tmp402)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102632
                                    if len(subjects399) == 0:
                                        pass
                                        # State 102633
                                        if len(subjects) == 0:
                                            pass
                                            # 36: a*tan(c + x*d)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                subjects399.appendleft(tmp402)
                        if len(subjects399) >= 1 and isinstance(subjects399[0], Mul):
                            tmp404 = subjects399.popleft()
                            associative1 = tmp404
                            associative_type1 = type(tmp404)
                            subjects405 = deque(tmp404._args)
                            matcher = CommutativeMatcher102635.get()
                            tmp406 = subjects405
                            subjects405 = []
                            for s in tmp406:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp406, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102636
                                    if len(subjects399) == 0:
                                        pass
                                        # State 102637
                                        if len(subjects) == 0:
                                            pass
                                            # 36: a*tan(c + x*d)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                            subjects399.appendleft(tmp404)
                    if len(subjects399) >= 1 and isinstance(subjects399[0], Add):
                        tmp407 = subjects399.popleft()
                        associative1 = tmp407
                        associative_type1 = type(tmp407)
                        subjects408 = deque(tmp407._args)
                        matcher = CommutativeMatcher102639.get()
                        tmp409 = subjects408
                        subjects408 = []
                        for s in tmp409:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp409, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102645
                                if len(subjects399) == 0:
                                    pass
                                    # State 102646
                                    if len(subjects) == 0:
                                        pass
                                        # 36: a*tan(c + x*d)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                        subjects399.appendleft(tmp407)
                    subjects.appendleft(tmp398)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp410 = subjects.popleft()
                    subjects411 = deque(tmp410._args)
                    # State 102874
                    if len(subjects411) >= 1 and isinstance(subjects411[0], tan):
                        tmp412 = subjects411.popleft()
                        subjects413 = deque(tmp412._args)
                        # State 102875
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102876
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 102877
                                if len(subjects413) >= 1:
                                    tmp416 = subjects413.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.4.1.0', tmp416)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 102878
                                        if len(subjects413) == 0:
                                            pass
                                            # State 102879
                                            if len(subjects411) >= 1 and subjects411[0] == -1:
                                                tmp418 = subjects411.popleft()
                                                # State 102880
                                                if len(subjects411) == 0:
                                                    pass
                                                    # State 102881
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 38: a*(1/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                subjects411.appendleft(tmp418)
                                    subjects413.appendleft(tmp416)
                            if len(subjects413) >= 1 and isinstance(subjects413[0], Mul):
                                tmp419 = subjects413.popleft()
                                associative1 = tmp419
                                associative_type1 = type(tmp419)
                                subjects420 = deque(tmp419._args)
                                matcher = CommutativeMatcher102883.get()
                                tmp421 = subjects420
                                subjects420 = []
                                for s in tmp421:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp421, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 102884
                                        if len(subjects413) == 0:
                                            pass
                                            # State 102885
                                            if len(subjects411) >= 1 and subjects411[0] == -1:
                                                tmp422 = subjects411.popleft()
                                                # State 102886
                                                if len(subjects411) == 0:
                                                    pass
                                                    # State 102887
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 38: a*(1/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                subjects411.appendleft(tmp422)
                                subjects413.appendleft(tmp419)
                        if len(subjects413) >= 1 and isinstance(subjects413[0], Add):
                            tmp423 = subjects413.popleft()
                            associative1 = tmp423
                            associative_type1 = type(tmp423)
                            subjects424 = deque(tmp423._args)
                            matcher = CommutativeMatcher102889.get()
                            tmp425 = subjects424
                            subjects424 = []
                            for s in tmp425:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp425, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102895
                                    if len(subjects413) == 0:
                                        pass
                                        # State 102896
                                        if len(subjects411) >= 1 and subjects411[0] == -1:
                                            tmp426 = subjects411.popleft()
                                            # State 102897
                                            if len(subjects411) == 0:
                                                pass
                                                # State 102898
                                                if len(subjects) == 0:
                                                    pass
                                                    # 38: a*(1/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                            subjects411.appendleft(tmp426)
                            subjects413.appendleft(tmp423)
                        subjects411.appendleft(tmp412)
                    subjects.appendleft(tmp410)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp427 = subjects.popleft()
                subjects428 = deque(tmp427._args)
                # State 2415
                if len(subjects428) >= 1:
                    tmp429 = subjects428.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp429)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2416
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2417
                            if len(subjects428) == 0:
                                pass
                                # State 2418
                                if len(subjects) == 0:
                                    pass
                                    # 3: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                    # 4: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                    # 11: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                    # 13: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                    # 15: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                    # 60: b*x**s /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f54) and (cons_f802) and (cons_f2033) and (With6981)
                        if len(subjects428) >= 1:
                            tmp432 = subjects428.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp432)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 2417
                                if len(subjects428) == 0:
                                    pass
                                    # State 2418
                                    if len(subjects) == 0:
                                        pass
                                        # 3: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                                        # 4: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                                        # 11: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                                        # 13: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                                        # 15: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                                        # 60: b*x**s /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f54) and (cons_f802) and (cons_f2033) and (With6981)
                            subjects428.appendleft(tmp432)
                        if len(subjects428) >= 1:
                            tmp434 = subjects428.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp434)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 18524
                                if len(subjects428) == 0:
                                    pass
                                    # State 18525
                                    if len(subjects) == 0:
                                        pass
                                        # 22: c*x**n2 /; (cons_f1101) and (cons_f3) and (cons_f1156)
                            subjects428.appendleft(tmp434)
                    subjects428.appendleft(tmp429)
                if len(subjects428) >= 1:
                    tmp436 = subjects428.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp436)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12756
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 12757
                            if len(subjects428) == 0:
                                pass
                                # State 12758
                                if len(subjects) == 0:
                                    pass
                                    # 18: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1042) and (cons_f1043)
                        if len(subjects428) >= 1:
                            tmp439 = subjects428.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp439)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 12757
                                if len(subjects428) == 0:
                                    pass
                                    # State 12758
                                    if len(subjects) == 0:
                                        pass
                                        # 18: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1042) and (cons_f1043)
                            subjects428.appendleft(tmp439)
                        if len(subjects428) >= 1:
                            tmp441 = subjects428.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp441)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 14383
                                if len(subjects428) == 0:
                                    pass
                                    # State 14384
                                    if len(subjects) == 0:
                                        pass
                                        # 20: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f1074)
                            subjects428.appendleft(tmp441)
                    subjects428.appendleft(tmp436)
                if len(subjects428) >= 1:
                    tmp443 = subjects428.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1_1', tmp443)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 18537
                        if len(subjects428) >= 1:
                            tmp445 = subjects428.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp445)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 18538
                                if len(subjects428) == 0:
                                    pass
                                    # State 18539
                                    if len(subjects) == 0:
                                        pass
                                        # 23: b*G**w /; (cons_f1139) and (cons_f3) and (cons_f1156)
                                        # 55: b*y**n /; (cons_f3) and (cons_f4) and (cons_f48) and (cons_f2011) and (With6955)
                            subjects428.appendleft(tmp445)
                    subjects428.appendleft(tmp443)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0_1', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 151488
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151489
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.1.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151490
                            if len(subjects428) >= 1:
                                tmp450 = subjects428.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.1.1', tmp450)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 151491
                                    if len(subjects428) >= 1 and subjects428[0] == 1/2:
                                        tmp452 = subjects428.popleft()
                                        # State 151492
                                        if len(subjects428) == 0:
                                            pass
                                            # State 151493
                                            if len(subjects) == 0:
                                                pass
                                                # 50: f*sqrt(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1039)
                                                # 52: f*sqrt(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1038)
                                        subjects428.appendleft(tmp452)
                                subjects428.appendleft(tmp450)
                        if len(subjects428) >= 1 and isinstance(subjects428[0], Pow):
                            tmp453 = subjects428.popleft()
                            subjects454 = deque(tmp453._args)
                            # State 151494
                            if len(subjects454) >= 1:
                                tmp455 = subjects454.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.1.1', tmp455)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 151495
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.1.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 151496
                                        if len(subjects454) == 0:
                                            pass
                                            # State 151497
                                            if len(subjects428) >= 1 and subjects428[0] == 1/2:
                                                tmp458 = subjects428.popleft()
                                                # State 151498
                                                if len(subjects428) == 0:
                                                    pass
                                                    # State 151499
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 50: f*sqrt(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1039)
                                                        # 52: f*sqrt(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1038)
                                                subjects428.appendleft(tmp458)
                                    if len(subjects454) >= 1:
                                        tmp459 = subjects454.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.1.2', tmp459)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 151496
                                            if len(subjects454) == 0:
                                                pass
                                                # State 151497
                                                if len(subjects428) >= 1 and subjects428[0] == 1/2:
                                                    tmp461 = subjects428.popleft()
                                                    # State 151498
                                                    if len(subjects428) == 0:
                                                        pass
                                                        # State 151499
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 50: f*sqrt(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1039)
                                                            # 52: f*sqrt(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1038)
                                                    subjects428.appendleft(tmp461)
                                        subjects454.appendleft(tmp459)
                                subjects454.appendleft(tmp455)
                            subjects428.appendleft(tmp453)
                    if len(subjects428) >= 1 and isinstance(subjects428[0], Mul):
                        tmp462 = subjects428.popleft()
                        associative1 = tmp462
                        associative_type1 = type(tmp462)
                        subjects463 = deque(tmp462._args)
                        matcher = CommutativeMatcher151501.get()
                        tmp464 = subjects463
                        subjects463 = []
                        for s in tmp464:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp464, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 151508
                                if len(subjects428) >= 1 and subjects428[0] == 1/2:
                                    tmp465 = subjects428.popleft()
                                    # State 151509
                                    if len(subjects428) == 0:
                                        pass
                                        # State 151510
                                        if len(subjects) == 0:
                                            pass
                                            # 50: f*sqrt(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1039)
                                            # 52: f*sqrt(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1038)
                                    subjects428.appendleft(tmp465)
                        subjects428.appendleft(tmp462)
                if len(subjects428) >= 1:
                    tmp466 = subjects428.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1', tmp466)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 152068
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 152069
                            if len(subjects428) == 0:
                                pass
                                # State 152070
                                if len(subjects) == 0:
                                    pass
                                    # 62: a*x**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f19) and (cons_f4) and (cons_f1856)
                        if len(subjects428) >= 1:
                            tmp469 = subjects428.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp469)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 152069
                                if len(subjects428) == 0:
                                    pass
                                    # State 152070
                                    if len(subjects) == 0:
                                        pass
                                        # 62: a*x**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f19) and (cons_f4) and (cons_f1856)
                            subjects428.appendleft(tmp469)
                    subjects428.appendleft(tmp466)
                if len(subjects428) >= 1 and isinstance(subjects428[0], sin):
                    tmp471 = subjects428.popleft()
                    subjects472 = deque(tmp471._args)
                    # State 101821
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101822
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 101823
                            if len(subjects472) >= 1:
                                tmp475 = subjects472.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.3.1.0', tmp475)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 101824
                                    if len(subjects472) == 0:
                                        pass
                                        # State 101825
                                        if len(subjects428) >= 1 and subjects428[0] == 2:
                                            tmp477 = subjects428.popleft()
                                            # State 101826
                                            if len(subjects428) == 0:
                                                pass
                                                # State 101827
                                                if len(subjects) == 0:
                                                    pass
                                                    # 30: c*sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                                            subjects428.appendleft(tmp477)
                                subjects472.appendleft(tmp475)
                        if len(subjects472) >= 1 and isinstance(subjects472[0], Mul):
                            tmp478 = subjects472.popleft()
                            associative1 = tmp478
                            associative_type1 = type(tmp478)
                            subjects479 = deque(tmp478._args)
                            matcher = CommutativeMatcher101829.get()
                            tmp480 = subjects479
                            subjects479 = []
                            for s in tmp480:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp480, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 101830
                                    if len(subjects472) == 0:
                                        pass
                                        # State 101831
                                        if len(subjects428) >= 1 and subjects428[0] == 2:
                                            tmp481 = subjects428.popleft()
                                            # State 101832
                                            if len(subjects428) == 0:
                                                pass
                                                # State 101833
                                                if len(subjects) == 0:
                                                    pass
                                                    # 30: c*sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                                            subjects428.appendleft(tmp481)
                            subjects472.appendleft(tmp478)
                    if len(subjects472) >= 1 and isinstance(subjects472[0], Add):
                        tmp482 = subjects472.popleft()
                        associative1 = tmp482
                        associative_type1 = type(tmp482)
                        subjects483 = deque(tmp482._args)
                        matcher = CommutativeMatcher101835.get()
                        tmp484 = subjects483
                        subjects483 = []
                        for s in tmp484:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp484, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 101841
                                if len(subjects472) == 0:
                                    pass
                                    # State 101842
                                    if len(subjects428) >= 1 and subjects428[0] == 2:
                                        tmp485 = subjects428.popleft()
                                        # State 101843
                                        if len(subjects428) == 0:
                                            pass
                                            # State 101844
                                            if len(subjects) == 0:
                                                pass
                                                # 30: c*sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                                        subjects428.appendleft(tmp485)
                        subjects472.appendleft(tmp482)
                    subjects428.appendleft(tmp471)
                if len(subjects428) >= 1 and isinstance(subjects428[0], tan):
                    tmp486 = subjects428.popleft()
                    subjects487 = deque(tmp486._args)
                    # State 101993
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101994
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 101995
                            if len(subjects487) >= 1:
                                tmp490 = subjects487.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.3.1.0', tmp490)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 101996
                                    if len(subjects487) == 0:
                                        pass
                                        # State 101997
                                        if len(subjects428) >= 1 and subjects428[0] == 2:
                                            tmp492 = subjects428.popleft()
                                            # State 101998
                                            if len(subjects428) == 0:
                                                pass
                                                # State 101999
                                                if len(subjects) == 0:
                                                    pass
                                                    # 32: b*tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                            subjects428.appendleft(tmp492)
                                        if len(subjects428) >= 1 and subjects428[0] == -2:
                                            tmp493 = subjects428.popleft()
                                            # State 102172
                                            if len(subjects428) == 0:
                                                pass
                                                # State 102173
                                                if len(subjects) == 0:
                                                    pass
                                                    # 34: b/tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                            subjects428.appendleft(tmp493)
                                subjects487.appendleft(tmp490)
                        if len(subjects487) >= 1 and isinstance(subjects487[0], Mul):
                            tmp494 = subjects487.popleft()
                            associative1 = tmp494
                            associative_type1 = type(tmp494)
                            subjects495 = deque(tmp494._args)
                            matcher = CommutativeMatcher102001.get()
                            tmp496 = subjects495
                            subjects495 = []
                            for s in tmp496:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp496, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102002
                                    if len(subjects487) == 0:
                                        pass
                                        # State 102003
                                        if len(subjects428) >= 1 and subjects428[0] == 2:
                                            tmp497 = subjects428.popleft()
                                            # State 102004
                                            if len(subjects428) == 0:
                                                pass
                                                # State 102005
                                                if len(subjects) == 0:
                                                    pass
                                                    # 32: b*tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                            subjects428.appendleft(tmp497)
                                        if len(subjects428) >= 1 and subjects428[0] == -2:
                                            tmp498 = subjects428.popleft()
                                            # State 102174
                                            if len(subjects428) == 0:
                                                pass
                                                # State 102175
                                                if len(subjects) == 0:
                                                    pass
                                                    # 34: b/tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                            subjects428.appendleft(tmp498)
                            subjects487.appendleft(tmp494)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102647
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102648
                            if len(subjects487) >= 1:
                                tmp501 = subjects487.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.4.1.0', tmp501)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102649
                                    if len(subjects487) == 0:
                                        pass
                                        # State 102650
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.5', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 102651
                                            if len(subjects428) == 0:
                                                pass
                                                # State 102652
                                                if len(subjects) == 0:
                                                    pass
                                                    # 36: a*tan(c + x*d)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                        if len(subjects428) >= 1:
                                            tmp504 = subjects428.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.5', tmp504)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 102651
                                                if len(subjects428) == 0:
                                                    pass
                                                    # State 102652
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 36: a*tan(c + x*d)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                            subjects428.appendleft(tmp504)
                                subjects487.appendleft(tmp501)
                        if len(subjects487) >= 1 and isinstance(subjects487[0], Mul):
                            tmp506 = subjects487.popleft()
                            associative1 = tmp506
                            associative_type1 = type(tmp506)
                            subjects507 = deque(tmp506._args)
                            matcher = CommutativeMatcher102654.get()
                            tmp508 = subjects507
                            subjects507 = []
                            for s in tmp508:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp508, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102655
                                    if len(subjects487) == 0:
                                        pass
                                        # State 102656
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.5', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 102657
                                            if len(subjects428) == 0:
                                                pass
                                                # State 102658
                                                if len(subjects) == 0:
                                                    pass
                                                    # 36: a*tan(c + x*d)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                        if len(subjects428) >= 1:
                                            tmp510 = subjects428.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.5', tmp510)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 102657
                                                if len(subjects428) == 0:
                                                    pass
                                                    # State 102658
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 36: a*tan(c + x*d)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                            subjects428.appendleft(tmp510)
                            subjects487.appendleft(tmp506)
                    if len(subjects487) >= 1 and isinstance(subjects487[0], Add):
                        tmp512 = subjects487.popleft()
                        associative1 = tmp512
                        associative_type1 = type(tmp512)
                        subjects513 = deque(tmp512._args)
                        matcher = CommutativeMatcher102007.get()
                        tmp514 = subjects513
                        subjects513 = []
                        for s in tmp514:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp514, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102013
                                if len(subjects487) == 0:
                                    pass
                                    # State 102014
                                    if len(subjects428) >= 1 and subjects428[0] == 2:
                                        tmp515 = subjects428.popleft()
                                        # State 102015
                                        if len(subjects428) == 0:
                                            pass
                                            # State 102016
                                            if len(subjects) == 0:
                                                pass
                                                # 32: b*tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                        subjects428.appendleft(tmp515)
                                    if len(subjects428) >= 1 and subjects428[0] == -2:
                                        tmp516 = subjects428.popleft()
                                        # State 102176
                                        if len(subjects428) == 0:
                                            pass
                                            # State 102177
                                            if len(subjects) == 0:
                                                pass
                                                # 34: b/tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                                        subjects428.appendleft(tmp516)
                            if pattern_index == 1:
                                pass
                                # State 102662
                                if len(subjects487) == 0:
                                    pass
                                    # State 102663
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.5', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 102664
                                        if len(subjects428) == 0:
                                            pass
                                            # State 102665
                                            if len(subjects) == 0:
                                                pass
                                                # 36: a*tan(c + x*d)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                    if len(subjects428) >= 1:
                                        tmp518 = subjects428.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.5', tmp518)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 102664
                                            if len(subjects428) == 0:
                                                pass
                                                # State 102665
                                                if len(subjects) == 0:
                                                    pass
                                                    # 36: a*tan(c + x*d)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                        subjects428.appendleft(tmp518)
                        subjects487.appendleft(tmp512)
                    subjects428.appendleft(tmp486)
                if len(subjects428) >= 1 and isinstance(subjects428[0], Pow):
                    tmp520 = subjects428.popleft()
                    subjects521 = deque(tmp520._args)
                    # State 102899
                    if len(subjects521) >= 1 and isinstance(subjects521[0], tan):
                        tmp522 = subjects521.popleft()
                        subjects523 = deque(tmp522._args)
                        # State 102900
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.4.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102901
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.4.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 102902
                                if len(subjects523) >= 1:
                                    tmp526 = subjects523.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.4.1.0', tmp526)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 102903
                                        if len(subjects523) == 0:
                                            pass
                                            # State 102904
                                            if len(subjects521) >= 1 and subjects521[0] == -1:
                                                tmp528 = subjects521.popleft()
                                                # State 102905
                                                if len(subjects521) == 0:
                                                    pass
                                                    # State 102906
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102907
                                                        if len(subjects428) == 0:
                                                            pass
                                                            # State 102908
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 38: a*(1/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                    if len(subjects428) >= 1:
                                                        tmp530 = subjects428.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.5', tmp530)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 102907
                                                            if len(subjects428) == 0:
                                                                pass
                                                                # State 102908
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 38: a*(1/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                        subjects428.appendleft(tmp530)
                                                subjects521.appendleft(tmp528)
                                    subjects523.appendleft(tmp526)
                            if len(subjects523) >= 1 and isinstance(subjects523[0], Mul):
                                tmp532 = subjects523.popleft()
                                associative1 = tmp532
                                associative_type1 = type(tmp532)
                                subjects533 = deque(tmp532._args)
                                matcher = CommutativeMatcher102910.get()
                                tmp534 = subjects533
                                subjects533 = []
                                for s in tmp534:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp534, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 102911
                                        if len(subjects523) == 0:
                                            pass
                                            # State 102912
                                            if len(subjects521) >= 1 and subjects521[0] == -1:
                                                tmp535 = subjects521.popleft()
                                                # State 102913
                                                if len(subjects521) == 0:
                                                    pass
                                                    # State 102914
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.5', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102915
                                                        if len(subjects428) == 0:
                                                            pass
                                                            # State 102916
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 38: a*(1/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                    if len(subjects428) >= 1:
                                                        tmp537 = subjects428.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i2.2.1.5', tmp537)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 102915
                                                            if len(subjects428) == 0:
                                                                pass
                                                                # State 102916
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 38: a*(1/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                        subjects428.appendleft(tmp537)
                                                subjects521.appendleft(tmp535)
                                subjects523.appendleft(tmp532)
                        if len(subjects523) >= 1 and isinstance(subjects523[0], Add):
                            tmp539 = subjects523.popleft()
                            associative1 = tmp539
                            associative_type1 = type(tmp539)
                            subjects540 = deque(tmp539._args)
                            matcher = CommutativeMatcher102918.get()
                            tmp541 = subjects540
                            subjects540 = []
                            for s in tmp541:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp541, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102924
                                    if len(subjects523) == 0:
                                        pass
                                        # State 102925
                                        if len(subjects521) >= 1 and subjects521[0] == -1:
                                            tmp542 = subjects521.popleft()
                                            # State 102926
                                            if len(subjects521) == 0:
                                                pass
                                                # State 102927
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 102928
                                                    if len(subjects428) == 0:
                                                        pass
                                                        # State 102929
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 38: a*(1/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                if len(subjects428) >= 1:
                                                    tmp544 = subjects428.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.5', tmp544)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102928
                                                        if len(subjects428) == 0:
                                                            pass
                                                            # State 102929
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 38: a*(1/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                                                    subjects428.appendleft(tmp544)
                                            subjects521.appendleft(tmp542)
                            subjects523.appendleft(tmp539)
                        subjects521.appendleft(tmp522)
                    subjects428.appendleft(tmp520)
                if len(subjects428) >= 1 and isinstance(subjects428[0], Add):
                    tmp546 = subjects428.popleft()
                    associative1 = tmp546
                    associative_type1 = type(tmp546)
                    subjects547 = deque(tmp546._args)
                    matcher = CommutativeMatcher151512.get()
                    tmp548 = subjects547
                    subjects547 = []
                    for s in tmp548:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp548, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 151529
                            if len(subjects428) >= 1 and subjects428[0] == 1/2:
                                tmp549 = subjects428.popleft()
                                # State 151530
                                if len(subjects428) == 0:
                                    pass
                                    # State 151531
                                    if len(subjects) == 0:
                                        pass
                                        # 50: f*sqrt(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1039)
                                        # 52: f*sqrt(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1038)
                                subjects428.appendleft(tmp549)
                    subjects428.appendleft(tmp546)
                subjects.appendleft(tmp427)
            if len(subjects) >= 1 and isinstance(subjects[0], sin):
                tmp550 = subjects.popleft()
                subjects551 = deque(tmp550._args)
                # State 103323
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 103324
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 103325
                        if len(subjects551) >= 1:
                            tmp554 = subjects551.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.1.0', tmp554)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 103326
                                if len(subjects551) == 0:
                                    pass
                                    # State 103327
                                    if len(subjects) == 0:
                                        pass
                                        # 40: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                            subjects551.appendleft(tmp554)
                    if len(subjects551) >= 1 and isinstance(subjects551[0], Mul):
                        tmp556 = subjects551.popleft()
                        associative1 = tmp556
                        associative_type1 = type(tmp556)
                        subjects557 = deque(tmp556._args)
                        matcher = CommutativeMatcher103329.get()
                        tmp558 = subjects557
                        subjects557 = []
                        for s in tmp558:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp558, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 103330
                                if len(subjects551) == 0:
                                    pass
                                    # State 103331
                                    if len(subjects) == 0:
                                        pass
                                        # 40: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                        subjects551.appendleft(tmp556)
                if len(subjects551) >= 1:
                    tmp559 = subjects551.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp559)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 107932
                        if len(subjects551) == 0:
                            pass
                            # State 107933
                            if len(subjects) == 0:
                                pass
                                # 42: b*sin(v) /; (cons_f3) and (cons_f1441)
                    subjects551.appendleft(tmp559)
                if len(subjects551) >= 1 and isinstance(subjects551[0], Add):
                    tmp561 = subjects551.popleft()
                    associative1 = tmp561
                    associative_type1 = type(tmp561)
                    subjects562 = deque(tmp561._args)
                    matcher = CommutativeMatcher103333.get()
                    tmp563 = subjects562
                    subjects562 = []
                    for s in tmp563:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp563, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 103339
                            if len(subjects551) == 0:
                                pass
                                # State 103340
                                if len(subjects) == 0:
                                    pass
                                    # 40: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                    subjects551.appendleft(tmp561)
                subjects.appendleft(tmp550)
            if len(subjects) >= 1 and isinstance(subjects[0], sinh):
                tmp564 = subjects.popleft()
                subjects565 = deque(tmp564._args)
                # State 137667
                if len(subjects565) >= 1:
                    tmp566 = subjects565.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp566)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 137668
                        if len(subjects565) == 0:
                            pass
                            # State 137669
                            if len(subjects) == 0:
                                pass
                                # 46: b*sinh(v) /; (cons_f3) and (cons_f1267)
                    subjects565.appendleft(tmp566)
                subjects.appendleft(tmp564)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2496
            if len(subjects) >= 1:
                tmp569 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp569)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2497
                    if len(subjects) == 0:
                        pass
                        # 7: v*b /; (cons_f3) and (cons_f10)
                subjects.appendleft(tmp569)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 2810
                if len(subjects) >= 1:
                    tmp572 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp572)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2811
                        if len(subjects) == 0:
                            pass
                            # 16: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                    subjects.appendleft(tmp572)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp574 = subjects.popleft()
                subjects575 = deque(tmp574._args)
                # State 2812
                if len(subjects575) >= 1:
                    tmp576 = subjects575.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp576)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2813
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2814
                            if len(subjects575) == 0:
                                pass
                                # State 2815
                                if len(subjects) == 0:
                                    pass
                                    # 16: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                        if len(subjects575) >= 1:
                            tmp579 = subjects575.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_2', tmp579)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 2814
                                if len(subjects575) == 0:
                                    pass
                                    # State 2815
                                    if len(subjects) == 0:
                                        pass
                                        # 16: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                            subjects575.appendleft(tmp579)
                    subjects575.appendleft(tmp576)
                subjects.appendleft(tmp574)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp581 = subjects.popleft()
            associative1 = tmp581
            associative_type1 = type(tmp581)
            subjects582 = deque(tmp581._args)
            matcher = CommutativeMatcher2230.get()
            tmp583 = subjects582
            subjects582 = []
            for s in tmp583:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp583, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 2237
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                        # 1: b*x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5) and (cons_f6)
                        # 2: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                        # 5: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f9)
                        # 12: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                        # 14: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51) and (cons_f53)
                        # 54: d*x**n /; (cons_f8) and (cons_f48) and (cons_f2011) and (With6955)
                        # 59: d*x**n /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f54) and (cons_f802) and (cons_f2033) and (With6981)
                if pattern_index == 1:
                    pass
                    # State 2423
                    if len(subjects) == 0:
                        pass
                        # 3: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7)
                        # 4: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f7) and (cons_f6)
                        # 11: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                        # 13: b*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f52) and (cons_f51)
                        # 15: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f51)
                        # 60: b*x**s /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f54) and (cons_f802) and (cons_f2033) and (With6981)
                if pattern_index == 2:
                    pass
                    # State 2495
                    if len(subjects) == 0:
                        pass
                        # 26: x*f /; (cons_f2)
                        # 6: v*a /; (cons_f2) and (cons_f10)
                if pattern_index == 3:
                    pass
                    # State 2498
                    if len(subjects) == 0:
                        pass
                        # 7: v*b /; (cons_f3) and (cons_f10)
                if pattern_index == 4:
                    pass
                    # State 2717
                    if len(subjects) == 0:
                        pass
                        # 8: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                if pattern_index == 5:
                    pass
                    # State 2719
                    if len(subjects) == 0:
                        pass
                        # 9: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f47)
                if pattern_index == 6:
                    pass
                    # State 2758
                    if len(subjects) == 0:
                        pass
                        # 10: d*x**j /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f48) and (cons_f47)
                        # 21: d*x**j /; (cons_f1101) and (cons_f2) and (cons_f1156)
                        # 53: d*x**n /; (cons_f3) and (cons_f4) and (cons_f1246) and (With6953)
                        # 56: d*x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f198) and (cons_f2031)
                        # 57: d*x**n /; (cons_f3) and (cons_f198) and (cons_f842) and (cons_f2032)
                if pattern_index == 7:
                    pass
                    # State 2820
                    if len(subjects) == 0:
                        pass
                        # 16: c*x**r /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f53)
                if pattern_index == 8:
                    pass
                    # State 12753
                    if len(subjects) == 0:
                        pass
                        # 17: c*sqrt(a + b*x**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1042) and (cons_f1043)
                        # 51: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1038)
                        # 49: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1039)
                if pattern_index == 9:
                    pass
                    # State 12763
                    if len(subjects) == 0:
                        pass
                        # 18: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1042) and (cons_f1043)
                if pattern_index == 10:
                    pass
                    # State 14382
                    if len(subjects) == 0:
                        pass
                        # 19: e*sqrt(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f1074)
                if pattern_index == 11:
                    pass
                    # State 14387
                    if len(subjects) == 0:
                        pass
                        # 20: d*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f1074)
                if pattern_index == 12:
                    pass
                    # State 18528
                    if len(subjects) == 0:
                        pass
                        # 22: c*x**n2 /; (cons_f1101) and (cons_f3) and (cons_f1156)
                if pattern_index == 13:
                    pass
                    # State 18543
                    if len(subjects) == 0:
                        pass
                        # 23: b*G**w /; (cons_f1139) and (cons_f3) and (cons_f1156)
                        # 55: b*y**n /; (cons_f3) and (cons_f4) and (cons_f48) and (cons_f2011) and (With6955)
                if pattern_index == 14:
                    pass
                    # State 43509
                    if len(subjects) == 0:
                        pass
                        # 24: b*log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                if pattern_index == 15:
                    pass
                    # State 45388
                    if len(subjects) == 0:
                        pass
                        # 25: b*log(c*(d*v**p)**q) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                if pattern_index == 16:
                    pass
                    # State 54191
                    if len(subjects) == 0:
                        pass
                        # 27: w*b*log(v)**n /; (cons_f3) and (cons_f4)
                if pattern_index == 17:
                    pass
                    # State 55249
                    if len(subjects) == 0:
                        pass
                        # 28: b*log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                if pattern_index == 18:
                    pass
                    # State 101820
                    if len(subjects) == 0:
                        pass
                        # 29: b*cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                if pattern_index == 19:
                    pass
                    # State 101869
                    if len(subjects) == 0:
                        pass
                        # 30: c*sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1677)
                if pattern_index == 20:
                    pass
                    # State 101992
                    if len(subjects) == 0:
                        pass
                        # 31: c/cos(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                if pattern_index == 21:
                    pass
                    # State 102041
                    if len(subjects) == 0:
                        pass
                        # 32: b*tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                if pattern_index == 22:
                    pass
                    # State 102171
                    if len(subjects) == 0:
                        pass
                        # 33: c/sin(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                if pattern_index == 23:
                    pass
                    # State 102184
                    if len(subjects) == 0:
                        pass
                        # 34: b/tan(e + x*f)**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f1678)
                if pattern_index == 24:
                    pass
                    # State 102627
                    if len(subjects) == 0:
                        pass
                        # 35: b*(1/cos(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                if pattern_index == 25:
                    pass
                    # State 102703
                    if len(subjects) == 0:
                        pass
                        # 36: a*tan(c + x*d)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                if pattern_index == 26:
                    pass
                    # State 102873
                    if len(subjects) == 0:
                        pass
                        # 37: b*(1/sin(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                if pattern_index == 27:
                    pass
                    # State 102984
                    if len(subjects) == 0:
                        pass
                        # 38: a*(1/tan(c + x*d))**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378)
                if pattern_index == 28:
                    pass
                    # State 103322
                    if len(subjects) == 0:
                        pass
                        # 39: a*cos(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                if pattern_index == 29:
                    pass
                    # State 103359
                    if len(subjects) == 0:
                        pass
                        # 40: b*sin(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1441)
                if pattern_index == 30:
                    pass
                    # State 107931
                    if len(subjects) == 0:
                        pass
                        # 41: a*cos(v) /; (cons_f2) and (cons_f1441)
                if pattern_index == 31:
                    pass
                    # State 107936
                    if len(subjects) == 0:
                        pass
                        # 42: b*sin(v) /; (cons_f3) and (cons_f1441)
                if pattern_index == 32:
                    pass
                    # State 110148
                    if len(subjects) == 0:
                        pass
                        # 43: b*asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                if pattern_index == 33:
                    pass
                    # State 110245
                    if len(subjects) == 0:
                        pass
                        # 44: b*acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                if pattern_index == 34:
                    pass
                    # State 137666
                    if len(subjects) == 0:
                        pass
                        # 45: a*cosh(v) /; (cons_f2) and (cons_f1267)
                if pattern_index == 35:
                    pass
                    # State 137673
                    if len(subjects) == 0:
                        pass
                        # 46: b*sinh(v) /; (cons_f3) and (cons_f1267)
                if pattern_index == 36:
                    pass
                    # State 139883
                    if len(subjects) == 0:
                        pass
                        # 47: b*asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                if pattern_index == 37:
                    pass
                    # State 139980
                    if len(subjects) == 0:
                        pass
                        # 48: b*acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                if pattern_index == 38:
                    pass
                    # State 151566
                    if len(subjects) == 0:
                        pass
                        # 50: f*sqrt(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1039)
                        # 52: f*sqrt(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f1038)
                if pattern_index == 39:
                    pass
                    # State 151989
                    if len(subjects) == 0:
                        pass
                        # 58: b*x**n*w**n2 /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f5) and (cons_f198) and (cons_f842)
                if pattern_index == 40:
                    pass
                    # State 152066
                    if len(subjects) == 0:
                        pass
                        # 61: b*sqrt(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f19) and (cons_f4) and (cons_f1856)
                if pattern_index == 41:
                    pass
                    # State 152075
                    if len(subjects) == 0:
                        pass
                        # 62: a*x**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f19) and (cons_f4) and (cons_f1856)
            subjects.appendleft(tmp581)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
