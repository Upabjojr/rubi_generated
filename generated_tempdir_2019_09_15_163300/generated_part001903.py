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


class CommutativeMatcher23084(CommutativeMatcher):
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
        if CommutativeMatcher23084._instance is None:
            CommutativeMatcher23084._instance = CommutativeMatcher23084()
        return CommutativeMatcher23084._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 23083
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 23085
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 23086
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 23087
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 23088
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 23089
                            if len(subjects) >= 1:
                                tmp6 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp6)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 23090
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
                            # State 34423
                            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                                tmp9 = subjects.popleft()
                                subjects10 = deque(tmp9._args)
                                # State 34424
                                if len(subjects10) >= 1:
                                    tmp11 = subjects10.popleft()
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2.1.1', tmp11)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 34425
                                        if len(subjects10) >= 1:
                                            tmp13 = subjects10.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2.2.1.2', tmp13)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34426
                                                if len(subjects10) == 0:
                                                    pass
                                                    # State 34427
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst7
                                            subjects10.appendleft(tmp13)
                                    subjects10.appendleft(tmp11)
                                subjects.appendleft(tmp9)
                        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                            tmp15 = subjects.popleft()
                            associative1 = tmp15
                            associative_type1 = type(tmp15)
                            subjects16 = deque(tmp15._args)
                            matcher = CommutativeMatcher23092.get()
                            tmp17 = subjects16
                            subjects16 = []
                            for s in tmp17:
                                matcher.add_subject(s)
                            for pattern_index, subst5 in matcher.match(tmp17, subst4):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 23093
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(e + x*f)**p)**q
                                        yield 0, subst5
                                if pattern_index == 1:
                                    pass
                                    # State 34432
                                    if len(subjects) == 0:
                                        pass
                                        # 5: (d*(e + f*x**m)**p)**q
                                        yield 5, subst5
                            subjects.appendleft(tmp15)
                    if len(subjects) >= 1:
                        tmp18 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.1', tmp18)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45517
                            if len(subjects) == 0:
                                pass
                                # 7: (d*v**p)**q
                                yield 7, subst4
                        subjects.appendleft(tmp18)
                    if len(subjects) >= 1 and isinstance(subjects[0], Add):
                        tmp20 = subjects.popleft()
                        associative1 = tmp20
                        associative_type1 = type(tmp20)
                        subjects21 = deque(tmp20._args)
                        matcher = CommutativeMatcher23095.get()
                        tmp22 = subjects21
                        subjects21 = []
                        for s in tmp22:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp22, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 23101
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q
                                    yield 0, subst4
                            if pattern_index == 1:
                                pass
                                # State 28853
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x**m)**p)**q
                                    yield 3, subst4
                            if pattern_index == 2:
                                pass
                                # State 34433
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x**m)**p)**q
                                    yield 5, subst4
                            if pattern_index == 3:
                                pass
                                # State 43945
                                if len(subjects) == 0:
                                    pass
                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                    yield 6, subst4
                        subjects.appendleft(tmp20)
                    if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                        tmp23 = subjects.popleft()
                        associative1 = tmp23
                        associative_type1 = type(tmp23)
                        subjects24 = deque(tmp23._args)
                        matcher = CommutativeMatcher31202.get()
                        tmp25 = subjects24
                        subjects24 = []
                        for s in tmp25:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp25, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 31226
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                    yield 4, subst4
                        subjects.appendleft(tmp23)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp26 = subjects.popleft()
                    subjects27 = deque(tmp26._args)
                    # State 23102
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 23103
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 23104
                            if len(subjects27) >= 1:
                                tmp30 = subjects27.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp30)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 23105
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 23106
                                        if len(subjects27) == 0:
                                            pass
                                            # State 23107
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                                yield 0, subst6
                                    if len(subjects27) >= 1:
                                        tmp33 = subjects27.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp33)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 23106
                                            if len(subjects27) == 0:
                                                pass
                                                # State 23107
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst6
                                        subjects27.appendleft(tmp33)
                                subjects27.appendleft(tmp30)
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 34434
                            if len(subjects27) >= 1 and isinstance(subjects27[0], Pow):
                                tmp36 = subjects27.popleft()
                                subjects37 = deque(tmp36._args)
                                # State 34435
                                if len(subjects37) >= 1:
                                    tmp38 = subjects37.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.1', tmp38)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 34436
                                        if len(subjects37) >= 1:
                                            tmp40 = subjects37.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.2', tmp40)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34437
                                                if len(subjects37) == 0:
                                                    pass
                                                    # State 34438
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34439
                                                        if len(subjects27) == 0:
                                                            pass
                                                            # State 34440
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                yield 5, subst7
                                                    if len(subjects27) >= 1:
                                                        tmp43 = subjects27.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2.2', tmp43)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 34439
                                                            if len(subjects27) == 0:
                                                                pass
                                                                # State 34440
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                                    yield 5, subst7
                                                        subjects27.appendleft(tmp43)
                                            subjects37.appendleft(tmp40)
                                    subjects37.appendleft(tmp38)
                                subjects27.appendleft(tmp36)
                        if len(subjects27) >= 1 and isinstance(subjects27[0], Mul):
                            tmp45 = subjects27.popleft()
                            associative1 = tmp45
                            associative_type1 = type(tmp45)
                            subjects46 = deque(tmp45._args)
                            matcher = CommutativeMatcher23109.get()
                            tmp47 = subjects46
                            subjects46 = []
                            for s in tmp47:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp47, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 23110
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 23111
                                        if len(subjects27) == 0:
                                            pass
                                            # State 23112
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                                yield 0, subst5
                                    if len(subjects27) >= 1:
                                        tmp49 = []
                                        tmp49.append(subjects27.popleft())
                                        while True:
                                            if len(tmp49) > 1:
                                                tmp50 = create_operation_expression(associative1, tmp49)
                                            elif len(tmp49) == 1:
                                                tmp50 = tmp49[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', tmp50)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 23111
                                                if len(subjects27) == 0:
                                                    pass
                                                    # State 23112
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst5
                                            if len(subjects27) == 0:
                                                break
                                            tmp49.append(subjects27.popleft())
                                        subjects27.extendleft(reversed(tmp49))
                                if pattern_index == 1:
                                    pass
                                    # State 34445
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 34446
                                        if len(subjects27) == 0:
                                            pass
                                            # State 34447
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x**m)**p)**q
                                                yield 5, subst5
                                    if len(subjects27) >= 1:
                                        tmp53 = []
                                        tmp53.append(subjects27.popleft())
                                        while True:
                                            if len(tmp53) > 1:
                                                tmp54 = create_operation_expression(associative1, tmp53)
                                            elif len(tmp53) == 1:
                                                tmp54 = tmp53[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', tmp54)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34446
                                                if len(subjects27) == 0:
                                                    pass
                                                    # State 34447
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst5
                                            if len(subjects27) == 0:
                                                break
                                            tmp53.append(subjects27.popleft())
                                        subjects27.extendleft(reversed(tmp53))
                            subjects27.appendleft(tmp45)
                    if len(subjects27) >= 1:
                        tmp56 = subjects27.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1', tmp56)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25595
                            if len(subjects27) >= 1:
                                tmp58 = subjects27.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp58)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25596
                                    if len(subjects27) == 0:
                                        pass
                                        # State 25597
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q
                                            yield 1, subst4
                                subjects27.appendleft(tmp58)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45518
                                if len(subjects27) == 0:
                                    pass
                                    # State 45519
                                    if len(subjects) == 0:
                                        pass
                                        # 7: (d*v**p)**q
                                        yield 7, subst4
                            if len(subjects27) >= 1:
                                tmp61 = subjects27.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp61)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45518
                                    if len(subjects27) == 0:
                                        pass
                                        # State 45519
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*v**p)**q
                                            yield 7, subst4
                                subjects27.appendleft(tmp61)
                        subjects27.appendleft(tmp56)
                    if len(subjects27) >= 1 and isinstance(subjects27[0], Add):
                        tmp63 = subjects27.popleft()
                        associative1 = tmp63
                        associative_type1 = type(tmp63)
                        subjects64 = deque(tmp63._args)
                        matcher = CommutativeMatcher23114.get()
                        tmp65 = subjects64
                        subjects64 = []
                        for s in tmp65:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp65, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 23120
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 23121
                                    if len(subjects27) == 0:
                                        pass
                                        # State 23122
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                            yield 0, subst4
                                if len(subjects27) >= 1:
                                    tmp67 = []
                                    tmp67.append(subjects27.popleft())
                                    while True:
                                        if len(tmp67) > 1:
                                            tmp68 = create_operation_expression(associative1, tmp67)
                                        elif len(tmp67) == 1:
                                            tmp68 = tmp67[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp68)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 23121
                                            if len(subjects27) == 0:
                                                pass
                                                # State 23122
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst4
                                        if len(subjects27) == 0:
                                            break
                                        tmp67.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp67))
                            if pattern_index == 1:
                                pass
                                # State 28864
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28865
                                    if len(subjects27) == 0:
                                        pass
                                        # State 28866
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                            yield 3, subst4
                                if len(subjects27) >= 1:
                                    tmp71 = []
                                    tmp71.append(subjects27.popleft())
                                    while True:
                                        if len(tmp71) > 1:
                                            tmp72 = create_operation_expression(associative1, tmp71)
                                        elif len(tmp71) == 1:
                                            tmp72 = tmp71[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp72)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28865
                                            if len(subjects27) == 0:
                                                pass
                                                # State 28866
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                                    yield 3, subst4
                                        if len(subjects27) == 0:
                                            break
                                        tmp71.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp71))
                            if pattern_index == 2:
                                pass
                                # State 34448
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 34449
                                    if len(subjects27) == 0:
                                        pass
                                        # State 34450
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                            yield 5, subst4
                                if len(subjects27) >= 1:
                                    tmp75 = []
                                    tmp75.append(subjects27.popleft())
                                    while True:
                                        if len(tmp75) > 1:
                                            tmp76 = create_operation_expression(associative1, tmp75)
                                        elif len(tmp75) == 1:
                                            tmp76 = tmp75[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp76)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 34449
                                            if len(subjects27) == 0:
                                                pass
                                                # State 34450
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                                    yield 5, subst4
                                        if len(subjects27) == 0:
                                            break
                                        tmp75.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp75))
                            if pattern_index == 3:
                                pass
                                # State 43953
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 43954
                                    if len(subjects27) == 0:
                                        pass
                                        # State 43955
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                            yield 6, subst4
                                if len(subjects27) >= 1:
                                    tmp79 = []
                                    tmp79.append(subjects27.popleft())
                                    while True:
                                        if len(tmp79) > 1:
                                            tmp80 = create_operation_expression(associative1, tmp79)
                                        elif len(tmp79) == 1:
                                            tmp80 = tmp79[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp80)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43954
                                            if len(subjects27) == 0:
                                                pass
                                                # State 43955
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                                    yield 6, subst4
                                        if len(subjects27) == 0:
                                            break
                                        tmp79.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp79))
                        subjects27.appendleft(tmp63)
                    if len(subjects27) >= 1 and isinstance(subjects27[0], Mul):
                        tmp82 = subjects27.popleft()
                        associative1 = tmp82
                        associative_type1 = type(tmp82)
                        subjects83 = deque(tmp82._args)
                        matcher = CommutativeMatcher31228.get()
                        tmp84 = subjects83
                        subjects83 = []
                        for s in tmp84:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp84, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 31252
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 31253
                                    if len(subjects27) == 0:
                                        pass
                                        # State 31254
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                            yield 4, subst4
                                if len(subjects27) >= 1:
                                    tmp86 = []
                                    tmp86.append(subjects27.popleft())
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
                                            # State 31253
                                            if len(subjects27) == 0:
                                                pass
                                                # State 31254
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                    yield 4, subst4
                                        if len(subjects27) == 0:
                                            break
                                        tmp86.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp86))
                        subjects27.appendleft(tmp82)
                    subjects.appendleft(tmp26)
            if len(subjects) >= 1:
                tmp89 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1', tmp89)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53244
                    if len(subjects) == 0:
                        pass
                        # 8: RFx**p
                        yield 8, subst2
                subjects.appendleft(tmp89)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp91 = subjects.popleft()
                associative1 = tmp91
                associative_type1 = type(tmp91)
                subjects92 = deque(tmp91._args)
                matcher = CommutativeMatcher23124.get()
                tmp93 = subjects92
                subjects92 = []
                for s in tmp93:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp93, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 23161
                        if len(subjects) == 0:
                            pass
                            # 0: (d*(e + x*f)**p)**q
                            yield 0, subst2
                    if pattern_index == 1:
                        pass
                        # State 25601
                        if len(subjects) == 0:
                            pass
                            # 1: (d*v**p)**q
                            yield 1, subst2
                    if pattern_index == 2:
                        pass
                        # State 28891
                        if len(subjects) == 0:
                            pass
                            # 3: (d*(e + f*x**m)**p)**q
                            yield 3, subst2
                    if pattern_index == 3:
                        pass
                        # State 31309
                        if len(subjects) == 0:
                            pass
                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                            yield 4, subst2
                    if pattern_index == 4:
                        pass
                        # State 34479
                        if len(subjects) == 0:
                            pass
                            # 5: (d*(e + f*x**m)**p)**q
                            yield 5, subst2
                    if pattern_index == 5:
                        pass
                        # State 43974
                        if len(subjects) == 0:
                            pass
                            # 6: (d*(e + f*x + g*x**2)**p)**q
                            yield 6, subst2
                    if pattern_index == 6:
                        pass
                        # State 45523
                        if len(subjects) == 0:
                            pass
                            # 7: (d*v**p)**q
                            yield 7, subst2
                subjects.appendleft(tmp91)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 26083
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 26084
                if len(subjects) >= 1:
                    tmp96 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1.0', tmp96)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 26085
                        if len(subjects) == 0:
                            pass
                            # 2: e + x*f
                            yield 2, subst3
                    subjects.appendleft(tmp96)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp98 = subjects.popleft()
                associative1 = tmp98
                associative_type1 = type(tmp98)
                subjects99 = deque(tmp98._args)
                matcher = CommutativeMatcher26087.get()
                tmp100 = subjects99
                subjects99 = []
                for s in tmp100:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp100, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 26088
                        if len(subjects) == 0:
                            pass
                            # 2: e + x*f
                            yield 2, subst2
                subjects.appendleft(tmp98)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp101 = subjects.popleft()
            subjects102 = deque(tmp101._args)
            # State 23162
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 23163
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 23164
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 23165
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 23166
                            if len(subjects102) >= 1:
                                tmp107 = subjects102.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp107)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 23167
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 23168
                                        if len(subjects102) == 0:
                                            pass
                                            # State 23169
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                                yield 0, subst6
                                    if len(subjects102) >= 1:
                                        tmp110 = subjects102.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2', tmp110)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 23168
                                            if len(subjects102) == 0:
                                                pass
                                                # State 23169
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst6
                                        subjects102.appendleft(tmp110)
                                subjects102.appendleft(tmp107)
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 34480
                            if len(subjects102) >= 1 and isinstance(subjects102[0], Pow):
                                tmp113 = subjects102.popleft()
                                subjects114 = deque(tmp113._args)
                                # State 34481
                                if len(subjects114) >= 1:
                                    tmp115 = subjects114.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.1', tmp115)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 34482
                                        if len(subjects114) >= 1:
                                            tmp117 = subjects114.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.2', tmp117)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34483
                                                if len(subjects114) == 0:
                                                    pass
                                                    # State 34484
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34485
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 34486
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                yield 5, subst7
                                                    if len(subjects102) >= 1:
                                                        tmp120 = subjects102.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', tmp120)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 34485
                                                            if len(subjects102) == 0:
                                                                pass
                                                                # State 34486
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                                    yield 5, subst7
                                                        subjects102.appendleft(tmp120)
                                            subjects114.appendleft(tmp117)
                                    subjects114.appendleft(tmp115)
                                subjects102.appendleft(tmp113)
                        if len(subjects102) >= 1 and isinstance(subjects102[0], Mul):
                            tmp122 = subjects102.popleft()
                            associative1 = tmp122
                            associative_type1 = type(tmp122)
                            subjects123 = deque(tmp122._args)
                            matcher = CommutativeMatcher23171.get()
                            tmp124 = subjects123
                            subjects123 = []
                            for s in tmp124:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp124, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 23172
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 23173
                                        if len(subjects102) == 0:
                                            pass
                                            # State 23174
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                                yield 0, subst5
                                    if len(subjects102) >= 1:
                                        tmp126 = []
                                        tmp126.append(subjects102.popleft())
                                        while True:
                                            if len(tmp126) > 1:
                                                tmp127 = create_operation_expression(associative1, tmp126)
                                            elif len(tmp126) == 1:
                                                tmp127 = tmp126[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', tmp127)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 23173
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 23174
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst5
                                            if len(subjects102) == 0:
                                                break
                                            tmp126.append(subjects102.popleft())
                                        subjects102.extendleft(reversed(tmp126))
                                if pattern_index == 1:
                                    pass
                                    # State 34491
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 34492
                                        if len(subjects102) == 0:
                                            pass
                                            # State 34493
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x**m)**p)**q
                                                yield 5, subst5
                                    if len(subjects102) >= 1:
                                        tmp130 = []
                                        tmp130.append(subjects102.popleft())
                                        while True:
                                            if len(tmp130) > 1:
                                                tmp131 = create_operation_expression(associative1, tmp130)
                                            elif len(tmp130) == 1:
                                                tmp131 = tmp130[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', tmp131)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34492
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 34493
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst5
                                            if len(subjects102) == 0:
                                                break
                                            tmp130.append(subjects102.popleft())
                                        subjects102.extendleft(reversed(tmp130))
                            subjects102.appendleft(tmp122)
                    if len(subjects102) >= 1:
                        tmp133 = subjects102.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1', tmp133)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45524
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45525
                                if len(subjects102) == 0:
                                    pass
                                    # State 45526
                                    if len(subjects) == 0:
                                        pass
                                        # 7: (d*v**p)**q
                                        yield 7, subst4
                            if len(subjects102) >= 1:
                                tmp136 = subjects102.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', tmp136)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45525
                                    if len(subjects102) == 0:
                                        pass
                                        # State 45526
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*v**p)**q
                                            yield 7, subst4
                                subjects102.appendleft(tmp136)
                        subjects102.appendleft(tmp133)
                    if len(subjects102) >= 1 and isinstance(subjects102[0], Add):
                        tmp138 = subjects102.popleft()
                        associative1 = tmp138
                        associative_type1 = type(tmp138)
                        subjects139 = deque(tmp138._args)
                        matcher = CommutativeMatcher23176.get()
                        tmp140 = subjects139
                        subjects139 = []
                        for s in tmp140:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp140, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 23182
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 23183
                                    if len(subjects102) == 0:
                                        pass
                                        # State 23184
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                            yield 0, subst4
                                if len(subjects102) >= 1:
                                    tmp142 = []
                                    tmp142.append(subjects102.popleft())
                                    while True:
                                        if len(tmp142) > 1:
                                            tmp143 = create_operation_expression(associative1, tmp142)
                                        elif len(tmp142) == 1:
                                            tmp143 = tmp142[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp143)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 23183
                                            if len(subjects102) == 0:
                                                pass
                                                # State 23184
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst4
                                        if len(subjects102) == 0:
                                            break
                                        tmp142.append(subjects102.popleft())
                                    subjects102.extendleft(reversed(tmp142))
                            if pattern_index == 1:
                                pass
                                # State 28902
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28903
                                    if len(subjects102) == 0:
                                        pass
                                        # State 28904
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                            yield 3, subst4
                                if len(subjects102) >= 1:
                                    tmp146 = []
                                    tmp146.append(subjects102.popleft())
                                    while True:
                                        if len(tmp146) > 1:
                                            tmp147 = create_operation_expression(associative1, tmp146)
                                        elif len(tmp146) == 1:
                                            tmp147 = tmp146[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp147)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28903
                                            if len(subjects102) == 0:
                                                pass
                                                # State 28904
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                                    yield 3, subst4
                                        if len(subjects102) == 0:
                                            break
                                        tmp146.append(subjects102.popleft())
                                    subjects102.extendleft(reversed(tmp146))
                            if pattern_index == 2:
                                pass
                                # State 34494
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 34495
                                    if len(subjects102) == 0:
                                        pass
                                        # State 34496
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                            yield 5, subst4
                                if len(subjects102) >= 1:
                                    tmp150 = []
                                    tmp150.append(subjects102.popleft())
                                    while True:
                                        if len(tmp150) > 1:
                                            tmp151 = create_operation_expression(associative1, tmp150)
                                        elif len(tmp150) == 1:
                                            tmp151 = tmp150[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp151)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 34495
                                            if len(subjects102) == 0:
                                                pass
                                                # State 34496
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                                    yield 5, subst4
                                        if len(subjects102) == 0:
                                            break
                                        tmp150.append(subjects102.popleft())
                                    subjects102.extendleft(reversed(tmp150))
                            if pattern_index == 3:
                                pass
                                # State 43982
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 43983
                                    if len(subjects102) == 0:
                                        pass
                                        # State 43984
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                            yield 6, subst4
                                if len(subjects102) >= 1:
                                    tmp154 = []
                                    tmp154.append(subjects102.popleft())
                                    while True:
                                        if len(tmp154) > 1:
                                            tmp155 = create_operation_expression(associative1, tmp154)
                                        elif len(tmp154) == 1:
                                            tmp155 = tmp154[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp155)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43983
                                            if len(subjects102) == 0:
                                                pass
                                                # State 43984
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                                    yield 6, subst4
                                        if len(subjects102) == 0:
                                            break
                                        tmp154.append(subjects102.popleft())
                                    subjects102.extendleft(reversed(tmp154))
                        subjects102.appendleft(tmp138)
                    if len(subjects102) >= 1 and isinstance(subjects102[0], Mul):
                        tmp157 = subjects102.popleft()
                        associative1 = tmp157
                        associative_type1 = type(tmp157)
                        subjects158 = deque(tmp157._args)
                        matcher = CommutativeMatcher31311.get()
                        tmp159 = subjects158
                        subjects158 = []
                        for s in tmp159:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp159, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 31335
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 31336
                                    if len(subjects102) == 0:
                                        pass
                                        # State 31337
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                            yield 4, subst4
                                if len(subjects102) >= 1:
                                    tmp161 = []
                                    tmp161.append(subjects102.popleft())
                                    while True:
                                        if len(tmp161) > 1:
                                            tmp162 = create_operation_expression(associative1, tmp161)
                                        elif len(tmp161) == 1:
                                            tmp162 = tmp161[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp162)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 31336
                                            if len(subjects102) == 0:
                                                pass
                                                # State 31337
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                    yield 4, subst4
                                        if len(subjects102) == 0:
                                            break
                                        tmp161.append(subjects102.popleft())
                                    subjects102.extendleft(reversed(tmp161))
                        subjects102.appendleft(tmp157)
                if len(subjects102) >= 1 and isinstance(subjects102[0], Pow):
                    tmp164 = subjects102.popleft()
                    subjects165 = deque(tmp164._args)
                    # State 23185
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 23186
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 23187
                            if len(subjects165) >= 1:
                                tmp168 = subjects165.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0', tmp168)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 23188
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 23189
                                        if len(subjects165) == 0:
                                            pass
                                            # State 23190
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 23191
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 23192
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst6
                                            if len(subjects102) >= 1:
                                                tmp172 = subjects102.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', tmp172)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 23191
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 23192
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                            yield 0, subst6
                                                subjects102.appendleft(tmp172)
                                    if len(subjects165) >= 1:
                                        tmp174 = subjects165.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp174)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 23189
                                            if len(subjects165) == 0:
                                                pass
                                                # State 23190
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 23191
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 23192
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                            yield 0, subst6
                                                if len(subjects102) >= 1:
                                                    tmp177 = subjects102.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp177)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 23191
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 23192
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                                yield 0, subst6
                                                    subjects102.appendleft(tmp177)
                                        subjects165.appendleft(tmp174)
                                subjects165.appendleft(tmp168)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 34497
                            if len(subjects165) >= 1 and isinstance(subjects165[0], Pow):
                                tmp180 = subjects165.popleft()
                                subjects181 = deque(tmp180._args)
                                # State 34498
                                if len(subjects181) >= 1:
                                    tmp182 = subjects181.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2.1.1', tmp182)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 34499
                                        if len(subjects181) >= 1:
                                            tmp184 = subjects181.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2.1.2', tmp184)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34500
                                                if len(subjects181) == 0:
                                                    pass
                                                    # State 34501
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34502
                                                        if len(subjects165) == 0:
                                                            pass
                                                            # State 34503
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 34504
                                                                if len(subjects102) == 0:
                                                                    pass
                                                                    # State 34505
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 5: (d*(e + f*x**m)**p)**q
                                                                        yield 5, subst7
                                                            if len(subjects102) >= 1:
                                                                tmp188 = subjects102.popleft()
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', tmp188)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 34504
                                                                    if len(subjects102) == 0:
                                                                        pass
                                                                        # State 34505
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: (d*(e + f*x**m)**p)**q
                                                                            yield 5, subst7
                                                                subjects102.appendleft(tmp188)
                                                    if len(subjects165) >= 1:
                                                        tmp190 = subjects165.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp190)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 34502
                                                            if len(subjects165) == 0:
                                                                pass
                                                                # State 34503
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 34504
                                                                    if len(subjects102) == 0:
                                                                        pass
                                                                        # State 34505
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: (d*(e + f*x**m)**p)**q
                                                                            yield 5, subst7
                                                                if len(subjects102) >= 1:
                                                                    tmp193 = subjects102.popleft()
                                                                    subst7 = Substitution(subst6)
                                                                    try:
                                                                        subst7.try_add_variable('i2.2.1.2.2', tmp193)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 34504
                                                                        if len(subjects102) == 0:
                                                                            pass
                                                                            # State 34505
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                                yield 5, subst7
                                                                    subjects102.appendleft(tmp193)
                                                        subjects165.appendleft(tmp190)
                                            subjects181.appendleft(tmp184)
                                    subjects181.appendleft(tmp182)
                                subjects165.appendleft(tmp180)
                        if len(subjects165) >= 1 and isinstance(subjects165[0], Mul):
                            tmp195 = subjects165.popleft()
                            associative1 = tmp195
                            associative_type1 = type(tmp195)
                            subjects196 = deque(tmp195._args)
                            matcher = CommutativeMatcher23194.get()
                            tmp197 = subjects196
                            subjects196 = []
                            for s in tmp197:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp197, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 23195
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 23196
                                        if len(subjects165) == 0:
                                            pass
                                            # State 23197
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 23198
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 23199
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst5
                                            if len(subjects102) >= 1:
                                                tmp200 = subjects102.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp200)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 23198
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 23199
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                            yield 0, subst5
                                                subjects102.appendleft(tmp200)
                                    if len(subjects165) >= 1:
                                        tmp202 = []
                                        tmp202.append(subjects165.popleft())
                                        while True:
                                            if len(tmp202) > 1:
                                                tmp203 = create_operation_expression(associative1, tmp202)
                                            elif len(tmp202) == 1:
                                                tmp203 = tmp202[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2.2', tmp203)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 23196
                                                if len(subjects165) == 0:
                                                    pass
                                                    # State 23197
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 23198
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 23199
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                                yield 0, subst5
                                                    if len(subjects102) >= 1:
                                                        tmp206 = subjects102.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', tmp206)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 23198
                                                            if len(subjects102) == 0:
                                                                pass
                                                                # State 23199
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 0: (d*(e + x*f)**p)**q
                                                                    yield 0, subst5
                                                        subjects102.appendleft(tmp206)
                                            if len(subjects165) == 0:
                                                break
                                            tmp202.append(subjects165.popleft())
                                        subjects165.extendleft(reversed(tmp202))
                                if pattern_index == 1:
                                    pass
                                    # State 34510
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 34511
                                        if len(subjects165) == 0:
                                            pass
                                            # State 34512
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34513
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 34514
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst5
                                            if len(subjects102) >= 1:
                                                tmp210 = subjects102.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp210)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 34513
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 34514
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x**m)**p)**q
                                                            yield 5, subst5
                                                subjects102.appendleft(tmp210)
                                    if len(subjects165) >= 1:
                                        tmp212 = []
                                        tmp212.append(subjects165.popleft())
                                        while True:
                                            if len(tmp212) > 1:
                                                tmp213 = create_operation_expression(associative1, tmp212)
                                            elif len(tmp212) == 1:
                                                tmp213 = tmp212[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2.2', tmp213)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34511
                                                if len(subjects165) == 0:
                                                    pass
                                                    # State 34512
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34513
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 34514
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                yield 5, subst5
                                                    if len(subjects102) >= 1:
                                                        tmp216 = subjects102.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', tmp216)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 34513
                                                            if len(subjects102) == 0:
                                                                pass
                                                                # State 34514
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                                    yield 5, subst5
                                                        subjects102.appendleft(tmp216)
                                            if len(subjects165) == 0:
                                                break
                                            tmp212.append(subjects165.popleft())
                                        subjects165.extendleft(reversed(tmp212))
                            subjects165.appendleft(tmp195)
                    if len(subjects165) >= 1:
                        tmp218 = subjects165.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.1', tmp218)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25602
                            if len(subjects165) >= 1:
                                tmp220 = subjects165.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', tmp220)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25603
                                    if len(subjects165) == 0:
                                        pass
                                        # State 25604
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25605
                                            if len(subjects102) == 0:
                                                pass
                                                # State 25606
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*v**p)**q
                                                    yield 1, subst4
                                        if len(subjects102) >= 1:
                                            tmp223 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp223)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 25605
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 25606
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*v**p)**q
                                                        yield 1, subst4
                                            subjects102.appendleft(tmp223)
                                subjects165.appendleft(tmp220)
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45527
                                if len(subjects165) == 0:
                                    pass
                                    # State 45528
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45529
                                        if len(subjects102) == 0:
                                            pass
                                            # State 45530
                                            if len(subjects) == 0:
                                                pass
                                                # 7: (d*v**p)**q
                                                yield 7, subst4
                                    if len(subjects102) >= 1:
                                        tmp227 = subjects102.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp227)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45529
                                            if len(subjects102) == 0:
                                                pass
                                                # State 45530
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (d*v**p)**q
                                                    yield 7, subst4
                                        subjects102.appendleft(tmp227)
                            if len(subjects165) >= 1:
                                tmp229 = subjects165.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', tmp229)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45527
                                    if len(subjects165) == 0:
                                        pass
                                        # State 45528
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45529
                                            if len(subjects102) == 0:
                                                pass
                                                # State 45530
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (d*v**p)**q
                                                    yield 7, subst4
                                        if len(subjects102) >= 1:
                                            tmp232 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp232)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45529
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 45530
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: (d*v**p)**q
                                                        yield 7, subst4
                                            subjects102.appendleft(tmp232)
                                subjects165.appendleft(tmp229)
                        subjects165.appendleft(tmp218)
                    if len(subjects165) >= 1 and isinstance(subjects165[0], Add):
                        tmp234 = subjects165.popleft()
                        associative1 = tmp234
                        associative_type1 = type(tmp234)
                        subjects235 = deque(tmp234._args)
                        matcher = CommutativeMatcher23201.get()
                        tmp236 = subjects235
                        subjects235 = []
                        for s in tmp236:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp236, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 23207
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 23208
                                    if len(subjects165) == 0:
                                        pass
                                        # State 23209
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 23210
                                            if len(subjects102) == 0:
                                                pass
                                                # State 23211
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                                    yield 0, subst4
                                        if len(subjects102) >= 1:
                                            tmp239 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp239)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 23210
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 23211
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                                        yield 0, subst4
                                            subjects102.appendleft(tmp239)
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
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp242)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 23208
                                            if len(subjects165) == 0:
                                                pass
                                                # State 23209
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 23210
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 23211
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                            yield 0, subst4
                                                if len(subjects102) >= 1:
                                                    tmp245 = subjects102.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp245)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 23210
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 23211
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                                yield 0, subst4
                                                    subjects102.appendleft(tmp245)
                                        if len(subjects165) == 0:
                                            break
                                        tmp241.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp241))
                            if pattern_index == 1:
                                pass
                                # State 28915
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28916
                                    if len(subjects165) == 0:
                                        pass
                                        # State 28917
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28918
                                            if len(subjects102) == 0:
                                                pass
                                                # State 28919
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                                    yield 3, subst4
                                        if len(subjects102) >= 1:
                                            tmp249 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp249)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 28918
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 28919
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x**m)**p)**q
                                                        yield 3, subst4
                                            subjects102.appendleft(tmp249)
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
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp252)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28916
                                            if len(subjects165) == 0:
                                                pass
                                                # State 28917
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28918
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 28919
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: (d*(e + f*x**m)**p)**q
                                                            yield 3, subst4
                                                if len(subjects102) >= 1:
                                                    tmp255 = subjects102.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp255)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 28918
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 28919
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: (d*(e + f*x**m)**p)**q
                                                                yield 3, subst4
                                                    subjects102.appendleft(tmp255)
                                        if len(subjects165) == 0:
                                            break
                                        tmp251.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp251))
                            if pattern_index == 2:
                                pass
                                # State 34515
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 34516
                                    if len(subjects165) == 0:
                                        pass
                                        # State 34517
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 34518
                                            if len(subjects102) == 0:
                                                pass
                                                # State 34519
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                                    yield 5, subst4
                                        if len(subjects102) >= 1:
                                            tmp259 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp259)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 34518
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 34519
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                                        yield 5, subst4
                                            subjects102.appendleft(tmp259)
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
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp262)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 34516
                                            if len(subjects165) == 0:
                                                pass
                                                # State 34517
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 34518
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 34519
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x**m)**p)**q
                                                            yield 5, subst4
                                                if len(subjects102) >= 1:
                                                    tmp265 = subjects102.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp265)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 34518
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 34519
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                yield 5, subst4
                                                    subjects102.appendleft(tmp265)
                                        if len(subjects165) == 0:
                                            break
                                        tmp261.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp261))
                            if pattern_index == 3:
                                pass
                                # State 43992
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 43993
                                    if len(subjects165) == 0:
                                        pass
                                        # State 43994
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43995
                                            if len(subjects102) == 0:
                                                pass
                                                # State 43996
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                                    yield 6, subst4
                                        if len(subjects102) >= 1:
                                            tmp269 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp269)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 43995
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 43996
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(e + f*x + g*x**2)**p)**q
                                                        yield 6, subst4
                                            subjects102.appendleft(tmp269)
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
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp272)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 43993
                                            if len(subjects165) == 0:
                                                pass
                                                # State 43994
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 43995
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 43996
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                                            yield 6, subst4
                                                if len(subjects102) >= 1:
                                                    tmp275 = subjects102.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp275)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 43995
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 43996
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: (d*(e + f*x + g*x**2)**p)**q
                                                                yield 6, subst4
                                                    subjects102.appendleft(tmp275)
                                        if len(subjects165) == 0:
                                            break
                                        tmp271.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp271))
                        subjects165.appendleft(tmp234)
                    if len(subjects165) >= 1 and isinstance(subjects165[0], Mul):
                        tmp277 = subjects165.popleft()
                        associative1 = tmp277
                        associative_type1 = type(tmp277)
                        subjects278 = deque(tmp277._args)
                        matcher = CommutativeMatcher31339.get()
                        tmp279 = subjects278
                        subjects278 = []
                        for s in tmp279:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp279, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 31363
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 31364
                                    if len(subjects165) == 0:
                                        pass
                                        # State 31365
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 31366
                                            if len(subjects102) == 0:
                                                pass
                                                # State 31367
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                    yield 4, subst4
                                        if len(subjects102) >= 1:
                                            tmp282 = subjects102.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp282)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 31366
                                                if len(subjects102) == 0:
                                                    pass
                                                    # State 31367
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                        yield 4, subst4
                                            subjects102.appendleft(tmp282)
                                if len(subjects165) >= 1:
                                    tmp284 = []
                                    tmp284.append(subjects165.popleft())
                                    while True:
                                        if len(tmp284) > 1:
                                            tmp285 = create_operation_expression(associative1, tmp284)
                                        elif len(tmp284) == 1:
                                            tmp285 = tmp284[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp285)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 31364
                                            if len(subjects165) == 0:
                                                pass
                                                # State 31365
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 31366
                                                    if len(subjects102) == 0:
                                                        pass
                                                        # State 31367
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                            yield 4, subst4
                                                if len(subjects102) >= 1:
                                                    tmp288 = subjects102.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp288)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 31366
                                                        if len(subjects102) == 0:
                                                            pass
                                                            # State 31367
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                                yield 4, subst4
                                                    subjects102.appendleft(tmp288)
                                        if len(subjects165) == 0:
                                            break
                                        tmp284.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp284))
                        subjects165.appendleft(tmp277)
                    subjects102.appendleft(tmp164)
            if len(subjects102) >= 1:
                tmp290 = subjects102.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1', tmp290)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53245
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53246
                        if len(subjects102) == 0:
                            pass
                            # State 53247
                            if len(subjects) == 0:
                                pass
                                # 8: RFx**p
                                yield 8, subst2
                    if len(subjects102) >= 1:
                        tmp293 = subjects102.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', tmp293)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53246
                            if len(subjects102) == 0:
                                pass
                                # State 53247
                                if len(subjects) == 0:
                                    pass
                                    # 8: RFx**p
                                    yield 8, subst2
                        subjects102.appendleft(tmp293)
                subjects102.appendleft(tmp290)
            if len(subjects102) >= 1 and isinstance(subjects102[0], Mul):
                tmp295 = subjects102.popleft()
                associative1 = tmp295
                associative_type1 = type(tmp295)
                subjects296 = deque(tmp295._args)
                matcher = CommutativeMatcher23213.get()
                tmp297 = subjects296
                subjects296 = []
                for s in tmp297:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp297, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 23250
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 23251
                            if len(subjects102) == 0:
                                pass
                                # State 23252
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q
                                    yield 0, subst2
                        if len(subjects102) >= 1:
                            tmp299 = []
                            tmp299.append(subjects102.popleft())
                            while True:
                                if len(tmp299) > 1:
                                    tmp300 = create_operation_expression(associative1, tmp299)
                                elif len(tmp299) == 1:
                                    tmp300 = tmp299[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp300)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 23251
                                    if len(subjects102) == 0:
                                        pass
                                        # State 23252
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                            yield 0, subst2
                                if len(subjects102) == 0:
                                    break
                                tmp299.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp299))
                    if pattern_index == 1:
                        pass
                        # State 25610
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25611
                            if len(subjects102) == 0:
                                pass
                                # State 25612
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d*v**p)**q
                                    yield 1, subst2
                        if len(subjects102) >= 1:
                            tmp303 = []
                            tmp303.append(subjects102.popleft())
                            while True:
                                if len(tmp303) > 1:
                                    tmp304 = create_operation_expression(associative1, tmp303)
                                elif len(tmp303) == 1:
                                    tmp304 = tmp303[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp304)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25611
                                    if len(subjects102) == 0:
                                        pass
                                        # State 25612
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q
                                            yield 1, subst2
                                if len(subjects102) == 0:
                                    break
                                tmp303.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp303))
                    if pattern_index == 2:
                        pass
                        # State 28944
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 28945
                            if len(subjects102) == 0:
                                pass
                                # State 28946
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x**m)**p)**q
                                    yield 3, subst2
                        if len(subjects102) >= 1:
                            tmp307 = []
                            tmp307.append(subjects102.popleft())
                            while True:
                                if len(tmp307) > 1:
                                    tmp308 = create_operation_expression(associative1, tmp307)
                                elif len(tmp307) == 1:
                                    tmp308 = tmp307[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp308)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28945
                                    if len(subjects102) == 0:
                                        pass
                                        # State 28946
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                            yield 3, subst2
                                if len(subjects102) == 0:
                                    break
                                tmp307.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp307))
                    if pattern_index == 3:
                        pass
                        # State 31422
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 31423
                            if len(subjects102) == 0:
                                pass
                                # State 31424
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                    yield 4, subst2
                        if len(subjects102) >= 1:
                            tmp311 = []
                            tmp311.append(subjects102.popleft())
                            while True:
                                if len(tmp311) > 1:
                                    tmp312 = create_operation_expression(associative1, tmp311)
                                elif len(tmp311) == 1:
                                    tmp312 = tmp311[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp312)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 31423
                                    if len(subjects102) == 0:
                                        pass
                                        # State 31424
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                            yield 4, subst2
                                if len(subjects102) == 0:
                                    break
                                tmp311.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp311))
                    if pattern_index == 4:
                        pass
                        # State 34548
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 34549
                            if len(subjects102) == 0:
                                pass
                                # State 34550
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x**m)**p)**q
                                    yield 5, subst2
                        if len(subjects102) >= 1:
                            tmp315 = []
                            tmp315.append(subjects102.popleft())
                            while True:
                                if len(tmp315) > 1:
                                    tmp316 = create_operation_expression(associative1, tmp315)
                                elif len(tmp315) == 1:
                                    tmp316 = tmp315[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp316)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 34549
                                    if len(subjects102) == 0:
                                        pass
                                        # State 34550
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                            yield 5, subst2
                                if len(subjects102) == 0:
                                    break
                                tmp315.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp315))
                    if pattern_index == 5:
                        pass
                        # State 44015
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 44016
                            if len(subjects102) == 0:
                                pass
                                # State 44017
                                if len(subjects) == 0:
                                    pass
                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                    yield 6, subst2
                        if len(subjects102) >= 1:
                            tmp319 = []
                            tmp319.append(subjects102.popleft())
                            while True:
                                if len(tmp319) > 1:
                                    tmp320 = create_operation_expression(associative1, tmp319)
                                elif len(tmp319) == 1:
                                    tmp320 = tmp319[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp320)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44016
                                    if len(subjects102) == 0:
                                        pass
                                        # State 44017
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                            yield 6, subst2
                                if len(subjects102) == 0:
                                    break
                                tmp319.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp319))
                    if pattern_index == 6:
                        pass
                        # State 45534
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45535
                            if len(subjects102) == 0:
                                pass
                                # State 45536
                                if len(subjects) == 0:
                                    pass
                                    # 7: (d*v**p)**q
                                    yield 7, subst2
                        if len(subjects102) >= 1:
                            tmp323 = []
                            tmp323.append(subjects102.popleft())
                            while True:
                                if len(tmp323) > 1:
                                    tmp324 = create_operation_expression(associative1, tmp323)
                                elif len(tmp323) == 1:
                                    tmp324 = tmp323[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp324)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45535
                                    if len(subjects102) == 0:
                                        pass
                                        # State 45536
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*v**p)**q
                                            yield 7, subst2
                                if len(subjects102) == 0:
                                    break
                                tmp323.append(subjects102.popleft())
                            subjects102.extendleft(reversed(tmp323))
                subjects102.appendleft(tmp295)
            subjects.appendleft(tmp101)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp326 = subjects.popleft()
            associative1 = tmp326
            associative_type1 = type(tmp326)
            subjects327 = deque(tmp326._args)
            matcher = CommutativeMatcher26090.get()
            tmp328 = subjects327
            subjects327 = []
            for s in tmp328:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp328, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 26096
                    if len(subjects) == 0:
                        pass
                        # 2: e + x*f
                        yield 2, subst1
            subjects.appendleft(tmp326)
        return
        yield


from .generated_part001911 import *
from .generated_part001929 import *
from .generated_part001930 import *
from .generated_part001905 import *
from .generated_part001955 import *
from .generated_part001939 import *
from collections import deque
from matchpy.utils import VariableWithCount
from .generated_part001933 import *
from .generated_part001942 import *
from .generated_part001931 import *
from .generated_part001907 import *
from .generated_part001916 import *
from multiset import Multiset
from .generated_part001936 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part001910 import *
from .generated_part001913 import *
from .generated_part001937 import *
from .generated_part001904 import *