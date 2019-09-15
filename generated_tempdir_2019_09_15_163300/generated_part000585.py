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


class CommutativeMatcher2333(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({11: 1, 12: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher2333._instance is None:
            CommutativeMatcher2333._instance = CommutativeMatcher2333()
        return CommutativeMatcher2333._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2332
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 2334
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2335
                    if len(subjects) == 0:
                        pass
                        # 0: x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 151976
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1_1', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151977
                    if len(subjects) == 0:
                        pass
                        # 11: w**n2 /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f5) and (cons_f842)
                        yield 11, subst2
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp7 = subjects.popleft()
            subjects8 = deque(tmp7._args)
            # State 2336
            if len(subjects8) >= 1:
                tmp9 = subjects8.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp9)
                except ValueError:
                    pass
                else:
                    pass
                    # State 2337
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 2338
                        if len(subjects8) == 0:
                            pass
                            # State 2339
                            if len(subjects) == 0:
                                pass
                                # 0: x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                yield 0, subst2
                    if len(subjects8) >= 1:
                        tmp12 = subjects8.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp12)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 2338
                            if len(subjects8) == 0:
                                pass
                                # State 2339
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n /; (cons_f2) and (cons_f3) and (cons_f4) and (cons_f5)
                                    yield 0, subst2
                        subjects8.appendleft(tmp12)
                    if len(subjects8) >= 1:
                        tmp14 = subjects8.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp14)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151753
                            if len(subjects8) == 0:
                                pass
                                # State 151754
                                if len(subjects) == 0:
                                    pass
                                    # 8: x**n /; (cons_f4) and (cons_f1246) and (With6953)
                                    yield 8, subst2
                                    # 9: x**n /; (cons_f2) and (cons_f3) and (cons_f5) and (cons_f198) and (cons_f2031)
                                    yield 9, subst2
                                    # 10: x**n /; (cons_f198) and (cons_f842) and (cons_f2032)
                                    yield 10, subst2
                                    # 12: x**n /; (cons_f198) and (cons_f842)
                                    yield 12, subst2
                        subjects8.appendleft(tmp14)
                subjects8.appendleft(tmp9)
            if len(subjects8) >= 1:
                tmp16 = subjects8.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1_1', tmp16)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151978
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151979
                        if len(subjects8) == 0:
                            pass
                            # State 151980
                            if len(subjects) == 0:
                                pass
                                # 11: w**n2 /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f5) and (cons_f842)
                                yield 11, subst2
                    if len(subjects8) >= 1:
                        tmp19 = subjects8.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp19)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151979
                            if len(subjects8) == 0:
                                pass
                                # State 151980
                                if len(subjects) == 0:
                                    pass
                                    # 11: w**n2 /; (cons_f2) and (cons_f3) and (cons_f19) and (cons_f5) and (cons_f842)
                                    yield 11, subst2
                        subjects8.appendleft(tmp19)
                subjects8.appendleft(tmp16)
            subjects.appendleft(tmp7)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp21 = subjects.popleft()
            subjects22 = deque(tmp21._args)
            # State 42412
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 42413
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 42414
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 42415
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 42416
                            if len(subjects22) >= 1 and isinstance(subjects22[0], Add):
                                tmp27 = subjects22.popleft()
                                associative1 = tmp27
                                associative_type1 = type(tmp27)
                                subjects28 = deque(tmp27._args)
                                matcher = CommutativeMatcher42418.get()
                                tmp29 = subjects28
                                subjects28 = []
                                for s in tmp29:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp29, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 42434
                                        if len(subjects22) == 0:
                                            pass
                                            # State 42435
                                            if len(subjects) == 0:
                                                pass
                                                # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                yield 1, subst5
                                    if pattern_index == 1:
                                        pass
                                        # State 54534
                                        if len(subjects22) == 0:
                                            pass
                                            # State 54535
                                            if len(subjects) == 0:
                                                pass
                                                # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                yield 3, subst5
                                subjects22.appendleft(tmp27)
                            if len(subjects22) >= 1:
                                tmp30 = subjects22.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.1', tmp30)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45215
                                    if len(subjects22) == 0:
                                        pass
                                        # State 45216
                                        if len(subjects) == 0:
                                            pass
                                            # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                            yield 2, subst5
                                subjects22.appendleft(tmp30)
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 54524
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54525
                                    if len(subjects22) >= 1:
                                        tmp34 = subjects22.popleft()
                                        subst7 = Substitution(subst6)
                                        try:
                                            subst7.try_add_variable('i2.2.1.2.2.2.1.0', tmp34)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54526
                                            if len(subjects22) == 0:
                                                pass
                                                # State 54527
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                    yield 3, subst7
                                        subjects22.appendleft(tmp34)
                                if len(subjects22) >= 1 and isinstance(subjects22[0], Mul):
                                    tmp36 = subjects22.popleft()
                                    associative1 = tmp36
                                    associative_type1 = type(tmp36)
                                    subjects37 = deque(tmp36._args)
                                    matcher = CommutativeMatcher54529.get()
                                    tmp38 = subjects37
                                    subjects37 = []
                                    for s in tmp38:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp38, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 54530
                                            if len(subjects22) == 0:
                                                pass
                                                # State 54531
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                    yield 3, subst6
                                    subjects22.appendleft(tmp36)
                        if len(subjects22) >= 1 and isinstance(subjects22[0], Pow):
                            tmp39 = subjects22.popleft()
                            subjects40 = deque(tmp39._args)
                            # State 42436
                            if len(subjects40) >= 1 and isinstance(subjects40[0], Add):
                                tmp41 = subjects40.popleft()
                                associative1 = tmp41
                                associative_type1 = type(tmp41)
                                subjects42 = deque(tmp41._args)
                                matcher = CommutativeMatcher42438.get()
                                tmp43 = subjects42
                                subjects42 = []
                                for s in tmp43:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp43, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 42454
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 42455
                                            if len(subjects40) == 0:
                                                pass
                                                # State 42456
                                                if len(subjects22) == 0:
                                                    pass
                                                    # State 42457
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                        yield 1, subst5
                                        if len(subjects40) >= 1:
                                            tmp45 = []
                                            tmp45.append(subjects40.popleft())
                                            while True:
                                                if len(tmp45) > 1:
                                                    tmp46 = create_operation_expression(associative1, tmp45)
                                                elif len(tmp45) == 1:
                                                    tmp46 = tmp45[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp46)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 42455
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 42456
                                                        if len(subjects22) == 0:
                                                            pass
                                                            # State 42457
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                yield 1, subst5
                                                if len(subjects40) == 0:
                                                    break
                                                tmp45.append(subjects40.popleft())
                                            subjects40.extendleft(reversed(tmp45))
                                    if pattern_index == 1:
                                        pass
                                        # State 54550
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54551
                                            if len(subjects40) == 0:
                                                pass
                                                # State 54552
                                                if len(subjects22) == 0:
                                                    pass
                                                    # State 54553
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                        yield 3, subst5
                                        if len(subjects40) >= 1:
                                            tmp49 = []
                                            tmp49.append(subjects40.popleft())
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
                                                    # State 54551
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 54552
                                                        if len(subjects22) == 0:
                                                            pass
                                                            # State 54553
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                yield 3, subst5
                                                if len(subjects40) == 0:
                                                    break
                                                tmp49.append(subjects40.popleft())
                                            subjects40.extendleft(reversed(tmp49))
                                subjects40.appendleft(tmp41)
                            if len(subjects40) >= 1:
                                tmp52 = subjects40.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.1', tmp52)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45217
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45218
                                        if len(subjects40) == 0:
                                            pass
                                            # State 45219
                                            if len(subjects22) == 0:
                                                pass
                                                # State 45220
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                    yield 2, subst5
                                    if len(subjects40) >= 1:
                                        tmp55 = subjects40.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp55)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45218
                                            if len(subjects40) == 0:
                                                pass
                                                # State 45219
                                                if len(subjects22) == 0:
                                                    pass
                                                    # State 45220
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                        yield 2, subst5
                                        subjects40.appendleft(tmp55)
                                subjects40.appendleft(tmp52)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 54536
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54537
                                    if len(subjects40) >= 1:
                                        tmp59 = subjects40.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp59)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54538
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54539
                                                if len(subjects40) == 0:
                                                    pass
                                                    # State 54540
                                                    if len(subjects22) == 0:
                                                        pass
                                                        # State 54541
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                            yield 3, subst7
                                            if len(subjects40) >= 1:
                                                tmp62 = subjects40.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.2.2.2', tmp62)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54539
                                                    if len(subjects40) == 0:
                                                        pass
                                                        # State 54540
                                                        if len(subjects22) == 0:
                                                            pass
                                                            # State 54541
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                yield 3, subst7
                                                subjects40.appendleft(tmp62)
                                        subjects40.appendleft(tmp59)
                                if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                                    tmp64 = subjects40.popleft()
                                    associative1 = tmp64
                                    associative_type1 = type(tmp64)
                                    subjects65 = deque(tmp64._args)
                                    matcher = CommutativeMatcher54543.get()
                                    tmp66 = subjects65
                                    subjects65 = []
                                    for s in tmp66:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp66, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 54544
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54545
                                                if len(subjects40) == 0:
                                                    pass
                                                    # State 54546
                                                    if len(subjects22) == 0:
                                                        pass
                                                        # State 54547
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                            yield 3, subst6
                                            if len(subjects40) >= 1:
                                                tmp68 = []
                                                tmp68.append(subjects40.popleft())
                                                while True:
                                                    if len(tmp68) > 1:
                                                        tmp69 = create_operation_expression(associative1, tmp68)
                                                    elif len(tmp68) == 1:
                                                        tmp69 = tmp68[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', tmp69)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54545
                                                        if len(subjects40) == 0:
                                                            pass
                                                            # State 54546
                                                            if len(subjects22) == 0:
                                                                pass
                                                                # State 54547
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                    yield 3, subst6
                                                    if len(subjects40) == 0:
                                                        break
                                                    tmp68.append(subjects40.popleft())
                                                subjects40.extendleft(reversed(tmp68))
                                    subjects40.appendleft(tmp64)
                            subjects22.appendleft(tmp39)
                    if len(subjects22) >= 1 and isinstance(subjects22[0], Mul):
                        tmp71 = subjects22.popleft()
                        associative1 = tmp71
                        associative_type1 = type(tmp71)
                        subjects72 = deque(tmp71._args)
                        matcher = CommutativeMatcher42459.get()
                        tmp73 = subjects72
                        subjects72 = []
                        for s in tmp73:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp73, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 42500
                                if len(subjects22) == 0:
                                    pass
                                    # State 42501
                                    if len(subjects) == 0:
                                        pass
                                        # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                        yield 1, subst3
                            if pattern_index == 1:
                                pass
                                # State 45225
                                if len(subjects22) == 0:
                                    pass
                                    # State 45226
                                    if len(subjects) == 0:
                                        pass
                                        # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                        yield 2, subst3
                            if pattern_index == 2:
                                pass
                                # State 54578
                                if len(subjects22) == 0:
                                    pass
                                    # State 54579
                                    if len(subjects) == 0:
                                        pass
                                        # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                        yield 3, subst3
                        subjects22.appendleft(tmp71)
                if len(subjects22) >= 1 and isinstance(subjects22[0], Pow):
                    tmp74 = subjects22.popleft()
                    subjects75 = deque(tmp74._args)
                    # State 42502
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 42503
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 42504
                            if len(subjects75) >= 1 and isinstance(subjects75[0], Add):
                                tmp78 = subjects75.popleft()
                                associative1 = tmp78
                                associative_type1 = type(tmp78)
                                subjects79 = deque(tmp78._args)
                                matcher = CommutativeMatcher42506.get()
                                tmp80 = subjects79
                                subjects79 = []
                                for s in tmp80:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp80, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 42522
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 42523
                                            if len(subjects75) == 0:
                                                pass
                                                # State 42524
                                                if len(subjects22) == 0:
                                                    pass
                                                    # State 42525
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                        yield 1, subst5
                                        if len(subjects75) >= 1:
                                            tmp82 = []
                                            tmp82.append(subjects75.popleft())
                                            while True:
                                                if len(tmp82) > 1:
                                                    tmp83 = create_operation_expression(associative1, tmp82)
                                                elif len(tmp82) == 1:
                                                    tmp83 = tmp82[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp83)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 42523
                                                    if len(subjects75) == 0:
                                                        pass
                                                        # State 42524
                                                        if len(subjects22) == 0:
                                                            pass
                                                            # State 42525
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                yield 1, subst5
                                                if len(subjects75) == 0:
                                                    break
                                                tmp82.append(subjects75.popleft())
                                            subjects75.extendleft(reversed(tmp82))
                                    if pattern_index == 1:
                                        pass
                                        # State 54594
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54595
                                            if len(subjects75) == 0:
                                                pass
                                                # State 54596
                                                if len(subjects22) == 0:
                                                    pass
                                                    # State 54597
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                        yield 3, subst5
                                        if len(subjects75) >= 1:
                                            tmp86 = []
                                            tmp86.append(subjects75.popleft())
                                            while True:
                                                if len(tmp86) > 1:
                                                    tmp87 = create_operation_expression(associative1, tmp86)
                                                elif len(tmp86) == 1:
                                                    tmp87 = tmp86[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp87)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54595
                                                    if len(subjects75) == 0:
                                                        pass
                                                        # State 54596
                                                        if len(subjects22) == 0:
                                                            pass
                                                            # State 54597
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                yield 3, subst5
                                                if len(subjects75) == 0:
                                                    break
                                                tmp86.append(subjects75.popleft())
                                            subjects75.extendleft(reversed(tmp86))
                                subjects75.appendleft(tmp78)
                            if len(subjects75) >= 1:
                                tmp89 = subjects75.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.1', tmp89)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45227
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45228
                                        if len(subjects75) == 0:
                                            pass
                                            # State 45229
                                            if len(subjects22) == 0:
                                                pass
                                                # State 45230
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                    yield 2, subst5
                                    if len(subjects75) >= 1:
                                        tmp92 = subjects75.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', tmp92)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45228
                                            if len(subjects75) == 0:
                                                pass
                                                # State 45229
                                                if len(subjects22) == 0:
                                                    pass
                                                    # State 45230
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                        yield 2, subst5
                                        subjects75.appendleft(tmp92)
                                subjects75.appendleft(tmp89)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 54580
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54581
                                    if len(subjects75) >= 1:
                                        tmp96 = subjects75.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp96)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54582
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54583
                                                if len(subjects75) == 0:
                                                    pass
                                                    # State 54584
                                                    if len(subjects22) == 0:
                                                        pass
                                                        # State 54585
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                            yield 3, subst7
                                            if len(subjects75) >= 1:
                                                tmp99 = subjects75.popleft()
                                                subst7 = Substitution(subst6)
                                                try:
                                                    subst7.try_add_variable('i2.2.1.2.2', tmp99)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54583
                                                    if len(subjects75) == 0:
                                                        pass
                                                        # State 54584
                                                        if len(subjects22) == 0:
                                                            pass
                                                            # State 54585
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                yield 3, subst7
                                                subjects75.appendleft(tmp99)
                                        subjects75.appendleft(tmp96)
                                if len(subjects75) >= 1 and isinstance(subjects75[0], Mul):
                                    tmp101 = subjects75.popleft()
                                    associative1 = tmp101
                                    associative_type1 = type(tmp101)
                                    subjects102 = deque(tmp101._args)
                                    matcher = CommutativeMatcher54587.get()
                                    tmp103 = subjects102
                                    subjects102 = []
                                    for s in tmp103:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp103, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 54588
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54589
                                                if len(subjects75) == 0:
                                                    pass
                                                    # State 54590
                                                    if len(subjects22) == 0:
                                                        pass
                                                        # State 54591
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                            yield 3, subst6
                                            if len(subjects75) >= 1:
                                                tmp105 = []
                                                tmp105.append(subjects75.popleft())
                                                while True:
                                                    if len(tmp105) > 1:
                                                        tmp106 = create_operation_expression(associative1, tmp105)
                                                    elif len(tmp105) == 1:
                                                        tmp106 = tmp105[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp106)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54589
                                                        if len(subjects75) == 0:
                                                            pass
                                                            # State 54590
                                                            if len(subjects22) == 0:
                                                                pass
                                                                # State 54591
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                    yield 3, subst6
                                                    if len(subjects75) == 0:
                                                        break
                                                    tmp105.append(subjects75.popleft())
                                                subjects75.extendleft(reversed(tmp105))
                                    subjects75.appendleft(tmp101)
                        if len(subjects75) >= 1 and isinstance(subjects75[0], Pow):
                            tmp108 = subjects75.popleft()
                            subjects109 = deque(tmp108._args)
                            # State 42526
                            if len(subjects109) >= 1 and isinstance(subjects109[0], Add):
                                tmp110 = subjects109.popleft()
                                associative1 = tmp110
                                associative_type1 = type(tmp110)
                                subjects111 = deque(tmp110._args)
                                matcher = CommutativeMatcher42528.get()
                                tmp112 = subjects111
                                subjects111 = []
                                for s in tmp112:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp112, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 42544
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 42545
                                            if len(subjects109) == 0:
                                                pass
                                                # State 42546
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 42547
                                                    if len(subjects75) == 0:
                                                        pass
                                                        # State 42548
                                                        if len(subjects22) == 0:
                                                            pass
                                                            # State 42549
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                yield 1, subst5
                                                if len(subjects75) >= 1:
                                                    tmp115 = subjects75.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp115)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 42547
                                                        if len(subjects75) == 0:
                                                            pass
                                                            # State 42548
                                                            if len(subjects22) == 0:
                                                                pass
                                                                # State 42549
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                    yield 1, subst5
                                                    subjects75.appendleft(tmp115)
                                        if len(subjects109) >= 1:
                                            tmp117 = []
                                            tmp117.append(subjects109.popleft())
                                            while True:
                                                if len(tmp117) > 1:
                                                    tmp118 = create_operation_expression(associative1, tmp117)
                                                elif len(tmp117) == 1:
                                                    tmp118 = tmp117[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp118)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 42545
                                                    if len(subjects109) == 0:
                                                        pass
                                                        # State 42546
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 42547
                                                            if len(subjects75) == 0:
                                                                pass
                                                                # State 42548
                                                                if len(subjects22) == 0:
                                                                    pass
                                                                    # State 42549
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                        yield 1, subst5
                                                        if len(subjects75) >= 1:
                                                            tmp121 = subjects75.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp121)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 42547
                                                                if len(subjects75) == 0:
                                                                    pass
                                                                    # State 42548
                                                                    if len(subjects22) == 0:
                                                                        pass
                                                                        # State 42549
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                                            yield 1, subst5
                                                            subjects75.appendleft(tmp121)
                                                if len(subjects109) == 0:
                                                    break
                                                tmp117.append(subjects109.popleft())
                                            subjects109.extendleft(reversed(tmp117))
                                    if pattern_index == 1:
                                        pass
                                        # State 54616
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54617
                                            if len(subjects109) == 0:
                                                pass
                                                # State 54618
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54619
                                                    if len(subjects75) == 0:
                                                        pass
                                                        # State 54620
                                                        if len(subjects22) == 0:
                                                            pass
                                                            # State 54621
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                yield 3, subst5
                                                if len(subjects75) >= 1:
                                                    tmp125 = subjects75.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp125)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54619
                                                        if len(subjects75) == 0:
                                                            pass
                                                            # State 54620
                                                            if len(subjects22) == 0:
                                                                pass
                                                                # State 54621
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                    yield 3, subst5
                                                    subjects75.appendleft(tmp125)
                                        if len(subjects109) >= 1:
                                            tmp127 = []
                                            tmp127.append(subjects109.popleft())
                                            while True:
                                                if len(tmp127) > 1:
                                                    tmp128 = create_operation_expression(associative1, tmp127)
                                                elif len(tmp127) == 1:
                                                    tmp128 = tmp127[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp128)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54617
                                                    if len(subjects109) == 0:
                                                        pass
                                                        # State 54618
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 54619
                                                            if len(subjects75) == 0:
                                                                pass
                                                                # State 54620
                                                                if len(subjects22) == 0:
                                                                    pass
                                                                    # State 54621
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                        yield 3, subst5
                                                        if len(subjects75) >= 1:
                                                            tmp131 = subjects75.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp131)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 54619
                                                                if len(subjects75) == 0:
                                                                    pass
                                                                    # State 54620
                                                                    if len(subjects22) == 0:
                                                                        pass
                                                                        # State 54621
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                            yield 3, subst5
                                                            subjects75.appendleft(tmp131)
                                                if len(subjects109) == 0:
                                                    break
                                                tmp127.append(subjects109.popleft())
                                            subjects109.extendleft(reversed(tmp127))
                                subjects109.appendleft(tmp110)
                            if len(subjects109) >= 1:
                                tmp133 = subjects109.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.1', tmp133)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45231
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45232
                                        if len(subjects109) == 0:
                                            pass
                                            # State 45233
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45234
                                                if len(subjects75) == 0:
                                                    pass
                                                    # State 45235
                                                    if len(subjects22) == 0:
                                                        pass
                                                        # State 45236
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                            yield 2, subst5
                                            if len(subjects75) >= 1:
                                                tmp137 = subjects75.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp137)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 45234
                                                    if len(subjects75) == 0:
                                                        pass
                                                        # State 45235
                                                        if len(subjects22) == 0:
                                                            pass
                                                            # State 45236
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                                yield 2, subst5
                                                subjects75.appendleft(tmp137)
                                    if len(subjects109) >= 1:
                                        tmp139 = subjects109.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp139)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45232
                                            if len(subjects109) == 0:
                                                pass
                                                # State 45233
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 45234
                                                    if len(subjects75) == 0:
                                                        pass
                                                        # State 45235
                                                        if len(subjects22) == 0:
                                                            pass
                                                            # State 45236
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                                yield 2, subst5
                                                if len(subjects75) >= 1:
                                                    tmp142 = subjects75.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp142)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 45234
                                                        if len(subjects75) == 0:
                                                            pass
                                                            # State 45235
                                                            if len(subjects22) == 0:
                                                                pass
                                                                # State 45236
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                                    yield 2, subst5
                                                    subjects75.appendleft(tmp142)
                                        subjects109.appendleft(tmp139)
                                subjects109.appendleft(tmp133)
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 54598
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54599
                                    if len(subjects109) >= 1:
                                        tmp146 = subjects109.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp146)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54600
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54601
                                                if len(subjects109) == 0:
                                                    pass
                                                    # State 54602
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54603
                                                        if len(subjects75) == 0:
                                                            pass
                                                            # State 54604
                                                            if len(subjects22) == 0:
                                                                pass
                                                                # State 54605
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                    yield 3, subst7
                                                    if len(subjects75) >= 1:
                                                        tmp150 = subjects75.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', tmp150)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 54603
                                                            if len(subjects75) == 0:
                                                                pass
                                                                # State 54604
                                                                if len(subjects22) == 0:
                                                                    pass
                                                                    # State 54605
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                        yield 3, subst7
                                                        subjects75.appendleft(tmp150)
                                            if len(subjects109) >= 1:
                                                tmp152 = subjects109.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2.2', tmp152)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54601
                                                    if len(subjects109) == 0:
                                                        pass
                                                        # State 54602
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 54603
                                                            if len(subjects75) == 0:
                                                                pass
                                                                # State 54604
                                                                if len(subjects22) == 0:
                                                                    pass
                                                                    # State 54605
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                        yield 3, subst7
                                                        if len(subjects75) >= 1:
                                                            tmp155 = subjects75.popleft()
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2', tmp155)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 54603
                                                                if len(subjects75) == 0:
                                                                    pass
                                                                    # State 54604
                                                                    if len(subjects22) == 0:
                                                                        pass
                                                                        # State 54605
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                            yield 3, subst7
                                                            subjects75.appendleft(tmp155)
                                                subjects109.appendleft(tmp152)
                                        subjects109.appendleft(tmp146)
                                if len(subjects109) >= 1 and isinstance(subjects109[0], Mul):
                                    tmp157 = subjects109.popleft()
                                    associative1 = tmp157
                                    associative_type1 = type(tmp157)
                                    subjects158 = deque(tmp157._args)
                                    matcher = CommutativeMatcher54607.get()
                                    tmp159 = subjects158
                                    subjects158 = []
                                    for s in tmp159:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp159, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 54608
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54609
                                                if len(subjects109) == 0:
                                                    pass
                                                    # State 54610
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54611
                                                        if len(subjects75) == 0:
                                                            pass
                                                            # State 54612
                                                            if len(subjects22) == 0:
                                                                pass
                                                                # State 54613
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                    yield 3, subst6
                                                    if len(subjects75) >= 1:
                                                        tmp162 = subjects75.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp162)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 54611
                                                            if len(subjects75) == 0:
                                                                pass
                                                                # State 54612
                                                                if len(subjects22) == 0:
                                                                    pass
                                                                    # State 54613
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                        yield 3, subst6
                                                        subjects75.appendleft(tmp162)
                                            if len(subjects109) >= 1:
                                                tmp164 = []
                                                tmp164.append(subjects109.popleft())
                                                while True:
                                                    if len(tmp164) > 1:
                                                        tmp165 = create_operation_expression(associative1, tmp164)
                                                    elif len(tmp164) == 1:
                                                        tmp165 = tmp164[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2.2', tmp165)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54609
                                                        if len(subjects109) == 0:
                                                            pass
                                                            # State 54610
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 54611
                                                                if len(subjects75) == 0:
                                                                    pass
                                                                    # State 54612
                                                                    if len(subjects22) == 0:
                                                                        pass
                                                                        # State 54613
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                            yield 3, subst6
                                                            if len(subjects75) >= 1:
                                                                tmp168 = subjects75.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2.1.2.2', tmp168)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 54611
                                                                    if len(subjects75) == 0:
                                                                        pass
                                                                        # State 54612
                                                                        if len(subjects22) == 0:
                                                                            pass
                                                                            # State 54613
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                                                yield 3, subst6
                                                                subjects75.appendleft(tmp168)
                                                    if len(subjects109) == 0:
                                                        break
                                                    tmp164.append(subjects109.popleft())
                                                subjects109.extendleft(reversed(tmp164))
                                    subjects109.appendleft(tmp157)
                            subjects75.appendleft(tmp108)
                    if len(subjects75) >= 1 and isinstance(subjects75[0], Mul):
                        tmp170 = subjects75.popleft()
                        associative1 = tmp170
                        associative_type1 = type(tmp170)
                        subjects171 = deque(tmp170._args)
                        matcher = CommutativeMatcher42551.get()
                        tmp172 = subjects171
                        subjects171 = []
                        for s in tmp172:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp172, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 42592
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 42593
                                    if len(subjects75) == 0:
                                        pass
                                        # State 42594
                                        if len(subjects22) == 0:
                                            pass
                                            # State 42595
                                            if len(subjects) == 0:
                                                pass
                                                # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                yield 1, subst3
                                if len(subjects75) >= 1:
                                    tmp174 = []
                                    tmp174.append(subjects75.popleft())
                                    while True:
                                        if len(tmp174) > 1:
                                            tmp175 = create_operation_expression(associative1, tmp174)
                                        elif len(tmp174) == 1:
                                            tmp175 = tmp174[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp175)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 42593
                                            if len(subjects75) == 0:
                                                pass
                                                # State 42594
                                                if len(subjects22) == 0:
                                                    pass
                                                    # State 42595
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                                        yield 1, subst3
                                        if len(subjects75) == 0:
                                            break
                                        tmp174.append(subjects75.popleft())
                                    subjects75.extendleft(reversed(tmp174))
                            if pattern_index == 1:
                                pass
                                # State 45241
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45242
                                    if len(subjects75) == 0:
                                        pass
                                        # State 45243
                                        if len(subjects22) == 0:
                                            pass
                                            # State 45244
                                            if len(subjects) == 0:
                                                pass
                                                # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                yield 2, subst3
                                if len(subjects75) >= 1:
                                    tmp178 = []
                                    tmp178.append(subjects75.popleft())
                                    while True:
                                        if len(tmp178) > 1:
                                            tmp179 = create_operation_expression(associative1, tmp178)
                                        elif len(tmp178) == 1:
                                            tmp179 = tmp178[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp179)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45242
                                            if len(subjects75) == 0:
                                                pass
                                                # State 45243
                                                if len(subjects22) == 0:
                                                    pass
                                                    # State 45244
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                                        yield 2, subst3
                                        if len(subjects75) == 0:
                                            break
                                        tmp178.append(subjects75.popleft())
                                    subjects75.extendleft(reversed(tmp178))
                            if pattern_index == 2:
                                pass
                                # State 54646
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54647
                                    if len(subjects75) == 0:
                                        pass
                                        # State 54648
                                        if len(subjects22) == 0:
                                            pass
                                            # State 54649
                                            if len(subjects) == 0:
                                                pass
                                                # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                yield 3, subst3
                                if len(subjects75) >= 1:
                                    tmp182 = []
                                    tmp182.append(subjects75.popleft())
                                    while True:
                                        if len(tmp182) > 1:
                                            tmp183 = create_operation_expression(associative1, tmp182)
                                        elif len(tmp182) == 1:
                                            tmp183 = tmp182[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp183)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54647
                                            if len(subjects75) == 0:
                                                pass
                                                # State 54648
                                                if len(subjects22) == 0:
                                                    pass
                                                    # State 54649
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                                        yield 3, subst3
                                        if len(subjects75) == 0:
                                            break
                                        tmp182.append(subjects75.popleft())
                                    subjects75.extendleft(reversed(tmp182))
                        subjects75.appendleft(tmp170)
                    subjects22.appendleft(tmp74)
            if len(subjects22) >= 1 and isinstance(subjects22[0], Mul):
                tmp185 = subjects22.popleft()
                associative1 = tmp185
                associative_type1 = type(tmp185)
                subjects186 = deque(tmp185._args)
                matcher = CommutativeMatcher42597.get()
                tmp187 = subjects186
                subjects186 = []
                for s in tmp187:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp187, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 42774
                        if len(subjects22) == 0:
                            pass
                            # State 42775
                            if len(subjects) == 0:
                                pass
                                # 1: log(c*(d*(e + f*x + g*x**2)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                yield 1, subst1
                    if pattern_index == 1:
                        pass
                        # State 45269
                        if len(subjects22) == 0:
                            pass
                            # State 45270
                            if len(subjects) == 0:
                                pass
                                # 2: log(c*(d*v**p)**q) /; (cons_f8) and (cons_f29) and (cons_f5) and (cons_f52) and (cons_f554) and (cons_f1202)
                                yield 2, subst1
                    if pattern_index == 2:
                        pass
                        # State 54762
                        if len(subjects22) == 0:
                            pass
                            # State 54763
                            if len(subjects) == 0:
                                pass
                                # 3: log(c*(d*(e + x*f)**p)**q) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                                yield 3, subst1
                subjects22.appendleft(tmp185)
            subjects.appendleft(tmp21)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp188 = subjects.popleft()
            subjects189 = deque(tmp188._args)
            # State 110119
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 110120
                if len(subjects189) >= 1:
                    tmp191 = subjects189.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp191)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 110121
                        if len(subjects189) == 0:
                            pass
                            # State 110122
                            if len(subjects) == 0:
                                pass
                                # 4: asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 4, subst2
                    subjects189.appendleft(tmp191)
            if len(subjects189) >= 1 and isinstance(subjects189[0], Mul):
                tmp193 = subjects189.popleft()
                associative1 = tmp193
                associative_type1 = type(tmp193)
                subjects194 = deque(tmp193._args)
                matcher = CommutativeMatcher110124.get()
                tmp195 = subjects194
                subjects194 = []
                for s in tmp195:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp195, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110125
                        if len(subjects189) == 0:
                            pass
                            # State 110126
                            if len(subjects) == 0:
                                pass
                                # 4: asin(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 4, subst1
                subjects189.appendleft(tmp193)
            subjects.appendleft(tmp188)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp196 = subjects.popleft()
            subjects197 = deque(tmp196._args)
            # State 110216
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 110217
                if len(subjects197) >= 1:
                    tmp199 = subjects197.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp199)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 110218
                        if len(subjects197) == 0:
                            pass
                            # State 110219
                            if len(subjects) == 0:
                                pass
                                # 5: acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 5, subst2
                    subjects197.appendleft(tmp199)
            if len(subjects197) >= 1 and isinstance(subjects197[0], Mul):
                tmp201 = subjects197.popleft()
                associative1 = tmp201
                associative_type1 = type(tmp201)
                subjects202 = deque(tmp201._args)
                matcher = CommutativeMatcher110221.get()
                tmp203 = subjects202
                subjects202 = []
                for s in tmp203:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp203, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 110222
                        if len(subjects197) == 0:
                            pass
                            # State 110223
                            if len(subjects) == 0:
                                pass
                                # 5: acos(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 5, subst1
                subjects197.appendleft(tmp201)
            subjects.appendleft(tmp196)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp204 = subjects.popleft()
            subjects205 = deque(tmp204._args)
            # State 139854
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139855
                if len(subjects205) >= 1:
                    tmp207 = subjects205.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp207)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139856
                        if len(subjects205) == 0:
                            pass
                            # State 139857
                            if len(subjects) == 0:
                                pass
                                # 6: asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 6, subst2
                    subjects205.appendleft(tmp207)
            if len(subjects205) >= 1 and isinstance(subjects205[0], Mul):
                tmp209 = subjects205.popleft()
                associative1 = tmp209
                associative_type1 = type(tmp209)
                subjects210 = deque(tmp209._args)
                matcher = CommutativeMatcher139859.get()
                tmp211 = subjects210
                subjects210 = []
                for s in tmp211:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp211, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 139860
                        if len(subjects205) == 0:
                            pass
                            # State 139861
                            if len(subjects) == 0:
                                pass
                                # 6: asinh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 6, subst1
                subjects205.appendleft(tmp209)
            subjects.appendleft(tmp204)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp212 = subjects.popleft()
            subjects213 = deque(tmp212._args)
            # State 139951
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139952
                if len(subjects213) >= 1:
                    tmp215 = subjects213.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp215)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139953
                        if len(subjects213) == 0:
                            pass
                            # State 139954
                            if len(subjects) == 0:
                                pass
                                # 7: acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 7, subst2
                    subjects213.appendleft(tmp215)
            if len(subjects213) >= 1 and isinstance(subjects213[0], Mul):
                tmp217 = subjects213.popleft()
                associative1 = tmp217
                associative_type1 = type(tmp217)
                subjects218 = deque(tmp217._args)
                matcher = CommutativeMatcher139956.get()
                tmp219 = subjects218
                subjects218 = []
                for s in tmp219:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp219, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 139957
                        if len(subjects213) == 0:
                            pass
                            # State 139958
                            if len(subjects) == 0:
                                pass
                                # 7: acosh(x*c) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                yield 7, subst1
                subjects213.appendleft(tmp217)
            subjects.appendleft(tmp212)
        return
        yield


from .generated_part000589 import *
from .generated_part000601 import *
from .generated_part000640 import *
from .generated_part000586 import *
from .generated_part000641 import *
from collections import deque
from .generated_part000612 import *
from .generated_part000639 import *
from matchpy.utils import VariableWithCount
from .generated_part000642 import *
from .generated_part000604 import *
from .generated_part000588 import *
from .generated_part000599 import *
from .generated_part000591 import *
from multiset import Multiset
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part000592 import *
from .generated_part000605 import *
from .generated_part000602 import *