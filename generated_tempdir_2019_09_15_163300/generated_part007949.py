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


class CommutativeMatcher145110(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({6: 1}), [
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
        if CommutativeMatcher145110._instance is None:
            CommutativeMatcher145110._instance = CommutativeMatcher145110()
        return CommutativeMatcher145110._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 145109
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 145200
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 145201
                    if len(subjects) == 0:
                        pass
                        # 0: x**n
                        yield 0, subst2
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 145202
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 145203
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 145204
                        if len(subjects5) == 0:
                            pass
                            # State 145205
                            if len(subjects) == 0:
                                pass
                                # 0: x**n
                                yield 0, subst2
                    if len(subjects5) >= 1:
                        tmp9 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 145204
                            if len(subjects5) == 0:
                                pass
                                # State 145205
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects5.appendleft(tmp9)
                    if len(subjects5) >= 1:
                        tmp11 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp11)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 145253
                            if len(subjects5) == 0:
                                pass
                                # State 145254
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                                    yield 1, subst2
                        subjects5.appendleft(tmp11)
                subjects5.appendleft(tmp6)
            if len(subjects5) >= 1:
                tmp13 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp13)
                except ValueError:
                    pass
                else:
                    pass
                    # State 145518
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 145519
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 145520
                            if len(subjects5) >= 1:
                                tmp17 = subjects5.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1', tmp17)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 145521
                                    if len(subjects5) == 0:
                                        pass
                                        # State 145522
                                        if len(subjects) == 0:
                                            pass
                                            # 2: f**(x*d + c)
                                            yield 2, subst4
                                subjects5.appendleft(tmp17)
                        if len(subjects5) >= 1 and isinstance(subjects5[0], Mul):
                            tmp19 = subjects5.popleft()
                            associative1 = tmp19
                            associative_type1 = type(tmp19)
                            subjects20 = deque(tmp19._args)
                            matcher = CommutativeMatcher145524.get()
                            tmp21 = subjects20
                            subjects20 = []
                            for s in tmp21:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp21, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 145525
                                    if len(subjects5) == 0:
                                        pass
                                        # State 145526
                                        if len(subjects) == 0:
                                            pass
                                            # 2: f**(x*d + c)
                                            yield 2, subst3
                            subjects5.appendleft(tmp19)
                    if len(subjects5) >= 1 and isinstance(subjects5[0], Add):
                        tmp22 = subjects5.popleft()
                        associative1 = tmp22
                        associative_type1 = type(tmp22)
                        subjects23 = deque(tmp22._args)
                        matcher = CommutativeMatcher145528.get()
                        tmp24 = subjects23
                        subjects23 = []
                        for s in tmp24:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp24, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 145534
                                if len(subjects5) == 0:
                                    pass
                                    # State 145535
                                    if len(subjects) == 0:
                                        pass
                                        # 2: f**(x*d + c)
                                        yield 2, subst2
                        subjects5.appendleft(tmp22)
                subjects5.appendleft(tmp13)
            if len(subjects5) >= 1 and isinstance(subjects5[0], tanh):
                tmp25 = subjects5.popleft()
                subjects26 = deque(tmp25._args)
                # State 147437
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 147438
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 147439
                        if len(subjects26) >= 1:
                            tmp29 = subjects26.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.0', tmp29)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 147440
                                if len(subjects26) == 0:
                                    pass
                                    # State 147441
                                    if len(subjects5) >= 1 and subjects5[0] == Integer(-1):
                                        tmp31 = subjects5.popleft()
                                        # State 147442
                                        if len(subjects5) == 0:
                                            pass
                                            # State 147443
                                            if len(subjects) == 0:
                                                pass
                                                # 4: 1/tanh(x*b + a)
                                                yield 4, subst3
                                        subjects5.appendleft(tmp31)
                            subjects26.appendleft(tmp29)
                    if len(subjects26) >= 1 and isinstance(subjects26[0], Mul):
                        tmp32 = subjects26.popleft()
                        associative1 = tmp32
                        associative_type1 = type(tmp32)
                        subjects33 = deque(tmp32._args)
                        matcher = CommutativeMatcher147445.get()
                        tmp34 = subjects33
                        subjects33 = []
                        for s in tmp34:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp34, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 147446
                                if len(subjects26) == 0:
                                    pass
                                    # State 147447
                                    if len(subjects5) >= 1 and subjects5[0] == Integer(-1):
                                        tmp35 = subjects5.popleft()
                                        # State 147448
                                        if len(subjects5) == 0:
                                            pass
                                            # State 147449
                                            if len(subjects) == 0:
                                                pass
                                                # 4: 1/tanh(x*b + a)
                                                yield 4, subst2
                                        subjects5.appendleft(tmp35)
                        subjects26.appendleft(tmp32)
                if len(subjects26) >= 1 and isinstance(subjects26[0], Add):
                    tmp36 = subjects26.popleft()
                    associative1 = tmp36
                    associative_type1 = type(tmp36)
                    subjects37 = deque(tmp36._args)
                    matcher = CommutativeMatcher147451.get()
                    tmp38 = subjects37
                    subjects37 = []
                    for s in tmp38:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp38, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 147457
                            if len(subjects26) == 0:
                                pass
                                # State 147458
                                if len(subjects5) >= 1 and subjects5[0] == Integer(-1):
                                    tmp39 = subjects5.popleft()
                                    # State 147459
                                    if len(subjects5) == 0:
                                        pass
                                        # State 147460
                                        if len(subjects) == 0:
                                            pass
                                            # 4: 1/tanh(x*b + a)
                                            yield 4, subst1
                                    subjects5.appendleft(tmp39)
                    subjects26.appendleft(tmp36)
                subjects5.appendleft(tmp25)
            if len(subjects5) >= 1 and isinstance(subjects5[0], tan):
                tmp40 = subjects5.popleft()
                subjects41 = deque(tmp40._args)
                # State 148488
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 148489
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 148490
                        if len(subjects41) >= 1:
                            tmp44 = subjects41.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.0', tmp44)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 148491
                                if len(subjects41) == 0:
                                    pass
                                    # State 148492
                                    if len(subjects5) >= 1 and subjects5[0] == Integer(-1):
                                        tmp46 = subjects5.popleft()
                                        # State 148493
                                        if len(subjects5) == 0:
                                            pass
                                            # State 148494
                                            if len(subjects) == 0:
                                                pass
                                                # 6: 1/tan(x*e + d)
                                                yield 6, subst3
                                        subjects5.appendleft(tmp46)
                            subjects41.appendleft(tmp44)
                    if len(subjects41) >= 1 and isinstance(subjects41[0], Mul):
                        tmp47 = subjects41.popleft()
                        associative1 = tmp47
                        associative_type1 = type(tmp47)
                        subjects48 = deque(tmp47._args)
                        matcher = CommutativeMatcher148496.get()
                        tmp49 = subjects48
                        subjects48 = []
                        for s in tmp49:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp49, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 148497
                                if len(subjects41) == 0:
                                    pass
                                    # State 148498
                                    if len(subjects5) >= 1 and subjects5[0] == Integer(-1):
                                        tmp50 = subjects5.popleft()
                                        # State 148499
                                        if len(subjects5) == 0:
                                            pass
                                            # State 148500
                                            if len(subjects) == 0:
                                                pass
                                                # 6: 1/tan(x*e + d)
                                                yield 6, subst2
                                        subjects5.appendleft(tmp50)
                        subjects41.appendleft(tmp47)
                if len(subjects41) >= 1 and isinstance(subjects41[0], Add):
                    tmp51 = subjects41.popleft()
                    associative1 = tmp51
                    associative_type1 = type(tmp51)
                    subjects52 = deque(tmp51._args)
                    matcher = CommutativeMatcher148502.get()
                    tmp53 = subjects52
                    subjects52 = []
                    for s in tmp53:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp53, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 148508
                            if len(subjects41) == 0:
                                pass
                                # State 148509
                                if len(subjects5) >= 1 and subjects5[0] == Integer(-1):
                                    tmp54 = subjects5.popleft()
                                    # State 148510
                                    if len(subjects5) == 0:
                                        pass
                                        # State 148511
                                        if len(subjects) == 0:
                                            pass
                                            # 6: 1/tan(x*e + d)
                                            yield 6, subst1
                                    subjects5.appendleft(tmp54)
                    subjects41.appendleft(tmp51)
                subjects5.appendleft(tmp40)
            subjects.appendleft(tmp4)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp55 = subjects.popleft()
            subjects56 = deque(tmp55._args)
            # State 147245
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 147246
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 147247
                    if len(subjects56) >= 1:
                        tmp59 = subjects56.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp59)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 147248
                            if len(subjects56) == 0:
                                pass
                                # State 147249
                                if len(subjects) == 0:
                                    pass
                                    # 3: tanh(x*b + a)
                                    yield 3, subst3
                        subjects56.appendleft(tmp59)
                if len(subjects56) >= 1 and isinstance(subjects56[0], Mul):
                    tmp61 = subjects56.popleft()
                    associative1 = tmp61
                    associative_type1 = type(tmp61)
                    subjects62 = deque(tmp61._args)
                    matcher = CommutativeMatcher147251.get()
                    tmp63 = subjects62
                    subjects62 = []
                    for s in tmp63:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp63, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 147252
                            if len(subjects56) == 0:
                                pass
                                # State 147253
                                if len(subjects) == 0:
                                    pass
                                    # 3: tanh(x*b + a)
                                    yield 3, subst2
                    subjects56.appendleft(tmp61)
            if len(subjects56) >= 1 and isinstance(subjects56[0], Add):
                tmp64 = subjects56.popleft()
                associative1 = tmp64
                associative_type1 = type(tmp64)
                subjects65 = deque(tmp64._args)
                matcher = CommutativeMatcher147255.get()
                tmp66 = subjects65
                subjects65 = []
                for s in tmp66:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp66, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 147261
                        if len(subjects56) == 0:
                            pass
                            # State 147262
                            if len(subjects) == 0:
                                pass
                                # 3: tanh(x*b + a)
                                yield 3, subst1
                subjects56.appendleft(tmp64)
            subjects.appendleft(tmp55)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp67 = subjects.popleft()
            subjects68 = deque(tmp67._args)
            # State 148304
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 148305
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 148306
                    if len(subjects68) >= 1:
                        tmp71 = subjects68.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp71)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 148307
                            if len(subjects68) == 0:
                                pass
                                # State 148308
                                if len(subjects) == 0:
                                    pass
                                    # 5: tan(x*f + e)
                                    yield 5, subst3
                        subjects68.appendleft(tmp71)
                if len(subjects68) >= 1 and isinstance(subjects68[0], Mul):
                    tmp73 = subjects68.popleft()
                    associative1 = tmp73
                    associative_type1 = type(tmp73)
                    subjects74 = deque(tmp73._args)
                    matcher = CommutativeMatcher148310.get()
                    tmp75 = subjects74
                    subjects74 = []
                    for s in tmp75:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp75, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 148311
                            if len(subjects68) == 0:
                                pass
                                # State 148312
                                if len(subjects) == 0:
                                    pass
                                    # 5: tan(x*f + e)
                                    yield 5, subst2
                    subjects68.appendleft(tmp73)
            if len(subjects68) >= 1 and isinstance(subjects68[0], Add):
                tmp76 = subjects68.popleft()
                associative1 = tmp76
                associative_type1 = type(tmp76)
                subjects77 = deque(tmp76._args)
                matcher = CommutativeMatcher148314.get()
                tmp78 = subjects77
                subjects77 = []
                for s in tmp78:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp78, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 148320
                        if len(subjects68) == 0:
                            pass
                            # State 148321
                            if len(subjects) == 0:
                                pass
                                # 5: tan(x*f + e)
                                yield 5, subst1
                subjects68.appendleft(tmp76)
            subjects.appendleft(tmp67)
        return
        yield


from .generated_part007959 import *
from .generated_part007953 import *
from .generated_part007954 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part007963 import *
from .generated_part007956 import *
from .generated_part007960 import *
from .generated_part007962 import *
from collections import deque
from .generated_part007957 import *
from .generated_part007951 import *
from .generated_part007950 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset