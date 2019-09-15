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


class CommutativeMatcher18265(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      
]),
    1: (1, Multiset({2: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({3: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({4: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher18265._instance is None:
            CommutativeMatcher18265._instance = CommutativeMatcher18265()
        return CommutativeMatcher18265._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 18264
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 18266
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i4.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 18267
                    if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                        tmp5 = subjects2.popleft()
                        # State 18268
                        if len(subjects2) == 0:
                            pass
                            # State 18269
                            if len(subjects) == 0:
                                pass
                                # 0: x**(-2) /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f1153)
                                yield 0, subst1
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1 and isinstance(subjects2[0], asinh):
                tmp6 = subjects2.popleft()
                subjects7 = deque(tmp6._args)
                # State 141800
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i4.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 141801
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i4.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 141802
                        if len(subjects7) >= 1:
                            tmp10 = subjects7.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i4.3.1.0', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 141803
                                if len(subjects7) == 0:
                                    pass
                                    # State 141804
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i4.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 141805
                                        if len(subjects2) == 0:
                                            pass
                                            # State 141806
                                            if len(subjects) == 0:
                                                pass
                                                # 3: asinh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 3, subst4
                                    if len(subjects2) >= 1:
                                        tmp13 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i4.3', tmp13)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 141805
                                            if len(subjects2) == 0:
                                                pass
                                                # State 141806
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: asinh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                    yield 3, subst4
                                        subjects2.appendleft(tmp13)
                            subjects7.appendleft(tmp10)
                    if len(subjects7) >= 1 and isinstance(subjects7[0], Mul):
                        tmp15 = subjects7.popleft()
                        associative1 = tmp15
                        associative_type1 = type(tmp15)
                        subjects16 = deque(tmp15._args)
                        matcher = CommutativeMatcher141808.get()
                        tmp17 = subjects16
                        subjects16 = []
                        for s in tmp17:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp17, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 141809
                                if len(subjects7) == 0:
                                    pass
                                    # State 141810
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i4.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 141811
                                        if len(subjects2) == 0:
                                            pass
                                            # State 141812
                                            if len(subjects) == 0:
                                                pass
                                                # 3: asinh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 3, subst3
                                    if len(subjects2) >= 1:
                                        tmp19 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i4.3', tmp19)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 141811
                                            if len(subjects2) == 0:
                                                pass
                                                # State 141812
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: asinh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                    yield 3, subst3
                                        subjects2.appendleft(tmp19)
                        subjects7.appendleft(tmp15)
                if len(subjects7) >= 1 and isinstance(subjects7[0], Add):
                    tmp21 = subjects7.popleft()
                    associative1 = tmp21
                    associative_type1 = type(tmp21)
                    subjects22 = deque(tmp21._args)
                    matcher = CommutativeMatcher141814.get()
                    tmp23 = subjects22
                    subjects22 = []
                    for s in tmp23:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp23, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 141820
                            if len(subjects7) == 0:
                                pass
                                # State 141821
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i4.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 141822
                                    if len(subjects2) == 0:
                                        pass
                                        # State 141823
                                        if len(subjects) == 0:
                                            pass
                                            # 3: asinh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                            yield 3, subst2
                                if len(subjects2) >= 1:
                                    tmp25 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i4.3', tmp25)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 141822
                                        if len(subjects2) == 0:
                                            pass
                                            # State 141823
                                            if len(subjects) == 0:
                                                pass
                                                # 3: asinh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 3, subst2
                                    subjects2.appendleft(tmp25)
                    subjects7.appendleft(tmp21)
                subjects2.appendleft(tmp6)
            if len(subjects2) >= 1 and isinstance(subjects2[0], acosh):
                tmp27 = subjects2.popleft()
                subjects28 = deque(tmp27._args)
                # State 141906
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i4.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 141907
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i4.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 141908
                        if len(subjects28) >= 1:
                            tmp31 = subjects28.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i4.3.1.0', tmp31)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 141909
                                if len(subjects28) == 0:
                                    pass
                                    # State 141910
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i4.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 141911
                                        if len(subjects2) == 0:
                                            pass
                                            # State 141912
                                            if len(subjects) == 0:
                                                pass
                                                # 4: acosh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 4, subst4
                                    if len(subjects2) >= 1:
                                        tmp34 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i4.3', tmp34)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 141911
                                            if len(subjects2) == 0:
                                                pass
                                                # State 141912
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: acosh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                    yield 4, subst4
                                        subjects2.appendleft(tmp34)
                            subjects28.appendleft(tmp31)
                    if len(subjects28) >= 1 and isinstance(subjects28[0], Mul):
                        tmp36 = subjects28.popleft()
                        associative1 = tmp36
                        associative_type1 = type(tmp36)
                        subjects37 = deque(tmp36._args)
                        matcher = CommutativeMatcher141914.get()
                        tmp38 = subjects37
                        subjects37 = []
                        for s in tmp38:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp38, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 141915
                                if len(subjects28) == 0:
                                    pass
                                    # State 141916
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i4.3', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 141917
                                        if len(subjects2) == 0:
                                            pass
                                            # State 141918
                                            if len(subjects) == 0:
                                                pass
                                                # 4: acosh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 4, subst3
                                    if len(subjects2) >= 1:
                                        tmp40 = subjects2.popleft()
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i4.3', tmp40)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 141917
                                            if len(subjects2) == 0:
                                                pass
                                                # State 141918
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: acosh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                    yield 4, subst3
                                        subjects2.appendleft(tmp40)
                        subjects28.appendleft(tmp36)
                if len(subjects28) >= 1 and isinstance(subjects28[0], Add):
                    tmp42 = subjects28.popleft()
                    associative1 = tmp42
                    associative_type1 = type(tmp42)
                    subjects43 = deque(tmp42._args)
                    matcher = CommutativeMatcher141920.get()
                    tmp44 = subjects43
                    subjects43 = []
                    for s in tmp44:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp44, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 141926
                            if len(subjects28) == 0:
                                pass
                                # State 141927
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i4.3', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 141928
                                    if len(subjects2) == 0:
                                        pass
                                        # State 141929
                                        if len(subjects) == 0:
                                            pass
                                            # 4: acosh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                            yield 4, subst2
                                if len(subjects2) >= 1:
                                    tmp46 = subjects2.popleft()
                                    subst2 = Substitution(subst1)
                                    try:
                                        subst2.try_add_variable('i4.3', tmp46)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 141928
                                        if len(subjects2) == 0:
                                            pass
                                            # State 141929
                                            if len(subjects) == 0:
                                                pass
                                                # 4: acosh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                                yield 4, subst2
                                    subjects2.appendleft(tmp46)
                    subjects28.appendleft(tmp42)
                subjects2.appendleft(tmp27)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 18270
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i4.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 18271
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp50 = subjects.popleft()
                    subjects51 = deque(tmp50._args)
                    # State 18272
                    if len(subjects51) >= 1:
                        tmp52 = subjects51.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.1', tmp52)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18273
                            if len(subjects51) >= 1 and subjects51[0] == Integer(4):
                                tmp54 = subjects51.popleft()
                                # State 18274
                                if len(subjects51) == 0:
                                    pass
                                    # State 18275
                                    if len(subjects) == 0:
                                        pass
                                        # 1: a + b*x**4 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f1153)
                                        yield 1, subst3
                                subjects51.appendleft(tmp54)
                        subjects51.appendleft(tmp52)
                    subjects.appendleft(tmp50)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp55 = subjects.popleft()
                associative1 = tmp55
                associative_type1 = type(tmp55)
                subjects56 = deque(tmp55._args)
                matcher = CommutativeMatcher18277.get()
                tmp57 = subjects56
                subjects56 = []
                for s in tmp57:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp57, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 18282
                        if len(subjects) == 0:
                            pass
                            # 1: a + b*x**4 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f1153)
                            yield 1, subst2
                subjects.appendleft(tmp55)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 141781
            if len(subjects) >= 1 and isinstance(subjects[0], asinh):
                tmp59 = subjects.popleft()
                subjects60 = deque(tmp59._args)
                # State 141782
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 141783
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i4.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 141784
                        if len(subjects60) >= 1:
                            tmp63 = subjects60.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i4.3.1.0', tmp63)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 141785
                                if len(subjects60) == 0:
                                    pass
                                    # State 141786
                                    if len(subjects) == 0:
                                        pass
                                        # 3: asinh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                        yield 3, subst4
                            subjects60.appendleft(tmp63)
                    if len(subjects60) >= 1 and isinstance(subjects60[0], Mul):
                        tmp65 = subjects60.popleft()
                        associative1 = tmp65
                        associative_type1 = type(tmp65)
                        subjects66 = deque(tmp65._args)
                        matcher = CommutativeMatcher141788.get()
                        tmp67 = subjects66
                        subjects66 = []
                        for s in tmp67:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp67, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 141789
                                if len(subjects60) == 0:
                                    pass
                                    # State 141790
                                    if len(subjects) == 0:
                                        pass
                                        # 3: asinh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                        yield 3, subst3
                        subjects60.appendleft(tmp65)
                if len(subjects60) >= 1 and isinstance(subjects60[0], Add):
                    tmp68 = subjects60.popleft()
                    associative1 = tmp68
                    associative_type1 = type(tmp68)
                    subjects69 = deque(tmp68._args)
                    matcher = CommutativeMatcher141792.get()
                    tmp70 = subjects69
                    subjects69 = []
                    for s in tmp70:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp70, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 141798
                            if len(subjects60) == 0:
                                pass
                                # State 141799
                                if len(subjects) == 0:
                                    pass
                                    # 3: asinh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                    yield 3, subst2
                    subjects60.appendleft(tmp68)
                subjects.appendleft(tmp59)
            if len(subjects) >= 1 and isinstance(subjects[0], acosh):
                tmp71 = subjects.popleft()
                subjects72 = deque(tmp71._args)
                # State 141888
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 141889
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i4.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 141890
                        if len(subjects72) >= 1:
                            tmp75 = subjects72.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i4.3.1.0', tmp75)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 141891
                                if len(subjects72) == 0:
                                    pass
                                    # State 141892
                                    if len(subjects) == 0:
                                        pass
                                        # 4: acosh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                        yield 4, subst4
                            subjects72.appendleft(tmp75)
                    if len(subjects72) >= 1 and isinstance(subjects72[0], Mul):
                        tmp77 = subjects72.popleft()
                        associative1 = tmp77
                        associative_type1 = type(tmp77)
                        subjects78 = deque(tmp77._args)
                        matcher = CommutativeMatcher141894.get()
                        tmp79 = subjects78
                        subjects78 = []
                        for s in tmp79:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp79, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 141895
                                if len(subjects72) == 0:
                                    pass
                                    # State 141896
                                    if len(subjects) == 0:
                                        pass
                                        # 4: acosh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                        yield 4, subst3
                        subjects72.appendleft(tmp77)
                if len(subjects72) >= 1 and isinstance(subjects72[0], Add):
                    tmp80 = subjects72.popleft()
                    associative1 = tmp80
                    associative_type1 = type(tmp80)
                    subjects81 = deque(tmp80._args)
                    matcher = CommutativeMatcher141898.get()
                    tmp82 = subjects81
                    subjects81 = []
                    for s in tmp82:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp82, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 141904
                            if len(subjects72) == 0:
                                pass
                                # State 141905
                                if len(subjects) == 0:
                                    pass
                                    # 4: acosh(a + x*b)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127) and (cons_f150)
                                    yield 4, subst2
                    subjects72.appendleft(tmp80)
                subjects.appendleft(tmp71)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp83 = subjects.popleft()
            associative1 = tmp83
            associative_type1 = type(tmp83)
            subjects84 = deque(tmp83._args)
            matcher = CommutativeMatcher18284.get()
            tmp85 = subjects84
            subjects84 = []
            for s in tmp85:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp85, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 18297
                    if len(subjects) == 0:
                        pass
                        # 1: a + b*x**4 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f1153)
                        yield 1, subst1
            subjects.appendleft(tmp83)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp86 = subjects.popleft()
            subjects87 = deque(tmp86._args)
            # State 54149
            if len(subjects87) >= 1:
                tmp88 = subjects87.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i4.1', tmp88)
                except ValueError:
                    pass
                else:
                    pass
                    # State 54150
                    if len(subjects87) == 0:
                        pass
                        # State 54151
                        if len(subjects) == 0:
                            pass
                            # 2: log(u)
                            yield 2, subst1
                subjects87.appendleft(tmp88)
            subjects.appendleft(tmp86)
        return
        yield


from .generated_part008106 import *
from .generated_part008108 import *
from .generated_part008098 import *
from .generated_part008101 import *
from .generated_part008096 import *
from .generated_part008102 import *
from .generated_part008105 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part008099 import *
from .generated_part008103 import *
from collections import deque
from .generated_part008095 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset