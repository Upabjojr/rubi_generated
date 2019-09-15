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


class CommutativeMatcher10249(CommutativeMatcher):
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
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({10: 1}), [
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
        if CommutativeMatcher10249._instance is None:
            CommutativeMatcher10249._instance = CommutativeMatcher10249()
        return CommutativeMatcher10249._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 10248
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 10250
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 10251
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10252
                            if len(subjects2) == 0:
                                pass
                                # State 10253
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                        tmp7 = subjects2.popleft()
                        # State 10719
                        if len(subjects2) == 0:
                            pass
                            # State 10720
                            if len(subjects) == 0:
                                pass
                                # 1: 1/x
                                yield 1, subst1
                        subjects2.appendleft(tmp7)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp8 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 10855
                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                        tmp10 = subjects2.popleft()
                        # State 10856
                        if len(subjects2) == 0:
                            pass
                            # State 10857
                            if len(subjects) == 0:
                                pass
                                # 2: 1/x
                                yield 2, subst1
                        subjects2.appendleft(tmp10)
                subjects2.appendleft(tmp8)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp11 = subjects2.popleft()
                subjects12 = deque(tmp11._args)
                # State 82557
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 82558
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 82559
                        if len(subjects12) >= 1:
                            tmp15 = subjects12.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.3.1.0', tmp15)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 82560
                                if len(subjects12) == 0:
                                    pass
                                    # State 82561
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp17 = subjects2.popleft()
                                        # State 82562
                                        if len(subjects2) == 0:
                                            pass
                                            # State 82563
                                            if len(subjects) == 0:
                                                pass
                                                # 8: 1/tan(c + x*d)
                                                yield 8, subst3
                                        subjects2.appendleft(tmp17)
                            subjects12.appendleft(tmp15)
                    if len(subjects12) >= 1 and isinstance(subjects12[0], Mul):
                        tmp18 = subjects12.popleft()
                        associative1 = tmp18
                        associative_type1 = type(tmp18)
                        subjects19 = deque(tmp18._args)
                        matcher = CommutativeMatcher82565.get()
                        tmp20 = subjects19
                        subjects19 = []
                        for s in tmp20:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp20, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 82566
                                if len(subjects12) == 0:
                                    pass
                                    # State 82567
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp21 = subjects2.popleft()
                                        # State 82568
                                        if len(subjects2) == 0:
                                            pass
                                            # State 82569
                                            if len(subjects) == 0:
                                                pass
                                                # 8: 1/tan(c + x*d)
                                                yield 8, subst2
                                        subjects2.appendleft(tmp21)
                        subjects12.appendleft(tmp18)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 83161
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 83162
                        if len(subjects12) >= 1:
                            tmp24 = subjects12.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.0', tmp24)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 83163
                                if len(subjects12) == 0:
                                    pass
                                    # State 83164
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp26 = subjects2.popleft()
                                        # State 83165
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83166
                                            if len(subjects) == 0:
                                                pass
                                                # 10: 1/tan(e + x*f)
                                                yield 10, subst3
                                        subjects2.appendleft(tmp26)
                            subjects12.appendleft(tmp24)
                    if len(subjects12) >= 1 and isinstance(subjects12[0], Mul):
                        tmp27 = subjects12.popleft()
                        associative1 = tmp27
                        associative_type1 = type(tmp27)
                        subjects28 = deque(tmp27._args)
                        matcher = CommutativeMatcher83168.get()
                        tmp29 = subjects28
                        subjects28 = []
                        for s in tmp29:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp29, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 83169
                                if len(subjects12) == 0:
                                    pass
                                    # State 83170
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp30 = subjects2.popleft()
                                        # State 83171
                                        if len(subjects2) == 0:
                                            pass
                                            # State 83172
                                            if len(subjects) == 0:
                                                pass
                                                # 10: 1/tan(e + x*f)
                                                yield 10, subst2
                                        subjects2.appendleft(tmp30)
                        subjects12.appendleft(tmp27)
                if len(subjects12) >= 1 and isinstance(subjects12[0], Add):
                    tmp31 = subjects12.popleft()
                    associative1 = tmp31
                    associative_type1 = type(tmp31)
                    subjects32 = deque(tmp31._args)
                    matcher = CommutativeMatcher82571.get()
                    tmp33 = subjects32
                    subjects32 = []
                    for s in tmp33:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp33, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 82577
                            if len(subjects12) == 0:
                                pass
                                # State 82578
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp34 = subjects2.popleft()
                                    # State 82579
                                    if len(subjects2) == 0:
                                        pass
                                        # State 82580
                                        if len(subjects) == 0:
                                            pass
                                            # 8: 1/tan(c + x*d)
                                            yield 8, subst1
                                    subjects2.appendleft(tmp34)
                        if pattern_index == 1:
                            pass
                            # State 83176
                            if len(subjects12) == 0:
                                pass
                                # State 83177
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp35 = subjects2.popleft()
                                    # State 83178
                                    if len(subjects2) == 0:
                                        pass
                                        # State 83179
                                        if len(subjects) == 0:
                                            pass
                                            # 10: 1/tan(e + x*f)
                                            yield 10, subst1
                                    subjects2.appendleft(tmp35)
                    subjects12.appendleft(tmp31)
                subjects2.appendleft(tmp11)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp36 = subjects.popleft()
            subjects37 = deque(tmp36._args)
            # State 68150
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 68151
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68152
                    if len(subjects37) >= 1:
                        tmp40 = subjects37.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp40)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68153
                            if len(subjects37) == 0:
                                pass
                                # State 68154
                                if len(subjects) == 0:
                                    pass
                                    # 3: sin(c + x*d)
                                    yield 3, subst3
                        subjects37.appendleft(tmp40)
                if len(subjects37) >= 1 and isinstance(subjects37[0], Mul):
                    tmp42 = subjects37.popleft()
                    associative1 = tmp42
                    associative_type1 = type(tmp42)
                    subjects43 = deque(tmp42._args)
                    matcher = CommutativeMatcher68156.get()
                    tmp44 = subjects43
                    subjects43 = []
                    for s in tmp44:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp44, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 68157
                            if len(subjects37) == 0:
                                pass
                                # State 68158
                                if len(subjects) == 0:
                                    pass
                                    # 3: sin(c + x*d)
                                    yield 3, subst2
                    subjects37.appendleft(tmp42)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 71481
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 71482
                    if len(subjects37) >= 1:
                        tmp47 = subjects37.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp47)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 71483
                            if len(subjects37) == 0:
                                pass
                                # State 71484
                                if len(subjects) == 0:
                                    pass
                                    # 6: sin(e + x*f)
                                    yield 6, subst3
                        subjects37.appendleft(tmp47)
                if len(subjects37) >= 1 and isinstance(subjects37[0], Mul):
                    tmp49 = subjects37.popleft()
                    associative1 = tmp49
                    associative_type1 = type(tmp49)
                    subjects50 = deque(tmp49._args)
                    matcher = CommutativeMatcher71486.get()
                    tmp51 = subjects50
                    subjects50 = []
                    for s in tmp51:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp51, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 71487
                            if len(subjects37) == 0:
                                pass
                                # State 71488
                                if len(subjects) == 0:
                                    pass
                                    # 6: sin(e + x*f)
                                    yield 6, subst2
                    subjects37.appendleft(tmp49)
            if len(subjects37) >= 1 and isinstance(subjects37[0], Add):
                tmp52 = subjects37.popleft()
                associative1 = tmp52
                associative_type1 = type(tmp52)
                subjects53 = deque(tmp52._args)
                matcher = CommutativeMatcher68160.get()
                tmp54 = subjects53
                subjects53 = []
                for s in tmp54:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp54, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 68166
                        if len(subjects37) == 0:
                            pass
                            # State 68167
                            if len(subjects) == 0:
                                pass
                                # 3: sin(c + x*d)
                                yield 3, subst1
                    if pattern_index == 1:
                        pass
                        # State 71492
                        if len(subjects37) == 0:
                            pass
                            # State 71493
                            if len(subjects) == 0:
                                pass
                                # 6: sin(e + x*f)
                                yield 6, subst1
                subjects37.appendleft(tmp52)
            subjects.appendleft(tmp36)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp55 = subjects.popleft()
            subjects56 = deque(tmp55._args)
            # State 68371
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 68372
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68373
                    if len(subjects56) >= 1:
                        tmp59 = subjects56.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp59)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68374
                            if len(subjects56) == 0:
                                pass
                                # State 68375
                                if len(subjects) == 0:
                                    pass
                                    # 4: cos(c + x*d)
                                    yield 4, subst3
                        subjects56.appendleft(tmp59)
                if len(subjects56) >= 1 and isinstance(subjects56[0], Mul):
                    tmp61 = subjects56.popleft()
                    associative1 = tmp61
                    associative_type1 = type(tmp61)
                    subjects62 = deque(tmp61._args)
                    matcher = CommutativeMatcher68377.get()
                    tmp63 = subjects62
                    subjects62 = []
                    for s in tmp63:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp63, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 68378
                            if len(subjects56) == 0:
                                pass
                                # State 68379
                                if len(subjects) == 0:
                                    pass
                                    # 4: cos(c + x*d)
                                    yield 4, subst2
                    subjects56.appendleft(tmp61)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 68592
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 68593
                    if len(subjects56) >= 1:
                        tmp66 = subjects56.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp66)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 68594
                            if len(subjects56) == 0:
                                pass
                                # State 68595
                                if len(subjects) == 0:
                                    pass
                                    # 5: cos(e + x*f)
                                    yield 5, subst3
                        subjects56.appendleft(tmp66)
                if len(subjects56) >= 1 and isinstance(subjects56[0], Mul):
                    tmp68 = subjects56.popleft()
                    associative1 = tmp68
                    associative_type1 = type(tmp68)
                    subjects69 = deque(tmp68._args)
                    matcher = CommutativeMatcher68597.get()
                    tmp70 = subjects69
                    subjects69 = []
                    for s in tmp70:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp70, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 68598
                            if len(subjects56) == 0:
                                pass
                                # State 68599
                                if len(subjects) == 0:
                                    pass
                                    # 5: cos(e + x*f)
                                    yield 5, subst2
                    subjects56.appendleft(tmp68)
            if len(subjects56) >= 1 and isinstance(subjects56[0], Add):
                tmp71 = subjects56.popleft()
                associative1 = tmp71
                associative_type1 = type(tmp71)
                subjects72 = deque(tmp71._args)
                matcher = CommutativeMatcher68381.get()
                tmp73 = subjects72
                subjects72 = []
                for s in tmp73:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp73, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 68387
                        if len(subjects56) == 0:
                            pass
                            # State 68388
                            if len(subjects) == 0:
                                pass
                                # 4: cos(c + x*d)
                                yield 4, subst1
                    if pattern_index == 1:
                        pass
                        # State 68603
                        if len(subjects56) == 0:
                            pass
                            # State 68604
                            if len(subjects) == 0:
                                pass
                                # 5: cos(e + x*f)
                                yield 5, subst1
                subjects56.appendleft(tmp71)
            subjects.appendleft(tmp55)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp74 = subjects.popleft()
            subjects75 = deque(tmp74._args)
            # State 82436
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 82437
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 82438
                    if len(subjects75) >= 1:
                        tmp78 = subjects75.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1.0', tmp78)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 82439
                            if len(subjects75) == 0:
                                pass
                                # State 82440
                                if len(subjects) == 0:
                                    pass
                                    # 7: tan(c + x*d)
                                    yield 7, subst3
                        subjects75.appendleft(tmp78)
                if len(subjects75) >= 1 and isinstance(subjects75[0], Mul):
                    tmp80 = subjects75.popleft()
                    associative1 = tmp80
                    associative_type1 = type(tmp80)
                    subjects81 = deque(tmp80._args)
                    matcher = CommutativeMatcher82442.get()
                    tmp82 = subjects81
                    subjects81 = []
                    for s in tmp82:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp82, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 82443
                            if len(subjects75) == 0:
                                pass
                                # State 82444
                                if len(subjects) == 0:
                                    pass
                                    # 7: tan(c + x*d)
                                    yield 7, subst2
                    subjects75.appendleft(tmp80)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 82950
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 82951
                    if len(subjects75) >= 1:
                        tmp85 = subjects75.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp85)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 82952
                            if len(subjects75) == 0:
                                pass
                                # State 82953
                                if len(subjects) == 0:
                                    pass
                                    # 9: tan(e + x*f)
                                    yield 9, subst3
                        subjects75.appendleft(tmp85)
                if len(subjects75) >= 1 and isinstance(subjects75[0], Mul):
                    tmp87 = subjects75.popleft()
                    associative1 = tmp87
                    associative_type1 = type(tmp87)
                    subjects88 = deque(tmp87._args)
                    matcher = CommutativeMatcher82955.get()
                    tmp89 = subjects88
                    subjects88 = []
                    for s in tmp89:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp89, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 82956
                            if len(subjects75) == 0:
                                pass
                                # State 82957
                                if len(subjects) == 0:
                                    pass
                                    # 9: tan(e + x*f)
                                    yield 9, subst2
                    subjects75.appendleft(tmp87)
            if len(subjects75) >= 1 and isinstance(subjects75[0], Add):
                tmp90 = subjects75.popleft()
                associative1 = tmp90
                associative_type1 = type(tmp90)
                subjects91 = deque(tmp90._args)
                matcher = CommutativeMatcher82446.get()
                tmp92 = subjects91
                subjects91 = []
                for s in tmp92:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp92, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 82452
                        if len(subjects75) == 0:
                            pass
                            # State 82453
                            if len(subjects) == 0:
                                pass
                                # 7: tan(c + x*d)
                                yield 7, subst1
                    if pattern_index == 1:
                        pass
                        # State 82961
                        if len(subjects75) == 0:
                            pass
                            # State 82962
                            if len(subjects) == 0:
                                pass
                                # 9: tan(e + x*f)
                                yield 9, subst1
                subjects75.appendleft(tmp90)
            subjects.appendleft(tmp74)
        return
        yield


from .generated_part005224 import *
from .generated_part005226 import *
from .generated_part005222 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part005217 import *
from .generated_part005218 import *
from collections import deque
from .generated_part005220 import *
from .generated_part005221 import *
from .generated_part005225 import *
from .generated_part005213 import *
from .generated_part005212 import *
from .generated_part005214 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part005216 import *