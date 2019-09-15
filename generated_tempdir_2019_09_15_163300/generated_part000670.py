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


class CommutativeMatcher112089(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
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
        if CommutativeMatcher112089._instance is None:
            CommutativeMatcher112089._instance = CommutativeMatcher112089()
        return CommutativeMatcher112089._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 112088
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 112090
            if len(subjects) >= 1 and isinstance(subjects[0], asin):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 112091
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 112092
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112093
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.3.1.0', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 112094
                                if len(subjects3) == 0:
                                    pass
                                    # State 112095
                                    if len(subjects) == 0:
                                        pass
                                        # 0: asin(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                        yield 0, subst4
                            subjects3.appendleft(tmp6)
                    if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                        tmp8 = subjects3.popleft()
                        associative1 = tmp8
                        associative_type1 = type(tmp8)
                        subjects9 = deque(tmp8._args)
                        matcher = CommutativeMatcher112097.get()
                        tmp10 = subjects9
                        subjects9 = []
                        for s in tmp10:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp10, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 112098
                                if len(subjects3) == 0:
                                    pass
                                    # State 112099
                                    if len(subjects) == 0:
                                        pass
                                        # 0: asin(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                        yield 0, subst3
                        subjects3.appendleft(tmp8)
                if len(subjects3) >= 1 and isinstance(subjects3[0], Add):
                    tmp11 = subjects3.popleft()
                    associative1 = tmp11
                    associative_type1 = type(tmp11)
                    subjects12 = deque(tmp11._args)
                    matcher = CommutativeMatcher112101.get()
                    tmp13 = subjects12
                    subjects12 = []
                    for s in tmp13:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp13, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 112107
                            if len(subjects3) == 0:
                                pass
                                # State 112108
                                if len(subjects) == 0:
                                    pass
                                    # 0: asin(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                    yield 0, subst2
                    subjects3.appendleft(tmp11)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], acos):
                tmp14 = subjects.popleft()
                subjects15 = deque(tmp14._args)
                # State 112295
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 112296
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112297
                        if len(subjects15) >= 1:
                            tmp18 = subjects15.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.3.1.0', tmp18)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 112298
                                if len(subjects15) == 0:
                                    pass
                                    # State 112299
                                    if len(subjects) == 0:
                                        pass
                                        # 1: acos(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                        yield 1, subst4
                            subjects15.appendleft(tmp18)
                    if len(subjects15) >= 1 and isinstance(subjects15[0], Mul):
                        tmp20 = subjects15.popleft()
                        associative1 = tmp20
                        associative_type1 = type(tmp20)
                        subjects21 = deque(tmp20._args)
                        matcher = CommutativeMatcher112301.get()
                        tmp22 = subjects21
                        subjects21 = []
                        for s in tmp22:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp22, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 112302
                                if len(subjects15) == 0:
                                    pass
                                    # State 112303
                                    if len(subjects) == 0:
                                        pass
                                        # 1: acos(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                        yield 1, subst3
                        subjects15.appendleft(tmp20)
                if len(subjects15) >= 1 and isinstance(subjects15[0], Add):
                    tmp23 = subjects15.popleft()
                    associative1 = tmp23
                    associative_type1 = type(tmp23)
                    subjects24 = deque(tmp23._args)
                    matcher = CommutativeMatcher112305.get()
                    tmp25 = subjects24
                    subjects24 = []
                    for s in tmp25:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp25, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 112311
                            if len(subjects15) == 0:
                                pass
                                # State 112312
                                if len(subjects) == 0:
                                    pass
                                    # 1: acos(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                    yield 1, subst2
                    subjects15.appendleft(tmp23)
                subjects.appendleft(tmp14)
            if len(subjects) >= 1 and isinstance(subjects[0], asec):
                tmp26 = subjects.popleft()
                subjects27 = deque(tmp26._args)
                # State 121205
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 121206
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 121207
                        if len(subjects27) >= 1:
                            tmp30 = subjects27.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.3.1.0', tmp30)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 121208
                                if len(subjects27) == 0:
                                    pass
                                    # State 121209
                                    if len(subjects) == 0:
                                        pass
                                        # 2: asec(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                        yield 2, subst4
                            subjects27.appendleft(tmp30)
                    if len(subjects27) >= 1 and isinstance(subjects27[0], Mul):
                        tmp32 = subjects27.popleft()
                        associative1 = tmp32
                        associative_type1 = type(tmp32)
                        subjects33 = deque(tmp32._args)
                        matcher = CommutativeMatcher121211.get()
                        tmp34 = subjects33
                        subjects33 = []
                        for s in tmp34:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp34, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 121212
                                if len(subjects27) == 0:
                                    pass
                                    # State 121213
                                    if len(subjects) == 0:
                                        pass
                                        # 2: asec(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                        yield 2, subst3
                        subjects27.appendleft(tmp32)
                if len(subjects27) >= 1 and isinstance(subjects27[0], Add):
                    tmp35 = subjects27.popleft()
                    associative1 = tmp35
                    associative_type1 = type(tmp35)
                    subjects36 = deque(tmp35._args)
                    matcher = CommutativeMatcher121215.get()
                    tmp37 = subjects36
                    subjects36 = []
                    for s in tmp37:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp37, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 121221
                            if len(subjects27) == 0:
                                pass
                                # State 121222
                                if len(subjects) == 0:
                                    pass
                                    # 2: asec(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                    yield 2, subst2
                    subjects27.appendleft(tmp35)
                subjects.appendleft(tmp26)
            if len(subjects) >= 1 and isinstance(subjects[0], acsc):
                tmp38 = subjects.popleft()
                subjects39 = deque(tmp38._args)
                # State 121406
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 121407
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 121408
                        if len(subjects39) >= 1:
                            tmp42 = subjects39.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.3.1.0', tmp42)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 121409
                                if len(subjects39) == 0:
                                    pass
                                    # State 121410
                                    if len(subjects) == 0:
                                        pass
                                        # 3: acsc(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                        yield 3, subst4
                            subjects39.appendleft(tmp42)
                    if len(subjects39) >= 1 and isinstance(subjects39[0], Mul):
                        tmp44 = subjects39.popleft()
                        associative1 = tmp44
                        associative_type1 = type(tmp44)
                        subjects45 = deque(tmp44._args)
                        matcher = CommutativeMatcher121412.get()
                        tmp46 = subjects45
                        subjects45 = []
                        for s in tmp46:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp46, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 121413
                                if len(subjects39) == 0:
                                    pass
                                    # State 121414
                                    if len(subjects) == 0:
                                        pass
                                        # 3: acsc(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                        yield 3, subst3
                        subjects39.appendleft(tmp44)
                if len(subjects39) >= 1 and isinstance(subjects39[0], Add):
                    tmp47 = subjects39.popleft()
                    associative1 = tmp47
                    associative_type1 = type(tmp47)
                    subjects48 = deque(tmp47._args)
                    matcher = CommutativeMatcher121416.get()
                    tmp49 = subjects48
                    subjects48 = []
                    for s in tmp49:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp49, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 121422
                            if len(subjects39) == 0:
                                pass
                                # State 121423
                                if len(subjects) == 0:
                                    pass
                                    # 3: acsc(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                    yield 3, subst2
                    subjects39.appendleft(tmp47)
                subjects.appendleft(tmp38)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp50 = subjects.popleft()
            subjects51 = deque(tmp50._args)
            # State 112109
            if len(subjects51) >= 1 and isinstance(subjects51[0], asin):
                tmp52 = subjects51.popleft()
                subjects53 = deque(tmp52._args)
                # State 112110
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 112111
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112112
                        if len(subjects53) >= 1:
                            tmp56 = subjects53.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.3.1.0', tmp56)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 112113
                                if len(subjects53) == 0:
                                    pass
                                    # State 112114
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 112115
                                        if len(subjects51) == 0:
                                            pass
                                            # State 112116
                                            if len(subjects) == 0:
                                                pass
                                                # 0: asin(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 0, subst4
                                    if len(subjects51) >= 1:
                                        tmp59 = subjects51.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.3', tmp59)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 112115
                                            if len(subjects51) == 0:
                                                pass
                                                # State 112116
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: asin(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                    yield 0, subst4
                                        subjects51.appendleft(tmp59)
                            subjects53.appendleft(tmp56)
                    if len(subjects53) >= 1 and isinstance(subjects53[0], Mul):
                        tmp61 = subjects53.popleft()
                        associative1 = tmp61
                        associative_type1 = type(tmp61)
                        subjects62 = deque(tmp61._args)
                        matcher = CommutativeMatcher112118.get()
                        tmp63 = subjects62
                        subjects62 = []
                        for s in tmp63:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp63, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 112119
                                if len(subjects53) == 0:
                                    pass
                                    # State 112120
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 112121
                                        if len(subjects51) == 0:
                                            pass
                                            # State 112122
                                            if len(subjects) == 0:
                                                pass
                                                # 0: asin(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 0, subst3
                                    if len(subjects51) >= 1:
                                        tmp65 = subjects51.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.3.3', tmp65)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 112121
                                            if len(subjects51) == 0:
                                                pass
                                                # State 112122
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: asin(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                    yield 0, subst3
                                        subjects51.appendleft(tmp65)
                        subjects53.appendleft(tmp61)
                if len(subjects53) >= 1 and isinstance(subjects53[0], Add):
                    tmp67 = subjects53.popleft()
                    associative1 = tmp67
                    associative_type1 = type(tmp67)
                    subjects68 = deque(tmp67._args)
                    matcher = CommutativeMatcher112124.get()
                    tmp69 = subjects68
                    subjects68 = []
                    for s in tmp69:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp69, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 112130
                            if len(subjects53) == 0:
                                pass
                                # State 112131
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 112132
                                    if len(subjects51) == 0:
                                        pass
                                        # State 112133
                                        if len(subjects) == 0:
                                            pass
                                            # 0: asin(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                            yield 0, subst2
                                if len(subjects51) >= 1:
                                    tmp71 = subjects51.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.3.3', tmp71)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 112132
                                        if len(subjects51) == 0:
                                            pass
                                            # State 112133
                                            if len(subjects) == 0:
                                                pass
                                                # 0: asin(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 0, subst2
                                    subjects51.appendleft(tmp71)
                    subjects53.appendleft(tmp67)
                subjects51.appendleft(tmp52)
            if len(subjects51) >= 1 and isinstance(subjects51[0], acos):
                tmp73 = subjects51.popleft()
                subjects74 = deque(tmp73._args)
                # State 112313
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 112314
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112315
                        if len(subjects74) >= 1:
                            tmp77 = subjects74.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.3.1.0', tmp77)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 112316
                                if len(subjects74) == 0:
                                    pass
                                    # State 112317
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 112318
                                        if len(subjects51) == 0:
                                            pass
                                            # State 112319
                                            if len(subjects) == 0:
                                                pass
                                                # 1: acos(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 1, subst4
                                    if len(subjects51) >= 1:
                                        tmp80 = subjects51.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.3', tmp80)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 112318
                                            if len(subjects51) == 0:
                                                pass
                                                # State 112319
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: acos(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                    yield 1, subst4
                                        subjects51.appendleft(tmp80)
                            subjects74.appendleft(tmp77)
                    if len(subjects74) >= 1 and isinstance(subjects74[0], Mul):
                        tmp82 = subjects74.popleft()
                        associative1 = tmp82
                        associative_type1 = type(tmp82)
                        subjects83 = deque(tmp82._args)
                        matcher = CommutativeMatcher112321.get()
                        tmp84 = subjects83
                        subjects83 = []
                        for s in tmp84:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp84, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 112322
                                if len(subjects74) == 0:
                                    pass
                                    # State 112323
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 112324
                                        if len(subjects51) == 0:
                                            pass
                                            # State 112325
                                            if len(subjects) == 0:
                                                pass
                                                # 1: acos(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 1, subst3
                                    if len(subjects51) >= 1:
                                        tmp86 = subjects51.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.3.3', tmp86)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 112324
                                            if len(subjects51) == 0:
                                                pass
                                                # State 112325
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: acos(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                    yield 1, subst3
                                        subjects51.appendleft(tmp86)
                        subjects74.appendleft(tmp82)
                if len(subjects74) >= 1 and isinstance(subjects74[0], Add):
                    tmp88 = subjects74.popleft()
                    associative1 = tmp88
                    associative_type1 = type(tmp88)
                    subjects89 = deque(tmp88._args)
                    matcher = CommutativeMatcher112327.get()
                    tmp90 = subjects89
                    subjects89 = []
                    for s in tmp90:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp90, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 112333
                            if len(subjects74) == 0:
                                pass
                                # State 112334
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 112335
                                    if len(subjects51) == 0:
                                        pass
                                        # State 112336
                                        if len(subjects) == 0:
                                            pass
                                            # 1: acos(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                            yield 1, subst2
                                if len(subjects51) >= 1:
                                    tmp92 = subjects51.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.3.3', tmp92)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 112335
                                        if len(subjects51) == 0:
                                            pass
                                            # State 112336
                                            if len(subjects) == 0:
                                                pass
                                                # 1: acos(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 1, subst2
                                    subjects51.appendleft(tmp92)
                    subjects74.appendleft(tmp88)
                subjects51.appendleft(tmp73)
            if len(subjects51) >= 1 and isinstance(subjects51[0], asec):
                tmp94 = subjects51.popleft()
                subjects95 = deque(tmp94._args)
                # State 121223
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 121224
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 121225
                        if len(subjects95) >= 1:
                            tmp98 = subjects95.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.3.1.0', tmp98)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 121226
                                if len(subjects95) == 0:
                                    pass
                                    # State 121227
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 121228
                                        if len(subjects51) == 0:
                                            pass
                                            # State 121229
                                            if len(subjects) == 0:
                                                pass
                                                # 2: asec(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 2, subst4
                                    if len(subjects51) >= 1:
                                        tmp101 = subjects51.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.3', tmp101)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 121228
                                            if len(subjects51) == 0:
                                                pass
                                                # State 121229
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: asec(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                    yield 2, subst4
                                        subjects51.appendleft(tmp101)
                            subjects95.appendleft(tmp98)
                    if len(subjects95) >= 1 and isinstance(subjects95[0], Mul):
                        tmp103 = subjects95.popleft()
                        associative1 = tmp103
                        associative_type1 = type(tmp103)
                        subjects104 = deque(tmp103._args)
                        matcher = CommutativeMatcher121231.get()
                        tmp105 = subjects104
                        subjects104 = []
                        for s in tmp105:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp105, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 121232
                                if len(subjects95) == 0:
                                    pass
                                    # State 121233
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 121234
                                        if len(subjects51) == 0:
                                            pass
                                            # State 121235
                                            if len(subjects) == 0:
                                                pass
                                                # 2: asec(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 2, subst3
                                    if len(subjects51) >= 1:
                                        tmp107 = subjects51.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.3.3', tmp107)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 121234
                                            if len(subjects51) == 0:
                                                pass
                                                # State 121235
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: asec(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                    yield 2, subst3
                                        subjects51.appendleft(tmp107)
                        subjects95.appendleft(tmp103)
                if len(subjects95) >= 1 and isinstance(subjects95[0], Add):
                    tmp109 = subjects95.popleft()
                    associative1 = tmp109
                    associative_type1 = type(tmp109)
                    subjects110 = deque(tmp109._args)
                    matcher = CommutativeMatcher121237.get()
                    tmp111 = subjects110
                    subjects110 = []
                    for s in tmp111:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp111, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 121243
                            if len(subjects95) == 0:
                                pass
                                # State 121244
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 121245
                                    if len(subjects51) == 0:
                                        pass
                                        # State 121246
                                        if len(subjects) == 0:
                                            pass
                                            # 2: asec(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                            yield 2, subst2
                                if len(subjects51) >= 1:
                                    tmp113 = subjects51.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.3.3', tmp113)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 121245
                                        if len(subjects51) == 0:
                                            pass
                                            # State 121246
                                            if len(subjects) == 0:
                                                pass
                                                # 2: asec(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 2, subst2
                                    subjects51.appendleft(tmp113)
                    subjects95.appendleft(tmp109)
                subjects51.appendleft(tmp94)
            if len(subjects51) >= 1 and isinstance(subjects51[0], acsc):
                tmp115 = subjects51.popleft()
                subjects116 = deque(tmp115._args)
                # State 121424
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 121425
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 121426
                        if len(subjects116) >= 1:
                            tmp119 = subjects116.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.3.1.0', tmp119)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 121427
                                if len(subjects116) == 0:
                                    pass
                                    # State 121428
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 121429
                                        if len(subjects51) == 0:
                                            pass
                                            # State 121430
                                            if len(subjects) == 0:
                                                pass
                                                # 3: acsc(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 3, subst4
                                    if len(subjects51) >= 1:
                                        tmp122 = subjects51.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.3', tmp122)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 121429
                                            if len(subjects51) == 0:
                                                pass
                                                # State 121430
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: acsc(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                    yield 3, subst4
                                        subjects51.appendleft(tmp122)
                            subjects116.appendleft(tmp119)
                    if len(subjects116) >= 1 and isinstance(subjects116[0], Mul):
                        tmp124 = subjects116.popleft()
                        associative1 = tmp124
                        associative_type1 = type(tmp124)
                        subjects125 = deque(tmp124._args)
                        matcher = CommutativeMatcher121432.get()
                        tmp126 = subjects125
                        subjects125 = []
                        for s in tmp126:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp126, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 121433
                                if len(subjects116) == 0:
                                    pass
                                    # State 121434
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 121435
                                        if len(subjects51) == 0:
                                            pass
                                            # State 121436
                                            if len(subjects) == 0:
                                                pass
                                                # 3: acsc(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 3, subst3
                                    if len(subjects51) >= 1:
                                        tmp128 = subjects51.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.3.3', tmp128)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 121435
                                            if len(subjects51) == 0:
                                                pass
                                                # State 121436
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: acsc(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                    yield 3, subst3
                                        subjects51.appendleft(tmp128)
                        subjects116.appendleft(tmp124)
                if len(subjects116) >= 1 and isinstance(subjects116[0], Add):
                    tmp130 = subjects116.popleft()
                    associative1 = tmp130
                    associative_type1 = type(tmp130)
                    subjects131 = deque(tmp130._args)
                    matcher = CommutativeMatcher121438.get()
                    tmp132 = subjects131
                    subjects131 = []
                    for s in tmp132:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp132, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 121444
                            if len(subjects116) == 0:
                                pass
                                # State 121445
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 121446
                                    if len(subjects51) == 0:
                                        pass
                                        # State 121447
                                        if len(subjects) == 0:
                                            pass
                                            # 3: acsc(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                            yield 3, subst2
                                if len(subjects51) >= 1:
                                    tmp134 = subjects51.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i2.3.3', tmp134)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 121446
                                        if len(subjects51) == 0:
                                            pass
                                            # State 121447
                                            if len(subjects) == 0:
                                                pass
                                                # 3: acsc(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 3, subst2
                                    subjects51.appendleft(tmp134)
                    subjects116.appendleft(tmp130)
                subjects51.appendleft(tmp115)
            subjects.appendleft(tmp50)
        return
        yield


from .generated_part000683 import *
from .generated_part000689 import *
from .generated_part000672 import *
from .generated_part000680 import *
from .generated_part000692 import *
from .generated_part000675 import *
from .generated_part000687 import *
from .generated_part000678 import *
from .generated_part000677 import *
from collections import deque
from matchpy.utils import VariableWithCount
from .generated_part000674 import *
from .generated_part000690 import *
from .generated_part000693 import *
from .generated_part000671 import *
from multiset import Multiset
from .generated_part000686 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part000681 import *
from .generated_part000684 import *