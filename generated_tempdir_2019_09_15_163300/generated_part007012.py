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


class CommutativeMatcher121761(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1, 4: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({5: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({4: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.3.0_2', 1, 1, S(0)), Add)
]),
    10: (10, Multiset({10: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    11: (11, Multiset({11: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    12: (12, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    13: (13, Multiset({13: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    14: (14, Multiset({14: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    15: (15, Multiset({13: 1}), [
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
        if CommutativeMatcher121761._instance is None:
            CommutativeMatcher121761._instance = CommutativeMatcher121761()
        return CommutativeMatcher121761._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 121760
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 121762
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 121763
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst2
                subjects.appendleft(tmp2)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 125390
                if len(subjects) >= 1:
                    tmp5 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1', tmp5)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125391
                        if len(subjects) == 0:
                            pass
                            # 2: x**n*b
                            yield 2, subst3
                    subjects.appendleft(tmp5)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp7 = subjects.popleft()
                subjects8 = deque(tmp7._args)
                # State 124538
                if len(subjects8) >= 1:
                    tmp9 = subjects8.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp9)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124539
                        if len(subjects8) >= 1:
                            tmp11 = subjects8.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp11)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124540
                                if len(subjects8) == 0:
                                    pass
                                    # State 124541
                                    if len(subjects) == 0:
                                        pass
                                        # 1: x**n*b
                                        yield 1, subst3
                            subjects8.appendleft(tmp11)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 125392
                            if len(subjects8) == 0:
                                pass
                                # State 125393
                                if len(subjects) == 0:
                                    pass
                                    # 2: x**n*b
                                    yield 2, subst3
                        if len(subjects8) >= 1:
                            tmp14 = subjects8.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp14)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125392
                                if len(subjects8) == 0:
                                    pass
                                    # State 125393
                                    if len(subjects) == 0:
                                        pass
                                        # 2: x**n*b
                                        yield 2, subst3
                            subjects8.appendleft(tmp14)
                    subjects8.appendleft(tmp9)
                if len(subjects8) >= 1:
                    tmp16 = subjects8.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp16)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125740
                        if len(subjects8) >= 1 and subjects8[0] == Integer(2):
                            tmp18 = subjects8.popleft()
                            # State 125741
                            if len(subjects8) == 0:
                                pass
                                # State 125742
                                if len(subjects) == 0:
                                    pass
                                    # 3: x**2*c
                                    yield 3, subst2
                            subjects8.appendleft(tmp18)
                    subjects8.appendleft(tmp16)
                if len(subjects8) >= 1 and isinstance(subjects8[0], Add):
                    tmp19 = subjects8.popleft()
                    associative1 = tmp19
                    associative_type1 = type(tmp19)
                    subjects20 = deque(tmp19._args)
                    matcher = CommutativeMatcher136997.get()
                    tmp21 = subjects20
                    subjects20 = []
                    for s in tmp21:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp21, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 137003
                            if len(subjects8) >= 1:
                                tmp22 = []
                                tmp22.append(subjects8.popleft())
                                while True:
                                    if len(tmp22) > 1:
                                        tmp23 = create_operation_expression(associative1, tmp22)
                                    elif len(tmp22) == 1:
                                        tmp23 = tmp22[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.1.2', tmp23)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 137004
                                        if len(subjects8) == 0:
                                            pass
                                            # State 137005
                                            if len(subjects) == 0:
                                                pass
                                                # 11: b*(x*d + c)**n
                                                yield 11, subst3
                                    if len(subjects8) == 0:
                                        break
                                    tmp22.append(subjects8.popleft())
                                subjects8.extendleft(reversed(tmp22))
                    subjects8.appendleft(tmp19)
                subjects.appendleft(tmp7)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp25 = subjects.popleft()
                subjects26 = deque(tmp25._args)
                # State 134118
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 134119
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 134120
                        if len(subjects26) >= 1:
                            tmp29 = subjects26.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1', tmp29)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 134121
                                if len(subjects26) == 0:
                                    pass
                                    # State 134122
                                    if len(subjects) == 0:
                                        pass
                                        # 10: b*log(x**n*c)
                                        yield 10, subst4
                            subjects26.appendleft(tmp29)
                    if len(subjects26) >= 1 and isinstance(subjects26[0], Pow):
                        tmp31 = subjects26.popleft()
                        subjects32 = deque(tmp31._args)
                        # State 134123
                        if len(subjects32) >= 1:
                            tmp33 = subjects32.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1', tmp33)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 134124
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 134125
                                    if len(subjects32) == 0:
                                        pass
                                        # State 134126
                                        if len(subjects26) == 0:
                                            pass
                                            # State 134127
                                            if len(subjects) == 0:
                                                pass
                                                # 10: b*log(x**n*c)
                                                yield 10, subst4
                                if len(subjects32) >= 1:
                                    tmp36 = subjects32.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.1.2.2', tmp36)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 134125
                                        if len(subjects32) == 0:
                                            pass
                                            # State 134126
                                            if len(subjects26) == 0:
                                                pass
                                                # State 134127
                                                if len(subjects) == 0:
                                                    pass
                                                    # 10: b*log(x**n*c)
                                                    yield 10, subst4
                                    subjects32.appendleft(tmp36)
                            subjects32.appendleft(tmp33)
                        subjects26.appendleft(tmp31)
                if len(subjects26) >= 1 and isinstance(subjects26[0], Mul):
                    tmp38 = subjects26.popleft()
                    associative1 = tmp38
                    associative_type1 = type(tmp38)
                    subjects39 = deque(tmp38._args)
                    matcher = CommutativeMatcher134129.get()
                    tmp40 = subjects39
                    subjects39 = []
                    for s in tmp40:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp40, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 134136
                            if len(subjects26) == 0:
                                pass
                                # State 134137
                                if len(subjects) == 0:
                                    pass
                                    # 10: b*log(x**n*c)
                                    yield 10, subst2
                    subjects26.appendleft(tmp38)
                subjects.appendleft(tmp25)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 125747
            if len(subjects) >= 1:
                tmp42 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp42)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125748
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                        yield 4, subst2
                subjects.appendleft(tmp42)
            if len(subjects) >= 1:
                tmp44 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1.0', tmp44)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132549
                    if len(subjects) == 0:
                        pass
                        # 7: e*x
                        yield 7, subst2
                subjects.appendleft(tmp44)
            if len(subjects) >= 1:
                tmp46 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp46)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137537
                    if len(subjects) == 0:
                        pass
                        # 14: x*e
                        yield 14, subst2
                subjects.appendleft(tmp46)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132208
            if len(subjects) >= 1:
                tmp49 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp49)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132209
                    if len(subjects) == 0:
                        pass
                        # 5: x*b
                        yield 5, subst2
                subjects.appendleft(tmp49)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132371
            if len(subjects) >= 1:
                tmp52 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp52)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132372
                    if len(subjects) == 0:
                        pass
                        # 6: x*f
                        yield 6, subst2
                subjects.appendleft(tmp52)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132772
            if len(subjects) >= 1:
                tmp55 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp55)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132773
                    if len(subjects) == 0:
                        pass
                        # 8: x*d
                        yield 8, subst2
                subjects.appendleft(tmp55)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132938
            if len(subjects) >= 1:
                tmp58 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp58)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132939
                    if len(subjects) == 0:
                        pass
                        # 9: x*e
                        yield 9, subst2
                subjects.appendleft(tmp58)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 137383
            if len(subjects) >= 1:
                tmp61 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp61)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137384
                    if len(subjects) == 0:
                        pass
                        # 12: x*e
                        yield 12, subst2
                subjects.appendleft(tmp61)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 137512
            if len(subjects) >= 1:
                tmp64 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp64)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137513
                    if len(subjects) == 0:
                        pass
                        # 13: x*d
                        yield 13, subst2
                subjects.appendleft(tmp64)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp66 = subjects.popleft()
            associative1 = tmp66
            associative_type1 = type(tmp66)
            subjects67 = deque(tmp66._args)
            matcher = CommutativeMatcher121765.get()
            tmp68 = subjects67
            subjects67 = []
            for s in tmp68:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp68, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 121766
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 124546
                    if len(subjects) == 0:
                        pass
                        # 1: x**n*b
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 125398
                    if len(subjects) == 0:
                        pass
                        # 2: x**n*b
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 125746
                    if len(subjects) == 0:
                        pass
                        # 3: x**2*c
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 125749
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 132210
                    if len(subjects) == 0:
                        pass
                        # 5: x*b
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 132373
                    if len(subjects) == 0:
                        pass
                        # 6: x*f
                        yield 6, subst1
                if pattern_index == 7:
                    pass
                    # State 132550
                    if len(subjects) == 0:
                        pass
                        # 7: e*x
                        yield 7, subst1
                if pattern_index == 8:
                    pass
                    # State 132774
                    if len(subjects) == 0:
                        pass
                        # 8: x*d
                        yield 8, subst1
                if pattern_index == 9:
                    pass
                    # State 132940
                    if len(subjects) == 0:
                        pass
                        # 9: x*e
                        yield 9, subst1
                if pattern_index == 10:
                    pass
                    # State 134158
                    if len(subjects) == 0:
                        pass
                        # 10: b*log(x**n*c)
                        yield 10, subst1
                if pattern_index == 11:
                    pass
                    # State 137016
                    if len(subjects) == 0:
                        pass
                        # 11: b*(x*d + c)**n
                        yield 11, subst1
                if pattern_index == 12:
                    pass
                    # State 137385
                    if len(subjects) == 0:
                        pass
                        # 12: x*e
                        yield 12, subst1
                if pattern_index == 13:
                    pass
                    # State 137514
                    if len(subjects) == 0:
                        pass
                        # 13: x*d
                        yield 13, subst1
                if pattern_index == 14:
                    pass
                    # State 137538
                    if len(subjects) == 0:
                        pass
                        # 14: x*e
                        yield 14, subst1
            subjects.appendleft(tmp66)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part007016 import *
from collections import deque
from multiset import Multiset
from matchpy.utils import VariableWithCount
from .generated_part007013 import *
from .generated_part007015 import *