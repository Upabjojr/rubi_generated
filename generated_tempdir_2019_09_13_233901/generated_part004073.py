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

class CommutativeMatcher3631(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({3: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({4: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({5: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({6: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({7: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({8: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({9: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({10: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({11: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({12: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul)
]),
    16: (16, Multiset({13: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({14: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({15: 1}), [
      (VariableWithCount('i2.1.1.0_1', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher3631._instance is None:
            CommutativeMatcher3631._instance = CommutativeMatcher3631()
        return CommutativeMatcher3631._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3630
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 59795
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 59796
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59797
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 59798
                            if len(subjects2) == 0:
                                pass
                                # State 59799
                                if len(subjects) == 0:
                                    pass
                                    # 0: sin(e + x*f)
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp7 = subjects2.popleft()
                    associative1 = tmp7
                    associative_type1 = type(tmp7)
                    subjects8 = deque(tmp7._args)
                    matcher = CommutativeMatcher59801.get()
                    tmp9 = subjects8
                    subjects8 = []
                    for s in tmp9:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp9, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 59802
                            if len(subjects2) == 0:
                                pass
                                # State 59803
                                if len(subjects) == 0:
                                    pass
                                    # 0: sin(e + x*f)
                    subjects2.appendleft(tmp7)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 65001
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65002
                    if len(subjects2) >= 1:
                        tmp12 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp12)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 65003
                            if len(subjects2) == 0:
                                pass
                                # State 65004
                                if len(subjects) == 0:
                                    pass
                                    # 2: sin(c + x*d)
                        subjects2.appendleft(tmp12)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp14 = subjects2.popleft()
                    associative1 = tmp14
                    associative_type1 = type(tmp14)
                    subjects15 = deque(tmp14._args)
                    matcher = CommutativeMatcher65006.get()
                    tmp16 = subjects15
                    subjects15 = []
                    for s in tmp16:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp16, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 65007
                            if len(subjects2) == 0:
                                pass
                                # State 65008
                                if len(subjects) == 0:
                                    pass
                                    # 2: sin(c + x*d)
                    subjects2.appendleft(tmp14)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp17 = subjects2.popleft()
                associative1 = tmp17
                associative_type1 = type(tmp17)
                subjects18 = deque(tmp17._args)
                matcher = CommutativeMatcher59805.get()
                tmp19 = subjects18
                subjects18 = []
                for s in tmp19:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp19, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 59811
                        if len(subjects2) == 0:
                            pass
                            # State 59812
                            if len(subjects) == 0:
                                pass
                                # 0: sin(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 65012
                        if len(subjects2) == 0:
                            pass
                            # State 65013
                            if len(subjects) == 0:
                                pass
                                # 2: sin(c + x*d)
                subjects2.appendleft(tmp17)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp20 = subjects.popleft()
            subjects21 = deque(tmp20._args)
            # State 59883
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 59884
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59885
                    if len(subjects21) >= 1:
                        tmp24 = subjects21.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.1.0', tmp24)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 59886
                            if len(subjects21) == 0:
                                pass
                                # State 59887
                                if len(subjects) == 0:
                                    pass
                                    # 1: cos(e + x*f)
                        subjects21.appendleft(tmp24)
                if len(subjects21) >= 1 and isinstance(subjects21[0], Mul):
                    tmp26 = subjects21.popleft()
                    associative1 = tmp26
                    associative_type1 = type(tmp26)
                    subjects27 = deque(tmp26._args)
                    matcher = CommutativeMatcher59889.get()
                    tmp28 = subjects27
                    subjects27 = []
                    for s in tmp28:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp28, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 59890
                            if len(subjects21) == 0:
                                pass
                                # State 59891
                                if len(subjects) == 0:
                                    pass
                                    # 1: cos(e + x*f)
                    subjects21.appendleft(tmp26)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 65094
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 65095
                    if len(subjects21) >= 1:
                        tmp31 = subjects21.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp31)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 65096
                            if len(subjects21) == 0:
                                pass
                                # State 65097
                                if len(subjects) == 0:
                                    pass
                                    # 3: cos(c + x*d)
                        subjects21.appendleft(tmp31)
                if len(subjects21) >= 1 and isinstance(subjects21[0], Mul):
                    tmp33 = subjects21.popleft()
                    associative1 = tmp33
                    associative_type1 = type(tmp33)
                    subjects34 = deque(tmp33._args)
                    matcher = CommutativeMatcher65099.get()
                    tmp35 = subjects34
                    subjects34 = []
                    for s in tmp35:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp35, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 65100
                            if len(subjects21) == 0:
                                pass
                                # State 65101
                                if len(subjects) == 0:
                                    pass
                                    # 3: cos(c + x*d)
                    subjects21.appendleft(tmp33)
            if len(subjects21) >= 1 and isinstance(subjects21[0], Add):
                tmp36 = subjects21.popleft()
                associative1 = tmp36
                associative_type1 = type(tmp36)
                subjects37 = deque(tmp36._args)
                matcher = CommutativeMatcher59893.get()
                tmp38 = subjects37
                subjects37 = []
                for s in tmp38:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp38, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 59899
                        if len(subjects21) == 0:
                            pass
                            # State 59900
                            if len(subjects) == 0:
                                pass
                                # 1: cos(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 65105
                        if len(subjects21) == 0:
                            pass
                            # State 65106
                            if len(subjects) == 0:
                                pass
                                # 3: cos(c + x*d)
                subjects21.appendleft(tmp36)
            subjects.appendleft(tmp20)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp39 = subjects.popleft()
            subjects40 = deque(tmp39._args)
            # State 78907
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 78908
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78909
                    if len(subjects40) >= 1:
                        tmp43 = subjects40.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.1.0', tmp43)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 78910
                            if len(subjects40) == 0:
                                pass
                                # State 78911
                                if len(subjects) == 0:
                                    pass
                                    # 4: tan(e + x*f)
                        subjects40.appendleft(tmp43)
                if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                    tmp45 = subjects40.popleft()
                    associative1 = tmp45
                    associative_type1 = type(tmp45)
                    subjects46 = deque(tmp45._args)
                    matcher = CommutativeMatcher78913.get()
                    tmp47 = subjects46
                    subjects46 = []
                    for s in tmp47:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp47, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 78914
                            if len(subjects40) == 0:
                                pass
                                # State 78915
                                if len(subjects) == 0:
                                    pass
                                    # 4: tan(e + x*f)
                    subjects40.appendleft(tmp45)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 81123
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 81124
                    if len(subjects40) >= 1:
                        tmp50 = subjects40.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp50)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 81125
                            if len(subjects40) == 0:
                                pass
                                # State 81126
                                if len(subjects) == 0:
                                    pass
                                    # 6: tan(c + x*d)
                        subjects40.appendleft(tmp50)
                if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                    tmp52 = subjects40.popleft()
                    associative1 = tmp52
                    associative_type1 = type(tmp52)
                    subjects53 = deque(tmp52._args)
                    matcher = CommutativeMatcher81128.get()
                    tmp54 = subjects53
                    subjects53 = []
                    for s in tmp54:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp54, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 81129
                            if len(subjects40) == 0:
                                pass
                                # State 81130
                                if len(subjects) == 0:
                                    pass
                                    # 6: tan(c + x*d)
                    subjects40.appendleft(tmp52)
            if len(subjects40) >= 1 and isinstance(subjects40[0], Add):
                tmp55 = subjects40.popleft()
                associative1 = tmp55
                associative_type1 = type(tmp55)
                subjects56 = deque(tmp55._args)
                matcher = CommutativeMatcher78917.get()
                tmp57 = subjects56
                subjects56 = []
                for s in tmp57:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp57, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 78923
                        if len(subjects40) == 0:
                            pass
                            # State 78924
                            if len(subjects) == 0:
                                pass
                                # 4: tan(e + x*f)
                    if pattern_index == 1:
                        pass
                        # State 81134
                        if len(subjects40) == 0:
                            pass
                            # State 81135
                            if len(subjects) == 0:
                                pass
                                # 6: tan(c + x*d)
                subjects40.appendleft(tmp55)
            subjects.appendleft(tmp39)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp58 = subjects.popleft()
            subjects59 = deque(tmp58._args)
            # State 78955
            if len(subjects59) >= 1 and isinstance(subjects59[0], tan):
                tmp60 = subjects59.popleft()
                subjects61 = deque(tmp60._args)
                # State 78956
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78957
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 78958
                        if len(subjects61) >= 1:
                            tmp64 = subjects61.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.3.1.0', tmp64)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 78959
                                if len(subjects61) == 0:
                                    pass
                                    # State 78960
                                    if len(subjects59) >= 1 and subjects59[0] == -1:
                                        tmp66 = subjects59.popleft()
                                        # State 78961
                                        if len(subjects59) == 0:
                                            pass
                                            # State 78962
                                            if len(subjects) == 0:
                                                pass
                                                # 5: 1/tan(e + x*f)
                                        subjects59.appendleft(tmp66)
                            subjects61.appendleft(tmp64)
                    if len(subjects61) >= 1 and isinstance(subjects61[0], Mul):
                        tmp67 = subjects61.popleft()
                        associative1 = tmp67
                        associative_type1 = type(tmp67)
                        subjects68 = deque(tmp67._args)
                        matcher = CommutativeMatcher78964.get()
                        tmp69 = subjects68
                        subjects68 = []
                        for s in tmp69:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp69, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 78965
                                if len(subjects61) == 0:
                                    pass
                                    # State 78966
                                    if len(subjects59) >= 1 and subjects59[0] == -1:
                                        tmp70 = subjects59.popleft()
                                        # State 78967
                                        if len(subjects59) == 0:
                                            pass
                                            # State 78968
                                            if len(subjects) == 0:
                                                pass
                                                # 5: 1/tan(e + x*f)
                                        subjects59.appendleft(tmp70)
                        subjects61.appendleft(tmp67)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 81174
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 81175
                        if len(subjects61) >= 1:
                            tmp73 = subjects61.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp73)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 81176
                                if len(subjects61) == 0:
                                    pass
                                    # State 81177
                                    if len(subjects59) >= 1 and subjects59[0] == -1:
                                        tmp75 = subjects59.popleft()
                                        # State 81178
                                        if len(subjects59) == 0:
                                            pass
                                            # State 81179
                                            if len(subjects) == 0:
                                                pass
                                                # 7: 1/tan(e + x*f)
                                        subjects59.appendleft(tmp75)
                                    if len(subjects59) >= 1 and subjects59[0] == -2:
                                        tmp76 = subjects59.popleft()
                                        # State 81973
                                        if len(subjects59) == 0:
                                            pass
                                            # State 81974
                                            if len(subjects) == 0:
                                                pass
                                                # 8: tan(e + x*f)**(-2)
                                        subjects59.appendleft(tmp76)
                            subjects61.appendleft(tmp73)
                    if len(subjects61) >= 1 and isinstance(subjects61[0], Mul):
                        tmp77 = subjects61.popleft()
                        associative1 = tmp77
                        associative_type1 = type(tmp77)
                        subjects78 = deque(tmp77._args)
                        matcher = CommutativeMatcher81181.get()
                        tmp79 = subjects78
                        subjects78 = []
                        for s in tmp79:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp79, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 81182
                                if len(subjects61) == 0:
                                    pass
                                    # State 81183
                                    if len(subjects59) >= 1 and subjects59[0] == -1:
                                        tmp80 = subjects59.popleft()
                                        # State 81184
                                        if len(subjects59) == 0:
                                            pass
                                            # State 81185
                                            if len(subjects) == 0:
                                                pass
                                                # 7: 1/tan(e + x*f)
                                        subjects59.appendleft(tmp80)
                                    if len(subjects59) >= 1 and subjects59[0] == -2:
                                        tmp81 = subjects59.popleft()
                                        # State 81975
                                        if len(subjects59) == 0:
                                            pass
                                            # State 81976
                                            if len(subjects) == 0:
                                                pass
                                                # 8: tan(e + x*f)**(-2)
                                        subjects59.appendleft(tmp81)
                        subjects61.appendleft(tmp77)
                if len(subjects61) >= 1 and isinstance(subjects61[0], Add):
                    tmp82 = subjects61.popleft()
                    associative1 = tmp82
                    associative_type1 = type(tmp82)
                    subjects83 = deque(tmp82._args)
                    matcher = CommutativeMatcher78970.get()
                    tmp84 = subjects83
                    subjects83 = []
                    for s in tmp84:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp84, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 78976
                            if len(subjects61) == 0:
                                pass
                                # State 78977
                                if len(subjects59) >= 1 and subjects59[0] == -1:
                                    tmp85 = subjects59.popleft()
                                    # State 78978
                                    if len(subjects59) == 0:
                                        pass
                                        # State 78979
                                        if len(subjects) == 0:
                                            pass
                                            # 5: 1/tan(e + x*f)
                                    subjects59.appendleft(tmp85)
                        if pattern_index == 1:
                            pass
                            # State 81189
                            if len(subjects61) == 0:
                                pass
                                # State 81190
                                if len(subjects59) >= 1 and subjects59[0] == -1:
                                    tmp86 = subjects59.popleft()
                                    # State 81191
                                    if len(subjects59) == 0:
                                        pass
                                        # State 81192
                                        if len(subjects) == 0:
                                            pass
                                            # 7: 1/tan(e + x*f)
                                    subjects59.appendleft(tmp86)
                                if len(subjects59) >= 1 and subjects59[0] == -2:
                                    tmp87 = subjects59.popleft()
                                    # State 81977
                                    if len(subjects59) == 0:
                                        pass
                                        # State 81978
                                        if len(subjects) == 0:
                                            pass
                                            # 8: tan(e + x*f)**(-2)
                                    subjects59.appendleft(tmp87)
                    subjects61.appendleft(tmp82)
                subjects59.appendleft(tmp60)
            if len(subjects59) >= 1 and isinstance(subjects59[0], cos):
                tmp88 = subjects59.popleft()
                subjects89 = deque(tmp88._args)
                # State 93766
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 93767
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 93768
                        if len(subjects89) >= 1:
                            tmp92 = subjects89.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.3.1.0', tmp92)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 93769
                                if len(subjects89) == 0:
                                    pass
                                    # State 93770
                                    if len(subjects59) >= 1 and subjects59[0] == -2:
                                        tmp94 = subjects59.popleft()
                                        # State 93771
                                        if len(subjects59) == 0:
                                            pass
                                            # State 93772
                                            if len(subjects) == 0:
                                                pass
                                                # 9: cos(c + x*d)**(-2)
                                        subjects59.appendleft(tmp94)
                            subjects89.appendleft(tmp92)
                    if len(subjects89) >= 1 and isinstance(subjects89[0], Mul):
                        tmp95 = subjects89.popleft()
                        associative1 = tmp95
                        associative_type1 = type(tmp95)
                        subjects96 = deque(tmp95._args)
                        matcher = CommutativeMatcher93774.get()
                        tmp97 = subjects96
                        subjects96 = []
                        for s in tmp97:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp97, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 93775
                                if len(subjects89) == 0:
                                    pass
                                    # State 93776
                                    if len(subjects59) >= 1 and subjects59[0] == -2:
                                        tmp98 = subjects59.popleft()
                                        # State 93777
                                        if len(subjects59) == 0:
                                            pass
                                            # State 93778
                                            if len(subjects) == 0:
                                                pass
                                                # 9: cos(c + x*d)**(-2)
                                        subjects59.appendleft(tmp98)
                        subjects89.appendleft(tmp95)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 94372
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 94373
                        if len(subjects89) >= 1:
                            tmp101 = subjects89.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp101)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 94374
                                if len(subjects89) == 0:
                                    pass
                                    # State 94375
                                    if len(subjects59) >= 1 and subjects59[0] == -2:
                                        tmp103 = subjects59.popleft()
                                        # State 94376
                                        if len(subjects59) == 0:
                                            pass
                                            # State 94377
                                            if len(subjects) == 0:
                                                pass
                                                # 11: cos(e + x*f)**(-2)
                                        subjects59.appendleft(tmp103)
                            subjects89.appendleft(tmp101)
                    if len(subjects89) >= 1 and isinstance(subjects89[0], Mul):
                        tmp104 = subjects89.popleft()
                        associative1 = tmp104
                        associative_type1 = type(tmp104)
                        subjects105 = deque(tmp104._args)
                        matcher = CommutativeMatcher94379.get()
                        tmp106 = subjects105
                        subjects105 = []
                        for s in tmp106:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp106, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 94380
                                if len(subjects89) == 0:
                                    pass
                                    # State 94381
                                    if len(subjects59) >= 1 and subjects59[0] == -2:
                                        tmp107 = subjects59.popleft()
                                        # State 94382
                                        if len(subjects59) == 0:
                                            pass
                                            # State 94383
                                            if len(subjects) == 0:
                                                pass
                                                # 11: cos(e + x*f)**(-2)
                                        subjects59.appendleft(tmp107)
                        subjects89.appendleft(tmp104)
                if len(subjects89) >= 1 and isinstance(subjects89[0], Add):
                    tmp108 = subjects89.popleft()
                    associative1 = tmp108
                    associative_type1 = type(tmp108)
                    subjects109 = deque(tmp108._args)
                    matcher = CommutativeMatcher93780.get()
                    tmp110 = subjects109
                    subjects109 = []
                    for s in tmp110:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp110, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 93786
                            if len(subjects89) == 0:
                                pass
                                # State 93787
                                if len(subjects59) >= 1 and subjects59[0] == -2:
                                    tmp111 = subjects59.popleft()
                                    # State 93788
                                    if len(subjects59) == 0:
                                        pass
                                        # State 93789
                                        if len(subjects) == 0:
                                            pass
                                            # 9: cos(c + x*d)**(-2)
                                    subjects59.appendleft(tmp111)
                        if pattern_index == 1:
                            pass
                            # State 94387
                            if len(subjects89) == 0:
                                pass
                                # State 94388
                                if len(subjects59) >= 1 and subjects59[0] == -2:
                                    tmp112 = subjects59.popleft()
                                    # State 94389
                                    if len(subjects59) == 0:
                                        pass
                                        # State 94390
                                        if len(subjects) == 0:
                                            pass
                                            # 11: cos(e + x*f)**(-2)
                                    subjects59.appendleft(tmp112)
                    subjects89.appendleft(tmp108)
                subjects59.appendleft(tmp88)
            if len(subjects59) >= 1 and isinstance(subjects59[0], sin):
                tmp113 = subjects59.popleft()
                subjects114 = deque(tmp113._args)
                # State 93826
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 93827
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 93828
                        if len(subjects114) >= 1:
                            tmp117 = subjects114.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.3.1.0', tmp117)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 93829
                                if len(subjects114) == 0:
                                    pass
                                    # State 93830
                                    if len(subjects59) >= 1 and subjects59[0] == -2:
                                        tmp119 = subjects59.popleft()
                                        # State 93831
                                        if len(subjects59) == 0:
                                            pass
                                            # State 93832
                                            if len(subjects) == 0:
                                                pass
                                                # 10: sin(c + x*d)**(-2)
                                        subjects59.appendleft(tmp119)
                            subjects114.appendleft(tmp117)
                    if len(subjects114) >= 1 and isinstance(subjects114[0], Mul):
                        tmp120 = subjects114.popleft()
                        associative1 = tmp120
                        associative_type1 = type(tmp120)
                        subjects121 = deque(tmp120._args)
                        matcher = CommutativeMatcher93834.get()
                        tmp122 = subjects121
                        subjects121 = []
                        for s in tmp122:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp122, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 93835
                                if len(subjects114) == 0:
                                    pass
                                    # State 93836
                                    if len(subjects59) >= 1 and subjects59[0] == -2:
                                        tmp123 = subjects59.popleft()
                                        # State 93837
                                        if len(subjects59) == 0:
                                            pass
                                            # State 93838
                                            if len(subjects) == 0:
                                                pass
                                                # 10: sin(c + x*d)**(-2)
                                        subjects59.appendleft(tmp123)
                        subjects114.appendleft(tmp120)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 94415
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 94416
                        if len(subjects114) >= 1:
                            tmp126 = subjects114.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp126)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 94417
                                if len(subjects114) == 0:
                                    pass
                                    # State 94418
                                    if len(subjects59) >= 1 and subjects59[0] == -2:
                                        tmp128 = subjects59.popleft()
                                        # State 94419
                                        if len(subjects59) == 0:
                                            pass
                                            # State 94420
                                            if len(subjects) == 0:
                                                pass
                                                # 12: sin(e + x*f)**(-2)
                                        subjects59.appendleft(tmp128)
                            subjects114.appendleft(tmp126)
                    if len(subjects114) >= 1 and isinstance(subjects114[0], Mul):
                        tmp129 = subjects114.popleft()
                        associative1 = tmp129
                        associative_type1 = type(tmp129)
                        subjects130 = deque(tmp129._args)
                        matcher = CommutativeMatcher94422.get()
                        tmp131 = subjects130
                        subjects130 = []
                        for s in tmp131:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp131, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 94423
                                if len(subjects114) == 0:
                                    pass
                                    # State 94424
                                    if len(subjects59) >= 1 and subjects59[0] == -2:
                                        tmp132 = subjects59.popleft()
                                        # State 94425
                                        if len(subjects59) == 0:
                                            pass
                                            # State 94426
                                            if len(subjects) == 0:
                                                pass
                                                # 12: sin(e + x*f)**(-2)
                                        subjects59.appendleft(tmp132)
                        subjects114.appendleft(tmp129)
                if len(subjects114) >= 1 and isinstance(subjects114[0], Add):
                    tmp133 = subjects114.popleft()
                    associative1 = tmp133
                    associative_type1 = type(tmp133)
                    subjects134 = deque(tmp133._args)
                    matcher = CommutativeMatcher93840.get()
                    tmp135 = subjects134
                    subjects134 = []
                    for s in tmp135:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp135, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 93846
                            if len(subjects114) == 0:
                                pass
                                # State 93847
                                if len(subjects59) >= 1 and subjects59[0] == -2:
                                    tmp136 = subjects59.popleft()
                                    # State 93848
                                    if len(subjects59) == 0:
                                        pass
                                        # State 93849
                                        if len(subjects) == 0:
                                            pass
                                            # 10: sin(c + x*d)**(-2)
                                    subjects59.appendleft(tmp136)
                        if pattern_index == 1:
                            pass
                            # State 94430
                            if len(subjects114) == 0:
                                pass
                                # State 94431
                                if len(subjects59) >= 1 and subjects59[0] == -2:
                                    tmp137 = subjects59.popleft()
                                    # State 94432
                                    if len(subjects59) == 0:
                                        pass
                                        # State 94433
                                        if len(subjects) == 0:
                                            pass
                                            # 12: sin(e + x*f)**(-2)
                                    subjects59.appendleft(tmp137)
                    subjects114.appendleft(tmp133)
                subjects59.appendleft(tmp113)
            subjects.appendleft(tmp58)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp138 = subjects.popleft()
            subjects139 = deque(tmp138._args)
            # State 113935
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_2', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 113936
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 113937
                    if len(subjects139) >= 1 and isinstance(subjects139[0], Pow):
                        tmp142 = subjects139.popleft()
                        subjects143 = deque(tmp142._args)
                        # State 113938
                        if len(subjects143) >= 1:
                            tmp144 = subjects143.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.0', tmp144)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 113939
                                if len(subjects143) >= 1 and subjects143[0] == 2:
                                    tmp146 = subjects143.popleft()
                                    # State 113940
                                    if len(subjects143) == 0:
                                        pass
                                        # State 113941
                                        if len(subjects139) == 0:
                                            pass
                                            # State 113942
                                            if len(subjects) == 0:
                                                pass
                                                # 13: log(x**2*g + f)
                                    subjects143.appendleft(tmp146)
                            subjects143.appendleft(tmp144)
                        subjects139.appendleft(tmp142)
                if len(subjects139) >= 1 and isinstance(subjects139[0], Mul):
                    tmp147 = subjects139.popleft()
                    associative1 = tmp147
                    associative_type1 = type(tmp147)
                    subjects148 = deque(tmp147._args)
                    matcher = CommutativeMatcher113944.get()
                    tmp149 = subjects148
                    subjects148 = []
                    for s in tmp149:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp149, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 113949
                            if len(subjects139) == 0:
                                pass
                                # State 113950
                                if len(subjects) == 0:
                                    pass
                                    # 13: log(x**2*g + f)
                    subjects139.appendleft(tmp147)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 114101
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 114102
                    if len(subjects139) >= 1 and isinstance(subjects139[0], Pow):
                        tmp152 = subjects139.popleft()
                        subjects153 = deque(tmp152._args)
                        # State 114103
                        if len(subjects153) >= 1:
                            tmp154 = subjects153.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1', tmp154)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 114104
                                if len(subjects153) >= 1 and subjects153[0] == 2:
                                    tmp156 = subjects153.popleft()
                                    # State 114105
                                    if len(subjects153) == 0:
                                        pass
                                        # State 114106
                                        if len(subjects139) == 0:
                                            pass
                                            # State 114107
                                            if len(subjects) == 0:
                                                pass
                                                # 14: log(f + g*x**2)
                                    subjects153.appendleft(tmp156)
                            subjects153.appendleft(tmp154)
                        subjects139.appendleft(tmp152)
                if len(subjects139) >= 1 and isinstance(subjects139[0], Mul):
                    tmp157 = subjects139.popleft()
                    associative1 = tmp157
                    associative_type1 = type(tmp157)
                    subjects158 = deque(tmp157._args)
                    matcher = CommutativeMatcher114109.get()
                    tmp159 = subjects158
                    subjects158 = []
                    for s in tmp159:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp159, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 114114
                            if len(subjects139) == 0:
                                pass
                                # State 114115
                                if len(subjects) == 0:
                                    pass
                                    # 14: log(f + g*x**2)
                    subjects139.appendleft(tmp157)
            if len(subjects139) >= 1 and isinstance(subjects139[0], Add):
                tmp160 = subjects139.popleft()
                associative1 = tmp160
                associative_type1 = type(tmp160)
                subjects161 = deque(tmp160._args)
                matcher = CommutativeMatcher113952.get()
                tmp162 = subjects161
                subjects161 = []
                for s in tmp162:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp162, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 113965
                        if len(subjects139) == 0:
                            pass
                            # State 113966
                            if len(subjects) == 0:
                                pass
                                # 13: log(x**2*g + f)
                    if pattern_index == 1:
                        pass
                        # State 114123
                        if len(subjects139) == 0:
                            pass
                            # State 114124
                            if len(subjects) == 0:
                                pass
                                # 14: log(f + g*x**2)
                subjects139.appendleft(tmp160)
            subjects.appendleft(tmp138)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp163 = subjects.popleft()
            subjects164 = deque(tmp163._args)
            # State 139240
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139241
                if len(subjects164) >= 1:
                    tmp166 = subjects164.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp166)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139242
                        if len(subjects164) == 0:
                            pass
                            # State 139243
                            if len(subjects) == 0:
                                pass
                                # 15: acosh(c*x)
                    subjects164.appendleft(tmp166)
            if len(subjects164) >= 1 and isinstance(subjects164[0], Mul):
                tmp168 = subjects164.popleft()
                associative1 = tmp168
                associative_type1 = type(tmp168)
                subjects169 = deque(tmp168._args)
                matcher = CommutativeMatcher139245.get()
                tmp170 = subjects169
                subjects169 = []
                for s in tmp170:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp170, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 139246
                        if len(subjects164) == 0:
                            pass
                            # State 139247
                            if len(subjects) == 0:
                                pass
                                # 15: acosh(c*x)
                subjects164.appendleft(tmp168)
            subjects.appendleft(tmp163)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
