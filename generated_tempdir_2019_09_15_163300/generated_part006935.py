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


class CommutativeMatcher57250(CommutativeMatcher):
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
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1, 9: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({10: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    10: (10, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.2.3.0', 1, 1, S(0)), Add)
]),
    11: (11, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.4.0', 1, 1, S(0)), Add)
]),
    12: (12, Multiset({13: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    13: (13, Multiset({14: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    14: (14, Multiset({9: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    15: (15, Multiset({15: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    16: (16, Multiset({16: 1}), [
      (VariableWithCount('i2.3.0_2', 1, 1, S(0)), Add)
]),
    17: (17, Multiset({17: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    18: (18, Multiset({18: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    19: (19, Multiset({19: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    20: (20, Multiset({20: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    21: (21, Multiset({20: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, None), Add)
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
        if CommutativeMatcher57250._instance is None:
            CommutativeMatcher57250._instance = CommutativeMatcher57250()
        return CommutativeMatcher57250._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 57249
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 57251
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 57252
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
            # State 58519
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58520
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
            # State 64332
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 64333
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
            # State 65672
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 65673
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst2
                subjects.appendleft(tmp11)
            if len(subjects) >= 1:
                tmp13 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp13)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75809
                    if len(subjects) == 0:
                        pass
                        # 9: x*b
                        yield 9, subst2
                subjects.appendleft(tmp13)
            if len(subjects) >= 1:
                tmp15 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1.0', tmp15)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103847
                    if len(subjects) == 0:
                        pass
                        # 15: e*x
                        yield 15, subst2
                subjects.appendleft(tmp15)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 68421
            if len(subjects) >= 1:
                tmp18 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0', tmp18)
                except ValueError:
                    pass
                else:
                    pass
                    # State 68422
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                        yield 4, subst2
                subjects.appendleft(tmp18)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 72082
            if len(subjects) >= 1:
                tmp21 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp21)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72083
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                        yield 5, subst2
                subjects.appendleft(tmp21)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 75472
                if len(subjects) >= 1:
                    tmp24 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1', tmp24)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75473
                        if len(subjects) == 0:
                            pass
                            # 7: x**n*b
                            yield 7, subst3
                    subjects.appendleft(tmp24)
            if len(subjects) >= 1:
                tmp26 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp26)
                except ValueError:
                    pass
                else:
                    pass
                    # State 100904
                    if len(subjects) == 0:
                        pass
                        # 13: x*b
                        yield 13, subst2
                subjects.appendleft(tmp26)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp28 = subjects.popleft()
                subjects29 = deque(tmp28._args)
                # State 74624
                if len(subjects29) >= 1:
                    tmp30 = subjects29.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp30)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74625
                        if len(subjects29) >= 1:
                            tmp32 = subjects29.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp32)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74626
                                if len(subjects29) == 0:
                                    pass
                                    # State 74627
                                    if len(subjects) == 0:
                                        pass
                                        # 6: x**n*b
                                        yield 6, subst3
                            subjects29.appendleft(tmp32)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 75474
                            if len(subjects29) == 0:
                                pass
                                # State 75475
                                if len(subjects) == 0:
                                    pass
                                    # 7: x**n*b
                                    yield 7, subst3
                        if len(subjects29) >= 1:
                            tmp35 = subjects29.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp35)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75474
                                if len(subjects29) == 0:
                                    pass
                                    # State 75475
                                    if len(subjects) == 0:
                                        pass
                                        # 7: x**n*b
                                        yield 7, subst3
                            subjects29.appendleft(tmp35)
                    subjects29.appendleft(tmp30)
                if len(subjects29) >= 1:
                    tmp37 = subjects29.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp37)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75802
                        if len(subjects29) >= 1 and subjects29[0] == Integer(2):
                            tmp39 = subjects29.popleft()
                            # State 75803
                            if len(subjects29) == 0:
                                pass
                                # State 75804
                                if len(subjects) == 0:
                                    pass
                                    # 8: v**2*c
                                    yield 8, subst2
                            subjects29.appendleft(tmp39)
                    subjects29.appendleft(tmp37)
                if len(subjects29) >= 1 and isinstance(subjects29[0], Add):
                    tmp40 = subjects29.popleft()
                    associative1 = tmp40
                    associative_type1 = type(tmp40)
                    subjects41 = deque(tmp40._args)
                    matcher = CommutativeMatcher107363.get()
                    tmp42 = subjects41
                    subjects41 = []
                    for s in tmp42:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp42, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 107369
                            if len(subjects29) >= 1:
                                tmp43 = []
                                tmp43.append(subjects29.popleft())
                                while True:
                                    if len(tmp43) > 1:
                                        tmp44 = create_operation_expression(associative1, tmp43)
                                    elif len(tmp43) == 1:
                                        tmp44 = tmp43[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.1.2', tmp44)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 107370
                                        if len(subjects29) == 0:
                                            pass
                                            # State 107371
                                            if len(subjects) == 0:
                                                pass
                                                # 18: b*(x*d + c)**n
                                                yield 18, subst3
                                    if len(subjects29) == 0:
                                        break
                                    tmp43.append(subjects29.popleft())
                                subjects29.extendleft(reversed(tmp43))
                    subjects29.appendleft(tmp40)
                subjects.appendleft(tmp28)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp46 = subjects.popleft()
                subjects47 = deque(tmp46._args)
                # State 104991
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 104992
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 104993
                        if len(subjects47) >= 1:
                            tmp50 = subjects47.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1', tmp50)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 104994
                                if len(subjects47) == 0:
                                    pass
                                    # State 104995
                                    if len(subjects) == 0:
                                        pass
                                        # 17: b*log(x**n*c)
                                        yield 17, subst4
                            subjects47.appendleft(tmp50)
                    if len(subjects47) >= 1 and isinstance(subjects47[0], Pow):
                        tmp52 = subjects47.popleft()
                        subjects53 = deque(tmp52._args)
                        # State 104996
                        if len(subjects53) >= 1:
                            tmp54 = subjects53.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1', tmp54)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 104997
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 104998
                                    if len(subjects53) == 0:
                                        pass
                                        # State 104999
                                        if len(subjects47) == 0:
                                            pass
                                            # State 105000
                                            if len(subjects) == 0:
                                                pass
                                                # 17: b*log(x**n*c)
                                                yield 17, subst4
                                if len(subjects53) >= 1:
                                    tmp57 = subjects53.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.1.2.2', tmp57)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 104998
                                        if len(subjects53) == 0:
                                            pass
                                            # State 104999
                                            if len(subjects47) == 0:
                                                pass
                                                # State 105000
                                                if len(subjects) == 0:
                                                    pass
                                                    # 17: b*log(x**n*c)
                                                    yield 17, subst4
                                    subjects53.appendleft(tmp57)
                            subjects53.appendleft(tmp54)
                        subjects47.appendleft(tmp52)
                if len(subjects47) >= 1 and isinstance(subjects47[0], Mul):
                    tmp59 = subjects47.popleft()
                    associative1 = tmp59
                    associative_type1 = type(tmp59)
                    subjects60 = deque(tmp59._args)
                    matcher = CommutativeMatcher105002.get()
                    tmp61 = subjects60
                    subjects60 = []
                    for s in tmp61:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp61, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 105009
                            if len(subjects47) == 0:
                                pass
                                # State 105010
                                if len(subjects) == 0:
                                    pass
                                    # 17: b*log(x**n*c)
                                    yield 17, subst2
                    subjects47.appendleft(tmp59)
                subjects.appendleft(tmp46)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 76607
            if len(subjects) >= 1:
                tmp63 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp63)
                except ValueError:
                    pass
                else:
                    pass
                    # State 76608
                    if len(subjects) == 0:
                        pass
                        # 10: x*f
                        yield 10, subst2
                subjects.appendleft(tmp63)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 85691
            if len(subjects) >= 1:
                tmp66 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.3.1.0', tmp66)
                except ValueError:
                    pass
                else:
                    pass
                    # State 85692
                    if len(subjects) == 0:
                        pass
                        # 11: x*d
                        yield 11, subst2
                subjects.appendleft(tmp66)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 85900
            if len(subjects) >= 1:
                tmp69 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.4.1.0', tmp69)
                except ValueError:
                    pass
                else:
                    pass
                    # State 85901
                    if len(subjects) == 0:
                        pass
                        # 12: x*d
                        yield 12, subst2
                subjects.appendleft(tmp69)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 103613
            if len(subjects) >= 1:
                tmp72 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp72)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103614
                    if len(subjects) == 0:
                        pass
                        # 14: x*f
                        yield 14, subst2
                subjects.appendleft(tmp72)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 104088
            if len(subjects) >= 1:
                tmp75 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp75)
                except ValueError:
                    pass
                else:
                    pass
                    # State 104089
                    if len(subjects) == 0:
                        pass
                        # 16: x*f
                        yield 16, subst2
                subjects.appendleft(tmp75)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 107708
            if len(subjects) >= 1:
                tmp78 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp78)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107709
                    if len(subjects) == 0:
                        pass
                        # 19: x*e
                        yield 19, subst2
                subjects.appendleft(tmp78)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 107822
            if len(subjects) >= 1:
                tmp81 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp81)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107823
                    if len(subjects) == 0:
                        pass
                        # 20: x*d
                        yield 20, subst2
                subjects.appendleft(tmp81)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp83 = subjects.popleft()
            associative1 = tmp83
            associative_type1 = type(tmp83)
            subjects84 = deque(tmp83._args)
            matcher = CommutativeMatcher57254.get()
            tmp85 = subjects84
            subjects84 = []
            for s in tmp85:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp85, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 57255
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 58521
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 64334
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 65674
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 68423
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 72084
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 74632
                    if len(subjects) == 0:
                        pass
                        # 6: x**n*b
                        yield 6, subst1
                if pattern_index == 7:
                    pass
                    # State 75480
                    if len(subjects) == 0:
                        pass
                        # 7: x**n*b
                        yield 7, subst1
                if pattern_index == 8:
                    pass
                    # State 75808
                    if len(subjects) == 0:
                        pass
                        # 8: v**2*c
                        yield 8, subst1
                if pattern_index == 9:
                    pass
                    # State 75810
                    if len(subjects) == 0:
                        pass
                        # 9: x*b
                        yield 9, subst1
                if pattern_index == 10:
                    pass
                    # State 76609
                    if len(subjects) == 0:
                        pass
                        # 10: x*f
                        yield 10, subst1
                if pattern_index == 11:
                    pass
                    # State 85693
                    if len(subjects) == 0:
                        pass
                        # 11: x*d
                        yield 11, subst1
                if pattern_index == 12:
                    pass
                    # State 85902
                    if len(subjects) == 0:
                        pass
                        # 12: x*d
                        yield 12, subst1
                if pattern_index == 13:
                    pass
                    # State 100905
                    if len(subjects) == 0:
                        pass
                        # 13: x*b
                        yield 13, subst1
                if pattern_index == 14:
                    pass
                    # State 103615
                    if len(subjects) == 0:
                        pass
                        # 14: x*f
                        yield 14, subst1
                if pattern_index == 15:
                    pass
                    # State 103848
                    if len(subjects) == 0:
                        pass
                        # 15: e*x
                        yield 15, subst1
                if pattern_index == 16:
                    pass
                    # State 104090
                    if len(subjects) == 0:
                        pass
                        # 16: x*f
                        yield 16, subst1
                if pattern_index == 17:
                    pass
                    # State 105031
                    if len(subjects) == 0:
                        pass
                        # 17: b*log(x**n*c)
                        yield 17, subst1
                if pattern_index == 18:
                    pass
                    # State 107382
                    if len(subjects) == 0:
                        pass
                        # 18: b*(x*d + c)**n
                        yield 18, subst1
                if pattern_index == 19:
                    pass
                    # State 107710
                    if len(subjects) == 0:
                        pass
                        # 19: x*e
                        yield 19, subst1
                if pattern_index == 20:
                    pass
                    # State 107824
                    if len(subjects) == 0:
                        pass
                        # 20: x*d
                        yield 20, subst1
            subjects.appendleft(tmp83)
        return
        yield


from .generated_part006936 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part006938 import *
from collections import deque
from .generated_part006939 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset