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


class CommutativeMatcher16909(CommutativeMatcher):
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
    5: (5, Multiset({4: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({5: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({6: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({7: 1}), [
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
        if CommutativeMatcher16909._instance is None:
            CommutativeMatcher16909._instance = CommutativeMatcher16909()
        return CommutativeMatcher16909._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 16908
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 46152
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 46153
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp4 = subjects2.popleft()
                    subjects5 = deque(tmp4._args)
                    # State 46154
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 46155
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 46156
                            if len(subjects5) >= 1:
                                tmp8 = subjects5.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2.1', tmp8)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46157
                                    if len(subjects5) >= 1:
                                        tmp10 = subjects5.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.3.2.2', tmp10)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 46158
                                            if len(subjects5) == 0:
                                                pass
                                                # State 46159
                                                if len(subjects2) >= 1:
                                                    tmp12 = subjects2.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.3.2', tmp12)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 46160
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 46161
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (b*(c*x**n)**p)**q
                                                                yield 0, subst6
                                                    subjects2.appendleft(tmp12)
                                        subjects5.appendleft(tmp10)
                                subjects5.appendleft(tmp8)
                        if len(subjects5) >= 1 and isinstance(subjects5[0], Pow):
                            tmp14 = subjects5.popleft()
                            subjects15 = deque(tmp14._args)
                            # State 46162
                            if len(subjects15) >= 1:
                                tmp16 = subjects15.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.3.2.2.1', tmp16)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46163
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 46164
                                        if len(subjects15) == 0:
                                            pass
                                            # State 46165
                                            if len(subjects5) >= 1:
                                                tmp19 = subjects5.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.3.2.2', tmp19)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 46166
                                                    if len(subjects5) == 0:
                                                        pass
                                                        # State 46167
                                                        if len(subjects2) >= 1:
                                                            tmp21 = subjects2.popleft()
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.3.2', tmp21)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 46168
                                                                if len(subjects2) == 0:
                                                                    pass
                                                                    # State 46169
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 0: (b*(c*x**n)**p)**q
                                                                        yield 0, subst6
                                                            subjects2.appendleft(tmp21)
                                                subjects5.appendleft(tmp19)
                                    if len(subjects15) >= 1:
                                        tmp23 = subjects15.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.2.2.2', tmp23)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 46164
                                            if len(subjects15) == 0:
                                                pass
                                                # State 46165
                                                if len(subjects5) >= 1:
                                                    tmp25 = subjects5.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.3.2.2', tmp25)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 46166
                                                        if len(subjects5) == 0:
                                                            pass
                                                            # State 46167
                                                            if len(subjects2) >= 1:
                                                                tmp27 = subjects2.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.3.2', tmp27)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 46168
                                                                    if len(subjects2) == 0:
                                                                        pass
                                                                        # State 46169
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 0: (b*(c*x**n)**p)**q
                                                                            yield 0, subst6
                                                                subjects2.appendleft(tmp27)
                                                    subjects5.appendleft(tmp25)
                                        subjects15.appendleft(tmp23)
                                subjects15.appendleft(tmp16)
                            subjects5.appendleft(tmp14)
                    if len(subjects5) >= 1 and isinstance(subjects5[0], Mul):
                        tmp29 = subjects5.popleft()
                        associative1 = tmp29
                        associative_type1 = type(tmp29)
                        subjects30 = deque(tmp29._args)
                        matcher = CommutativeMatcher46171.get()
                        tmp31 = subjects30
                        subjects30 = []
                        for s in tmp31:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp31, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 46178
                                if len(subjects5) >= 1:
                                    tmp32 = []
                                    tmp32.append(subjects5.popleft())
                                    while True:
                                        if len(tmp32) > 1:
                                            tmp33 = create_operation_expression(associative1, tmp32)
                                        elif len(tmp32) == 1:
                                            tmp33 = tmp32[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.3.2.2', tmp33)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 46179
                                            if len(subjects5) == 0:
                                                pass
                                                # State 46180
                                                if len(subjects2) >= 1:
                                                    tmp35 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.3.2', tmp35)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 46181
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 46182
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (b*(c*x**n)**p)**q
                                                                yield 0, subst4
                                                    subjects2.appendleft(tmp35)
                                        if len(subjects5) == 0:
                                            break
                                        tmp32.append(subjects5.popleft())
                                    subjects5.extendleft(reversed(tmp32))
                        subjects5.appendleft(tmp29)
                    subjects2.appendleft(tmp4)
            if len(subjects2) >= 1:
                tmp37 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1', tmp37)
                except ValueError:
                    pass
                else:
                    pass
                    # State 48183
                    if len(subjects2) >= 1:
                        tmp39 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', tmp39)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48184
                            if len(subjects2) == 0:
                                pass
                                # State 48185
                                if len(subjects) == 0:
                                    pass
                                    # 3: u**n
                                    yield 3, subst2
                        subjects2.appendleft(tmp39)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 56625
                        if len(subjects2) == 0:
                            pass
                            # State 56626
                            if len(subjects) == 0:
                                pass
                                # 7: x**m
                                yield 7, subst2
                    if len(subjects2) >= 1:
                        tmp42 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', tmp42)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 56625
                            if len(subjects2) == 0:
                                pass
                                # State 56626
                                if len(subjects) == 0:
                                    pass
                                    # 7: x**m
                                    yield 7, subst2
                        subjects2.appendleft(tmp42)
                subjects2.appendleft(tmp37)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp44 = subjects2.popleft()
                associative1 = tmp44
                associative_type1 = type(tmp44)
                subjects45 = deque(tmp44._args)
                matcher = CommutativeMatcher46184.get()
                tmp46 = subjects45
                subjects45 = []
                for s in tmp46:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp46, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46208
                        if len(subjects2) >= 1:
                            tmp47 = []
                            tmp47.append(subjects2.popleft())
                            while True:
                                if len(tmp47) > 1:
                                    tmp48 = create_operation_expression(associative1, tmp47)
                                elif len(tmp47) == 1:
                                    tmp48 = tmp47[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp48)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46209
                                    if len(subjects2) == 0:
                                        pass
                                        # State 46210
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (b*(c*x**n)**p)**q
                                            yield 0, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp47.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp47))
                    if pattern_index == 1:
                        pass
                        # State 46858
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 46859
                            if len(subjects2) == 0:
                                pass
                                # State 46860
                                if len(subjects) == 0:
                                    pass
                                    # 1: (e1*(a + b*x)/(a + x*b))**n
                                    yield 1, subst2
                        if len(subjects2) >= 1:
                            tmp51 = []
                            tmp51.append(subjects2.popleft())
                            while True:
                                if len(tmp51) > 1:
                                    tmp52 = create_operation_expression(associative1, tmp51)
                                elif len(tmp51) == 1:
                                    tmp52 = tmp51[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp52)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46859
                                    if len(subjects2) == 0:
                                        pass
                                        # State 46860
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (e1*(a + b*x)/(a + x*b))**n
                                            yield 1, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp51.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp51))
                    if pattern_index == 2:
                        pass
                        # State 47676
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47677
                            if len(subjects2) == 0:
                                pass
                                # State 47678
                                if len(subjects) == 0:
                                    pass
                                    # 2: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                                    yield 2, subst2
                        if len(subjects2) >= 1:
                            tmp55 = []
                            tmp55.append(subjects2.popleft())
                            while True:
                                if len(tmp55) > 1:
                                    tmp56 = create_operation_expression(associative1, tmp55)
                                elif len(tmp55) == 1:
                                    tmp56 = tmp55[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp56)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47677
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47678
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                                            yield 2, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp55.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp55))
                    if pattern_index == 3:
                        pass
                        # State 48302
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48303
                            if len(subjects2) == 0:
                                pass
                                # State 48304
                                if len(subjects) == 0:
                                    pass
                                    # 4: (e1*(e + x*f)**n2*(x*b + a)**n1)**n
                                    yield 4, subst2
                        if len(subjects2) >= 1:
                            tmp59 = []
                            tmp59.append(subjects2.popleft())
                            while True:
                                if len(tmp59) > 1:
                                    tmp60 = create_operation_expression(associative1, tmp59)
                                elif len(tmp59) == 1:
                                    tmp60 = tmp59[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp60)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48303
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48304
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (e1*(e + x*f)**n2*(x*b + a)**n1)**n
                                            yield 4, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp59.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp59))
                    if pattern_index == 4:
                        pass
                        # State 48548
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48549
                            if len(subjects2) == 0:
                                pass
                                # State 48550
                                if len(subjects) == 0:
                                    pass
                                    # 5: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                                    yield 5, subst2
                        if len(subjects2) >= 1:
                            tmp63 = []
                            tmp63.append(subjects2.popleft())
                            while True:
                                if len(tmp63) > 1:
                                    tmp64 = create_operation_expression(associative1, tmp63)
                                elif len(tmp63) == 1:
                                    tmp64 = tmp63[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2', tmp64)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48549
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48550
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                                            yield 5, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp63.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp63))
                    if pattern_index == 5:
                        pass
                        # State 48994
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48995
                            if len(subjects2) == 0:
                                pass
                                # State 48996
                                if len(subjects) == 0:
                                    pass
                                    # 6: (e1*(c + x*d)**n2*(c + x*d)**n1)**n
                                    yield 6, subst2
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
                                    subst2.try_add_variable('i2.3.2', tmp68)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48995
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48996
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (e1*(c + x*d)**n2*(c + x*d)**n1)**n
                                            yield 6, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp67.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp67))
                subjects2.appendleft(tmp44)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 46785
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp71 = subjects.popleft()
                associative1 = tmp71
                associative_type1 = type(tmp71)
                subjects72 = deque(tmp71._args)
                matcher = CommutativeMatcher46787.get()
                tmp73 = subjects72
                subjects72 = []
                for s in tmp73:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp73, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46823
                        if len(subjects) == 0:
                            pass
                            # 1: (e1*(a + b*x)/(a + x*b))**n
                            yield 1, subst2
                    if pattern_index == 1:
                        pass
                        # State 47632
                        if len(subjects) == 0:
                            pass
                            # 2: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                            yield 2, subst2
                    if pattern_index == 2:
                        pass
                        # State 48285
                        if len(subjects) == 0:
                            pass
                            # 4: (e1*(e + x*f)**n2*(x*b + a)**n1)**n
                            yield 4, subst2
                    if pattern_index == 3:
                        pass
                        # State 48520
                        if len(subjects) == 0:
                            pass
                            # 5: (e1*(x*d + c)**n2*(x*b + a)**n1)**n
                            yield 5, subst2
                    if pattern_index == 4:
                        pass
                        # State 48967
                        if len(subjects) == 0:
                            pass
                            # 6: (e1*(c + x*d)**n2*(c + x*d)**n1)**n
                            yield 6, subst2
                subjects.appendleft(tmp71)
            if len(subjects) >= 1:
                tmp74 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1', tmp74)
                except ValueError:
                    pass
                else:
                    pass
                    # State 56624
                    if len(subjects) == 0:
                        pass
                        # 7: x**m
                        yield 7, subst2
                subjects.appendleft(tmp74)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part004154 import *
from collections import deque
from .generated_part004141 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part004140 import *