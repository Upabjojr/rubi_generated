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


class CommutativeMatcher14697(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.3.0_2', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({3: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({4: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({5: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({6: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({7: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({8: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({9: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({10: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({11: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({12: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({13: 1}), [
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
        if CommutativeMatcher14697._instance is None:
            CommutativeMatcher14697._instance = CommutativeMatcher14697()
        return CommutativeMatcher14697._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 14696
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 14698
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 14699
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.0', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 14700
                        if len(subjects) == 0:
                            pass
                            # 0: x*f + e
                            yield 0, subst3
                    subjects.appendleft(tmp3)
                if len(subjects) >= 1:
                    tmp5 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.0', tmp5)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 16942
                        if len(subjects) == 0:
                            pass
                            # 1: x*b + a
                            yield 1, subst3
                    subjects.appendleft(tmp5)
                if len(subjects) >= 1:
                    tmp7 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.3.1.1.0', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17943
                        if len(subjects) == 0:
                            pass
                            # 2: x*g + f
                            yield 2, subst3
                    subjects.appendleft(tmp7)
                if len(subjects) >= 1:
                    tmp9 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.4.1.0', tmp9)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 103952
                        if len(subjects) == 0:
                            pass
                            # 6: a + b*x
                            yield 6, subst3
                    subjects.appendleft(tmp9)
                if len(subjects) >= 1:
                    tmp11 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', tmp11)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 104000
                        if len(subjects) == 0:
                            pass
                            # 7: x*b + a
                            yield 7, subst3
                    subjects.appendleft(tmp11)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 101404
                if len(subjects) >= 1:
                    tmp14 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.1.0', tmp14)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101405
                        if len(subjects) == 0:
                            pass
                            # 4: a + x*b
                            yield 4, subst3
                    subjects.appendleft(tmp14)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp16 = subjects.popleft()
                associative1 = tmp16
                associative_type1 = type(tmp16)
                subjects17 = deque(tmp16._args)
                matcher = CommutativeMatcher14702.get()
                tmp18 = subjects17
                subjects17 = []
                for s in tmp18:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp18, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 14703
                        if len(subjects) == 0:
                            pass
                            # 0: x*f + e
                            yield 0, subst2
                    if pattern_index == 1:
                        pass
                        # State 16943
                        if len(subjects) == 0:
                            pass
                            # 1: x*b + a
                            yield 1, subst2
                    if pattern_index == 2:
                        pass
                        # State 17944
                        if len(subjects) == 0:
                            pass
                            # 2: x*g + f
                            yield 2, subst2
                    if pattern_index == 3:
                        pass
                        # State 101406
                        if len(subjects) == 0:
                            pass
                            # 4: a + x*b
                            yield 4, subst2
                    if pattern_index == 4:
                        pass
                        # State 103953
                        if len(subjects) == 0:
                            pass
                            # 6: a + b*x
                            yield 6, subst2
                    if pattern_index == 5:
                        pass
                        # State 104001
                        if len(subjects) == 0:
                            pass
                            # 7: x*b + a
                            yield 7, subst2
                subjects.appendleft(tmp16)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 18207
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 18208
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.3.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 18209
                    if len(subjects) >= 1:
                        tmp22 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.1', tmp22)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18210
                            if len(subjects) == 0:
                                pass
                                # 3: (x*e + d)**n
                                yield 3, subst4
                        subjects.appendleft(tmp22)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp24 = subjects.popleft()
                    associative1 = tmp24
                    associative_type1 = type(tmp24)
                    subjects25 = deque(tmp24._args)
                    matcher = CommutativeMatcher18212.get()
                    tmp26 = subjects25
                    subjects25 = []
                    for s in tmp26:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp26, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 18213
                            if len(subjects) == 0:
                                pass
                                # 3: (x*e + d)**n
                                yield 3, subst3
                    subjects.appendleft(tmp24)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp27 = subjects.popleft()
                associative1 = tmp27
                associative_type1 = type(tmp27)
                subjects28 = deque(tmp27._args)
                matcher = CommutativeMatcher18215.get()
                tmp29 = subjects28
                subjects28 = []
                for s in tmp29:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp29, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 18221
                        if len(subjects) == 0:
                            pass
                            # 3: (x*e + d)**n
                            yield 3, subst2
                subjects.appendleft(tmp27)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_2', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 103879
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 103880
                if len(subjects) >= 1:
                    tmp32 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.0', tmp32)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 103881
                        if len(subjects) == 0:
                            pass
                            # 5: x*b + a
                            yield 5, subst3
                    subjects.appendleft(tmp32)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp34 = subjects.popleft()
                associative1 = tmp34
                associative_type1 = type(tmp34)
                subjects35 = deque(tmp34._args)
                matcher = CommutativeMatcher103883.get()
                tmp36 = subjects35
                subjects35 = []
                for s in tmp36:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp36, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 103884
                        if len(subjects) == 0:
                            pass
                            # 5: x*b + a
                            yield 5, subst2
                subjects.appendleft(tmp34)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 112187
            if len(subjects) >= 1 and isinstance(subjects[0], asin):
                tmp38 = subjects.popleft()
                subjects39 = deque(tmp38._args)
                # State 112188
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 112189
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112190
                        if len(subjects39) >= 1:
                            tmp42 = subjects39.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.3.1.0', tmp42)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 112191
                                if len(subjects39) == 0:
                                    pass
                                    # State 112192
                                    if len(subjects) == 0:
                                        pass
                                        # 8: asin(a + x*b)**n
                                        yield 8, subst4
                            subjects39.appendleft(tmp42)
                    if len(subjects39) >= 1 and isinstance(subjects39[0], Mul):
                        tmp44 = subjects39.popleft()
                        associative1 = tmp44
                        associative_type1 = type(tmp44)
                        subjects45 = deque(tmp44._args)
                        matcher = CommutativeMatcher112194.get()
                        tmp46 = subjects45
                        subjects45 = []
                        for s in tmp46:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp46, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 112195
                                if len(subjects39) == 0:
                                    pass
                                    # State 112196
                                    if len(subjects) == 0:
                                        pass
                                        # 8: asin(a + x*b)**n
                                        yield 8, subst3
                        subjects39.appendleft(tmp44)
                if len(subjects39) >= 1 and isinstance(subjects39[0], Add):
                    tmp47 = subjects39.popleft()
                    associative1 = tmp47
                    associative_type1 = type(tmp47)
                    subjects48 = deque(tmp47._args)
                    matcher = CommutativeMatcher112198.get()
                    tmp49 = subjects48
                    subjects48 = []
                    for s in tmp49:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp49, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 112204
                            if len(subjects39) == 0:
                                pass
                                # State 112205
                                if len(subjects) == 0:
                                    pass
                                    # 8: asin(a + x*b)**n
                                    yield 8, subst2
                    subjects39.appendleft(tmp47)
                subjects.appendleft(tmp38)
            if len(subjects) >= 1 and isinstance(subjects[0], acos):
                tmp50 = subjects.popleft()
                subjects51 = deque(tmp50._args)
                # State 112389
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 112390
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112391
                        if len(subjects51) >= 1:
                            tmp54 = subjects51.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.3.1.0', tmp54)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 112392
                                if len(subjects51) == 0:
                                    pass
                                    # State 112393
                                    if len(subjects) == 0:
                                        pass
                                        # 9: acos(a + x*b)**n
                                        yield 9, subst4
                            subjects51.appendleft(tmp54)
                    if len(subjects51) >= 1 and isinstance(subjects51[0], Mul):
                        tmp56 = subjects51.popleft()
                        associative1 = tmp56
                        associative_type1 = type(tmp56)
                        subjects57 = deque(tmp56._args)
                        matcher = CommutativeMatcher112395.get()
                        tmp58 = subjects57
                        subjects57 = []
                        for s in tmp58:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp58, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 112396
                                if len(subjects51) == 0:
                                    pass
                                    # State 112397
                                    if len(subjects) == 0:
                                        pass
                                        # 9: acos(a + x*b)**n
                                        yield 9, subst3
                        subjects51.appendleft(tmp56)
                if len(subjects51) >= 1 and isinstance(subjects51[0], Add):
                    tmp59 = subjects51.popleft()
                    associative1 = tmp59
                    associative_type1 = type(tmp59)
                    subjects60 = deque(tmp59._args)
                    matcher = CommutativeMatcher112399.get()
                    tmp61 = subjects60
                    subjects60 = []
                    for s in tmp61:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp61, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 112405
                            if len(subjects51) == 0:
                                pass
                                # State 112406
                                if len(subjects) == 0:
                                    pass
                                    # 9: acos(a + x*b)**n
                                    yield 9, subst2
                    subjects51.appendleft(tmp59)
                subjects.appendleft(tmp50)
            if len(subjects) >= 1 and isinstance(subjects[0], asec):
                tmp62 = subjects.popleft()
                subjects63 = deque(tmp62._args)
                # State 121299
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 121300
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 121301
                        if len(subjects63) >= 1:
                            tmp66 = subjects63.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.3.1.0', tmp66)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 121302
                                if len(subjects63) == 0:
                                    pass
                                    # State 121303
                                    if len(subjects) == 0:
                                        pass
                                        # 10: asec(a + x*b)**n
                                        yield 10, subst4
                            subjects63.appendleft(tmp66)
                    if len(subjects63) >= 1 and isinstance(subjects63[0], Mul):
                        tmp68 = subjects63.popleft()
                        associative1 = tmp68
                        associative_type1 = type(tmp68)
                        subjects69 = deque(tmp68._args)
                        matcher = CommutativeMatcher121305.get()
                        tmp70 = subjects69
                        subjects69 = []
                        for s in tmp70:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp70, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 121306
                                if len(subjects63) == 0:
                                    pass
                                    # State 121307
                                    if len(subjects) == 0:
                                        pass
                                        # 10: asec(a + x*b)**n
                                        yield 10, subst3
                        subjects63.appendleft(tmp68)
                if len(subjects63) >= 1 and isinstance(subjects63[0], Add):
                    tmp71 = subjects63.popleft()
                    associative1 = tmp71
                    associative_type1 = type(tmp71)
                    subjects72 = deque(tmp71._args)
                    matcher = CommutativeMatcher121309.get()
                    tmp73 = subjects72
                    subjects72 = []
                    for s in tmp73:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp73, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 121315
                            if len(subjects63) == 0:
                                pass
                                # State 121316
                                if len(subjects) == 0:
                                    pass
                                    # 10: asec(a + x*b)**n
                                    yield 10, subst2
                    subjects63.appendleft(tmp71)
                subjects.appendleft(tmp62)
            if len(subjects) >= 1 and isinstance(subjects[0], acsc):
                tmp74 = subjects.popleft()
                subjects75 = deque(tmp74._args)
                # State 121500
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 121501
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 121502
                        if len(subjects75) >= 1:
                            tmp78 = subjects75.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.3.1.0', tmp78)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 121503
                                if len(subjects75) == 0:
                                    pass
                                    # State 121504
                                    if len(subjects) == 0:
                                        pass
                                        # 11: acsc(a + x*b)**n
                                        yield 11, subst4
                            subjects75.appendleft(tmp78)
                    if len(subjects75) >= 1 and isinstance(subjects75[0], Mul):
                        tmp80 = subjects75.popleft()
                        associative1 = tmp80
                        associative_type1 = type(tmp80)
                        subjects81 = deque(tmp80._args)
                        matcher = CommutativeMatcher121506.get()
                        tmp82 = subjects81
                        subjects81 = []
                        for s in tmp82:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp82, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 121507
                                if len(subjects75) == 0:
                                    pass
                                    # State 121508
                                    if len(subjects) == 0:
                                        pass
                                        # 11: acsc(a + x*b)**n
                                        yield 11, subst3
                        subjects75.appendleft(tmp80)
                if len(subjects75) >= 1 and isinstance(subjects75[0], Add):
                    tmp83 = subjects75.popleft()
                    associative1 = tmp83
                    associative_type1 = type(tmp83)
                    subjects84 = deque(tmp83._args)
                    matcher = CommutativeMatcher121510.get()
                    tmp85 = subjects84
                    subjects84 = []
                    for s in tmp85:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp85, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 121516
                            if len(subjects75) == 0:
                                pass
                                # State 121517
                                if len(subjects) == 0:
                                    pass
                                    # 11: acsc(a + x*b)**n
                                    yield 11, subst2
                    subjects75.appendleft(tmp83)
                subjects.appendleft(tmp74)
            if len(subjects) >= 1 and isinstance(subjects[0], asinh):
                tmp86 = subjects.popleft()
                subjects87 = deque(tmp86._args)
                # State 141982
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 141983
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 141984
                        if len(subjects87) >= 1:
                            tmp90 = subjects87.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.3.1.0', tmp90)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 141985
                                if len(subjects87) == 0:
                                    pass
                                    # State 141986
                                    if len(subjects) == 0:
                                        pass
                                        # 12: asinh(a + x*b)**n
                                        yield 12, subst4
                            subjects87.appendleft(tmp90)
                    if len(subjects87) >= 1 and isinstance(subjects87[0], Mul):
                        tmp92 = subjects87.popleft()
                        associative1 = tmp92
                        associative_type1 = type(tmp92)
                        subjects93 = deque(tmp92._args)
                        matcher = CommutativeMatcher141988.get()
                        tmp94 = subjects93
                        subjects93 = []
                        for s in tmp94:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp94, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 141989
                                if len(subjects87) == 0:
                                    pass
                                    # State 141990
                                    if len(subjects) == 0:
                                        pass
                                        # 12: asinh(a + x*b)**n
                                        yield 12, subst3
                        subjects87.appendleft(tmp92)
                if len(subjects87) >= 1 and isinstance(subjects87[0], Add):
                    tmp95 = subjects87.popleft()
                    associative1 = tmp95
                    associative_type1 = type(tmp95)
                    subjects96 = deque(tmp95._args)
                    matcher = CommutativeMatcher141992.get()
                    tmp97 = subjects96
                    subjects96 = []
                    for s in tmp97:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp97, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 141998
                            if len(subjects87) == 0:
                                pass
                                # State 141999
                                if len(subjects) == 0:
                                    pass
                                    # 12: asinh(a + x*b)**n
                                    yield 12, subst2
                    subjects87.appendleft(tmp95)
                subjects.appendleft(tmp86)
            if len(subjects) >= 1 and isinstance(subjects[0], acosh):
                tmp98 = subjects.popleft()
                subjects99 = deque(tmp98._args)
                # State 142081
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 142082
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142083
                        if len(subjects99) >= 1:
                            tmp102 = subjects99.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.3.1.0', tmp102)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 142084
                                if len(subjects99) == 0:
                                    pass
                                    # State 142085
                                    if len(subjects) == 0:
                                        pass
                                        # 13: acosh(a + x*b)**n
                                        yield 13, subst4
                            subjects99.appendleft(tmp102)
                    if len(subjects99) >= 1 and isinstance(subjects99[0], Mul):
                        tmp104 = subjects99.popleft()
                        associative1 = tmp104
                        associative_type1 = type(tmp104)
                        subjects105 = deque(tmp104._args)
                        matcher = CommutativeMatcher142087.get()
                        tmp106 = subjects105
                        subjects105 = []
                        for s in tmp106:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp106, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 142088
                                if len(subjects99) == 0:
                                    pass
                                    # State 142089
                                    if len(subjects) == 0:
                                        pass
                                        # 13: acosh(a + x*b)**n
                                        yield 13, subst3
                        subjects99.appendleft(tmp104)
                if len(subjects99) >= 1 and isinstance(subjects99[0], Add):
                    tmp107 = subjects99.popleft()
                    associative1 = tmp107
                    associative_type1 = type(tmp107)
                    subjects108 = deque(tmp107._args)
                    matcher = CommutativeMatcher142091.get()
                    tmp109 = subjects108
                    subjects108 = []
                    for s in tmp109:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp109, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 142097
                            if len(subjects99) == 0:
                                pass
                                # State 142098
                                if len(subjects) == 0:
                                    pass
                                    # 13: acosh(a + x*b)**n
                                    yield 13, subst2
                    subjects99.appendleft(tmp107)
                subjects.appendleft(tmp98)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp110 = subjects.popleft()
            associative1 = tmp110
            associative_type1 = type(tmp110)
            subjects111 = deque(tmp110._args)
            matcher = CommutativeMatcher14705.get()
            tmp112 = subjects111
            subjects111 = []
            for s in tmp112:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp112, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 14711
                    if len(subjects) == 0:
                        pass
                        # 0: x*f + e
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 16946
                    if len(subjects) == 0:
                        pass
                        # 1: x*b + a
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 17947
                    if len(subjects) == 0:
                        pass
                        # 2: x*g + f
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 101410
                    if len(subjects) == 0:
                        pass
                        # 4: a + x*b
                        yield 4, subst1
                if pattern_index == 4:
                    pass
                    # State 103887
                    if len(subjects) == 0:
                        pass
                        # 5: x*b + a
                        yield 5, subst1
                if pattern_index == 5:
                    pass
                    # State 103956
                    if len(subjects) == 0:
                        pass
                        # 6: a + b*x
                        yield 6, subst1
                if pattern_index == 6:
                    pass
                    # State 104004
                    if len(subjects) == 0:
                        pass
                        # 7: x*b + a
                        yield 7, subst1
            subjects.appendleft(tmp110)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp113 = subjects.popleft()
            subjects114 = deque(tmp113._args)
            # State 18222
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 18223
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 18224
                    if len(subjects114) >= 1:
                        tmp117 = subjects114.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp117)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18225
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 18226
                                if len(subjects114) == 0:
                                    pass
                                    # State 18227
                                    if len(subjects) == 0:
                                        pass
                                        # 3: (x*e + d)**n
                                        yield 3, subst4
                            if len(subjects114) >= 1:
                                tmp120 = subjects114.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2', tmp120)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18226
                                    if len(subjects114) == 0:
                                        pass
                                        # State 18227
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (x*e + d)**n
                                            yield 3, subst4
                                subjects114.appendleft(tmp120)
                        subjects114.appendleft(tmp117)
                if len(subjects114) >= 1 and isinstance(subjects114[0], Mul):
                    tmp122 = subjects114.popleft()
                    associative1 = tmp122
                    associative_type1 = type(tmp122)
                    subjects123 = deque(tmp122._args)
                    matcher = CommutativeMatcher18229.get()
                    tmp124 = subjects123
                    subjects123 = []
                    for s in tmp124:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp124, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 18230
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 18231
                                if len(subjects114) == 0:
                                    pass
                                    # State 18232
                                    if len(subjects) == 0:
                                        pass
                                        # 3: (x*e + d)**n
                                        yield 3, subst3
                            if len(subjects114) >= 1:
                                tmp126 = []
                                tmp126.append(subjects114.popleft())
                                while True:
                                    if len(tmp126) > 1:
                                        tmp127 = create_operation_expression(associative1, tmp126)
                                    elif len(tmp126) == 1:
                                        tmp127 = tmp126[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2', tmp127)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 18231
                                        if len(subjects114) == 0:
                                            pass
                                            # State 18232
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (x*e + d)**n
                                                yield 3, subst3
                                    if len(subjects114) == 0:
                                        break
                                    tmp126.append(subjects114.popleft())
                                subjects114.extendleft(reversed(tmp126))
                    subjects114.appendleft(tmp122)
            if len(subjects114) >= 1 and isinstance(subjects114[0], Add):
                tmp129 = subjects114.popleft()
                associative1 = tmp129
                associative_type1 = type(tmp129)
                subjects130 = deque(tmp129._args)
                matcher = CommutativeMatcher18234.get()
                tmp131 = subjects130
                subjects130 = []
                for s in tmp131:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp131, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 18240
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18241
                            if len(subjects114) == 0:
                                pass
                                # State 18242
                                if len(subjects) == 0:
                                    pass
                                    # 3: (x*e + d)**n
                                    yield 3, subst2
                        if len(subjects114) >= 1:
                            tmp133 = []
                            tmp133.append(subjects114.popleft())
                            while True:
                                if len(tmp133) > 1:
                                    tmp134 = create_operation_expression(associative1, tmp133)
                                elif len(tmp133) == 1:
                                    tmp134 = tmp133[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp134)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18241
                                    if len(subjects114) == 0:
                                        pass
                                        # State 18242
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (x*e + d)**n
                                            yield 3, subst2
                                if len(subjects114) == 0:
                                    break
                                tmp133.append(subjects114.popleft())
                            subjects114.extendleft(reversed(tmp133))
                subjects114.appendleft(tmp129)
            if len(subjects114) >= 1 and isinstance(subjects114[0], asin):
                tmp136 = subjects114.popleft()
                subjects137 = deque(tmp136._args)
                # State 112206
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 112207
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112208
                        if len(subjects137) >= 1:
                            tmp140 = subjects137.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.3.1.0', tmp140)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 112209
                                if len(subjects137) == 0:
                                    pass
                                    # State 112210
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 112211
                                        if len(subjects114) == 0:
                                            pass
                                            # State 112212
                                            if len(subjects) == 0:
                                                pass
                                                # 8: asin(a + x*b)**n
                                                yield 8, subst4
                                    if len(subjects114) >= 1:
                                        tmp143 = subjects114.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.3', tmp143)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 112211
                                            if len(subjects114) == 0:
                                                pass
                                                # State 112212
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: asin(a + x*b)**n
                                                    yield 8, subst4
                                        subjects114.appendleft(tmp143)
                            subjects137.appendleft(tmp140)
                    if len(subjects137) >= 1 and isinstance(subjects137[0], Mul):
                        tmp145 = subjects137.popleft()
                        associative1 = tmp145
                        associative_type1 = type(tmp145)
                        subjects146 = deque(tmp145._args)
                        matcher = CommutativeMatcher112214.get()
                        tmp147 = subjects146
                        subjects146 = []
                        for s in tmp147:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp147, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 112215
                                if len(subjects137) == 0:
                                    pass
                                    # State 112216
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 112217
                                        if len(subjects114) == 0:
                                            pass
                                            # State 112218
                                            if len(subjects) == 0:
                                                pass
                                                # 8: asin(a + x*b)**n
                                                yield 8, subst3
                                    if len(subjects114) >= 1:
                                        tmp149 = subjects114.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.3.3', tmp149)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 112217
                                            if len(subjects114) == 0:
                                                pass
                                                # State 112218
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: asin(a + x*b)**n
                                                    yield 8, subst3
                                        subjects114.appendleft(tmp149)
                        subjects137.appendleft(tmp145)
                if len(subjects137) >= 1 and isinstance(subjects137[0], Add):
                    tmp151 = subjects137.popleft()
                    associative1 = tmp151
                    associative_type1 = type(tmp151)
                    subjects152 = deque(tmp151._args)
                    matcher = CommutativeMatcher112220.get()
                    tmp153 = subjects152
                    subjects152 = []
                    for s in tmp153:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp153, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 112226
                            if len(subjects137) == 0:
                                pass
                                # State 112227
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 112228
                                    if len(subjects114) == 0:
                                        pass
                                        # State 112229
                                        if len(subjects) == 0:
                                            pass
                                            # 8: asin(a + x*b)**n
                                            yield 8, subst2
                                if len(subjects114) >= 1:
                                    tmp155 = subjects114.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.3.3', tmp155)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 112228
                                        if len(subjects114) == 0:
                                            pass
                                            # State 112229
                                            if len(subjects) == 0:
                                                pass
                                                # 8: asin(a + x*b)**n
                                                yield 8, subst2
                                    subjects114.appendleft(tmp155)
                    subjects137.appendleft(tmp151)
                subjects114.appendleft(tmp136)
            if len(subjects114) >= 1 and isinstance(subjects114[0], acos):
                tmp157 = subjects114.popleft()
                subjects158 = deque(tmp157._args)
                # State 112407
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 112408
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112409
                        if len(subjects158) >= 1:
                            tmp161 = subjects158.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.3.1.0', tmp161)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 112410
                                if len(subjects158) == 0:
                                    pass
                                    # State 112411
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 112412
                                        if len(subjects114) == 0:
                                            pass
                                            # State 112413
                                            if len(subjects) == 0:
                                                pass
                                                # 9: acos(a + x*b)**n
                                                yield 9, subst4
                                    if len(subjects114) >= 1:
                                        tmp164 = subjects114.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.3', tmp164)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 112412
                                            if len(subjects114) == 0:
                                                pass
                                                # State 112413
                                                if len(subjects) == 0:
                                                    pass
                                                    # 9: acos(a + x*b)**n
                                                    yield 9, subst4
                                        subjects114.appendleft(tmp164)
                            subjects158.appendleft(tmp161)
                    if len(subjects158) >= 1 and isinstance(subjects158[0], Mul):
                        tmp166 = subjects158.popleft()
                        associative1 = tmp166
                        associative_type1 = type(tmp166)
                        subjects167 = deque(tmp166._args)
                        matcher = CommutativeMatcher112415.get()
                        tmp168 = subjects167
                        subjects167 = []
                        for s in tmp168:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp168, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 112416
                                if len(subjects158) == 0:
                                    pass
                                    # State 112417
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 112418
                                        if len(subjects114) == 0:
                                            pass
                                            # State 112419
                                            if len(subjects) == 0:
                                                pass
                                                # 9: acos(a + x*b)**n
                                                yield 9, subst3
                                    if len(subjects114) >= 1:
                                        tmp170 = subjects114.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.3.3', tmp170)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 112418
                                            if len(subjects114) == 0:
                                                pass
                                                # State 112419
                                                if len(subjects) == 0:
                                                    pass
                                                    # 9: acos(a + x*b)**n
                                                    yield 9, subst3
                                        subjects114.appendleft(tmp170)
                        subjects158.appendleft(tmp166)
                if len(subjects158) >= 1 and isinstance(subjects158[0], Add):
                    tmp172 = subjects158.popleft()
                    associative1 = tmp172
                    associative_type1 = type(tmp172)
                    subjects173 = deque(tmp172._args)
                    matcher = CommutativeMatcher112421.get()
                    tmp174 = subjects173
                    subjects173 = []
                    for s in tmp174:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp174, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 112427
                            if len(subjects158) == 0:
                                pass
                                # State 112428
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 112429
                                    if len(subjects114) == 0:
                                        pass
                                        # State 112430
                                        if len(subjects) == 0:
                                            pass
                                            # 9: acos(a + x*b)**n
                                            yield 9, subst2
                                if len(subjects114) >= 1:
                                    tmp176 = subjects114.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.3.3', tmp176)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 112429
                                        if len(subjects114) == 0:
                                            pass
                                            # State 112430
                                            if len(subjects) == 0:
                                                pass
                                                # 9: acos(a + x*b)**n
                                                yield 9, subst2
                                    subjects114.appendleft(tmp176)
                    subjects158.appendleft(tmp172)
                subjects114.appendleft(tmp157)
            if len(subjects114) >= 1 and isinstance(subjects114[0], asec):
                tmp178 = subjects114.popleft()
                subjects179 = deque(tmp178._args)
                # State 121317
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 121318
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 121319
                        if len(subjects179) >= 1:
                            tmp182 = subjects179.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.3.1.0', tmp182)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 121320
                                if len(subjects179) == 0:
                                    pass
                                    # State 121321
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 121322
                                        if len(subjects114) == 0:
                                            pass
                                            # State 121323
                                            if len(subjects) == 0:
                                                pass
                                                # 10: asec(a + x*b)**n
                                                yield 10, subst4
                                    if len(subjects114) >= 1:
                                        tmp185 = subjects114.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.3', tmp185)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 121322
                                            if len(subjects114) == 0:
                                                pass
                                                # State 121323
                                                if len(subjects) == 0:
                                                    pass
                                                    # 10: asec(a + x*b)**n
                                                    yield 10, subst4
                                        subjects114.appendleft(tmp185)
                            subjects179.appendleft(tmp182)
                    if len(subjects179) >= 1 and isinstance(subjects179[0], Mul):
                        tmp187 = subjects179.popleft()
                        associative1 = tmp187
                        associative_type1 = type(tmp187)
                        subjects188 = deque(tmp187._args)
                        matcher = CommutativeMatcher121325.get()
                        tmp189 = subjects188
                        subjects188 = []
                        for s in tmp189:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp189, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 121326
                                if len(subjects179) == 0:
                                    pass
                                    # State 121327
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 121328
                                        if len(subjects114) == 0:
                                            pass
                                            # State 121329
                                            if len(subjects) == 0:
                                                pass
                                                # 10: asec(a + x*b)**n
                                                yield 10, subst3
                                    if len(subjects114) >= 1:
                                        tmp191 = subjects114.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.3.3', tmp191)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 121328
                                            if len(subjects114) == 0:
                                                pass
                                                # State 121329
                                                if len(subjects) == 0:
                                                    pass
                                                    # 10: asec(a + x*b)**n
                                                    yield 10, subst3
                                        subjects114.appendleft(tmp191)
                        subjects179.appendleft(tmp187)
                if len(subjects179) >= 1 and isinstance(subjects179[0], Add):
                    tmp193 = subjects179.popleft()
                    associative1 = tmp193
                    associative_type1 = type(tmp193)
                    subjects194 = deque(tmp193._args)
                    matcher = CommutativeMatcher121331.get()
                    tmp195 = subjects194
                    subjects194 = []
                    for s in tmp195:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp195, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 121337
                            if len(subjects179) == 0:
                                pass
                                # State 121338
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 121339
                                    if len(subjects114) == 0:
                                        pass
                                        # State 121340
                                        if len(subjects) == 0:
                                            pass
                                            # 10: asec(a + x*b)**n
                                            yield 10, subst2
                                if len(subjects114) >= 1:
                                    tmp197 = subjects114.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.3.3', tmp197)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 121339
                                        if len(subjects114) == 0:
                                            pass
                                            # State 121340
                                            if len(subjects) == 0:
                                                pass
                                                # 10: asec(a + x*b)**n
                                                yield 10, subst2
                                    subjects114.appendleft(tmp197)
                    subjects179.appendleft(tmp193)
                subjects114.appendleft(tmp178)
            if len(subjects114) >= 1 and isinstance(subjects114[0], acsc):
                tmp199 = subjects114.popleft()
                subjects200 = deque(tmp199._args)
                # State 121518
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 121519
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 121520
                        if len(subjects200) >= 1:
                            tmp203 = subjects200.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.3.1.0', tmp203)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 121521
                                if len(subjects200) == 0:
                                    pass
                                    # State 121522
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 121523
                                        if len(subjects114) == 0:
                                            pass
                                            # State 121524
                                            if len(subjects) == 0:
                                                pass
                                                # 11: acsc(a + x*b)**n
                                                yield 11, subst4
                                    if len(subjects114) >= 1:
                                        tmp206 = subjects114.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.3', tmp206)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 121523
                                            if len(subjects114) == 0:
                                                pass
                                                # State 121524
                                                if len(subjects) == 0:
                                                    pass
                                                    # 11: acsc(a + x*b)**n
                                                    yield 11, subst4
                                        subjects114.appendleft(tmp206)
                            subjects200.appendleft(tmp203)
                    if len(subjects200) >= 1 and isinstance(subjects200[0], Mul):
                        tmp208 = subjects200.popleft()
                        associative1 = tmp208
                        associative_type1 = type(tmp208)
                        subjects209 = deque(tmp208._args)
                        matcher = CommutativeMatcher121526.get()
                        tmp210 = subjects209
                        subjects209 = []
                        for s in tmp210:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp210, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 121527
                                if len(subjects200) == 0:
                                    pass
                                    # State 121528
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 121529
                                        if len(subjects114) == 0:
                                            pass
                                            # State 121530
                                            if len(subjects) == 0:
                                                pass
                                                # 11: acsc(a + x*b)**n
                                                yield 11, subst3
                                    if len(subjects114) >= 1:
                                        tmp212 = subjects114.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.3.3', tmp212)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 121529
                                            if len(subjects114) == 0:
                                                pass
                                                # State 121530
                                                if len(subjects) == 0:
                                                    pass
                                                    # 11: acsc(a + x*b)**n
                                                    yield 11, subst3
                                        subjects114.appendleft(tmp212)
                        subjects200.appendleft(tmp208)
                if len(subjects200) >= 1 and isinstance(subjects200[0], Add):
                    tmp214 = subjects200.popleft()
                    associative1 = tmp214
                    associative_type1 = type(tmp214)
                    subjects215 = deque(tmp214._args)
                    matcher = CommutativeMatcher121532.get()
                    tmp216 = subjects215
                    subjects215 = []
                    for s in tmp216:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp216, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 121538
                            if len(subjects200) == 0:
                                pass
                                # State 121539
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 121540
                                    if len(subjects114) == 0:
                                        pass
                                        # State 121541
                                        if len(subjects) == 0:
                                            pass
                                            # 11: acsc(a + x*b)**n
                                            yield 11, subst2
                                if len(subjects114) >= 1:
                                    tmp218 = subjects114.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.3.3', tmp218)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 121540
                                        if len(subjects114) == 0:
                                            pass
                                            # State 121541
                                            if len(subjects) == 0:
                                                pass
                                                # 11: acsc(a + x*b)**n
                                                yield 11, subst2
                                    subjects114.appendleft(tmp218)
                    subjects200.appendleft(tmp214)
                subjects114.appendleft(tmp199)
            if len(subjects114) >= 1 and isinstance(subjects114[0], asinh):
                tmp220 = subjects114.popleft()
                subjects221 = deque(tmp220._args)
                # State 142000
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 142001
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142002
                        if len(subjects221) >= 1:
                            tmp224 = subjects221.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.3.1.0', tmp224)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 142003
                                if len(subjects221) == 0:
                                    pass
                                    # State 142004
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 142005
                                        if len(subjects114) == 0:
                                            pass
                                            # State 142006
                                            if len(subjects) == 0:
                                                pass
                                                # 12: asinh(a + x*b)**n
                                                yield 12, subst4
                                    if len(subjects114) >= 1:
                                        tmp227 = subjects114.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.3', tmp227)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 142005
                                            if len(subjects114) == 0:
                                                pass
                                                # State 142006
                                                if len(subjects) == 0:
                                                    pass
                                                    # 12: asinh(a + x*b)**n
                                                    yield 12, subst4
                                        subjects114.appendleft(tmp227)
                            subjects221.appendleft(tmp224)
                    if len(subjects221) >= 1 and isinstance(subjects221[0], Mul):
                        tmp229 = subjects221.popleft()
                        associative1 = tmp229
                        associative_type1 = type(tmp229)
                        subjects230 = deque(tmp229._args)
                        matcher = CommutativeMatcher142008.get()
                        tmp231 = subjects230
                        subjects230 = []
                        for s in tmp231:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp231, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 142009
                                if len(subjects221) == 0:
                                    pass
                                    # State 142010
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 142011
                                        if len(subjects114) == 0:
                                            pass
                                            # State 142012
                                            if len(subjects) == 0:
                                                pass
                                                # 12: asinh(a + x*b)**n
                                                yield 12, subst3
                                    if len(subjects114) >= 1:
                                        tmp233 = subjects114.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.3.3', tmp233)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 142011
                                            if len(subjects114) == 0:
                                                pass
                                                # State 142012
                                                if len(subjects) == 0:
                                                    pass
                                                    # 12: asinh(a + x*b)**n
                                                    yield 12, subst3
                                        subjects114.appendleft(tmp233)
                        subjects221.appendleft(tmp229)
                if len(subjects221) >= 1 and isinstance(subjects221[0], Add):
                    tmp235 = subjects221.popleft()
                    associative1 = tmp235
                    associative_type1 = type(tmp235)
                    subjects236 = deque(tmp235._args)
                    matcher = CommutativeMatcher142014.get()
                    tmp237 = subjects236
                    subjects236 = []
                    for s in tmp237:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp237, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 142020
                            if len(subjects221) == 0:
                                pass
                                # State 142021
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 142022
                                    if len(subjects114) == 0:
                                        pass
                                        # State 142023
                                        if len(subjects) == 0:
                                            pass
                                            # 12: asinh(a + x*b)**n
                                            yield 12, subst2
                                if len(subjects114) >= 1:
                                    tmp239 = subjects114.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.3.3', tmp239)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 142022
                                        if len(subjects114) == 0:
                                            pass
                                            # State 142023
                                            if len(subjects) == 0:
                                                pass
                                                # 12: asinh(a + x*b)**n
                                                yield 12, subst2
                                    subjects114.appendleft(tmp239)
                    subjects221.appendleft(tmp235)
                subjects114.appendleft(tmp220)
            if len(subjects114) >= 1 and isinstance(subjects114[0], acosh):
                tmp241 = subjects114.popleft()
                subjects242 = deque(tmp241._args)
                # State 142099
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 142100
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142101
                        if len(subjects242) >= 1:
                            tmp245 = subjects242.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.3.1.0', tmp245)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 142102
                                if len(subjects242) == 0:
                                    pass
                                    # State 142103
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 142104
                                        if len(subjects114) == 0:
                                            pass
                                            # State 142105
                                            if len(subjects) == 0:
                                                pass
                                                # 13: acosh(a + x*b)**n
                                                yield 13, subst4
                                    if len(subjects114) >= 1:
                                        tmp248 = subjects114.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.3', tmp248)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 142104
                                            if len(subjects114) == 0:
                                                pass
                                                # State 142105
                                                if len(subjects) == 0:
                                                    pass
                                                    # 13: acosh(a + x*b)**n
                                                    yield 13, subst4
                                        subjects114.appendleft(tmp248)
                            subjects242.appendleft(tmp245)
                    if len(subjects242) >= 1 and isinstance(subjects242[0], Mul):
                        tmp250 = subjects242.popleft()
                        associative1 = tmp250
                        associative_type1 = type(tmp250)
                        subjects251 = deque(tmp250._args)
                        matcher = CommutativeMatcher142107.get()
                        tmp252 = subjects251
                        subjects251 = []
                        for s in tmp252:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp252, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 142108
                                if len(subjects242) == 0:
                                    pass
                                    # State 142109
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 142110
                                        if len(subjects114) == 0:
                                            pass
                                            # State 142111
                                            if len(subjects) == 0:
                                                pass
                                                # 13: acosh(a + x*b)**n
                                                yield 13, subst3
                                    if len(subjects114) >= 1:
                                        tmp254 = subjects114.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.3.3', tmp254)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 142110
                                            if len(subjects114) == 0:
                                                pass
                                                # State 142111
                                                if len(subjects) == 0:
                                                    pass
                                                    # 13: acosh(a + x*b)**n
                                                    yield 13, subst3
                                        subjects114.appendleft(tmp254)
                        subjects242.appendleft(tmp250)
                if len(subjects242) >= 1 and isinstance(subjects242[0], Add):
                    tmp256 = subjects242.popleft()
                    associative1 = tmp256
                    associative_type1 = type(tmp256)
                    subjects257 = deque(tmp256._args)
                    matcher = CommutativeMatcher142113.get()
                    tmp258 = subjects257
                    subjects257 = []
                    for s in tmp258:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp258, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 142119
                            if len(subjects242) == 0:
                                pass
                                # State 142120
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 142121
                                    if len(subjects114) == 0:
                                        pass
                                        # State 142122
                                        if len(subjects) == 0:
                                            pass
                                            # 13: acosh(a + x*b)**n
                                            yield 13, subst2
                                if len(subjects114) >= 1:
                                    tmp260 = subjects114.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.3.3', tmp260)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 142121
                                        if len(subjects114) == 0:
                                            pass
                                            # State 142122
                                            if len(subjects) == 0:
                                                pass
                                                # 13: acosh(a + x*b)**n
                                                yield 13, subst2
                                    subjects114.appendleft(tmp260)
                    subjects242.appendleft(tmp256)
                subjects114.appendleft(tmp241)
            subjects.appendleft(tmp113)
        return
        yield


from .generated_part005951 import *
from .generated_part005983 import *
from .generated_part005987 import *
from .generated_part005989 import *
from .generated_part005947 import *
from .generated_part005946 import *
from .generated_part005963 import *
from .generated_part005980 import *
from .generated_part005952 import *
from .generated_part005957 import *
from collections import deque
from .generated_part005960 import *
from .generated_part005977 import *
from matchpy.utils import VariableWithCount
from .generated_part005967 import *
from .generated_part005948 import *
from .generated_part005955 import *
from .generated_part005986 import *
from .generated_part005978 import *
from .generated_part005990 import *
from .generated_part005975 import *
from .generated_part005981 import *
from multiset import Multiset
from .generated_part005961 import *
from .generated_part005971 import *
from .generated_part005969 import *
from .generated_part005972 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part005954 import *
from .generated_part005964 import *
from .generated_part005984 import *
from .generated_part005974 import *
from .generated_part005958 import *
from .generated_part005966 import *
from .generated_part005950 import *