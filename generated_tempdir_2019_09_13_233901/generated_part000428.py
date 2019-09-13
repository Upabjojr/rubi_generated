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

class CommutativeMatcher2230(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    6: (6, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({13: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({14: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({15: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({16: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({17: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({18: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({19: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({20: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({21: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({22: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({23: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    27: (27, Multiset({24: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({25: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({26: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({27: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    31: (31, Multiset({28: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({29: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    33: (33, Multiset({30: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({31: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({32: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    36: (36, Multiset({33: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    37: (37, Multiset({34: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    38: (38, Multiset({35: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({36: 1, 3: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({37: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    41: (41, Multiset({38: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher2230._instance is None:
            CommutativeMatcher2230._instance = CommutativeMatcher2230()
        return CommutativeMatcher2230._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2229
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2231
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2232
                    if len(subjects) == 0:
                        pass
                        # 0: x**n
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 12759
                    if len(subjects) == 0:
                        pass
                        # 6: x**n
                subjects.appendleft(tmp4)
            if len(subjects) >= 1:
                tmp6 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 152071
                    if len(subjects) == 0:
                        pass
                        # 38: x**m
                subjects.appendleft(tmp6)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2419
            if len(subjects) >= 1:
                tmp9 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp9)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2420
                    if len(subjects) == 0:
                        pass
                        # 1: x**n
                subjects.appendleft(tmp9)
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1_1', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151986
                    if len(subjects) == 0:
                        pass
                        # 36: w**n2
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2816
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2817
                    if len(subjects) == 0:
                        pass
                        # 4: x**r
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 54182
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp17 = subjects.popleft()
                subjects18 = deque(tmp17._args)
                # State 54183
                if len(subjects18) >= 1:
                    tmp19 = subjects18.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', tmp19)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 54184
                        if len(subjects18) == 0:
                            pass
                            # State 54185
                            if len(subjects) == 0:
                                pass
                                # 13: log(v)**n
                    subjects18.appendleft(tmp19)
                subjects.appendleft(tmp17)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.5', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 102570
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp22 = subjects.popleft()
                subjects23 = deque(tmp22._args)
                # State 102571
                if len(subjects23) >= 1 and isinstance(subjects23[0], cos):
                    tmp24 = subjects23.popleft()
                    subjects25 = deque(tmp24._args)
                    # State 102572
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102573
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102574
                            if len(subjects25) >= 1:
                                tmp28 = subjects25.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.4.1.0', tmp28)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102575
                                    if len(subjects25) == 0:
                                        pass
                                        # State 102576
                                        if len(subjects23) >= 1 and subjects23[0] == -1:
                                            tmp30 = subjects23.popleft()
                                            # State 102577
                                            if len(subjects23) == 0:
                                                pass
                                                # State 102578
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: (1/cos(c + x*d))**n
                                            subjects23.appendleft(tmp30)
                                subjects25.appendleft(tmp28)
                        if len(subjects25) >= 1 and isinstance(subjects25[0], Mul):
                            tmp31 = subjects25.popleft()
                            associative1 = tmp31
                            associative_type1 = type(tmp31)
                            subjects32 = deque(tmp31._args)
                            matcher = CommutativeMatcher102580.get()
                            tmp33 = subjects32
                            subjects32 = []
                            for s in tmp33:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp33, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102581
                                    if len(subjects25) == 0:
                                        pass
                                        # State 102582
                                        if len(subjects23) >= 1 and subjects23[0] == -1:
                                            tmp34 = subjects23.popleft()
                                            # State 102583
                                            if len(subjects23) == 0:
                                                pass
                                                # State 102584
                                                if len(subjects) == 0:
                                                    pass
                                                    # 21: (1/cos(c + x*d))**n
                                            subjects23.appendleft(tmp34)
                            subjects25.appendleft(tmp31)
                    if len(subjects25) >= 1 and isinstance(subjects25[0], Add):
                        tmp35 = subjects25.popleft()
                        associative1 = tmp35
                        associative_type1 = type(tmp35)
                        subjects36 = deque(tmp35._args)
                        matcher = CommutativeMatcher102586.get()
                        tmp37 = subjects36
                        subjects36 = []
                        for s in tmp37:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp37, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102592
                                if len(subjects25) == 0:
                                    pass
                                    # State 102593
                                    if len(subjects23) >= 1 and subjects23[0] == -1:
                                        tmp38 = subjects23.popleft()
                                        # State 102594
                                        if len(subjects23) == 0:
                                            pass
                                            # State 102595
                                            if len(subjects) == 0:
                                                pass
                                                # 21: (1/cos(c + x*d))**n
                                        subjects23.appendleft(tmp38)
                        subjects25.appendleft(tmp35)
                    subjects23.appendleft(tmp24)
                if len(subjects23) >= 1 and isinstance(subjects23[0], sin):
                    tmp39 = subjects23.popleft()
                    subjects40 = deque(tmp39._args)
                    # State 102819
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102820
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102821
                            if len(subjects40) >= 1:
                                tmp43 = subjects40.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.4.1.0', tmp43)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102822
                                    if len(subjects40) == 0:
                                        pass
                                        # State 102823
                                        if len(subjects23) >= 1 and subjects23[0] == -1:
                                            tmp45 = subjects23.popleft()
                                            # State 102824
                                            if len(subjects23) == 0:
                                                pass
                                                # State 102825
                                                if len(subjects) == 0:
                                                    pass
                                                    # 23: (1/sin(c + x*d))**n
                                            subjects23.appendleft(tmp45)
                                subjects40.appendleft(tmp43)
                        if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                            tmp46 = subjects40.popleft()
                            associative1 = tmp46
                            associative_type1 = type(tmp46)
                            subjects47 = deque(tmp46._args)
                            matcher = CommutativeMatcher102827.get()
                            tmp48 = subjects47
                            subjects47 = []
                            for s in tmp48:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp48, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102828
                                    if len(subjects40) == 0:
                                        pass
                                        # State 102829
                                        if len(subjects23) >= 1 and subjects23[0] == -1:
                                            tmp49 = subjects23.popleft()
                                            # State 102830
                                            if len(subjects23) == 0:
                                                pass
                                                # State 102831
                                                if len(subjects) == 0:
                                                    pass
                                                    # 23: (1/sin(c + x*d))**n
                                            subjects23.appendleft(tmp49)
                            subjects40.appendleft(tmp46)
                    if len(subjects40) >= 1 and isinstance(subjects40[0], Add):
                        tmp50 = subjects40.popleft()
                        associative1 = tmp50
                        associative_type1 = type(tmp50)
                        subjects51 = deque(tmp50._args)
                        matcher = CommutativeMatcher102833.get()
                        tmp52 = subjects51
                        subjects51 = []
                        for s in tmp52:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp52, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102839
                                if len(subjects40) == 0:
                                    pass
                                    # State 102840
                                    if len(subjects23) >= 1 and subjects23[0] == -1:
                                        tmp53 = subjects23.popleft()
                                        # State 102841
                                        if len(subjects23) == 0:
                                            pass
                                            # State 102842
                                            if len(subjects) == 0:
                                                pass
                                                # 23: (1/sin(c + x*d))**n
                                        subjects23.appendleft(tmp53)
                        subjects40.appendleft(tmp50)
                    subjects23.appendleft(tmp39)
                if len(subjects23) >= 1 and isinstance(subjects23[0], tan):
                    tmp54 = subjects23.popleft()
                    subjects55 = deque(tmp54._args)
                    # State 102930
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102931
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102932
                            if len(subjects55) >= 1:
                                tmp58 = subjects55.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.4.1.0', tmp58)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102933
                                    if len(subjects55) == 0:
                                        pass
                                        # State 102934
                                        if len(subjects23) >= 1 and subjects23[0] == -1:
                                            tmp60 = subjects23.popleft()
                                            # State 102935
                                            if len(subjects23) == 0:
                                                pass
                                                # State 102936
                                                if len(subjects) == 0:
                                                    pass
                                                    # 24: (1/tan(c + x*d))**n
                                            subjects23.appendleft(tmp60)
                                subjects55.appendleft(tmp58)
                        if len(subjects55) >= 1 and isinstance(subjects55[0], Mul):
                            tmp61 = subjects55.popleft()
                            associative1 = tmp61
                            associative_type1 = type(tmp61)
                            subjects62 = deque(tmp61._args)
                            matcher = CommutativeMatcher102938.get()
                            tmp63 = subjects62
                            subjects62 = []
                            for s in tmp63:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp63, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102939
                                    if len(subjects55) == 0:
                                        pass
                                        # State 102940
                                        if len(subjects23) >= 1 and subjects23[0] == -1:
                                            tmp64 = subjects23.popleft()
                                            # State 102941
                                            if len(subjects23) == 0:
                                                pass
                                                # State 102942
                                                if len(subjects) == 0:
                                                    pass
                                                    # 24: (1/tan(c + x*d))**n
                                            subjects23.appendleft(tmp64)
                            subjects55.appendleft(tmp61)
                    if len(subjects55) >= 1 and isinstance(subjects55[0], Add):
                        tmp65 = subjects55.popleft()
                        associative1 = tmp65
                        associative_type1 = type(tmp65)
                        subjects66 = deque(tmp65._args)
                        matcher = CommutativeMatcher102944.get()
                        tmp67 = subjects66
                        subjects66 = []
                        for s in tmp67:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp67, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102950
                                if len(subjects55) == 0:
                                    pass
                                    # State 102951
                                    if len(subjects23) >= 1 and subjects23[0] == -1:
                                        tmp68 = subjects23.popleft()
                                        # State 102952
                                        if len(subjects23) == 0:
                                            pass
                                            # State 102953
                                            if len(subjects) == 0:
                                                pass
                                                # 24: (1/tan(c + x*d))**n
                                        subjects23.appendleft(tmp68)
                        subjects55.appendleft(tmp65)
                    subjects23.appendleft(tmp54)
                subjects.appendleft(tmp22)
            if len(subjects) >= 1 and isinstance(subjects[0], tan):
                tmp69 = subjects.popleft()
                subjects70 = deque(tmp69._args)
                # State 102666
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 102667
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102668
                        if len(subjects70) >= 1:
                            tmp73 = subjects70.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.4.1.0', tmp73)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 102669
                                if len(subjects70) == 0:
                                    pass
                                    # State 102670
                                    if len(subjects) == 0:
                                        pass
                                        # 22: tan(c + x*d)**n
                            subjects70.appendleft(tmp73)
                    if len(subjects70) >= 1 and isinstance(subjects70[0], Mul):
                        tmp75 = subjects70.popleft()
                        associative1 = tmp75
                        associative_type1 = type(tmp75)
                        subjects76 = deque(tmp75._args)
                        matcher = CommutativeMatcher102672.get()
                        tmp77 = subjects76
                        subjects76 = []
                        for s in tmp77:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp77, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102673
                                if len(subjects70) == 0:
                                    pass
                                    # State 102674
                                    if len(subjects) == 0:
                                        pass
                                        # 22: tan(c + x*d)**n
                        subjects70.appendleft(tmp75)
                if len(subjects70) >= 1 and isinstance(subjects70[0], Add):
                    tmp78 = subjects70.popleft()
                    associative1 = tmp78
                    associative_type1 = type(tmp78)
                    subjects79 = deque(tmp78._args)
                    matcher = CommutativeMatcher102676.get()
                    tmp80 = subjects79
                    subjects79 = []
                    for s in tmp80:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp80, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 102682
                            if len(subjects70) == 0:
                                pass
                                # State 102683
                                if len(subjects) == 0:
                                    pass
                                    # 22: tan(c + x*d)**n
                    subjects70.appendleft(tmp78)
                subjects.appendleft(tmp69)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp81 = subjects.popleft()
            subjects82 = deque(tmp81._args)
            # State 2233
            if len(subjects82) >= 1:
                tmp83 = subjects82.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp83)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2234
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2235
                        if len(subjects82) == 0:
                            pass
                            # State 2236
                            if len(subjects) == 0:
                                pass
                                # 0: x**n
                    if len(subjects82) >= 1:
                        tmp86 = subjects82.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp86)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2235
                            if len(subjects82) == 0:
                                pass
                                # State 2236
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects82.appendleft(tmp86)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2421
                        if len(subjects82) == 0:
                            pass
                            # State 2422
                            if len(subjects) == 0:
                                pass
                                # 1: x**n
                    if len(subjects82) >= 1:
                        tmp89 = subjects82.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp89)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2421
                            if len(subjects82) == 0:
                                pass
                                # State 2422
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                        subjects82.appendleft(tmp89)
                    if len(subjects82) >= 1:
                        tmp91 = subjects82.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp91)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2756
                            if len(subjects82) == 0:
                                pass
                                # State 2757
                                if len(subjects) == 0:
                                    pass
                                    # 3: x**j
                        subjects82.appendleft(tmp91)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2818
                        if len(subjects82) == 0:
                            pass
                            # State 2819
                            if len(subjects) == 0:
                                pass
                                # 4: x**r
                    if len(subjects82) >= 1:
                        tmp94 = subjects82.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_2', tmp94)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2818
                            if len(subjects82) == 0:
                                pass
                                # State 2819
                                if len(subjects) == 0:
                                    pass
                                    # 4: x**r
                        subjects82.appendleft(tmp94)
                    if len(subjects82) >= 1:
                        tmp96 = subjects82.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp96)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18526
                            if len(subjects82) == 0:
                                pass
                                # State 18527
                                if len(subjects) == 0:
                                    pass
                                    # 9: x**n2
                        subjects82.appendleft(tmp96)
                    if len(subjects82) >= 1 and subjects82[0] == 2:
                        tmp98 = subjects82.popleft()
                        # State 2715
                        if len(subjects82) == 0:
                            pass
                            # State 2716
                            if len(subjects) == 0:
                                pass
                                # 2: x**2
                        subjects82.appendleft(tmp98)
                subjects82.appendleft(tmp83)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 12709
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 12710
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12711
                        if len(subjects82) >= 1:
                            tmp102 = subjects82.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.1.1', tmp102)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 12712
                                if len(subjects82) >= 1 and subjects82[0] == 1/2:
                                    tmp104 = subjects82.popleft()
                                    # State 12713
                                    if len(subjects82) == 0:
                                        pass
                                        # State 12714
                                        if len(subjects) == 0:
                                            pass
                                            # 5: sqrt(a + b*x**p)
                                    subjects82.appendleft(tmp104)
                            subjects82.appendleft(tmp102)
                    if len(subjects82) >= 1 and isinstance(subjects82[0], Pow):
                        tmp105 = subjects82.popleft()
                        subjects106 = deque(tmp105._args)
                        # State 12715
                        if len(subjects106) >= 1:
                            tmp107 = subjects106.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp107)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 12716
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 12717
                                    if len(subjects106) == 0:
                                        pass
                                        # State 12718
                                        if len(subjects82) >= 1 and subjects82[0] == 1/2:
                                            tmp110 = subjects82.popleft()
                                            # State 12719
                                            if len(subjects82) == 0:
                                                pass
                                                # State 12720
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: sqrt(a + b*x**p)
                                            subjects82.appendleft(tmp110)
                                if len(subjects106) >= 1:
                                    tmp111 = subjects106.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp111)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 12717
                                        if len(subjects106) == 0:
                                            pass
                                            # State 12718
                                            if len(subjects82) >= 1 and subjects82[0] == 1/2:
                                                tmp113 = subjects82.popleft()
                                                # State 12719
                                                if len(subjects82) == 0:
                                                    pass
                                                    # State 12720
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: sqrt(a + b*x**p)
                                                subjects82.appendleft(tmp113)
                                    subjects106.appendleft(tmp111)
                            subjects106.appendleft(tmp107)
                        subjects82.appendleft(tmp105)
                if len(subjects82) >= 1 and isinstance(subjects82[0], Mul):
                    tmp114 = subjects82.popleft()
                    associative1 = tmp114
                    associative_type1 = type(tmp114)
                    subjects115 = deque(tmp114._args)
                    matcher = CommutativeMatcher12722.get()
                    tmp116 = subjects115
                    subjects115 = []
                    for s in tmp116:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp116, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 12729
                            if len(subjects82) >= 1 and subjects82[0] == 1/2:
                                tmp117 = subjects82.popleft()
                                # State 12730
                                if len(subjects82) == 0:
                                    pass
                                    # State 12731
                                    if len(subjects) == 0:
                                        pass
                                        # 5: sqrt(a + b*x**p)
                                subjects82.appendleft(tmp117)
                    subjects82.appendleft(tmp114)
            if len(subjects82) >= 1:
                tmp118 = subjects82.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1.1', tmp118)
                except ValueError:
                    pass
                else:
                    pass
                    # State 12760
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12761
                        if len(subjects82) == 0:
                            pass
                            # State 12762
                            if len(subjects) == 0:
                                pass
                                # 6: x**n
                    if len(subjects82) >= 1:
                        tmp121 = subjects82.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp121)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 12761
                            if len(subjects82) == 0:
                                pass
                                # State 12762
                                if len(subjects) == 0:
                                    pass
                                    # 6: x**n
                        subjects82.appendleft(tmp121)
                    if len(subjects82) >= 1:
                        tmp123 = subjects82.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1.2', tmp123)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 14385
                            if len(subjects82) == 0:
                                pass
                                # State 14386
                                if len(subjects) == 0:
                                    pass
                                    # 8: x**n
                        subjects82.appendleft(tmp123)
                subjects82.appendleft(tmp118)
            if len(subjects82) >= 1:
                tmp125 = subjects82.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1_1', tmp125)
                except ValueError:
                    pass
                else:
                    pass
                    # State 18540
                    if len(subjects82) >= 1:
                        tmp127 = subjects82.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp127)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18541
                            if len(subjects82) == 0:
                                pass
                                # State 18542
                                if len(subjects) == 0:
                                    pass
                                    # 10: G**w
                        subjects82.appendleft(tmp127)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151987
                        if len(subjects82) == 0:
                            pass
                            # State 151988
                            if len(subjects) == 0:
                                pass
                                # 36: w**n2
                    if len(subjects82) >= 1:
                        tmp130 = subjects82.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp130)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151987
                            if len(subjects82) == 0:
                                pass
                                # State 151988
                                if len(subjects) == 0:
                                    pass
                                    # 36: w**n2
                        subjects82.appendleft(tmp130)
                subjects82.appendleft(tmp125)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 151532
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 151533
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151534
                        if len(subjects82) >= 1:
                            tmp135 = subjects82.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.1.1', tmp135)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 151535
                                if len(subjects82) >= 1 and subjects82[0] == 1/2:
                                    tmp137 = subjects82.popleft()
                                    # State 151536
                                    if len(subjects82) == 0:
                                        pass
                                        # State 151537
                                        if len(subjects) == 0:
                                            pass
                                            # 35: sqrt(c + d*x**n)
                                    subjects82.appendleft(tmp137)
                            subjects82.appendleft(tmp135)
                    if len(subjects82) >= 1 and isinstance(subjects82[0], Pow):
                        tmp138 = subjects82.popleft()
                        subjects139 = deque(tmp138._args)
                        # State 151538
                        if len(subjects139) >= 1:
                            tmp140 = subjects139.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.1', tmp140)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 151539
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 151540
                                    if len(subjects139) == 0:
                                        pass
                                        # State 151541
                                        if len(subjects82) >= 1 and subjects82[0] == 1/2:
                                            tmp143 = subjects82.popleft()
                                            # State 151542
                                            if len(subjects82) == 0:
                                                pass
                                                # State 151543
                                                if len(subjects) == 0:
                                                    pass
                                                    # 35: sqrt(c + d*x**n)
                                            subjects82.appendleft(tmp143)
                                if len(subjects139) >= 1:
                                    tmp144 = subjects139.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.1.2', tmp144)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 151540
                                        if len(subjects139) == 0:
                                            pass
                                            # State 151541
                                            if len(subjects82) >= 1 and subjects82[0] == 1/2:
                                                tmp146 = subjects82.popleft()
                                                # State 151542
                                                if len(subjects82) == 0:
                                                    pass
                                                    # State 151543
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 35: sqrt(c + d*x**n)
                                                subjects82.appendleft(tmp146)
                                    subjects139.appendleft(tmp144)
                            subjects139.appendleft(tmp140)
                        subjects82.appendleft(tmp138)
                if len(subjects82) >= 1 and isinstance(subjects82[0], Mul):
                    tmp147 = subjects82.popleft()
                    associative1 = tmp147
                    associative_type1 = type(tmp147)
                    subjects148 = deque(tmp147._args)
                    matcher = CommutativeMatcher151545.get()
                    tmp149 = subjects148
                    subjects148 = []
                    for s in tmp149:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp149, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 151552
                            if len(subjects82) >= 1 and subjects82[0] == 1/2:
                                tmp150 = subjects82.popleft()
                                # State 151553
                                if len(subjects82) == 0:
                                    pass
                                    # State 151554
                                    if len(subjects) == 0:
                                        pass
                                        # 35: sqrt(c + d*x**n)
                                subjects82.appendleft(tmp150)
                    subjects82.appendleft(tmp147)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 152050
                if len(subjects82) >= 1 and isinstance(subjects82[0], Pow):
                    tmp152 = subjects82.popleft()
                    subjects153 = deque(tmp152._args)
                    # State 152051
                    if len(subjects153) >= 1:
                        tmp154 = subjects153.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1', tmp154)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 152052
                            if len(subjects153) >= 1:
                                tmp156 = subjects153.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', tmp156)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 152053
                                    if len(subjects153) == 0:
                                        pass
                                        # State 152054
                                        if len(subjects82) >= 1 and subjects82[0] == 1/2:
                                            tmp158 = subjects82.popleft()
                                            # State 152055
                                            if len(subjects82) == 0:
                                                pass
                                                # State 152056
                                                if len(subjects) == 0:
                                                    pass
                                                    # 37: sqrt(c*x**n)
                                            subjects82.appendleft(tmp158)
                                subjects153.appendleft(tmp156)
                        subjects153.appendleft(tmp154)
                    subjects82.appendleft(tmp152)
            if len(subjects82) >= 1:
                tmp159 = subjects82.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1', tmp159)
                except ValueError:
                    pass
                else:
                    pass
                    # State 152072
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 152073
                        if len(subjects82) == 0:
                            pass
                            # State 152074
                            if len(subjects) == 0:
                                pass
                                # 38: x**m
                    if len(subjects82) >= 1:
                        tmp162 = subjects82.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp162)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 152073
                            if len(subjects82) == 0:
                                pass
                                # State 152074
                                if len(subjects) == 0:
                                    pass
                                    # 38: x**m
                        subjects82.appendleft(tmp162)
                subjects82.appendleft(tmp159)
            if len(subjects82) >= 1 and isinstance(subjects82[0], Add):
                tmp164 = subjects82.popleft()
                associative1 = tmp164
                associative_type1 = type(tmp164)
                subjects165 = deque(tmp164._args)
                matcher = CommutativeMatcher12733.get()
                tmp166 = subjects165
                subjects165 = []
                for s in tmp166:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp166, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 12750
                        if len(subjects82) >= 1 and subjects82[0] == 1/2:
                            tmp167 = subjects82.popleft()
                            # State 12751
                            if len(subjects82) == 0:
                                pass
                                # State 12752
                                if len(subjects) == 0:
                                    pass
                                    # 5: sqrt(a + b*x**p)
                            subjects82.appendleft(tmp167)
                    if pattern_index == 1:
                        pass
                        # State 14379
                        if len(subjects82) >= 1 and subjects82[0] == 1/2:
                            tmp168 = subjects82.popleft()
                            # State 14380
                            if len(subjects82) == 0:
                                pass
                                # State 14381
                                if len(subjects) == 0:
                                    pass
                                    # 7: sqrt(a + b*x**n)
                            subjects82.appendleft(tmp168)
                    if pattern_index == 2:
                        pass
                        # State 151563
                        if len(subjects82) >= 1 and subjects82[0] == 1/2:
                            tmp169 = subjects82.popleft()
                            # State 151564
                            if len(subjects82) == 0:
                                pass
                                # State 151565
                                if len(subjects) == 0:
                                    pass
                                    # 35: sqrt(c + d*x**n)
                            subjects82.appendleft(tmp169)
                subjects82.appendleft(tmp164)
            if len(subjects82) >= 1 and isinstance(subjects82[0], log):
                tmp170 = subjects82.popleft()
                subjects171 = deque(tmp170._args)
                # State 54186
                if len(subjects171) >= 1:
                    tmp172 = subjects171.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp172)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 54187
                        if len(subjects171) == 0:
                            pass
                            # State 54188
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i2.2.1.3', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 54189
                                if len(subjects82) == 0:
                                    pass
                                    # State 54190
                                    if len(subjects) == 0:
                                        pass
                                        # 13: log(v)**n
                            if len(subjects82) >= 1:
                                tmp175 = subjects82.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.3', tmp175)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54189
                                    if len(subjects82) == 0:
                                        pass
                                        # State 54190
                                        if len(subjects) == 0:
                                            pass
                                            # 13: log(v)**n
                                subjects82.appendleft(tmp175)
                    subjects171.appendleft(tmp172)
                subjects82.appendleft(tmp170)
            if len(subjects82) >= 1 and isinstance(subjects82[0], cos):
                tmp177 = subjects82.popleft()
                subjects178 = deque(tmp177._args)
                # State 101796
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 101797
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101798
                        if len(subjects178) >= 1:
                            tmp181 = subjects178.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp181)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 101799
                                if len(subjects178) == 0:
                                    pass
                                    # State 101800
                                    if len(subjects82) >= 1 and subjects82[0] == 2:
                                        tmp183 = subjects82.popleft()
                                        # State 101801
                                        if len(subjects82) == 0:
                                            pass
                                            # State 101802
                                            if len(subjects) == 0:
                                                pass
                                                # 15: cos(e + x*f)**2
                                        subjects82.appendleft(tmp183)
                                    if len(subjects82) >= 1 and subjects82[0] == -2:
                                        tmp184 = subjects82.popleft()
                                        # State 101986
                                        if len(subjects82) == 0:
                                            pass
                                            # State 101987
                                            if len(subjects) == 0:
                                                pass
                                                # 17: cos(e + x*f)**(-2)
                                        subjects82.appendleft(tmp184)
                            subjects178.appendleft(tmp181)
                    if len(subjects178) >= 1 and isinstance(subjects178[0], Mul):
                        tmp185 = subjects178.popleft()
                        associative1 = tmp185
                        associative_type1 = type(tmp185)
                        subjects186 = deque(tmp185._args)
                        matcher = CommutativeMatcher101804.get()
                        tmp187 = subjects186
                        subjects186 = []
                        for s in tmp187:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp187, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 101805
                                if len(subjects178) == 0:
                                    pass
                                    # State 101806
                                    if len(subjects82) >= 1 and subjects82[0] == 2:
                                        tmp188 = subjects82.popleft()
                                        # State 101807
                                        if len(subjects82) == 0:
                                            pass
                                            # State 101808
                                            if len(subjects) == 0:
                                                pass
                                                # 15: cos(e + x*f)**2
                                        subjects82.appendleft(tmp188)
                                    if len(subjects82) >= 1 and subjects82[0] == -2:
                                        tmp189 = subjects82.popleft()
                                        # State 101988
                                        if len(subjects82) == 0:
                                            pass
                                            # State 101989
                                            if len(subjects) == 0:
                                                pass
                                                # 17: cos(e + x*f)**(-2)
                                        subjects82.appendleft(tmp189)
                        subjects178.appendleft(tmp185)
                if len(subjects178) >= 1 and isinstance(subjects178[0], Add):
                    tmp190 = subjects178.popleft()
                    associative1 = tmp190
                    associative_type1 = type(tmp190)
                    subjects191 = deque(tmp190._args)
                    matcher = CommutativeMatcher101810.get()
                    tmp192 = subjects191
                    subjects191 = []
                    for s in tmp192:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp192, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 101816
                            if len(subjects178) == 0:
                                pass
                                # State 101817
                                if len(subjects82) >= 1 and subjects82[0] == 2:
                                    tmp193 = subjects82.popleft()
                                    # State 101818
                                    if len(subjects82) == 0:
                                        pass
                                        # State 101819
                                        if len(subjects) == 0:
                                            pass
                                            # 15: cos(e + x*f)**2
                                    subjects82.appendleft(tmp193)
                                if len(subjects82) >= 1 and subjects82[0] == -2:
                                    tmp194 = subjects82.popleft()
                                    # State 101990
                                    if len(subjects82) == 0:
                                        pass
                                        # State 101991
                                        if len(subjects) == 0:
                                            pass
                                            # 17: cos(e + x*f)**(-2)
                                    subjects82.appendleft(tmp194)
                    subjects178.appendleft(tmp190)
                subjects82.appendleft(tmp177)
            if len(subjects82) >= 1 and isinstance(subjects82[0], sin):
                tmp195 = subjects82.popleft()
                subjects196 = deque(tmp195._args)
                # State 101845
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 101846
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101847
                        if len(subjects196) >= 1:
                            tmp199 = subjects196.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp199)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 101848
                                if len(subjects196) == 0:
                                    pass
                                    # State 101849
                                    if len(subjects82) >= 1 and subjects82[0] == 2:
                                        tmp201 = subjects82.popleft()
                                        # State 101850
                                        if len(subjects82) == 0:
                                            pass
                                            # State 101851
                                            if len(subjects) == 0:
                                                pass
                                                # 16: sin(e + x*f)**2
                                        subjects82.appendleft(tmp201)
                                    if len(subjects82) >= 1 and subjects82[0] == -2:
                                        tmp202 = subjects82.popleft()
                                        # State 102165
                                        if len(subjects82) == 0:
                                            pass
                                            # State 102166
                                            if len(subjects) == 0:
                                                pass
                                                # 19: sin(e + x*f)**(-2)
                                        subjects82.appendleft(tmp202)
                            subjects196.appendleft(tmp199)
                    if len(subjects196) >= 1 and isinstance(subjects196[0], Mul):
                        tmp203 = subjects196.popleft()
                        associative1 = tmp203
                        associative_type1 = type(tmp203)
                        subjects204 = deque(tmp203._args)
                        matcher = CommutativeMatcher101853.get()
                        tmp205 = subjects204
                        subjects204 = []
                        for s in tmp205:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp205, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 101854
                                if len(subjects196) == 0:
                                    pass
                                    # State 101855
                                    if len(subjects82) >= 1 and subjects82[0] == 2:
                                        tmp206 = subjects82.popleft()
                                        # State 101856
                                        if len(subjects82) == 0:
                                            pass
                                            # State 101857
                                            if len(subjects) == 0:
                                                pass
                                                # 16: sin(e + x*f)**2
                                        subjects82.appendleft(tmp206)
                                    if len(subjects82) >= 1 and subjects82[0] == -2:
                                        tmp207 = subjects82.popleft()
                                        # State 102167
                                        if len(subjects82) == 0:
                                            pass
                                            # State 102168
                                            if len(subjects) == 0:
                                                pass
                                                # 19: sin(e + x*f)**(-2)
                                        subjects82.appendleft(tmp207)
                        subjects196.appendleft(tmp203)
                if len(subjects196) >= 1 and isinstance(subjects196[0], Add):
                    tmp208 = subjects196.popleft()
                    associative1 = tmp208
                    associative_type1 = type(tmp208)
                    subjects209 = deque(tmp208._args)
                    matcher = CommutativeMatcher101859.get()
                    tmp210 = subjects209
                    subjects209 = []
                    for s in tmp210:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp210, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 101865
                            if len(subjects196) == 0:
                                pass
                                # State 101866
                                if len(subjects82) >= 1 and subjects82[0] == 2:
                                    tmp211 = subjects82.popleft()
                                    # State 101867
                                    if len(subjects82) == 0:
                                        pass
                                        # State 101868
                                        if len(subjects) == 0:
                                            pass
                                            # 16: sin(e + x*f)**2
                                    subjects82.appendleft(tmp211)
                                if len(subjects82) >= 1 and subjects82[0] == -2:
                                    tmp212 = subjects82.popleft()
                                    # State 102169
                                    if len(subjects82) == 0:
                                        pass
                                        # State 102170
                                        if len(subjects) == 0:
                                            pass
                                            # 19: sin(e + x*f)**(-2)
                                    subjects82.appendleft(tmp212)
                    subjects196.appendleft(tmp208)
                subjects82.appendleft(tmp195)
            if len(subjects82) >= 1 and isinstance(subjects82[0], tan):
                tmp213 = subjects82.popleft()
                subjects214 = deque(tmp213._args)
                # State 102017
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 102018
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102019
                        if len(subjects214) >= 1:
                            tmp217 = subjects214.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp217)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 102020
                                if len(subjects214) == 0:
                                    pass
                                    # State 102021
                                    if len(subjects82) >= 1 and subjects82[0] == 2:
                                        tmp219 = subjects82.popleft()
                                        # State 102022
                                        if len(subjects82) == 0:
                                            pass
                                            # State 102023
                                            if len(subjects) == 0:
                                                pass
                                                # 18: tan(e + x*f)**2
                                        subjects82.appendleft(tmp219)
                                    if len(subjects82) >= 1 and subjects82[0] == -2:
                                        tmp220 = subjects82.popleft()
                                        # State 102178
                                        if len(subjects82) == 0:
                                            pass
                                            # State 102179
                                            if len(subjects) == 0:
                                                pass
                                                # 20: tan(e + x*f)**(-2)
                                        subjects82.appendleft(tmp220)
                            subjects214.appendleft(tmp217)
                    if len(subjects214) >= 1 and isinstance(subjects214[0], Mul):
                        tmp221 = subjects214.popleft()
                        associative1 = tmp221
                        associative_type1 = type(tmp221)
                        subjects222 = deque(tmp221._args)
                        matcher = CommutativeMatcher102025.get()
                        tmp223 = subjects222
                        subjects222 = []
                        for s in tmp223:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp223, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102026
                                if len(subjects214) == 0:
                                    pass
                                    # State 102027
                                    if len(subjects82) >= 1 and subjects82[0] == 2:
                                        tmp224 = subjects82.popleft()
                                        # State 102028
                                        if len(subjects82) == 0:
                                            pass
                                            # State 102029
                                            if len(subjects) == 0:
                                                pass
                                                # 18: tan(e + x*f)**2
                                        subjects82.appendleft(tmp224)
                                    if len(subjects82) >= 1 and subjects82[0] == -2:
                                        tmp225 = subjects82.popleft()
                                        # State 102180
                                        if len(subjects82) == 0:
                                            pass
                                            # State 102181
                                            if len(subjects) == 0:
                                                pass
                                                # 20: tan(e + x*f)**(-2)
                                        subjects82.appendleft(tmp225)
                        subjects214.appendleft(tmp221)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 102684
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102685
                        if len(subjects214) >= 1:
                            tmp228 = subjects214.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.4.1.0', tmp228)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 102686
                                if len(subjects214) == 0:
                                    pass
                                    # State 102687
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.5', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 102688
                                        if len(subjects82) == 0:
                                            pass
                                            # State 102689
                                            if len(subjects) == 0:
                                                pass
                                                # 22: tan(c + x*d)**n
                                    if len(subjects82) >= 1:
                                        tmp231 = subjects82.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.5', tmp231)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 102688
                                            if len(subjects82) == 0:
                                                pass
                                                # State 102689
                                                if len(subjects) == 0:
                                                    pass
                                                    # 22: tan(c + x*d)**n
                                        subjects82.appendleft(tmp231)
                            subjects214.appendleft(tmp228)
                    if len(subjects214) >= 1 and isinstance(subjects214[0], Mul):
                        tmp233 = subjects214.popleft()
                        associative1 = tmp233
                        associative_type1 = type(tmp233)
                        subjects234 = deque(tmp233._args)
                        matcher = CommutativeMatcher102691.get()
                        tmp235 = subjects234
                        subjects234 = []
                        for s in tmp235:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp235, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102692
                                if len(subjects214) == 0:
                                    pass
                                    # State 102693
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.5', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 102694
                                        if len(subjects82) == 0:
                                            pass
                                            # State 102695
                                            if len(subjects) == 0:
                                                pass
                                                # 22: tan(c + x*d)**n
                                    if len(subjects82) >= 1:
                                        tmp237 = subjects82.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.5', tmp237)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 102694
                                            if len(subjects82) == 0:
                                                pass
                                                # State 102695
                                                if len(subjects) == 0:
                                                    pass
                                                    # 22: tan(c + x*d)**n
                                        subjects82.appendleft(tmp237)
                        subjects214.appendleft(tmp233)
                if len(subjects214) >= 1 and isinstance(subjects214[0], Add):
                    tmp239 = subjects214.popleft()
                    associative1 = tmp239
                    associative_type1 = type(tmp239)
                    subjects240 = deque(tmp239._args)
                    matcher = CommutativeMatcher102031.get()
                    tmp241 = subjects240
                    subjects240 = []
                    for s in tmp241:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp241, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 102037
                            if len(subjects214) == 0:
                                pass
                                # State 102038
                                if len(subjects82) >= 1 and subjects82[0] == 2:
                                    tmp242 = subjects82.popleft()
                                    # State 102039
                                    if len(subjects82) == 0:
                                        pass
                                        # State 102040
                                        if len(subjects) == 0:
                                            pass
                                            # 18: tan(e + x*f)**2
                                    subjects82.appendleft(tmp242)
                                if len(subjects82) >= 1 and subjects82[0] == -2:
                                    tmp243 = subjects82.popleft()
                                    # State 102182
                                    if len(subjects82) == 0:
                                        pass
                                        # State 102183
                                        if len(subjects) == 0:
                                            pass
                                            # 20: tan(e + x*f)**(-2)
                                    subjects82.appendleft(tmp243)
                        if pattern_index == 1:
                            pass
                            # State 102699
                            if len(subjects214) == 0:
                                pass
                                # State 102700
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.5', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102701
                                    if len(subjects82) == 0:
                                        pass
                                        # State 102702
                                        if len(subjects) == 0:
                                            pass
                                            # 22: tan(c + x*d)**n
                                if len(subjects82) >= 1:
                                    tmp245 = subjects82.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.1.5', tmp245)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 102701
                                        if len(subjects82) == 0:
                                            pass
                                            # State 102702
                                            if len(subjects) == 0:
                                                pass
                                                # 22: tan(c + x*d)**n
                                    subjects82.appendleft(tmp245)
                    subjects214.appendleft(tmp239)
                subjects82.appendleft(tmp213)
            if len(subjects82) >= 1 and isinstance(subjects82[0], Pow):
                tmp247 = subjects82.popleft()
                subjects248 = deque(tmp247._args)
                # State 102596
                if len(subjects248) >= 1 and isinstance(subjects248[0], cos):
                    tmp249 = subjects248.popleft()
                    subjects250 = deque(tmp249._args)
                    # State 102597
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102598
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102599
                            if len(subjects250) >= 1:
                                tmp253 = subjects250.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.4.1.0', tmp253)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102600
                                    if len(subjects250) == 0:
                                        pass
                                        # State 102601
                                        if len(subjects248) >= 1 and subjects248[0] == -1:
                                            tmp255 = subjects248.popleft()
                                            # State 102602
                                            if len(subjects248) == 0:
                                                pass
                                                # State 102603
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 102604
                                                    if len(subjects82) == 0:
                                                        pass
                                                        # State 102605
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 21: (1/cos(c + x*d))**n
                                                if len(subjects82) >= 1:
                                                    tmp257 = subjects82.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.5', tmp257)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102604
                                                        if len(subjects82) == 0:
                                                            pass
                                                            # State 102605
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 21: (1/cos(c + x*d))**n
                                                    subjects82.appendleft(tmp257)
                                            subjects248.appendleft(tmp255)
                                subjects250.appendleft(tmp253)
                        if len(subjects250) >= 1 and isinstance(subjects250[0], Mul):
                            tmp259 = subjects250.popleft()
                            associative1 = tmp259
                            associative_type1 = type(tmp259)
                            subjects260 = deque(tmp259._args)
                            matcher = CommutativeMatcher102607.get()
                            tmp261 = subjects260
                            subjects260 = []
                            for s in tmp261:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp261, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102608
                                    if len(subjects250) == 0:
                                        pass
                                        # State 102609
                                        if len(subjects248) >= 1 and subjects248[0] == -1:
                                            tmp262 = subjects248.popleft()
                                            # State 102610
                                            if len(subjects248) == 0:
                                                pass
                                                # State 102611
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 102612
                                                    if len(subjects82) == 0:
                                                        pass
                                                        # State 102613
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 21: (1/cos(c + x*d))**n
                                                if len(subjects82) >= 1:
                                                    tmp264 = subjects82.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.5', tmp264)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102612
                                                        if len(subjects82) == 0:
                                                            pass
                                                            # State 102613
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 21: (1/cos(c + x*d))**n
                                                    subjects82.appendleft(tmp264)
                                            subjects248.appendleft(tmp262)
                            subjects250.appendleft(tmp259)
                    if len(subjects250) >= 1 and isinstance(subjects250[0], Add):
                        tmp266 = subjects250.popleft()
                        associative1 = tmp266
                        associative_type1 = type(tmp266)
                        subjects267 = deque(tmp266._args)
                        matcher = CommutativeMatcher102615.get()
                        tmp268 = subjects267
                        subjects267 = []
                        for s in tmp268:
                            matcher.add_subject(s)
                        for pattern_index, subst1 in matcher.match(tmp268, subst0):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102621
                                if len(subjects250) == 0:
                                    pass
                                    # State 102622
                                    if len(subjects248) >= 1 and subjects248[0] == -1:
                                        tmp269 = subjects248.popleft()
                                        # State 102623
                                        if len(subjects248) == 0:
                                            pass
                                            # State 102624
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.5', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 102625
                                                if len(subjects82) == 0:
                                                    pass
                                                    # State 102626
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 21: (1/cos(c + x*d))**n
                                            if len(subjects82) >= 1:
                                                tmp271 = subjects82.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.5', tmp271)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 102625
                                                    if len(subjects82) == 0:
                                                        pass
                                                        # State 102626
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 21: (1/cos(c + x*d))**n
                                                subjects82.appendleft(tmp271)
                                        subjects248.appendleft(tmp269)
                        subjects250.appendleft(tmp266)
                    subjects248.appendleft(tmp249)
                if len(subjects248) >= 1 and isinstance(subjects248[0], sin):
                    tmp273 = subjects248.popleft()
                    subjects274 = deque(tmp273._args)
                    # State 102843
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102844
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102845
                            if len(subjects274) >= 1:
                                tmp277 = subjects274.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.4.1.0', tmp277)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102846
                                    if len(subjects274) == 0:
                                        pass
                                        # State 102847
                                        if len(subjects248) >= 1 and subjects248[0] == -1:
                                            tmp279 = subjects248.popleft()
                                            # State 102848
                                            if len(subjects248) == 0:
                                                pass
                                                # State 102849
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 102850
                                                    if len(subjects82) == 0:
                                                        pass
                                                        # State 102851
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 23: (1/sin(c + x*d))**n
                                                if len(subjects82) >= 1:
                                                    tmp281 = subjects82.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.5', tmp281)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102850
                                                        if len(subjects82) == 0:
                                                            pass
                                                            # State 102851
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 23: (1/sin(c + x*d))**n
                                                    subjects82.appendleft(tmp281)
                                            subjects248.appendleft(tmp279)
                                subjects274.appendleft(tmp277)
                        if len(subjects274) >= 1 and isinstance(subjects274[0], Mul):
                            tmp283 = subjects274.popleft()
                            associative1 = tmp283
                            associative_type1 = type(tmp283)
                            subjects284 = deque(tmp283._args)
                            matcher = CommutativeMatcher102853.get()
                            tmp285 = subjects284
                            subjects284 = []
                            for s in tmp285:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp285, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102854
                                    if len(subjects274) == 0:
                                        pass
                                        # State 102855
                                        if len(subjects248) >= 1 and subjects248[0] == -1:
                                            tmp286 = subjects248.popleft()
                                            # State 102856
                                            if len(subjects248) == 0:
                                                pass
                                                # State 102857
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 102858
                                                    if len(subjects82) == 0:
                                                        pass
                                                        # State 102859
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 23: (1/sin(c + x*d))**n
                                                if len(subjects82) >= 1:
                                                    tmp288 = subjects82.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.5', tmp288)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102858
                                                        if len(subjects82) == 0:
                                                            pass
                                                            # State 102859
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 23: (1/sin(c + x*d))**n
                                                    subjects82.appendleft(tmp288)
                                            subjects248.appendleft(tmp286)
                            subjects274.appendleft(tmp283)
                    if len(subjects274) >= 1 and isinstance(subjects274[0], Add):
                        tmp290 = subjects274.popleft()
                        associative1 = tmp290
                        associative_type1 = type(tmp290)
                        subjects291 = deque(tmp290._args)
                        matcher = CommutativeMatcher102861.get()
                        tmp292 = subjects291
                        subjects291 = []
                        for s in tmp292:
                            matcher.add_subject(s)
                        for pattern_index, subst1 in matcher.match(tmp292, subst0):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102867
                                if len(subjects274) == 0:
                                    pass
                                    # State 102868
                                    if len(subjects248) >= 1 and subjects248[0] == -1:
                                        tmp293 = subjects248.popleft()
                                        # State 102869
                                        if len(subjects248) == 0:
                                            pass
                                            # State 102870
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.5', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 102871
                                                if len(subjects82) == 0:
                                                    pass
                                                    # State 102872
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 23: (1/sin(c + x*d))**n
                                            if len(subjects82) >= 1:
                                                tmp295 = subjects82.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.5', tmp295)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 102871
                                                    if len(subjects82) == 0:
                                                        pass
                                                        # State 102872
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 23: (1/sin(c + x*d))**n
                                                subjects82.appendleft(tmp295)
                                        subjects248.appendleft(tmp293)
                        subjects274.appendleft(tmp290)
                    subjects248.appendleft(tmp273)
                if len(subjects248) >= 1 and isinstance(subjects248[0], tan):
                    tmp297 = subjects248.popleft()
                    subjects298 = deque(tmp297._args)
                    # State 102954
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.4.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102955
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.4.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102956
                            if len(subjects298) >= 1:
                                tmp301 = subjects298.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.4.1.0', tmp301)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102957
                                    if len(subjects298) == 0:
                                        pass
                                        # State 102958
                                        if len(subjects248) >= 1 and subjects248[0] == -1:
                                            tmp303 = subjects248.popleft()
                                            # State 102959
                                            if len(subjects248) == 0:
                                                pass
                                                # State 102960
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 102961
                                                    if len(subjects82) == 0:
                                                        pass
                                                        # State 102962
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 24: (1/tan(c + x*d))**n
                                                if len(subjects82) >= 1:
                                                    tmp305 = subjects82.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.5', tmp305)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102961
                                                        if len(subjects82) == 0:
                                                            pass
                                                            # State 102962
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 24: (1/tan(c + x*d))**n
                                                    subjects82.appendleft(tmp305)
                                            subjects248.appendleft(tmp303)
                                subjects298.appendleft(tmp301)
                        if len(subjects298) >= 1 and isinstance(subjects298[0], Mul):
                            tmp307 = subjects298.popleft()
                            associative1 = tmp307
                            associative_type1 = type(tmp307)
                            subjects308 = deque(tmp307._args)
                            matcher = CommutativeMatcher102964.get()
                            tmp309 = subjects308
                            subjects308 = []
                            for s in tmp309:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp309, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102965
                                    if len(subjects298) == 0:
                                        pass
                                        # State 102966
                                        if len(subjects248) >= 1 and subjects248[0] == -1:
                                            tmp310 = subjects248.popleft()
                                            # State 102967
                                            if len(subjects248) == 0:
                                                pass
                                                # State 102968
                                                subst3 = Substitution(subst2)
                                                try:
                                                    subst3.try_add_variable('i2.2.1.5', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 102969
                                                    if len(subjects82) == 0:
                                                        pass
                                                        # State 102970
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 24: (1/tan(c + x*d))**n
                                                if len(subjects82) >= 1:
                                                    tmp312 = subjects82.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.1.5', tmp312)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 102969
                                                        if len(subjects82) == 0:
                                                            pass
                                                            # State 102970
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 24: (1/tan(c + x*d))**n
                                                    subjects82.appendleft(tmp312)
                                            subjects248.appendleft(tmp310)
                            subjects298.appendleft(tmp307)
                    if len(subjects298) >= 1 and isinstance(subjects298[0], Add):
                        tmp314 = subjects298.popleft()
                        associative1 = tmp314
                        associative_type1 = type(tmp314)
                        subjects315 = deque(tmp314._args)
                        matcher = CommutativeMatcher102972.get()
                        tmp316 = subjects315
                        subjects315 = []
                        for s in tmp316:
                            matcher.add_subject(s)
                        for pattern_index, subst1 in matcher.match(tmp316, subst0):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102978
                                if len(subjects298) == 0:
                                    pass
                                    # State 102979
                                    if len(subjects248) >= 1 and subjects248[0] == -1:
                                        tmp317 = subjects248.popleft()
                                        # State 102980
                                        if len(subjects248) == 0:
                                            pass
                                            # State 102981
                                            subst2 = Substitution(subst1)
                                            try:
                                                subst2.try_add_variable('i2.2.1.5', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 102982
                                                if len(subjects82) == 0:
                                                    pass
                                                    # State 102983
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 24: (1/tan(c + x*d))**n
                                            if len(subjects82) >= 1:
                                                tmp319 = subjects82.popleft()
                                                subst2 = Substitution(subst1)
                                                try:
                                                    subst2.try_add_variable('i2.2.1.5', tmp319)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 102982
                                                    if len(subjects82) == 0:
                                                        pass
                                                        # State 102983
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 24: (1/tan(c + x*d))**n
                                                subjects82.appendleft(tmp319)
                                        subjects248.appendleft(tmp317)
                        subjects298.appendleft(tmp314)
                    subjects248.appendleft(tmp297)
                subjects82.appendleft(tmp247)
            if len(subjects82) >= 1 and isinstance(subjects82[0], Mul):
                tmp321 = subjects82.popleft()
                associative1 = tmp321
                associative_type1 = type(tmp321)
                subjects322 = deque(tmp321._args)
                matcher = CommutativeMatcher152058.get()
                tmp323 = subjects322
                subjects322 = []
                for s in tmp323:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp323, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 152063
                        if len(subjects82) >= 1 and subjects82[0] == 1/2:
                            tmp324 = subjects82.popleft()
                            # State 152064
                            if len(subjects82) == 0:
                                pass
                                # State 152065
                                if len(subjects) == 0:
                                    pass
                                    # 37: sqrt(c*x**n)
                            subjects82.appendleft(tmp324)
                subjects82.appendleft(tmp321)
            subjects.appendleft(tmp81)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp325 = subjects.popleft()
            subjects326 = deque(tmp325._args)
            # State 43145
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 43146
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 43147
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 43148
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 43149
                            if len(subjects326) >= 1 and isinstance(subjects326[0], Add):
                                tmp331 = subjects326.popleft()
                                associative1 = tmp331
                                associative_type1 = type(tmp331)
                                subjects332 = deque(tmp331._args)
                                matcher = CommutativeMatcher43151.get()
                                tmp333 = subjects332
                                subjects332 = []
                                for s in tmp333:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp333, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 43167
                                        if len(subjects326) == 0:
                                            pass
                                            # State 43168
                                            if len(subjects) == 0:
                                                pass
                                                # 11: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                    if pattern_index == 1:
                                        pass
                                        # State 55019
                                        if len(subjects326) == 0:
                                            pass
                                            # State 55020
                                            if len(subjects) == 0:
                                                pass
                                                # 14: log(c*(d*(e + x*f)**p)**q)
                                subjects326.appendleft(tmp331)
                            if len(subjects326) >= 1:
                                tmp334 = subjects326.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.1', tmp334)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45332
                                    if len(subjects326) == 0:
                                        pass
                                        # State 45333
                                        if len(subjects) == 0:
                                            pass
                                            # 12: log(c*(d*v**p)**q)
                                subjects326.appendleft(tmp334)
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 55009
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 55010
                                    if len(subjects326) >= 1:
                                        tmp338 = subjects326.popleft()
                                        subst7 = Substitution(subst6)
                                        try:
                                            subst7.try_add_variable('i2.2.1.2.2.2.1.0', tmp338)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 55011
                                            if len(subjects326) == 0:
                                                pass
                                                # State 55012
                                                if len(subjects) == 0:
                                                    pass
                                                    # 14: log(c*(d*(e + x*f)**p)**q)
                                        subjects326.appendleft(tmp338)
                                if len(subjects326) >= 1 and isinstance(subjects326[0], Mul):
                                    tmp340 = subjects326.popleft()
                                    associative1 = tmp340
                                    associative_type1 = type(tmp340)
                                    subjects341 = deque(tmp340._args)
                                    matcher = CommutativeMatcher55014.get()
                                    tmp342 = subjects341
                                    subjects341 = []
                                    for s in tmp342:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp342, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 55015
                                            if len(subjects326) == 0:
                                                pass
                                                # State 55016
                                                if len(subjects) == 0:
                                                    pass
                                                    # 14: log(c*(d*(e + x*f)**p)**q)
                                    subjects326.appendleft(tmp340)
                        if len(subjects326) >= 1 and isinstance(subjects326[0], Pow):
                            tmp343 = subjects326.popleft()
                            subjects344 = deque(tmp343._args)
                            # State 43169
                            if len(subjects344) >= 1 and isinstance(subjects344[0], Add):
                                tmp345 = subjects344.popleft()
                                associative1 = tmp345
                                associative_type1 = type(tmp345)
                                subjects346 = deque(tmp345._args)
                                matcher = CommutativeMatcher43171.get()
                                tmp347 = subjects346
                                subjects346 = []
                                for s in tmp347:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp347, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 43187
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43188
                                            if len(subjects344) == 0:
                                                pass
                                                # State 43189
                                                if len(subjects326) == 0:
                                                    pass
                                                    # State 43190
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 11: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                        if len(subjects344) >= 1:
                                            tmp349 = []
                                            tmp349.append(subjects344.popleft())
                                            while True:
                                                if len(tmp349) > 1:
                                                    tmp350 = create_operation_expression(associative1, tmp349)
                                                elif len(tmp349) == 1:
                                                    tmp350 = tmp349[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp350)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 43188
                                                    if len(subjects344) == 0:
                                                        pass
                                                        # State 43189
                                                        if len(subjects326) == 0:
                                                            pass
                                                            # State 43190
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 11: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                if len(subjects344) == 0:
                                                    break
                                                tmp349.append(subjects344.popleft())
                                            subjects344.extendleft(reversed(tmp349))
                                    if pattern_index == 1:
                                        pass
                                        # State 55035
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 55036
                                            if len(subjects344) == 0:
                                                pass
                                                # State 55037
                                                if len(subjects326) == 0:
                                                    pass
                                                    # State 55038
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 14: log(c*(d*(e + x*f)**p)**q)
                                        if len(subjects344) >= 1:
                                            tmp353 = []
                                            tmp353.append(subjects344.popleft())
                                            while True:
                                                if len(tmp353) > 1:
                                                    tmp354 = create_operation_expression(associative1, tmp353)
                                                elif len(tmp353) == 1:
                                                    tmp354 = tmp353[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp354)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 55036
                                                    if len(subjects344) == 0:
                                                        pass
                                                        # State 55037
                                                        if len(subjects326) == 0:
                                                            pass
                                                            # State 55038
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 14: log(c*(d*(e + x*f)**p)**q)
                                                if len(subjects344) == 0:
                                                    break
                                                tmp353.append(subjects344.popleft())
                                            subjects344.extendleft(reversed(tmp353))
                                subjects344.appendleft(tmp345)
                            if len(subjects344) >= 1:
                                tmp356 = subjects344.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.1', tmp356)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45334
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45335
                                        if len(subjects344) == 0:
                                            pass
                                            # State 45336
                                            if len(subjects326) == 0:
                                                pass
                                                # State 45337
                                                if len(subjects) == 0:
                                                    pass
                                                    # 12: log(c*(d*v**p)**q)
                                    if len(subjects344) >= 1:
                                        tmp359 = subjects344.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp359)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45335
                                            if len(subjects344) == 0:
                                                pass
                                                # State 45336
                                                if len(subjects326) == 0:
                                                    pass
                                                    # State 45337
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 12: log(c*(d*v**p)**q)
                                        subjects344.appendleft(tmp359)
                                subjects344.appendleft(tmp356)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 55021
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 55022
                                    if len(subjects344) >= 1:
                                        tmp363 = subjects344.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp363)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 55023
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 55024
                                                if len(subjects344) == 0:
                                                    pass
                                                    # State 55025
                                                    if len(subjects326) == 0:
                                                        pass
                                                        # State 55026
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 14: log(c*(d*(e + x*f)**p)**q)
                                            if len(subjects344) >= 1:
                                                tmp366 = subjects344.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.2.2.2', tmp366)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 55024
                                                    if len(subjects344) == 0:
                                                        pass
                                                        # State 55025
                                                        if len(subjects326) == 0:
                                                            pass
                                                            # State 55026
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 14: log(c*(d*(e + x*f)**p)**q)
                                                subjects344.appendleft(tmp366)
                                        subjects344.appendleft(tmp363)
                                if len(subjects344) >= 1 and isinstance(subjects344[0], Mul):
                                    tmp368 = subjects344.popleft()
                                    associative1 = tmp368
                                    associative_type1 = type(tmp368)
                                    subjects369 = deque(tmp368._args)
                                    matcher = CommutativeMatcher55028.get()
                                    tmp370 = subjects369
                                    subjects369 = []
                                    for s in tmp370:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp370, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 55029
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 55030
                                                if len(subjects344) == 0:
                                                    pass
                                                    # State 55031
                                                    if len(subjects326) == 0:
                                                        pass
                                                        # State 55032
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 14: log(c*(d*(e + x*f)**p)**q)
                                            if len(subjects344) >= 1:
                                                tmp372 = []
                                                tmp372.append(subjects344.popleft())
                                                while True:
                                                    if len(tmp372) > 1:
                                                        tmp373 = create_operation_expression(associative1, tmp372)
                                                    elif len(tmp372) == 1:
                                                        tmp373 = tmp372[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', tmp373)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 55030
                                                        if len(subjects344) == 0:
                                                            pass
                                                            # State 55031
                                                            if len(subjects326) == 0:
                                                                pass
                                                                # State 55032
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 14: log(c*(d*(e + x*f)**p)**q)
                                                    if len(subjects344) == 0:
                                                        break
                                                    tmp372.append(subjects344.popleft())
                                                subjects344.extendleft(reversed(tmp372))
                                    subjects344.appendleft(tmp368)
                            subjects326.appendleft(tmp343)
                    if len(subjects326) >= 1 and isinstance(subjects326[0], Mul):
                        tmp375 = subjects326.popleft()
                        associative1 = tmp375
                        associative_type1 = type(tmp375)
                        subjects376 = deque(tmp375._args)
                        matcher = CommutativeMatcher43192.get()
                        tmp377 = subjects376
                        subjects376 = []
                        for s in tmp377:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp377, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 43233
                                if len(subjects326) == 0:
                                    pass
                                    # State 43234
                                    if len(subjects) == 0:
                                        pass
                                        # 11: log(c*(d*(e + f*x + g*x**2)**p)**q)
                            if pattern_index == 1:
                                pass
                                # State 45342
                                if len(subjects326) == 0:
                                    pass
                                    # State 45343
                                    if len(subjects) == 0:
                                        pass
                                        # 12: log(c*(d*v**p)**q)
                            if pattern_index == 2:
                                pass
                                # State 55063
                                if len(subjects326) == 0:
                                    pass
                                    # State 55064
                                    if len(subjects) == 0:
                                        pass
                                        # 14: log(c*(d*(e + x*f)**p)**q)
                        subjects326.appendleft(tmp375)
                if len(subjects326) >= 1 and isinstance(subjects326[0], Pow):
                    tmp378 = subjects326.popleft()
                    subjects379 = deque(tmp378._args)
                    # State 43235
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 43236
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 43237
                            if len(subjects379) >= 1 and isinstance(subjects379[0], Add):
                                tmp382 = subjects379.popleft()
                                associative1 = tmp382
                                associative_type1 = type(tmp382)
                                subjects383 = deque(tmp382._args)
                                matcher = CommutativeMatcher43239.get()
                                tmp384 = subjects383
                                subjects383 = []
                                for s in tmp384:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp384, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 43255
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43256
                                            if len(subjects379) == 0:
                                                pass
                                                # State 43257
                                                if len(subjects326) == 0:
                                                    pass
                                                    # State 43258
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 11: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                        if len(subjects379) >= 1:
                                            tmp386 = []
                                            tmp386.append(subjects379.popleft())
                                            while True:
                                                if len(tmp386) > 1:
                                                    tmp387 = create_operation_expression(associative1, tmp386)
                                                elif len(tmp386) == 1:
                                                    tmp387 = tmp386[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp387)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 43256
                                                    if len(subjects379) == 0:
                                                        pass
                                                        # State 43257
                                                        if len(subjects326) == 0:
                                                            pass
                                                            # State 43258
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 11: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                if len(subjects379) == 0:
                                                    break
                                                tmp386.append(subjects379.popleft())
                                            subjects379.extendleft(reversed(tmp386))
                                    if pattern_index == 1:
                                        pass
                                        # State 55079
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 55080
                                            if len(subjects379) == 0:
                                                pass
                                                # State 55081
                                                if len(subjects326) == 0:
                                                    pass
                                                    # State 55082
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 14: log(c*(d*(e + x*f)**p)**q)
                                        if len(subjects379) >= 1:
                                            tmp390 = []
                                            tmp390.append(subjects379.popleft())
                                            while True:
                                                if len(tmp390) > 1:
                                                    tmp391 = create_operation_expression(associative1, tmp390)
                                                elif len(tmp390) == 1:
                                                    tmp391 = tmp390[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp391)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 55080
                                                    if len(subjects379) == 0:
                                                        pass
                                                        # State 55081
                                                        if len(subjects326) == 0:
                                                            pass
                                                            # State 55082
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 14: log(c*(d*(e + x*f)**p)**q)
                                                if len(subjects379) == 0:
                                                    break
                                                tmp390.append(subjects379.popleft())
                                            subjects379.extendleft(reversed(tmp390))
                                subjects379.appendleft(tmp382)
                            if len(subjects379) >= 1:
                                tmp393 = subjects379.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.1', tmp393)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45344
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45345
                                        if len(subjects379) == 0:
                                            pass
                                            # State 45346
                                            if len(subjects326) == 0:
                                                pass
                                                # State 45347
                                                if len(subjects) == 0:
                                                    pass
                                                    # 12: log(c*(d*v**p)**q)
                                    if len(subjects379) >= 1:
                                        tmp396 = subjects379.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', tmp396)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45345
                                            if len(subjects379) == 0:
                                                pass
                                                # State 45346
                                                if len(subjects326) == 0:
                                                    pass
                                                    # State 45347
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 12: log(c*(d*v**p)**q)
                                        subjects379.appendleft(tmp396)
                                subjects379.appendleft(tmp393)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 55065
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 55066
                                    if len(subjects379) >= 1:
                                        tmp400 = subjects379.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp400)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 55067
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 55068
                                                if len(subjects379) == 0:
                                                    pass
                                                    # State 55069
                                                    if len(subjects326) == 0:
                                                        pass
                                                        # State 55070
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 14: log(c*(d*(e + x*f)**p)**q)
                                            if len(subjects379) >= 1:
                                                tmp403 = subjects379.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.2.2', tmp403)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 55068
                                                    if len(subjects379) == 0:
                                                        pass
                                                        # State 55069
                                                        if len(subjects326) == 0:
                                                            pass
                                                            # State 55070
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 14: log(c*(d*(e + x*f)**p)**q)
                                                subjects379.appendleft(tmp403)
                                        subjects379.appendleft(tmp400)
                                if len(subjects379) >= 1 and isinstance(subjects379[0], Mul):
                                    tmp405 = subjects379.popleft()
                                    associative1 = tmp405
                                    associative_type1 = type(tmp405)
                                    subjects406 = deque(tmp405._args)
                                    matcher = CommutativeMatcher55072.get()
                                    tmp407 = subjects406
                                    subjects406 = []
                                    for s in tmp407:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp407, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 55073
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 55074
                                                if len(subjects379) == 0:
                                                    pass
                                                    # State 55075
                                                    if len(subjects326) == 0:
                                                        pass
                                                        # State 55076
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 14: log(c*(d*(e + x*f)**p)**q)
                                            if len(subjects379) >= 1:
                                                tmp409 = []
                                                tmp409.append(subjects379.popleft())
                                                while True:
                                                    if len(tmp409) > 1:
                                                        tmp410 = create_operation_expression(associative1, tmp409)
                                                    elif len(tmp409) == 1:
                                                        tmp410 = tmp409[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp410)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 55074
                                                        if len(subjects379) == 0:
                                                            pass
                                                            # State 55075
                                                            if len(subjects326) == 0:
                                                                pass
                                                                # State 55076
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 14: log(c*(d*(e + x*f)**p)**q)
                                                    if len(subjects379) == 0:
                                                        break
                                                    tmp409.append(subjects379.popleft())
                                                subjects379.extendleft(reversed(tmp409))
                                    subjects379.appendleft(tmp405)
                        if len(subjects379) >= 1 and isinstance(subjects379[0], Pow):
                            tmp412 = subjects379.popleft()
                            subjects413 = deque(tmp412._args)
                            # State 43259
                            if len(subjects413) >= 1 and isinstance(subjects413[0], Add):
                                tmp414 = subjects413.popleft()
                                associative1 = tmp414
                                associative_type1 = type(tmp414)
                                subjects415 = deque(tmp414._args)
                                matcher = CommutativeMatcher43261.get()
                                tmp416 = subjects415
                                subjects415 = []
                                for s in tmp416:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp416, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 43277
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43278
                                            if len(subjects413) == 0:
                                                pass
                                                # State 43279
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 43280
                                                    if len(subjects379) == 0:
                                                        pass
                                                        # State 43281
                                                        if len(subjects326) == 0:
                                                            pass
                                                            # State 43282
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 11: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                if len(subjects379) >= 1:
                                                    tmp419 = subjects379.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp419)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 43280
                                                        if len(subjects379) == 0:
                                                            pass
                                                            # State 43281
                                                            if len(subjects326) == 0:
                                                                pass
                                                                # State 43282
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 11: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                    subjects379.appendleft(tmp419)
                                        if len(subjects413) >= 1:
                                            tmp421 = []
                                            tmp421.append(subjects413.popleft())
                                            while True:
                                                if len(tmp421) > 1:
                                                    tmp422 = create_operation_expression(associative1, tmp421)
                                                elif len(tmp421) == 1:
                                                    tmp422 = tmp421[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp422)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 43278
                                                    if len(subjects413) == 0:
                                                        pass
                                                        # State 43279
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 43280
                                                            if len(subjects379) == 0:
                                                                pass
                                                                # State 43281
                                                                if len(subjects326) == 0:
                                                                    pass
                                                                    # State 43282
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 11: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                        if len(subjects379) >= 1:
                                                            tmp425 = subjects379.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp425)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 43280
                                                                if len(subjects379) == 0:
                                                                    pass
                                                                    # State 43281
                                                                    if len(subjects326) == 0:
                                                                        pass
                                                                        # State 43282
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 11: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                            subjects379.appendleft(tmp425)
                                                if len(subjects413) == 0:
                                                    break
                                                tmp421.append(subjects413.popleft())
                                            subjects413.extendleft(reversed(tmp421))
                                    if pattern_index == 1:
                                        pass
                                        # State 55101
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 55102
                                            if len(subjects413) == 0:
                                                pass
                                                # State 55103
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 55104
                                                    if len(subjects379) == 0:
                                                        pass
                                                        # State 55105
                                                        if len(subjects326) == 0:
                                                            pass
                                                            # State 55106
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 14: log(c*(d*(e + x*f)**p)**q)
                                                if len(subjects379) >= 1:
                                                    tmp429 = subjects379.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp429)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 55104
                                                        if len(subjects379) == 0:
                                                            pass
                                                            # State 55105
                                                            if len(subjects326) == 0:
                                                                pass
                                                                # State 55106
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 14: log(c*(d*(e + x*f)**p)**q)
                                                    subjects379.appendleft(tmp429)
                                        if len(subjects413) >= 1:
                                            tmp431 = []
                                            tmp431.append(subjects413.popleft())
                                            while True:
                                                if len(tmp431) > 1:
                                                    tmp432 = create_operation_expression(associative1, tmp431)
                                                elif len(tmp431) == 1:
                                                    tmp432 = tmp431[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp432)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 55102
                                                    if len(subjects413) == 0:
                                                        pass
                                                        # State 55103
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 55104
                                                            if len(subjects379) == 0:
                                                                pass
                                                                # State 55105
                                                                if len(subjects326) == 0:
                                                                    pass
                                                                    # State 55106
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 14: log(c*(d*(e + x*f)**p)**q)
                                                        if len(subjects379) >= 1:
                                                            tmp435 = subjects379.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp435)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 55104
                                                                if len(subjects379) == 0:
                                                                    pass
                                                                    # State 55105
                                                                    if len(subjects326) == 0:
                                                                        pass
                                                                        # State 55106
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 14: log(c*(d*(e + x*f)**p)**q)
                                                            subjects379.appendleft(tmp435)
                                                if len(subjects413) == 0:
                                                    break
                                                tmp431.append(subjects413.popleft())
                                            subjects413.extendleft(reversed(tmp431))
                                subjects413.appendleft(tmp414)
                            if len(subjects413) >= 1:
                                tmp437 = subjects413.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.1', tmp437)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45348
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45349
                                        if len(subjects413) == 0:
                                            pass
                                            # State 45350
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45351
                                                if len(subjects379) == 0:
                                                    pass
                                                    # State 45352
                                                    if len(subjects326) == 0:
                                                        pass
                                                        # State 45353
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 12: log(c*(d*v**p)**q)
                                            if len(subjects379) >= 1:
                                                tmp441 = subjects379.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp441)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 45351
                                                    if len(subjects379) == 0:
                                                        pass
                                                        # State 45352
                                                        if len(subjects326) == 0:
                                                            pass
                                                            # State 45353
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 12: log(c*(d*v**p)**q)
                                                subjects379.appendleft(tmp441)
                                    if len(subjects413) >= 1:
                                        tmp443 = subjects413.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp443)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45349
                                            if len(subjects413) == 0:
                                                pass
                                                # State 45350
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 45351
                                                    if len(subjects379) == 0:
                                                        pass
                                                        # State 45352
                                                        if len(subjects326) == 0:
                                                            pass
                                                            # State 45353
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 12: log(c*(d*v**p)**q)
                                                if len(subjects379) >= 1:
                                                    tmp446 = subjects379.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp446)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 45351
                                                        if len(subjects379) == 0:
                                                            pass
                                                            # State 45352
                                                            if len(subjects326) == 0:
                                                                pass
                                                                # State 45353
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 12: log(c*(d*v**p)**q)
                                                    subjects379.appendleft(tmp446)
                                        subjects413.appendleft(tmp443)
                                subjects413.appendleft(tmp437)
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 55083
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 55084
                                    if len(subjects413) >= 1:
                                        tmp450 = subjects413.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp450)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 55085
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 55086
                                                if len(subjects413) == 0:
                                                    pass
                                                    # State 55087
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 55088
                                                        if len(subjects379) == 0:
                                                            pass
                                                            # State 55089
                                                            if len(subjects326) == 0:
                                                                pass
                                                                # State 55090
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 14: log(c*(d*(e + x*f)**p)**q)
                                                    if len(subjects379) >= 1:
                                                        tmp454 = subjects379.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', tmp454)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 55088
                                                            if len(subjects379) == 0:
                                                                pass
                                                                # State 55089
                                                                if len(subjects326) == 0:
                                                                    pass
                                                                    # State 55090
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 14: log(c*(d*(e + x*f)**p)**q)
                                                        subjects379.appendleft(tmp454)
                                            if len(subjects413) >= 1:
                                                tmp456 = subjects413.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2.2', tmp456)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 55086
                                                    if len(subjects413) == 0:
                                                        pass
                                                        # State 55087
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 55088
                                                            if len(subjects379) == 0:
                                                                pass
                                                                # State 55089
                                                                if len(subjects326) == 0:
                                                                    pass
                                                                    # State 55090
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 14: log(c*(d*(e + x*f)**p)**q)
                                                        if len(subjects379) >= 1:
                                                            tmp459 = subjects379.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2', tmp459)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 55088
                                                                if len(subjects379) == 0:
                                                                    pass
                                                                    # State 55089
                                                                    if len(subjects326) == 0:
                                                                        pass
                                                                        # State 55090
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 14: log(c*(d*(e + x*f)**p)**q)
                                                            subjects379.appendleft(tmp459)
                                                subjects413.appendleft(tmp456)
                                        subjects413.appendleft(tmp450)
                                if len(subjects413) >= 1 and isinstance(subjects413[0], Mul):
                                    tmp461 = subjects413.popleft()
                                    associative1 = tmp461
                                    associative_type1 = type(tmp461)
                                    subjects462 = deque(tmp461._args)
                                    matcher = CommutativeMatcher55092.get()
                                    tmp463 = subjects462
                                    subjects462 = []
                                    for s in tmp463:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp463, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 55093
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 55094
                                                if len(subjects413) == 0:
                                                    pass
                                                    # State 55095
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 55096
                                                        if len(subjects379) == 0:
                                                            pass
                                                            # State 55097
                                                            if len(subjects326) == 0:
                                                                pass
                                                                # State 55098
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 14: log(c*(d*(e + x*f)**p)**q)
                                                    if len(subjects379) >= 1:
                                                        tmp466 = subjects379.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp466)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 55096
                                                            if len(subjects379) == 0:
                                                                pass
                                                                # State 55097
                                                                if len(subjects326) == 0:
                                                                    pass
                                                                    # State 55098
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 14: log(c*(d*(e + x*f)**p)**q)
                                                        subjects379.appendleft(tmp466)
                                            if len(subjects413) >= 1:
                                                tmp468 = []
                                                tmp468.append(subjects413.popleft())
                                                while True:
                                                    if len(tmp468) > 1:
                                                        tmp469 = create_operation_expression(associative1, tmp468)
                                                    elif len(tmp468) == 1:
                                                        tmp469 = tmp468[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2.2', tmp469)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 55094
                                                        if len(subjects413) == 0:
                                                            pass
                                                            # State 55095
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 55096
                                                                if len(subjects379) == 0:
                                                                    pass
                                                                    # State 55097
                                                                    if len(subjects326) == 0:
                                                                        pass
                                                                        # State 55098
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 14: log(c*(d*(e + x*f)**p)**q)
                                                            if len(subjects379) >= 1:
                                                                tmp472 = subjects379.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2.1.2.2', tmp472)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 55096
                                                                    if len(subjects379) == 0:
                                                                        pass
                                                                        # State 55097
                                                                        if len(subjects326) == 0:
                                                                            pass
                                                                            # State 55098
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 14: log(c*(d*(e + x*f)**p)**q)
                                                                subjects379.appendleft(tmp472)
                                                    if len(subjects413) == 0:
                                                        break
                                                    tmp468.append(subjects413.popleft())
                                                subjects413.extendleft(reversed(tmp468))
                                    subjects413.appendleft(tmp461)
                            subjects379.appendleft(tmp412)
                    if len(subjects379) >= 1 and isinstance(subjects379[0], Mul):
                        tmp474 = subjects379.popleft()
                        associative1 = tmp474
                        associative_type1 = type(tmp474)
                        subjects475 = deque(tmp474._args)
                        matcher = CommutativeMatcher43284.get()
                        tmp476 = subjects475
                        subjects475 = []
                        for s in tmp476:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp476, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 43325
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 43326
                                    if len(subjects379) == 0:
                                        pass
                                        # State 43327
                                        if len(subjects326) == 0:
                                            pass
                                            # State 43328
                                            if len(subjects) == 0:
                                                pass
                                                # 11: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                if len(subjects379) >= 1:
                                    tmp478 = []
                                    tmp478.append(subjects379.popleft())
                                    while True:
                                        if len(tmp478) > 1:
                                            tmp479 = create_operation_expression(associative1, tmp478)
                                        elif len(tmp478) == 1:
                                            tmp479 = tmp478[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp479)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43326
                                            if len(subjects379) == 0:
                                                pass
                                                # State 43327
                                                if len(subjects326) == 0:
                                                    pass
                                                    # State 43328
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 11: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                        if len(subjects379) == 0:
                                            break
                                        tmp478.append(subjects379.popleft())
                                    subjects379.extendleft(reversed(tmp478))
                            if pattern_index == 1:
                                pass
                                # State 45358
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45359
                                    if len(subjects379) == 0:
                                        pass
                                        # State 45360
                                        if len(subjects326) == 0:
                                            pass
                                            # State 45361
                                            if len(subjects) == 0:
                                                pass
                                                # 12: log(c*(d*v**p)**q)
                                if len(subjects379) >= 1:
                                    tmp482 = []
                                    tmp482.append(subjects379.popleft())
                                    while True:
                                        if len(tmp482) > 1:
                                            tmp483 = create_operation_expression(associative1, tmp482)
                                        elif len(tmp482) == 1:
                                            tmp483 = tmp482[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp483)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45359
                                            if len(subjects379) == 0:
                                                pass
                                                # State 45360
                                                if len(subjects326) == 0:
                                                    pass
                                                    # State 45361
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 12: log(c*(d*v**p)**q)
                                        if len(subjects379) == 0:
                                            break
                                        tmp482.append(subjects379.popleft())
                                    subjects379.extendleft(reversed(tmp482))
                            if pattern_index == 2:
                                pass
                                # State 55131
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 55132
                                    if len(subjects379) == 0:
                                        pass
                                        # State 55133
                                        if len(subjects326) == 0:
                                            pass
                                            # State 55134
                                            if len(subjects) == 0:
                                                pass
                                                # 14: log(c*(d*(e + x*f)**p)**q)
                                if len(subjects379) >= 1:
                                    tmp486 = []
                                    tmp486.append(subjects379.popleft())
                                    while True:
                                        if len(tmp486) > 1:
                                            tmp487 = create_operation_expression(associative1, tmp486)
                                        elif len(tmp486) == 1:
                                            tmp487 = tmp486[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp487)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 55132
                                            if len(subjects379) == 0:
                                                pass
                                                # State 55133
                                                if len(subjects326) == 0:
                                                    pass
                                                    # State 55134
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 14: log(c*(d*(e + x*f)**p)**q)
                                        if len(subjects379) == 0:
                                            break
                                        tmp486.append(subjects379.popleft())
                                    subjects379.extendleft(reversed(tmp486))
                        subjects379.appendleft(tmp474)
                    subjects326.appendleft(tmp378)
            if len(subjects326) >= 1 and isinstance(subjects326[0], Mul):
                tmp489 = subjects326.popleft()
                associative1 = tmp489
                associative_type1 = type(tmp489)
                subjects490 = deque(tmp489._args)
                matcher = CommutativeMatcher43330.get()
                tmp491 = subjects490
                subjects490 = []
                for s in tmp491:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp491, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 43507
                        if len(subjects326) == 0:
                            pass
                            # State 43508
                            if len(subjects) == 0:
                                pass
                                # 11: log(c*(d*(e + f*x + g*x**2)**p)**q)
                    if pattern_index == 1:
                        pass
                        # State 45386
                        if len(subjects326) == 0:
                            pass
                            # State 45387
                            if len(subjects) == 0:
                                pass
                                # 12: log(c*(d*v**p)**q)
                    if pattern_index == 2:
                        pass
                        # State 55247
                        if len(subjects326) == 0:
                            pass
                            # State 55248
                            if len(subjects) == 0:
                                pass
                                # 14: log(c*(d*(e + x*f)**p)**q)
                subjects326.appendleft(tmp489)
            subjects.appendleft(tmp325)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp492 = subjects.popleft()
            subjects493 = deque(tmp492._args)
            # State 103304
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 103305
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 103306
                    if len(subjects493) >= 1:
                        tmp496 = subjects493.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp496)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 103307
                            if len(subjects493) == 0:
                                pass
                                # State 103308
                                if len(subjects) == 0:
                                    pass
                                    # 25: cos(c + x*d)
                        subjects493.appendleft(tmp496)
                if len(subjects493) >= 1 and isinstance(subjects493[0], Mul):
                    tmp498 = subjects493.popleft()
                    associative1 = tmp498
                    associative_type1 = type(tmp498)
                    subjects499 = deque(tmp498._args)
                    matcher = CommutativeMatcher103310.get()
                    tmp500 = subjects499
                    subjects499 = []
                    for s in tmp500:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp500, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 103311
                            if len(subjects493) == 0:
                                pass
                                # State 103312
                                if len(subjects) == 0:
                                    pass
                                    # 25: cos(c + x*d)
                    subjects493.appendleft(tmp498)
            if len(subjects493) >= 1:
                tmp501 = subjects493.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp501)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107929
                    if len(subjects493) == 0:
                        pass
                        # State 107930
                        if len(subjects) == 0:
                            pass
                            # 27: cos(v)
                subjects493.appendleft(tmp501)
            if len(subjects493) >= 1 and isinstance(subjects493[0], Add):
                tmp503 = subjects493.popleft()
                associative1 = tmp503
                associative_type1 = type(tmp503)
                subjects504 = deque(tmp503._args)
                matcher = CommutativeMatcher103314.get()
                tmp505 = subjects504
                subjects504 = []
                for s in tmp505:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp505, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 103320
                        if len(subjects493) == 0:
                            pass
                            # State 103321
                            if len(subjects) == 0:
                                pass
                                # 25: cos(c + x*d)
                subjects493.appendleft(tmp503)
            subjects.appendleft(tmp492)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp506 = subjects.popleft()
            subjects507 = deque(tmp506._args)
            # State 103341
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 103342
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 103343
                    if len(subjects507) >= 1:
                        tmp510 = subjects507.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp510)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 103344
                            if len(subjects507) == 0:
                                pass
                                # State 103345
                                if len(subjects) == 0:
                                    pass
                                    # 26: sin(c + x*d)
                        subjects507.appendleft(tmp510)
                if len(subjects507) >= 1 and isinstance(subjects507[0], Mul):
                    tmp512 = subjects507.popleft()
                    associative1 = tmp512
                    associative_type1 = type(tmp512)
                    subjects513 = deque(tmp512._args)
                    matcher = CommutativeMatcher103347.get()
                    tmp514 = subjects513
                    subjects513 = []
                    for s in tmp514:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp514, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 103348
                            if len(subjects507) == 0:
                                pass
                                # State 103349
                                if len(subjects) == 0:
                                    pass
                                    # 26: sin(c + x*d)
                    subjects507.appendleft(tmp512)
            if len(subjects507) >= 1:
                tmp515 = subjects507.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp515)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107934
                    if len(subjects507) == 0:
                        pass
                        # State 107935
                        if len(subjects) == 0:
                            pass
                            # 28: sin(v)
                subjects507.appendleft(tmp515)
            if len(subjects507) >= 1 and isinstance(subjects507[0], Add):
                tmp517 = subjects507.popleft()
                associative1 = tmp517
                associative_type1 = type(tmp517)
                subjects518 = deque(tmp517._args)
                matcher = CommutativeMatcher103351.get()
                tmp519 = subjects518
                subjects518 = []
                for s in tmp519:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp519, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 103357
                        if len(subjects507) == 0:
                            pass
                            # State 103358
                            if len(subjects) == 0:
                                pass
                                # 26: sin(c + x*d)
                subjects507.appendleft(tmp517)
            subjects.appendleft(tmp506)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp520 = subjects.popleft()
            subjects521 = deque(tmp520._args)
            # State 110140
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 110141
                if len(subjects521) >= 1:
                    tmp523 = subjects521.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp523)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 110142
                        if len(subjects521) == 0:
                            pass
                            # State 110143
                            if len(subjects) == 0:
                                pass
                                # 29: asin(x*c)
                    subjects521.appendleft(tmp523)
            if len(subjects521) >= 1 and isinstance(subjects521[0], Mul):
                tmp525 = subjects521.popleft()
                associative1 = tmp525
                associative_type1 = type(tmp525)
                subjects526 = deque(tmp525._args)
                matcher = CommutativeMatcher110145.get()
                tmp527 = subjects526
                subjects526 = []
                for s in tmp527:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp527, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110146
                        if len(subjects521) == 0:
                            pass
                            # State 110147
                            if len(subjects) == 0:
                                pass
                                # 29: asin(x*c)
                subjects521.appendleft(tmp525)
            subjects.appendleft(tmp520)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp528 = subjects.popleft()
            subjects529 = deque(tmp528._args)
            # State 110237
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 110238
                if len(subjects529) >= 1:
                    tmp531 = subjects529.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp531)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 110239
                        if len(subjects529) == 0:
                            pass
                            # State 110240
                            if len(subjects) == 0:
                                pass
                                # 30: acos(x*c)
                    subjects529.appendleft(tmp531)
            if len(subjects529) >= 1 and isinstance(subjects529[0], Mul):
                tmp533 = subjects529.popleft()
                associative1 = tmp533
                associative_type1 = type(tmp533)
                subjects534 = deque(tmp533._args)
                matcher = CommutativeMatcher110242.get()
                tmp535 = subjects534
                subjects534 = []
                for s in tmp535:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp535, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110243
                        if len(subjects529) == 0:
                            pass
                            # State 110244
                            if len(subjects) == 0:
                                pass
                                # 30: acos(x*c)
                subjects529.appendleft(tmp533)
            subjects.appendleft(tmp528)
        if len(subjects) >= 1 and isinstance(subjects[0], cosh):
            tmp536 = subjects.popleft()
            subjects537 = deque(tmp536._args)
            # State 137663
            if len(subjects537) >= 1:
                tmp538 = subjects537.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp538)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137664
                    if len(subjects537) == 0:
                        pass
                        # State 137665
                        if len(subjects) == 0:
                            pass
                            # 31: cosh(v)
                subjects537.appendleft(tmp538)
            subjects.appendleft(tmp536)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp540 = subjects.popleft()
            subjects541 = deque(tmp540._args)
            # State 137670
            if len(subjects541) >= 1:
                tmp542 = subjects541.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp542)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137671
                    if len(subjects541) == 0:
                        pass
                        # State 137672
                        if len(subjects) == 0:
                            pass
                            # 32: sinh(v)
                subjects541.appendleft(tmp542)
            subjects.appendleft(tmp540)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp544 = subjects.popleft()
            subjects545 = deque(tmp544._args)
            # State 139875
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139876
                if len(subjects545) >= 1:
                    tmp547 = subjects545.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp547)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139877
                        if len(subjects545) == 0:
                            pass
                            # State 139878
                            if len(subjects) == 0:
                                pass
                                # 33: asinh(x*c)
                    subjects545.appendleft(tmp547)
            if len(subjects545) >= 1 and isinstance(subjects545[0], Mul):
                tmp549 = subjects545.popleft()
                associative1 = tmp549
                associative_type1 = type(tmp549)
                subjects550 = deque(tmp549._args)
                matcher = CommutativeMatcher139880.get()
                tmp551 = subjects550
                subjects550 = []
                for s in tmp551:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp551, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 139881
                        if len(subjects545) == 0:
                            pass
                            # State 139882
                            if len(subjects) == 0:
                                pass
                                # 33: asinh(x*c)
                subjects545.appendleft(tmp549)
            subjects.appendleft(tmp544)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp552 = subjects.popleft()
            subjects553 = deque(tmp552._args)
            # State 139972
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139973
                if len(subjects553) >= 1:
                    tmp555 = subjects553.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp555)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139974
                        if len(subjects553) == 0:
                            pass
                            # State 139975
                            if len(subjects) == 0:
                                pass
                                # 34: acosh(x*c)
                    subjects553.appendleft(tmp555)
            if len(subjects553) >= 1 and isinstance(subjects553[0], Mul):
                tmp557 = subjects553.popleft()
                associative1 = tmp557
                associative_type1 = type(tmp557)
                subjects558 = deque(tmp557._args)
                matcher = CommutativeMatcher139977.get()
                tmp559 = subjects558
                subjects558 = []
                for s in tmp559:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp559, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 139978
                        if len(subjects553) == 0:
                            pass
                            # State 139979
                            if len(subjects) == 0:
                                pass
                                # 34: acosh(x*c)
                subjects553.appendleft(tmp557)
            subjects.appendleft(tmp552)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
