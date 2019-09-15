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


class CommutativeMatcher16919(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.0_1', 1, 1, S(1)), Mul)
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
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({4: 1, 5: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({10: 1}), [
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
        if CommutativeMatcher16919._instance is None:
            CommutativeMatcher16919._instance = CommutativeMatcher16919()
        return CommutativeMatcher16919._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 16918
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 23719
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 23720
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.3.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 23721
                    if len(subjects) >= 1:
                        tmp4 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.0', tmp4)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 23722
                            if len(subjects) == 0:
                                pass
                                # 0: (x*f + e)**p
                                yield 0, subst4
                        subjects.appendleft(tmp4)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp6 = subjects.popleft()
                    associative1 = tmp6
                    associative_type1 = type(tmp6)
                    subjects7 = deque(tmp6._args)
                    matcher = CommutativeMatcher23724.get()
                    tmp8 = subjects7
                    subjects7 = []
                    for s in tmp8:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp8, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 23725
                            if len(subjects) == 0:
                                pass
                                # 0: (x*f + e)**p
                                yield 0, subst3
                    subjects.appendleft(tmp6)
            if len(subjects) >= 1:
                tmp9 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1', tmp9)
                except ValueError:
                    pass
                else:
                    pass
                    # State 56638
                    if len(subjects) == 0:
                        pass
                        # 10: x**m
                        yield 10, subst2
                subjects.appendleft(tmp9)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp11 = subjects.popleft()
                associative1 = tmp11
                associative_type1 = type(tmp11)
                subjects12 = deque(tmp11._args)
                matcher = CommutativeMatcher23727.get()
                tmp13 = subjects12
                subjects12 = []
                for s in tmp13:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp13, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 23733
                        if len(subjects) == 0:
                            pass
                            # 0: (x*f + e)**p
                            yield 0, subst2
                subjects.appendleft(tmp11)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp14 = subjects.popleft()
                associative1 = tmp14
                associative_type1 = type(tmp14)
                subjects15 = deque(tmp14._args)
                matcher = CommutativeMatcher46945.get()
                tmp16 = subjects15
                subjects15 = []
                for s in tmp16:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp16, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46981
                        if len(subjects) == 0:
                            pass
                            # 2: (e1*(a + b*x)/(a + x*b))**n
                            yield 2, subst2
                    if pattern_index == 1:
                        pass
                        # State 47820
                        if len(subjects) == 0:
                            pass
                            # 3: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                            yield 3, subst2
                    if pattern_index == 2:
                        pass
                        # State 48365
                        if len(subjects) == 0:
                            pass
                            # 7: (e1*(e + x*f)**n2*(x*b + a)**n1)**n
                            yield 7, subst2
                    if pattern_index == 3:
                        pass
                        # State 48644
                        if len(subjects) == 0:
                            pass
                            # 8: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                            yield 8, subst2
                    if pattern_index == 4:
                        pass
                        # State 49087
                        if len(subjects) == 0:
                            pass
                            # 9: (e1*(c + x*d)**n2*(c + x*d)**n1)**n
                            yield 9, subst2
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 48125
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 48126
                if len(subjects) >= 1:
                    tmp19 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.0', tmp19)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 48127
                        if len(subjects) == 0:
                            pass
                            # 5: x*b + a
                            yield 5, subst3
                    subjects.appendleft(tmp19)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp21 = subjects.popleft()
                associative1 = tmp21
                associative_type1 = type(tmp21)
                subjects22 = deque(tmp21._args)
                matcher = CommutativeMatcher48129.get()
                tmp23 = subjects22
                subjects22 = []
                for s in tmp23:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp23, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 48130
                        if len(subjects) == 0:
                            pass
                            # 5: x*b + a
                            yield 5, subst2
                subjects.appendleft(tmp21)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp24 = subjects.popleft()
            subjects25 = deque(tmp24._args)
            # State 23734
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 23735
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 23736
                    if len(subjects25) >= 1:
                        tmp28 = subjects25.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp28)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 23737
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 23738
                                if len(subjects25) == 0:
                                    pass
                                    # State 23739
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (x*f + e)**p
                                        yield 0, subst4
                            if len(subjects25) >= 1:
                                tmp31 = subjects25.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2', tmp31)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 23738
                                    if len(subjects25) == 0:
                                        pass
                                        # State 23739
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (x*f + e)**p
                                            yield 0, subst4
                                subjects25.appendleft(tmp31)
                            if len(subjects25) >= 1 and subjects25[0] == Integer(-1):
                                tmp33 = subjects25.popleft()
                                # State 48119
                                if len(subjects25) == 0:
                                    pass
                                    # State 48120
                                    if len(subjects) == 0:
                                        pass
                                        # 4: 1/(x*f + e)
                                        yield 4, subst3
                                subjects25.appendleft(tmp33)
                        subjects25.appendleft(tmp28)
                if len(subjects25) >= 1 and isinstance(subjects25[0], Mul):
                    tmp34 = subjects25.popleft()
                    associative1 = tmp34
                    associative_type1 = type(tmp34)
                    subjects35 = deque(tmp34._args)
                    matcher = CommutativeMatcher23741.get()
                    tmp36 = subjects35
                    subjects35 = []
                    for s in tmp36:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp36, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 23742
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 23743
                                if len(subjects25) == 0:
                                    pass
                                    # State 23744
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (x*f + e)**p
                                        yield 0, subst3
                            if len(subjects25) >= 1:
                                tmp38 = []
                                tmp38.append(subjects25.popleft())
                                while True:
                                    if len(tmp38) > 1:
                                        tmp39 = create_operation_expression(associative1, tmp38)
                                    elif len(tmp38) == 1:
                                        tmp39 = tmp38[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2', tmp39)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 23743
                                        if len(subjects25) == 0:
                                            pass
                                            # State 23744
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (x*f + e)**p
                                                yield 0, subst3
                                    if len(subjects25) == 0:
                                        break
                                    tmp38.append(subjects25.popleft())
                                subjects25.extendleft(reversed(tmp38))
                            if len(subjects25) >= 1 and subjects25[0] == Integer(-1):
                                tmp41 = subjects25.popleft()
                                # State 48121
                                if len(subjects25) == 0:
                                    pass
                                    # State 48122
                                    if len(subjects) == 0:
                                        pass
                                        # 4: 1/(x*f + e)
                                        yield 4, subst2
                                subjects25.appendleft(tmp41)
                    subjects25.appendleft(tmp34)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 46283
                if len(subjects25) >= 1 and isinstance(subjects25[0], Pow):
                    tmp43 = subjects25.popleft()
                    subjects44 = deque(tmp43._args)
                    # State 46284
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 46285
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 46286
                            if len(subjects44) >= 1:
                                tmp47 = subjects44.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2.1', tmp47)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46287
                                    if len(subjects44) >= 1:
                                        tmp49 = subjects44.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.3.2.2', tmp49)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 46288
                                            if len(subjects44) == 0:
                                                pass
                                                # State 46289
                                                if len(subjects25) >= 1:
                                                    tmp51 = subjects25.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.3.2', tmp51)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 46290
                                                        if len(subjects25) == 0:
                                                            pass
                                                            # State 46291
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (b*(c*x**n)**p)**q
                                                                yield 1, subst6
                                                    subjects25.appendleft(tmp51)
                                        subjects44.appendleft(tmp49)
                                subjects44.appendleft(tmp47)
                        if len(subjects44) >= 1 and isinstance(subjects44[0], Pow):
                            tmp53 = subjects44.popleft()
                            subjects54 = deque(tmp53._args)
                            # State 46292
                            if len(subjects54) >= 1:
                                tmp55 = subjects54.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.3.2.2.1', tmp55)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46293
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 46294
                                        if len(subjects54) == 0:
                                            pass
                                            # State 46295
                                            if len(subjects44) >= 1:
                                                tmp58 = subjects44.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.3.2.2', tmp58)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 46296
                                                    if len(subjects44) == 0:
                                                        pass
                                                        # State 46297
                                                        if len(subjects25) >= 1:
                                                            tmp60 = subjects25.popleft()
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.3.2', tmp60)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 46298
                                                                if len(subjects25) == 0:
                                                                    pass
                                                                    # State 46299
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 1: (b*(c*x**n)**p)**q
                                                                        yield 1, subst6
                                                            subjects25.appendleft(tmp60)
                                                subjects44.appendleft(tmp58)
                                    if len(subjects54) >= 1:
                                        tmp62 = subjects54.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.2.2.2', tmp62)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 46294
                                            if len(subjects54) == 0:
                                                pass
                                                # State 46295
                                                if len(subjects44) >= 1:
                                                    tmp64 = subjects44.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.3.2.2', tmp64)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 46296
                                                        if len(subjects44) == 0:
                                                            pass
                                                            # State 46297
                                                            if len(subjects25) >= 1:
                                                                tmp66 = subjects25.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.3.2', tmp66)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 46298
                                                                    if len(subjects25) == 0:
                                                                        pass
                                                                        # State 46299
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 1: (b*(c*x**n)**p)**q
                                                                            yield 1, subst6
                                                                subjects25.appendleft(tmp66)
                                                    subjects44.appendleft(tmp64)
                                        subjects54.appendleft(tmp62)
                                subjects54.appendleft(tmp55)
                            subjects44.appendleft(tmp53)
                    if len(subjects44) >= 1 and isinstance(subjects44[0], Mul):
                        tmp68 = subjects44.popleft()
                        associative1 = tmp68
                        associative_type1 = type(tmp68)
                        subjects69 = deque(tmp68._args)
                        matcher = CommutativeMatcher46301.get()
                        tmp70 = subjects69
                        subjects69 = []
                        for s in tmp70:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp70, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 46308
                                if len(subjects44) >= 1:
                                    tmp71 = []
                                    tmp71.append(subjects44.popleft())
                                    while True:
                                        if len(tmp71) > 1:
                                            tmp72 = create_operation_expression(associative1, tmp71)
                                        elif len(tmp71) == 1:
                                            tmp72 = tmp71[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.3.2.2', tmp72)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 46309
                                            if len(subjects44) == 0:
                                                pass
                                                # State 46310
                                                if len(subjects25) >= 1:
                                                    tmp74 = subjects25.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.3.2', tmp74)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 46311
                                                        if len(subjects25) == 0:
                                                            pass
                                                            # State 46312
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (b*(c*x**n)**p)**q
                                                                yield 1, subst4
                                                    subjects25.appendleft(tmp74)
                                        if len(subjects44) == 0:
                                            break
                                        tmp71.append(subjects44.popleft())
                                    subjects44.extendleft(reversed(tmp71))
                        subjects44.appendleft(tmp68)
                    subjects25.appendleft(tmp43)
            if len(subjects25) >= 1:
                tmp76 = subjects25.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1', tmp76)
                except ValueError:
                    pass
                else:
                    pass
                    # State 48194
                    if len(subjects25) >= 1:
                        tmp78 = subjects25.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', tmp78)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48195
                            if len(subjects25) == 0:
                                pass
                                # State 48196
                                if len(subjects) == 0:
                                    pass
                                    # 6: u**n
                                    yield 6, subst2
                        subjects25.appendleft(tmp78)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 56639
                        if len(subjects25) == 0:
                            pass
                            # State 56640
                            if len(subjects) == 0:
                                pass
                                # 10: x**m
                                yield 10, subst2
                    if len(subjects25) >= 1:
                        tmp81 = subjects25.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', tmp81)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 56639
                            if len(subjects25) == 0:
                                pass
                                # State 56640
                                if len(subjects) == 0:
                                    pass
                                    # 10: x**m
                                    yield 10, subst2
                        subjects25.appendleft(tmp81)
                subjects25.appendleft(tmp76)
            if len(subjects25) >= 1 and isinstance(subjects25[0], Add):
                tmp83 = subjects25.popleft()
                associative1 = tmp83
                associative_type1 = type(tmp83)
                subjects84 = deque(tmp83._args)
                matcher = CommutativeMatcher23746.get()
                tmp85 = subjects84
                subjects84 = []
                for s in tmp85:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp85, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 23752
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 23753
                            if len(subjects25) == 0:
                                pass
                                # State 23754
                                if len(subjects) == 0:
                                    pass
                                    # 0: (x*f + e)**p
                                    yield 0, subst2
                        if len(subjects25) >= 1:
                            tmp87 = []
                            tmp87.append(subjects25.popleft())
                            while True:
                                if len(tmp87) > 1:
                                    tmp88 = create_operation_expression(associative1, tmp87)
                                elif len(tmp87) == 1:
                                    tmp88 = tmp87[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp88)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 23753
                                    if len(subjects25) == 0:
                                        pass
                                        # State 23754
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (x*f + e)**p
                                            yield 0, subst2
                                if len(subjects25) == 0:
                                    break
                                tmp87.append(subjects25.popleft())
                            subjects25.extendleft(reversed(tmp87))
                        if len(subjects25) >= 1 and subjects25[0] == Integer(-1):
                            tmp90 = subjects25.popleft()
                            # State 48123
                            if len(subjects25) == 0:
                                pass
                                # State 48124
                                if len(subjects) == 0:
                                    pass
                                    # 4: 1/(x*f + e)
                                    yield 4, subst1
                            subjects25.appendleft(tmp90)
                subjects25.appendleft(tmp83)
            if len(subjects25) >= 1 and isinstance(subjects25[0], Mul):
                tmp91 = subjects25.popleft()
                associative1 = tmp91
                associative_type1 = type(tmp91)
                subjects92 = deque(tmp91._args)
                matcher = CommutativeMatcher46314.get()
                tmp93 = subjects92
                subjects92 = []
                for s in tmp93:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp93, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46338
                        if len(subjects25) >= 1:
                            tmp94 = []
                            tmp94.append(subjects25.popleft())
                            while True:
                                if len(tmp94) > 1:
                                    tmp95 = create_operation_expression(associative1, tmp94)
                                elif len(tmp94) == 1:
                                    tmp95 = tmp94[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp95)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46339
                                    if len(subjects25) == 0:
                                        pass
                                        # State 46340
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (b*(c*x**n)**p)**q
                                            yield 1, subst2
                                if len(subjects25) == 0:
                                    break
                                tmp94.append(subjects25.popleft())
                            subjects25.extendleft(reversed(tmp94))
                    if pattern_index == 1:
                        pass
                        # State 47016
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47017
                            if len(subjects25) == 0:
                                pass
                                # State 47018
                                if len(subjects) == 0:
                                    pass
                                    # 2: (e1*(a + b*x)/(a + x*b))**n
                                    yield 2, subst2
                        if len(subjects25) >= 1:
                            tmp98 = []
                            tmp98.append(subjects25.popleft())
                            while True:
                                if len(tmp98) > 1:
                                    tmp99 = create_operation_expression(associative1, tmp98)
                                elif len(tmp98) == 1:
                                    tmp99 = tmp98[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp99)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47017
                                    if len(subjects25) == 0:
                                        pass
                                        # State 47018
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (e1*(a + b*x)/(a + x*b))**n
                                            yield 2, subst2
                                if len(subjects25) == 0:
                                    break
                                tmp98.append(subjects25.popleft())
                            subjects25.extendleft(reversed(tmp98))
                    if pattern_index == 2:
                        pass
                        # State 47864
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47865
                            if len(subjects25) == 0:
                                pass
                                # State 47866
                                if len(subjects) == 0:
                                    pass
                                    # 3: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                                    yield 3, subst2
                        if len(subjects25) >= 1:
                            tmp102 = []
                            tmp102.append(subjects25.popleft())
                            while True:
                                if len(tmp102) > 1:
                                    tmp103 = create_operation_expression(associative1, tmp102)
                                elif len(tmp102) == 1:
                                    tmp103 = tmp102[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp103)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47865
                                    if len(subjects25) == 0:
                                        pass
                                        # State 47866
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                                            yield 3, subst2
                                if len(subjects25) == 0:
                                    break
                                tmp102.append(subjects25.popleft())
                            subjects25.extendleft(reversed(tmp102))
                    if pattern_index == 3:
                        pass
                        # State 48382
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48383
                            if len(subjects25) == 0:
                                pass
                                # State 48384
                                if len(subjects) == 0:
                                    pass
                                    # 7: (e1*(e + x*f)**n2*(x*b + a)**n1)**n
                                    yield 7, subst2
                        if len(subjects25) >= 1:
                            tmp106 = []
                            tmp106.append(subjects25.popleft())
                            while True:
                                if len(tmp106) > 1:
                                    tmp107 = create_operation_expression(associative1, tmp106)
                                elif len(tmp106) == 1:
                                    tmp107 = tmp106[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp107)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48383
                                    if len(subjects25) == 0:
                                        pass
                                        # State 48384
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (e1*(e + x*f)**n2*(x*b + a)**n1)**n
                                            yield 7, subst2
                                if len(subjects25) == 0:
                                    break
                                tmp106.append(subjects25.popleft())
                            subjects25.extendleft(reversed(tmp106))
                    if pattern_index == 4:
                        pass
                        # State 48672
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48673
                            if len(subjects25) == 0:
                                pass
                                # State 48674
                                if len(subjects) == 0:
                                    pass
                                    # 8: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                                    yield 8, subst2
                        if len(subjects25) >= 1:
                            tmp110 = []
                            tmp110.append(subjects25.popleft())
                            while True:
                                if len(tmp110) > 1:
                                    tmp111 = create_operation_expression(associative1, tmp110)
                                elif len(tmp110) == 1:
                                    tmp111 = tmp110[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp111)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48673
                                    if len(subjects25) == 0:
                                        pass
                                        # State 48674
                                        if len(subjects) == 0:
                                            pass
                                            # 8: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                                            yield 8, subst2
                                if len(subjects25) == 0:
                                    break
                                tmp110.append(subjects25.popleft())
                            subjects25.extendleft(reversed(tmp110))
                    if pattern_index == 5:
                        pass
                        # State 49114
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49115
                            if len(subjects25) == 0:
                                pass
                                # State 49116
                                if len(subjects) == 0:
                                    pass
                                    # 9: (e1*(c + x*d)**n2*(c + x*d)**n1)**n
                                    yield 9, subst2
                        if len(subjects25) >= 1:
                            tmp114 = []
                            tmp114.append(subjects25.popleft())
                            while True:
                                if len(tmp114) > 1:
                                    tmp115 = create_operation_expression(associative1, tmp114)
                                elif len(tmp114) == 1:
                                    tmp115 = tmp114[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp115)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49115
                                    if len(subjects25) == 0:
                                        pass
                                        # State 49116
                                        if len(subjects) == 0:
                                            pass
                                            # 9: (e1*(c + x*d)**n2*(c + x*d)**n1)**n
                                            yield 9, subst2
                                if len(subjects25) == 0:
                                    break
                                tmp114.append(subjects25.popleft())
                            subjects25.extendleft(reversed(tmp114))
                subjects25.appendleft(tmp91)
            subjects.appendleft(tmp24)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp117 = subjects.popleft()
            associative1 = tmp117
            associative_type1 = type(tmp117)
            subjects118 = deque(tmp117._args)
            matcher = CommutativeMatcher48132.get()
            tmp119 = subjects118
            subjects118 = []
            for s in tmp119:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp119, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 48138
                    if len(subjects) == 0:
                        pass
                        # 5: x*b + a
                        yield 5, subst1
            subjects.appendleft(tmp117)
        return
        yield


from .generated_part006732 import *
from .generated_part006729 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part006734 import *
from .generated_part006715 import *
from collections import deque
from .generated_part006747 import *
from .generated_part006717 import *
from .generated_part006730 import *
from .generated_part006731 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part006714 import *