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


class CommutativeMatcher57205(CommutativeMatcher):
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
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    10: (10, Multiset({11: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    11: (11, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.2.3.0', 1, 1, S(0)), Add)
]),
    12: (12, Multiset({13: 1}), [
      (VariableWithCount('i2.2.1.4.0', 1, 1, S(0)), Add)
]),
    13: (13, Multiset({14: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    14: (14, Multiset({15: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    15: (15, Multiset({9: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    16: (16, Multiset({16: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    17: (17, Multiset({17: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    18: (18, Multiset({18: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    19: (19, Multiset({19: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    20: (20, Multiset({19: 1}), [
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
        if CommutativeMatcher57205._instance is None:
            CommutativeMatcher57205._instance = CommutativeMatcher57205()
        return CommutativeMatcher57205._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 57204
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 57206
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 57207
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
            # State 58406
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58407
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
            # State 64367
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 64368
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
            # State 65747
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 65748
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
                    # State 75825
                    if len(subjects) == 0:
                        pass
                        # 9: x*b
                        yield 9, subst2
                subjects.appendleft(tmp13)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 68200
            if len(subjects) >= 1:
                tmp16 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0', tmp16)
                except ValueError:
                    pass
                else:
                    pass
                    # State 68201
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                        yield 4, subst2
                subjects.appendleft(tmp16)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 72101
            if len(subjects) >= 1:
                tmp19 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp19)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72102
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                        yield 5, subst2
                subjects.appendleft(tmp19)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 75573
                if len(subjects) >= 1:
                    tmp22 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.1', tmp22)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75574
                        if len(subjects) == 0:
                            pass
                            # 7: b*x**n
                            yield 7, subst3
                    subjects.appendleft(tmp22)
            if len(subjects) >= 1:
                tmp24 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp24)
                except ValueError:
                    pass
                else:
                    pass
                    # State 100887
                    if len(subjects) == 0:
                        pass
                        # 14: x*b
                        yield 14, subst2
                subjects.appendleft(tmp24)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp26 = subjects.popleft()
                subjects27 = deque(tmp26._args)
                # State 74655
                if len(subjects27) >= 1:
                    tmp28 = subjects27.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.1', tmp28)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74656
                        if len(subjects27) >= 1:
                            tmp30 = subjects27.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp30)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74657
                                if len(subjects27) == 0:
                                    pass
                                    # State 74658
                                    if len(subjects) == 0:
                                        pass
                                        # 6: b*x**n
                                        yield 6, subst3
                            subjects27.appendleft(tmp30)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 75575
                            if len(subjects27) == 0:
                                pass
                                # State 75576
                                if len(subjects) == 0:
                                    pass
                                    # 7: b*x**n
                                    yield 7, subst3
                        if len(subjects27) >= 1:
                            tmp33 = subjects27.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp33)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75575
                                if len(subjects27) == 0:
                                    pass
                                    # State 75576
                                    if len(subjects) == 0:
                                        pass
                                        # 7: b*x**n
                                        yield 7, subst3
                            subjects27.appendleft(tmp33)
                    subjects27.appendleft(tmp28)
                if len(subjects27) >= 1:
                    tmp35 = subjects27.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp35)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75818
                        if len(subjects27) >= 1 and subjects27[0] == Integer(2):
                            tmp37 = subjects27.popleft()
                            # State 75819
                            if len(subjects27) == 0:
                                pass
                                # State 75820
                                if len(subjects) == 0:
                                    pass
                                    # 8: v**2*c
                                    yield 8, subst2
                            subjects27.appendleft(tmp37)
                    subjects27.appendleft(tmp35)
                if len(subjects27) >= 1 and isinstance(subjects27[0], Add):
                    tmp38 = subjects27.popleft()
                    associative1 = tmp38
                    associative_type1 = type(tmp38)
                    subjects39 = deque(tmp38._args)
                    matcher = CommutativeMatcher107464.get()
                    tmp40 = subjects39
                    subjects39 = []
                    for s in tmp40:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp40, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 107470
                            if len(subjects27) >= 1:
                                tmp41 = []
                                tmp41.append(subjects27.popleft())
                                while True:
                                    if len(tmp41) > 1:
                                        tmp42 = create_operation_expression(associative1, tmp41)
                                    elif len(tmp41) == 1:
                                        tmp42 = tmp41[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.1.2', tmp42)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 107471
                                        if len(subjects27) == 0:
                                            pass
                                            # State 107472
                                            if len(subjects) == 0:
                                                pass
                                                # 17: b*(x*d + c)**n
                                                yield 17, subst3
                                    if len(subjects27) == 0:
                                        break
                                    tmp41.append(subjects27.popleft())
                                subjects27.extendleft(reversed(tmp41))
                    subjects27.appendleft(tmp38)
                subjects.appendleft(tmp26)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp44 = subjects.popleft()
                subjects45 = deque(tmp44._args)
                # State 105092
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 105093
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 105094
                        if len(subjects45) >= 1:
                            tmp48 = subjects45.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.1.2.1', tmp48)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105095
                                if len(subjects45) == 0:
                                    pass
                                    # State 105096
                                    if len(subjects) == 0:
                                        pass
                                        # 16: b*log(c*x**n)
                                        yield 16, subst4
                            subjects45.appendleft(tmp48)
                    if len(subjects45) >= 1 and isinstance(subjects45[0], Pow):
                        tmp50 = subjects45.popleft()
                        subjects51 = deque(tmp50._args)
                        # State 105097
                        if len(subjects51) >= 1:
                            tmp52 = subjects51.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2.1', tmp52)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105098
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 105099
                                    if len(subjects51) == 0:
                                        pass
                                        # State 105100
                                        if len(subjects45) == 0:
                                            pass
                                            # State 105101
                                            if len(subjects) == 0:
                                                pass
                                                # 16: b*log(c*x**n)
                                                yield 16, subst4
                                if len(subjects51) >= 1:
                                    tmp55 = subjects51.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.1.2.2', tmp55)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 105099
                                        if len(subjects51) == 0:
                                            pass
                                            # State 105100
                                            if len(subjects45) == 0:
                                                pass
                                                # State 105101
                                                if len(subjects) == 0:
                                                    pass
                                                    # 16: b*log(c*x**n)
                                                    yield 16, subst4
                                    subjects51.appendleft(tmp55)
                            subjects51.appendleft(tmp52)
                        subjects45.appendleft(tmp50)
                if len(subjects45) >= 1 and isinstance(subjects45[0], Mul):
                    tmp57 = subjects45.popleft()
                    associative1 = tmp57
                    associative_type1 = type(tmp57)
                    subjects58 = deque(tmp57._args)
                    matcher = CommutativeMatcher105103.get()
                    tmp59 = subjects58
                    subjects58 = []
                    for s in tmp59:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp59, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 105110
                            if len(subjects45) == 0:
                                pass
                                # State 105111
                                if len(subjects) == 0:
                                    pass
                                    # 16: b*log(c*x**n)
                                    yield 16, subst2
                    subjects45.appendleft(tmp57)
                subjects.appendleft(tmp44)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 75950
            if len(subjects) >= 1:
                tmp61 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp61)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75951
                    if len(subjects) == 0:
                        pass
                        # 10: x*f
                        yield 10, subst2
                subjects.appendleft(tmp61)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 75988
            if len(subjects) >= 1:
                tmp64 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp64)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75989
                    if len(subjects) == 0:
                        pass
                        # 11: x*f
                        yield 11, subst2
                subjects.appendleft(tmp64)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 82600
            if len(subjects) >= 1:
                tmp67 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.3.1.0', tmp67)
                except ValueError:
                    pass
                else:
                    pass
                    # State 82601
                    if len(subjects) == 0:
                        pass
                        # 12: x*d
                        yield 12, subst2
                subjects.appendleft(tmp67)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 82794
            if len(subjects) >= 1:
                tmp70 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.4.1.0', tmp70)
                except ValueError:
                    pass
                else:
                    pass
                    # State 82795
                    if len(subjects) == 0:
                        pass
                        # 13: x*d
                        yield 13, subst2
                subjects.appendleft(tmp70)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 103699
            if len(subjects) >= 1:
                tmp73 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp73)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103700
                    if len(subjects) == 0:
                        pass
                        # 15: x*d
                        yield 15, subst2
                subjects.appendleft(tmp73)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 107637
            if len(subjects) >= 1:
                tmp76 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp76)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107638
                    if len(subjects) == 0:
                        pass
                        # 18: x*e
                        yield 18, subst2
                subjects.appendleft(tmp76)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 107851
            if len(subjects) >= 1:
                tmp79 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp79)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107852
                    if len(subjects) == 0:
                        pass
                        # 19: x*d
                        yield 19, subst2
                subjects.appendleft(tmp79)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp81 = subjects.popleft()
            associative1 = tmp81
            associative_type1 = type(tmp81)
            subjects82 = deque(tmp81._args)
            matcher = CommutativeMatcher57209.get()
            tmp83 = subjects82
            subjects82 = []
            for s in tmp83:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp83, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 57210
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 58408
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 64369
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 65749
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 68202
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 72103
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 74663
                    if len(subjects) == 0:
                        pass
                        # 6: b*x**n
                        yield 6, subst1
                if pattern_index == 7:
                    pass
                    # State 75581
                    if len(subjects) == 0:
                        pass
                        # 7: b*x**n
                        yield 7, subst1
                if pattern_index == 8:
                    pass
                    # State 75824
                    if len(subjects) == 0:
                        pass
                        # 8: v**2*c
                        yield 8, subst1
                if pattern_index == 9:
                    pass
                    # State 75826
                    if len(subjects) == 0:
                        pass
                        # 9: x*b
                        yield 9, subst1
                if pattern_index == 10:
                    pass
                    # State 75952
                    if len(subjects) == 0:
                        pass
                        # 10: x*f
                        yield 10, subst1
                if pattern_index == 11:
                    pass
                    # State 75990
                    if len(subjects) == 0:
                        pass
                        # 11: x*f
                        yield 11, subst1
                if pattern_index == 12:
                    pass
                    # State 82602
                    if len(subjects) == 0:
                        pass
                        # 12: x*d
                        yield 12, subst1
                if pattern_index == 13:
                    pass
                    # State 82796
                    if len(subjects) == 0:
                        pass
                        # 13: x*d
                        yield 13, subst1
                if pattern_index == 14:
                    pass
                    # State 100888
                    if len(subjects) == 0:
                        pass
                        # 14: x*b
                        yield 14, subst1
                if pattern_index == 15:
                    pass
                    # State 103701
                    if len(subjects) == 0:
                        pass
                        # 15: x*d
                        yield 15, subst1
                if pattern_index == 16:
                    pass
                    # State 105132
                    if len(subjects) == 0:
                        pass
                        # 16: b*log(c*x**n)
                        yield 16, subst1
                if pattern_index == 17:
                    pass
                    # State 107483
                    if len(subjects) == 0:
                        pass
                        # 17: b*(x*d + c)**n
                        yield 17, subst1
                if pattern_index == 18:
                    pass
                    # State 107639
                    if len(subjects) == 0:
                        pass
                        # 18: x*e
                        yield 18, subst1
                if pattern_index == 19:
                    pass
                    # State 107853
                    if len(subjects) == 0:
                        pass
                        # 19: x*d
                        yield 19, subst1
            subjects.appendleft(tmp81)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part006907 import *
from collections import deque
from .generated_part006904 import *
from .generated_part006906 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset