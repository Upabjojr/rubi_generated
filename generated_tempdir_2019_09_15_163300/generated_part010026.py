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


class CommutativeMatcher114285(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i4.0', 1, 1, None), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i4.0', 1, 1, None), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i4.0', 1, 1, None), Mul)
]),
    10: (10, Multiset({10: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({11: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({12: 1}), [
      (VariableWithCount('i4.0', 1, 1, None), Mul)
]),
    13: (13, Multiset({13: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({14: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({15: 1}), [
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
        if CommutativeMatcher114285._instance is None:
            CommutativeMatcher114285._instance = CommutativeMatcher114285()
        return CommutativeMatcher114285._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 114284
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 114286
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 114287
                if len(subjects2) >= 1:
                    tmp4 = subjects2.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i4.2.0', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114288
                        if len(subjects2) == 0:
                            pass
                            # State 114289
                            if len(subjects) == 0:
                                pass
                                # 0: atan(x*a) /; (cons_f2)
                                yield 0, subst2
                                # 1: atan(x*a) /; (cons_f2) and (cons_f4)
                                yield 1, subst2
                    subjects2.appendleft(tmp4)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 114532
                if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                    tmp7 = subjects2.popleft()
                    associative1 = tmp7
                    associative_type1 = type(tmp7)
                    subjects8 = deque(tmp7._args)
                    matcher = CommutativeMatcher114534.get()
                    tmp9 = subjects8
                    subjects8 = []
                    for s in tmp9:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp9, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 114540
                            if len(subjects2) == 0:
                                pass
                                # State 114541
                                if len(subjects) == 0:
                                    pass
                                    # 2: atan(c*(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 2, subst2
                    subjects2.appendleft(tmp7)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp10 = subjects2.popleft()
                associative1 = tmp10
                associative_type1 = type(tmp10)
                subjects11 = deque(tmp10._args)
                matcher = CommutativeMatcher114291.get()
                tmp12 = subjects11
                subjects11 = []
                for s in tmp12:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp12, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 114292
                        if len(subjects2) == 0:
                            pass
                            # State 114293
                            if len(subjects) == 0:
                                pass
                                # 0: atan(x*a) /; (cons_f2)
                                yield 0, subst1
                                # 1: atan(x*a) /; (cons_f2) and (cons_f4)
                                yield 1, subst1
                    if pattern_index == 1:
                        pass
                        # State 114550
                        if len(subjects2) == 0:
                            pass
                            # State 114551
                            if len(subjects) == 0:
                                pass
                                # 2: atan(c*(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 2, subst1
                subjects2.appendleft(tmp10)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp13 = subjects.popleft()
            subjects14 = deque(tmp13._args)
            # State 114892
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 114893
                if len(subjects14) >= 1:
                    tmp16 = subjects14.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i4.2.0', tmp16)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114894
                        if len(subjects14) == 0:
                            pass
                            # State 114895
                            if len(subjects) == 0:
                                pass
                                # 3: acot(x*a) /; (cons_f2)
                                yield 3, subst2
                                # 4: acot(x*a) /; (cons_f2) and (cons_f4)
                                yield 4, subst2
                    subjects14.appendleft(tmp16)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 115117
                if len(subjects14) >= 1 and isinstance(subjects14[0], Add):
                    tmp19 = subjects14.popleft()
                    associative1 = tmp19
                    associative_type1 = type(tmp19)
                    subjects20 = deque(tmp19._args)
                    matcher = CommutativeMatcher115119.get()
                    tmp21 = subjects20
                    subjects20 = []
                    for s in tmp21:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp21, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 115125
                            if len(subjects14) == 0:
                                pass
                                # State 115126
                                if len(subjects) == 0:
                                    pass
                                    # 5: acot(c*(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                    yield 5, subst2
                    subjects14.appendleft(tmp19)
            if len(subjects14) >= 1 and isinstance(subjects14[0], Mul):
                tmp22 = subjects14.popleft()
                associative1 = tmp22
                associative_type1 = type(tmp22)
                subjects23 = deque(tmp22._args)
                matcher = CommutativeMatcher114897.get()
                tmp24 = subjects23
                subjects23 = []
                for s in tmp24:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp24, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 114898
                        if len(subjects14) == 0:
                            pass
                            # State 114899
                            if len(subjects) == 0:
                                pass
                                # 3: acot(x*a) /; (cons_f2)
                                yield 3, subst1
                                # 4: acot(x*a) /; (cons_f2) and (cons_f4)
                                yield 4, subst1
                    if pattern_index == 1:
                        pass
                        # State 115135
                        if len(subjects14) == 0:
                            pass
                            # State 115136
                            if len(subjects) == 0:
                                pass
                                # 5: acot(c*(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                yield 5, subst1
                subjects14.appendleft(tmp22)
            subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp25 = subjects.popleft()
            subjects26 = deque(tmp25._args)
            # State 142178
            if len(subjects26) >= 1:
                tmp27 = subjects26.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i4.1', tmp27)
                except ValueError:
                    pass
                else:
                    pass
                    # State 142179
                    if len(subjects26) == 0:
                        pass
                        # State 142180
                        if len(subjects) == 0:
                            pass
                            # 6: asinh(u) /; (cons_f806)
                            yield 6, subst1
                subjects26.appendleft(tmp27)
            subjects.appendleft(tmp25)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp29 = subjects.popleft()
            subjects30 = deque(tmp29._args)
            # State 142203
            if len(subjects30) >= 1:
                tmp31 = subjects30.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i4.1', tmp31)
                except ValueError:
                    pass
                else:
                    pass
                    # State 142204
                    if len(subjects30) == 0:
                        pass
                        # State 142205
                        if len(subjects) == 0:
                            pass
                            # 7: acosh(u) /; (cons_f806)
                            yield 7, subst1
                subjects30.appendleft(tmp31)
            subjects.appendleft(tmp29)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp33 = subjects.popleft()
            subjects34 = deque(tmp33._args)
            # State 143642
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 143643
                if len(subjects34) >= 1:
                    tmp36 = subjects34.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i4.2.0', tmp36)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 143644
                        if len(subjects34) == 0:
                            pass
                            # State 143645
                            if len(subjects) == 0:
                                pass
                                # 8: atanh(x*a) /; (cons_f2)
                                yield 8, subst2
                                # 9: atanh(x*a) /; (cons_f2) and (cons_f4)
                                yield 9, subst2
                    subjects34.appendleft(tmp36)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 143830
                if len(subjects34) >= 1 and isinstance(subjects34[0], Add):
                    tmp39 = subjects34.popleft()
                    associative1 = tmp39
                    associative_type1 = type(tmp39)
                    subjects40 = deque(tmp39._args)
                    matcher = CommutativeMatcher143832.get()
                    tmp41 = subjects40
                    subjects40 = []
                    for s in tmp41:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp41, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 143838
                            if len(subjects34) == 0:
                                pass
                                # State 143839
                                if len(subjects) == 0:
                                    pass
                                    # 10: atanh(c*(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 10, subst2
                    subjects34.appendleft(tmp39)
            if len(subjects34) >= 1 and isinstance(subjects34[0], Mul):
                tmp42 = subjects34.popleft()
                associative1 = tmp42
                associative_type1 = type(tmp42)
                subjects43 = deque(tmp42._args)
                matcher = CommutativeMatcher143647.get()
                tmp44 = subjects43
                subjects43 = []
                for s in tmp44:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp44, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 143648
                        if len(subjects34) == 0:
                            pass
                            # State 143649
                            if len(subjects) == 0:
                                pass
                                # 8: atanh(x*a) /; (cons_f2)
                                yield 8, subst1
                                # 9: atanh(x*a) /; (cons_f2) and (cons_f4)
                                yield 9, subst1
                    if pattern_index == 1:
                        pass
                        # State 143848
                        if len(subjects34) == 0:
                            pass
                            # State 143849
                            if len(subjects) == 0:
                                pass
                                # 10: atanh(c*(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 10, subst1
                subjects34.appendleft(tmp42)
            subjects.appendleft(tmp33)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp45 = subjects.popleft()
            subjects46 = deque(tmp45._args)
            # State 144197
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 144198
                if len(subjects46) >= 1:
                    tmp48 = subjects46.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i4.2.0', tmp48)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 144199
                        if len(subjects46) == 0:
                            pass
                            # State 144200
                            if len(subjects) == 0:
                                pass
                                # 11: acoth(x*a) /; (cons_f2)
                                yield 11, subst2
                                # 12: acoth(x*a) /; (cons_f2) and (cons_f4)
                                yield 12, subst2
                    subjects46.appendleft(tmp48)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 144403
                if len(subjects46) >= 1 and isinstance(subjects46[0], Add):
                    tmp51 = subjects46.popleft()
                    associative1 = tmp51
                    associative_type1 = type(tmp51)
                    subjects52 = deque(tmp51._args)
                    matcher = CommutativeMatcher144405.get()
                    tmp53 = subjects52
                    subjects52 = []
                    for s in tmp53:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp53, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 144411
                            if len(subjects46) == 0:
                                pass
                                # State 144412
                                if len(subjects) == 0:
                                    pass
                                    # 13: acoth(c*(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                    yield 13, subst2
                    subjects46.appendleft(tmp51)
            if len(subjects46) >= 1 and isinstance(subjects46[0], Mul):
                tmp54 = subjects46.popleft()
                associative1 = tmp54
                associative_type1 = type(tmp54)
                subjects55 = deque(tmp54._args)
                matcher = CommutativeMatcher144202.get()
                tmp56 = subjects55
                subjects55 = []
                for s in tmp56:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp56, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144203
                        if len(subjects46) == 0:
                            pass
                            # State 144204
                            if len(subjects) == 0:
                                pass
                                # 11: acoth(x*a) /; (cons_f2)
                                yield 11, subst1
                                # 12: acoth(x*a) /; (cons_f2) and (cons_f4)
                                yield 12, subst1
                    if pattern_index == 1:
                        pass
                        # State 144421
                        if len(subjects46) == 0:
                            pass
                            # State 144422
                            if len(subjects) == 0:
                                pass
                                # 13: acoth(c*(a + x*b)) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4)
                                yield 13, subst1
                subjects46.appendleft(tmp54)
            subjects.appendleft(tmp45)
        if len(subjects) >= 1 and isinstance(subjects[0], asech):
            tmp57 = subjects.popleft()
            subjects58 = deque(tmp57._args)
            # State 150388
            if len(subjects58) >= 1:
                tmp59 = subjects58.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i4.1', tmp59)
                except ValueError:
                    pass
                else:
                    pass
                    # State 150389
                    if len(subjects58) == 0:
                        pass
                        # State 150390
                        if len(subjects) == 0:
                            pass
                            # 14: asech(u)
                            yield 14, subst1
                subjects58.appendleft(tmp59)
            subjects.appendleft(tmp57)
        if len(subjects) >= 1 and isinstance(subjects[0], acsch):
            tmp61 = subjects.popleft()
            subjects62 = deque(tmp61._args)
            # State 150401
            if len(subjects62) >= 1:
                tmp63 = subjects62.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i4.1', tmp63)
                except ValueError:
                    pass
                else:
                    pass
                    # State 150402
                    if len(subjects62) == 0:
                        pass
                        # State 150403
                        if len(subjects) == 0:
                            pass
                            # 15: acsch(u)
                            yield 15, subst1
                subjects62.appendleft(tmp63)
            subjects.appendleft(tmp61)
        return
        yield


from .generated_part010044 import *
from .generated_part010027 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part010037 import *
from .generated_part010039 import *
from collections import deque
from .generated_part010029 import *
from .generated_part010032 import *
from .generated_part010034 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part010042 import *