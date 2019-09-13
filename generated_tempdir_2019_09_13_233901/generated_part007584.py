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

class CommutativeMatcher23879(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1, 6: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({1: 1, 0: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({8: 1, 9: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({2: 1, 10: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({11: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({12: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({12: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({13: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({14: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({15: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher23879._instance is None:
            CommutativeMatcher23879._instance = CommutativeMatcher23879()
        return CommutativeMatcher23879._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 23878
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 23880
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 23881
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.0', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 23882
                        if len(subjects) == 0:
                            pass
                            # 0: x*f + e
                    subjects.appendleft(tmp3)
                if len(subjects) >= 1:
                    tmp5 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.1.0', tmp5)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 27492
                        if len(subjects) == 0:
                            pass
                            # 3: j + k*x
                    subjects.appendleft(tmp5)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp7 = subjects.popleft()
                associative1 = tmp7
                associative_type1 = type(tmp7)
                subjects8 = deque(tmp7._args)
                matcher = CommutativeMatcher23884.get()
                tmp9 = subjects8
                subjects8 = []
                for s in tmp9:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp9, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 23885
                        if len(subjects) == 0:
                            pass
                            # 0: x*f + e
                    if pattern_index == 1:
                        pass
                        # State 27493
                        if len(subjects) == 0:
                            pass
                            # 3: j + k*x
                subjects.appendleft(tmp7)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 40479
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 40480
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp12 = subjects.popleft()
                    subjects13 = deque(tmp12._args)
                    # State 40481
                    if len(subjects13) >= 1:
                        tmp14 = subjects13.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp14)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40482
                            if len(subjects13) >= 1:
                                tmp16 = subjects13.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.1.2', tmp16)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40483
                                    if len(subjects13) == 0:
                                        pass
                                        # State 40484
                                        if len(subjects) == 0:
                                            pass
                                            # 4: a + b*x**mn
                                subjects13.appendleft(tmp16)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 40512
                                if len(subjects13) == 0:
                                    pass
                                    # State 40513
                                    if len(subjects) == 0:
                                        pass
                                        # 6: b + a*x**n
                            if len(subjects13) >= 1:
                                tmp19 = subjects13.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2', tmp19)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40512
                                    if len(subjects13) == 0:
                                        pass
                                        # State 40513
                                        if len(subjects) == 0:
                                            pass
                                            # 6: b + a*x**n
                                subjects13.appendleft(tmp19)
                        subjects13.appendleft(tmp14)
                    subjects.appendleft(tmp12)
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 40510
                    if len(subjects) >= 1:
                        tmp22 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.1', tmp22)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40511
                            if len(subjects) == 0:
                                pass
                                # 6: b + a*x**n
                        subjects.appendleft(tmp22)
                if len(subjects) >= 1:
                    tmp24 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp24)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 48423
                        if len(subjects) == 0:
                            pass
                            # 10: a + b*x
                    subjects.appendleft(tmp24)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp26 = subjects.popleft()
                associative1 = tmp26
                associative_type1 = type(tmp26)
                subjects27 = deque(tmp26._args)
                matcher = CommutativeMatcher40486.get()
                tmp28 = subjects27
                subjects27 = []
                for s in tmp28:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp28, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 40491
                        if len(subjects) == 0:
                            pass
                            # 4: a + b*x**mn
                    if pattern_index == 1:
                        pass
                        # State 40518
                        if len(subjects) == 0:
                            pass
                            # 6: b + a*x**n
                    if pattern_index == 2:
                        pass
                        # State 48424
                        if len(subjects) == 0:
                            pass
                            # 10: a + b*x
                subjects.appendleft(tmp26)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 47992
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp30 = subjects.popleft()
                associative1 = tmp30
                associative_type1 = type(tmp30)
                subjects31 = deque(tmp30._args)
                matcher = CommutativeMatcher47994.get()
                tmp32 = subjects31
                subjects31 = []
                for s in tmp32:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp32, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 48047
                        if len(subjects) == 0:
                            pass
                            # 7: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                    if pattern_index == 1:
                        pass
                        # State 48844
                        if len(subjects) == 0:
                            pass
                            # 11: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                subjects.appendleft(tmp30)
            if len(subjects) >= 1:
                tmp33 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1', tmp33)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53343
                    if len(subjects) == 0:
                        pass
                        # 12: x**n
                subjects.appendleft(tmp33)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 109765
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 109766
                    if len(subjects) >= 1:
                        tmp37 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.1', tmp37)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 109767
                            if len(subjects) == 0:
                                pass
                                # 14: (x*g + f)**m
                        subjects.appendleft(tmp37)
                    if len(subjects) >= 1:
                        tmp39 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.0', tmp39)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 139551
                            if len(subjects) == 0:
                                pass
                                # 15: (x*g + f)**m
                        subjects.appendleft(tmp39)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp41 = subjects.popleft()
                    associative1 = tmp41
                    associative_type1 = type(tmp41)
                    subjects42 = deque(tmp41._args)
                    matcher = CommutativeMatcher109769.get()
                    tmp43 = subjects42
                    subjects42 = []
                    for s in tmp43:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp43, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 109770
                            if len(subjects) == 0:
                                pass
                                # 14: (x*g + f)**m
                        if pattern_index == 1:
                            pass
                            # State 139552
                            if len(subjects) == 0:
                                pass
                                # 15: (x*g + f)**m
                    subjects.appendleft(tmp41)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp44 = subjects.popleft()
                associative1 = tmp44
                associative_type1 = type(tmp44)
                subjects45 = deque(tmp44._args)
                matcher = CommutativeMatcher109772.get()
                tmp46 = subjects45
                subjects45 = []
                for s in tmp46:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp46, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 109778
                        if len(subjects) == 0:
                            pass
                            # 14: (x*g + f)**m
                    if pattern_index == 1:
                        pass
                        # State 139555
                        if len(subjects) == 0:
                            pass
                            # 15: (x*g + f)**m
                subjects.appendleft(tmp44)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_3', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 48408
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 48409
                if len(subjects) >= 1:
                    tmp49 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.0', tmp49)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 48410
                        if len(subjects) == 0:
                            pass
                            # 9: x*f + a
                    subjects.appendleft(tmp49)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp51 = subjects.popleft()
                associative1 = tmp51
                associative_type1 = type(tmp51)
                subjects52 = deque(tmp51._args)
                matcher = CommutativeMatcher48412.get()
                tmp53 = subjects52
                subjects52 = []
                for s in tmp53:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp53, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 48413
                        if len(subjects) == 0:
                            pass
                            # 9: x*f + a
                subjects.appendleft(tmp51)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 53975
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp55 = subjects.popleft()
                subjects56 = deque(tmp55._args)
                # State 53976
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 53977
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.3.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53978
                        if len(subjects56) >= 1:
                            tmp59 = subjects56.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1', tmp59)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53979
                                if len(subjects56) == 0:
                                    pass
                                    # State 53980
                                    if len(subjects) == 0:
                                        pass
                                        # 13: log(x**n*b)**p
                            subjects56.appendleft(tmp59)
                    if len(subjects56) >= 1 and isinstance(subjects56[0], Pow):
                        tmp61 = subjects56.popleft()
                        subjects62 = deque(tmp61._args)
                        # State 53981
                        if len(subjects62) >= 1:
                            tmp63 = subjects62.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1', tmp63)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53982
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.3.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53983
                                    if len(subjects62) == 0:
                                        pass
                                        # State 53984
                                        if len(subjects56) == 0:
                                            pass
                                            # State 53985
                                            if len(subjects) == 0:
                                                pass
                                                # 13: log(x**n*b)**p
                                if len(subjects62) >= 1:
                                    tmp66 = subjects62.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.3.2', tmp66)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 53983
                                        if len(subjects62) == 0:
                                            pass
                                            # State 53984
                                            if len(subjects56) == 0:
                                                pass
                                                # State 53985
                                                if len(subjects) == 0:
                                                    pass
                                                    # 13: log(x**n*b)**p
                                    subjects62.appendleft(tmp66)
                            subjects62.appendleft(tmp63)
                        subjects56.appendleft(tmp61)
                if len(subjects56) >= 1 and isinstance(subjects56[0], Mul):
                    tmp68 = subjects56.popleft()
                    associative1 = tmp68
                    associative_type1 = type(tmp68)
                    subjects69 = deque(tmp68._args)
                    matcher = CommutativeMatcher53987.get()
                    tmp70 = subjects69
                    subjects69 = []
                    for s in tmp70:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp70, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 53994
                            if len(subjects56) == 0:
                                pass
                                # State 53995
                                if len(subjects) == 0:
                                    pass
                                    # 13: log(x**n*b)**p
                    subjects56.appendleft(tmp68)
                subjects.appendleft(tmp55)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp71 = subjects.popleft()
            associative1 = tmp71
            associative_type1 = type(tmp71)
            subjects72 = deque(tmp71._args)
            matcher = CommutativeMatcher23887.get()
            tmp73 = subjects72
            subjects72 = []
            for s in tmp73:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp73, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 23893
                    if len(subjects) == 0:
                        pass
                        # 0: x*f + e
                if pattern_index == 1:
                    pass
                    # State 27496
                    if len(subjects) == 0:
                        pass
                        # 3: j + k*x
                if pattern_index == 2:
                    pass
                    # State 40501
                    if len(subjects) == 0:
                        pass
                        # 4: a + b*x**mn
                if pattern_index == 3:
                    pass
                    # State 40528
                    if len(subjects) == 0:
                        pass
                        # 6: b + a*x**n
                if pattern_index == 4:
                    pass
                    # State 48414
                    if len(subjects) == 0:
                        pass
                        # 9: x*f + a
                if pattern_index == 5:
                    pass
                    # State 48427
                    if len(subjects) == 0:
                        pass
                        # 10: a + b*x
            subjects.appendleft(tmp71)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp74 = subjects.popleft()
            subjects75 = deque(tmp74._args)
            # State 25875
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 25876
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 25877
                    if len(subjects75) >= 1:
                        tmp78 = subjects75.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp78)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25878
                            if len(subjects75) >= 1 and subjects75[0] == -1:
                                tmp80 = subjects75.popleft()
                                # State 25879
                                if len(subjects75) == 0:
                                    pass
                                    # State 25880
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/(x*f + e)
                                subjects75.appendleft(tmp80)
                        subjects75.appendleft(tmp78)
                    if len(subjects75) >= 1:
                        tmp81 = subjects75.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp81)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 26357
                            if len(subjects75) >= 1 and subjects75[0] == -1:
                                tmp83 = subjects75.popleft()
                                # State 26358
                                if len(subjects75) == 0:
                                    pass
                                    # State 26359
                                    if len(subjects) == 0:
                                        pass
                                        # 2: 1/(x*f + e)
                                subjects75.appendleft(tmp83)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 109779
                                if len(subjects75) == 0:
                                    pass
                                    # State 109780
                                    if len(subjects) == 0:
                                        pass
                                        # 14: (x*g + f)**m
                            if len(subjects75) >= 1:
                                tmp85 = subjects75.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2', tmp85)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 109779
                                    if len(subjects75) == 0:
                                        pass
                                        # State 109780
                                        if len(subjects) == 0:
                                            pass
                                            # 14: (x*g + f)**m
                                subjects75.appendleft(tmp85)
                        subjects75.appendleft(tmp81)
                    if len(subjects75) >= 1:
                        tmp87 = subjects75.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.0', tmp87)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 139556
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 139557
                                if len(subjects75) == 0:
                                    pass
                                    # State 139558
                                    if len(subjects) == 0:
                                        pass
                                        # 15: (x*g + f)**m
                            if len(subjects75) >= 1:
                                tmp90 = subjects75.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2', tmp90)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 139557
                                    if len(subjects75) == 0:
                                        pass
                                        # State 139558
                                        if len(subjects) == 0:
                                            pass
                                            # 15: (x*g + f)**m
                                subjects75.appendleft(tmp90)
                        subjects75.appendleft(tmp87)
                if len(subjects75) >= 1 and isinstance(subjects75[0], Mul):
                    tmp92 = subjects75.popleft()
                    associative1 = tmp92
                    associative_type1 = type(tmp92)
                    subjects93 = deque(tmp92._args)
                    matcher = CommutativeMatcher25882.get()
                    tmp94 = subjects93
                    subjects93 = []
                    for s in tmp94:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp94, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 25883
                            if len(subjects75) >= 1 and subjects75[0] == -1:
                                tmp95 = subjects75.popleft()
                                # State 25884
                                if len(subjects75) == 0:
                                    pass
                                    # State 25885
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/(x*f + e)
                                subjects75.appendleft(tmp95)
                        if pattern_index == 1:
                            pass
                            # State 26360
                            if len(subjects75) >= 1 and subjects75[0] == -1:
                                tmp96 = subjects75.popleft()
                                # State 26361
                                if len(subjects75) == 0:
                                    pass
                                    # State 26362
                                    if len(subjects) == 0:
                                        pass
                                        # 2: 1/(x*f + e)
                                subjects75.appendleft(tmp96)
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 109781
                                if len(subjects75) == 0:
                                    pass
                                    # State 109782
                                    if len(subjects) == 0:
                                        pass
                                        # 14: (x*g + f)**m
                            if len(subjects75) >= 1:
                                tmp98 = []
                                tmp98.append(subjects75.popleft())
                                while True:
                                    if len(tmp98) > 1:
                                        tmp99 = create_operation_expression(associative1, tmp98)
                                    elif len(tmp98) == 1:
                                        tmp99 = tmp98[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.2', tmp99)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 109781
                                        if len(subjects75) == 0:
                                            pass
                                            # State 109782
                                            if len(subjects) == 0:
                                                pass
                                                # 14: (x*g + f)**m
                                    if len(subjects75) == 0:
                                        break
                                    tmp98.append(subjects75.popleft())
                                subjects75.extendleft(reversed(tmp98))
                        if pattern_index == 2:
                            pass
                            # State 139559
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 139560
                                if len(subjects75) == 0:
                                    pass
                                    # State 139561
                                    if len(subjects) == 0:
                                        pass
                                        # 15: (x*g + f)**m
                            if len(subjects75) >= 1:
                                tmp102 = []
                                tmp102.append(subjects75.popleft())
                                while True:
                                    if len(tmp102) > 1:
                                        tmp103 = create_operation_expression(associative1, tmp102)
                                    elif len(tmp102) == 1:
                                        tmp103 = tmp102[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.2', tmp103)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 139560
                                        if len(subjects75) == 0:
                                            pass
                                            # State 139561
                                            if len(subjects) == 0:
                                                pass
                                                # 15: (x*g + f)**m
                                    if len(subjects75) == 0:
                                        break
                                    tmp102.append(subjects75.popleft())
                                subjects75.extendleft(reversed(tmp102))
                    subjects75.appendleft(tmp92)
            if len(subjects75) >= 1:
                tmp105 = subjects75.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp105)
                except ValueError:
                    pass
                else:
                    pass
                    # State 40507
                    if len(subjects75) >= 1:
                        tmp107 = subjects75.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp107)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40508
                            if len(subjects75) == 0:
                                pass
                                # State 40509
                                if len(subjects) == 0:
                                    pass
                                    # 5: x**mn
                        subjects75.appendleft(tmp107)
                subjects75.appendleft(tmp105)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 48392
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 48393
                    if len(subjects75) >= 1:
                        tmp111 = subjects75.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp111)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48394
                            if len(subjects75) >= 1 and subjects75[0] == -1:
                                tmp113 = subjects75.popleft()
                                # State 48395
                                if len(subjects75) == 0:
                                    pass
                                    # State 48396
                                    if len(subjects) == 0:
                                        pass
                                        # 8: 1/(a + v*a)
                                subjects75.appendleft(tmp113)
                        subjects75.appendleft(tmp111)
                if len(subjects75) >= 1 and isinstance(subjects75[0], Mul):
                    tmp114 = subjects75.popleft()
                    associative1 = tmp114
                    associative_type1 = type(tmp114)
                    subjects115 = deque(tmp114._args)
                    matcher = CommutativeMatcher48398.get()
                    tmp116 = subjects115
                    subjects115 = []
                    for s in tmp116:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp116, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 48399
                            if len(subjects75) >= 1 and subjects75[0] == -1:
                                tmp117 = subjects75.popleft()
                                # State 48400
                                if len(subjects75) == 0:
                                    pass
                                    # State 48401
                                    if len(subjects) == 0:
                                        pass
                                        # 8: 1/(a + v*a)
                                subjects75.appendleft(tmp117)
                    subjects75.appendleft(tmp114)
            if len(subjects75) >= 1:
                tmp118 = subjects75.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1', tmp118)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53344
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53345
                        if len(subjects75) == 0:
                            pass
                            # State 53346
                            if len(subjects) == 0:
                                pass
                                # 12: x**n
                    if len(subjects75) >= 1:
                        tmp121 = subjects75.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp121)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53345
                            if len(subjects75) == 0:
                                pass
                                # State 53346
                                if len(subjects) == 0:
                                    pass
                                    # 12: x**n
                        subjects75.appendleft(tmp121)
                subjects75.appendleft(tmp118)
            if len(subjects75) >= 1 and isinstance(subjects75[0], Add):
                tmp123 = subjects75.popleft()
                associative1 = tmp123
                associative_type1 = type(tmp123)
                subjects124 = deque(tmp123._args)
                matcher = CommutativeMatcher25887.get()
                tmp125 = subjects124
                subjects124 = []
                for s in tmp125:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp125, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 25893
                        if len(subjects75) >= 1 and subjects75[0] == -1:
                            tmp126 = subjects75.popleft()
                            # State 25894
                            if len(subjects75) == 0:
                                pass
                                # State 25895
                                if len(subjects) == 0:
                                    pass
                                    # 1: 1/(x*f + e)
                            subjects75.appendleft(tmp126)
                    if pattern_index == 1:
                        pass
                        # State 26365
                        if len(subjects75) >= 1 and subjects75[0] == -1:
                            tmp127 = subjects75.popleft()
                            # State 26366
                            if len(subjects75) == 0:
                                pass
                                # State 26367
                                if len(subjects) == 0:
                                    pass
                                    # 2: 1/(x*f + e)
                            subjects75.appendleft(tmp127)
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 109783
                            if len(subjects75) == 0:
                                pass
                                # State 109784
                                if len(subjects) == 0:
                                    pass
                                    # 14: (x*g + f)**m
                        if len(subjects75) >= 1:
                            tmp129 = []
                            tmp129.append(subjects75.popleft())
                            while True:
                                if len(tmp129) > 1:
                                    tmp130 = create_operation_expression(associative1, tmp129)
                                elif len(tmp129) == 1:
                                    tmp130 = tmp129[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp130)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 109783
                                    if len(subjects75) == 0:
                                        pass
                                        # State 109784
                                        if len(subjects) == 0:
                                            pass
                                            # 14: (x*g + f)**m
                                if len(subjects75) == 0:
                                    break
                                tmp129.append(subjects75.popleft())
                            subjects75.extendleft(reversed(tmp129))
                    if pattern_index == 2:
                        pass
                        # State 48405
                        if len(subjects75) >= 1 and subjects75[0] == -1:
                            tmp132 = subjects75.popleft()
                            # State 48406
                            if len(subjects75) == 0:
                                pass
                                # State 48407
                                if len(subjects) == 0:
                                    pass
                                    # 8: 1/(a + v*a)
                            subjects75.appendleft(tmp132)
                    if pattern_index == 3:
                        pass
                        # State 139564
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 139565
                            if len(subjects75) == 0:
                                pass
                                # State 139566
                                if len(subjects) == 0:
                                    pass
                                    # 15: (x*g + f)**m
                        if len(subjects75) >= 1:
                            tmp134 = []
                            tmp134.append(subjects75.popleft())
                            while True:
                                if len(tmp134) > 1:
                                    tmp135 = create_operation_expression(associative1, tmp134)
                                elif len(tmp134) == 1:
                                    tmp135 = tmp134[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp135)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 139565
                                    if len(subjects75) == 0:
                                        pass
                                        # State 139566
                                        if len(subjects) == 0:
                                            pass
                                            # 15: (x*g + f)**m
                                if len(subjects75) == 0:
                                    break
                                tmp134.append(subjects75.popleft())
                            subjects75.extendleft(reversed(tmp134))
                subjects75.appendleft(tmp123)
            if len(subjects75) >= 1 and isinstance(subjects75[0], Mul):
                tmp137 = subjects75.popleft()
                associative1 = tmp137
                associative_type1 = type(tmp137)
                subjects138 = deque(tmp137._args)
                matcher = CommutativeMatcher48049.get()
                tmp139 = subjects138
                subjects138 = []
                for s in tmp139:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp139, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 48102
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48103
                            if len(subjects75) == 0:
                                pass
                                # State 48104
                                if len(subjects) == 0:
                                    pass
                                    # 7: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                        if len(subjects75) >= 1:
                            tmp141 = []
                            tmp141.append(subjects75.popleft())
                            while True:
                                if len(tmp141) > 1:
                                    tmp142 = create_operation_expression(associative1, tmp141)
                                elif len(tmp141) == 1:
                                    tmp142 = tmp141[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp142)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48103
                                    if len(subjects75) == 0:
                                        pass
                                        # State 48104
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                                if len(subjects75) == 0:
                                    break
                                tmp141.append(subjects75.popleft())
                            subjects75.extendleft(reversed(tmp141))
                    if pattern_index == 1:
                        pass
                        # State 48872
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48873
                            if len(subjects75) == 0:
                                pass
                                # State 48874
                                if len(subjects) == 0:
                                    pass
                                    # 11: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                        if len(subjects75) >= 1:
                            tmp145 = []
                            tmp145.append(subjects75.popleft())
                            while True:
                                if len(tmp145) > 1:
                                    tmp146 = create_operation_expression(associative1, tmp145)
                                elif len(tmp145) == 1:
                                    tmp146 = tmp145[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp146)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48873
                                    if len(subjects75) == 0:
                                        pass
                                        # State 48874
                                        if len(subjects) == 0:
                                            pass
                                            # 11: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                                if len(subjects75) == 0:
                                    break
                                tmp145.append(subjects75.popleft())
                            subjects75.extendleft(reversed(tmp145))
                subjects75.appendleft(tmp137)
            if len(subjects75) >= 1 and isinstance(subjects75[0], log):
                tmp148 = subjects75.popleft()
                subjects149 = deque(tmp148._args)
                # State 53996
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 53997
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53998
                        if len(subjects149) >= 1:
                            tmp152 = subjects149.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1', tmp152)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53999
                                if len(subjects149) == 0:
                                    pass
                                    # State 54000
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54001
                                        if len(subjects75) == 0:
                                            pass
                                            # State 54002
                                            if len(subjects) == 0:
                                                pass
                                                # 13: log(x**n*b)**p
                                    if len(subjects75) >= 1:
                                        tmp155 = subjects75.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.3', tmp155)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54001
                                            if len(subjects75) == 0:
                                                pass
                                                # State 54002
                                                if len(subjects) == 0:
                                                    pass
                                                    # 13: log(x**n*b)**p
                                        subjects75.appendleft(tmp155)
                            subjects149.appendleft(tmp152)
                    if len(subjects149) >= 1 and isinstance(subjects149[0], Pow):
                        tmp157 = subjects149.popleft()
                        subjects158 = deque(tmp157._args)
                        # State 54003
                        if len(subjects158) >= 1:
                            tmp159 = subjects158.popleft()
                            subst2 = Substitution(subst1)
                            try:
                                subst2.try_add_variable('i2.1', tmp159)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 54004
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.3.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54005
                                    if len(subjects158) == 0:
                                        pass
                                        # State 54006
                                        if len(subjects149) == 0:
                                            pass
                                            # State 54007
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.3', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54008
                                                if len(subjects75) == 0:
                                                    pass
                                                    # State 54009
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 13: log(x**n*b)**p
                                            if len(subjects75) >= 1:
                                                tmp163 = subjects75.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.3', tmp163)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54008
                                                    if len(subjects75) == 0:
                                                        pass
                                                        # State 54009
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 13: log(x**n*b)**p
                                                subjects75.appendleft(tmp163)
                                if len(subjects158) >= 1:
                                    tmp165 = subjects158.popleft()
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.3.2', tmp165)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54005
                                        if len(subjects158) == 0:
                                            pass
                                            # State 54006
                                            if len(subjects149) == 0:
                                                pass
                                                # State 54007
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.3', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54008
                                                    if len(subjects75) == 0:
                                                        pass
                                                        # State 54009
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 13: log(x**n*b)**p
                                                if len(subjects75) >= 1:
                                                    tmp168 = subjects75.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.3', tmp168)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54008
                                                        if len(subjects75) == 0:
                                                            pass
                                                            # State 54009
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 13: log(x**n*b)**p
                                                    subjects75.appendleft(tmp168)
                                    subjects158.appendleft(tmp165)
                            subjects158.appendleft(tmp159)
                        subjects149.appendleft(tmp157)
                if len(subjects149) >= 1 and isinstance(subjects149[0], Mul):
                    tmp170 = subjects149.popleft()
                    associative1 = tmp170
                    associative_type1 = type(tmp170)
                    subjects171 = deque(tmp170._args)
                    matcher = CommutativeMatcher54011.get()
                    tmp172 = subjects171
                    subjects171 = []
                    for s in tmp172:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp172, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 54018
                            if len(subjects149) == 0:
                                pass
                                # State 54019
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54020
                                    if len(subjects75) == 0:
                                        pass
                                        # State 54021
                                        if len(subjects) == 0:
                                            pass
                                            # 13: log(x**n*b)**p
                                if len(subjects75) >= 1:
                                    tmp174 = subjects75.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.2.3', tmp174)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54020
                                        if len(subjects75) == 0:
                                            pass
                                            # State 54021
                                            if len(subjects) == 0:
                                                pass
                                                # 13: log(x**n*b)**p
                                    subjects75.appendleft(tmp174)
                    subjects149.appendleft(tmp170)
                subjects75.appendleft(tmp148)
            subjects.appendleft(tmp74)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
