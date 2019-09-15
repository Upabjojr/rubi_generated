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


class CommutativeMatcher57183(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.4.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    10: (10, Multiset({10: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    11: (11, Multiset({11: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 1
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher57183._instance is None:
            CommutativeMatcher57183._instance = CommutativeMatcher57183()
        return CommutativeMatcher57183._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 57182
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 57184
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 57185
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 58389
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58390
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 64350
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 64351
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst2
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 65730
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 65731
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst2
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 68183
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 68184
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                        yield 4, subst2
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 75539
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 75540
                if len(subjects) >= 1:
                    tmp18 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.1', tmp18)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75541
                        if len(subjects) == 0:
                            pass
                            # 5: b*x**n
                            yield 5, subst3
                    subjects.appendleft(tmp18)
            if len(subjects) >= 1:
                tmp20 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp20)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103445
                    if len(subjects) == 0:
                        pass
                        # 9: x*f
                        yield 9, subst2
                subjects.appendleft(tmp20)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp22 = subjects.popleft()
                subjects23 = deque(tmp22._args)
                # State 75542
                if len(subjects23) >= 1:
                    tmp24 = subjects23.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.1', tmp24)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75543
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 75544
                            if len(subjects23) == 0:
                                pass
                                # State 75545
                                if len(subjects) == 0:
                                    pass
                                    # 5: b*x**n
                                    yield 5, subst3
                        if len(subjects23) >= 1:
                            tmp27 = subjects23.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp27)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75544
                                if len(subjects23) == 0:
                                    pass
                                    # State 75545
                                    if len(subjects) == 0:
                                        pass
                                        # 5: b*x**n
                                        yield 5, subst3
                            subjects23.appendleft(tmp27)
                    subjects23.appendleft(tmp24)
                if len(subjects23) >= 1 and isinstance(subjects23[0], Add):
                    tmp29 = subjects23.popleft()
                    associative1 = tmp29
                    associative_type1 = type(tmp29)
                    subjects30 = deque(tmp29._args)
                    matcher = CommutativeMatcher107414.get()
                    tmp31 = subjects30
                    subjects30 = []
                    for s in tmp31:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp31, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 107420
                            if len(subjects23) >= 1:
                                tmp32 = []
                                tmp32.append(subjects23.popleft())
                                while True:
                                    if len(tmp32) > 1:
                                        tmp33 = create_operation_expression(associative1, tmp32)
                                    elif len(tmp32) == 1:
                                        tmp33 = tmp32[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.1.2', tmp33)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 107421
                                        if len(subjects23) == 0:
                                            pass
                                            # State 107422
                                            if len(subjects) == 0:
                                                pass
                                                # 11: b*(x*d + c)**n
                                                yield 11, subst3
                                    if len(subjects23) == 0:
                                        break
                                    tmp32.append(subjects23.popleft())
                                subjects23.extendleft(reversed(tmp32))
                    subjects23.appendleft(tmp29)
                subjects.appendleft(tmp22)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp35 = subjects.popleft()
                subjects36 = deque(tmp35._args)
                # State 105290
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 105291
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 105292
                        if len(subjects36) >= 1:
                            tmp39 = subjects36.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.1.2.1', tmp39)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105293
                                if len(subjects36) == 0:
                                    pass
                                    # State 105294
                                    if len(subjects) == 0:
                                        pass
                                        # 10: b*log(c*x**n)
                                        yield 10, subst4
                            subjects36.appendleft(tmp39)
                    if len(subjects36) >= 1 and isinstance(subjects36[0], Pow):
                        tmp41 = subjects36.popleft()
                        subjects42 = deque(tmp41._args)
                        # State 105295
                        if len(subjects42) >= 1:
                            tmp43 = subjects42.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2.1', tmp43)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105296
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 105297
                                    if len(subjects42) == 0:
                                        pass
                                        # State 105298
                                        if len(subjects36) == 0:
                                            pass
                                            # State 105299
                                            if len(subjects) == 0:
                                                pass
                                                # 10: b*log(c*x**n)
                                                yield 10, subst4
                                if len(subjects42) >= 1:
                                    tmp46 = subjects42.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.1.2.2', tmp46)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 105297
                                        if len(subjects42) == 0:
                                            pass
                                            # State 105298
                                            if len(subjects36) == 0:
                                                pass
                                                # State 105299
                                                if len(subjects) == 0:
                                                    pass
                                                    # 10: b*log(c*x**n)
                                                    yield 10, subst4
                                    subjects42.appendleft(tmp46)
                            subjects42.appendleft(tmp43)
                        subjects36.appendleft(tmp41)
                if len(subjects36) >= 1 and isinstance(subjects36[0], Mul):
                    tmp48 = subjects36.popleft()
                    associative1 = tmp48
                    associative_type1 = type(tmp48)
                    subjects49 = deque(tmp48._args)
                    matcher = CommutativeMatcher105301.get()
                    tmp50 = subjects49
                    subjects49 = []
                    for s in tmp50:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp50, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 105308
                            if len(subjects36) == 0:
                                pass
                                # State 105309
                                if len(subjects) == 0:
                                    pass
                                    # 10: b*log(c*x**n)
                                    yield 10, subst2
                    subjects36.appendleft(tmp48)
                subjects.appendleft(tmp35)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 75933
            if len(subjects) >= 1:
                tmp52 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp52)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75934
                    if len(subjects) == 0:
                        pass
                        # 6: x*f
                        yield 6, subst2
                subjects.appendleft(tmp52)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 75971
            if len(subjects) >= 1:
                tmp55 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp55)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75972
                    if len(subjects) == 0:
                        pass
                        # 7: x*f
                        yield 7, subst2
                subjects.appendleft(tmp55)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 82777
            if len(subjects) >= 1:
                tmp58 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.4.1.0', tmp58)
                except ValueError:
                    pass
                else:
                    pass
                    # State 82778
                    if len(subjects) == 0:
                        pass
                        # 8: x*d
                        yield 8, subst2
                subjects.appendleft(tmp58)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp60 = subjects.popleft()
            associative1 = tmp60
            associative_type1 = type(tmp60)
            subjects61 = deque(tmp60._args)
            matcher = CommutativeMatcher57187.get()
            tmp62 = subjects61
            subjects61 = []
            for s in tmp62:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp62, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 57188
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 58391
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 64352
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 65732
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 68185
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 75552
                    if len(subjects) == 0:
                        pass
                        # 5: b*x**n
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 75935
                    if len(subjects) == 0:
                        pass
                        # 6: x*f
                        yield 6, subst1
                if pattern_index == 7:
                    pass
                    # State 75973
                    if len(subjects) == 0:
                        pass
                        # 7: x*f
                        yield 7, subst1
                if pattern_index == 8:
                    pass
                    # State 82779
                    if len(subjects) == 0:
                        pass
                        # 8: x*d
                        yield 8, subst1
                if pattern_index == 9:
                    pass
                    # State 103446
                    if len(subjects) == 0:
                        pass
                        # 9: x*f
                        yield 9, subst1
                if pattern_index == 10:
                    pass
                    # State 105330
                    if len(subjects) == 0:
                        pass
                        # 10: b*log(c*x**n)
                        yield 10, subst1
                if pattern_index == 11:
                    pass
                    # State 107433
                    if len(subjects) == 0:
                        pass
                        # 11: b*(x*d + c)**n
                        yield 11, subst1
            subjects.appendleft(tmp60)
        return
        yield


from .generated_part004194 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part004196 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part004197 import *