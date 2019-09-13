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

class CommutativeMatcher56292(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    7: (7, Multiset({6: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({7: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({8: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    10: (10, Multiset({9: 1, 10: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    11: (11, Multiset({11: 1, 12: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    12: (12, Multiset({13: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    13: (13, Multiset({14: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    14: (14, Multiset({15: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    15: (15, Multiset({16: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    16: (16, Multiset({17: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    17: (17, Multiset({18: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    18: (18, Multiset({19: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    19: (19, Multiset({20: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    20: (20, Multiset({21: 1}), [
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
        if CommutativeMatcher56292._instance is None:
            CommutativeMatcher56292._instance = CommutativeMatcher56292()
        return CommutativeMatcher56292._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 56291
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 56293
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 56294
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72432
                    if len(subjects) == 0:
                        pass
                        # 4: d*x
                subjects.appendleft(tmp4)
            if len(subjects) >= 1:
                tmp6 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72486
                    if len(subjects) == 0:
                        pass
                        # 5: x*d
                subjects.appendleft(tmp6)
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75729
                    if len(subjects) == 0:
                        pass
                        # 10: x*b
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 56321
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 56322
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                subjects.appendleft(tmp11)
            if len(subjects) >= 1:
                tmp13 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp13)
                except ValueError:
                    pass
                else:
                    pass
                    # State 101009
                    if len(subjects) == 0:
                        pass
                        # 16: b*x
                subjects.appendleft(tmp13)
            if len(subjects) >= 1:
                tmp15 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp15)
                except ValueError:
                    pass
                else:
                    pass
                    # State 101044
                    if len(subjects) == 0:
                        pass
                        # 17: b*x
                subjects.appendleft(tmp15)
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1.0', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103832
                    if len(subjects) == 0:
                        pass
                        # 20: e*x
                subjects.appendleft(tmp17)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp19 = subjects.popleft()
                subjects20 = deque(tmp19._args)
                # State 73618
                if len(subjects20) >= 1:
                    tmp21 = subjects20.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp21)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 73619
                        if len(subjects20) >= 1:
                            tmp23 = subjects20.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp23)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 73620
                                if len(subjects20) == 0:
                                    pass
                                    # State 73621
                                    if len(subjects) == 0:
                                        pass
                                        # 6: x**n*d
                            subjects20.appendleft(tmp23)
                    subjects20.appendleft(tmp21)
                if len(subjects20) >= 1:
                    tmp25 = subjects20.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp25)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74585
                        if len(subjects20) >= 1:
                            tmp27 = subjects20.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp27)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74586
                                if len(subjects20) == 0:
                                    pass
                                    # State 74587
                                    if len(subjects) == 0:
                                        pass
                                        # 7: x**n*b
                            subjects20.appendleft(tmp27)
                    subjects20.appendleft(tmp25)
                if len(subjects20) >= 1:
                    tmp29 = subjects20.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.0', tmp29)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75722
                        if len(subjects20) >= 1 and subjects20[0] == 2:
                            tmp31 = subjects20.popleft()
                            # State 75723
                            if len(subjects20) == 0:
                                pass
                                # State 75724
                                if len(subjects) == 0:
                                    pass
                                    # 9: x**2*c
                            subjects20.appendleft(tmp31)
                    subjects20.appendleft(tmp29)
                subjects.appendleft(tmp19)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp32 = subjects.popleft()
                subjects33 = deque(tmp32._args)
                # State 105482
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 105483
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 105484
                        if len(subjects33) >= 1:
                            tmp36 = subjects33.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1', tmp36)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105485
                                if len(subjects33) == 0:
                                    pass
                                    # State 105486
                                    if len(subjects) == 0:
                                        pass
                                        # 21: b*log(x**n*c)
                            subjects33.appendleft(tmp36)
                    if len(subjects33) >= 1 and isinstance(subjects33[0], Pow):
                        tmp38 = subjects33.popleft()
                        subjects39 = deque(tmp38._args)
                        # State 105487
                        if len(subjects39) >= 1:
                            tmp40 = subjects39.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1', tmp40)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105488
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 105489
                                    if len(subjects39) == 0:
                                        pass
                                        # State 105490
                                        if len(subjects33) == 0:
                                            pass
                                            # State 105491
                                            if len(subjects) == 0:
                                                pass
                                                # 21: b*log(x**n*c)
                                if len(subjects39) >= 1:
                                    tmp43 = subjects39.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', tmp43)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 105489
                                        if len(subjects39) == 0:
                                            pass
                                            # State 105490
                                            if len(subjects33) == 0:
                                                pass
                                                # State 105491
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: b*log(x**n*c)
                                    subjects39.appendleft(tmp43)
                            subjects39.appendleft(tmp40)
                        subjects33.appendleft(tmp38)
                if len(subjects33) >= 1 and isinstance(subjects33[0], Mul):
                    tmp45 = subjects33.popleft()
                    associative1 = tmp45
                    associative_type1 = type(tmp45)
                    subjects46 = deque(tmp45._args)
                    matcher = CommutativeMatcher105493.get()
                    tmp47 = subjects46
                    subjects46 = []
                    for s in tmp47:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp47, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 105500
                            if len(subjects33) == 0:
                                pass
                                # State 105501
                                if len(subjects) == 0:
                                    pass
                                    # 21: b*log(x**n*c)
                    subjects33.appendleft(tmp45)
                subjects.appendleft(tmp32)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 62169
            if len(subjects) >= 1:
                tmp49 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp49)
                except ValueError:
                    pass
                else:
                    pass
                    # State 62170
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                subjects.appendleft(tmp49)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 72001
            if len(subjects) >= 1:
                tmp52 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp52)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72002
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                subjects.appendleft(tmp52)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp54 = subjects.popleft()
                subjects55 = deque(tmp54._args)
                # State 75762
                if len(subjects55) >= 1:
                    tmp56 = subjects55.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp56)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75763
                        if len(subjects55) >= 1 and subjects55[0] == 2:
                            tmp58 = subjects55.popleft()
                            # State 75764
                            if len(subjects55) == 0:
                                pass
                                # State 75765
                                if len(subjects) == 0:
                                    pass
                                    # 11: v**2*c
                            subjects55.appendleft(tmp58)
                    subjects55.appendleft(tmp56)
                subjects.appendleft(tmp54)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 75505
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 75506
                if len(subjects) >= 1:
                    tmp61 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1', tmp61)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75507
                        if len(subjects) == 0:
                            pass
                            # 8: x**n*b
                    subjects.appendleft(tmp61)
            if len(subjects) >= 1:
                tmp63 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp63)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103434
                    if len(subjects) == 0:
                        pass
                        # 18: x*f
                subjects.appendleft(tmp63)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp65 = subjects.popleft()
                subjects66 = deque(tmp65._args)
                # State 75508
                if len(subjects66) >= 1:
                    tmp67 = subjects66.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp67)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75509
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 75510
                            if len(subjects66) == 0:
                                pass
                                # State 75511
                                if len(subjects) == 0:
                                    pass
                                    # 8: x**n*b
                        if len(subjects66) >= 1:
                            tmp70 = subjects66.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp70)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75510
                                if len(subjects66) == 0:
                                    pass
                                    # State 75511
                                    if len(subjects) == 0:
                                        pass
                                        # 8: x**n*b
                            subjects66.appendleft(tmp70)
                    subjects66.appendleft(tmp67)
                subjects.appendleft(tmp65)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 75770
            if len(subjects) >= 1:
                tmp73 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp73)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75771
                    if len(subjects) == 0:
                        pass
                        # 12: x*b
                subjects.appendleft(tmp73)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 76625
            if len(subjects) >= 1:
                tmp76 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp76)
                except ValueError:
                    pass
                else:
                    pass
                    # State 76626
                    if len(subjects) == 0:
                        pass
                        # 13: x*f
                subjects.appendleft(tmp76)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 90709
            if len(subjects) >= 1:
                tmp79 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp79)
                except ValueError:
                    pass
                else:
                    pass
                    # State 90710
                    if len(subjects) == 0:
                        pass
                        # 14: x*f
                subjects.appendleft(tmp79)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 99558
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.4.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 99559
                if len(subjects) >= 1:
                    tmp83 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.4.1.1', tmp83)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99560
                        if len(subjects) == 0:
                            pass
                            # 15: b*x**n
                    subjects.appendleft(tmp83)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp85 = subjects.popleft()
                subjects86 = deque(tmp85._args)
                # State 99561
                if len(subjects86) >= 1:
                    tmp87 = subjects86.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.1', tmp87)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99562
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 99563
                            if len(subjects86) == 0:
                                pass
                                # State 99564
                                if len(subjects) == 0:
                                    pass
                                    # 15: b*x**n
                        if len(subjects86) >= 1:
                            tmp90 = subjects86.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.2', tmp90)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 99563
                                if len(subjects86) == 0:
                                    pass
                                    # State 99564
                                    if len(subjects) == 0:
                                        pass
                                        # 15: b*x**n
                            subjects86.appendleft(tmp90)
                    subjects86.appendleft(tmp87)
                subjects.appendleft(tmp85)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 103679
            if len(subjects) >= 1:
                tmp93 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp93)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103680
                    if len(subjects) == 0:
                        pass
                        # 19: x*d
                subjects.appendleft(tmp93)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp95 = subjects.popleft()
            associative1 = tmp95
            associative_type1 = type(tmp95)
            subjects96 = deque(tmp95._args)
            matcher = CommutativeMatcher56296.get()
            tmp97 = subjects96
            subjects96 = []
            for s in tmp97:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp97, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 56297
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 56323
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                if pattern_index == 2:
                    pass
                    # State 62171
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                if pattern_index == 3:
                    pass
                    # State 72003
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                if pattern_index == 4:
                    pass
                    # State 72433
                    if len(subjects) == 0:
                        pass
                        # 4: d*x
                if pattern_index == 5:
                    pass
                    # State 72487
                    if len(subjects) == 0:
                        pass
                        # 5: x*d
                if pattern_index == 6:
                    pass
                    # State 73626
                    if len(subjects) == 0:
                        pass
                        # 6: x**n*d
                if pattern_index == 7:
                    pass
                    # State 74591
                    if len(subjects) == 0:
                        pass
                        # 7: x**n*b
                if pattern_index == 8:
                    pass
                    # State 75516
                    if len(subjects) == 0:
                        pass
                        # 8: x**n*b
                if pattern_index == 9:
                    pass
                    # State 75728
                    if len(subjects) == 0:
                        pass
                        # 9: x**2*c
                if pattern_index == 10:
                    pass
                    # State 75730
                    if len(subjects) == 0:
                        pass
                        # 10: x*b
                if pattern_index == 11:
                    pass
                    # State 75769
                    if len(subjects) == 0:
                        pass
                        # 11: v**2*c
                if pattern_index == 12:
                    pass
                    # State 75772
                    if len(subjects) == 0:
                        pass
                        # 12: x*b
                if pattern_index == 13:
                    pass
                    # State 76627
                    if len(subjects) == 0:
                        pass
                        # 13: x*f
                if pattern_index == 14:
                    pass
                    # State 90711
                    if len(subjects) == 0:
                        pass
                        # 14: x*f
                if pattern_index == 15:
                    pass
                    # State 99570
                    if len(subjects) == 0:
                        pass
                        # 15: b*x**n
                if pattern_index == 16:
                    pass
                    # State 101010
                    if len(subjects) == 0:
                        pass
                        # 16: b*x
                if pattern_index == 17:
                    pass
                    # State 101045
                    if len(subjects) == 0:
                        pass
                        # 17: b*x
                if pattern_index == 18:
                    pass
                    # State 103435
                    if len(subjects) == 0:
                        pass
                        # 18: x*f
                if pattern_index == 19:
                    pass
                    # State 103681
                    if len(subjects) == 0:
                        pass
                        # 19: x*d
                if pattern_index == 20:
                    pass
                    # State 103833
                    if len(subjects) == 0:
                        pass
                        # 20: e*x
                if pattern_index == 21:
                    pass
                    # State 105522
                    if len(subjects) == 0:
                        pass
                        # 21: b*log(x**n*c)
            subjects.appendleft(tmp95)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
