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

class CommutativeMatcher10401(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({4: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({5: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({6: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.0_1', 1, 1, None), Mul)
]),
    6: (6, Multiset({7: 1, 8: 1}), [
      
]),
    7: (7, Multiset({9: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({10: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({11: 1, 12: 1, 13: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({11: 1, 12: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({14: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher10401._instance is None:
            CommutativeMatcher10401._instance = CommutativeMatcher10401()
        return CommutativeMatcher10401._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 10400
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 10402
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp3 = subjects2.popleft()
                associative1 = tmp3
                associative_type1 = type(tmp3)
                subjects4 = deque(tmp3._args)
                matcher = CommutativeMatcher10404.get()
                tmp5 = subjects4
                subjects4 = []
                for s in tmp5:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp5, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10421
                        if len(subjects2) >= 1 and subjects2[0] == -1:
                            tmp6 = subjects2.popleft()
                            # State 10422
                            if len(subjects2) == 0:
                                pass
                                # State 10423
                                if len(subjects) == 0:
                                    pass
                                    # 0: 1/(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f27)
                                    # 2: 1/(a + b*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f803) and (cons_f804)
                            subjects2.appendleft(tmp6)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp7 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 18513
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18514
                            if len(subjects2) == 0:
                                pass
                                # State 18515
                                if len(subjects) == 0:
                                    pass
                                    # 4: x**n /; (cons_f1101)
                        subjects2.appendleft(tmp9)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 102273
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 102274
                            if len(subjects2) >= 1:
                                tmp13 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.3.1.0', tmp13)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102275
                                    if len(subjects2) == 0:
                                        pass
                                        # State 102276
                                        if len(subjects) == 0:
                                            pass
                                            # 5: F**(e + x*f) /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1666)
                                subjects2.appendleft(tmp13)
                        if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                            tmp15 = subjects2.popleft()
                            associative1 = tmp15
                            associative_type1 = type(tmp15)
                            subjects16 = deque(tmp15._args)
                            matcher = CommutativeMatcher102278.get()
                            tmp17 = subjects16
                            subjects16 = []
                            for s in tmp17:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp17, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 102279
                                    if len(subjects2) == 0:
                                        pass
                                        # State 102280
                                        if len(subjects) == 0:
                                            pass
                                            # 5: F**(e + x*f) /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1666)
                            subjects2.appendleft(tmp15)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 103393
                        if len(subjects2) == 0:
                            pass
                            # State 103394
                            if len(subjects) == 0:
                                pass
                                # 11: v**m /; (cons_f19) and (cons_f10)
                                # 14: v**m /; (cons_f19) and (cons_f10) and (cons_f2029) and (cons_f2030)
                                # 7: v**m /; (cons_f19) and (cons_f1683)
                    if len(subjects2) >= 1:
                        tmp19 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2', tmp19)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 103393
                            if len(subjects2) == 0:
                                pass
                                # State 103394
                                if len(subjects) == 0:
                                    pass
                                    # 11: v**m /; (cons_f19) and (cons_f10)
                                    # 14: v**m /; (cons_f19) and (cons_f10) and (cons_f2029) and (cons_f2030)
                                    # 7: v**m /; (cons_f19) and (cons_f1683)
                        subjects2.appendleft(tmp19)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                        tmp21 = subjects2.popleft()
                        associative1 = tmp21
                        associative_type1 = type(tmp21)
                        subjects22 = deque(tmp21._args)
                        matcher = CommutativeMatcher102282.get()
                        tmp23 = subjects22
                        subjects22 = []
                        for s in tmp23:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp23, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 102288
                                if len(subjects2) == 0:
                                    pass
                                    # State 102289
                                    if len(subjects) == 0:
                                        pass
                                        # 5: F**(e + x*f) /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1666)
                        subjects2.appendleft(tmp21)
                subjects2.appendleft(tmp7)
            if len(subjects2) >= 1:
                tmp24 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1_1', tmp24)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103397
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 103398
                        if len(subjects2) == 0:
                            pass
                            # State 103399
                            if len(subjects) == 0:
                                pass
                                # 8: w**n /; (cons_f4) and (cons_f1683)
                                # 12: w**n /; (cons_f4) and (cons_f2027)
                    if len(subjects2) >= 1:
                        tmp27 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2_1', tmp27)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 103398
                            if len(subjects2) == 0:
                                pass
                                # State 103399
                                if len(subjects) == 0:
                                    pass
                                    # 8: w**n /; (cons_f4) and (cons_f1683)
                                    # 12: w**n /; (cons_f4) and (cons_f2027)
                        subjects2.appendleft(tmp27)
                subjects2.appendleft(tmp24)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 150669
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp30 = subjects2.popleft()
                    subjects31 = deque(tmp30._args)
                    # State 150670
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 150671
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 150672
                            if len(subjects31) >= 1:
                                tmp34 = subjects31.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.2.1.0', tmp34)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150673
                                    if len(subjects31) >= 1:
                                        tmp36 = subjects31.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.2.2', tmp36)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 150674
                                            if len(subjects31) == 0:
                                                pass
                                                # State 150675
                                                if len(subjects2) >= 1:
                                                    tmp38 = subjects2.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.2', tmp38)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 150676
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 150677
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 10: (d*(a + x*b)**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f149)
                                                    subjects2.appendleft(tmp38)
                                        subjects31.appendleft(tmp36)
                                subjects31.appendleft(tmp34)
                        if len(subjects31) >= 1 and isinstance(subjects31[0], Mul):
                            tmp40 = subjects31.popleft()
                            associative1 = tmp40
                            associative_type1 = type(tmp40)
                            subjects41 = deque(tmp40._args)
                            matcher = CommutativeMatcher150679.get()
                            tmp42 = subjects41
                            subjects41 = []
                            for s in tmp42:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp42, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 150680
                                    if len(subjects31) >= 1:
                                        tmp43 = []
                                        tmp43.append(subjects31.popleft())
                                        while True:
                                            if len(tmp43) > 1:
                                                tmp44 = create_operation_expression(associative1, tmp43)
                                            elif len(tmp43) == 1:
                                                tmp44 = tmp43[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.2.2', tmp44)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 150681
                                                if len(subjects31) == 0:
                                                    pass
                                                    # State 150682
                                                    if len(subjects2) >= 1:
                                                        tmp46 = subjects2.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.2', tmp46)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 150683
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 150684
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 10: (d*(a + x*b)**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f149)
                                                        subjects2.appendleft(tmp46)
                                            if len(subjects31) == 0:
                                                break
                                            tmp43.append(subjects31.popleft())
                                        subjects31.extendleft(reversed(tmp43))
                            subjects31.appendleft(tmp40)
                    if len(subjects31) >= 1 and isinstance(subjects31[0], Add):
                        tmp48 = subjects31.popleft()
                        associative1 = tmp48
                        associative_type1 = type(tmp48)
                        subjects49 = deque(tmp48._args)
                        matcher = CommutativeMatcher150686.get()
                        tmp50 = subjects49
                        subjects49 = []
                        for s in tmp50:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp50, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 150692
                                if len(subjects31) >= 1:
                                    tmp51 = []
                                    tmp51.append(subjects31.popleft())
                                    while True:
                                        if len(tmp51) > 1:
                                            tmp52 = create_operation_expression(associative1, tmp51)
                                        elif len(tmp51) == 1:
                                            tmp52 = tmp51[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.2.2', tmp52)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 150693
                                            if len(subjects31) == 0:
                                                pass
                                                # State 150694
                                                if len(subjects2) >= 1:
                                                    tmp54 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.2', tmp54)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 150695
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 150696
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 10: (d*(a + x*b)**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f149)
                                                    subjects2.appendleft(tmp54)
                                        if len(subjects31) == 0:
                                            break
                                        tmp51.append(subjects31.popleft())
                                    subjects31.extendleft(reversed(tmp51))
                        subjects31.appendleft(tmp48)
                    subjects2.appendleft(tmp30)
            if len(subjects2) >= 1:
                tmp56 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1_2', tmp56)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151898
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2_2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151899
                        if len(subjects2) == 0:
                            pass
                            # State 151900
                            if len(subjects) == 0:
                                pass
                                # 13: z**q /; (cons_f52) and (cons_f2028)
                    if len(subjects2) >= 1:
                        tmp59 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2_2', tmp59)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151899
                            if len(subjects2) == 0:
                                pass
                                # State 151900
                                if len(subjects) == 0:
                                    pass
                                    # 13: z**q /; (cons_f52) and (cons_f2028)
                        subjects2.appendleft(tmp59)
                subjects2.appendleft(tmp56)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp61 = subjects2.popleft()
                associative1 = tmp61
                associative_type1 = type(tmp61)
                subjects62 = deque(tmp61._args)
                matcher = CommutativeMatcher102413.get()
                tmp63 = subjects62
                subjects62 = []
                for s in tmp63:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp63, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 102428
                        if len(subjects2) >= 1:
                            tmp64 = []
                            tmp64.append(subjects2.popleft())
                            while True:
                                if len(tmp64) > 1:
                                    tmp65 = create_operation_expression(associative1, tmp64)
                                elif len(tmp64) == 1:
                                    tmp65 = tmp64[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp65)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102429
                                    if len(subjects2) == 0:
                                        pass
                                        # State 102430
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (F*b*(c + x*d))**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1666) and (cons_f149)
                                if len(subjects2) == 0:
                                    break
                                tmp64.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp64))
                    if pattern_index == 1:
                        pass
                        # State 150579
                        if len(subjects2) >= 1:
                            tmp67 = []
                            tmp67.append(subjects2.popleft())
                            while True:
                                if len(tmp67) > 1:
                                    tmp68 = create_operation_expression(associative1, tmp67)
                                elif len(tmp67) == 1:
                                    tmp68 = tmp67[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp68)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150580
                                    if len(subjects2) == 0:
                                        pass
                                        # State 150581
                                        if len(subjects) == 0:
                                            pass
                                            # 9: (d*(a + x*b))**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f149)
                                if len(subjects2) == 0:
                                    break
                                tmp67.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp67))
                    if pattern_index == 2:
                        pass
                        # State 150718
                        if len(subjects2) >= 1:
                            tmp70 = []
                            tmp70.append(subjects2.popleft())
                            while True:
                                if len(tmp70) > 1:
                                    tmp71 = create_operation_expression(associative1, tmp70)
                                elif len(tmp70) == 1:
                                    tmp71 = tmp70[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp71)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 150719
                                    if len(subjects2) == 0:
                                        pass
                                        # State 150720
                                        if len(subjects) == 0:
                                            pass
                                            # 10: (d*(a + x*b)**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f149)
                                if len(subjects2) == 0:
                                    break
                                tmp70.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp70))
                subjects2.appendleft(tmp61)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 10424
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10425
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.2.1.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 10426
                    if len(subjects) >= 1:
                        tmp76 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.2.1.1', tmp76)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10427
                            if len(subjects) == 0:
                                pass
                                # 1: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f27)
                                # 3: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f803) and (cons_f804)
                        subjects.appendleft(tmp76)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp78 = subjects.popleft()
                    subjects79 = deque(tmp78._args)
                    # State 10428
                    if len(subjects79) >= 1:
                        tmp80 = subjects79.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.1', tmp80)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10429
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 10430
                                if len(subjects79) == 0:
                                    pass
                                    # State 10431
                                    if len(subjects) == 0:
                                        pass
                                        # 1: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f27)
                                        # 3: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f803) and (cons_f804)
                            if len(subjects79) >= 1:
                                tmp83 = subjects79.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.1.2', tmp83)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10430
                                    if len(subjects79) == 0:
                                        pass
                                        # State 10431
                                        if len(subjects) == 0:
                                            pass
                                            # 1: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f27)
                                            # 3: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f803) and (cons_f804)
                                subjects79.appendleft(tmp83)
                        subjects79.appendleft(tmp80)
                    subjects.appendleft(tmp78)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp85 = subjects.popleft()
                associative1 = tmp85
                associative_type1 = type(tmp85)
                subjects86 = deque(tmp85._args)
                matcher = CommutativeMatcher10433.get()
                tmp87 = subjects86
                subjects86 = []
                for s in tmp87:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp87, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10440
                        if len(subjects) == 0:
                            pass
                            # 1: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f27)
                            # 3: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f803) and (cons_f804)
                subjects.appendleft(tmp85)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 103391
            if len(subjects) >= 1:
                tmp89 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1', tmp89)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103392
                    if len(subjects) == 0:
                        pass
                        # 11: v**m /; (cons_f19) and (cons_f10)
                        # 14: v**m /; (cons_f19) and (cons_f10) and (cons_f2029) and (cons_f2030)
                        # 7: v**m /; (cons_f19) and (cons_f1683)
                subjects.appendleft(tmp89)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 103395
            if len(subjects) >= 1:
                tmp92 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1_1', tmp92)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103396
                    if len(subjects) == 0:
                        pass
                        # 8: w**n /; (cons_f4) and (cons_f1683)
                        # 12: w**n /; (cons_f4) and (cons_f2027)
                subjects.appendleft(tmp92)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 151896
            if len(subjects) >= 1:
                tmp95 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1_2', tmp95)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151897
                    if len(subjects) == 0:
                        pass
                        # 13: z**q /; (cons_f52) and (cons_f2028)
                subjects.appendleft(tmp95)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp97 = subjects.popleft()
            associative1 = tmp97
            associative_type1 = type(tmp97)
            subjects98 = deque(tmp97._args)
            matcher = CommutativeMatcher10442.get()
            tmp99 = subjects98
            subjects98 = []
            for s in tmp99:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp99, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 10459
                    if len(subjects) == 0:
                        pass
                        # 1: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f27)
                        # 3: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f803) and (cons_f804)
            subjects.appendleft(tmp97)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
