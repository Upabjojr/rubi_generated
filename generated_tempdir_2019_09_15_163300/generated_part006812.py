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


class CommutativeMatcher114299(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({3: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    5: (5, Multiset({2: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    6: (6, Multiset({4: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    7: (7, Multiset({5: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({6: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({7: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({8: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    11: (11, Multiset({9: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    12: (12, Multiset({9: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({10: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({11: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({12: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    16: (16, Multiset({13: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    17: (17, Multiset({14: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({15: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({16: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({17: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({18: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({19: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({19: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    24: (24, Multiset({20: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    25: (25, Multiset({3: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    26: (26, Multiset({21: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    27: (27, Multiset({22: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({23: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({24: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({25: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    31: (31, Multiset({26: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({26: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    33: (33, Multiset({27: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({28: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({28: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    36: (36, Multiset({29: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul)
]),
    37: (37, Multiset({30: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    38: (38, Multiset({31: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({32: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({33: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher114299._instance is None:
            CommutativeMatcher114299._instance = CommutativeMatcher114299()
        return CommutativeMatcher114299._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 114298
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 114300
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 114301
                if len(subjects2) >= 1:
                    tmp4 = subjects2.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114302
                        if len(subjects2) == 0:
                            pass
                            # State 114303
                            if len(subjects) == 0:
                                pass
                                # 0: atan(x*a)
                                yield 0, subst2
                    subjects2.appendleft(tmp4)
                if len(subjects2) >= 1:
                    tmp6 = subjects2.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp6)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114354
                        if len(subjects2) == 0:
                            pass
                            # State 114355
                            if len(subjects) == 0:
                                pass
                                # 1: atan(x*a)
                                yield 1, subst2
                    subjects2.appendleft(tmp6)
                if len(subjects2) >= 1:
                    tmp8 = subjects2.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp8)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114386
                        if len(subjects2) == 0:
                            pass
                            # State 114387
                            if len(subjects) == 0:
                                pass
                                # 2: atan(x*a)
                                yield 2, subst2
                    subjects2.appendleft(tmp8)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                    tmp10 = subjects2.popleft()
                    associative1 = tmp10
                    associative_type1 = type(tmp10)
                    subjects11 = deque(tmp10._args)
                    matcher = CommutativeMatcher114557.get()
                    tmp12 = subjects11
                    subjects11 = []
                    for s in tmp12:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp12, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 114563
                            if len(subjects2) == 0:
                                pass
                                # State 114564
                                if len(subjects) == 0:
                                    pass
                                    # 4: atan(c*(x*b + a))
                                    yield 4, subst2
                        if pattern_index == 1:
                            pass
                            # State 114603
                            if len(subjects2) == 0:
                                pass
                                # State 114604
                                if len(subjects) == 0:
                                    pass
                                    # 5: atan(c*(x*b + a))
                                    yield 5, subst2
                    subjects2.appendleft(tmp10)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp13 = subjects2.popleft()
                    subjects14 = deque(tmp13._args)
                    # State 114815
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114816
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 114817
                            if len(subjects14) >= 1:
                                tmp17 = subjects14.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2.1.0', tmp17)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 114818
                                    if len(subjects14) >= 1 and subjects14[0] == Integer(-1):
                                        tmp19 = subjects14.popleft()
                                        # State 114819
                                        if len(subjects14) == 0:
                                            pass
                                            # State 114820
                                            if len(subjects2) == 0:
                                                pass
                                                # State 114821
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: atan(c/(a + x*b))
                                                    yield 7, subst4
                                        subjects14.appendleft(tmp19)
                                subjects14.appendleft(tmp17)
                        if len(subjects14) >= 1 and isinstance(subjects14[0], Mul):
                            tmp20 = subjects14.popleft()
                            associative1 = tmp20
                            associative_type1 = type(tmp20)
                            subjects21 = deque(tmp20._args)
                            matcher = CommutativeMatcher114823.get()
                            tmp22 = subjects21
                            subjects21 = []
                            for s in tmp22:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp22, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 114824
                                    if len(subjects14) >= 1 and subjects14[0] == Integer(-1):
                                        tmp23 = subjects14.popleft()
                                        # State 114825
                                        if len(subjects14) == 0:
                                            pass
                                            # State 114826
                                            if len(subjects2) == 0:
                                                pass
                                                # State 114827
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: atan(c/(a + x*b))
                                                    yield 7, subst3
                                        subjects14.appendleft(tmp23)
                            subjects14.appendleft(tmp20)
                    if len(subjects14) >= 1 and isinstance(subjects14[0], Add):
                        tmp24 = subjects14.popleft()
                        associative1 = tmp24
                        associative_type1 = type(tmp24)
                        subjects25 = deque(tmp24._args)
                        matcher = CommutativeMatcher114829.get()
                        tmp26 = subjects25
                        subjects25 = []
                        for s in tmp26:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp26, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 114835
                                if len(subjects14) >= 1 and subjects14[0] == Integer(-1):
                                    tmp27 = subjects14.popleft()
                                    # State 114836
                                    if len(subjects14) == 0:
                                        pass
                                        # State 114837
                                        if len(subjects2) == 0:
                                            pass
                                            # State 114838
                                            if len(subjects) == 0:
                                                pass
                                                # 7: atan(c/(a + x*b))
                                                yield 7, subst2
                                    subjects14.appendleft(tmp27)
                        subjects14.appendleft(tmp24)
                    subjects2.appendleft(tmp13)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp28 = subjects2.popleft()
                associative1 = tmp28
                associative_type1 = type(tmp28)
                subjects29 = deque(tmp28._args)
                matcher = CommutativeMatcher114305.get()
                tmp30 = subjects29
                subjects29 = []
                for s in tmp30:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp30, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 114306
                        if len(subjects2) == 0:
                            pass
                            # State 114307
                            if len(subjects) == 0:
                                pass
                                # 0: atan(x*a)
                                yield 0, subst1
                    if pattern_index == 1:
                        pass
                        # State 114356
                        if len(subjects2) == 0:
                            pass
                            # State 114357
                            if len(subjects) == 0:
                                pass
                                # 1: atan(x*a)
                                yield 1, subst1
                    if pattern_index == 2:
                        pass
                        # State 114388
                        if len(subjects2) == 0:
                            pass
                            # State 114389
                            if len(subjects) == 0:
                                pass
                                # 2: atan(x*a)
                                yield 2, subst1
                    if pattern_index == 3:
                        pass
                        # State 114573
                        if len(subjects2) == 0:
                            pass
                            # State 114574
                            if len(subjects) == 0:
                                pass
                                # 4: atan(c*(x*b + a))
                                yield 4, subst1
                    if pattern_index == 4:
                        pass
                        # State 114608
                        if len(subjects2) == 0:
                            pass
                            # State 114609
                            if len(subjects) == 0:
                                pass
                                # 5: atan(c*(x*b + a))
                                yield 5, subst1
                    if pattern_index == 5:
                        pass
                        # State 114860
                        if len(subjects2) == 0:
                            pass
                            # State 114861
                            if len(subjects) == 0:
                                pass
                                # 7: atan(c/(a + x*b))
                                yield 7, subst1
                subjects2.appendleft(tmp28)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp31 = subjects2.popleft()
                associative1 = tmp31
                associative_type1 = type(tmp31)
                subjects32 = deque(tmp31._args)
                matcher = CommutativeMatcher114626.get()
                tmp33 = subjects32
                subjects32 = []
                for s in tmp33:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp33, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 114632
                        if len(subjects2) == 0:
                            pass
                            # State 114633
                            if len(subjects) == 0:
                                pass
                                # 6: atan(x*b + a)
                                yield 6, subst1
                subjects2.appendleft(tmp31)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp34 = subjects.popleft()
            subjects35 = deque(tmp34._args)
            # State 114397
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 114398
                if len(subjects35) >= 1:
                    tmp37 = subjects35.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp37)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114399
                        if len(subjects35) == 0:
                            pass
                            # State 114400
                            if len(subjects) == 0:
                                pass
                                # 3: atanh(x*a)
                                yield 3, subst2
                    subjects35.appendleft(tmp37)
                if len(subjects35) >= 1:
                    tmp39 = subjects35.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp39)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143664
                        if len(subjects35) == 0:
                            pass
                            # State 143665
                            if len(subjects) == 0:
                                pass
                                # 19: atanh(x*a)
                                yield 19, subst2
                    subjects35.appendleft(tmp39)
                if len(subjects35) >= 1:
                    tmp41 = subjects35.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp41)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143688
                        if len(subjects35) == 0:
                            pass
                            # State 143689
                            if len(subjects) == 0:
                                pass
                                # 20: atanh(x*a)
                                yield 20, subst2
                    subjects35.appendleft(tmp41)
                if len(subjects35) >= 1 and isinstance(subjects35[0], Add):
                    tmp43 = subjects35.popleft()
                    associative1 = tmp43
                    associative_type1 = type(tmp43)
                    subjects44 = deque(tmp43._args)
                    matcher = CommutativeMatcher143855.get()
                    tmp45 = subjects44
                    subjects44 = []
                    for s in tmp45:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp45, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 143861
                            if len(subjects35) == 0:
                                pass
                                # State 143862
                                if len(subjects) == 0:
                                    pass
                                    # 21: atanh(c*(x*b + a))
                                    yield 21, subst2
                        if pattern_index == 1:
                            pass
                            # State 143901
                            if len(subjects35) == 0:
                                pass
                                # State 143902
                                if len(subjects) == 0:
                                    pass
                                    # 22: atanh(c*(x*b + a))
                                    yield 22, subst2
                    subjects35.appendleft(tmp43)
                if len(subjects35) >= 1 and isinstance(subjects35[0], Pow):
                    tmp46 = subjects35.popleft()
                    subjects47 = deque(tmp46._args)
                    # State 144109
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 144110
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 144111
                            if len(subjects47) >= 1:
                                tmp50 = subjects47.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2.1.0', tmp50)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 144112
                                    if len(subjects47) >= 1 and subjects47[0] == Integer(-1):
                                        tmp52 = subjects47.popleft()
                                        # State 144113
                                        if len(subjects47) == 0:
                                            pass
                                            # State 144114
                                            if len(subjects35) == 0:
                                                pass
                                                # State 144115
                                                if len(subjects) == 0:
                                                    pass
                                                    # 24: atanh(c/(a + x*b))
                                                    yield 24, subst4
                                        subjects47.appendleft(tmp52)
                                subjects47.appendleft(tmp50)
                        if len(subjects47) >= 1 and isinstance(subjects47[0], Mul):
                            tmp53 = subjects47.popleft()
                            associative1 = tmp53
                            associative_type1 = type(tmp53)
                            subjects54 = deque(tmp53._args)
                            matcher = CommutativeMatcher144117.get()
                            tmp55 = subjects54
                            subjects54 = []
                            for s in tmp55:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp55, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 144118
                                    if len(subjects47) >= 1 and subjects47[0] == Integer(-1):
                                        tmp56 = subjects47.popleft()
                                        # State 144119
                                        if len(subjects47) == 0:
                                            pass
                                            # State 144120
                                            if len(subjects35) == 0:
                                                pass
                                                # State 144121
                                                if len(subjects) == 0:
                                                    pass
                                                    # 24: atanh(c/(a + x*b))
                                                    yield 24, subst3
                                        subjects47.appendleft(tmp56)
                            subjects47.appendleft(tmp53)
                    if len(subjects47) >= 1 and isinstance(subjects47[0], Add):
                        tmp57 = subjects47.popleft()
                        associative1 = tmp57
                        associative_type1 = type(tmp57)
                        subjects58 = deque(tmp57._args)
                        matcher = CommutativeMatcher144123.get()
                        tmp59 = subjects58
                        subjects58 = []
                        for s in tmp59:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp59, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 144129
                                if len(subjects47) >= 1 and subjects47[0] == Integer(-1):
                                    tmp60 = subjects47.popleft()
                                    # State 144130
                                    if len(subjects47) == 0:
                                        pass
                                        # State 144131
                                        if len(subjects35) == 0:
                                            pass
                                            # State 144132
                                            if len(subjects) == 0:
                                                pass
                                                # 24: atanh(c/(a + x*b))
                                                yield 24, subst2
                                    subjects47.appendleft(tmp60)
                        subjects47.appendleft(tmp57)
                    subjects35.appendleft(tmp46)
            if len(subjects35) >= 1 and isinstance(subjects35[0], Mul):
                tmp61 = subjects35.popleft()
                associative1 = tmp61
                associative_type1 = type(tmp61)
                subjects62 = deque(tmp61._args)
                matcher = CommutativeMatcher114402.get()
                tmp63 = subjects62
                subjects62 = []
                for s in tmp63:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp63, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 114403
                        if len(subjects35) == 0:
                            pass
                            # State 114404
                            if len(subjects) == 0:
                                pass
                                # 3: atanh(x*a)
                                yield 3, subst1
                    if pattern_index == 1:
                        pass
                        # State 143666
                        if len(subjects35) == 0:
                            pass
                            # State 143667
                            if len(subjects) == 0:
                                pass
                                # 19: atanh(x*a)
                                yield 19, subst1
                    if pattern_index == 2:
                        pass
                        # State 143690
                        if len(subjects35) == 0:
                            pass
                            # State 143691
                            if len(subjects) == 0:
                                pass
                                # 20: atanh(x*a)
                                yield 20, subst1
                    if pattern_index == 3:
                        pass
                        # State 143871
                        if len(subjects35) == 0:
                            pass
                            # State 143872
                            if len(subjects) == 0:
                                pass
                                # 21: atanh(c*(x*b + a))
                                yield 21, subst1
                    if pattern_index == 4:
                        pass
                        # State 143906
                        if len(subjects35) == 0:
                            pass
                            # State 143907
                            if len(subjects) == 0:
                                pass
                                # 22: atanh(c*(x*b + a))
                                yield 22, subst1
                    if pattern_index == 5:
                        pass
                        # State 144154
                        if len(subjects35) == 0:
                            pass
                            # State 144155
                            if len(subjects) == 0:
                                pass
                                # 24: atanh(c/(a + x*b))
                                yield 24, subst1
                subjects35.appendleft(tmp61)
            if len(subjects35) >= 1 and isinstance(subjects35[0], Add):
                tmp64 = subjects35.popleft()
                associative1 = tmp64
                associative_type1 = type(tmp64)
                subjects65 = deque(tmp64._args)
                matcher = CommutativeMatcher143924.get()
                tmp66 = subjects65
                subjects65 = []
                for s in tmp66:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp66, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 143930
                        if len(subjects35) == 0:
                            pass
                            # State 143931
                            if len(subjects) == 0:
                                pass
                                # 23: atanh(x*b + a)
                                yield 23, subst1
                subjects35.appendleft(tmp64)
            subjects.appendleft(tmp34)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp67 = subjects.popleft()
            subjects68 = deque(tmp67._args)
            # State 114879
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 114880
                if len(subjects68) >= 1:
                    tmp70 = subjects68.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.0', tmp70)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114881
                        if len(subjects68) == 0:
                            pass
                            # State 114882
                            if len(subjects) == 0:
                                pass
                                # 8: acot(x*a)
                                yield 8, subst2
                    subjects68.appendleft(tmp70)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 114904
                if len(subjects68) >= 1:
                    tmp73 = subjects68.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp73)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114905
                        if len(subjects68) == 0:
                            pass
                            # State 114906
                            if len(subjects) == 0:
                                pass
                                # 9: acot(x*a)
                                yield 9, subst2
                    subjects68.appendleft(tmp73)
                if len(subjects68) >= 1:
                    tmp75 = subjects68.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp75)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114959
                        if len(subjects68) == 0:
                            pass
                            # State 114960
                            if len(subjects) == 0:
                                pass
                                # 10: acot(x*a)
                                yield 10, subst2
                    subjects68.appendleft(tmp75)
                if len(subjects68) >= 1:
                    tmp77 = subjects68.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp77)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114977
                        if len(subjects68) == 0:
                            pass
                            # State 114978
                            if len(subjects) == 0:
                                pass
                                # 11: acot(x*a)
                                yield 11, subst2
                    subjects68.appendleft(tmp77)
                if len(subjects68) >= 1 and isinstance(subjects68[0], Add):
                    tmp79 = subjects68.popleft()
                    associative1 = tmp79
                    associative_type1 = type(tmp79)
                    subjects80 = deque(tmp79._args)
                    matcher = CommutativeMatcher115068.get()
                    tmp81 = subjects80
                    subjects80 = []
                    for s in tmp81:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp81, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 115074
                            if len(subjects68) == 0:
                                pass
                                # State 115075
                                if len(subjects) == 0:
                                    pass
                                    # 12: acot(c*(a + x*b))
                                    yield 12, subst2
                    subjects68.appendleft(tmp79)
                if len(subjects68) >= 1 and isinstance(subjects68[0], Pow):
                    tmp82 = subjects68.popleft()
                    subjects83 = deque(tmp82._args)
                    # State 115400
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 115401
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 115402
                            if len(subjects83) >= 1:
                                tmp86 = subjects83.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2.1.0', tmp86)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 115403
                                    if len(subjects83) >= 1 and subjects83[0] == Integer(-1):
                                        tmp88 = subjects83.popleft()
                                        # State 115404
                                        if len(subjects83) == 0:
                                            pass
                                            # State 115405
                                            if len(subjects68) == 0:
                                                pass
                                                # State 115406
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: acot(c/(a + x*b))
                                                    yield 16, subst4
                                        subjects83.appendleft(tmp88)
                                subjects83.appendleft(tmp86)
                        if len(subjects83) >= 1 and isinstance(subjects83[0], Mul):
                            tmp89 = subjects83.popleft()
                            associative1 = tmp89
                            associative_type1 = type(tmp89)
                            subjects90 = deque(tmp89._args)
                            matcher = CommutativeMatcher115408.get()
                            tmp91 = subjects90
                            subjects90 = []
                            for s in tmp91:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp91, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 115409
                                    if len(subjects83) >= 1 and subjects83[0] == Integer(-1):
                                        tmp92 = subjects83.popleft()
                                        # State 115410
                                        if len(subjects83) == 0:
                                            pass
                                            # State 115411
                                            if len(subjects68) == 0:
                                                pass
                                                # State 115412
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: acot(c/(a + x*b))
                                                    yield 16, subst3
                                        subjects83.appendleft(tmp92)
                            subjects83.appendleft(tmp89)
                    if len(subjects83) >= 1 and isinstance(subjects83[0], Add):
                        tmp93 = subjects83.popleft()
                        associative1 = tmp93
                        associative_type1 = type(tmp93)
                        subjects94 = deque(tmp93._args)
                        matcher = CommutativeMatcher115414.get()
                        tmp95 = subjects94
                        subjects94 = []
                        for s in tmp95:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp95, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 115420
                                if len(subjects83) >= 1 and subjects83[0] == Integer(-1):
                                    tmp96 = subjects83.popleft()
                                    # State 115421
                                    if len(subjects83) == 0:
                                        pass
                                        # State 115422
                                        if len(subjects68) == 0:
                                            pass
                                            # State 115423
                                            if len(subjects) == 0:
                                                pass
                                                # 16: acot(c/(a + x*b))
                                                yield 16, subst2
                                    subjects83.appendleft(tmp96)
                        subjects83.appendleft(tmp93)
                    subjects68.appendleft(tmp82)
            if len(subjects68) >= 1 and isinstance(subjects68[0], Mul):
                tmp97 = subjects68.popleft()
                associative1 = tmp97
                associative_type1 = type(tmp97)
                subjects98 = deque(tmp97._args)
                matcher = CommutativeMatcher114884.get()
                tmp99 = subjects98
                subjects98 = []
                for s in tmp99:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp99, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 114885
                        if len(subjects68) == 0:
                            pass
                            # State 114886
                            if len(subjects) == 0:
                                pass
                                # 8: acot(x*a)
                                yield 8, subst1
                    if pattern_index == 1:
                        pass
                        # State 114907
                        if len(subjects68) == 0:
                            pass
                            # State 114908
                            if len(subjects) == 0:
                                pass
                                # 9: acot(x*a)
                                yield 9, subst1
                    if pattern_index == 2:
                        pass
                        # State 114961
                        if len(subjects68) == 0:
                            pass
                            # State 114962
                            if len(subjects) == 0:
                                pass
                                # 10: acot(x*a)
                                yield 10, subst1
                    if pattern_index == 3:
                        pass
                        # State 114979
                        if len(subjects68) == 0:
                            pass
                            # State 114980
                            if len(subjects) == 0:
                                pass
                                # 11: acot(x*a)
                                yield 11, subst1
                    if pattern_index == 4:
                        pass
                        # State 115084
                        if len(subjects68) == 0:
                            pass
                            # State 115085
                            if len(subjects) == 0:
                                pass
                                # 12: acot(c*(a + x*b))
                                yield 12, subst1
                    if pattern_index == 5:
                        pass
                        # State 115445
                        if len(subjects68) == 0:
                            pass
                            # State 115446
                            if len(subjects) == 0:
                                pass
                                # 16: acot(c/(a + x*b))
                                yield 16, subst1
                subjects68.appendleft(tmp97)
            if len(subjects68) >= 1 and isinstance(subjects68[0], Add):
                tmp100 = subjects68.popleft()
                associative1 = tmp100
                associative_type1 = type(tmp100)
                subjects101 = deque(tmp100._args)
                matcher = CommutativeMatcher115219.get()
                tmp102 = subjects101
                subjects101 = []
                for s in tmp102:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp102, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115225
                        if len(subjects68) == 0:
                            pass
                            # State 115226
                            if len(subjects) == 0:
                                pass
                                # 15: acot(x*b + a)
                                yield 15, subst1
                subjects68.appendleft(tmp100)
            subjects.appendleft(tmp67)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp103 = subjects.popleft()
            subjects104 = deque(tmp103._args)
            # State 115141
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 115142
                if len(subjects104) >= 1 and isinstance(subjects104[0], Add):
                    tmp106 = subjects104.popleft()
                    associative1 = tmp106
                    associative_type1 = type(tmp106)
                    subjects107 = deque(tmp106._args)
                    matcher = CommutativeMatcher115144.get()
                    tmp108 = subjects107
                    subjects107 = []
                    for s in tmp108:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp108, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 115150
                            if len(subjects104) == 0:
                                pass
                                # State 115151
                                if len(subjects) == 0:
                                    pass
                                    # 13: acoth(c*(x*b + a))
                                    yield 13, subst2
                        if pattern_index == 1:
                            pass
                            # State 115196
                            if len(subjects104) == 0:
                                pass
                                # State 115197
                                if len(subjects) == 0:
                                    pass
                                    # 14: acoth(c*(x*b + a))
                                    yield 14, subst2
                        if pattern_index == 2:
                            pass
                            # State 144364
                            if len(subjects104) == 0:
                                pass
                                # State 144365
                                if len(subjects) == 0:
                                    pass
                                    # 29: acoth(c*(a + x*b))
                                    yield 29, subst2
                    subjects104.appendleft(tmp106)
                if len(subjects104) >= 1:
                    tmp109 = subjects104.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp109)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 144215
                        if len(subjects104) == 0:
                            pass
                            # State 144216
                            if len(subjects) == 0:
                                pass
                                # 26: acoth(x*a)
                                yield 26, subst2
                    subjects104.appendleft(tmp109)
                if len(subjects104) >= 1:
                    tmp111 = subjects104.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp111)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 144245
                        if len(subjects104) == 0:
                            pass
                            # State 144246
                            if len(subjects) == 0:
                                pass
                                # 27: acoth(x*a)
                                yield 27, subst2
                    subjects104.appendleft(tmp111)
                if len(subjects104) >= 1:
                    tmp113 = subjects104.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp113)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 144266
                        if len(subjects104) == 0:
                            pass
                            # State 144267
                            if len(subjects) == 0:
                                pass
                                # 28: acoth(x*a)
                                yield 28, subst2
                    subjects104.appendleft(tmp113)
                if len(subjects104) >= 1 and isinstance(subjects104[0], Pow):
                    tmp115 = subjects104.popleft()
                    subjects116 = deque(tmp115._args)
                    # State 144625
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 144626
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 144627
                            if len(subjects116) >= 1:
                                tmp119 = subjects116.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2.1.0', tmp119)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 144628
                                    if len(subjects116) >= 1 and subjects116[0] == Integer(-1):
                                        tmp121 = subjects116.popleft()
                                        # State 144629
                                        if len(subjects116) == 0:
                                            pass
                                            # State 144630
                                            if len(subjects104) == 0:
                                                pass
                                                # State 144631
                                                if len(subjects) == 0:
                                                    pass
                                                    # 31: acoth(c/(a + x*b))
                                                    yield 31, subst4
                                        subjects116.appendleft(tmp121)
                                subjects116.appendleft(tmp119)
                        if len(subjects116) >= 1 and isinstance(subjects116[0], Mul):
                            tmp122 = subjects116.popleft()
                            associative1 = tmp122
                            associative_type1 = type(tmp122)
                            subjects123 = deque(tmp122._args)
                            matcher = CommutativeMatcher144633.get()
                            tmp124 = subjects123
                            subjects123 = []
                            for s in tmp124:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp124, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 144634
                                    if len(subjects116) >= 1 and subjects116[0] == Integer(-1):
                                        tmp125 = subjects116.popleft()
                                        # State 144635
                                        if len(subjects116) == 0:
                                            pass
                                            # State 144636
                                            if len(subjects104) == 0:
                                                pass
                                                # State 144637
                                                if len(subjects) == 0:
                                                    pass
                                                    # 31: acoth(c/(a + x*b))
                                                    yield 31, subst3
                                        subjects116.appendleft(tmp125)
                            subjects116.appendleft(tmp122)
                    if len(subjects116) >= 1 and isinstance(subjects116[0], Add):
                        tmp126 = subjects116.popleft()
                        associative1 = tmp126
                        associative_type1 = type(tmp126)
                        subjects127 = deque(tmp126._args)
                        matcher = CommutativeMatcher144639.get()
                        tmp128 = subjects127
                        subjects127 = []
                        for s in tmp128:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp128, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 144645
                                if len(subjects116) >= 1 and subjects116[0] == Integer(-1):
                                    tmp129 = subjects116.popleft()
                                    # State 144646
                                    if len(subjects116) == 0:
                                        pass
                                        # State 144647
                                        if len(subjects104) == 0:
                                            pass
                                            # State 144648
                                            if len(subjects) == 0:
                                                pass
                                                # 31: acoth(c/(a + x*b))
                                                yield 31, subst2
                                    subjects116.appendleft(tmp129)
                        subjects116.appendleft(tmp126)
                    subjects104.appendleft(tmp115)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 144173
                if len(subjects104) >= 1:
                    tmp131 = subjects104.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.0', tmp131)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 144174
                        if len(subjects104) == 0:
                            pass
                            # State 144175
                            if len(subjects) == 0:
                                pass
                                # 25: acoth(x*a)
                                yield 25, subst2
                    subjects104.appendleft(tmp131)
            if len(subjects104) >= 1 and isinstance(subjects104[0], Mul):
                tmp133 = subjects104.popleft()
                associative1 = tmp133
                associative_type1 = type(tmp133)
                subjects134 = deque(tmp133._args)
                matcher = CommutativeMatcher115153.get()
                tmp135 = subjects134
                subjects134 = []
                for s in tmp135:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp135, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 115162
                        if len(subjects104) == 0:
                            pass
                            # State 115163
                            if len(subjects) == 0:
                                pass
                                # 13: acoth(c*(x*b + a))
                                yield 13, subst1
                    if pattern_index == 1:
                        pass
                        # State 115201
                        if len(subjects104) == 0:
                            pass
                            # State 115202
                            if len(subjects) == 0:
                                pass
                                # 14: acoth(c*(x*b + a))
                                yield 14, subst1
                    if pattern_index == 2:
                        pass
                        # State 144176
                        if len(subjects104) == 0:
                            pass
                            # State 144177
                            if len(subjects) == 0:
                                pass
                                # 25: acoth(x*a)
                                yield 25, subst1
                    if pattern_index == 3:
                        pass
                        # State 144217
                        if len(subjects104) == 0:
                            pass
                            # State 144218
                            if len(subjects) == 0:
                                pass
                                # 26: acoth(x*a)
                                yield 26, subst1
                    if pattern_index == 4:
                        pass
                        # State 144247
                        if len(subjects104) == 0:
                            pass
                            # State 144248
                            if len(subjects) == 0:
                                pass
                                # 27: acoth(x*a)
                                yield 27, subst1
                    if pattern_index == 5:
                        pass
                        # State 144268
                        if len(subjects104) == 0:
                            pass
                            # State 144269
                            if len(subjects) == 0:
                                pass
                                # 28: acoth(x*a)
                                yield 28, subst1
                    if pattern_index == 6:
                        pass
                        # State 144370
                        if len(subjects104) == 0:
                            pass
                            # State 144371
                            if len(subjects) == 0:
                                pass
                                # 29: acoth(c*(a + x*b))
                                yield 29, subst1
                    if pattern_index == 7:
                        pass
                        # State 144670
                        if len(subjects104) == 0:
                            pass
                            # State 144671
                            if len(subjects) == 0:
                                pass
                                # 31: acoth(c/(a + x*b))
                                yield 31, subst1
                subjects104.appendleft(tmp133)
            if len(subjects104) >= 1 and isinstance(subjects104[0], Add):
                tmp136 = subjects104.popleft()
                associative1 = tmp136
                associative_type1 = type(tmp136)
                subjects137 = deque(tmp136._args)
                matcher = CommutativeMatcher144444.get()
                tmp138 = subjects137
                subjects137 = []
                for s in tmp138:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp138, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144450
                        if len(subjects104) == 0:
                            pass
                            # State 144451
                            if len(subjects) == 0:
                                pass
                                # 30: acoth(x*b + a)
                                yield 30, subst1
                subjects104.appendleft(tmp136)
            subjects.appendleft(tmp103)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp139 = subjects.popleft()
            subjects140 = deque(tmp139._args)
            # State 142189
            if len(subjects140) >= 1:
                tmp141 = subjects140.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1', tmp141)
                except ValueError:
                    pass
                else:
                    pass
                    # State 142190
                    if len(subjects140) == 0:
                        pass
                        # State 142191
                        if len(subjects) == 0:
                            pass
                            # 17: asinh(u)
                            yield 17, subst1
                subjects140.appendleft(tmp141)
            subjects.appendleft(tmp139)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp143 = subjects.popleft()
            subjects144 = deque(tmp143._args)
            # State 142214
            if len(subjects144) >= 1:
                tmp145 = subjects144.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1', tmp145)
                except ValueError:
                    pass
                else:
                    pass
                    # State 142215
                    if len(subjects144) == 0:
                        pass
                        # State 142216
                        if len(subjects) == 0:
                            pass
                            # 18: acosh(u)
                            yield 18, subst1
                subjects144.appendleft(tmp145)
            subjects.appendleft(tmp143)
        if len(subjects) >= 1 and isinstance(subjects[0], asech):
            tmp147 = subjects.popleft()
            subjects148 = deque(tmp147._args)
            # State 150467
            if len(subjects148) >= 1:
                tmp149 = subjects148.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1', tmp149)
                except ValueError:
                    pass
                else:
                    pass
                    # State 150468
                    if len(subjects148) == 0:
                        pass
                        # State 150469
                        if len(subjects) == 0:
                            pass
                            # 32: asech(u)
                            yield 32, subst1
                subjects148.appendleft(tmp149)
            subjects.appendleft(tmp147)
        if len(subjects) >= 1 and isinstance(subjects[0], acsch):
            tmp151 = subjects.popleft()
            subjects152 = deque(tmp151._args)
            # State 150479
            if len(subjects152) >= 1:
                tmp153 = subjects152.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1', tmp153)
                except ValueError:
                    pass
                else:
                    pass
                    # State 150480
                    if len(subjects152) == 0:
                        pass
                        # State 150481
                        if len(subjects) == 0:
                            pass
                            # 33: acsch(u)
                            yield 33, subst1
                subjects152.appendleft(tmp153)
            subjects.appendleft(tmp151)
        return
        yield


from .generated_part006816 import *
from .generated_part006857 import *
from .generated_part006844 import *
from .generated_part006831 import *
from .generated_part006824 import *
from .generated_part006850 import *
from .generated_part006855 import *
from .generated_part006837 import *
from .generated_part006813 import *
from .generated_part006828 import *
from .generated_part006854 import *
from .generated_part006839 import *
from collections import deque
from .generated_part006842 import *
from .generated_part006815 import *
from .generated_part006863 import *
from matchpy.utils import VariableWithCount
from .generated_part006829 import *
from .generated_part006841 import *
from .generated_part006818 import *
from .generated_part006852 import *
from multiset import Multiset
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part006826 import *