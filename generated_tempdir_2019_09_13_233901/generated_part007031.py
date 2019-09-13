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

class CommutativeMatcher121788(CommutativeMatcher):
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
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({4: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
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
    14: (14, Multiset({13: 1}), [
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
        if CommutativeMatcher121788._instance is None:
            CommutativeMatcher121788._instance = CommutativeMatcher121788()
        return CommutativeMatcher121788._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 121787
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 121789
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 121790
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                subjects.appendleft(tmp2)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 125499
                if len(subjects) >= 1:
                    tmp5 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.1', tmp5)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125500
                        if len(subjects) == 0:
                            pass
                            # 2: b*x**n
                    subjects.appendleft(tmp5)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp7 = subjects.popleft()
                subjects8 = deque(tmp7._args)
                # State 124569
                if len(subjects8) >= 1:
                    tmp9 = subjects8.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.1', tmp9)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124570
                        if len(subjects8) >= 1:
                            tmp11 = subjects8.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp11)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124571
                                if len(subjects8) == 0:
                                    pass
                                    # State 124572
                                    if len(subjects) == 0:
                                        pass
                                        # 1: b*x**n
                            subjects8.appendleft(tmp11)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 125501
                            if len(subjects8) == 0:
                                pass
                                # State 125502
                                if len(subjects) == 0:
                                    pass
                                    # 2: b*x**n
                        if len(subjects8) >= 1:
                            tmp14 = subjects8.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp14)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125501
                                if len(subjects8) == 0:
                                    pass
                                    # State 125502
                                    if len(subjects) == 0:
                                        pass
                                        # 2: b*x**n
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
                        # State 125757
                        if len(subjects8) >= 1 and subjects8[0] == 2:
                            tmp18 = subjects8.popleft()
                            # State 125758
                            if len(subjects8) == 0:
                                pass
                                # State 125759
                                if len(subjects) == 0:
                                    pass
                                    # 3: x**2*c
                            subjects8.appendleft(tmp18)
                    subjects8.appendleft(tmp16)
                if len(subjects8) >= 1 and isinstance(subjects8[0], Add):
                    tmp19 = subjects8.popleft()
                    associative1 = tmp19
                    associative_type1 = type(tmp19)
                    subjects20 = deque(tmp19._args)
                    matcher = CommutativeMatcher137098.get()
                    tmp21 = subjects20
                    subjects20 = []
                    for s in tmp21:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp21, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 137104
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
                                        # State 137105
                                        if len(subjects8) == 0:
                                            pass
                                            # State 137106
                                            if len(subjects) == 0:
                                                pass
                                                # 11: b*(x*d + c)**n
                                    if len(subjects8) == 0:
                                        break
                                    tmp22.append(subjects8.popleft())
                                subjects8.extendleft(reversed(tmp22))
                    subjects8.appendleft(tmp19)
                subjects.appendleft(tmp7)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp25 = subjects.popleft()
                subjects26 = deque(tmp25._args)
                # State 134219
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 134220
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 134221
                        if len(subjects26) >= 1:
                            tmp29 = subjects26.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.1.2.1', tmp29)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 134222
                                if len(subjects26) == 0:
                                    pass
                                    # State 134223
                                    if len(subjects) == 0:
                                        pass
                                        # 10: b*log(c*x**n)
                            subjects26.appendleft(tmp29)
                    if len(subjects26) >= 1 and isinstance(subjects26[0], Pow):
                        tmp31 = subjects26.popleft()
                        subjects32 = deque(tmp31._args)
                        # State 134224
                        if len(subjects32) >= 1:
                            tmp33 = subjects32.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2.1', tmp33)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 134225
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 134226
                                    if len(subjects32) == 0:
                                        pass
                                        # State 134227
                                        if len(subjects26) == 0:
                                            pass
                                            # State 134228
                                            if len(subjects) == 0:
                                                pass
                                                # 10: b*log(c*x**n)
                                if len(subjects32) >= 1:
                                    tmp36 = subjects32.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.1.2.2', tmp36)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 134226
                                        if len(subjects32) == 0:
                                            pass
                                            # State 134227
                                            if len(subjects26) == 0:
                                                pass
                                                # State 134228
                                                if len(subjects) == 0:
                                                    pass
                                                    # 10: b*log(c*x**n)
                                    subjects32.appendleft(tmp36)
                            subjects32.appendleft(tmp33)
                        subjects26.appendleft(tmp31)
                if len(subjects26) >= 1 and isinstance(subjects26[0], Mul):
                    tmp38 = subjects26.popleft()
                    associative1 = tmp38
                    associative_type1 = type(tmp38)
                    subjects39 = deque(tmp38._args)
                    matcher = CommutativeMatcher134230.get()
                    tmp40 = subjects39
                    subjects39 = []
                    for s in tmp40:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp40, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 134237
                            if len(subjects26) == 0:
                                pass
                                # State 134238
                                if len(subjects) == 0:
                                    pass
                                    # 10: b*log(c*x**n)
                    subjects26.appendleft(tmp38)
                subjects.appendleft(tmp25)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 125764
            if len(subjects) >= 1:
                tmp42 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp42)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125765
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                subjects.appendleft(tmp42)
            if len(subjects) >= 1:
                tmp44 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp44)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132567
                    if len(subjects) == 0:
                        pass
                        # 8: x*e
                subjects.appendleft(tmp44)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132111
            if len(subjects) >= 1:
                tmp47 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp47)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132112
                    if len(subjects) == 0:
                        pass
                        # 5: x*b
                subjects.appendleft(tmp47)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132349
            if len(subjects) >= 1:
                tmp50 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp50)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132350
                    if len(subjects) == 0:
                        pass
                        # 6: x*b
                subjects.appendleft(tmp50)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132393
            if len(subjects) >= 1:
                tmp53 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp53)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132394
                    if len(subjects) == 0:
                        pass
                        # 7: x*f
                subjects.appendleft(tmp53)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132737
            if len(subjects) >= 1:
                tmp56 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp56)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132738
                    if len(subjects) == 0:
                        pass
                        # 9: x*d
                subjects.appendleft(tmp56)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 137298
            if len(subjects) >= 1:
                tmp59 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp59)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137299
                    if len(subjects) == 0:
                        pass
                        # 12: x*e
                subjects.appendleft(tmp59)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 137565
            if len(subjects) >= 1:
                tmp62 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp62)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137566
                    if len(subjects) == 0:
                        pass
                        # 13: x*d
                subjects.appendleft(tmp62)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp64 = subjects.popleft()
            associative1 = tmp64
            associative_type1 = type(tmp64)
            subjects65 = deque(tmp64._args)
            matcher = CommutativeMatcher121792.get()
            tmp66 = subjects65
            subjects65 = []
            for s in tmp66:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp66, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 121793
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                if pattern_index == 1:
                    pass
                    # State 124577
                    if len(subjects) == 0:
                        pass
                        # 1: b*x**n
                if pattern_index == 2:
                    pass
                    # State 125507
                    if len(subjects) == 0:
                        pass
                        # 2: b*x**n
                if pattern_index == 3:
                    pass
                    # State 125763
                    if len(subjects) == 0:
                        pass
                        # 3: x**2*c
                if pattern_index == 4:
                    pass
                    # State 125766
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                if pattern_index == 5:
                    pass
                    # State 132113
                    if len(subjects) == 0:
                        pass
                        # 5: x*b
                if pattern_index == 6:
                    pass
                    # State 132351
                    if len(subjects) == 0:
                        pass
                        # 6: x*b
                if pattern_index == 7:
                    pass
                    # State 132395
                    if len(subjects) == 0:
                        pass
                        # 7: x*f
                if pattern_index == 8:
                    pass
                    # State 132568
                    if len(subjects) == 0:
                        pass
                        # 8: x*e
                if pattern_index == 9:
                    pass
                    # State 132739
                    if len(subjects) == 0:
                        pass
                        # 9: x*d
                if pattern_index == 10:
                    pass
                    # State 134259
                    if len(subjects) == 0:
                        pass
                        # 10: b*log(c*x**n)
                if pattern_index == 11:
                    pass
                    # State 137117
                    if len(subjects) == 0:
                        pass
                        # 11: b*(x*d + c)**n
                if pattern_index == 12:
                    pass
                    # State 137300
                    if len(subjects) == 0:
                        pass
                        # 12: x*e
                if pattern_index == 13:
                    pass
                    # State 137567
                    if len(subjects) == 0:
                        pass
                        # 13: x*d
            subjects.appendleft(tmp64)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
