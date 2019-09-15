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


class CommutativeMatcher3814(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1, 2: 1, 3: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({4: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({5: 1, 6: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({7: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({8: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({9: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({10: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({11: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Mul)
]),
    8: (8, Multiset({12: 1}), [
      (VariableWithCount('i3.0', 1, 1, None), Mul)
]),
    9: (9, Multiset({13: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({14: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({15: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({16: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({17: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({18: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({19: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({20: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({21: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({22: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({23: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({24: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({25: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({26: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({27: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({28: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 1
    anonymous_patterns = {8, 7}

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher3814._instance is None:
            CommutativeMatcher3814._instance = CommutativeMatcher3814()
        return CommutativeMatcher3814._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3813
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 3815
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 3816
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 3817
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 3818
                            if len(subjects2) >= 1:
                                tmp7 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2', tmp7)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 3819
                                    if len(subjects2) == 0:
                                        pass
                                        # State 3820
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (a + x*b)**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f226) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f225)
                                            yield 0, subst4
                                subjects2.appendleft(tmp7)
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp9 = subjects2.popleft()
                    associative1 = tmp9
                    associative_type1 = type(tmp9)
                    subjects10 = deque(tmp9._args)
                    matcher = CommutativeMatcher3822.get()
                    tmp11 = subjects10
                    subjects10 = []
                    for s in tmp11:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp11, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 3823
                            if len(subjects2) >= 1:
                                tmp12 = []
                                tmp12.append(subjects2.popleft())
                                while True:
                                    if len(tmp12) > 1:
                                        tmp13 = create_operation_expression(associative1, tmp12)
                                    elif len(tmp12) == 1:
                                        tmp13 = tmp12[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.2', tmp13)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 3824
                                        if len(subjects2) == 0:
                                            pass
                                            # State 3825
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (a + x*b)**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f226) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f225)
                                                yield 0, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp12.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp12))
                    subjects2.appendleft(tmp9)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 3836
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.0_2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 3837
                    if len(subjects2) >= 1:
                        tmp17 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.2.1.0', tmp17)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 3838
                            if len(subjects2) >= 1:
                                tmp19 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2_1', tmp19)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 3839
                                    if len(subjects2) == 0:
                                        pass
                                        # State 3840
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (c + x*d)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f226) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f225)
                                            yield 1, subst4
                                subjects2.appendleft(tmp19)
                        subjects2.appendleft(tmp17)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp21 = subjects2.popleft()
                    associative1 = tmp21
                    associative_type1 = type(tmp21)
                    subjects22 = deque(tmp21._args)
                    matcher = CommutativeMatcher3842.get()
                    tmp23 = subjects22
                    subjects22 = []
                    for s in tmp23:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp23, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 3843
                            if len(subjects2) >= 1:
                                tmp24 = []
                                tmp24.append(subjects2.popleft())
                                while True:
                                    if len(tmp24) > 1:
                                        tmp25 = create_operation_expression(associative1, tmp24)
                                    elif len(tmp24) == 1:
                                        tmp25 = tmp24[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.2_1', tmp25)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 3844
                                        if len(subjects2) == 0:
                                            pass
                                            # State 3845
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (c + x*d)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f226) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f225)
                                                yield 1, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp24.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp24))
                    subjects2.appendleft(tmp21)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.2.0_2', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 3852
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.0_3', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 3853
                    if len(subjects2) >= 1:
                        tmp29 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.2.1.0', tmp29)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 3854
                            if len(subjects2) >= 1:
                                tmp31 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2_2', tmp31)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 3855
                                    if len(subjects2) == 0:
                                        pass
                                        # State 3856
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (e + x*f)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f226) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f225)
                                            yield 2, subst4
                                subjects2.appendleft(tmp31)
                        subjects2.appendleft(tmp29)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp33 = subjects2.popleft()
                    associative1 = tmp33
                    associative_type1 = type(tmp33)
                    subjects34 = deque(tmp33._args)
                    matcher = CommutativeMatcher3858.get()
                    tmp35 = subjects34
                    subjects34 = []
                    for s in tmp35:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp35, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 3859
                            if len(subjects2) >= 1:
                                tmp36 = []
                                tmp36.append(subjects2.popleft())
                                while True:
                                    if len(tmp36) > 1:
                                        tmp37 = create_operation_expression(associative1, tmp36)
                                    elif len(tmp36) == 1:
                                        tmp37 = tmp36[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.2_2', tmp37)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 3860
                                        if len(subjects2) == 0:
                                            pass
                                            # State 3861
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (e + x*f)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f226) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f225)
                                                yield 2, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp36.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp36))
                    subjects2.appendleft(tmp33)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.2.0_3', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 3868
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.0_4', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 3869
                    if len(subjects2) >= 1:
                        tmp41 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.2.1.0', tmp41)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 3870
                            if len(subjects2) >= 1:
                                tmp43 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2_3', tmp43)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 3871
                                    if len(subjects2) == 0:
                                        pass
                                        # State 3872
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (g + x*h)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f226) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f225)
                                            yield 3, subst4
                                subjects2.appendleft(tmp43)
                        subjects2.appendleft(tmp41)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp45 = subjects2.popleft()
                    associative1 = tmp45
                    associative_type1 = type(tmp45)
                    subjects46 = deque(tmp45._args)
                    matcher = CommutativeMatcher3874.get()
                    tmp47 = subjects46
                    subjects46 = []
                    for s in tmp47:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp47, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 3875
                            if len(subjects2) >= 1:
                                tmp48 = []
                                tmp48.append(subjects2.popleft())
                                while True:
                                    if len(tmp48) > 1:
                                        tmp49 = create_operation_expression(associative1, tmp48)
                                    elif len(tmp48) == 1:
                                        tmp49 = tmp48[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.2_3', tmp49)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 3876
                                        if len(subjects2) == 0:
                                            pass
                                            # State 3877
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (g + x*h)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f226) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f225)
                                                yield 3, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp48.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp48))
                    subjects2.appendleft(tmp45)
            if len(subjects2) >= 1:
                tmp51 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1', tmp51)
                except ValueError:
                    pass
                else:
                    pass
                    # State 6070
                    if len(subjects2) >= 1:
                        tmp53 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.2', tmp53)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 6071
                            if len(subjects2) == 0:
                                pass
                                # State 6072
                                if len(subjects) == 0:
                                    pass
                                    # 4: x**n /; (cons_f3) and (cons_f4) and (cons_f5) and (cons_f461)
                                    yield 4, subst2
                        subjects2.appendleft(tmp53)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 101268
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.3.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 101269
                            if len(subjects2) >= 1:
                                tmp57 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.3.1.0', tmp57)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 101270
                                    if len(subjects2) == 0:
                                        pass
                                        # State 101271
                                        if len(subjects) == 0:
                                            pass
                                            # 27: F**(c + x*d) /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1666)
                                            yield 27, subst4
                                subjects2.appendleft(tmp57)
                        if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                            tmp59 = subjects2.popleft()
                            associative1 = tmp59
                            associative_type1 = type(tmp59)
                            subjects60 = deque(tmp59._args)
                            matcher = CommutativeMatcher101273.get()
                            tmp61 = subjects60
                            subjects60 = []
                            for s in tmp61:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp61, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 101274
                                    if len(subjects2) == 0:
                                        pass
                                        # State 101275
                                        if len(subjects) == 0:
                                            pass
                                            # 27: F**(c + x*d) /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1666)
                                            yield 27, subst3
                            subjects2.appendleft(tmp59)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                        tmp62 = subjects2.popleft()
                        associative1 = tmp62
                        associative_type1 = type(tmp62)
                        subjects63 = deque(tmp62._args)
                        matcher = CommutativeMatcher101277.get()
                        tmp64 = subjects63
                        subjects63 = []
                        for s in tmp64:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp64, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 101283
                                if len(subjects2) == 0:
                                    pass
                                    # State 101284
                                    if len(subjects) == 0:
                                        pass
                                        # 27: F**(c + x*d) /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1666)
                                        yield 27, subst2
                        subjects2.appendleft(tmp62)
                subjects2.appendleft(tmp51)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp65 = subjects2.popleft()
                associative1 = tmp65
                associative_type1 = type(tmp65)
                subjects66 = deque(tmp65._args)
                matcher = CommutativeMatcher3827.get()
                tmp67 = subjects66
                subjects66 = []
                for s in tmp67:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp67, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 3833
                        if len(subjects2) >= 1:
                            tmp68 = []
                            tmp68.append(subjects2.popleft())
                            while True:
                                if len(tmp68) > 1:
                                    tmp69 = create_operation_expression(associative1, tmp68)
                                elif len(tmp68) == 1:
                                    tmp69 = tmp68[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2', tmp69)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 3834
                                    if len(subjects2) == 0:
                                        pass
                                        # State 3835
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (a + x*b)**m /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f226) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f225)
                                            yield 0, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp68.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp68))
                    if pattern_index == 1:
                        pass
                        # State 3849
                        if len(subjects2) >= 1:
                            tmp71 = []
                            tmp71.append(subjects2.popleft())
                            while True:
                                if len(tmp71) > 1:
                                    tmp72 = create_operation_expression(associative1, tmp71)
                                elif len(tmp71) == 1:
                                    tmp72 = tmp71[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2_1', tmp72)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 3850
                                    if len(subjects2) == 0:
                                        pass
                                        # State 3851
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (c + x*d)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f226) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f225)
                                            yield 1, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp71.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp71))
                    if pattern_index == 2:
                        pass
                        # State 3865
                        if len(subjects2) >= 1:
                            tmp74 = []
                            tmp74.append(subjects2.popleft())
                            while True:
                                if len(tmp74) > 1:
                                    tmp75 = create_operation_expression(associative1, tmp74)
                                elif len(tmp74) == 1:
                                    tmp75 = tmp74[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2_2', tmp75)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 3866
                                    if len(subjects2) == 0:
                                        pass
                                        # State 3867
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (e + x*f)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f226) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f225)
                                            yield 2, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp74.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp74))
                    if pattern_index == 3:
                        pass
                        # State 3881
                        if len(subjects2) >= 1:
                            tmp77 = []
                            tmp77.append(subjects2.popleft())
                            while True:
                                if len(tmp77) > 1:
                                    tmp78 = create_operation_expression(associative1, tmp77)
                                elif len(tmp77) == 1:
                                    tmp78 = tmp77[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2_3', tmp78)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 3882
                                    if len(subjects2) == 0:
                                        pass
                                        # State 3883
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (g + x*h)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f226) and (cons_f19) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f225)
                                            yield 3, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp77.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp77))
                    if pattern_index == 4:
                        pass
                        # State 10531
                        if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                            tmp80 = subjects2.popleft()
                            # State 10532
                            if len(subjects2) == 0:
                                pass
                                # State 10533
                                if len(subjects) == 0:
                                    pass
                                    # 5: 1/(c + d*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f805)
                                    yield 5, subst1
                            subjects2.appendleft(tmp80)
                subjects2.appendleft(tmp65)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp81 = subjects2.popleft()
                subjects82 = deque(tmp81._args)
                # State 67659
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 67660
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 67661
                        if len(subjects82) >= 1:
                            tmp85 = subjects82.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.3.1.0', tmp85)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 67662
                                if len(subjects82) == 0:
                                    pass
                                    # State 67663
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                        tmp87 = subjects2.popleft()
                                        # State 67664
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67665
                                            if len(subjects) == 0:
                                                pass
                                                # 15: sin(c + x*d)**2 /; (cons_f3) and (cons_f8) and (cons_f29)
                                                yield 15, subst3
                                        subjects2.appendleft(tmp87)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp88 = subjects2.popleft()
                                        # State 89980
                                        if len(subjects2) == 0:
                                            pass
                                            # State 89981
                                            if len(subjects) == 0:
                                                pass
                                                # 24: 1/sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                yield 24, subst3
                                                # 22: 1/sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                                yield 22, subst3
                                        subjects2.appendleft(tmp88)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                        tmp89 = subjects2.popleft()
                                        # State 94768
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94769
                                            if len(subjects) == 0:
                                                pass
                                                # 26: sin(c + x*d)**(-2) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1645)
                                                yield 26, subst3
                                        subjects2.appendleft(tmp89)
                            subjects82.appendleft(tmp85)
                    if len(subjects82) >= 1 and isinstance(subjects82[0], Mul):
                        tmp90 = subjects82.popleft()
                        associative1 = tmp90
                        associative_type1 = type(tmp90)
                        subjects91 = deque(tmp90._args)
                        matcher = CommutativeMatcher67667.get()
                        tmp92 = subjects91
                        subjects91 = []
                        for s in tmp92:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp92, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 67668
                                if len(subjects82) == 0:
                                    pass
                                    # State 67669
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                        tmp93 = subjects2.popleft()
                                        # State 67670
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67671
                                            if len(subjects) == 0:
                                                pass
                                                # 15: sin(c + x*d)**2 /; (cons_f3) and (cons_f8) and (cons_f29)
                                                yield 15, subst2
                                        subjects2.appendleft(tmp93)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp94 = subjects2.popleft()
                                        # State 89982
                                        if len(subjects2) == 0:
                                            pass
                                            # State 89983
                                            if len(subjects) == 0:
                                                pass
                                                # 24: 1/sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                yield 24, subst2
                                                # 22: 1/sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                                yield 22, subst2
                                        subjects2.appendleft(tmp94)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                        tmp95 = subjects2.popleft()
                                        # State 94770
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94771
                                            if len(subjects) == 0:
                                                pass
                                                # 26: sin(c + x*d)**(-2) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1645)
                                                yield 26, subst2
                                        subjects2.appendleft(tmp95)
                        subjects82.appendleft(tmp90)
                if len(subjects82) >= 1 and isinstance(subjects82[0], Add):
                    tmp96 = subjects82.popleft()
                    associative1 = tmp96
                    associative_type1 = type(tmp96)
                    subjects97 = deque(tmp96._args)
                    matcher = CommutativeMatcher67673.get()
                    tmp98 = subjects97
                    subjects97 = []
                    for s in tmp98:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp98, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 67679
                            if len(subjects82) == 0:
                                pass
                                # State 67680
                                if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                    tmp99 = subjects2.popleft()
                                    # State 67681
                                    if len(subjects2) == 0:
                                        pass
                                        # State 67682
                                        if len(subjects) == 0:
                                            pass
                                            # 15: sin(c + x*d)**2 /; (cons_f3) and (cons_f8) and (cons_f29)
                                            yield 15, subst1
                                    subjects2.appendleft(tmp99)
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp100 = subjects2.popleft()
                                    # State 89984
                                    if len(subjects2) == 0:
                                        pass
                                        # State 89985
                                        if len(subjects) == 0:
                                            pass
                                            # 24: 1/sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                            yield 24, subst1
                                            # 22: 1/sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                            yield 22, subst1
                                    subjects2.appendleft(tmp100)
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                    tmp101 = subjects2.popleft()
                                    # State 94772
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94773
                                        if len(subjects) == 0:
                                            pass
                                            # 26: sin(c + x*d)**(-2) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1645)
                                            yield 26, subst1
                                    subjects2.appendleft(tmp101)
                    subjects82.appendleft(tmp96)
                subjects2.appendleft(tmp81)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp102 = subjects2.popleft()
                subjects103 = deque(tmp102._args)
                # State 67724
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 67725
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 67726
                        if len(subjects103) >= 1:
                            tmp106 = subjects103.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.3.1.0', tmp106)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 67727
                                if len(subjects103) == 0:
                                    pass
                                    # State 67728
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                        tmp108 = subjects2.popleft()
                                        # State 67729
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67730
                                            if len(subjects) == 0:
                                                pass
                                                # 16: cos(c + x*d)**2 /; (cons_f3) and (cons_f8) and (cons_f29)
                                                yield 16, subst3
                                        subjects2.appendleft(tmp108)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp109 = subjects2.popleft()
                                        # State 89951
                                        if len(subjects2) == 0:
                                            pass
                                            # State 89952
                                            if len(subjects) == 0:
                                                pass
                                                # 21: 1/cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                                yield 21, subst3
                                                # 23: 1/cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                yield 23, subst3
                                        subjects2.appendleft(tmp109)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                        tmp110 = subjects2.popleft()
                                        # State 94737
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94738
                                            if len(subjects) == 0:
                                                pass
                                                # 25: cos(c + x*d)**(-2) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1645)
                                                yield 25, subst3
                                        subjects2.appendleft(tmp110)
                            subjects103.appendleft(tmp106)
                    if len(subjects103) >= 1 and isinstance(subjects103[0], Mul):
                        tmp111 = subjects103.popleft()
                        associative1 = tmp111
                        associative_type1 = type(tmp111)
                        subjects112 = deque(tmp111._args)
                        matcher = CommutativeMatcher67732.get()
                        tmp113 = subjects112
                        subjects112 = []
                        for s in tmp113:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp113, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 67733
                                if len(subjects103) == 0:
                                    pass
                                    # State 67734
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                        tmp114 = subjects2.popleft()
                                        # State 67735
                                        if len(subjects2) == 0:
                                            pass
                                            # State 67736
                                            if len(subjects) == 0:
                                                pass
                                                # 16: cos(c + x*d)**2 /; (cons_f3) and (cons_f8) and (cons_f29)
                                                yield 16, subst2
                                        subjects2.appendleft(tmp114)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp115 = subjects2.popleft()
                                        # State 89953
                                        if len(subjects2) == 0:
                                            pass
                                            # State 89954
                                            if len(subjects) == 0:
                                                pass
                                                # 21: 1/cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                                yield 21, subst2
                                                # 23: 1/cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                yield 23, subst2
                                        subjects2.appendleft(tmp115)
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                        tmp116 = subjects2.popleft()
                                        # State 94739
                                        if len(subjects2) == 0:
                                            pass
                                            # State 94740
                                            if len(subjects) == 0:
                                                pass
                                                # 25: cos(c + x*d)**(-2) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1645)
                                                yield 25, subst2
                                        subjects2.appendleft(tmp116)
                        subjects103.appendleft(tmp111)
                if len(subjects103) >= 1 and isinstance(subjects103[0], Add):
                    tmp117 = subjects103.popleft()
                    associative1 = tmp117
                    associative_type1 = type(tmp117)
                    subjects118 = deque(tmp117._args)
                    matcher = CommutativeMatcher67738.get()
                    tmp119 = subjects118
                    subjects118 = []
                    for s in tmp119:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp119, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 67744
                            if len(subjects103) == 0:
                                pass
                                # State 67745
                                if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                                    tmp120 = subjects2.popleft()
                                    # State 67746
                                    if len(subjects2) == 0:
                                        pass
                                        # State 67747
                                        if len(subjects) == 0:
                                            pass
                                            # 16: cos(c + x*d)**2 /; (cons_f3) and (cons_f8) and (cons_f29)
                                            yield 16, subst1
                                    subjects2.appendleft(tmp120)
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp121 = subjects2.popleft()
                                    # State 89955
                                    if len(subjects2) == 0:
                                        pass
                                        # State 89956
                                        if len(subjects) == 0:
                                            pass
                                            # 21: 1/cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                            yield 21, subst1
                                            # 23: 1/cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                            yield 23, subst1
                                    subjects2.appendleft(tmp121)
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-2):
                                    tmp122 = subjects2.popleft()
                                    # State 94741
                                    if len(subjects2) == 0:
                                        pass
                                        # State 94742
                                        if len(subjects) == 0:
                                            pass
                                            # 25: cos(c + x*d)**(-2) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1645)
                                            yield 25, subst1
                                    subjects2.appendleft(tmp122)
                    subjects103.appendleft(tmp117)
                subjects2.appendleft(tmp102)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp123 = subjects2.popleft()
                subjects124 = deque(tmp123._args)
                # State 77344
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 77345
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 77346
                        if len(subjects124) >= 1:
                            tmp127 = subjects124.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.3.1.0', tmp127)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 77347
                                if len(subjects124) == 0:
                                    pass
                                    # State 77348
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp129 = subjects2.popleft()
                                        # State 77349
                                        if len(subjects2) == 0:
                                            pass
                                            # State 77350
                                            if len(subjects) == 0:
                                                pass
                                                # 18: 1/tan(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                                yield 18, subst3
                                                # 20: 1/tan(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                yield 20, subst3
                                        subjects2.appendleft(tmp129)
                            subjects124.appendleft(tmp127)
                    if len(subjects124) >= 1 and isinstance(subjects124[0], Mul):
                        tmp130 = subjects124.popleft()
                        associative1 = tmp130
                        associative_type1 = type(tmp130)
                        subjects131 = deque(tmp130._args)
                        matcher = CommutativeMatcher77352.get()
                        tmp132 = subjects131
                        subjects131 = []
                        for s in tmp132:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp132, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 77353
                                if len(subjects124) == 0:
                                    pass
                                    # State 77354
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp133 = subjects2.popleft()
                                        # State 77355
                                        if len(subjects2) == 0:
                                            pass
                                            # State 77356
                                            if len(subjects) == 0:
                                                pass
                                                # 18: 1/tan(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                                yield 18, subst2
                                                # 20: 1/tan(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                                yield 20, subst2
                                        subjects2.appendleft(tmp133)
                        subjects124.appendleft(tmp130)
                if len(subjects124) >= 1 and isinstance(subjects124[0], Add):
                    tmp134 = subjects124.popleft()
                    associative1 = tmp134
                    associative_type1 = type(tmp134)
                    subjects135 = deque(tmp134._args)
                    matcher = CommutativeMatcher77358.get()
                    tmp136 = subjects135
                    subjects135 = []
                    for s in tmp136:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp136, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 77364
                            if len(subjects124) == 0:
                                pass
                                # State 77365
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp137 = subjects2.popleft()
                                    # State 77366
                                    if len(subjects2) == 0:
                                        pass
                                        # State 77367
                                        if len(subjects) == 0:
                                            pass
                                            # 18: 1/tan(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                            yield 18, subst1
                                            # 20: 1/tan(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                            yield 20, subst1
                                    subjects2.appendleft(tmp137)
                    subjects124.appendleft(tmp134)
                subjects2.appendleft(tmp123)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp138 = subjects2.popleft()
                associative1 = tmp138
                associative_type1 = type(tmp138)
                subjects139 = deque(tmp138._args)
                matcher = CommutativeMatcher101359.get()
                tmp140 = subjects139
                subjects139 = []
                for s in tmp140:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp140, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 101374
                        if len(subjects2) >= 1:
                            tmp141 = []
                            tmp141.append(subjects2.popleft())
                            while True:
                                if len(tmp141) > 1:
                                    tmp142 = create_operation_expression(associative1, tmp141)
                                elif len(tmp141) == 1:
                                    tmp142 = tmp141[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2', tmp142)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 101375
                                    if len(subjects2) == 0:
                                        pass
                                        # State 101376
                                        if len(subjects) == 0:
                                            pass
                                            # 28: (F*b*(c + x*d))**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f5) and (cons_f1666) and (cons_f149)
                                            yield 28, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp141.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp141))
                subjects2.appendleft(tmp138)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 10534
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 10535
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i3.2.1.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 10536
                    if len(subjects) >= 1:
                        tmp147 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.2.1.1', tmp147)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10537
                            if len(subjects) == 0:
                                pass
                                # 6: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f805)
                                yield 6, subst4
                        subjects.appendleft(tmp147)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp149 = subjects.popleft()
                    subjects150 = deque(tmp149._args)
                    # State 10538
                    if len(subjects150) >= 1:
                        tmp151 = subjects150.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.2.1.1', tmp151)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10539
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 10540
                                if len(subjects150) == 0:
                                    pass
                                    # State 10541
                                    if len(subjects) == 0:
                                        pass
                                        # 6: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f805)
                                        yield 6, subst4
                            if len(subjects150) >= 1:
                                tmp154 = subjects150.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2.1.2', tmp154)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 10540
                                    if len(subjects150) == 0:
                                        pass
                                        # State 10541
                                        if len(subjects) == 0:
                                            pass
                                            # 6: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f805)
                                            yield 6, subst4
                                subjects150.appendleft(tmp154)
                        subjects150.appendleft(tmp151)
                    subjects.appendleft(tmp149)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp156 = subjects.popleft()
                associative1 = tmp156
                associative_type1 = type(tmp156)
                subjects157 = deque(tmp156._args)
                matcher = CommutativeMatcher10543.get()
                tmp158 = subjects157
                subjects157 = []
                for s in tmp158:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp158, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 10550
                        if len(subjects) == 0:
                            pass
                            # 6: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f805)
                            yield 6, subst2
                subjects.appendleft(tmp156)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp159 = subjects.popleft()
            associative1 = tmp159
            associative_type1 = type(tmp159)
            subjects160 = deque(tmp159._args)
            matcher = CommutativeMatcher10552.get()
            tmp161 = subjects160
            subjects160 = []
            for s in tmp161:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp161, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 10569
                    if len(subjects) == 0:
                        pass
                        # 6: a + b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f805)
                        yield 6, subst1
            subjects.appendleft(tmp159)
        if len(subjects) >= 1 and subjects[0] == LambertW(Add(Symbol('a'), Mul(Symbol('b'), Symbol('x')))):
            tmp162 = subjects.popleft()
            # State 56676
            if len(subjects) == 0:
                pass
                # 7: LambertW(a + b*x)
                yield 7, subst0
            subjects.appendleft(tmp162)
        if len(subjects) >= 1 and subjects[0] == LambertW(Mul(Symbol('a'), Pow(Symbol('x'), Symbol('n')))):
            tmp163 = subjects.popleft()
            # State 56725
            if len(subjects) == 0:
                pass
                # 8: LambertW(a*x**n)
                yield 8, subst0
            subjects.appendleft(tmp163)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp164 = subjects.popleft()
            subjects165 = deque(tmp164._args)
            # State 57856
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 57857
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57858
                    if len(subjects165) >= 1:
                        tmp168 = subjects165.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.2.1.0', tmp168)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 57859
                            if len(subjects165) == 0:
                                pass
                                # State 57860
                                if len(subjects) == 0:
                                    pass
                                    # 9: sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                    yield 9, subst3
                                    # 11: sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1265)
                                    yield 11, subst3
                                    # 13: sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 13, subst3
                        subjects165.appendleft(tmp168)
                if len(subjects165) >= 1 and isinstance(subjects165[0], Mul):
                    tmp170 = subjects165.popleft()
                    associative1 = tmp170
                    associative_type1 = type(tmp170)
                    subjects171 = deque(tmp170._args)
                    matcher = CommutativeMatcher57862.get()
                    tmp172 = subjects171
                    subjects171 = []
                    for s in tmp172:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp172, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57863
                            if len(subjects165) == 0:
                                pass
                                # State 57864
                                if len(subjects) == 0:
                                    pass
                                    # 9: sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                    yield 9, subst2
                                    # 11: sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1265)
                                    yield 11, subst2
                                    # 13: sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 13, subst2
                    subjects165.appendleft(tmp170)
            if len(subjects165) >= 1 and isinstance(subjects165[0], Add):
                tmp173 = subjects165.popleft()
                associative1 = tmp173
                associative_type1 = type(tmp173)
                subjects174 = deque(tmp173._args)
                matcher = CommutativeMatcher57866.get()
                tmp175 = subjects174
                subjects174 = []
                for s in tmp175:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp175, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 57872
                        if len(subjects165) == 0:
                            pass
                            # State 57873
                            if len(subjects) == 0:
                                pass
                                # 9: sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                yield 9, subst1
                                # 11: sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1265)
                                yield 11, subst1
                                # 13: sin(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                yield 13, subst1
                subjects165.appendleft(tmp173)
            subjects.appendleft(tmp164)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp176 = subjects.popleft()
            subjects177 = deque(tmp176._args)
            # State 57909
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 57910
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57911
                    if len(subjects177) >= 1:
                        tmp180 = subjects177.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.2.1.0', tmp180)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 57912
                            if len(subjects177) == 0:
                                pass
                                # State 57913
                                if len(subjects) == 0:
                                    pass
                                    # 10: cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                    yield 10, subst3
                                    # 12: cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1265)
                                    yield 12, subst3
                                    # 14: cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 14, subst3
                        subjects177.appendleft(tmp180)
                if len(subjects177) >= 1 and isinstance(subjects177[0], Mul):
                    tmp182 = subjects177.popleft()
                    associative1 = tmp182
                    associative_type1 = type(tmp182)
                    subjects183 = deque(tmp182._args)
                    matcher = CommutativeMatcher57915.get()
                    tmp184 = subjects183
                    subjects183 = []
                    for s in tmp184:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp184, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57916
                            if len(subjects177) == 0:
                                pass
                                # State 57917
                                if len(subjects) == 0:
                                    pass
                                    # 10: cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                    yield 10, subst2
                                    # 12: cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1265)
                                    yield 12, subst2
                                    # 14: cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 14, subst2
                    subjects177.appendleft(tmp182)
            if len(subjects177) >= 1 and isinstance(subjects177[0], Add):
                tmp185 = subjects177.popleft()
                associative1 = tmp185
                associative_type1 = type(tmp185)
                subjects186 = deque(tmp185._args)
                matcher = CommutativeMatcher57919.get()
                tmp187 = subjects186
                subjects186 = []
                for s in tmp187:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp187, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 57925
                        if len(subjects177) == 0:
                            pass
                            # State 57926
                            if len(subjects) == 0:
                                pass
                                # 10: cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                yield 10, subst1
                                # 12: cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1265)
                                yield 12, subst1
                                # 14: cos(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                yield 14, subst1
                subjects177.appendleft(tmp185)
            subjects.appendleft(tmp176)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp188 = subjects.popleft()
            subjects189 = deque(tmp188._args)
            # State 77285
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 77286
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 77287
                    if len(subjects189) >= 1:
                        tmp192 = subjects189.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.2.1.0', tmp192)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 77288
                            if len(subjects189) == 0:
                                pass
                                # State 77289
                                if len(subjects) == 0:
                                    pass
                                    # 17: tan(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                    yield 17, subst3
                                    # 19: tan(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 19, subst3
                        subjects189.appendleft(tmp192)
                if len(subjects189) >= 1 and isinstance(subjects189[0], Mul):
                    tmp194 = subjects189.popleft()
                    associative1 = tmp194
                    associative_type1 = type(tmp194)
                    subjects195 = deque(tmp194._args)
                    matcher = CommutativeMatcher77291.get()
                    tmp196 = subjects195
                    subjects195 = []
                    for s in tmp196:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp196, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 77292
                            if len(subjects189) == 0:
                                pass
                                # State 77293
                                if len(subjects) == 0:
                                    pass
                                    # 17: tan(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                    yield 17, subst2
                                    # 19: tan(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    yield 19, subst2
                    subjects189.appendleft(tmp194)
            if len(subjects189) >= 1 and isinstance(subjects189[0], Add):
                tmp197 = subjects189.popleft()
                associative1 = tmp197
                associative_type1 = type(tmp197)
                subjects198 = deque(tmp197._args)
                matcher = CommutativeMatcher77295.get()
                tmp199 = subjects198
                subjects198 = []
                for s in tmp199:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp199, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 77301
                        if len(subjects189) == 0:
                            pass
                            # State 77302
                            if len(subjects) == 0:
                                pass
                                # 17: tan(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29)
                                yield 17, subst1
                                # 19: tan(c + x*d) /; (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                yield 19, subst1
                subjects189.appendleft(tmp197)
            subjects.appendleft(tmp188)
        return
        yield


from .generated_part009849 import *
from .generated_part009874 import *
from .generated_part009867 import *
from .generated_part009881 import *
from .generated_part009872 import *
from .generated_part009856 import *
from .generated_part009861 import *
from .generated_part009864 import *
from .generated_part009878 import *
from .generated_part009871 import *
from .generated_part009858 import *
from .generated_part009875 import *
from .generated_part009853 import *
from collections import deque
from .generated_part009851 import *
from .generated_part009852 import *
from matchpy.utils import VariableWithCount
from .generated_part009862 import *
from .generated_part009865 import *
from .generated_part009880 import *
from .generated_part009859 import *
from multiset import Multiset
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part009850 import *
from .generated_part009877 import *
from .generated_part009854 import *