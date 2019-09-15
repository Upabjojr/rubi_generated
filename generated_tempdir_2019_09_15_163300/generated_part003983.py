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


class CommutativeMatcher23956(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({10: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher23956._instance is None:
            CommutativeMatcher23956._instance = CommutativeMatcher23956()
        return CommutativeMatcher23956._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 23955
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 23957
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.1.1.2.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 23958
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.0', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 23959
                        if len(subjects) == 0:
                            pass
                            # 0: e + f*x
                            yield 0, subst3
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp5 = subjects.popleft()
                associative1 = tmp5
                associative_type1 = type(tmp5)
                subjects6 = deque(tmp5._args)
                matcher = CommutativeMatcher23961.get()
                tmp7 = subjects6
                subjects6 = []
                for s in tmp7:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp7, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 23962
                        if len(subjects) == 0:
                            pass
                            # 0: e + f*x
                            yield 0, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 24587
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.1.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 24588
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.1.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 24589
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i2.1.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 24590
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24591
                            if len(subjects) >= 1:
                                tmp13 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.0', tmp13)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24592
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (d*(e + f*x)**p)**q
                                        yield 1, subst6
                                subjects.appendleft(tmp13)
                            if len(subjects) >= 1:
                                tmp15 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.1', tmp15)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26793
                                    if len(subjects) == 0:
                                        pass
                                        # 3: (d*(e + f*x)**p)**q
                                        yield 3, subst6
                                subjects.appendleft(tmp15)
                            if len(subjects) >= 1:
                                tmp17 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.3.1.0', tmp17)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27860
                                    if len(subjects) == 0:
                                        pass
                                        # 5: (d*(e + f*x)**p)**q
                                        yield 5, subst6
                                subjects.appendleft(tmp17)
                        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                            tmp19 = subjects.popleft()
                            associative1 = tmp19
                            associative_type1 = type(tmp19)
                            subjects20 = deque(tmp19._args)
                            matcher = CommutativeMatcher24594.get()
                            tmp21 = subjects20
                            subjects20 = []
                            for s in tmp21:
                                matcher.add_subject(s)
                            for pattern_index, subst5 in matcher.match(tmp21, subst4):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 24595
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (d*(e + f*x)**p)**q
                                        yield 1, subst5
                                if pattern_index == 1:
                                    pass
                                    # State 26794
                                    if len(subjects) == 0:
                                        pass
                                        # 3: (d*(e + f*x)**p)**q
                                        yield 3, subst5
                                if pattern_index == 2:
                                    pass
                                    # State 27861
                                    if len(subjects) == 0:
                                        pass
                                        # 5: (d*(e + f*x)**p)**q
                                        yield 5, subst5
                            subjects.appendleft(tmp19)
                    if len(subjects) >= 1 and isinstance(subjects[0], Add):
                        tmp22 = subjects.popleft()
                        associative1 = tmp22
                        associative_type1 = type(tmp22)
                        subjects23 = deque(tmp22._args)
                        matcher = CommutativeMatcher24597.get()
                        tmp24 = subjects23
                        subjects23 = []
                        for s in tmp24:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp24, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 24603
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d*(e + f*x)**p)**q
                                    yield 1, subst4
                            if pattern_index == 1:
                                pass
                                # State 26797
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x)**p)**q
                                    yield 3, subst4
                            if pattern_index == 2:
                                pass
                                # State 27319
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(e + f*x)**p)**q
                                    yield 4, subst4
                            if pattern_index == 3:
                                pass
                                # State 27864
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x)**p)**q
                                    yield 5, subst4
                        subjects.appendleft(tmp22)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp25 = subjects.popleft()
                    subjects26 = deque(tmp25._args)
                    # State 24604
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 24605
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24606
                            if len(subjects26) >= 1:
                                tmp29 = subjects26.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.0', tmp29)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24607
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 24608
                                        if len(subjects26) == 0:
                                            pass
                                            # State 24609
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (d*(e + f*x)**p)**q
                                                yield 1, subst6
                                    if len(subjects26) >= 1:
                                        tmp32 = subjects26.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2.2', tmp32)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24608
                                            if len(subjects26) == 0:
                                                pass
                                                # State 24609
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*(e + f*x)**p)**q
                                                    yield 1, subst6
                                        subjects26.appendleft(tmp32)
                                subjects26.appendleft(tmp29)
                            if len(subjects26) >= 1:
                                tmp34 = subjects26.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.1', tmp34)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26798
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 26799
                                        if len(subjects26) == 0:
                                            pass
                                            # State 26800
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (d*(e + f*x)**p)**q
                                                yield 3, subst6
                                    if len(subjects26) >= 1:
                                        tmp37 = subjects26.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2.2', tmp37)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26799
                                            if len(subjects26) == 0:
                                                pass
                                                # State 26800
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x)**p)**q
                                                    yield 3, subst6
                                        subjects26.appendleft(tmp37)
                                subjects26.appendleft(tmp34)
                            if len(subjects26) >= 1:
                                tmp39 = subjects26.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.3.1.0', tmp39)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27865
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27866
                                        if len(subjects26) == 0:
                                            pass
                                            # State 27867
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x)**p)**q
                                                yield 5, subst6
                                    if len(subjects26) >= 1:
                                        tmp42 = subjects26.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2.2', tmp42)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27866
                                            if len(subjects26) == 0:
                                                pass
                                                # State 27867
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x)**p)**q
                                                    yield 5, subst6
                                        subjects26.appendleft(tmp42)
                                subjects26.appendleft(tmp39)
                        if len(subjects26) >= 1 and isinstance(subjects26[0], Mul):
                            tmp44 = subjects26.popleft()
                            associative1 = tmp44
                            associative_type1 = type(tmp44)
                            subjects45 = deque(tmp44._args)
                            matcher = CommutativeMatcher24611.get()
                            tmp46 = subjects45
                            subjects45 = []
                            for s in tmp46:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp46, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 24612
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 24613
                                        if len(subjects26) == 0:
                                            pass
                                            # State 24614
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (d*(e + f*x)**p)**q
                                                yield 1, subst5
                                    if len(subjects26) >= 1:
                                        tmp48 = []
                                        tmp48.append(subjects26.popleft())
                                        while True:
                                            if len(tmp48) > 1:
                                                tmp49 = create_operation_expression(associative1, tmp48)
                                            elif len(tmp48) == 1:
                                                tmp49 = tmp48[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.2', tmp49)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24613
                                                if len(subjects26) == 0:
                                                    pass
                                                    # State 24614
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*(e + f*x)**p)**q
                                                        yield 1, subst5
                                            if len(subjects26) == 0:
                                                break
                                            tmp48.append(subjects26.popleft())
                                        subjects26.extendleft(reversed(tmp48))
                                if pattern_index == 1:
                                    pass
                                    # State 26801
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 26802
                                        if len(subjects26) == 0:
                                            pass
                                            # State 26803
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (d*(e + f*x)**p)**q
                                                yield 3, subst5
                                    if len(subjects26) >= 1:
                                        tmp52 = []
                                        tmp52.append(subjects26.popleft())
                                        while True:
                                            if len(tmp52) > 1:
                                                tmp53 = create_operation_expression(associative1, tmp52)
                                            elif len(tmp52) == 1:
                                                tmp53 = tmp52[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.2', tmp53)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26802
                                                if len(subjects26) == 0:
                                                    pass
                                                    # State 26803
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x)**p)**q
                                                        yield 3, subst5
                                            if len(subjects26) == 0:
                                                break
                                            tmp52.append(subjects26.popleft())
                                        subjects26.extendleft(reversed(tmp52))
                                if pattern_index == 2:
                                    pass
                                    # State 27868
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27869
                                        if len(subjects26) == 0:
                                            pass
                                            # State 27870
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x)**p)**q
                                                yield 5, subst5
                                    if len(subjects26) >= 1:
                                        tmp56 = []
                                        tmp56.append(subjects26.popleft())
                                        while True:
                                            if len(tmp56) > 1:
                                                tmp57 = create_operation_expression(associative1, tmp56)
                                            elif len(tmp56) == 1:
                                                tmp57 = tmp56[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.2', tmp57)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27869
                                                if len(subjects26) == 0:
                                                    pass
                                                    # State 27870
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x)**p)**q
                                                        yield 5, subst5
                                            if len(subjects26) == 0:
                                                break
                                            tmp56.append(subjects26.popleft())
                                        subjects26.extendleft(reversed(tmp56))
                            subjects26.appendleft(tmp44)
                    if len(subjects26) >= 1 and isinstance(subjects26[0], Add):
                        tmp59 = subjects26.popleft()
                        associative1 = tmp59
                        associative_type1 = type(tmp59)
                        subjects60 = deque(tmp59._args)
                        matcher = CommutativeMatcher24616.get()
                        tmp61 = subjects60
                        subjects60 = []
                        for s in tmp61:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp61, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 24622
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24623
                                    if len(subjects26) == 0:
                                        pass
                                        # State 24624
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*(e + f*x)**p)**q
                                            yield 1, subst4
                                if len(subjects26) >= 1:
                                    tmp63 = []
                                    tmp63.append(subjects26.popleft())
                                    while True:
                                        if len(tmp63) > 1:
                                            tmp64 = create_operation_expression(associative1, tmp63)
                                        elif len(tmp63) == 1:
                                            tmp64 = tmp63[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', tmp64)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24623
                                            if len(subjects26) == 0:
                                                pass
                                                # State 24624
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*(e + f*x)**p)**q
                                                    yield 1, subst4
                                        if len(subjects26) == 0:
                                            break
                                        tmp63.append(subjects26.popleft())
                                    subjects26.extendleft(reversed(tmp63))
                            if pattern_index == 1:
                                pass
                                # State 26806
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26807
                                    if len(subjects26) == 0:
                                        pass
                                        # State 26808
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x)**p)**q
                                            yield 3, subst4
                                if len(subjects26) >= 1:
                                    tmp67 = []
                                    tmp67.append(subjects26.popleft())
                                    while True:
                                        if len(tmp67) > 1:
                                            tmp68 = create_operation_expression(associative1, tmp67)
                                        elif len(tmp67) == 1:
                                            tmp68 = tmp67[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', tmp68)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26807
                                            if len(subjects26) == 0:
                                                pass
                                                # State 26808
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x)**p)**q
                                                    yield 3, subst4
                                        if len(subjects26) == 0:
                                            break
                                        tmp67.append(subjects26.popleft())
                                    subjects26.extendleft(reversed(tmp67))
                            if pattern_index == 2:
                                pass
                                # State 27320
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27321
                                    if len(subjects26) == 0:
                                        pass
                                        # State 27322
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(e + f*x)**p)**q
                                            yield 4, subst4
                                if len(subjects26) >= 1:
                                    tmp71 = []
                                    tmp71.append(subjects26.popleft())
                                    while True:
                                        if len(tmp71) > 1:
                                            tmp72 = create_operation_expression(associative1, tmp71)
                                        elif len(tmp71) == 1:
                                            tmp72 = tmp71[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', tmp72)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27321
                                            if len(subjects26) == 0:
                                                pass
                                                # State 27322
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(e + f*x)**p)**q
                                                    yield 4, subst4
                                        if len(subjects26) == 0:
                                            break
                                        tmp71.append(subjects26.popleft())
                                    subjects26.extendleft(reversed(tmp71))
                            if pattern_index == 3:
                                pass
                                # State 27873
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27874
                                    if len(subjects26) == 0:
                                        pass
                                        # State 27875
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x)**p)**q
                                            yield 5, subst4
                                if len(subjects26) >= 1:
                                    tmp75 = []
                                    tmp75.append(subjects26.popleft())
                                    while True:
                                        if len(tmp75) > 1:
                                            tmp76 = create_operation_expression(associative1, tmp75)
                                        elif len(tmp75) == 1:
                                            tmp76 = tmp75[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', tmp76)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27874
                                            if len(subjects26) == 0:
                                                pass
                                                # State 27875
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x)**p)**q
                                                    yield 5, subst4
                                        if len(subjects26) == 0:
                                            break
                                        tmp75.append(subjects26.popleft())
                                    subjects26.extendleft(reversed(tmp75))
                        subjects26.appendleft(tmp59)
                    subjects.appendleft(tmp25)
            if len(subjects) >= 1:
                tmp78 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp78)
                except ValueError:
                    pass
                else:
                    pass
                    # State 40415
                    if len(subjects) == 0:
                        pass
                        # 6: x**n
                        yield 6, subst2
                subjects.appendleft(tmp78)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.1.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 49474
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.1.1.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 49475
                    if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                        tmp82 = subjects.popleft()
                        subjects83 = deque(tmp82._args)
                        # State 49476
                        if len(subjects83) >= 1:
                            tmp84 = subjects83.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp84)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49477
                                if len(subjects83) >= 1:
                                    tmp86 = subjects83.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.1.2', tmp86)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49478
                                        if len(subjects83) == 0:
                                            pass
                                            # State 49479
                                            if len(subjects) == 0:
                                                pass
                                                # 7: (d + e*x**n)**p
                                                yield 7, subst5
                                    subjects83.appendleft(tmp86)
                            subjects83.appendleft(tmp84)
                        if len(subjects83) >= 1:
                            tmp88 = subjects83.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.1.0', tmp88)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49984
                                if len(subjects83) >= 1:
                                    tmp90 = subjects83.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.1.2', tmp90)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49985
                                        if len(subjects83) == 0:
                                            pass
                                            # State 49986
                                            if len(subjects) == 0:
                                                pass
                                                # 9: (d + e*x**n)**p
                                                yield 9, subst5
                                    subjects83.appendleft(tmp90)
                            subjects83.appendleft(tmp88)
                        if len(subjects83) >= 1:
                            tmp92 = subjects83.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.1', tmp92)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 50310
                                if len(subjects83) >= 1 and subjects83[0] == Integer(2):
                                    tmp94 = subjects83.popleft()
                                    # State 50311
                                    if len(subjects83) == 0:
                                        pass
                                        # State 50312
                                        if len(subjects) == 0:
                                            pass
                                            # 10: (d + e*x**2)**p
                                            yield 10, subst4
                                    subjects83.appendleft(tmp94)
                            subjects83.appendleft(tmp92)
                        subjects.appendleft(tmp82)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp95 = subjects.popleft()
                    associative1 = tmp95
                    associative_type1 = type(tmp95)
                    subjects96 = deque(tmp95._args)
                    matcher = CommutativeMatcher49481.get()
                    tmp97 = subjects96
                    subjects96 = []
                    for s in tmp97:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp97, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 49486
                            if len(subjects) == 0:
                                pass
                                # 7: (d + e*x**n)**p
                                yield 7, subst3
                        if pattern_index == 1:
                            pass
                            # State 49990
                            if len(subjects) == 0:
                                pass
                                # 9: (d + e*x**n)**p
                                yield 9, subst3
                        if pattern_index == 2:
                            pass
                            # State 50316
                            if len(subjects) == 0:
                                pass
                                # 10: (d + e*x**2)**p
                                yield 10, subst3
                    subjects.appendleft(tmp95)
            if len(subjects) >= 1:
                tmp98 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1', tmp98)
                except ValueError:
                    pass
                else:
                    pass
                    # State 49784
                    if len(subjects) == 0:
                        pass
                        # 8: v**p
                        yield 8, subst2
                subjects.appendleft(tmp98)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp100 = subjects.popleft()
                associative1 = tmp100
                associative_type1 = type(tmp100)
                subjects101 = deque(tmp100._args)
                matcher = CommutativeMatcher24626.get()
                tmp102 = subjects101
                subjects101 = []
                for s in tmp102:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp102, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 24663
                        if len(subjects) == 0:
                            pass
                            # 1: (d*(e + f*x)**p)**q
                            yield 1, subst2
                    if pattern_index == 1:
                        pass
                        # State 26825
                        if len(subjects) == 0:
                            pass
                            # 3: (d*(e + f*x)**p)**q
                            yield 3, subst2
                    if pattern_index == 2:
                        pass
                        # State 27327
                        if len(subjects) == 0:
                            pass
                            # 4: (d*(e + f*x)**p)**q
                            yield 4, subst2
                    if pattern_index == 3:
                        pass
                        # State 27892
                        if len(subjects) == 0:
                            pass
                            # 5: (d*(e + f*x)**p)**q
                            yield 5, subst2
                subjects.appendleft(tmp100)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp103 = subjects.popleft()
                associative1 = tmp103
                associative_type1 = type(tmp103)
                subjects104 = deque(tmp103._args)
                matcher = CommutativeMatcher49488.get()
                tmp105 = subjects104
                subjects104 = []
                for s in tmp105:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp105, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 49501
                        if len(subjects) == 0:
                            pass
                            # 7: (d + e*x**n)**p
                            yield 7, subst2
                    if pattern_index == 1:
                        pass
                        # State 49998
                        if len(subjects) == 0:
                            pass
                            # 9: (d + e*x**n)**p
                            yield 9, subst2
                    if pattern_index == 2:
                        pass
                        # State 50324
                        if len(subjects) == 0:
                            pass
                            # 10: (d + e*x**2)**p
                            yield 10, subst2
                subjects.appendleft(tmp103)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp106 = subjects.popleft()
            associative1 = tmp106
            associative_type1 = type(tmp106)
            subjects107 = deque(tmp106._args)
            matcher = CommutativeMatcher23964.get()
            tmp108 = subjects107
            subjects107 = []
            for s in tmp108:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp108, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 23970
                    if len(subjects) == 0:
                        pass
                        # 0: e + f*x
                        yield 0, subst1
            subjects.appendleft(tmp106)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp109 = subjects.popleft()
            subjects110 = deque(tmp109._args)
            # State 24664
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 24665
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 24666
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 24667
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24668
                            if len(subjects110) >= 1:
                                tmp115 = subjects110.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.0', tmp115)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24669
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 24670
                                        if len(subjects110) == 0:
                                            pass
                                            # State 24671
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (d*(e + f*x)**p)**q
                                                yield 1, subst6
                                    if len(subjects110) >= 1:
                                        tmp118 = subjects110.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2', tmp118)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24670
                                            if len(subjects110) == 0:
                                                pass
                                                # State 24671
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*(e + f*x)**p)**q
                                                    yield 1, subst6
                                        subjects110.appendleft(tmp118)
                                subjects110.appendleft(tmp115)
                            if len(subjects110) >= 1:
                                tmp120 = subjects110.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.1', tmp120)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26826
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 26827
                                        if len(subjects110) == 0:
                                            pass
                                            # State 26828
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (d*(e + f*x)**p)**q
                                                yield 3, subst6
                                    if len(subjects110) >= 1:
                                        tmp123 = subjects110.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2', tmp123)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26827
                                            if len(subjects110) == 0:
                                                pass
                                                # State 26828
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x)**p)**q
                                                    yield 3, subst6
                                        subjects110.appendleft(tmp123)
                                subjects110.appendleft(tmp120)
                            if len(subjects110) >= 1:
                                tmp125 = subjects110.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.3.1.0', tmp125)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27893
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27894
                                        if len(subjects110) == 0:
                                            pass
                                            # State 27895
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x)**p)**q
                                                yield 5, subst6
                                    if len(subjects110) >= 1:
                                        tmp128 = subjects110.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2', tmp128)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27894
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27895
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x)**p)**q
                                                    yield 5, subst6
                                        subjects110.appendleft(tmp128)
                                subjects110.appendleft(tmp125)
                        if len(subjects110) >= 1 and isinstance(subjects110[0], Mul):
                            tmp130 = subjects110.popleft()
                            associative1 = tmp130
                            associative_type1 = type(tmp130)
                            subjects131 = deque(tmp130._args)
                            matcher = CommutativeMatcher24673.get()
                            tmp132 = subjects131
                            subjects131 = []
                            for s in tmp132:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp132, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 24674
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 24675
                                        if len(subjects110) == 0:
                                            pass
                                            # State 24676
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (d*(e + f*x)**p)**q
                                                yield 1, subst5
                                    if len(subjects110) >= 1:
                                        tmp134 = []
                                        tmp134.append(subjects110.popleft())
                                        while True:
                                            if len(tmp134) > 1:
                                                tmp135 = create_operation_expression(associative1, tmp134)
                                            elif len(tmp134) == 1:
                                                tmp135 = tmp134[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', tmp135)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24675
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 24676
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*(e + f*x)**p)**q
                                                        yield 1, subst5
                                            if len(subjects110) == 0:
                                                break
                                            tmp134.append(subjects110.popleft())
                                        subjects110.extendleft(reversed(tmp134))
                                if pattern_index == 1:
                                    pass
                                    # State 26829
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 26830
                                        if len(subjects110) == 0:
                                            pass
                                            # State 26831
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (d*(e + f*x)**p)**q
                                                yield 3, subst5
                                    if len(subjects110) >= 1:
                                        tmp138 = []
                                        tmp138.append(subjects110.popleft())
                                        while True:
                                            if len(tmp138) > 1:
                                                tmp139 = create_operation_expression(associative1, tmp138)
                                            elif len(tmp138) == 1:
                                                tmp139 = tmp138[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', tmp139)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26830
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 26831
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x)**p)**q
                                                        yield 3, subst5
                                            if len(subjects110) == 0:
                                                break
                                            tmp138.append(subjects110.popleft())
                                        subjects110.extendleft(reversed(tmp138))
                                if pattern_index == 2:
                                    pass
                                    # State 27896
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27897
                                        if len(subjects110) == 0:
                                            pass
                                            # State 27898
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x)**p)**q
                                                yield 5, subst5
                                    if len(subjects110) >= 1:
                                        tmp142 = []
                                        tmp142.append(subjects110.popleft())
                                        while True:
                                            if len(tmp142) > 1:
                                                tmp143 = create_operation_expression(associative1, tmp142)
                                            elif len(tmp142) == 1:
                                                tmp143 = tmp142[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', tmp143)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27897
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27898
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x)**p)**q
                                                        yield 5, subst5
                                            if len(subjects110) == 0:
                                                break
                                            tmp142.append(subjects110.popleft())
                                        subjects110.extendleft(reversed(tmp142))
                            subjects110.appendleft(tmp130)
                    if len(subjects110) >= 1 and isinstance(subjects110[0], Add):
                        tmp145 = subjects110.popleft()
                        associative1 = tmp145
                        associative_type1 = type(tmp145)
                        subjects146 = deque(tmp145._args)
                        matcher = CommutativeMatcher24678.get()
                        tmp147 = subjects146
                        subjects146 = []
                        for s in tmp147:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp147, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 24684
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24685
                                    if len(subjects110) == 0:
                                        pass
                                        # State 24686
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*(e + f*x)**p)**q
                                            yield 1, subst4
                                if len(subjects110) >= 1:
                                    tmp149 = []
                                    tmp149.append(subjects110.popleft())
                                    while True:
                                        if len(tmp149) > 1:
                                            tmp150 = create_operation_expression(associative1, tmp149)
                                        elif len(tmp149) == 1:
                                            tmp150 = tmp149[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', tmp150)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24685
                                            if len(subjects110) == 0:
                                                pass
                                                # State 24686
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*(e + f*x)**p)**q
                                                    yield 1, subst4
                                        if len(subjects110) == 0:
                                            break
                                        tmp149.append(subjects110.popleft())
                                    subjects110.extendleft(reversed(tmp149))
                            if pattern_index == 1:
                                pass
                                # State 26834
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26835
                                    if len(subjects110) == 0:
                                        pass
                                        # State 26836
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x)**p)**q
                                            yield 3, subst4
                                if len(subjects110) >= 1:
                                    tmp153 = []
                                    tmp153.append(subjects110.popleft())
                                    while True:
                                        if len(tmp153) > 1:
                                            tmp154 = create_operation_expression(associative1, tmp153)
                                        elif len(tmp153) == 1:
                                            tmp154 = tmp153[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', tmp154)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26835
                                            if len(subjects110) == 0:
                                                pass
                                                # State 26836
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x)**p)**q
                                                    yield 3, subst4
                                        if len(subjects110) == 0:
                                            break
                                        tmp153.append(subjects110.popleft())
                                    subjects110.extendleft(reversed(tmp153))
                            if pattern_index == 2:
                                pass
                                # State 27328
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27329
                                    if len(subjects110) == 0:
                                        pass
                                        # State 27330
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(e + f*x)**p)**q
                                            yield 4, subst4
                                if len(subjects110) >= 1:
                                    tmp157 = []
                                    tmp157.append(subjects110.popleft())
                                    while True:
                                        if len(tmp157) > 1:
                                            tmp158 = create_operation_expression(associative1, tmp157)
                                        elif len(tmp157) == 1:
                                            tmp158 = tmp157[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', tmp158)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27329
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27330
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(e + f*x)**p)**q
                                                    yield 4, subst4
                                        if len(subjects110) == 0:
                                            break
                                        tmp157.append(subjects110.popleft())
                                    subjects110.extendleft(reversed(tmp157))
                            if pattern_index == 3:
                                pass
                                # State 27901
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27902
                                    if len(subjects110) == 0:
                                        pass
                                        # State 27903
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x)**p)**q
                                            yield 5, subst4
                                if len(subjects110) >= 1:
                                    tmp161 = []
                                    tmp161.append(subjects110.popleft())
                                    while True:
                                        if len(tmp161) > 1:
                                            tmp162 = create_operation_expression(associative1, tmp161)
                                        elif len(tmp161) == 1:
                                            tmp162 = tmp161[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', tmp162)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27902
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27903
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x)**p)**q
                                                    yield 5, subst4
                                        if len(subjects110) == 0:
                                            break
                                        tmp161.append(subjects110.popleft())
                                    subjects110.extendleft(reversed(tmp161))
                        subjects110.appendleft(tmp145)
                if len(subjects110) >= 1 and isinstance(subjects110[0], Pow):
                    tmp164 = subjects110.popleft()
                    subjects165 = deque(tmp164._args)
                    # State 24687
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 24688
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24689
                            if len(subjects165) >= 1:
                                tmp168 = subjects165.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.0', tmp168)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24690
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 24691
                                        if len(subjects165) == 0:
                                            pass
                                            # State 24692
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24693
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 24694
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*(e + f*x)**p)**q
                                                        yield 1, subst6
                                            if len(subjects110) >= 1:
                                                tmp172 = subjects110.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', tmp172)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24693
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 24694
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: (d*(e + f*x)**p)**q
                                                            yield 1, subst6
                                                subjects110.appendleft(tmp172)
                                    if len(subjects165) >= 1:
                                        tmp174 = subjects165.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', tmp174)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24691
                                            if len(subjects165) == 0:
                                                pass
                                                # State 24692
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24693
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 24694
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: (d*(e + f*x)**p)**q
                                                            yield 1, subst6
                                                if len(subjects110) >= 1:
                                                    tmp177 = subjects110.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp177)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 24693
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 24694
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (d*(e + f*x)**p)**q
                                                                yield 1, subst6
                                                    subjects110.appendleft(tmp177)
                                        subjects165.appendleft(tmp174)
                                subjects165.appendleft(tmp168)
                            if len(subjects165) >= 1:
                                tmp179 = subjects165.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.1', tmp179)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26837
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 26838
                                        if len(subjects165) == 0:
                                            pass
                                            # State 26839
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26840
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 26841
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x)**p)**q
                                                        yield 3, subst6
                                            if len(subjects110) >= 1:
                                                tmp183 = subjects110.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', tmp183)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26840
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 26841
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: (d*(e + f*x)**p)**q
                                                            yield 3, subst6
                                                subjects110.appendleft(tmp183)
                                    if len(subjects165) >= 1:
                                        tmp185 = subjects165.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', tmp185)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26838
                                            if len(subjects165) == 0:
                                                pass
                                                # State 26839
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26840
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 26841
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: (d*(e + f*x)**p)**q
                                                            yield 3, subst6
                                                if len(subjects110) >= 1:
                                                    tmp188 = subjects110.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp188)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 26840
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 26841
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: (d*(e + f*x)**p)**q
                                                                yield 3, subst6
                                                    subjects110.appendleft(tmp188)
                                        subjects165.appendleft(tmp185)
                                subjects165.appendleft(tmp179)
                            if len(subjects165) >= 1:
                                tmp190 = subjects165.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.0', tmp190)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27904
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27905
                                        if len(subjects165) == 0:
                                            pass
                                            # State 27906
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27907
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27908
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x)**p)**q
                                                        yield 5, subst6
                                            if len(subjects110) >= 1:
                                                tmp194 = subjects110.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', tmp194)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27907
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27908
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x)**p)**q
                                                            yield 5, subst6
                                                subjects110.appendleft(tmp194)
                                    if len(subjects165) >= 1:
                                        tmp196 = subjects165.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', tmp196)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27905
                                            if len(subjects165) == 0:
                                                pass
                                                # State 27906
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27907
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27908
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x)**p)**q
                                                            yield 5, subst6
                                                if len(subjects110) >= 1:
                                                    tmp199 = subjects110.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp199)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27907
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 27908
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x)**p)**q
                                                                yield 5, subst6
                                                    subjects110.appendleft(tmp199)
                                        subjects165.appendleft(tmp196)
                                subjects165.appendleft(tmp190)
                        if len(subjects165) >= 1 and isinstance(subjects165[0], Mul):
                            tmp201 = subjects165.popleft()
                            associative1 = tmp201
                            associative_type1 = type(tmp201)
                            subjects202 = deque(tmp201._args)
                            matcher = CommutativeMatcher24696.get()
                            tmp203 = subjects202
                            subjects202 = []
                            for s in tmp203:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp203, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 24697
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 24698
                                        if len(subjects165) == 0:
                                            pass
                                            # State 24699
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24700
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 24701
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*(e + f*x)**p)**q
                                                        yield 1, subst5
                                            if len(subjects110) >= 1:
                                                tmp206 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp206)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24700
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 24701
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: (d*(e + f*x)**p)**q
                                                            yield 1, subst5
                                                subjects110.appendleft(tmp206)
                                    if len(subjects165) >= 1:
                                        tmp208 = []
                                        tmp208.append(subjects165.popleft())
                                        while True:
                                            if len(tmp208) > 1:
                                                tmp209 = create_operation_expression(associative1, tmp208)
                                            elif len(tmp208) == 1:
                                                tmp209 = tmp208[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2.2', tmp209)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24698
                                                if len(subjects165) == 0:
                                                    pass
                                                    # State 24699
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 24700
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 24701
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (d*(e + f*x)**p)**q
                                                                yield 1, subst5
                                                    if len(subjects110) >= 1:
                                                        tmp212 = subjects110.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', tmp212)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 24700
                                                            if len(subjects110) == 0:
                                                                pass
                                                                # State 24701
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 1: (d*(e + f*x)**p)**q
                                                                    yield 1, subst5
                                                        subjects110.appendleft(tmp212)
                                            if len(subjects165) == 0:
                                                break
                                            tmp208.append(subjects165.popleft())
                                        subjects165.extendleft(reversed(tmp208))
                                if pattern_index == 1:
                                    pass
                                    # State 26842
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 26843
                                        if len(subjects165) == 0:
                                            pass
                                            # State 26844
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26845
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 26846
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x)**p)**q
                                                        yield 3, subst5
                                            if len(subjects110) >= 1:
                                                tmp216 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp216)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26845
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 26846
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: (d*(e + f*x)**p)**q
                                                            yield 3, subst5
                                                subjects110.appendleft(tmp216)
                                    if len(subjects165) >= 1:
                                        tmp218 = []
                                        tmp218.append(subjects165.popleft())
                                        while True:
                                            if len(tmp218) > 1:
                                                tmp219 = create_operation_expression(associative1, tmp218)
                                            elif len(tmp218) == 1:
                                                tmp219 = tmp218[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2.2', tmp219)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26843
                                                if len(subjects165) == 0:
                                                    pass
                                                    # State 26844
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 26845
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 26846
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: (d*(e + f*x)**p)**q
                                                                yield 3, subst5
                                                    if len(subjects110) >= 1:
                                                        tmp222 = subjects110.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', tmp222)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 26845
                                                            if len(subjects110) == 0:
                                                                pass
                                                                # State 26846
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 3: (d*(e + f*x)**p)**q
                                                                    yield 3, subst5
                                                        subjects110.appendleft(tmp222)
                                            if len(subjects165) == 0:
                                                break
                                            tmp218.append(subjects165.popleft())
                                        subjects165.extendleft(reversed(tmp218))
                                if pattern_index == 2:
                                    pass
                                    # State 27909
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27910
                                        if len(subjects165) == 0:
                                            pass
                                            # State 27911
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27912
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27913
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x)**p)**q
                                                        yield 5, subst5
                                            if len(subjects110) >= 1:
                                                tmp226 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp226)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27912
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27913
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x)**p)**q
                                                            yield 5, subst5
                                                subjects110.appendleft(tmp226)
                                    if len(subjects165) >= 1:
                                        tmp228 = []
                                        tmp228.append(subjects165.popleft())
                                        while True:
                                            if len(tmp228) > 1:
                                                tmp229 = create_operation_expression(associative1, tmp228)
                                            elif len(tmp228) == 1:
                                                tmp229 = tmp228[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2.2', tmp229)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27910
                                                if len(subjects165) == 0:
                                                    pass
                                                    # State 27911
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27912
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 27913
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x)**p)**q
                                                                yield 5, subst5
                                                    if len(subjects110) >= 1:
                                                        tmp232 = subjects110.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', tmp232)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 27912
                                                            if len(subjects110) == 0:
                                                                pass
                                                                # State 27913
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x)**p)**q
                                                                    yield 5, subst5
                                                        subjects110.appendleft(tmp232)
                                            if len(subjects165) == 0:
                                                break
                                            tmp228.append(subjects165.popleft())
                                        subjects165.extendleft(reversed(tmp228))
                            subjects165.appendleft(tmp201)
                    if len(subjects165) >= 1 and isinstance(subjects165[0], Add):
                        tmp234 = subjects165.popleft()
                        associative1 = tmp234
                        associative_type1 = type(tmp234)
                        subjects235 = deque(tmp234._args)
                        matcher = CommutativeMatcher24703.get()
                        tmp236 = subjects235
                        subjects235 = []
                        for s in tmp236:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp236, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 24709
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24710
                                    if len(subjects165) == 0:
                                        pass
                                        # State 24711
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24712
                                            if len(subjects110) == 0:
                                                pass
                                                # State 24713
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*(e + f*x)**p)**q
                                                    yield 1, subst4
                                        if len(subjects110) >= 1:
                                            tmp239 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp239)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24712
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 24713
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*(e + f*x)**p)**q
                                                        yield 1, subst4
                                            subjects110.appendleft(tmp239)
                                if len(subjects165) >= 1:
                                    tmp241 = []
                                    tmp241.append(subjects165.popleft())
                                    while True:
                                        if len(tmp241) > 1:
                                            tmp242 = create_operation_expression(associative1, tmp241)
                                        elif len(tmp241) == 1:
                                            tmp242 = tmp241[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2.2', tmp242)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24710
                                            if len(subjects165) == 0:
                                                pass
                                                # State 24711
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24712
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 24713
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: (d*(e + f*x)**p)**q
                                                            yield 1, subst4
                                                if len(subjects110) >= 1:
                                                    tmp245 = subjects110.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.2.2', tmp245)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 24712
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 24713
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (d*(e + f*x)**p)**q
                                                                yield 1, subst4
                                                    subjects110.appendleft(tmp245)
                                        if len(subjects165) == 0:
                                            break
                                        tmp241.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp241))
                            if pattern_index == 1:
                                pass
                                # State 26849
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26850
                                    if len(subjects165) == 0:
                                        pass
                                        # State 26851
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26852
                                            if len(subjects110) == 0:
                                                pass
                                                # State 26853
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x)**p)**q
                                                    yield 3, subst4
                                        if len(subjects110) >= 1:
                                            tmp249 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp249)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26852
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 26853
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x)**p)**q
                                                        yield 3, subst4
                                            subjects110.appendleft(tmp249)
                                if len(subjects165) >= 1:
                                    tmp251 = []
                                    tmp251.append(subjects165.popleft())
                                    while True:
                                        if len(tmp251) > 1:
                                            tmp252 = create_operation_expression(associative1, tmp251)
                                        elif len(tmp251) == 1:
                                            tmp252 = tmp251[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2.2', tmp252)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26850
                                            if len(subjects165) == 0:
                                                pass
                                                # State 26851
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26852
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 26853
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: (d*(e + f*x)**p)**q
                                                            yield 3, subst4
                                                if len(subjects110) >= 1:
                                                    tmp255 = subjects110.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.2.2', tmp255)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 26852
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 26853
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: (d*(e + f*x)**p)**q
                                                                yield 3, subst4
                                                    subjects110.appendleft(tmp255)
                                        if len(subjects165) == 0:
                                            break
                                        tmp251.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp251))
                            if pattern_index == 2:
                                pass
                                # State 27331
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27332
                                    if len(subjects165) == 0:
                                        pass
                                        # State 27333
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27334
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27335
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(e + f*x)**p)**q
                                                    yield 4, subst4
                                        if len(subjects110) >= 1:
                                            tmp259 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp259)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27334
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27335
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (d*(e + f*x)**p)**q
                                                        yield 4, subst4
                                            subjects110.appendleft(tmp259)
                                if len(subjects165) >= 1:
                                    tmp261 = []
                                    tmp261.append(subjects165.popleft())
                                    while True:
                                        if len(tmp261) > 1:
                                            tmp262 = create_operation_expression(associative1, tmp261)
                                        elif len(tmp261) == 1:
                                            tmp262 = tmp261[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2.2', tmp262)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27332
                                            if len(subjects165) == 0:
                                                pass
                                                # State 27333
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27334
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27335
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (d*(e + f*x)**p)**q
                                                            yield 4, subst4
                                                if len(subjects110) >= 1:
                                                    tmp265 = subjects110.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.2.2', tmp265)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27334
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 27335
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (d*(e + f*x)**p)**q
                                                                yield 4, subst4
                                                    subjects110.appendleft(tmp265)
                                        if len(subjects165) == 0:
                                            break
                                        tmp261.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp261))
                            if pattern_index == 3:
                                pass
                                # State 27916
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27917
                                    if len(subjects165) == 0:
                                        pass
                                        # State 27918
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27919
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27920
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x)**p)**q
                                                    yield 5, subst4
                                        if len(subjects110) >= 1:
                                            tmp269 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp269)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27919
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27920
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x)**p)**q
                                                        yield 5, subst4
                                            subjects110.appendleft(tmp269)
                                if len(subjects165) >= 1:
                                    tmp271 = []
                                    tmp271.append(subjects165.popleft())
                                    while True:
                                        if len(tmp271) > 1:
                                            tmp272 = create_operation_expression(associative1, tmp271)
                                        elif len(tmp271) == 1:
                                            tmp272 = tmp271[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2.2', tmp272)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27917
                                            if len(subjects165) == 0:
                                                pass
                                                # State 27918
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27919
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27920
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x)**p)**q
                                                            yield 5, subst4
                                                if len(subjects110) >= 1:
                                                    tmp275 = subjects110.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.2.2', tmp275)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27919
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 27920
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x)**p)**q
                                                                yield 5, subst4
                                                    subjects110.appendleft(tmp275)
                                        if len(subjects165) == 0:
                                            break
                                        tmp271.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp271))
                        subjects165.appendleft(tmp234)
                    subjects110.appendleft(tmp164)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 26441
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 26442
                    if len(subjects110) >= 1:
                        tmp279 = subjects110.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp279)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 26443
                            if len(subjects110) >= 1 and subjects110[0] == Integer(-1):
                                tmp281 = subjects110.popleft()
                                # State 26444
                                if len(subjects110) == 0:
                                    pass
                                    # State 26445
                                    if len(subjects) == 0:
                                        pass
                                        # 2: 1/(e + f*x)
                                        yield 2, subst3
                                subjects110.appendleft(tmp281)
                        subjects110.appendleft(tmp279)
                    if len(subjects110) >= 1 and isinstance(subjects110[0], Pow):
                        tmp282 = subjects110.popleft()
                        subjects283 = deque(tmp282._args)
                        # State 49502
                        if len(subjects283) >= 1:
                            tmp284 = subjects283.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.0', tmp284)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49503
                                if len(subjects283) >= 1:
                                    tmp286 = subjects283.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.1.2', tmp286)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49504
                                        if len(subjects283) == 0:
                                            pass
                                            # State 49505
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49506
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 49507
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: (d + e*x**n)**p
                                                        yield 7, subst5
                                            if len(subjects110) >= 1:
                                                tmp289 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp289)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 49506
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 49507
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 7: (d + e*x**n)**p
                                                            yield 7, subst5
                                                subjects110.appendleft(tmp289)
                                    subjects283.appendleft(tmp286)
                            subjects283.appendleft(tmp284)
                        if len(subjects283) >= 1:
                            tmp291 = subjects283.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.0', tmp291)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49999
                                if len(subjects283) >= 1:
                                    tmp293 = subjects283.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.1.2', tmp293)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50000
                                        if len(subjects283) == 0:
                                            pass
                                            # State 50001
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 50002
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 50003
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 9: (d + e*x**n)**p
                                                        yield 9, subst5
                                            if len(subjects110) >= 1:
                                                tmp296 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp296)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 50002
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 50003
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 9: (d + e*x**n)**p
                                                            yield 9, subst5
                                                subjects110.appendleft(tmp296)
                                    subjects283.appendleft(tmp293)
                            subjects283.appendleft(tmp291)
                        if len(subjects283) >= 1:
                            tmp298 = subjects283.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.1', tmp298)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 50325
                                if len(subjects283) >= 1 and subjects283[0] == Integer(2):
                                    tmp300 = subjects283.popleft()
                                    # State 50326
                                    if len(subjects283) == 0:
                                        pass
                                        # State 50327
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 50328
                                            if len(subjects110) == 0:
                                                pass
                                                # State 50329
                                                if len(subjects) == 0:
                                                    pass
                                                    # 10: (d + e*x**2)**p
                                                    yield 10, subst4
                                        if len(subjects110) >= 1:
                                            tmp302 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp302)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 50328
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 50329
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 10: (d + e*x**2)**p
                                                        yield 10, subst4
                                            subjects110.appendleft(tmp302)
                                    subjects283.appendleft(tmp300)
                            subjects283.appendleft(tmp298)
                        subjects110.appendleft(tmp282)
                if len(subjects110) >= 1 and isinstance(subjects110[0], Mul):
                    tmp304 = subjects110.popleft()
                    associative1 = tmp304
                    associative_type1 = type(tmp304)
                    subjects305 = deque(tmp304._args)
                    matcher = CommutativeMatcher26447.get()
                    tmp306 = subjects305
                    subjects305 = []
                    for s in tmp306:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp306, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 26448
                            if len(subjects110) >= 1 and subjects110[0] == Integer(-1):
                                tmp307 = subjects110.popleft()
                                # State 26449
                                if len(subjects110) == 0:
                                    pass
                                    # State 26450
                                    if len(subjects) == 0:
                                        pass
                                        # 2: 1/(e + f*x)
                                        yield 2, subst2
                                subjects110.appendleft(tmp307)
                        if pattern_index == 1:
                            pass
                            # State 49512
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49513
                                if len(subjects110) == 0:
                                    pass
                                    # State 49514
                                    if len(subjects) == 0:
                                        pass
                                        # 7: (d + e*x**n)**p
                                        yield 7, subst3
                            if len(subjects110) >= 1:
                                tmp309 = []
                                tmp309.append(subjects110.popleft())
                                while True:
                                    if len(tmp309) > 1:
                                        tmp310 = create_operation_expression(associative1, tmp309)
                                    elif len(tmp309) == 1:
                                        tmp310 = tmp309[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.1.1.2.2', tmp310)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49513
                                        if len(subjects110) == 0:
                                            pass
                                            # State 49514
                                            if len(subjects) == 0:
                                                pass
                                                # 7: (d + e*x**n)**p
                                                yield 7, subst3
                                    if len(subjects110) == 0:
                                        break
                                    tmp309.append(subjects110.popleft())
                                subjects110.extendleft(reversed(tmp309))
                        if pattern_index == 2:
                            pass
                            # State 50007
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 50008
                                if len(subjects110) == 0:
                                    pass
                                    # State 50009
                                    if len(subjects) == 0:
                                        pass
                                        # 9: (d + e*x**n)**p
                                        yield 9, subst3
                            if len(subjects110) >= 1:
                                tmp313 = []
                                tmp313.append(subjects110.popleft())
                                while True:
                                    if len(tmp313) > 1:
                                        tmp314 = create_operation_expression(associative1, tmp313)
                                    elif len(tmp313) == 1:
                                        tmp314 = tmp313[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.1.1.2.2', tmp314)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50008
                                        if len(subjects110) == 0:
                                            pass
                                            # State 50009
                                            if len(subjects) == 0:
                                                pass
                                                # 9: (d + e*x**n)**p
                                                yield 9, subst3
                                    if len(subjects110) == 0:
                                        break
                                    tmp313.append(subjects110.popleft())
                                subjects110.extendleft(reversed(tmp313))
                        if pattern_index == 3:
                            pass
                            # State 50333
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 50334
                                if len(subjects110) == 0:
                                    pass
                                    # State 50335
                                    if len(subjects) == 0:
                                        pass
                                        # 10: (d + e*x**2)**p
                                        yield 10, subst3
                            if len(subjects110) >= 1:
                                tmp317 = []
                                tmp317.append(subjects110.popleft())
                                while True:
                                    if len(tmp317) > 1:
                                        tmp318 = create_operation_expression(associative1, tmp317)
                                    elif len(tmp317) == 1:
                                        tmp318 = tmp317[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.1.1.2.2', tmp318)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50334
                                        if len(subjects110) == 0:
                                            pass
                                            # State 50335
                                            if len(subjects) == 0:
                                                pass
                                                # 10: (d + e*x**2)**p
                                                yield 10, subst3
                                    if len(subjects110) == 0:
                                        break
                                    tmp317.append(subjects110.popleft())
                                subjects110.extendleft(reversed(tmp317))
                    subjects110.appendleft(tmp304)
            if len(subjects110) >= 1:
                tmp320 = subjects110.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp320)
                except ValueError:
                    pass
                else:
                    pass
                    # State 40416
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 40417
                        if len(subjects110) == 0:
                            pass
                            # State 40418
                            if len(subjects) == 0:
                                pass
                                # 6: x**n
                                yield 6, subst2
                    if len(subjects110) >= 1:
                        tmp323 = subjects110.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', tmp323)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40417
                            if len(subjects110) == 0:
                                pass
                                # State 40418
                                if len(subjects) == 0:
                                    pass
                                    # 6: x**n
                                    yield 6, subst2
                        subjects110.appendleft(tmp323)
                subjects110.appendleft(tmp320)
            if len(subjects110) >= 1:
                tmp325 = subjects110.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.2.1', tmp325)
                except ValueError:
                    pass
                else:
                    pass
                    # State 49785
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 49786
                        if len(subjects110) == 0:
                            pass
                            # State 49787
                            if len(subjects) == 0:
                                pass
                                # 8: v**p
                                yield 8, subst2
                    if len(subjects110) >= 1:
                        tmp328 = subjects110.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', tmp328)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49786
                            if len(subjects110) == 0:
                                pass
                                # State 49787
                                if len(subjects) == 0:
                                    pass
                                    # 8: v**p
                                    yield 8, subst2
                        subjects110.appendleft(tmp328)
                subjects110.appendleft(tmp325)
            if len(subjects110) >= 1 and isinstance(subjects110[0], Mul):
                tmp330 = subjects110.popleft()
                associative1 = tmp330
                associative_type1 = type(tmp330)
                subjects331 = deque(tmp330._args)
                matcher = CommutativeMatcher24715.get()
                tmp332 = subjects331
                subjects331 = []
                for s in tmp332:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp332, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 24752
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24753
                            if len(subjects110) == 0:
                                pass
                                # State 24754
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d*(e + f*x)**p)**q
                                    yield 1, subst2
                        if len(subjects110) >= 1:
                            tmp334 = []
                            tmp334.append(subjects110.popleft())
                            while True:
                                if len(tmp334) > 1:
                                    tmp335 = create_operation_expression(associative1, tmp334)
                                elif len(tmp334) == 1:
                                    tmp335 = tmp334[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp335)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24753
                                    if len(subjects110) == 0:
                                        pass
                                        # State 24754
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*(e + f*x)**p)**q
                                            yield 1, subst2
                                if len(subjects110) == 0:
                                    break
                                tmp334.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp334))
                    if pattern_index == 1:
                        pass
                        # State 26870
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 26871
                            if len(subjects110) == 0:
                                pass
                                # State 26872
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x)**p)**q
                                    yield 3, subst2
                        if len(subjects110) >= 1:
                            tmp338 = []
                            tmp338.append(subjects110.popleft())
                            while True:
                                if len(tmp338) > 1:
                                    tmp339 = create_operation_expression(associative1, tmp338)
                                elif len(tmp338) == 1:
                                    tmp339 = tmp338[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp339)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26871
                                    if len(subjects110) == 0:
                                        pass
                                        # State 26872
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x)**p)**q
                                            yield 3, subst2
                                if len(subjects110) == 0:
                                    break
                                tmp338.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp338))
                    if pattern_index == 2:
                        pass
                        # State 27340
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 27341
                            if len(subjects110) == 0:
                                pass
                                # State 27342
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(e + f*x)**p)**q
                                    yield 4, subst2
                        if len(subjects110) >= 1:
                            tmp342 = []
                            tmp342.append(subjects110.popleft())
                            while True:
                                if len(tmp342) > 1:
                                    tmp343 = create_operation_expression(associative1, tmp342)
                                elif len(tmp342) == 1:
                                    tmp343 = tmp342[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp343)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27341
                                    if len(subjects110) == 0:
                                        pass
                                        # State 27342
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(e + f*x)**p)**q
                                            yield 4, subst2
                                if len(subjects110) == 0:
                                    break
                                tmp342.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp342))
                    if pattern_index == 3:
                        pass
                        # State 27937
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 27938
                            if len(subjects110) == 0:
                                pass
                                # State 27939
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x)**p)**q
                                    yield 5, subst2
                        if len(subjects110) >= 1:
                            tmp346 = []
                            tmp346.append(subjects110.popleft())
                            while True:
                                if len(tmp346) > 1:
                                    tmp347 = create_operation_expression(associative1, tmp346)
                                elif len(tmp346) == 1:
                                    tmp347 = tmp346[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp347)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27938
                                    if len(subjects110) == 0:
                                        pass
                                        # State 27939
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x)**p)**q
                                            yield 5, subst2
                                if len(subjects110) == 0:
                                    break
                                tmp346.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp346))
                subjects110.appendleft(tmp330)
            if len(subjects110) >= 1 and isinstance(subjects110[0], Add):
                tmp349 = subjects110.popleft()
                associative1 = tmp349
                associative_type1 = type(tmp349)
                subjects350 = deque(tmp349._args)
                matcher = CommutativeMatcher26452.get()
                tmp351 = subjects350
                subjects350 = []
                for s in tmp351:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp351, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 26458
                        if len(subjects110) >= 1 and subjects110[0] == Integer(-1):
                            tmp352 = subjects110.popleft()
                            # State 26459
                            if len(subjects110) == 0:
                                pass
                                # State 26460
                                if len(subjects) == 0:
                                    pass
                                    # 2: 1/(e + f*x)
                                    yield 2, subst1
                            subjects110.appendleft(tmp352)
                    if pattern_index == 1:
                        pass
                        # State 49524
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49525
                            if len(subjects110) == 0:
                                pass
                                # State 49526
                                if len(subjects) == 0:
                                    pass
                                    # 7: (d + e*x**n)**p
                                    yield 7, subst2
                        if len(subjects110) >= 1:
                            tmp354 = []
                            tmp354.append(subjects110.popleft())
                            while True:
                                if len(tmp354) > 1:
                                    tmp355 = create_operation_expression(associative1, tmp354)
                                elif len(tmp354) == 1:
                                    tmp355 = tmp354[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp355)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49525
                                    if len(subjects110) == 0:
                                        pass
                                        # State 49526
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d + e*x**n)**p
                                            yield 7, subst2
                                if len(subjects110) == 0:
                                    break
                                tmp354.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp354))
                    if pattern_index == 2:
                        pass
                        # State 50017
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 50018
                            if len(subjects110) == 0:
                                pass
                                # State 50019
                                if len(subjects) == 0:
                                    pass
                                    # 9: (d + e*x**n)**p
                                    yield 9, subst2
                        if len(subjects110) >= 1:
                            tmp358 = []
                            tmp358.append(subjects110.popleft())
                            while True:
                                if len(tmp358) > 1:
                                    tmp359 = create_operation_expression(associative1, tmp358)
                                elif len(tmp358) == 1:
                                    tmp359 = tmp358[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp359)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 50018
                                    if len(subjects110) == 0:
                                        pass
                                        # State 50019
                                        if len(subjects) == 0:
                                            pass
                                            # 9: (d + e*x**n)**p
                                            yield 9, subst2
                                if len(subjects110) == 0:
                                    break
                                tmp358.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp358))
                    if pattern_index == 3:
                        pass
                        # State 50343
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 50344
                            if len(subjects110) == 0:
                                pass
                                # State 50345
                                if len(subjects) == 0:
                                    pass
                                    # 10: (d + e*x**2)**p
                                    yield 10, subst2
                        if len(subjects110) >= 1:
                            tmp362 = []
                            tmp362.append(subjects110.popleft())
                            while True:
                                if len(tmp362) > 1:
                                    tmp363 = create_operation_expression(associative1, tmp362)
                                elif len(tmp362) == 1:
                                    tmp363 = tmp362[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp363)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 50344
                                    if len(subjects110) == 0:
                                        pass
                                        # State 50345
                                        if len(subjects) == 0:
                                            pass
                                            # 10: (d + e*x**2)**p
                                            yield 10, subst2
                                if len(subjects110) == 0:
                                    break
                                tmp362.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp362))
                subjects110.appendleft(tmp349)
            subjects.appendleft(tmp109)
        return
        yield


from .generated_part004006 import *
from .generated_part003991 import *
from .generated_part003989 import *
from .generated_part003984 import *
from .generated_part003988 import *
from .generated_part004003 import *
from collections import deque
from .generated_part003992 import *
from .generated_part004001 import *
from .generated_part003986 import *
from matchpy.utils import VariableWithCount
from .generated_part004009 import *
from .generated_part003999 import *
from multiset import Multiset
from .generated_part004007 import *
from .generated_part004017 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part003985 import *
from .generated_part004004 import *
from .generated_part004010 import *