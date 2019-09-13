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

class CommutativeMatcher11065(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher11065._instance is None:
            CommutativeMatcher11065._instance = CommutativeMatcher11065()
        return CommutativeMatcher11065._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 11064
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 11066
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11067
                    if len(subjects2) >= 1 and subjects2[0] == -1:
                        tmp5 = subjects2.popleft()
                        # State 11068
                        if len(subjects2) == 0:
                            pass
                            # State 11069
                            if len(subjects) == 0:
                                pass
                                # 0: 1/x
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp6 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11149
                    if len(subjects2) >= 1 and subjects2[0] == -1:
                        tmp8 = subjects2.popleft()
                        # State 11150
                        if len(subjects2) == 0:
                            pass
                            # State 11151
                            if len(subjects) == 0:
                                pass
                                # 1: 1/x
                        subjects2.appendleft(tmp8)
                subjects2.appendleft(tmp6)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp9 = subjects2.popleft()
                subjects10 = deque(tmp9._args)
                # State 84508
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 84509
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 84510
                        if len(subjects10) >= 1:
                            tmp13 = subjects10.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.3.1.0', tmp13)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 84511
                                if len(subjects10) == 0:
                                    pass
                                    # State 84512
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp15 = subjects2.popleft()
                                        # State 84513
                                        if len(subjects2) == 0:
                                            pass
                                            # State 84514
                                            if len(subjects) == 0:
                                                pass
                                                # 7: 1/tan(c + x*d)
                                        subjects2.appendleft(tmp15)
                            subjects10.appendleft(tmp13)
                    if len(subjects10) >= 1 and isinstance(subjects10[0], Mul):
                        tmp16 = subjects10.popleft()
                        associative1 = tmp16
                        associative_type1 = type(tmp16)
                        subjects17 = deque(tmp16._args)
                        matcher = CommutativeMatcher84516.get()
                        tmp18 = subjects17
                        subjects17 = []
                        for s in tmp18:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp18, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 84517
                                if len(subjects10) == 0:
                                    pass
                                    # State 84518
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp19 = subjects2.popleft()
                                        # State 84519
                                        if len(subjects2) == 0:
                                            pass
                                            # State 84520
                                            if len(subjects) == 0:
                                                pass
                                                # 7: 1/tan(c + x*d)
                                        subjects2.appendleft(tmp19)
                        subjects10.appendleft(tmp16)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 86251
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 86252
                        if len(subjects10) >= 1:
                            tmp22 = subjects10.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.0', tmp22)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 86253
                                if len(subjects10) == 0:
                                    pass
                                    # State 86254
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp24 = subjects2.popleft()
                                        # State 86255
                                        if len(subjects2) == 0:
                                            pass
                                            # State 86256
                                            if len(subjects) == 0:
                                                pass
                                                # 8: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp24)
                            subjects10.appendleft(tmp22)
                    if len(subjects10) >= 1 and isinstance(subjects10[0], Mul):
                        tmp25 = subjects10.popleft()
                        associative1 = tmp25
                        associative_type1 = type(tmp25)
                        subjects26 = deque(tmp25._args)
                        matcher = CommutativeMatcher86258.get()
                        tmp27 = subjects26
                        subjects26 = []
                        for s in tmp27:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp27, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 86259
                                if len(subjects10) == 0:
                                    pass
                                    # State 86260
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp28 = subjects2.popleft()
                                        # State 86261
                                        if len(subjects2) == 0:
                                            pass
                                            # State 86262
                                            if len(subjects) == 0:
                                                pass
                                                # 8: 1/tan(e + x*f)
                                        subjects2.appendleft(tmp28)
                        subjects10.appendleft(tmp25)
                if len(subjects10) >= 1 and isinstance(subjects10[0], Add):
                    tmp29 = subjects10.popleft()
                    associative1 = tmp29
                    associative_type1 = type(tmp29)
                    subjects30 = deque(tmp29._args)
                    matcher = CommutativeMatcher84522.get()
                    tmp31 = subjects30
                    subjects30 = []
                    for s in tmp31:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp31, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 84528
                            if len(subjects10) == 0:
                                pass
                                # State 84529
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp32 = subjects2.popleft()
                                    # State 84530
                                    if len(subjects2) == 0:
                                        pass
                                        # State 84531
                                        if len(subjects) == 0:
                                            pass
                                            # 7: 1/tan(c + x*d)
                                    subjects2.appendleft(tmp32)
                        if pattern_index == 1:
                            pass
                            # State 86266
                            if len(subjects10) == 0:
                                pass
                                # State 86267
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp33 = subjects2.popleft()
                                    # State 86268
                                    if len(subjects2) == 0:
                                        pass
                                        # State 86269
                                        if len(subjects) == 0:
                                            pass
                                            # 8: 1/tan(e + x*f)
                                    subjects2.appendleft(tmp33)
                    subjects10.appendleft(tmp29)
                subjects2.appendleft(tmp9)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp34 = subjects.popleft()
            subjects35 = deque(tmp34._args)
            # State 69997
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 69998
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 69999
                    if len(subjects35) >= 1:
                        tmp38 = subjects35.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp38)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 70000
                            if len(subjects35) == 0:
                                pass
                                # State 70001
                                if len(subjects) == 0:
                                    pass
                                    # 2: sin(c + x*d)
                        subjects35.appendleft(tmp38)
                if len(subjects35) >= 1 and isinstance(subjects35[0], Mul):
                    tmp40 = subjects35.popleft()
                    associative1 = tmp40
                    associative_type1 = type(tmp40)
                    subjects41 = deque(tmp40._args)
                    matcher = CommutativeMatcher70003.get()
                    tmp42 = subjects41
                    subjects41 = []
                    for s in tmp42:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp42, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 70004
                            if len(subjects35) == 0:
                                pass
                                # State 70005
                                if len(subjects) == 0:
                                    pass
                                    # 2: sin(c + x*d)
                    subjects35.appendleft(tmp40)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 71573
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 71574
                    if len(subjects35) >= 1:
                        tmp45 = subjects35.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp45)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 71575
                            if len(subjects35) == 0:
                                pass
                                # State 71576
                                if len(subjects) == 0:
                                    pass
                                    # 5: sin(e + x*f)
                        subjects35.appendleft(tmp45)
                if len(subjects35) >= 1 and isinstance(subjects35[0], Mul):
                    tmp47 = subjects35.popleft()
                    associative1 = tmp47
                    associative_type1 = type(tmp47)
                    subjects48 = deque(tmp47._args)
                    matcher = CommutativeMatcher71578.get()
                    tmp49 = subjects48
                    subjects48 = []
                    for s in tmp49:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp49, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 71579
                            if len(subjects35) == 0:
                                pass
                                # State 71580
                                if len(subjects) == 0:
                                    pass
                                    # 5: sin(e + x*f)
                    subjects35.appendleft(tmp47)
            if len(subjects35) >= 1 and isinstance(subjects35[0], Add):
                tmp50 = subjects35.popleft()
                associative1 = tmp50
                associative_type1 = type(tmp50)
                subjects51 = deque(tmp50._args)
                matcher = CommutativeMatcher70007.get()
                tmp52 = subjects51
                subjects51 = []
                for s in tmp52:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp52, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 70013
                        if len(subjects35) == 0:
                            pass
                            # State 70014
                            if len(subjects) == 0:
                                pass
                                # 2: sin(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 71584
                        if len(subjects35) == 0:
                            pass
                            # State 71585
                            if len(subjects) == 0:
                                pass
                                # 5: sin(e + x*f)
                subjects35.appendleft(tmp50)
            subjects.appendleft(tmp34)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp53 = subjects.popleft()
            subjects54 = deque(tmp53._args)
            # State 70442
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 70443
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 70444
                    if len(subjects54) >= 1:
                        tmp57 = subjects54.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp57)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 70445
                            if len(subjects54) == 0:
                                pass
                                # State 70446
                                if len(subjects) == 0:
                                    pass
                                    # 3: cos(c + x*d)
                        subjects54.appendleft(tmp57)
                if len(subjects54) >= 1 and isinstance(subjects54[0], Mul):
                    tmp59 = subjects54.popleft()
                    associative1 = tmp59
                    associative_type1 = type(tmp59)
                    subjects60 = deque(tmp59._args)
                    matcher = CommutativeMatcher70448.get()
                    tmp61 = subjects60
                    subjects60 = []
                    for s in tmp61:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp61, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 70449
                            if len(subjects54) == 0:
                                pass
                                # State 70450
                                if len(subjects) == 0:
                                    pass
                                    # 3: cos(c + x*d)
                    subjects54.appendleft(tmp59)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 70967
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 70968
                    if len(subjects54) >= 1:
                        tmp64 = subjects54.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp64)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 70969
                            if len(subjects54) == 0:
                                pass
                                # State 70970
                                if len(subjects) == 0:
                                    pass
                                    # 4: cos(e + x*f)
                        subjects54.appendleft(tmp64)
                if len(subjects54) >= 1 and isinstance(subjects54[0], Mul):
                    tmp66 = subjects54.popleft()
                    associative1 = tmp66
                    associative_type1 = type(tmp66)
                    subjects67 = deque(tmp66._args)
                    matcher = CommutativeMatcher70972.get()
                    tmp68 = subjects67
                    subjects67 = []
                    for s in tmp68:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp68, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 70973
                            if len(subjects54) == 0:
                                pass
                                # State 70974
                                if len(subjects) == 0:
                                    pass
                                    # 4: cos(e + x*f)
                    subjects54.appendleft(tmp66)
            if len(subjects54) >= 1 and isinstance(subjects54[0], Add):
                tmp69 = subjects54.popleft()
                associative1 = tmp69
                associative_type1 = type(tmp69)
                subjects70 = deque(tmp69._args)
                matcher = CommutativeMatcher70452.get()
                tmp71 = subjects70
                subjects70 = []
                for s in tmp71:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp71, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 70458
                        if len(subjects54) == 0:
                            pass
                            # State 70459
                            if len(subjects) == 0:
                                pass
                                # 3: cos(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 70978
                        if len(subjects54) == 0:
                            pass
                            # State 70979
                            if len(subjects) == 0:
                                pass
                                # 4: cos(e + x*f)
                subjects54.appendleft(tmp69)
            subjects.appendleft(tmp53)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp72 = subjects.popleft()
            subjects73 = deque(tmp72._args)
            # State 84225
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 84226
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 84227
                    if len(subjects73) >= 1:
                        tmp76 = subjects73.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp76)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 84228
                            if len(subjects73) == 0:
                                pass
                                # State 84229
                                if len(subjects) == 0:
                                    pass
                                    # 6: tan(c + x*d)
                        subjects73.appendleft(tmp76)
                if len(subjects73) >= 1 and isinstance(subjects73[0], Mul):
                    tmp78 = subjects73.popleft()
                    associative1 = tmp78
                    associative_type1 = type(tmp78)
                    subjects79 = deque(tmp78._args)
                    matcher = CommutativeMatcher84231.get()
                    tmp80 = subjects79
                    subjects79 = []
                    for s in tmp80:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp80, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 84232
                            if len(subjects73) == 0:
                                pass
                                # State 84233
                                if len(subjects) == 0:
                                    pass
                                    # 6: tan(c + x*d)
                    subjects73.appendleft(tmp78)
            if len(subjects73) >= 1 and isinstance(subjects73[0], Add):
                tmp81 = subjects73.popleft()
                associative1 = tmp81
                associative_type1 = type(tmp81)
                subjects82 = deque(tmp81._args)
                matcher = CommutativeMatcher84235.get()
                tmp83 = subjects82
                subjects82 = []
                for s in tmp83:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp83, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 84241
                        if len(subjects73) == 0:
                            pass
                            # State 84242
                            if len(subjects) == 0:
                                pass
                                # 6: tan(c + x*d)
                subjects73.appendleft(tmp81)
            subjects.appendleft(tmp72)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
