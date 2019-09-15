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


class CommutativeMatcher21859(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher21859._instance is None:
            CommutativeMatcher21859._instance = CommutativeMatcher21859()
        return CommutativeMatcher21859._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 21858
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 21860
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 21861
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 21862
                    if len(subjects) >= 1:
                        tmp4 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', tmp4)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21863
                            if len(subjects) == 0:
                                pass
                                # 0: (e + x*f)**p
                                yield 0, subst4
                        subjects.appendleft(tmp4)
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 35710
                    if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                        tmp7 = subjects.popleft()
                        subjects8 = deque(tmp7._args)
                        # State 35711
                        if len(subjects8) >= 1:
                            tmp9 = subjects8.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.1.1', tmp9)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 35712
                                if len(subjects8) >= 1:
                                    tmp11 = subjects8.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.2', tmp11)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35713
                                        if len(subjects8) == 0:
                                            pass
                                            # State 35714
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (e + f*x**m)**p
                                                yield 4, subst5
                                    subjects8.appendleft(tmp11)
                            subjects8.appendleft(tmp9)
                        if len(subjects8) >= 1:
                            tmp13 = subjects8.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.1', tmp13)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 40096
                                if len(subjects8) >= 1:
                                    tmp15 = subjects8.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2', tmp15)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 40097
                                        if len(subjects8) == 0:
                                            pass
                                            # State 40098
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (x**j*f + e)**p
                                                yield 5, subst5
                                    subjects8.appendleft(tmp15)
                            subjects8.appendleft(tmp13)
                        subjects.appendleft(tmp7)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp17 = subjects.popleft()
                    associative1 = tmp17
                    associative_type1 = type(tmp17)
                    subjects18 = deque(tmp17._args)
                    matcher = CommutativeMatcher21865.get()
                    tmp19 = subjects18
                    subjects18 = []
                    for s in tmp19:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp19, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 21866
                            if len(subjects) == 0:
                                pass
                                # 0: (e + x*f)**p
                                yield 0, subst3
                        if pattern_index == 1:
                            pass
                            # State 35719
                            if len(subjects) == 0:
                                pass
                                # 4: (e + f*x**m)**p
                                yield 4, subst3
                        if pattern_index == 2:
                            pass
                            # State 40102
                            if len(subjects) == 0:
                                pass
                                # 5: (x**j*f + e)**p
                                yield 5, subst3
                    subjects.appendleft(tmp17)
            if len(subjects) >= 1:
                tmp20 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1', tmp20)
                except ValueError:
                    pass
                else:
                    pass
                    # State 45755
                    if len(subjects) == 0:
                        pass
                        # 7: v**p
                        yield 7, subst2
                subjects.appendleft(tmp20)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp22 = subjects.popleft()
                associative1 = tmp22
                associative_type1 = type(tmp22)
                subjects23 = deque(tmp22._args)
                matcher = CommutativeMatcher21868.get()
                tmp24 = subjects23
                subjects23 = []
                for s in tmp24:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp24, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 21874
                        if len(subjects) == 0:
                            pass
                            # 0: (e + x*f)**p
                            yield 0, subst2
                    if pattern_index == 1:
                        pass
                        # State 29868
                        if len(subjects) == 0:
                            pass
                            # 2: (e + f*x**m)**p
                            yield 2, subst2
                    if pattern_index == 2:
                        pass
                        # State 35720
                        if len(subjects) == 0:
                            pass
                            # 4: (e + f*x**m)**p
                            yield 4, subst2
                    if pattern_index == 3:
                        pass
                        # State 40110
                        if len(subjects) == 0:
                            pass
                            # 5: (x**j*f + e)**p
                            yield 5, subst2
                    if pattern_index == 4:
                        pass
                        # State 44738
                        if len(subjects) == 0:
                            pass
                            # 6: (e + f*x + g*x**2)**p
                            yield 6, subst2
                subjects.appendleft(tmp22)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp25 = subjects.popleft()
                associative1 = tmp25
                associative_type1 = type(tmp25)
                subjects26 = deque(tmp25._args)
                matcher = CommutativeMatcher33327.get()
                tmp27 = subjects26
                subjects26 = []
                for s in tmp27:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp27, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 33351
                        if len(subjects) == 0:
                            pass
                            # 3: (x**m*(f + e*x**r))**p
                            yield 3, subst2
                subjects.appendleft(tmp25)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp28 = subjects.popleft()
            subjects29 = deque(tmp28._args)
            # State 21875
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 21876
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 21877
                    if len(subjects29) >= 1:
                        tmp32 = subjects29.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0', tmp32)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21878
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 21879
                                if len(subjects29) == 0:
                                    pass
                                    # State 21880
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (e + x*f)**p
                                        yield 0, subst4
                            if len(subjects29) >= 1:
                                tmp35 = subjects29.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp35)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21879
                                    if len(subjects29) == 0:
                                        pass
                                        # State 21880
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (e + x*f)**p
                                            yield 0, subst4
                                subjects29.appendleft(tmp35)
                        subjects29.appendleft(tmp32)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 35721
                    if len(subjects29) >= 1 and isinstance(subjects29[0], Pow):
                        tmp38 = subjects29.popleft()
                        subjects39 = deque(tmp38._args)
                        # State 35722
                        if len(subjects39) >= 1:
                            tmp40 = subjects39.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2.1.1', tmp40)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 35723
                                if len(subjects39) >= 1:
                                    tmp42 = subjects39.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2.1.2', tmp42)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35724
                                        if len(subjects39) == 0:
                                            pass
                                            # State 35725
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35726
                                                if len(subjects29) == 0:
                                                    pass
                                                    # State 35727
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (e + f*x**m)**p
                                                        yield 4, subst5
                                            if len(subjects29) >= 1:
                                                tmp45 = subjects29.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp45)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 35726
                                                    if len(subjects29) == 0:
                                                        pass
                                                        # State 35727
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (e + f*x**m)**p
                                                            yield 4, subst5
                                                subjects29.appendleft(tmp45)
                                    subjects39.appendleft(tmp42)
                            subjects39.appendleft(tmp40)
                        if len(subjects39) >= 1:
                            tmp47 = subjects39.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.1', tmp47)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 40111
                                if len(subjects39) >= 1:
                                    tmp49 = subjects39.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2', tmp49)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 40112
                                        if len(subjects39) == 0:
                                            pass
                                            # State 40113
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 40114
                                                if len(subjects29) == 0:
                                                    pass
                                                    # State 40115
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (x**j*f + e)**p
                                                        yield 5, subst5
                                            if len(subjects29) >= 1:
                                                tmp52 = subjects29.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp52)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 40114
                                                    if len(subjects29) == 0:
                                                        pass
                                                        # State 40115
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (x**j*f + e)**p
                                                            yield 5, subst5
                                                subjects29.appendleft(tmp52)
                                    subjects39.appendleft(tmp49)
                            subjects39.appendleft(tmp47)
                        subjects29.appendleft(tmp38)
                if len(subjects29) >= 1 and isinstance(subjects29[0], Mul):
                    tmp54 = subjects29.popleft()
                    associative1 = tmp54
                    associative_type1 = type(tmp54)
                    subjects55 = deque(tmp54._args)
                    matcher = CommutativeMatcher21882.get()
                    tmp56 = subjects55
                    subjects55 = []
                    for s in tmp56:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp56, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 21883
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 21884
                                if len(subjects29) == 0:
                                    pass
                                    # State 21885
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (e + x*f)**p
                                        yield 0, subst3
                            if len(subjects29) >= 1:
                                tmp58 = []
                                tmp58.append(subjects29.popleft())
                                while True:
                                    if len(tmp58) > 1:
                                        tmp59 = create_operation_expression(associative1, tmp58)
                                    elif len(tmp58) == 1:
                                        tmp59 = tmp58[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2.2.2', tmp59)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 21884
                                        if len(subjects29) == 0:
                                            pass
                                            # State 21885
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (e + x*f)**p
                                                yield 0, subst3
                                    if len(subjects29) == 0:
                                        break
                                    tmp58.append(subjects29.popleft())
                                subjects29.extendleft(reversed(tmp58))
                        if pattern_index == 1:
                            pass
                            # State 35732
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 35733
                                if len(subjects29) == 0:
                                    pass
                                    # State 35734
                                    if len(subjects) == 0:
                                        pass
                                        # 4: (e + f*x**m)**p
                                        yield 4, subst3
                            if len(subjects29) >= 1:
                                tmp62 = []
                                tmp62.append(subjects29.popleft())
                                while True:
                                    if len(tmp62) > 1:
                                        tmp63 = create_operation_expression(associative1, tmp62)
                                    elif len(tmp62) == 1:
                                        tmp63 = tmp62[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2.2.2', tmp63)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35733
                                        if len(subjects29) == 0:
                                            pass
                                            # State 35734
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (e + f*x**m)**p
                                                yield 4, subst3
                                    if len(subjects29) == 0:
                                        break
                                    tmp62.append(subjects29.popleft())
                                subjects29.extendleft(reversed(tmp62))
                        if pattern_index == 2:
                            pass
                            # State 40119
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 40120
                                if len(subjects29) == 0:
                                    pass
                                    # State 40121
                                    if len(subjects) == 0:
                                        pass
                                        # 5: (x**j*f + e)**p
                                        yield 5, subst3
                            if len(subjects29) >= 1:
                                tmp66 = []
                                tmp66.append(subjects29.popleft())
                                while True:
                                    if len(tmp66) > 1:
                                        tmp67 = create_operation_expression(associative1, tmp66)
                                    elif len(tmp66) == 1:
                                        tmp67 = tmp66[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2.2.2', tmp67)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 40120
                                        if len(subjects29) == 0:
                                            pass
                                            # State 40121
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (x**j*f + e)**p
                                                yield 5, subst3
                                    if len(subjects29) == 0:
                                        break
                                    tmp66.append(subjects29.popleft())
                                subjects29.extendleft(reversed(tmp66))
                    subjects29.appendleft(tmp54)
            if len(subjects29) >= 1:
                tmp69 = subjects29.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.2.1', tmp69)
                except ValueError:
                    pass
                else:
                    pass
                    # State 25802
                    if len(subjects29) >= 1:
                        tmp71 = subjects29.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', tmp71)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25803
                            if len(subjects29) == 0:
                                pass
                                # State 25804
                                if len(subjects) == 0:
                                    pass
                                    # 1: v**p
                                    yield 1, subst2
                        subjects29.appendleft(tmp71)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 45756
                        if len(subjects29) == 0:
                            pass
                            # State 45757
                            if len(subjects) == 0:
                                pass
                                # 7: v**p
                                yield 7, subst2
                    if len(subjects29) >= 1:
                        tmp74 = subjects29.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', tmp74)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45756
                            if len(subjects29) == 0:
                                pass
                                # State 45757
                                if len(subjects) == 0:
                                    pass
                                    # 7: v**p
                                    yield 7, subst2
                        subjects29.appendleft(tmp74)
                subjects29.appendleft(tmp69)
            if len(subjects29) >= 1 and isinstance(subjects29[0], Add):
                tmp76 = subjects29.popleft()
                associative1 = tmp76
                associative_type1 = type(tmp76)
                subjects77 = deque(tmp76._args)
                matcher = CommutativeMatcher21887.get()
                tmp78 = subjects77
                subjects77 = []
                for s in tmp78:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp78, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 21893
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21894
                            if len(subjects29) == 0:
                                pass
                                # State 21895
                                if len(subjects) == 0:
                                    pass
                                    # 0: (e + x*f)**p
                                    yield 0, subst2
                        if len(subjects29) >= 1:
                            tmp80 = []
                            tmp80.append(subjects29.popleft())
                            while True:
                                if len(tmp80) > 1:
                                    tmp81 = create_operation_expression(associative1, tmp80)
                                elif len(tmp80) == 1:
                                    tmp81 = tmp80[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp81)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21894
                                    if len(subjects29) == 0:
                                        pass
                                        # State 21895
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (e + x*f)**p
                                            yield 0, subst2
                                if len(subjects29) == 0:
                                    break
                                tmp80.append(subjects29.popleft())
                            subjects29.extendleft(reversed(tmp80))
                    if pattern_index == 1:
                        pass
                        # State 29879
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 29880
                            if len(subjects29) == 0:
                                pass
                                # State 29881
                                if len(subjects) == 0:
                                    pass
                                    # 2: (e + f*x**m)**p
                                    yield 2, subst2
                        if len(subjects29) >= 1:
                            tmp84 = []
                            tmp84.append(subjects29.popleft())
                            while True:
                                if len(tmp84) > 1:
                                    tmp85 = create_operation_expression(associative1, tmp84)
                                elif len(tmp84) == 1:
                                    tmp85 = tmp84[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp85)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 29880
                                    if len(subjects29) == 0:
                                        pass
                                        # State 29881
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (e + f*x**m)**p
                                            yield 2, subst2
                                if len(subjects29) == 0:
                                    break
                                tmp84.append(subjects29.popleft())
                            subjects29.extendleft(reversed(tmp84))
                    if pattern_index == 2:
                        pass
                        # State 35735
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35736
                            if len(subjects29) == 0:
                                pass
                                # State 35737
                                if len(subjects) == 0:
                                    pass
                                    # 4: (e + f*x**m)**p
                                    yield 4, subst2
                        if len(subjects29) >= 1:
                            tmp88 = []
                            tmp88.append(subjects29.popleft())
                            while True:
                                if len(tmp88) > 1:
                                    tmp89 = create_operation_expression(associative1, tmp88)
                                elif len(tmp88) == 1:
                                    tmp89 = tmp88[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp89)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35736
                                    if len(subjects29) == 0:
                                        pass
                                        # State 35737
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (e + f*x**m)**p
                                            yield 4, subst2
                                if len(subjects29) == 0:
                                    break
                                tmp88.append(subjects29.popleft())
                            subjects29.extendleft(reversed(tmp88))
                    if pattern_index == 3:
                        pass
                        # State 40129
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40130
                            if len(subjects29) == 0:
                                pass
                                # State 40131
                                if len(subjects) == 0:
                                    pass
                                    # 5: (x**j*f + e)**p
                                    yield 5, subst2
                        if len(subjects29) >= 1:
                            tmp92 = []
                            tmp92.append(subjects29.popleft())
                            while True:
                                if len(tmp92) > 1:
                                    tmp93 = create_operation_expression(associative1, tmp92)
                                elif len(tmp92) == 1:
                                    tmp93 = tmp92[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp93)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40130
                                    if len(subjects29) == 0:
                                        pass
                                        # State 40131
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (x**j*f + e)**p
                                            yield 5, subst2
                                if len(subjects29) == 0:
                                    break
                                tmp92.append(subjects29.popleft())
                            subjects29.extendleft(reversed(tmp92))
                    if pattern_index == 4:
                        pass
                        # State 44746
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 44747
                            if len(subjects29) == 0:
                                pass
                                # State 44748
                                if len(subjects) == 0:
                                    pass
                                    # 6: (e + f*x + g*x**2)**p
                                    yield 6, subst2
                        if len(subjects29) >= 1:
                            tmp96 = []
                            tmp96.append(subjects29.popleft())
                            while True:
                                if len(tmp96) > 1:
                                    tmp97 = create_operation_expression(associative1, tmp96)
                                elif len(tmp96) == 1:
                                    tmp97 = tmp96[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp97)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44747
                                    if len(subjects29) == 0:
                                        pass
                                        # State 44748
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (e + f*x + g*x**2)**p
                                            yield 6, subst2
                                if len(subjects29) == 0:
                                    break
                                tmp96.append(subjects29.popleft())
                            subjects29.extendleft(reversed(tmp96))
                subjects29.appendleft(tmp76)
            if len(subjects29) >= 1 and isinstance(subjects29[0], Mul):
                tmp99 = subjects29.popleft()
                associative1 = tmp99
                associative_type1 = type(tmp99)
                subjects100 = deque(tmp99._args)
                matcher = CommutativeMatcher33353.get()
                tmp101 = subjects100
                subjects100 = []
                for s in tmp101:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp101, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 33377
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 33378
                            if len(subjects29) == 0:
                                pass
                                # State 33379
                                if len(subjects) == 0:
                                    pass
                                    # 3: (x**m*(f + e*x**r))**p
                                    yield 3, subst2
                        if len(subjects29) >= 1:
                            tmp103 = []
                            tmp103.append(subjects29.popleft())
                            while True:
                                if len(tmp103) > 1:
                                    tmp104 = create_operation_expression(associative1, tmp103)
                                elif len(tmp103) == 1:
                                    tmp104 = tmp103[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp104)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 33378
                                    if len(subjects29) == 0:
                                        pass
                                        # State 33379
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (x**m*(f + e*x**r))**p
                                            yield 3, subst2
                                if len(subjects29) == 0:
                                    break
                                tmp103.append(subjects29.popleft())
                            subjects29.extendleft(reversed(tmp103))
                subjects29.appendleft(tmp99)
            subjects.appendleft(tmp28)
        return
        yield


from .generated_part005305 import *
from .generated_part005307 import *
from .generated_part005310 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part005313 import *
from collections import deque
from .generated_part005311 import *
from .generated_part005304 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset