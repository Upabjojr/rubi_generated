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


class CommutativeMatcher21997(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher21997._instance is None:
            CommutativeMatcher21997._instance = CommutativeMatcher21997()
        return CommutativeMatcher21997._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 21996
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 21998
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 21999
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 22000
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 22001
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 22002
                            if len(subjects) >= 1:
                                tmp6 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp6)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22003
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(e + x*f)**p)**q
                                        yield 0, subst6
                                subjects.appendleft(tmp6)
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35818
                            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                                tmp9 = subjects.popleft()
                                subjects10 = deque(tmp9._args)
                                # State 35819
                                if len(subjects10) >= 1:
                                    tmp11 = subjects10.popleft()
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2.1.1', tmp11)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35820
                                        if len(subjects10) >= 1:
                                            tmp13 = subjects10.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2.2.1.2', tmp13)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35821
                                                if len(subjects10) == 0:
                                                    pass
                                                    # State 35822
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst7
                                            subjects10.appendleft(tmp13)
                                    subjects10.appendleft(tmp11)
                                if len(subjects10) >= 1:
                                    tmp15 = subjects10.popleft()
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.1', tmp15)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 40228
                                        if len(subjects10) >= 1:
                                            tmp17 = subjects10.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2', tmp17)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 40229
                                                if len(subjects10) == 0:
                                                    pass
                                                    # State 40230
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(x**j*f + e)**p)**q
                                                        yield 6, subst7
                                            subjects10.appendleft(tmp17)
                                    subjects10.appendleft(tmp15)
                                subjects.appendleft(tmp9)
                        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                            tmp19 = subjects.popleft()
                            associative1 = tmp19
                            associative_type1 = type(tmp19)
                            subjects20 = deque(tmp19._args)
                            matcher = CommutativeMatcher22005.get()
                            tmp21 = subjects20
                            subjects20 = []
                            for s in tmp21:
                                matcher.add_subject(s)
                            for pattern_index, subst5 in matcher.match(tmp21, subst4):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 22006
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(e + x*f)**p)**q
                                        yield 0, subst5
                                if pattern_index == 1:
                                    pass
                                    # State 35827
                                    if len(subjects) == 0:
                                        pass
                                        # 5: (d*(e + f*x**m)**p)**q
                                        yield 5, subst5
                                if pattern_index == 2:
                                    pass
                                    # State 40234
                                    if len(subjects) == 0:
                                        pass
                                        # 6: (d*(x**j*f + e)**p)**q
                                        yield 6, subst5
                            subjects.appendleft(tmp19)
                    if len(subjects) >= 1:
                        tmp22 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.1', tmp22)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45776
                            if len(subjects) == 0:
                                pass
                                # 8: (d*v**p)**q
                                yield 8, subst4
                        subjects.appendleft(tmp22)
                    if len(subjects) >= 1 and isinstance(subjects[0], Add):
                        tmp24 = subjects.popleft()
                        associative1 = tmp24
                        associative_type1 = type(tmp24)
                        subjects25 = deque(tmp24._args)
                        matcher = CommutativeMatcher22008.get()
                        tmp26 = subjects25
                        subjects25 = []
                        for s in tmp26:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp26, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 22014
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q
                                    yield 0, subst4
                            if pattern_index == 1:
                                pass
                                # State 29952
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x**m)**p)**q
                                    yield 3, subst4
                            if pattern_index == 2:
                                pass
                                # State 35828
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x**m)**p)**q
                                    yield 5, subst4
                            if pattern_index == 3:
                                pass
                                # State 40242
                                if len(subjects) == 0:
                                    pass
                                    # 6: (d*(x**j*f + e)**p)**q
                                    yield 6, subst4
                            if pattern_index == 4:
                                pass
                                # State 44804
                                if len(subjects) == 0:
                                    pass
                                    # 7: (d*(e + f*x + g*x**2)**p)**q
                                    yield 7, subst4
                        subjects.appendleft(tmp24)
                    if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                        tmp27 = subjects.popleft()
                        associative1 = tmp27
                        associative_type1 = type(tmp27)
                        subjects28 = deque(tmp27._args)
                        matcher = CommutativeMatcher33501.get()
                        tmp29 = subjects28
                        subjects28 = []
                        for s in tmp29:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp29, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 33525
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                    yield 4, subst4
                        subjects.appendleft(tmp27)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp30 = subjects.popleft()
                    subjects31 = deque(tmp30._args)
                    # State 22015
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 22016
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 22017
                            if len(subjects31) >= 1:
                                tmp34 = subjects31.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp34)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22018
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 22019
                                        if len(subjects31) == 0:
                                            pass
                                            # State 22020
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                                yield 0, subst6
                                    if len(subjects31) >= 1:
                                        tmp37 = subjects31.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp37)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22019
                                            if len(subjects31) == 0:
                                                pass
                                                # State 22020
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst6
                                        subjects31.appendleft(tmp37)
                                subjects31.appendleft(tmp34)
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35829
                            if len(subjects31) >= 1 and isinstance(subjects31[0], Pow):
                                tmp40 = subjects31.popleft()
                                subjects41 = deque(tmp40._args)
                                # State 35830
                                if len(subjects41) >= 1:
                                    tmp42 = subjects41.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.1', tmp42)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35831
                                        if len(subjects41) >= 1:
                                            tmp44 = subjects41.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.2', tmp44)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35832
                                                if len(subjects41) == 0:
                                                    pass
                                                    # State 35833
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35834
                                                        if len(subjects31) == 0:
                                                            pass
                                                            # State 35835
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                yield 5, subst7
                                                    if len(subjects31) >= 1:
                                                        tmp47 = subjects31.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2.2', tmp47)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35834
                                                            if len(subjects31) == 0:
                                                                pass
                                                                # State 35835
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                                    yield 5, subst7
                                                        subjects31.appendleft(tmp47)
                                            subjects41.appendleft(tmp44)
                                    subjects41.appendleft(tmp42)
                                if len(subjects41) >= 1:
                                    tmp49 = subjects41.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.1', tmp49)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 40243
                                        if len(subjects41) >= 1:
                                            tmp51 = subjects41.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2', tmp51)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 40244
                                                if len(subjects41) == 0:
                                                    pass
                                                    # State 40245
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 40246
                                                        if len(subjects31) == 0:
                                                            pass
                                                            # State 40247
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: (d*(x**j*f + e)**p)**q
                                                                yield 6, subst7
                                                    if len(subjects31) >= 1:
                                                        tmp54 = subjects31.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2.2', tmp54)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 40246
                                                            if len(subjects31) == 0:
                                                                pass
                                                                # State 40247
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: (d*(x**j*f + e)**p)**q
                                                                    yield 6, subst7
                                                        subjects31.appendleft(tmp54)
                                            subjects41.appendleft(tmp51)
                                    subjects41.appendleft(tmp49)
                                subjects31.appendleft(tmp40)
                        if len(subjects31) >= 1 and isinstance(subjects31[0], Mul):
                            tmp56 = subjects31.popleft()
                            associative1 = tmp56
                            associative_type1 = type(tmp56)
                            subjects57 = deque(tmp56._args)
                            matcher = CommutativeMatcher22022.get()
                            tmp58 = subjects57
                            subjects57 = []
                            for s in tmp58:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp58, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 22023
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 22024
                                        if len(subjects31) == 0:
                                            pass
                                            # State 22025
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                                yield 0, subst5
                                    if len(subjects31) >= 1:
                                        tmp60 = []
                                        tmp60.append(subjects31.popleft())
                                        while True:
                                            if len(tmp60) > 1:
                                                tmp61 = create_operation_expression(associative1, tmp60)
                                            elif len(tmp60) == 1:
                                                tmp61 = tmp60[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', tmp61)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22024
                                                if len(subjects31) == 0:
                                                    pass
                                                    # State 22025
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst5
                                            if len(subjects31) == 0:
                                                break
                                            tmp60.append(subjects31.popleft())
                                        subjects31.extendleft(reversed(tmp60))
                                if pattern_index == 1:
                                    pass
                                    # State 35840
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35841
                                        if len(subjects31) == 0:
                                            pass
                                            # State 35842
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x**m)**p)**q
                                                yield 5, subst5
                                    if len(subjects31) >= 1:
                                        tmp64 = []
                                        tmp64.append(subjects31.popleft())
                                        while True:
                                            if len(tmp64) > 1:
                                                tmp65 = create_operation_expression(associative1, tmp64)
                                            elif len(tmp64) == 1:
                                                tmp65 = tmp64[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', tmp65)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35841
                                                if len(subjects31) == 0:
                                                    pass
                                                    # State 35842
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst5
                                            if len(subjects31) == 0:
                                                break
                                            tmp64.append(subjects31.popleft())
                                        subjects31.extendleft(reversed(tmp64))
                                if pattern_index == 2:
                                    pass
                                    # State 40251
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 40252
                                        if len(subjects31) == 0:
                                            pass
                                            # State 40253
                                            if len(subjects) == 0:
                                                pass
                                                # 6: (d*(x**j*f + e)**p)**q
                                                yield 6, subst5
                                    if len(subjects31) >= 1:
                                        tmp68 = []
                                        tmp68.append(subjects31.popleft())
                                        while True:
                                            if len(tmp68) > 1:
                                                tmp69 = create_operation_expression(associative1, tmp68)
                                            elif len(tmp68) == 1:
                                                tmp69 = tmp68[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', tmp69)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 40252
                                                if len(subjects31) == 0:
                                                    pass
                                                    # State 40253
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(x**j*f + e)**p)**q
                                                        yield 6, subst5
                                            if len(subjects31) == 0:
                                                break
                                            tmp68.append(subjects31.popleft())
                                        subjects31.extendleft(reversed(tmp68))
                            subjects31.appendleft(tmp56)
                    if len(subjects31) >= 1:
                        tmp71 = subjects31.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1', tmp71)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25820
                            if len(subjects31) >= 1:
                                tmp73 = subjects31.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp73)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25821
                                    if len(subjects31) == 0:
                                        pass
                                        # State 25822
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q
                                            yield 1, subst4
                                subjects31.appendleft(tmp73)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45777
                                if len(subjects31) == 0:
                                    pass
                                    # State 45778
                                    if len(subjects) == 0:
                                        pass
                                        # 8: (d*v**p)**q
                                        yield 8, subst4
                            if len(subjects31) >= 1:
                                tmp76 = subjects31.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp76)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45777
                                    if len(subjects31) == 0:
                                        pass
                                        # State 45778
                                        if len(subjects) == 0:
                                            pass
                                            # 8: (d*v**p)**q
                                            yield 8, subst4
                                subjects31.appendleft(tmp76)
                        subjects31.appendleft(tmp71)
                    if len(subjects31) >= 1 and isinstance(subjects31[0], Add):
                        tmp78 = subjects31.popleft()
                        associative1 = tmp78
                        associative_type1 = type(tmp78)
                        subjects79 = deque(tmp78._args)
                        matcher = CommutativeMatcher22027.get()
                        tmp80 = subjects79
                        subjects79 = []
                        for s in tmp80:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp80, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 22033
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22034
                                    if len(subjects31) == 0:
                                        pass
                                        # State 22035
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                            yield 0, subst4
                                if len(subjects31) >= 1:
                                    tmp82 = []
                                    tmp82.append(subjects31.popleft())
                                    while True:
                                        if len(tmp82) > 1:
                                            tmp83 = create_operation_expression(associative1, tmp82)
                                        elif len(tmp82) == 1:
                                            tmp83 = tmp82[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp83)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22034
                                            if len(subjects31) == 0:
                                                pass
                                                # State 22035
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst4
                                        if len(subjects31) == 0:
                                            break
                                        tmp82.append(subjects31.popleft())
                                    subjects31.extendleft(reversed(tmp82))
                            if pattern_index == 1:
                                pass
                                # State 29963
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 29964
                                    if len(subjects31) == 0:
                                        pass
                                        # State 29965
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                            yield 3, subst4
                                if len(subjects31) >= 1:
                                    tmp86 = []
                                    tmp86.append(subjects31.popleft())
                                    while True:
                                        if len(tmp86) > 1:
                                            tmp87 = create_operation_expression(associative1, tmp86)
                                        elif len(tmp86) == 1:
                                            tmp87 = tmp86[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp87)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 29964
                                            if len(subjects31) == 0:
                                                pass
                                                # State 29965
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                                    yield 3, subst4
                                        if len(subjects31) == 0:
                                            break
                                        tmp86.append(subjects31.popleft())
                                    subjects31.extendleft(reversed(tmp86))
                            if pattern_index == 2:
                                pass
                                # State 35843
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35844
                                    if len(subjects31) == 0:
                                        pass
                                        # State 35845
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                            yield 5, subst4
                                if len(subjects31) >= 1:
                                    tmp90 = []
                                    tmp90.append(subjects31.popleft())
                                    while True:
                                        if len(tmp90) > 1:
                                            tmp91 = create_operation_expression(associative1, tmp90)
                                        elif len(tmp90) == 1:
                                            tmp91 = tmp90[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp91)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35844
                                            if len(subjects31) == 0:
                                                pass
                                                # State 35845
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                                    yield 5, subst4
                                        if len(subjects31) == 0:
                                            break
                                        tmp90.append(subjects31.popleft())
                                    subjects31.extendleft(reversed(tmp90))
                            if pattern_index == 3:
                                pass
                                # State 40261
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40262
                                    if len(subjects31) == 0:
                                        pass
                                        # State 40263
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(x**j*f + e)**p)**q
                                            yield 6, subst4
                                if len(subjects31) >= 1:
                                    tmp94 = []
                                    tmp94.append(subjects31.popleft())
                                    while True:
                                        if len(tmp94) > 1:
                                            tmp95 = create_operation_expression(associative1, tmp94)
                                        elif len(tmp94) == 1:
                                            tmp95 = tmp94[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp95)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 40262
                                            if len(subjects31) == 0:
                                                pass
                                                # State 40263
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(x**j*f + e)**p)**q
                                                    yield 6, subst4
                                        if len(subjects31) == 0:
                                            break
                                        tmp94.append(subjects31.popleft())
                                    subjects31.extendleft(reversed(tmp94))
                            if pattern_index == 4:
                                pass
                                # State 44812
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44813
                                    if len(subjects31) == 0:
                                        pass
                                        # State 44814
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*(e + f*x + g*x**2)**p)**q
                                            yield 7, subst4
                                if len(subjects31) >= 1:
                                    tmp98 = []
                                    tmp98.append(subjects31.popleft())
                                    while True:
                                        if len(tmp98) > 1:
                                            tmp99 = create_operation_expression(associative1, tmp98)
                                        elif len(tmp98) == 1:
                                            tmp99 = tmp98[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp99)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44813
                                            if len(subjects31) == 0:
                                                pass
                                                # State 44814
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (d*(e + f*x + g*x**2)**p)**q
                                                    yield 7, subst4
                                        if len(subjects31) == 0:
                                            break
                                        tmp98.append(subjects31.popleft())
                                    subjects31.extendleft(reversed(tmp98))
                        subjects31.appendleft(tmp78)
                    if len(subjects31) >= 1 and isinstance(subjects31[0], Mul):
                        tmp101 = subjects31.popleft()
                        associative1 = tmp101
                        associative_type1 = type(tmp101)
                        subjects102 = deque(tmp101._args)
                        matcher = CommutativeMatcher33527.get()
                        tmp103 = subjects102
                        subjects102 = []
                        for s in tmp103:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp103, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 33551
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 33552
                                    if len(subjects31) == 0:
                                        pass
                                        # State 33553
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                            yield 4, subst4
                                if len(subjects31) >= 1:
                                    tmp105 = []
                                    tmp105.append(subjects31.popleft())
                                    while True:
                                        if len(tmp105) > 1:
                                            tmp106 = create_operation_expression(associative1, tmp105)
                                        elif len(tmp105) == 1:
                                            tmp106 = tmp105[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp106)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 33552
                                            if len(subjects31) == 0:
                                                pass
                                                # State 33553
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                    yield 4, subst4
                                        if len(subjects31) == 0:
                                            break
                                        tmp105.append(subjects31.popleft())
                                    subjects31.extendleft(reversed(tmp105))
                        subjects31.appendleft(tmp101)
                    subjects.appendleft(tmp30)
            if len(subjects) >= 1:
                tmp108 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1', tmp108)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53315
                    if len(subjects) == 0:
                        pass
                        # 10: RFx**p
                        yield 10, subst2
                subjects.appendleft(tmp108)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp110 = subjects.popleft()
                associative1 = tmp110
                associative_type1 = type(tmp110)
                subjects111 = deque(tmp110._args)
                matcher = CommutativeMatcher22037.get()
                tmp112 = subjects111
                subjects111 = []
                for s in tmp112:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp112, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 22074
                        if len(subjects) == 0:
                            pass
                            # 0: (d*(e + x*f)**p)**q
                            yield 0, subst2
                    if pattern_index == 1:
                        pass
                        # State 25826
                        if len(subjects) == 0:
                            pass
                            # 1: (d*v**p)**q
                            yield 1, subst2
                    if pattern_index == 2:
                        pass
                        # State 29990
                        if len(subjects) == 0:
                            pass
                            # 3: (d*(e + f*x**m)**p)**q
                            yield 3, subst2
                    if pattern_index == 3:
                        pass
                        # State 33608
                        if len(subjects) == 0:
                            pass
                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                            yield 4, subst2
                    if pattern_index == 4:
                        pass
                        # State 35874
                        if len(subjects) == 0:
                            pass
                            # 5: (d*(e + f*x**m)**p)**q
                            yield 5, subst2
                    if pattern_index == 5:
                        pass
                        # State 40300
                        if len(subjects) == 0:
                            pass
                            # 6: (d*(x**j*f + e)**p)**q
                            yield 6, subst2
                    if pattern_index == 6:
                        pass
                        # State 44833
                        if len(subjects) == 0:
                            pass
                            # 7: (d*(e + f*x + g*x**2)**p)**q
                            yield 7, subst2
                    if pattern_index == 7:
                        pass
                        # State 45782
                        if len(subjects) == 0:
                            pass
                            # 8: (d*v**p)**q
                            yield 8, subst2
                subjects.appendleft(tmp110)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp113 = subjects.popleft()
                associative1 = tmp113
                associative_type1 = type(tmp113)
                subjects114 = deque(tmp113._args)
                matcher = CommutativeMatcher51057.get()
                tmp115 = subjects114
                subjects114 = []
                for s in tmp115:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp115, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 51070
                        if len(subjects) == 0:
                            pass
                            # 9: (d + e*x**2)**p
                            yield 9, subst2
                subjects.appendleft(tmp113)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 26261
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 26262
                if len(subjects) >= 1:
                    tmp118 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1.0', tmp118)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 26263
                        if len(subjects) == 0:
                            pass
                            # 2: e + x*f
                            yield 2, subst3
                    subjects.appendleft(tmp118)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp120 = subjects.popleft()
                associative1 = tmp120
                associative_type1 = type(tmp120)
                subjects121 = deque(tmp120._args)
                matcher = CommutativeMatcher26265.get()
                tmp122 = subjects121
                subjects121 = []
                for s in tmp122:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp122, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 26266
                        if len(subjects) == 0:
                            pass
                            # 2: e + x*f
                            yield 2, subst2
                subjects.appendleft(tmp120)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp123 = subjects.popleft()
            subjects124 = deque(tmp123._args)
            # State 22075
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 22076
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 22077
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 22078
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 22079
                            if len(subjects124) >= 1:
                                tmp129 = subjects124.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp129)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22080
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 22081
                                        if len(subjects124) == 0:
                                            pass
                                            # State 22082
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                                yield 0, subst6
                                    if len(subjects124) >= 1:
                                        tmp132 = subjects124.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2', tmp132)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22081
                                            if len(subjects124) == 0:
                                                pass
                                                # State 22082
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst6
                                        subjects124.appendleft(tmp132)
                                subjects124.appendleft(tmp129)
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35875
                            if len(subjects124) >= 1 and isinstance(subjects124[0], Pow):
                                tmp135 = subjects124.popleft()
                                subjects136 = deque(tmp135._args)
                                # State 35876
                                if len(subjects136) >= 1:
                                    tmp137 = subjects136.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.1', tmp137)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35877
                                        if len(subjects136) >= 1:
                                            tmp139 = subjects136.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.2', tmp139)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35878
                                                if len(subjects136) == 0:
                                                    pass
                                                    # State 35879
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35880
                                                        if len(subjects124) == 0:
                                                            pass
                                                            # State 35881
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                yield 5, subst7
                                                    if len(subjects124) >= 1:
                                                        tmp142 = subjects124.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', tmp142)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35880
                                                            if len(subjects124) == 0:
                                                                pass
                                                                # State 35881
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                                    yield 5, subst7
                                                        subjects124.appendleft(tmp142)
                                            subjects136.appendleft(tmp139)
                                    subjects136.appendleft(tmp137)
                                if len(subjects136) >= 1:
                                    tmp144 = subjects136.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.1', tmp144)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 40301
                                        if len(subjects136) >= 1:
                                            tmp146 = subjects136.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2', tmp146)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 40302
                                                if len(subjects136) == 0:
                                                    pass
                                                    # State 40303
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 40304
                                                        if len(subjects124) == 0:
                                                            pass
                                                            # State 40305
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: (d*(x**j*f + e)**p)**q
                                                                yield 6, subst7
                                                    if len(subjects124) >= 1:
                                                        tmp149 = subjects124.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', tmp149)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 40304
                                                            if len(subjects124) == 0:
                                                                pass
                                                                # State 40305
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: (d*(x**j*f + e)**p)**q
                                                                    yield 6, subst7
                                                        subjects124.appendleft(tmp149)
                                            subjects136.appendleft(tmp146)
                                    subjects136.appendleft(tmp144)
                                subjects124.appendleft(tmp135)
                        if len(subjects124) >= 1 and isinstance(subjects124[0], Mul):
                            tmp151 = subjects124.popleft()
                            associative1 = tmp151
                            associative_type1 = type(tmp151)
                            subjects152 = deque(tmp151._args)
                            matcher = CommutativeMatcher22084.get()
                            tmp153 = subjects152
                            subjects152 = []
                            for s in tmp153:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp153, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 22085
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 22086
                                        if len(subjects124) == 0:
                                            pass
                                            # State 22087
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                                yield 0, subst5
                                    if len(subjects124) >= 1:
                                        tmp155 = []
                                        tmp155.append(subjects124.popleft())
                                        while True:
                                            if len(tmp155) > 1:
                                                tmp156 = create_operation_expression(associative1, tmp155)
                                            elif len(tmp155) == 1:
                                                tmp156 = tmp155[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', tmp156)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22086
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 22087
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst5
                                            if len(subjects124) == 0:
                                                break
                                            tmp155.append(subjects124.popleft())
                                        subjects124.extendleft(reversed(tmp155))
                                if pattern_index == 1:
                                    pass
                                    # State 35886
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35887
                                        if len(subjects124) == 0:
                                            pass
                                            # State 35888
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x**m)**p)**q
                                                yield 5, subst5
                                    if len(subjects124) >= 1:
                                        tmp159 = []
                                        tmp159.append(subjects124.popleft())
                                        while True:
                                            if len(tmp159) > 1:
                                                tmp160 = create_operation_expression(associative1, tmp159)
                                            elif len(tmp159) == 1:
                                                tmp160 = tmp159[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', tmp160)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35887
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 35888
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst5
                                            if len(subjects124) == 0:
                                                break
                                            tmp159.append(subjects124.popleft())
                                        subjects124.extendleft(reversed(tmp159))
                                if pattern_index == 2:
                                    pass
                                    # State 40309
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 40310
                                        if len(subjects124) == 0:
                                            pass
                                            # State 40311
                                            if len(subjects) == 0:
                                                pass
                                                # 6: (d*(x**j*f + e)**p)**q
                                                yield 6, subst5
                                    if len(subjects124) >= 1:
                                        tmp163 = []
                                        tmp163.append(subjects124.popleft())
                                        while True:
                                            if len(tmp163) > 1:
                                                tmp164 = create_operation_expression(associative1, tmp163)
                                            elif len(tmp163) == 1:
                                                tmp164 = tmp163[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', tmp164)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 40310
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 40311
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(x**j*f + e)**p)**q
                                                        yield 6, subst5
                                            if len(subjects124) == 0:
                                                break
                                            tmp163.append(subjects124.popleft())
                                        subjects124.extendleft(reversed(tmp163))
                            subjects124.appendleft(tmp151)
                    if len(subjects124) >= 1:
                        tmp166 = subjects124.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1', tmp166)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45783
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45784
                                if len(subjects124) == 0:
                                    pass
                                    # State 45785
                                    if len(subjects) == 0:
                                        pass
                                        # 8: (d*v**p)**q
                                        yield 8, subst4
                            if len(subjects124) >= 1:
                                tmp169 = subjects124.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', tmp169)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45784
                                    if len(subjects124) == 0:
                                        pass
                                        # State 45785
                                        if len(subjects) == 0:
                                            pass
                                            # 8: (d*v**p)**q
                                            yield 8, subst4
                                subjects124.appendleft(tmp169)
                        subjects124.appendleft(tmp166)
                    if len(subjects124) >= 1 and isinstance(subjects124[0], Add):
                        tmp171 = subjects124.popleft()
                        associative1 = tmp171
                        associative_type1 = type(tmp171)
                        subjects172 = deque(tmp171._args)
                        matcher = CommutativeMatcher22089.get()
                        tmp173 = subjects172
                        subjects172 = []
                        for s in tmp173:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp173, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 22095
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22096
                                    if len(subjects124) == 0:
                                        pass
                                        # State 22097
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                            yield 0, subst4
                                if len(subjects124) >= 1:
                                    tmp175 = []
                                    tmp175.append(subjects124.popleft())
                                    while True:
                                        if len(tmp175) > 1:
                                            tmp176 = create_operation_expression(associative1, tmp175)
                                        elif len(tmp175) == 1:
                                            tmp176 = tmp175[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp176)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22096
                                            if len(subjects124) == 0:
                                                pass
                                                # State 22097
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst4
                                        if len(subjects124) == 0:
                                            break
                                        tmp175.append(subjects124.popleft())
                                    subjects124.extendleft(reversed(tmp175))
                            if pattern_index == 1:
                                pass
                                # State 30001
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 30002
                                    if len(subjects124) == 0:
                                        pass
                                        # State 30003
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                            yield 3, subst4
                                if len(subjects124) >= 1:
                                    tmp179 = []
                                    tmp179.append(subjects124.popleft())
                                    while True:
                                        if len(tmp179) > 1:
                                            tmp180 = create_operation_expression(associative1, tmp179)
                                        elif len(tmp179) == 1:
                                            tmp180 = tmp179[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp180)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 30002
                                            if len(subjects124) == 0:
                                                pass
                                                # State 30003
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                                    yield 3, subst4
                                        if len(subjects124) == 0:
                                            break
                                        tmp179.append(subjects124.popleft())
                                    subjects124.extendleft(reversed(tmp179))
                            if pattern_index == 2:
                                pass
                                # State 35889
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35890
                                    if len(subjects124) == 0:
                                        pass
                                        # State 35891
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                            yield 5, subst4
                                if len(subjects124) >= 1:
                                    tmp183 = []
                                    tmp183.append(subjects124.popleft())
                                    while True:
                                        if len(tmp183) > 1:
                                            tmp184 = create_operation_expression(associative1, tmp183)
                                        elif len(tmp183) == 1:
                                            tmp184 = tmp183[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp184)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35890
                                            if len(subjects124) == 0:
                                                pass
                                                # State 35891
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                                    yield 5, subst4
                                        if len(subjects124) == 0:
                                            break
                                        tmp183.append(subjects124.popleft())
                                    subjects124.extendleft(reversed(tmp183))
                            if pattern_index == 3:
                                pass
                                # State 40319
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40320
                                    if len(subjects124) == 0:
                                        pass
                                        # State 40321
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(x**j*f + e)**p)**q
                                            yield 6, subst4
                                if len(subjects124) >= 1:
                                    tmp187 = []
                                    tmp187.append(subjects124.popleft())
                                    while True:
                                        if len(tmp187) > 1:
                                            tmp188 = create_operation_expression(associative1, tmp187)
                                        elif len(tmp187) == 1:
                                            tmp188 = tmp187[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp188)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 40320
                                            if len(subjects124) == 0:
                                                pass
                                                # State 40321
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(x**j*f + e)**p)**q
                                                    yield 6, subst4
                                        if len(subjects124) == 0:
                                            break
                                        tmp187.append(subjects124.popleft())
                                    subjects124.extendleft(reversed(tmp187))
                            if pattern_index == 4:
                                pass
                                # State 44841
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44842
                                    if len(subjects124) == 0:
                                        pass
                                        # State 44843
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*(e + f*x + g*x**2)**p)**q
                                            yield 7, subst4
                                if len(subjects124) >= 1:
                                    tmp191 = []
                                    tmp191.append(subjects124.popleft())
                                    while True:
                                        if len(tmp191) > 1:
                                            tmp192 = create_operation_expression(associative1, tmp191)
                                        elif len(tmp191) == 1:
                                            tmp192 = tmp191[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp192)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44842
                                            if len(subjects124) == 0:
                                                pass
                                                # State 44843
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (d*(e + f*x + g*x**2)**p)**q
                                                    yield 7, subst4
                                        if len(subjects124) == 0:
                                            break
                                        tmp191.append(subjects124.popleft())
                                    subjects124.extendleft(reversed(tmp191))
                        subjects124.appendleft(tmp171)
                    if len(subjects124) >= 1 and isinstance(subjects124[0], Mul):
                        tmp194 = subjects124.popleft()
                        associative1 = tmp194
                        associative_type1 = type(tmp194)
                        subjects195 = deque(tmp194._args)
                        matcher = CommutativeMatcher33610.get()
                        tmp196 = subjects195
                        subjects195 = []
                        for s in tmp196:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp196, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 33634
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 33635
                                    if len(subjects124) == 0:
                                        pass
                                        # State 33636
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                            yield 4, subst4
                                if len(subjects124) >= 1:
                                    tmp198 = []
                                    tmp198.append(subjects124.popleft())
                                    while True:
                                        if len(tmp198) > 1:
                                            tmp199 = create_operation_expression(associative1, tmp198)
                                        elif len(tmp198) == 1:
                                            tmp199 = tmp198[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp199)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 33635
                                            if len(subjects124) == 0:
                                                pass
                                                # State 33636
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                    yield 4, subst4
                                        if len(subjects124) == 0:
                                            break
                                        tmp198.append(subjects124.popleft())
                                    subjects124.extendleft(reversed(tmp198))
                        subjects124.appendleft(tmp194)
                if len(subjects124) >= 1 and isinstance(subjects124[0], Pow):
                    tmp201 = subjects124.popleft()
                    subjects202 = deque(tmp201._args)
                    # State 22098
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 22099
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 22100
                            if len(subjects202) >= 1:
                                tmp205 = subjects202.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0', tmp205)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22101
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 22102
                                        if len(subjects202) == 0:
                                            pass
                                            # State 22103
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22104
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 22105
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst6
                                            if len(subjects124) >= 1:
                                                tmp209 = subjects124.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', tmp209)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22104
                                                    if len(subjects124) == 0:
                                                        pass
                                                        # State 22105
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                            yield 0, subst6
                                                subjects124.appendleft(tmp209)
                                    if len(subjects202) >= 1:
                                        tmp211 = subjects202.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp211)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22102
                                            if len(subjects202) == 0:
                                                pass
                                                # State 22103
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22104
                                                    if len(subjects124) == 0:
                                                        pass
                                                        # State 22105
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                            yield 0, subst6
                                                if len(subjects124) >= 1:
                                                    tmp214 = subjects124.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp214)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 22104
                                                        if len(subjects124) == 0:
                                                            pass
                                                            # State 22105
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                                yield 0, subst6
                                                    subjects124.appendleft(tmp214)
                                        subjects202.appendleft(tmp211)
                                subjects202.appendleft(tmp205)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35892
                            if len(subjects202) >= 1 and isinstance(subjects202[0], Pow):
                                tmp217 = subjects202.popleft()
                                subjects218 = deque(tmp217._args)
                                # State 35893
                                if len(subjects218) >= 1:
                                    tmp219 = subjects218.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2.1.1', tmp219)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35894
                                        if len(subjects218) >= 1:
                                            tmp221 = subjects218.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2.1.2', tmp221)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35895
                                                if len(subjects218) == 0:
                                                    pass
                                                    # State 35896
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35897
                                                        if len(subjects202) == 0:
                                                            pass
                                                            # State 35898
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 35899
                                                                if len(subjects124) == 0:
                                                                    pass
                                                                    # State 35900
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 5: (d*(e + f*x**m)**p)**q
                                                                        yield 5, subst7
                                                            if len(subjects124) >= 1:
                                                                tmp225 = subjects124.popleft()
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', tmp225)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 35899
                                                                    if len(subjects124) == 0:
                                                                        pass
                                                                        # State 35900
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: (d*(e + f*x**m)**p)**q
                                                                            yield 5, subst7
                                                                subjects124.appendleft(tmp225)
                                                    if len(subjects202) >= 1:
                                                        tmp227 = subjects202.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp227)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35897
                                                            if len(subjects202) == 0:
                                                                pass
                                                                # State 35898
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 35899
                                                                    if len(subjects124) == 0:
                                                                        pass
                                                                        # State 35900
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: (d*(e + f*x**m)**p)**q
                                                                            yield 5, subst7
                                                                if len(subjects124) >= 1:
                                                                    tmp230 = subjects124.popleft()
                                                                    subst7 = Substitution(subst6)
                                                                    try:
                                                                        subst7.try_add_variable('i2.2.1.2.2', tmp230)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 35899
                                                                        if len(subjects124) == 0:
                                                                            pass
                                                                            # State 35900
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                                yield 5, subst7
                                                                    subjects124.appendleft(tmp230)
                                                        subjects202.appendleft(tmp227)
                                            subjects218.appendleft(tmp221)
                                    subjects218.appendleft(tmp219)
                                if len(subjects218) >= 1:
                                    tmp232 = subjects218.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.1', tmp232)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 40322
                                        if len(subjects218) >= 1:
                                            tmp234 = subjects218.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2', tmp234)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 40323
                                                if len(subjects218) == 0:
                                                    pass
                                                    # State 40324
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 40325
                                                        if len(subjects202) == 0:
                                                            pass
                                                            # State 40326
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 40327
                                                                if len(subjects124) == 0:
                                                                    pass
                                                                    # State 40328
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 6: (d*(x**j*f + e)**p)**q
                                                                        yield 6, subst7
                                                            if len(subjects124) >= 1:
                                                                tmp238 = subjects124.popleft()
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', tmp238)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 40327
                                                                    if len(subjects124) == 0:
                                                                        pass
                                                                        # State 40328
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 6: (d*(x**j*f + e)**p)**q
                                                                            yield 6, subst7
                                                                subjects124.appendleft(tmp238)
                                                    if len(subjects202) >= 1:
                                                        tmp240 = subjects202.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp240)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 40325
                                                            if len(subjects202) == 0:
                                                                pass
                                                                # State 40326
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 40327
                                                                    if len(subjects124) == 0:
                                                                        pass
                                                                        # State 40328
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 6: (d*(x**j*f + e)**p)**q
                                                                            yield 6, subst7
                                                                if len(subjects124) >= 1:
                                                                    tmp243 = subjects124.popleft()
                                                                    subst7 = Substitution(subst6)
                                                                    try:
                                                                        subst7.try_add_variable('i2.2.1.2.2', tmp243)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 40327
                                                                        if len(subjects124) == 0:
                                                                            pass
                                                                            # State 40328
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 6: (d*(x**j*f + e)**p)**q
                                                                                yield 6, subst7
                                                                    subjects124.appendleft(tmp243)
                                                        subjects202.appendleft(tmp240)
                                            subjects218.appendleft(tmp234)
                                    subjects218.appendleft(tmp232)
                                subjects202.appendleft(tmp217)
                        if len(subjects202) >= 1 and isinstance(subjects202[0], Mul):
                            tmp245 = subjects202.popleft()
                            associative1 = tmp245
                            associative_type1 = type(tmp245)
                            subjects246 = deque(tmp245._args)
                            matcher = CommutativeMatcher22107.get()
                            tmp247 = subjects246
                            subjects246 = []
                            for s in tmp247:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp247, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 22108
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 22109
                                        if len(subjects202) == 0:
                                            pass
                                            # State 22110
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22111
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 22112
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst5
                                            if len(subjects124) >= 1:
                                                tmp250 = subjects124.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp250)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22111
                                                    if len(subjects124) == 0:
                                                        pass
                                                        # State 22112
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                            yield 0, subst5
                                                subjects124.appendleft(tmp250)
                                    if len(subjects202) >= 1:
                                        tmp252 = []
                                        tmp252.append(subjects202.popleft())
                                        while True:
                                            if len(tmp252) > 1:
                                                tmp253 = create_operation_expression(associative1, tmp252)
                                            elif len(tmp252) == 1:
                                                tmp253 = tmp252[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2.2', tmp253)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22109
                                                if len(subjects202) == 0:
                                                    pass
                                                    # State 22110
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 22111
                                                        if len(subjects124) == 0:
                                                            pass
                                                            # State 22112
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                                yield 0, subst5
                                                    if len(subjects124) >= 1:
                                                        tmp256 = subjects124.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', tmp256)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 22111
                                                            if len(subjects124) == 0:
                                                                pass
                                                                # State 22112
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 0: (d*(e + x*f)**p)**q
                                                                    yield 0, subst5
                                                        subjects124.appendleft(tmp256)
                                            if len(subjects202) == 0:
                                                break
                                            tmp252.append(subjects202.popleft())
                                        subjects202.extendleft(reversed(tmp252))
                                if pattern_index == 1:
                                    pass
                                    # State 35905
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35906
                                        if len(subjects202) == 0:
                                            pass
                                            # State 35907
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35908
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 35909
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst5
                                            if len(subjects124) >= 1:
                                                tmp260 = subjects124.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp260)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 35908
                                                    if len(subjects124) == 0:
                                                        pass
                                                        # State 35909
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x**m)**p)**q
                                                            yield 5, subst5
                                                subjects124.appendleft(tmp260)
                                    if len(subjects202) >= 1:
                                        tmp262 = []
                                        tmp262.append(subjects202.popleft())
                                        while True:
                                            if len(tmp262) > 1:
                                                tmp263 = create_operation_expression(associative1, tmp262)
                                            elif len(tmp262) == 1:
                                                tmp263 = tmp262[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2.2', tmp263)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35906
                                                if len(subjects202) == 0:
                                                    pass
                                                    # State 35907
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35908
                                                        if len(subjects124) == 0:
                                                            pass
                                                            # State 35909
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                yield 5, subst5
                                                    if len(subjects124) >= 1:
                                                        tmp266 = subjects124.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', tmp266)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35908
                                                            if len(subjects124) == 0:
                                                                pass
                                                                # State 35909
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                                    yield 5, subst5
                                                        subjects124.appendleft(tmp266)
                                            if len(subjects202) == 0:
                                                break
                                            tmp262.append(subjects202.popleft())
                                        subjects202.extendleft(reversed(tmp262))
                                if pattern_index == 2:
                                    pass
                                    # State 40332
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 40333
                                        if len(subjects202) == 0:
                                            pass
                                            # State 40334
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 40335
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 40336
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(x**j*f + e)**p)**q
                                                        yield 6, subst5
                                            if len(subjects124) >= 1:
                                                tmp270 = subjects124.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp270)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 40335
                                                    if len(subjects124) == 0:
                                                        pass
                                                        # State 40336
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: (d*(x**j*f + e)**p)**q
                                                            yield 6, subst5
                                                subjects124.appendleft(tmp270)
                                    if len(subjects202) >= 1:
                                        tmp272 = []
                                        tmp272.append(subjects202.popleft())
                                        while True:
                                            if len(tmp272) > 1:
                                                tmp273 = create_operation_expression(associative1, tmp272)
                                            elif len(tmp272) == 1:
                                                tmp273 = tmp272[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2.2', tmp273)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 40333
                                                if len(subjects202) == 0:
                                                    pass
                                                    # State 40334
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 40335
                                                        if len(subjects124) == 0:
                                                            pass
                                                            # State 40336
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: (d*(x**j*f + e)**p)**q
                                                                yield 6, subst5
                                                    if len(subjects124) >= 1:
                                                        tmp276 = subjects124.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', tmp276)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 40335
                                                            if len(subjects124) == 0:
                                                                pass
                                                                # State 40336
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: (d*(x**j*f + e)**p)**q
                                                                    yield 6, subst5
                                                        subjects124.appendleft(tmp276)
                                            if len(subjects202) == 0:
                                                break
                                            tmp272.append(subjects202.popleft())
                                        subjects202.extendleft(reversed(tmp272))
                            subjects202.appendleft(tmp245)
                    if len(subjects202) >= 1:
                        tmp278 = subjects202.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.1', tmp278)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25827
                            if len(subjects202) >= 1:
                                tmp280 = subjects202.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', tmp280)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25828
                                    if len(subjects202) == 0:
                                        pass
                                        # State 25829
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25830
                                            if len(subjects124) == 0:
                                                pass
                                                # State 25831
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*v**p)**q
                                                    yield 1, subst4
                                        if len(subjects124) >= 1:
                                            tmp283 = subjects124.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp283)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 25830
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 25831
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*v**p)**q
                                                        yield 1, subst4
                                            subjects124.appendleft(tmp283)
                                subjects202.appendleft(tmp280)
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45786
                                if len(subjects202) == 0:
                                    pass
                                    # State 45787
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45788
                                        if len(subjects124) == 0:
                                            pass
                                            # State 45789
                                            if len(subjects) == 0:
                                                pass
                                                # 8: (d*v**p)**q
                                                yield 8, subst4
                                    if len(subjects124) >= 1:
                                        tmp287 = subjects124.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp287)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45788
                                            if len(subjects124) == 0:
                                                pass
                                                # State 45789
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: (d*v**p)**q
                                                    yield 8, subst4
                                        subjects124.appendleft(tmp287)
                            if len(subjects202) >= 1:
                                tmp289 = subjects202.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', tmp289)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45786
                                    if len(subjects202) == 0:
                                        pass
                                        # State 45787
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45788
                                            if len(subjects124) == 0:
                                                pass
                                                # State 45789
                                                if len(subjects) == 0:
                                                    pass
                                                    # 8: (d*v**p)**q
                                                    yield 8, subst4
                                        if len(subjects124) >= 1:
                                            tmp292 = subjects124.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp292)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45788
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 45789
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 8: (d*v**p)**q
                                                        yield 8, subst4
                                            subjects124.appendleft(tmp292)
                                subjects202.appendleft(tmp289)
                        subjects202.appendleft(tmp278)
                    if len(subjects202) >= 1 and isinstance(subjects202[0], Add):
                        tmp294 = subjects202.popleft()
                        associative1 = tmp294
                        associative_type1 = type(tmp294)
                        subjects295 = deque(tmp294._args)
                        matcher = CommutativeMatcher22114.get()
                        tmp296 = subjects295
                        subjects295 = []
                        for s in tmp296:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp296, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 22120
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22121
                                    if len(subjects202) == 0:
                                        pass
                                        # State 22122
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22123
                                            if len(subjects124) == 0:
                                                pass
                                                # State 22124
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst4
                                        if len(subjects124) >= 1:
                                            tmp299 = subjects124.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp299)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 22123
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 22124
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst4
                                            subjects124.appendleft(tmp299)
                                if len(subjects202) >= 1:
                                    tmp301 = []
                                    tmp301.append(subjects202.popleft())
                                    while True:
                                        if len(tmp301) > 1:
                                            tmp302 = create_operation_expression(associative1, tmp301)
                                        elif len(tmp301) == 1:
                                            tmp302 = tmp301[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp302)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 22121
                                            if len(subjects202) == 0:
                                                pass
                                                # State 22122
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 22123
                                                    if len(subjects124) == 0:
                                                        pass
                                                        # State 22124
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                            yield 0, subst4
                                                if len(subjects124) >= 1:
                                                    tmp305 = subjects124.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp305)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 22123
                                                        if len(subjects124) == 0:
                                                            pass
                                                            # State 22124
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                                yield 0, subst4
                                                    subjects124.appendleft(tmp305)
                                        if len(subjects202) == 0:
                                            break
                                        tmp301.append(subjects202.popleft())
                                    subjects202.extendleft(reversed(tmp301))
                            if pattern_index == 1:
                                pass
                                # State 30014
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 30015
                                    if len(subjects202) == 0:
                                        pass
                                        # State 30016
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 30017
                                            if len(subjects124) == 0:
                                                pass
                                                # State 30018
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                                    yield 3, subst4
                                        if len(subjects124) >= 1:
                                            tmp309 = subjects124.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp309)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 30017
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 30018
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x**m)**p)**q
                                                        yield 3, subst4
                                            subjects124.appendleft(tmp309)
                                if len(subjects202) >= 1:
                                    tmp311 = []
                                    tmp311.append(subjects202.popleft())
                                    while True:
                                        if len(tmp311) > 1:
                                            tmp312 = create_operation_expression(associative1, tmp311)
                                        elif len(tmp311) == 1:
                                            tmp312 = tmp311[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp312)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 30015
                                            if len(subjects202) == 0:
                                                pass
                                                # State 30016
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 30017
                                                    if len(subjects124) == 0:
                                                        pass
                                                        # State 30018
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: (d*(e + f*x**m)**p)**q
                                                            yield 3, subst4
                                                if len(subjects124) >= 1:
                                                    tmp315 = subjects124.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp315)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 30017
                                                        if len(subjects124) == 0:
                                                            pass
                                                            # State 30018
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: (d*(e + f*x**m)**p)**q
                                                                yield 3, subst4
                                                    subjects124.appendleft(tmp315)
                                        if len(subjects202) == 0:
                                            break
                                        tmp311.append(subjects202.popleft())
                                    subjects202.extendleft(reversed(tmp311))
                            if pattern_index == 2:
                                pass
                                # State 35910
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35911
                                    if len(subjects202) == 0:
                                        pass
                                        # State 35912
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35913
                                            if len(subjects124) == 0:
                                                pass
                                                # State 35914
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                                    yield 5, subst4
                                        if len(subjects124) >= 1:
                                            tmp319 = subjects124.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp319)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35913
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 35914
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst4
                                            subjects124.appendleft(tmp319)
                                if len(subjects202) >= 1:
                                    tmp321 = []
                                    tmp321.append(subjects202.popleft())
                                    while True:
                                        if len(tmp321) > 1:
                                            tmp322 = create_operation_expression(associative1, tmp321)
                                        elif len(tmp321) == 1:
                                            tmp322 = tmp321[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp322)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35911
                                            if len(subjects202) == 0:
                                                pass
                                                # State 35912
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 35913
                                                    if len(subjects124) == 0:
                                                        pass
                                                        # State 35914
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x**m)**p)**q
                                                            yield 5, subst4
                                                if len(subjects124) >= 1:
                                                    tmp325 = subjects124.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp325)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35913
                                                        if len(subjects124) == 0:
                                                            pass
                                                            # State 35914
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                yield 5, subst4
                                                    subjects124.appendleft(tmp325)
                                        if len(subjects202) == 0:
                                            break
                                        tmp321.append(subjects202.popleft())
                                    subjects202.extendleft(reversed(tmp321))
                            if pattern_index == 3:
                                pass
                                # State 40344
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40345
                                    if len(subjects202) == 0:
                                        pass
                                        # State 40346
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 40347
                                            if len(subjects124) == 0:
                                                pass
                                                # State 40348
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(x**j*f + e)**p)**q
                                                    yield 6, subst4
                                        if len(subjects124) >= 1:
                                            tmp329 = subjects124.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp329)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 40347
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 40348
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(x**j*f + e)**p)**q
                                                        yield 6, subst4
                                            subjects124.appendleft(tmp329)
                                if len(subjects202) >= 1:
                                    tmp331 = []
                                    tmp331.append(subjects202.popleft())
                                    while True:
                                        if len(tmp331) > 1:
                                            tmp332 = create_operation_expression(associative1, tmp331)
                                        elif len(tmp331) == 1:
                                            tmp332 = tmp331[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp332)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 40345
                                            if len(subjects202) == 0:
                                                pass
                                                # State 40346
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 40347
                                                    if len(subjects124) == 0:
                                                        pass
                                                        # State 40348
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: (d*(x**j*f + e)**p)**q
                                                            yield 6, subst4
                                                if len(subjects124) >= 1:
                                                    tmp335 = subjects124.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp335)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 40347
                                                        if len(subjects124) == 0:
                                                            pass
                                                            # State 40348
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: (d*(x**j*f + e)**p)**q
                                                                yield 6, subst4
                                                    subjects124.appendleft(tmp335)
                                        if len(subjects202) == 0:
                                            break
                                        tmp331.append(subjects202.popleft())
                                    subjects202.extendleft(reversed(tmp331))
                            if pattern_index == 4:
                                pass
                                # State 44851
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44852
                                    if len(subjects202) == 0:
                                        pass
                                        # State 44853
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44854
                                            if len(subjects124) == 0:
                                                pass
                                                # State 44855
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (d*(e + f*x + g*x**2)**p)**q
                                                    yield 7, subst4
                                        if len(subjects124) >= 1:
                                            tmp339 = subjects124.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp339)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 44854
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 44855
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: (d*(e + f*x + g*x**2)**p)**q
                                                        yield 7, subst4
                                            subjects124.appendleft(tmp339)
                                if len(subjects202) >= 1:
                                    tmp341 = []
                                    tmp341.append(subjects202.popleft())
                                    while True:
                                        if len(tmp341) > 1:
                                            tmp342 = create_operation_expression(associative1, tmp341)
                                        elif len(tmp341) == 1:
                                            tmp342 = tmp341[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp342)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44852
                                            if len(subjects202) == 0:
                                                pass
                                                # State 44853
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 44854
                                                    if len(subjects124) == 0:
                                                        pass
                                                        # State 44855
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 7: (d*(e + f*x + g*x**2)**p)**q
                                                            yield 7, subst4
                                                if len(subjects124) >= 1:
                                                    tmp345 = subjects124.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp345)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 44854
                                                        if len(subjects124) == 0:
                                                            pass
                                                            # State 44855
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 7: (d*(e + f*x + g*x**2)**p)**q
                                                                yield 7, subst4
                                                    subjects124.appendleft(tmp345)
                                        if len(subjects202) == 0:
                                            break
                                        tmp341.append(subjects202.popleft())
                                    subjects202.extendleft(reversed(tmp341))
                        subjects202.appendleft(tmp294)
                    if len(subjects202) >= 1 and isinstance(subjects202[0], Mul):
                        tmp347 = subjects202.popleft()
                        associative1 = tmp347
                        associative_type1 = type(tmp347)
                        subjects348 = deque(tmp347._args)
                        matcher = CommutativeMatcher33638.get()
                        tmp349 = subjects348
                        subjects348 = []
                        for s in tmp349:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp349, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 33662
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 33663
                                    if len(subjects202) == 0:
                                        pass
                                        # State 33664
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 33665
                                            if len(subjects124) == 0:
                                                pass
                                                # State 33666
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                    yield 4, subst4
                                        if len(subjects124) >= 1:
                                            tmp352 = subjects124.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp352)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 33665
                                                if len(subjects124) == 0:
                                                    pass
                                                    # State 33666
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                        yield 4, subst4
                                            subjects124.appendleft(tmp352)
                                if len(subjects202) >= 1:
                                    tmp354 = []
                                    tmp354.append(subjects202.popleft())
                                    while True:
                                        if len(tmp354) > 1:
                                            tmp355 = create_operation_expression(associative1, tmp354)
                                        elif len(tmp354) == 1:
                                            tmp355 = tmp354[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp355)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 33663
                                            if len(subjects202) == 0:
                                                pass
                                                # State 33664
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 33665
                                                    if len(subjects124) == 0:
                                                        pass
                                                        # State 33666
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                            yield 4, subst4
                                                if len(subjects124) >= 1:
                                                    tmp358 = subjects124.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp358)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 33665
                                                        if len(subjects124) == 0:
                                                            pass
                                                            # State 33666
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                                yield 4, subst4
                                                    subjects124.appendleft(tmp358)
                                        if len(subjects202) == 0:
                                            break
                                        tmp354.append(subjects202.popleft())
                                    subjects202.extendleft(reversed(tmp354))
                        subjects202.appendleft(tmp347)
                    subjects124.appendleft(tmp201)
            if len(subjects124) >= 1:
                tmp360 = subjects124.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1', tmp360)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53316
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53317
                        if len(subjects124) == 0:
                            pass
                            # State 53318
                            if len(subjects) == 0:
                                pass
                                # 10: RFx**p
                                yield 10, subst2
                    if len(subjects124) >= 1:
                        tmp363 = subjects124.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', tmp363)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53317
                            if len(subjects124) == 0:
                                pass
                                # State 53318
                                if len(subjects) == 0:
                                    pass
                                    # 10: RFx**p
                                    yield 10, subst2
                        subjects124.appendleft(tmp363)
                subjects124.appendleft(tmp360)
            if len(subjects124) >= 1 and isinstance(subjects124[0], Mul):
                tmp365 = subjects124.popleft()
                associative1 = tmp365
                associative_type1 = type(tmp365)
                subjects366 = deque(tmp365._args)
                matcher = CommutativeMatcher22126.get()
                tmp367 = subjects366
                subjects366 = []
                for s in tmp367:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp367, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 22163
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 22164
                            if len(subjects124) == 0:
                                pass
                                # State 22165
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q
                                    yield 0, subst2
                        if len(subjects124) >= 1:
                            tmp369 = []
                            tmp369.append(subjects124.popleft())
                            while True:
                                if len(tmp369) > 1:
                                    tmp370 = create_operation_expression(associative1, tmp369)
                                elif len(tmp369) == 1:
                                    tmp370 = tmp369[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp370)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 22164
                                    if len(subjects124) == 0:
                                        pass
                                        # State 22165
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                            yield 0, subst2
                                if len(subjects124) == 0:
                                    break
                                tmp369.append(subjects124.popleft())
                            subjects124.extendleft(reversed(tmp369))
                    if pattern_index == 1:
                        pass
                        # State 25835
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25836
                            if len(subjects124) == 0:
                                pass
                                # State 25837
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d*v**p)**q
                                    yield 1, subst2
                        if len(subjects124) >= 1:
                            tmp373 = []
                            tmp373.append(subjects124.popleft())
                            while True:
                                if len(tmp373) > 1:
                                    tmp374 = create_operation_expression(associative1, tmp373)
                                elif len(tmp373) == 1:
                                    tmp374 = tmp373[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp374)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25836
                                    if len(subjects124) == 0:
                                        pass
                                        # State 25837
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q
                                            yield 1, subst2
                                if len(subjects124) == 0:
                                    break
                                tmp373.append(subjects124.popleft())
                            subjects124.extendleft(reversed(tmp373))
                    if pattern_index == 2:
                        pass
                        # State 30043
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 30044
                            if len(subjects124) == 0:
                                pass
                                # State 30045
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x**m)**p)**q
                                    yield 3, subst2
                        if len(subjects124) >= 1:
                            tmp377 = []
                            tmp377.append(subjects124.popleft())
                            while True:
                                if len(tmp377) > 1:
                                    tmp378 = create_operation_expression(associative1, tmp377)
                                elif len(tmp377) == 1:
                                    tmp378 = tmp377[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp378)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 30044
                                    if len(subjects124) == 0:
                                        pass
                                        # State 30045
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                            yield 3, subst2
                                if len(subjects124) == 0:
                                    break
                                tmp377.append(subjects124.popleft())
                            subjects124.extendleft(reversed(tmp377))
                    if pattern_index == 3:
                        pass
                        # State 33721
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 33722
                            if len(subjects124) == 0:
                                pass
                                # State 33723
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                    yield 4, subst2
                        if len(subjects124) >= 1:
                            tmp381 = []
                            tmp381.append(subjects124.popleft())
                            while True:
                                if len(tmp381) > 1:
                                    tmp382 = create_operation_expression(associative1, tmp381)
                                elif len(tmp381) == 1:
                                    tmp382 = tmp381[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp382)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 33722
                                    if len(subjects124) == 0:
                                        pass
                                        # State 33723
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                            yield 4, subst2
                                if len(subjects124) == 0:
                                    break
                                tmp381.append(subjects124.popleft())
                            subjects124.extendleft(reversed(tmp381))
                    if pattern_index == 4:
                        pass
                        # State 35943
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35944
                            if len(subjects124) == 0:
                                pass
                                # State 35945
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x**m)**p)**q
                                    yield 5, subst2
                        if len(subjects124) >= 1:
                            tmp385 = []
                            tmp385.append(subjects124.popleft())
                            while True:
                                if len(tmp385) > 1:
                                    tmp386 = create_operation_expression(associative1, tmp385)
                                elif len(tmp385) == 1:
                                    tmp386 = tmp385[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp386)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35944
                                    if len(subjects124) == 0:
                                        pass
                                        # State 35945
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                            yield 5, subst2
                                if len(subjects124) == 0:
                                    break
                                tmp385.append(subjects124.popleft())
                            subjects124.extendleft(reversed(tmp385))
                    if pattern_index == 5:
                        pass
                        # State 40385
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40386
                            if len(subjects124) == 0:
                                pass
                                # State 40387
                                if len(subjects) == 0:
                                    pass
                                    # 6: (d*(x**j*f + e)**p)**q
                                    yield 6, subst2
                        if len(subjects124) >= 1:
                            tmp389 = []
                            tmp389.append(subjects124.popleft())
                            while True:
                                if len(tmp389) > 1:
                                    tmp390 = create_operation_expression(associative1, tmp389)
                                elif len(tmp389) == 1:
                                    tmp390 = tmp389[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp390)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40386
                                    if len(subjects124) == 0:
                                        pass
                                        # State 40387
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(x**j*f + e)**p)**q
                                            yield 6, subst2
                                if len(subjects124) == 0:
                                    break
                                tmp389.append(subjects124.popleft())
                            subjects124.extendleft(reversed(tmp389))
                    if pattern_index == 6:
                        pass
                        # State 44874
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 44875
                            if len(subjects124) == 0:
                                pass
                                # State 44876
                                if len(subjects) == 0:
                                    pass
                                    # 7: (d*(e + f*x + g*x**2)**p)**q
                                    yield 7, subst2
                        if len(subjects124) >= 1:
                            tmp393 = []
                            tmp393.append(subjects124.popleft())
                            while True:
                                if len(tmp393) > 1:
                                    tmp394 = create_operation_expression(associative1, tmp393)
                                elif len(tmp393) == 1:
                                    tmp394 = tmp393[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp394)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44875
                                    if len(subjects124) == 0:
                                        pass
                                        # State 44876
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*(e + f*x + g*x**2)**p)**q
                                            yield 7, subst2
                                if len(subjects124) == 0:
                                    break
                                tmp393.append(subjects124.popleft())
                            subjects124.extendleft(reversed(tmp393))
                    if pattern_index == 7:
                        pass
                        # State 45793
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45794
                            if len(subjects124) == 0:
                                pass
                                # State 45795
                                if len(subjects) == 0:
                                    pass
                                    # 8: (d*v**p)**q
                                    yield 8, subst2
                        if len(subjects124) >= 1:
                            tmp397 = []
                            tmp397.append(subjects124.popleft())
                            while True:
                                if len(tmp397) > 1:
                                    tmp398 = create_operation_expression(associative1, tmp397)
                                elif len(tmp397) == 1:
                                    tmp398 = tmp397[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp398)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45794
                                    if len(subjects124) == 0:
                                        pass
                                        # State 45795
                                        if len(subjects) == 0:
                                            pass
                                            # 8: (d*v**p)**q
                                            yield 8, subst2
                                if len(subjects124) == 0:
                                    break
                                tmp397.append(subjects124.popleft())
                            subjects124.extendleft(reversed(tmp397))
                subjects124.appendleft(tmp365)
            if len(subjects124) >= 1 and isinstance(subjects124[0], Add):
                tmp400 = subjects124.popleft()
                associative1 = tmp400
                associative_type1 = type(tmp400)
                subjects401 = deque(tmp400._args)
                matcher = CommutativeMatcher51072.get()
                tmp402 = subjects401
                subjects401 = []
                for s in tmp402:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp402, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 51085
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 51086
                            if len(subjects124) == 0:
                                pass
                                # State 51087
                                if len(subjects) == 0:
                                    pass
                                    # 9: (d + e*x**2)**p
                                    yield 9, subst2
                        if len(subjects124) >= 1:
                            tmp404 = []
                            tmp404.append(subjects124.popleft())
                            while True:
                                if len(tmp404) > 1:
                                    tmp405 = create_operation_expression(associative1, tmp404)
                                elif len(tmp404) == 1:
                                    tmp405 = tmp404[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp405)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51086
                                    if len(subjects124) == 0:
                                        pass
                                        # State 51087
                                        if len(subjects) == 0:
                                            pass
                                            # 9: (d + e*x**2)**p
                                            yield 9, subst2
                                if len(subjects124) == 0:
                                    break
                                tmp404.append(subjects124.popleft())
                            subjects124.extendleft(reversed(tmp404))
                subjects124.appendleft(tmp400)
            subjects.appendleft(tmp123)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp407 = subjects.popleft()
            associative1 = tmp407
            associative_type1 = type(tmp407)
            subjects408 = deque(tmp407._args)
            matcher = CommutativeMatcher26268.get()
            tmp409 = subjects408
            subjects408 = []
            for s in tmp409:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp409, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 26274
                    if len(subjects) == 0:
                        pass
                        # 2: e + x*f
                        yield 2, subst1
            subjects.appendleft(tmp407)
        return
        yield


from .generated_part005357 import *
from .generated_part005384 import *
from .generated_part005387 import *
from .generated_part005353 import *
from .generated_part005350 import *
from .generated_part005405 import *
from .generated_part005362 import *
from .generated_part005381 import *
from .generated_part005351 import *
from .generated_part005403 import *
from .generated_part005390 import *
from .generated_part005377 import *
from collections import deque
from .generated_part005375 import *
from matchpy.utils import VariableWithCount
from .generated_part005359 import *
from multiset import Multiset
from .generated_part005378 import *
from .generated_part005379 import *
from .generated_part005385 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part005356 import *