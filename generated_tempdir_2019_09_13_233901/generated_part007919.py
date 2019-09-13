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

class CommutativeMatcher147205(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher147205._instance is None:
            CommutativeMatcher147205._instance = CommutativeMatcher147205()
        return CommutativeMatcher147205._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 147204
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 147206
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 147207
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 147208
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 147209
                            if len(subjects2) == 0:
                                pass
                                # State 147210
                                if len(subjects) == 0:
                                    pass
                                    # 0: tanh(x*b + a)
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp7 = subjects2.popleft()
                    associative1 = tmp7
                    associative_type1 = type(tmp7)
                    subjects8 = deque(tmp7._args)
                    matcher = CommutativeMatcher147212.get()
                    tmp9 = subjects8
                    subjects8 = []
                    for s in tmp9:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp9, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 147213
                            if len(subjects2) == 0:
                                pass
                                # State 147214
                                if len(subjects) == 0:
                                    pass
                                    # 0: tanh(x*b + a)
                    subjects2.appendleft(tmp7)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp10 = subjects2.popleft()
                associative1 = tmp10
                associative_type1 = type(tmp10)
                subjects11 = deque(tmp10._args)
                matcher = CommutativeMatcher147216.get()
                tmp12 = subjects11
                subjects11 = []
                for s in tmp12:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp12, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 147222
                        if len(subjects2) == 0:
                            pass
                            # State 147223
                            if len(subjects) == 0:
                                pass
                                # 0: tanh(x*b + a)
                subjects2.appendleft(tmp10)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp13 = subjects.popleft()
            subjects14 = deque(tmp13._args)
            # State 147385
            if len(subjects14) >= 1 and isinstance(subjects14[0], tanh):
                tmp15 = subjects14.popleft()
                subjects16 = deque(tmp15._args)
                # State 147386
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 147387
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 147388
                        if len(subjects16) >= 1:
                            tmp19 = subjects16.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.0', tmp19)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 147389
                                if len(subjects16) == 0:
                                    pass
                                    # State 147390
                                    if len(subjects14) >= 1 and subjects14[0] == -1:
                                        tmp21 = subjects14.popleft()
                                        # State 147391
                                        if len(subjects14) == 0:
                                            pass
                                            # State 147392
                                            if len(subjects) == 0:
                                                pass
                                                # 1: 1/tanh(x*b + a)
                                        subjects14.appendleft(tmp21)
                            subjects16.appendleft(tmp19)
                    if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                        tmp22 = subjects16.popleft()
                        associative1 = tmp22
                        associative_type1 = type(tmp22)
                        subjects23 = deque(tmp22._args)
                        matcher = CommutativeMatcher147394.get()
                        tmp24 = subjects23
                        subjects23 = []
                        for s in tmp24:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp24, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 147395
                                if len(subjects16) == 0:
                                    pass
                                    # State 147396
                                    if len(subjects14) >= 1 and subjects14[0] == -1:
                                        tmp25 = subjects14.popleft()
                                        # State 147397
                                        if len(subjects14) == 0:
                                            pass
                                            # State 147398
                                            if len(subjects) == 0:
                                                pass
                                                # 1: 1/tanh(x*b + a)
                                        subjects14.appendleft(tmp25)
                        subjects16.appendleft(tmp22)
                if len(subjects16) >= 1 and isinstance(subjects16[0], Add):
                    tmp26 = subjects16.popleft()
                    associative1 = tmp26
                    associative_type1 = type(tmp26)
                    subjects27 = deque(tmp26._args)
                    matcher = CommutativeMatcher147400.get()
                    tmp28 = subjects27
                    subjects27 = []
                    for s in tmp28:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp28, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 147406
                            if len(subjects16) == 0:
                                pass
                                # State 147407
                                if len(subjects14) >= 1 and subjects14[0] == -1:
                                    tmp29 = subjects14.popleft()
                                    # State 147408
                                    if len(subjects14) == 0:
                                        pass
                                        # State 147409
                                        if len(subjects) == 0:
                                            pass
                                            # 1: 1/tanh(x*b + a)
                                    subjects14.appendleft(tmp29)
                    subjects16.appendleft(tmp26)
                subjects14.appendleft(tmp15)
            if len(subjects14) >= 1 and isinstance(subjects14[0], tan):
                tmp30 = subjects14.popleft()
                subjects31 = deque(tmp30._args)
                # State 148438
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 148439
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148440
                        if len(subjects31) >= 1:
                            tmp34 = subjects31.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.0', tmp34)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 148441
                                if len(subjects31) == 0:
                                    pass
                                    # State 148442
                                    if len(subjects14) >= 1 and subjects14[0] == -1:
                                        tmp36 = subjects14.popleft()
                                        # State 148443
                                        if len(subjects14) == 0:
                                            pass
                                            # State 148444
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/tan(x*e + d)
                                        subjects14.appendleft(tmp36)
                            subjects31.appendleft(tmp34)
                    if len(subjects31) >= 1 and isinstance(subjects31[0], Mul):
                        tmp37 = subjects31.popleft()
                        associative1 = tmp37
                        associative_type1 = type(tmp37)
                        subjects38 = deque(tmp37._args)
                        matcher = CommutativeMatcher148446.get()
                        tmp39 = subjects38
                        subjects38 = []
                        for s in tmp39:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp39, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 148447
                                if len(subjects31) == 0:
                                    pass
                                    # State 148448
                                    if len(subjects14) >= 1 and subjects14[0] == -1:
                                        tmp40 = subjects14.popleft()
                                        # State 148449
                                        if len(subjects14) == 0:
                                            pass
                                            # State 148450
                                            if len(subjects) == 0:
                                                pass
                                                # 3: 1/tan(x*e + d)
                                        subjects14.appendleft(tmp40)
                        subjects31.appendleft(tmp37)
                if len(subjects31) >= 1 and isinstance(subjects31[0], Add):
                    tmp41 = subjects31.popleft()
                    associative1 = tmp41
                    associative_type1 = type(tmp41)
                    subjects42 = deque(tmp41._args)
                    matcher = CommutativeMatcher148452.get()
                    tmp43 = subjects42
                    subjects42 = []
                    for s in tmp43:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp43, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 148458
                            if len(subjects31) == 0:
                                pass
                                # State 148459
                                if len(subjects14) >= 1 and subjects14[0] == -1:
                                    tmp44 = subjects14.popleft()
                                    # State 148460
                                    if len(subjects14) == 0:
                                        pass
                                        # State 148461
                                        if len(subjects) == 0:
                                            pass
                                            # 3: 1/tan(x*e + d)
                                    subjects14.appendleft(tmp44)
                    subjects31.appendleft(tmp41)
                subjects14.appendleft(tmp30)
            subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp45 = subjects.popleft()
            subjects46 = deque(tmp45._args)
            # State 148266
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 148267
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 148268
                    if len(subjects46) >= 1:
                        tmp49 = subjects46.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp49)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 148269
                            if len(subjects46) == 0:
                                pass
                                # State 148270
                                if len(subjects) == 0:
                                    pass
                                    # 2: tan(x*f + e)
                        subjects46.appendleft(tmp49)
                if len(subjects46) >= 1 and isinstance(subjects46[0], Mul):
                    tmp51 = subjects46.popleft()
                    associative1 = tmp51
                    associative_type1 = type(tmp51)
                    subjects52 = deque(tmp51._args)
                    matcher = CommutativeMatcher148272.get()
                    tmp53 = subjects52
                    subjects52 = []
                    for s in tmp53:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp53, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 148273
                            if len(subjects46) == 0:
                                pass
                                # State 148274
                                if len(subjects) == 0:
                                    pass
                                    # 2: tan(x*f + e)
                    subjects46.appendleft(tmp51)
            if len(subjects46) >= 1 and isinstance(subjects46[0], Add):
                tmp54 = subjects46.popleft()
                associative1 = tmp54
                associative_type1 = type(tmp54)
                subjects55 = deque(tmp54._args)
                matcher = CommutativeMatcher148276.get()
                tmp56 = subjects55
                subjects55 = []
                for s in tmp56:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp56, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 148282
                        if len(subjects46) == 0:
                            pass
                            # State 148283
                            if len(subjects) == 0:
                                pass
                                # 2: tan(x*f + e)
                subjects46.appendleft(tmp54)
            subjects.appendleft(tmp45)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque