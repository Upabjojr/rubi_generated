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

class CommutativeMatcher11019(CommutativeMatcher):
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
        if CommutativeMatcher11019._instance is None:
            CommutativeMatcher11019._instance = CommutativeMatcher11019()
        return CommutativeMatcher11019._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 11018
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 11020
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11021
                    if len(subjects2) >= 1 and subjects2[0] == -1:
                        tmp5 = subjects2.popleft()
                        # State 11022
                        if len(subjects2) == 0:
                            pass
                            # State 11023
                            if len(subjects) == 0:
                                pass
                                # 0: 1/x
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp6 = subjects2.popleft()
                subjects7 = deque(tmp6._args)
                # State 85642
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 85643
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 85644
                        if len(subjects7) >= 1:
                            tmp10 = subjects7.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.3.1.0', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 85645
                                if len(subjects7) == 0:
                                    pass
                                    # State 85646
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp12 = subjects2.popleft()
                                        # State 85647
                                        if len(subjects2) == 0:
                                            pass
                                            # State 85648
                                            if len(subjects) == 0:
                                                pass
                                                # 6: 1/tan(c + x*d)
                                        subjects2.appendleft(tmp12)
                            subjects7.appendleft(tmp10)
                    if len(subjects7) >= 1 and isinstance(subjects7[0], Mul):
                        tmp13 = subjects7.popleft()
                        associative1 = tmp13
                        associative_type1 = type(tmp13)
                        subjects14 = deque(tmp13._args)
                        matcher = CommutativeMatcher85650.get()
                        tmp15 = subjects14
                        subjects14 = []
                        for s in tmp15:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp15, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 85651
                                if len(subjects7) == 0:
                                    pass
                                    # State 85652
                                    if len(subjects2) >= 1 and subjects2[0] == -1:
                                        tmp16 = subjects2.popleft()
                                        # State 85653
                                        if len(subjects2) == 0:
                                            pass
                                            # State 85654
                                            if len(subjects) == 0:
                                                pass
                                                # 6: 1/tan(c + x*d)
                                        subjects2.appendleft(tmp16)
                        subjects7.appendleft(tmp13)
                if len(subjects7) >= 1 and isinstance(subjects7[0], Add):
                    tmp17 = subjects7.popleft()
                    associative1 = tmp17
                    associative_type1 = type(tmp17)
                    subjects18 = deque(tmp17._args)
                    matcher = CommutativeMatcher85656.get()
                    tmp19 = subjects18
                    subjects18 = []
                    for s in tmp19:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp19, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 85662
                            if len(subjects7) == 0:
                                pass
                                # State 85663
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp20 = subjects2.popleft()
                                    # State 85664
                                    if len(subjects2) == 0:
                                        pass
                                        # State 85665
                                        if len(subjects) == 0:
                                            pass
                                            # 6: 1/tan(c + x*d)
                                    subjects2.appendleft(tmp20)
                    subjects7.appendleft(tmp17)
                subjects2.appendleft(tmp6)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp21 = subjects.popleft()
            subjects22 = deque(tmp21._args)
            # State 69771
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 69772
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 69773
                    if len(subjects22) >= 1:
                        tmp25 = subjects22.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp25)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 69774
                            if len(subjects22) == 0:
                                pass
                                # State 69775
                                if len(subjects) == 0:
                                    pass
                                    # 1: sin(c + x*d)
                        subjects22.appendleft(tmp25)
                if len(subjects22) >= 1 and isinstance(subjects22[0], Mul):
                    tmp27 = subjects22.popleft()
                    associative1 = tmp27
                    associative_type1 = type(tmp27)
                    subjects28 = deque(tmp27._args)
                    matcher = CommutativeMatcher69777.get()
                    tmp29 = subjects28
                    subjects28 = []
                    for s in tmp29:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp29, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 69778
                            if len(subjects22) == 0:
                                pass
                                # State 69779
                                if len(subjects) == 0:
                                    pass
                                    # 1: sin(c + x*d)
                    subjects22.appendleft(tmp27)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 71403
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 71404
                    if len(subjects22) >= 1:
                        tmp32 = subjects22.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp32)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 71405
                            if len(subjects22) == 0:
                                pass
                                # State 71406
                                if len(subjects) == 0:
                                    pass
                                    # 4: sin(e + x*f)
                        subjects22.appendleft(tmp32)
                if len(subjects22) >= 1 and isinstance(subjects22[0], Mul):
                    tmp34 = subjects22.popleft()
                    associative1 = tmp34
                    associative_type1 = type(tmp34)
                    subjects35 = deque(tmp34._args)
                    matcher = CommutativeMatcher71408.get()
                    tmp36 = subjects35
                    subjects35 = []
                    for s in tmp36:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp36, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 71409
                            if len(subjects22) == 0:
                                pass
                                # State 71410
                                if len(subjects) == 0:
                                    pass
                                    # 4: sin(e + x*f)
                    subjects22.appendleft(tmp34)
            if len(subjects22) >= 1 and isinstance(subjects22[0], Add):
                tmp37 = subjects22.popleft()
                associative1 = tmp37
                associative_type1 = type(tmp37)
                subjects38 = deque(tmp37._args)
                matcher = CommutativeMatcher69781.get()
                tmp39 = subjects38
                subjects38 = []
                for s in tmp39:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp39, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 69787
                        if len(subjects22) == 0:
                            pass
                            # State 69788
                            if len(subjects) == 0:
                                pass
                                # 1: sin(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 71414
                        if len(subjects22) == 0:
                            pass
                            # State 71415
                            if len(subjects) == 0:
                                pass
                                # 4: sin(e + x*f)
                subjects22.appendleft(tmp37)
            subjects.appendleft(tmp21)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp40 = subjects.popleft()
            subjects41 = deque(tmp40._args)
            # State 70222
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 70223
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 70224
                    if len(subjects41) >= 1:
                        tmp44 = subjects41.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp44)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 70225
                            if len(subjects41) == 0:
                                pass
                                # State 70226
                                if len(subjects) == 0:
                                    pass
                                    # 2: cos(c + x*d)
                        subjects41.appendleft(tmp44)
                if len(subjects41) >= 1 and isinstance(subjects41[0], Mul):
                    tmp46 = subjects41.popleft()
                    associative1 = tmp46
                    associative_type1 = type(tmp46)
                    subjects47 = deque(tmp46._args)
                    matcher = CommutativeMatcher70228.get()
                    tmp48 = subjects47
                    subjects47 = []
                    for s in tmp48:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp48, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 70229
                            if len(subjects41) == 0:
                                pass
                                # State 70230
                                if len(subjects) == 0:
                                    pass
                                    # 2: cos(c + x*d)
                    subjects41.appendleft(tmp46)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 70868
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 70869
                    if len(subjects41) >= 1:
                        tmp51 = subjects41.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp51)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 70870
                            if len(subjects41) == 0:
                                pass
                                # State 70871
                                if len(subjects) == 0:
                                    pass
                                    # 3: cos(e + x*f)
                        subjects41.appendleft(tmp51)
                if len(subjects41) >= 1 and isinstance(subjects41[0], Mul):
                    tmp53 = subjects41.popleft()
                    associative1 = tmp53
                    associative_type1 = type(tmp53)
                    subjects54 = deque(tmp53._args)
                    matcher = CommutativeMatcher70873.get()
                    tmp55 = subjects54
                    subjects54 = []
                    for s in tmp55:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp55, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 70874
                            if len(subjects41) == 0:
                                pass
                                # State 70875
                                if len(subjects) == 0:
                                    pass
                                    # 3: cos(e + x*f)
                    subjects41.appendleft(tmp53)
            if len(subjects41) >= 1 and isinstance(subjects41[0], Add):
                tmp56 = subjects41.popleft()
                associative1 = tmp56
                associative_type1 = type(tmp56)
                subjects57 = deque(tmp56._args)
                matcher = CommutativeMatcher70232.get()
                tmp58 = subjects57
                subjects57 = []
                for s in tmp58:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp58, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 70238
                        if len(subjects41) == 0:
                            pass
                            # State 70239
                            if len(subjects) == 0:
                                pass
                                # 2: cos(c + x*d)
                    if pattern_index == 1:
                        pass
                        # State 70879
                        if len(subjects41) == 0:
                            pass
                            # State 70880
                            if len(subjects) == 0:
                                pass
                                # 3: cos(e + x*f)
                subjects41.appendleft(tmp56)
            subjects.appendleft(tmp40)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp59 = subjects.popleft()
            subjects60 = deque(tmp59._args)
            # State 85275
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 85276
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 85277
                    if len(subjects60) >= 1:
                        tmp63 = subjects60.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp63)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 85278
                            if len(subjects60) == 0:
                                pass
                                # State 85279
                                if len(subjects) == 0:
                                    pass
                                    # 5: tan(c + x*d)
                        subjects60.appendleft(tmp63)
                if len(subjects60) >= 1 and isinstance(subjects60[0], Mul):
                    tmp65 = subjects60.popleft()
                    associative1 = tmp65
                    associative_type1 = type(tmp65)
                    subjects66 = deque(tmp65._args)
                    matcher = CommutativeMatcher85281.get()
                    tmp67 = subjects66
                    subjects66 = []
                    for s in tmp67:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp67, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 85282
                            if len(subjects60) == 0:
                                pass
                                # State 85283
                                if len(subjects) == 0:
                                    pass
                                    # 5: tan(c + x*d)
                    subjects60.appendleft(tmp65)
            if len(subjects60) >= 1 and isinstance(subjects60[0], Add):
                tmp68 = subjects60.popleft()
                associative1 = tmp68
                associative_type1 = type(tmp68)
                subjects69 = deque(tmp68._args)
                matcher = CommutativeMatcher85285.get()
                tmp70 = subjects69
                subjects69 = []
                for s in tmp70:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp70, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 85291
                        if len(subjects60) == 0:
                            pass
                            # State 85292
                            if len(subjects) == 0:
                                pass
                                # 5: tan(c + x*d)
                subjects60.appendleft(tmp68)
            subjects.appendleft(tmp59)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
