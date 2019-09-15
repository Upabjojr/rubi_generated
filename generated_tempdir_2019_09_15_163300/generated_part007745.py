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


class CommutativeMatcher56442(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1, 9: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({10: 1, 11: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    10: (10, Multiset({12: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    11: (11, Multiset({13: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    12: (12, Multiset({14: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    13: (13, Multiset({15: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    14: (14, Multiset({16: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher56442._instance is None:
            CommutativeMatcher56442._instance = CommutativeMatcher56442()
        return CommutativeMatcher56442._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 56441
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 56443
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 56444
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 122299
                    if len(subjects) == 0:
                        pass
                        # 3: d*x
                        yield 3, subst2
                subjects.appendleft(tmp4)
            if len(subjects) >= 1:
                tmp6 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 122353
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                        yield 4, subst2
                subjects.appendleft(tmp6)
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125671
                    if len(subjects) == 0:
                        pass
                        # 9: x*b
                        yield 9, subst2
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 56471
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 56472
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                        yield 1, subst2
                subjects.appendleft(tmp11)
            if len(subjects) >= 1:
                tmp13 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1.0', tmp13)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132534
                    if len(subjects) == 0:
                        pass
                        # 15: e*x
                        yield 15, subst2
                subjects.appendleft(tmp13)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp15 = subjects.popleft()
                subjects16 = deque(tmp15._args)
                # State 123490
                if len(subjects16) >= 1:
                    tmp17 = subjects16.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp17)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 123491
                        if len(subjects16) >= 1:
                            tmp19 = subjects16.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp19)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 123492
                                if len(subjects16) == 0:
                                    pass
                                    # State 123493
                                    if len(subjects) == 0:
                                        pass
                                        # 5: x**n*b
                                        yield 5, subst3
                            subjects16.appendleft(tmp19)
                    subjects16.appendleft(tmp17)
                if len(subjects16) >= 1:
                    tmp21 = subjects16.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp21)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124499
                        if len(subjects16) >= 1:
                            tmp23 = subjects16.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp23)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124500
                                if len(subjects16) == 0:
                                    pass
                                    # State 124501
                                    if len(subjects) == 0:
                                        pass
                                        # 6: x**n*b
                                        yield 6, subst3
                            subjects16.appendleft(tmp23)
                    subjects16.appendleft(tmp21)
                if len(subjects16) >= 1:
                    tmp25 = subjects16.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.0', tmp25)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125664
                        if len(subjects16) >= 1 and subjects16[0] == Integer(2):
                            tmp27 = subjects16.popleft()
                            # State 125665
                            if len(subjects16) == 0:
                                pass
                                # State 125666
                                if len(subjects) == 0:
                                    pass
                                    # 8: x**2*c
                                    yield 8, subst2
                            subjects16.appendleft(tmp27)
                    subjects16.appendleft(tmp25)
                subjects.appendleft(tmp15)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp28 = subjects.popleft()
                subjects29 = deque(tmp28._args)
                # State 134605
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 134606
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 134607
                        if len(subjects29) >= 1:
                            tmp32 = subjects29.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1', tmp32)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 134608
                                if len(subjects29) == 0:
                                    pass
                                    # State 134609
                                    if len(subjects) == 0:
                                        pass
                                        # 16: b*log(x**n*c)
                                        yield 16, subst4
                            subjects29.appendleft(tmp32)
                    if len(subjects29) >= 1 and isinstance(subjects29[0], Pow):
                        tmp34 = subjects29.popleft()
                        subjects35 = deque(tmp34._args)
                        # State 134610
                        if len(subjects35) >= 1:
                            tmp36 = subjects35.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1', tmp36)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 134611
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 134612
                                    if len(subjects35) == 0:
                                        pass
                                        # State 134613
                                        if len(subjects29) == 0:
                                            pass
                                            # State 134614
                                            if len(subjects) == 0:
                                                pass
                                                # 16: b*log(x**n*c)
                                                yield 16, subst4
                                if len(subjects35) >= 1:
                                    tmp39 = subjects35.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', tmp39)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 134612
                                        if len(subjects35) == 0:
                                            pass
                                            # State 134613
                                            if len(subjects29) == 0:
                                                pass
                                                # State 134614
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: b*log(x**n*c)
                                                    yield 16, subst4
                                    subjects35.appendleft(tmp39)
                            subjects35.appendleft(tmp36)
                        subjects29.appendleft(tmp34)
                if len(subjects29) >= 1 and isinstance(subjects29[0], Mul):
                    tmp41 = subjects29.popleft()
                    associative1 = tmp41
                    associative_type1 = type(tmp41)
                    subjects42 = deque(tmp41._args)
                    matcher = CommutativeMatcher134616.get()
                    tmp43 = subjects42
                    subjects42 = []
                    for s in tmp43:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp43, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 134623
                            if len(subjects29) == 0:
                                pass
                                # State 134624
                                if len(subjects) == 0:
                                    pass
                                    # 16: b*log(x**n*c)
                                    yield 16, subst2
                    subjects29.appendleft(tmp41)
                subjects.appendleft(tmp28)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 121613
            if len(subjects) >= 1:
                tmp45 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp45)
                except ValueError:
                    pass
                else:
                    pass
                    # State 121614
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst2
                subjects.appendleft(tmp45)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp47 = subjects.popleft()
                subjects48 = deque(tmp47._args)
                # State 125700
                if len(subjects48) >= 1:
                    tmp49 = subjects48.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp49)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125701
                        if len(subjects48) >= 1 and subjects48[0] == Integer(2):
                            tmp51 = subjects48.popleft()
                            # State 125702
                            if len(subjects48) == 0:
                                pass
                                # State 125703
                                if len(subjects) == 0:
                                    pass
                                    # 10: x**2*c
                                    yield 10, subst2
                            subjects48.appendleft(tmp51)
                    subjects48.appendleft(tmp49)
                subjects.appendleft(tmp47)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 125423
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 125424
                if len(subjects) >= 1:
                    tmp54 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1', tmp54)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125425
                        if len(subjects) == 0:
                            pass
                            # 7: x**n*b
                            yield 7, subst3
                    subjects.appendleft(tmp54)
            if len(subjects) >= 1:
                tmp56 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp56)
                except ValueError:
                    pass
                else:
                    pass
                    # State 131961
                    if len(subjects) == 0:
                        pass
                        # 13: x*b
                        yield 13, subst2
                subjects.appendleft(tmp56)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp58 = subjects.popleft()
                subjects59 = deque(tmp58._args)
                # State 125426
                if len(subjects59) >= 1:
                    tmp60 = subjects59.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp60)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125427
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 125428
                            if len(subjects59) == 0:
                                pass
                                # State 125429
                                if len(subjects) == 0:
                                    pass
                                    # 7: x**n*b
                                    yield 7, subst3
                        if len(subjects59) >= 1:
                            tmp63 = subjects59.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp63)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125428
                                if len(subjects59) == 0:
                                    pass
                                    # State 125429
                                    if len(subjects) == 0:
                                        pass
                                        # 7: x**n*b
                                        yield 7, subst3
                            subjects59.appendleft(tmp63)
                    subjects59.appendleft(tmp60)
                subjects.appendleft(tmp58)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 125708
            if len(subjects) >= 1:
                tmp66 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp66)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125709
                    if len(subjects) == 0:
                        pass
                        # 11: x*b
                        yield 11, subst2
                subjects.appendleft(tmp66)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 131925
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.4.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 131926
                if len(subjects) >= 1:
                    tmp70 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.4.1.1', tmp70)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131927
                        if len(subjects) == 0:
                            pass
                            # 12: b*x**n
                            yield 12, subst3
                    subjects.appendleft(tmp70)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp72 = subjects.popleft()
                subjects73 = deque(tmp72._args)
                # State 131928
                if len(subjects73) >= 1:
                    tmp74 = subjects73.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.1', tmp74)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131929
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 131930
                            if len(subjects73) == 0:
                                pass
                                # State 131931
                                if len(subjects) == 0:
                                    pass
                                    # 12: b*x**n
                                    yield 12, subst3
                        if len(subjects73) >= 1:
                            tmp77 = subjects73.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.2', tmp77)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 131930
                                if len(subjects73) == 0:
                                    pass
                                    # State 131931
                                    if len(subjects) == 0:
                                        pass
                                        # 12: b*x**n
                                        yield 12, subst3
                            subjects73.appendleft(tmp77)
                    subjects73.appendleft(tmp74)
                subjects.appendleft(tmp72)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132313
            if len(subjects) >= 1:
                tmp80 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp80)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132314
                    if len(subjects) == 0:
                        pass
                        # 14: x*b
                        yield 14, subst2
                subjects.appendleft(tmp80)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp82 = subjects.popleft()
            associative1 = tmp82
            associative_type1 = type(tmp82)
            subjects83 = deque(tmp82._args)
            matcher = CommutativeMatcher56446.get()
            tmp84 = subjects83
            subjects83 = []
            for s in tmp84:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp84, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 56447
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 56473
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 121615
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 122300
                    if len(subjects) == 0:
                        pass
                        # 3: d*x
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 122354
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 123498
                    if len(subjects) == 0:
                        pass
                        # 5: x**n*b
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 124505
                    if len(subjects) == 0:
                        pass
                        # 6: x**n*b
                        yield 6, subst1
                if pattern_index == 7:
                    pass
                    # State 125434
                    if len(subjects) == 0:
                        pass
                        # 7: x**n*b
                        yield 7, subst1
                if pattern_index == 8:
                    pass
                    # State 125670
                    if len(subjects) == 0:
                        pass
                        # 8: x**2*c
                        yield 8, subst1
                if pattern_index == 9:
                    pass
                    # State 125672
                    if len(subjects) == 0:
                        pass
                        # 9: x*b
                        yield 9, subst1
                if pattern_index == 10:
                    pass
                    # State 125707
                    if len(subjects) == 0:
                        pass
                        # 10: x**2*c
                        yield 10, subst1
                if pattern_index == 11:
                    pass
                    # State 125710
                    if len(subjects) == 0:
                        pass
                        # 11: x*b
                        yield 11, subst1
                if pattern_index == 12:
                    pass
                    # State 131937
                    if len(subjects) == 0:
                        pass
                        # 12: b*x**n
                        yield 12, subst1
                if pattern_index == 13:
                    pass
                    # State 131962
                    if len(subjects) == 0:
                        pass
                        # 13: x*b
                        yield 13, subst1
                if pattern_index == 14:
                    pass
                    # State 132315
                    if len(subjects) == 0:
                        pass
                        # 14: x*b
                        yield 14, subst1
                if pattern_index == 15:
                    pass
                    # State 132535
                    if len(subjects) == 0:
                        pass
                        # 15: e*x
                        yield 15, subst1
                if pattern_index == 16:
                    pass
                    # State 134645
                    if len(subjects) == 0:
                        pass
                        # 16: b*log(x**n*c)
                        yield 16, subst1
            subjects.appendleft(tmp82)
        return
        yield


from .generated_part007746 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part007747 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset