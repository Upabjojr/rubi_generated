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

class CommutativeMatcher2208(CommutativeMatcher):
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
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({13: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({14: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({15: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({16: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({17: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({18: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({19: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({20: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({21: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({22: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({23: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher2208._instance is None:
            CommutativeMatcher2208._instance = CommutativeMatcher2208()
        return CommutativeMatcher2208._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2207
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2209
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2210
                    if len(subjects) == 0:
                        pass
                        # 0: x**n
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2404
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2405
                    if len(subjects) == 0:
                        pass
                        # 1: x**n
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2802
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2803
                    if len(subjects) == 0:
                        pass
                        # 4: x**r
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 54169
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp11 = subjects.popleft()
                subjects12 = deque(tmp11._args)
                # State 54170
                if len(subjects12) >= 1:
                    tmp13 = subjects12.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', tmp13)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 54171
                        if len(subjects12) == 0:
                            pass
                            # State 54172
                            if len(subjects) == 0:
                                pass
                                # 7: log(v)**n
                    subjects12.appendleft(tmp13)
                subjects.appendleft(tmp11)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp15 = subjects.popleft()
            subjects16 = deque(tmp15._args)
            # State 2211
            if len(subjects16) >= 1:
                tmp17 = subjects16.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2212
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2213
                        if len(subjects16) == 0:
                            pass
                            # State 2214
                            if len(subjects) == 0:
                                pass
                                # 0: x**n
                    if len(subjects16) >= 1:
                        tmp20 = subjects16.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp20)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2213
                            if len(subjects16) == 0:
                                pass
                                # State 2214
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects16.appendleft(tmp20)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2406
                        if len(subjects16) == 0:
                            pass
                            # State 2407
                            if len(subjects) == 0:
                                pass
                                # 1: x**n
                    if len(subjects16) >= 1:
                        tmp23 = subjects16.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp23)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2406
                            if len(subjects16) == 0:
                                pass
                                # State 2407
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                        subjects16.appendleft(tmp23)
                    if len(subjects16) >= 1:
                        tmp25 = subjects16.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp25)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2748
                            if len(subjects16) == 0:
                                pass
                                # State 2749
                                if len(subjects) == 0:
                                    pass
                                    # 3: x**j
                        subjects16.appendleft(tmp25)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2804
                        if len(subjects16) == 0:
                            pass
                            # State 2805
                            if len(subjects) == 0:
                                pass
                                # 4: x**r
                    if len(subjects16) >= 1:
                        tmp28 = subjects16.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_2', tmp28)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2804
                            if len(subjects16) == 0:
                                pass
                                # State 2805
                                if len(subjects) == 0:
                                    pass
                                    # 4: x**r
                        subjects16.appendleft(tmp28)
                    if len(subjects16) >= 1 and subjects16[0] == 2:
                        tmp30 = subjects16.popleft()
                        # State 2705
                        if len(subjects16) == 0:
                            pass
                            # State 2706
                            if len(subjects) == 0:
                                pass
                                # 2: x**2
                        subjects16.appendleft(tmp30)
                subjects16.appendleft(tmp17)
            if len(subjects16) >= 1 and isinstance(subjects16[0], log):
                tmp31 = subjects16.popleft()
                subjects32 = deque(tmp31._args)
                # State 54173
                if len(subjects32) >= 1:
                    tmp33 = subjects32.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp33)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 54174
                        if len(subjects32) == 0:
                            pass
                            # State 54175
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i2.2.1.3', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 54176
                                if len(subjects16) == 0:
                                    pass
                                    # State 54177
                                    if len(subjects) == 0:
                                        pass
                                        # 7: log(v)**n
                            if len(subjects16) >= 1:
                                tmp36 = subjects16.popleft()
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.3', tmp36)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54176
                                    if len(subjects16) == 0:
                                        pass
                                        # State 54177
                                        if len(subjects) == 0:
                                            pass
                                            # 7: log(v)**n
                                subjects16.appendleft(tmp36)
                    subjects32.appendleft(tmp33)
                subjects16.appendleft(tmp31)
            if len(subjects16) >= 1 and isinstance(subjects16[0], cos):
                tmp38 = subjects16.popleft()
                subjects39 = deque(tmp38._args)
                # State 101695
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 101696
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101697
                        if len(subjects39) >= 1:
                            tmp42 = subjects39.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp42)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 101698
                                if len(subjects39) == 0:
                                    pass
                                    # State 101699
                                    if len(subjects16) >= 1 and subjects16[0] == 2:
                                        tmp44 = subjects16.popleft()
                                        # State 101700
                                        if len(subjects16) == 0:
                                            pass
                                            # State 101701
                                            if len(subjects) == 0:
                                                pass
                                                # 8: cos(e + x*f)**2
                                        subjects16.appendleft(tmp44)
                                    if len(subjects16) >= 1 and subjects16[0] == -2:
                                        tmp45 = subjects16.popleft()
                                        # State 101921
                                        if len(subjects16) == 0:
                                            pass
                                            # State 101922
                                            if len(subjects) == 0:
                                                pass
                                                # 10: cos(e + x*f)**(-2)
                                        subjects16.appendleft(tmp45)
                            subjects39.appendleft(tmp42)
                    if len(subjects39) >= 1 and isinstance(subjects39[0], Mul):
                        tmp46 = subjects39.popleft()
                        associative1 = tmp46
                        associative_type1 = type(tmp46)
                        subjects47 = deque(tmp46._args)
                        matcher = CommutativeMatcher101703.get()
                        tmp48 = subjects47
                        subjects47 = []
                        for s in tmp48:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp48, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 101704
                                if len(subjects39) == 0:
                                    pass
                                    # State 101705
                                    if len(subjects16) >= 1 and subjects16[0] == 2:
                                        tmp49 = subjects16.popleft()
                                        # State 101706
                                        if len(subjects16) == 0:
                                            pass
                                            # State 101707
                                            if len(subjects) == 0:
                                                pass
                                                # 8: cos(e + x*f)**2
                                        subjects16.appendleft(tmp49)
                                    if len(subjects16) >= 1 and subjects16[0] == -2:
                                        tmp50 = subjects16.popleft()
                                        # State 101923
                                        if len(subjects16) == 0:
                                            pass
                                            # State 101924
                                            if len(subjects) == 0:
                                                pass
                                                # 10: cos(e + x*f)**(-2)
                                        subjects16.appendleft(tmp50)
                        subjects39.appendleft(tmp46)
                if len(subjects39) >= 1 and isinstance(subjects39[0], Add):
                    tmp51 = subjects39.popleft()
                    associative1 = tmp51
                    associative_type1 = type(tmp51)
                    subjects52 = deque(tmp51._args)
                    matcher = CommutativeMatcher101709.get()
                    tmp53 = subjects52
                    subjects52 = []
                    for s in tmp53:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp53, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 101715
                            if len(subjects39) == 0:
                                pass
                                # State 101716
                                if len(subjects16) >= 1 and subjects16[0] == 2:
                                    tmp54 = subjects16.popleft()
                                    # State 101717
                                    if len(subjects16) == 0:
                                        pass
                                        # State 101718
                                        if len(subjects) == 0:
                                            pass
                                            # 8: cos(e + x*f)**2
                                    subjects16.appendleft(tmp54)
                                if len(subjects16) >= 1 and subjects16[0] == -2:
                                    tmp55 = subjects16.popleft()
                                    # State 101925
                                    if len(subjects16) == 0:
                                        pass
                                        # State 101926
                                        if len(subjects) == 0:
                                            pass
                                            # 10: cos(e + x*f)**(-2)
                                    subjects16.appendleft(tmp55)
                    subjects39.appendleft(tmp51)
                subjects16.appendleft(tmp38)
            if len(subjects16) >= 1 and isinstance(subjects16[0], sin):
                tmp56 = subjects16.popleft()
                subjects57 = deque(tmp56._args)
                # State 101744
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 101745
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101746
                        if len(subjects57) >= 1:
                            tmp60 = subjects57.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp60)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 101747
                                if len(subjects57) == 0:
                                    pass
                                    # State 101748
                                    if len(subjects16) >= 1 and subjects16[0] == 2:
                                        tmp62 = subjects16.popleft()
                                        # State 101749
                                        if len(subjects16) == 0:
                                            pass
                                            # State 101750
                                            if len(subjects) == 0:
                                                pass
                                                # 9: sin(e + x*f)**2
                                        subjects16.appendleft(tmp62)
                                    if len(subjects16) >= 1 and subjects16[0] == -2:
                                        tmp63 = subjects16.popleft()
                                        # State 102118
                                        if len(subjects16) == 0:
                                            pass
                                            # State 102119
                                            if len(subjects) == 0:
                                                pass
                                                # 12: sin(e + x*f)**(-2)
                                        subjects16.appendleft(tmp63)
                            subjects57.appendleft(tmp60)
                    if len(subjects57) >= 1 and isinstance(subjects57[0], Mul):
                        tmp64 = subjects57.popleft()
                        associative1 = tmp64
                        associative_type1 = type(tmp64)
                        subjects65 = deque(tmp64._args)
                        matcher = CommutativeMatcher101752.get()
                        tmp66 = subjects65
                        subjects65 = []
                        for s in tmp66:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp66, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 101753
                                if len(subjects57) == 0:
                                    pass
                                    # State 101754
                                    if len(subjects16) >= 1 and subjects16[0] == 2:
                                        tmp67 = subjects16.popleft()
                                        # State 101755
                                        if len(subjects16) == 0:
                                            pass
                                            # State 101756
                                            if len(subjects) == 0:
                                                pass
                                                # 9: sin(e + x*f)**2
                                        subjects16.appendleft(tmp67)
                                    if len(subjects16) >= 1 and subjects16[0] == -2:
                                        tmp68 = subjects16.popleft()
                                        # State 102120
                                        if len(subjects16) == 0:
                                            pass
                                            # State 102121
                                            if len(subjects) == 0:
                                                pass
                                                # 12: sin(e + x*f)**(-2)
                                        subjects16.appendleft(tmp68)
                        subjects57.appendleft(tmp64)
                if len(subjects57) >= 1 and isinstance(subjects57[0], Add):
                    tmp69 = subjects57.popleft()
                    associative1 = tmp69
                    associative_type1 = type(tmp69)
                    subjects70 = deque(tmp69._args)
                    matcher = CommutativeMatcher101758.get()
                    tmp71 = subjects70
                    subjects70 = []
                    for s in tmp71:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp71, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 101764
                            if len(subjects57) == 0:
                                pass
                                # State 101765
                                if len(subjects16) >= 1 and subjects16[0] == 2:
                                    tmp72 = subjects16.popleft()
                                    # State 101766
                                    if len(subjects16) == 0:
                                        pass
                                        # State 101767
                                        if len(subjects) == 0:
                                            pass
                                            # 9: sin(e + x*f)**2
                                    subjects16.appendleft(tmp72)
                                if len(subjects16) >= 1 and subjects16[0] == -2:
                                    tmp73 = subjects16.popleft()
                                    # State 102122
                                    if len(subjects16) == 0:
                                        pass
                                        # State 102123
                                        if len(subjects) == 0:
                                            pass
                                            # 12: sin(e + x*f)**(-2)
                                    subjects16.appendleft(tmp73)
                    subjects57.appendleft(tmp69)
                subjects16.appendleft(tmp56)
            if len(subjects16) >= 1 and isinstance(subjects16[0], tan):
                tmp74 = subjects16.popleft()
                subjects75 = deque(tmp74._args)
                # State 101952
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 101953
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101954
                        if len(subjects75) >= 1:
                            tmp78 = subjects75.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp78)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 101955
                                if len(subjects75) == 0:
                                    pass
                                    # State 101956
                                    if len(subjects16) >= 1 and subjects16[0] == 2:
                                        tmp80 = subjects16.popleft()
                                        # State 101957
                                        if len(subjects16) == 0:
                                            pass
                                            # State 101958
                                            if len(subjects) == 0:
                                                pass
                                                # 11: tan(e + x*f)**2
                                        subjects16.appendleft(tmp80)
                                    if len(subjects16) >= 1 and subjects16[0] == -2:
                                        tmp81 = subjects16.popleft()
                                        # State 102131
                                        if len(subjects16) == 0:
                                            pass
                                            # State 102132
                                            if len(subjects) == 0:
                                                pass
                                                # 13: tan(e + x*f)**(-2)
                                        subjects16.appendleft(tmp81)
                            subjects75.appendleft(tmp78)
                    if len(subjects75) >= 1 and isinstance(subjects75[0], Mul):
                        tmp82 = subjects75.popleft()
                        associative1 = tmp82
                        associative_type1 = type(tmp82)
                        subjects83 = deque(tmp82._args)
                        matcher = CommutativeMatcher101960.get()
                        tmp84 = subjects83
                        subjects83 = []
                        for s in tmp84:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp84, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 101961
                                if len(subjects75) == 0:
                                    pass
                                    # State 101962
                                    if len(subjects16) >= 1 and subjects16[0] == 2:
                                        tmp85 = subjects16.popleft()
                                        # State 101963
                                        if len(subjects16) == 0:
                                            pass
                                            # State 101964
                                            if len(subjects) == 0:
                                                pass
                                                # 11: tan(e + x*f)**2
                                        subjects16.appendleft(tmp85)
                                    if len(subjects16) >= 1 and subjects16[0] == -2:
                                        tmp86 = subjects16.popleft()
                                        # State 102133
                                        if len(subjects16) == 0:
                                            pass
                                            # State 102134
                                            if len(subjects) == 0:
                                                pass
                                                # 13: tan(e + x*f)**(-2)
                                        subjects16.appendleft(tmp86)
                        subjects75.appendleft(tmp82)
                if len(subjects75) >= 1 and isinstance(subjects75[0], Add):
                    tmp87 = subjects75.popleft()
                    associative1 = tmp87
                    associative_type1 = type(tmp87)
                    subjects88 = deque(tmp87._args)
                    matcher = CommutativeMatcher101966.get()
                    tmp89 = subjects88
                    subjects88 = []
                    for s in tmp89:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp89, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 101972
                            if len(subjects75) == 0:
                                pass
                                # State 101973
                                if len(subjects16) >= 1 and subjects16[0] == 2:
                                    tmp90 = subjects16.popleft()
                                    # State 101974
                                    if len(subjects16) == 0:
                                        pass
                                        # State 101975
                                        if len(subjects) == 0:
                                            pass
                                            # 11: tan(e + x*f)**2
                                    subjects16.appendleft(tmp90)
                                if len(subjects16) >= 1 and subjects16[0] == -2:
                                    tmp91 = subjects16.popleft()
                                    # State 102135
                                    if len(subjects16) == 0:
                                        pass
                                        # State 102136
                                        if len(subjects) == 0:
                                            pass
                                            # 13: tan(e + x*f)**(-2)
                                    subjects16.appendleft(tmp91)
                    subjects75.appendleft(tmp87)
                subjects16.appendleft(tmp74)
            subjects.appendleft(tmp15)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp92 = subjects.popleft()
            subjects93 = deque(tmp92._args)
            # State 41652
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 41653
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 41654
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 41655
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 41656
                            if len(subjects93) >= 1 and isinstance(subjects93[0], Add):
                                tmp98 = subjects93.popleft()
                                associative1 = tmp98
                                associative_type1 = type(tmp98)
                                subjects99 = deque(tmp98._args)
                                matcher = CommutativeMatcher41658.get()
                                tmp100 = subjects99
                                subjects99 = []
                                for s in tmp100:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp100, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 41674
                                        if len(subjects93) == 0:
                                            pass
                                            # State 41675
                                            if len(subjects) == 0:
                                                pass
                                                # 5: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                subjects93.appendleft(tmp98)
                            if len(subjects93) >= 1:
                                tmp101 = subjects93.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.1', tmp101)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45071
                                    if len(subjects93) == 0:
                                        pass
                                        # State 45072
                                        if len(subjects) == 0:
                                            pass
                                            # 6: log(c*(d*v**p)**q)
                                subjects93.appendleft(tmp101)
                        if len(subjects93) >= 1 and isinstance(subjects93[0], Pow):
                            tmp103 = subjects93.popleft()
                            subjects104 = deque(tmp103._args)
                            # State 41676
                            if len(subjects104) >= 1 and isinstance(subjects104[0], Add):
                                tmp105 = subjects104.popleft()
                                associative1 = tmp105
                                associative_type1 = type(tmp105)
                                subjects106 = deque(tmp105._args)
                                matcher = CommutativeMatcher41678.get()
                                tmp107 = subjects106
                                subjects106 = []
                                for s in tmp107:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp107, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 41694
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 41695
                                            if len(subjects104) == 0:
                                                pass
                                                # State 41696
                                                if len(subjects93) == 0:
                                                    pass
                                                    # State 41697
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                        if len(subjects104) >= 1:
                                            tmp109 = []
                                            tmp109.append(subjects104.popleft())
                                            while True:
                                                if len(tmp109) > 1:
                                                    tmp110 = create_operation_expression(associative1, tmp109)
                                                elif len(tmp109) == 1:
                                                    tmp110 = tmp109[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp110)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 41695
                                                    if len(subjects104) == 0:
                                                        pass
                                                        # State 41696
                                                        if len(subjects93) == 0:
                                                            pass
                                                            # State 41697
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                if len(subjects104) == 0:
                                                    break
                                                tmp109.append(subjects104.popleft())
                                            subjects104.extendleft(reversed(tmp109))
                                subjects104.appendleft(tmp105)
                            if len(subjects104) >= 1:
                                tmp112 = subjects104.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.1', tmp112)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45073
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45074
                                        if len(subjects104) == 0:
                                            pass
                                            # State 45075
                                            if len(subjects93) == 0:
                                                pass
                                                # State 45076
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: log(c*(d*v**p)**q)
                                    if len(subjects104) >= 1:
                                        tmp115 = subjects104.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp115)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45074
                                            if len(subjects104) == 0:
                                                pass
                                                # State 45075
                                                if len(subjects93) == 0:
                                                    pass
                                                    # State 45076
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: log(c*(d*v**p)**q)
                                        subjects104.appendleft(tmp115)
                                subjects104.appendleft(tmp112)
                            subjects93.appendleft(tmp103)
                    if len(subjects93) >= 1 and isinstance(subjects93[0], Mul):
                        tmp117 = subjects93.popleft()
                        associative1 = tmp117
                        associative_type1 = type(tmp117)
                        subjects118 = deque(tmp117._args)
                        matcher = CommutativeMatcher41699.get()
                        tmp119 = subjects118
                        subjects118 = []
                        for s in tmp119:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp119, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 41740
                                if len(subjects93) == 0:
                                    pass
                                    # State 41741
                                    if len(subjects) == 0:
                                        pass
                                        # 5: log(c*(d*(e + f*x + g*x**2)**p)**q)
                            if pattern_index == 1:
                                pass
                                # State 45081
                                if len(subjects93) == 0:
                                    pass
                                    # State 45082
                                    if len(subjects) == 0:
                                        pass
                                        # 6: log(c*(d*v**p)**q)
                        subjects93.appendleft(tmp117)
                if len(subjects93) >= 1 and isinstance(subjects93[0], Pow):
                    tmp120 = subjects93.popleft()
                    subjects121 = deque(tmp120._args)
                    # State 41742
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 41743
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 41744
                            if len(subjects121) >= 1 and isinstance(subjects121[0], Add):
                                tmp124 = subjects121.popleft()
                                associative1 = tmp124
                                associative_type1 = type(tmp124)
                                subjects125 = deque(tmp124._args)
                                matcher = CommutativeMatcher41746.get()
                                tmp126 = subjects125
                                subjects125 = []
                                for s in tmp126:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp126, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 41762
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 41763
                                            if len(subjects121) == 0:
                                                pass
                                                # State 41764
                                                if len(subjects93) == 0:
                                                    pass
                                                    # State 41765
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                        if len(subjects121) >= 1:
                                            tmp128 = []
                                            tmp128.append(subjects121.popleft())
                                            while True:
                                                if len(tmp128) > 1:
                                                    tmp129 = create_operation_expression(associative1, tmp128)
                                                elif len(tmp128) == 1:
                                                    tmp129 = tmp128[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp129)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 41763
                                                    if len(subjects121) == 0:
                                                        pass
                                                        # State 41764
                                                        if len(subjects93) == 0:
                                                            pass
                                                            # State 41765
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                if len(subjects121) == 0:
                                                    break
                                                tmp128.append(subjects121.popleft())
                                            subjects121.extendleft(reversed(tmp128))
                                subjects121.appendleft(tmp124)
                            if len(subjects121) >= 1:
                                tmp131 = subjects121.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.1', tmp131)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45083
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45084
                                        if len(subjects121) == 0:
                                            pass
                                            # State 45085
                                            if len(subjects93) == 0:
                                                pass
                                                # State 45086
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: log(c*(d*v**p)**q)
                                    if len(subjects121) >= 1:
                                        tmp134 = subjects121.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', tmp134)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45084
                                            if len(subjects121) == 0:
                                                pass
                                                # State 45085
                                                if len(subjects93) == 0:
                                                    pass
                                                    # State 45086
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: log(c*(d*v**p)**q)
                                        subjects121.appendleft(tmp134)
                                subjects121.appendleft(tmp131)
                        if len(subjects121) >= 1 and isinstance(subjects121[0], Pow):
                            tmp136 = subjects121.popleft()
                            subjects137 = deque(tmp136._args)
                            # State 41766
                            if len(subjects137) >= 1 and isinstance(subjects137[0], Add):
                                tmp138 = subjects137.popleft()
                                associative1 = tmp138
                                associative_type1 = type(tmp138)
                                subjects139 = deque(tmp138._args)
                                matcher = CommutativeMatcher41768.get()
                                tmp140 = subjects139
                                subjects139 = []
                                for s in tmp140:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp140, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 41784
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 41785
                                            if len(subjects137) == 0:
                                                pass
                                                # State 41786
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 41787
                                                    if len(subjects121) == 0:
                                                        pass
                                                        # State 41788
                                                        if len(subjects93) == 0:
                                                            pass
                                                            # State 41789
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                if len(subjects121) >= 1:
                                                    tmp143 = subjects121.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp143)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 41787
                                                        if len(subjects121) == 0:
                                                            pass
                                                            # State 41788
                                                            if len(subjects93) == 0:
                                                                pass
                                                                # State 41789
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                    subjects121.appendleft(tmp143)
                                        if len(subjects137) >= 1:
                                            tmp145 = []
                                            tmp145.append(subjects137.popleft())
                                            while True:
                                                if len(tmp145) > 1:
                                                    tmp146 = create_operation_expression(associative1, tmp145)
                                                elif len(tmp145) == 1:
                                                    tmp146 = tmp145[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp146)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 41785
                                                    if len(subjects137) == 0:
                                                        pass
                                                        # State 41786
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 41787
                                                            if len(subjects121) == 0:
                                                                pass
                                                                # State 41788
                                                                if len(subjects93) == 0:
                                                                    pass
                                                                    # State 41789
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 5: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                        if len(subjects121) >= 1:
                                                            tmp149 = subjects121.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp149)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 41787
                                                                if len(subjects121) == 0:
                                                                    pass
                                                                    # State 41788
                                                                    if len(subjects93) == 0:
                                                                        pass
                                                                        # State 41789
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                                            subjects121.appendleft(tmp149)
                                                if len(subjects137) == 0:
                                                    break
                                                tmp145.append(subjects137.popleft())
                                            subjects137.extendleft(reversed(tmp145))
                                subjects137.appendleft(tmp138)
                            if len(subjects137) >= 1:
                                tmp151 = subjects137.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.1', tmp151)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45087
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45088
                                        if len(subjects137) == 0:
                                            pass
                                            # State 45089
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45090
                                                if len(subjects121) == 0:
                                                    pass
                                                    # State 45091
                                                    if len(subjects93) == 0:
                                                        pass
                                                        # State 45092
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: log(c*(d*v**p)**q)
                                            if len(subjects121) >= 1:
                                                tmp155 = subjects121.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp155)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 45090
                                                    if len(subjects121) == 0:
                                                        pass
                                                        # State 45091
                                                        if len(subjects93) == 0:
                                                            pass
                                                            # State 45092
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: log(c*(d*v**p)**q)
                                                subjects121.appendleft(tmp155)
                                    if len(subjects137) >= 1:
                                        tmp157 = subjects137.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp157)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45088
                                            if len(subjects137) == 0:
                                                pass
                                                # State 45089
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 45090
                                                    if len(subjects121) == 0:
                                                        pass
                                                        # State 45091
                                                        if len(subjects93) == 0:
                                                            pass
                                                            # State 45092
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: log(c*(d*v**p)**q)
                                                if len(subjects121) >= 1:
                                                    tmp160 = subjects121.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp160)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 45090
                                                        if len(subjects121) == 0:
                                                            pass
                                                            # State 45091
                                                            if len(subjects93) == 0:
                                                                pass
                                                                # State 45092
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: log(c*(d*v**p)**q)
                                                    subjects121.appendleft(tmp160)
                                        subjects137.appendleft(tmp157)
                                subjects137.appendleft(tmp151)
                            subjects121.appendleft(tmp136)
                    if len(subjects121) >= 1 and isinstance(subjects121[0], Mul):
                        tmp162 = subjects121.popleft()
                        associative1 = tmp162
                        associative_type1 = type(tmp162)
                        subjects163 = deque(tmp162._args)
                        matcher = CommutativeMatcher41791.get()
                        tmp164 = subjects163
                        subjects163 = []
                        for s in tmp164:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp164, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 41832
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 41833
                                    if len(subjects121) == 0:
                                        pass
                                        # State 41834
                                        if len(subjects93) == 0:
                                            pass
                                            # State 41835
                                            if len(subjects) == 0:
                                                pass
                                                # 5: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                if len(subjects121) >= 1:
                                    tmp166 = []
                                    tmp166.append(subjects121.popleft())
                                    while True:
                                        if len(tmp166) > 1:
                                            tmp167 = create_operation_expression(associative1, tmp166)
                                        elif len(tmp166) == 1:
                                            tmp167 = tmp166[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp167)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 41833
                                            if len(subjects121) == 0:
                                                pass
                                                # State 41834
                                                if len(subjects93) == 0:
                                                    pass
                                                    # State 41835
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: log(c*(d*(e + f*x + g*x**2)**p)**q)
                                        if len(subjects121) == 0:
                                            break
                                        tmp166.append(subjects121.popleft())
                                    subjects121.extendleft(reversed(tmp166))
                            if pattern_index == 1:
                                pass
                                # State 45097
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45098
                                    if len(subjects121) == 0:
                                        pass
                                        # State 45099
                                        if len(subjects93) == 0:
                                            pass
                                            # State 45100
                                            if len(subjects) == 0:
                                                pass
                                                # 6: log(c*(d*v**p)**q)
                                if len(subjects121) >= 1:
                                    tmp170 = []
                                    tmp170.append(subjects121.popleft())
                                    while True:
                                        if len(tmp170) > 1:
                                            tmp171 = create_operation_expression(associative1, tmp170)
                                        elif len(tmp170) == 1:
                                            tmp171 = tmp170[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp171)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45098
                                            if len(subjects121) == 0:
                                                pass
                                                # State 45099
                                                if len(subjects93) == 0:
                                                    pass
                                                    # State 45100
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: log(c*(d*v**p)**q)
                                        if len(subjects121) == 0:
                                            break
                                        tmp170.append(subjects121.popleft())
                                    subjects121.extendleft(reversed(tmp170))
                        subjects121.appendleft(tmp162)
                    subjects93.appendleft(tmp120)
            if len(subjects93) >= 1 and isinstance(subjects93[0], Mul):
                tmp173 = subjects93.popleft()
                associative1 = tmp173
                associative_type1 = type(tmp173)
                subjects174 = deque(tmp173._args)
                matcher = CommutativeMatcher41837.get()
                tmp175 = subjects174
                subjects174 = []
                for s in tmp175:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp175, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 42014
                        if len(subjects93) == 0:
                            pass
                            # State 42015
                            if len(subjects) == 0:
                                pass
                                # 5: log(c*(d*(e + f*x + g*x**2)**p)**q)
                    if pattern_index == 1:
                        pass
                        # State 45125
                        if len(subjects93) == 0:
                            pass
                            # State 45126
                            if len(subjects) == 0:
                                pass
                                # 6: log(c*(d*v**p)**q)
                subjects93.appendleft(tmp173)
            subjects.appendleft(tmp92)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp176 = subjects.popleft()
            subjects177 = deque(tmp176._args)
            # State 103227
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 103228
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 103229
                    if len(subjects177) >= 1:
                        tmp180 = subjects177.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp180)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 103230
                            if len(subjects177) == 0:
                                pass
                                # State 103231
                                if len(subjects) == 0:
                                    pass
                                    # 14: cos(c + x*d)
                        subjects177.appendleft(tmp180)
                if len(subjects177) >= 1 and isinstance(subjects177[0], Mul):
                    tmp182 = subjects177.popleft()
                    associative1 = tmp182
                    associative_type1 = type(tmp182)
                    subjects183 = deque(tmp182._args)
                    matcher = CommutativeMatcher103233.get()
                    tmp184 = subjects183
                    subjects183 = []
                    for s in tmp184:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp184, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 103234
                            if len(subjects177) == 0:
                                pass
                                # State 103235
                                if len(subjects) == 0:
                                    pass
                                    # 14: cos(c + x*d)
                    subjects177.appendleft(tmp182)
            if len(subjects177) >= 1:
                tmp185 = subjects177.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp185)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107916
                    if len(subjects177) == 0:
                        pass
                        # State 107917
                        if len(subjects) == 0:
                            pass
                            # 16: cos(v)
                subjects177.appendleft(tmp185)
            if len(subjects177) >= 1 and isinstance(subjects177[0], Add):
                tmp187 = subjects177.popleft()
                associative1 = tmp187
                associative_type1 = type(tmp187)
                subjects188 = deque(tmp187._args)
                matcher = CommutativeMatcher103237.get()
                tmp189 = subjects188
                subjects188 = []
                for s in tmp189:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp189, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 103243
                        if len(subjects177) == 0:
                            pass
                            # State 103244
                            if len(subjects) == 0:
                                pass
                                # 14: cos(c + x*d)
                subjects177.appendleft(tmp187)
            subjects.appendleft(tmp176)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp190 = subjects.popleft()
            subjects191 = deque(tmp190._args)
            # State 103264
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 103265
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 103266
                    if len(subjects191) >= 1:
                        tmp194 = subjects191.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp194)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 103267
                            if len(subjects191) == 0:
                                pass
                                # State 103268
                                if len(subjects) == 0:
                                    pass
                                    # 15: sin(c + x*d)
                        subjects191.appendleft(tmp194)
                if len(subjects191) >= 1 and isinstance(subjects191[0], Mul):
                    tmp196 = subjects191.popleft()
                    associative1 = tmp196
                    associative_type1 = type(tmp196)
                    subjects197 = deque(tmp196._args)
                    matcher = CommutativeMatcher103270.get()
                    tmp198 = subjects197
                    subjects197 = []
                    for s in tmp198:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp198, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 103271
                            if len(subjects191) == 0:
                                pass
                                # State 103272
                                if len(subjects) == 0:
                                    pass
                                    # 15: sin(c + x*d)
                    subjects191.appendleft(tmp196)
            if len(subjects191) >= 1:
                tmp199 = subjects191.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp199)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107921
                    if len(subjects191) == 0:
                        pass
                        # State 107922
                        if len(subjects) == 0:
                            pass
                            # 17: sin(v)
                subjects191.appendleft(tmp199)
            if len(subjects191) >= 1 and isinstance(subjects191[0], Add):
                tmp201 = subjects191.popleft()
                associative1 = tmp201
                associative_type1 = type(tmp201)
                subjects202 = deque(tmp201._args)
                matcher = CommutativeMatcher103274.get()
                tmp203 = subjects202
                subjects202 = []
                for s in tmp203:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp203, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 103280
                        if len(subjects191) == 0:
                            pass
                            # State 103281
                            if len(subjects) == 0:
                                pass
                                # 15: sin(c + x*d)
                subjects191.appendleft(tmp201)
            subjects.appendleft(tmp190)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp204 = subjects.popleft()
            subjects205 = deque(tmp204._args)
            # State 110091
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 110092
                if len(subjects205) >= 1:
                    tmp207 = subjects205.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp207)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 110093
                        if len(subjects205) == 0:
                            pass
                            # State 110094
                            if len(subjects) == 0:
                                pass
                                # 18: asin(x*c)
                    subjects205.appendleft(tmp207)
            if len(subjects205) >= 1 and isinstance(subjects205[0], Mul):
                tmp209 = subjects205.popleft()
                associative1 = tmp209
                associative_type1 = type(tmp209)
                subjects210 = deque(tmp209._args)
                matcher = CommutativeMatcher110096.get()
                tmp211 = subjects210
                subjects210 = []
                for s in tmp211:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp211, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110097
                        if len(subjects205) == 0:
                            pass
                            # State 110098
                            if len(subjects) == 0:
                                pass
                                # 18: asin(x*c)
                subjects205.appendleft(tmp209)
            subjects.appendleft(tmp204)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp212 = subjects.popleft()
            subjects213 = deque(tmp212._args)
            # State 110188
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 110189
                if len(subjects213) >= 1:
                    tmp215 = subjects213.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp215)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 110190
                        if len(subjects213) == 0:
                            pass
                            # State 110191
                            if len(subjects) == 0:
                                pass
                                # 19: acos(x*c)
                    subjects213.appendleft(tmp215)
            if len(subjects213) >= 1 and isinstance(subjects213[0], Mul):
                tmp217 = subjects213.popleft()
                associative1 = tmp217
                associative_type1 = type(tmp217)
                subjects218 = deque(tmp217._args)
                matcher = CommutativeMatcher110193.get()
                tmp219 = subjects218
                subjects218 = []
                for s in tmp219:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp219, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110194
                        if len(subjects213) == 0:
                            pass
                            # State 110195
                            if len(subjects) == 0:
                                pass
                                # 19: acos(x*c)
                subjects213.appendleft(tmp217)
            subjects.appendleft(tmp212)
        if len(subjects) >= 1 and isinstance(subjects[0], cosh):
            tmp220 = subjects.popleft()
            subjects221 = deque(tmp220._args)
            # State 137646
            if len(subjects221) >= 1:
                tmp222 = subjects221.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp222)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137647
                    if len(subjects221) == 0:
                        pass
                        # State 137648
                        if len(subjects) == 0:
                            pass
                            # 20: cosh(v)
                subjects221.appendleft(tmp222)
            subjects.appendleft(tmp220)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp224 = subjects.popleft()
            subjects225 = deque(tmp224._args)
            # State 137653
            if len(subjects225) >= 1:
                tmp226 = subjects225.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp226)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137654
                    if len(subjects225) == 0:
                        pass
                        # State 137655
                        if len(subjects) == 0:
                            pass
                            # 21: sinh(v)
                subjects225.appendleft(tmp226)
            subjects.appendleft(tmp224)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp228 = subjects.popleft()
            subjects229 = deque(tmp228._args)
            # State 139826
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139827
                if len(subjects229) >= 1:
                    tmp231 = subjects229.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp231)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139828
                        if len(subjects229) == 0:
                            pass
                            # State 139829
                            if len(subjects) == 0:
                                pass
                                # 22: asinh(x*c)
                    subjects229.appendleft(tmp231)
            if len(subjects229) >= 1 and isinstance(subjects229[0], Mul):
                tmp233 = subjects229.popleft()
                associative1 = tmp233
                associative_type1 = type(tmp233)
                subjects234 = deque(tmp233._args)
                matcher = CommutativeMatcher139831.get()
                tmp235 = subjects234
                subjects234 = []
                for s in tmp235:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp235, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 139832
                        if len(subjects229) == 0:
                            pass
                            # State 139833
                            if len(subjects) == 0:
                                pass
                                # 22: asinh(x*c)
                subjects229.appendleft(tmp233)
            subjects.appendleft(tmp228)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp236 = subjects.popleft()
            subjects237 = deque(tmp236._args)
            # State 139923
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139924
                if len(subjects237) >= 1:
                    tmp239 = subjects237.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp239)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139925
                        if len(subjects237) == 0:
                            pass
                            # State 139926
                            if len(subjects) == 0:
                                pass
                                # 23: acosh(x*c)
                    subjects237.appendleft(tmp239)
            if len(subjects237) >= 1 and isinstance(subjects237[0], Mul):
                tmp241 = subjects237.popleft()
                associative1 = tmp241
                associative_type1 = type(tmp241)
                subjects242 = deque(tmp241._args)
                matcher = CommutativeMatcher139928.get()
                tmp243 = subjects242
                subjects242 = []
                for s in tmp243:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp243, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 139929
                        if len(subjects237) == 0:
                            pass
                            # State 139930
                            if len(subjects) == 0:
                                pass
                                # 23: acosh(x*c)
                subjects237.appendleft(tmp241)
            subjects.appendleft(tmp236)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
