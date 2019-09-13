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

class CommutativeMatcher59369(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.4.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({9: 1, 10: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    10: (10, Multiset({11: 1, 12: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    11: (11, Multiset({13: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    12: (12, Multiset({14: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    13: (13, Multiset({15: 1}), [
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
        if CommutativeMatcher59369._instance is None:
            CommutativeMatcher59369._instance = CommutativeMatcher59369()
        return CommutativeMatcher59369._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 59368
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 59370
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 59371
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 68456
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 68457
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 68643
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 68644
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 75915
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75916
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                subjects.appendleft(tmp11)
            if len(subjects) >= 1:
                tmp13 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1', tmp13)
                except ValueError:
                    pass
                else:
                    pass
                    # State 89517
                    if len(subjects) == 0:
                        pass
                        # 10: b*x
                subjects.appendleft(tmp13)
            if len(subjects) >= 1:
                tmp15 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp15)
                except ValueError:
                    pass
                else:
                    pass
                    # State 89554
                    if len(subjects) == 0:
                        pass
                        # 12: x*b
                subjects.appendleft(tmp15)
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1.0', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103935
                    if len(subjects) == 0:
                        pass
                        # 14: e*x
                subjects.appendleft(tmp17)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 76104
            if len(subjects) >= 1:
                tmp20 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp20)
                except ValueError:
                    pass
                else:
                    pass
                    # State 76105
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                subjects.appendleft(tmp20)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 86487
            if len(subjects) >= 1:
                tmp23 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.4.1.0', tmp23)
                except ValueError:
                    pass
                else:
                    pass
                    # State 86488
                    if len(subjects) == 0:
                        pass
                        # 5: x*d
                subjects.appendleft(tmp23)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 86692
            if len(subjects) >= 1:
                tmp26 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp26)
                except ValueError:
                    pass
                else:
                    pass
                    # State 86693
                    if len(subjects) == 0:
                        pass
                        # 6: x*f
                subjects.appendleft(tmp26)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp28 = subjects.popleft()
                subjects29 = deque(tmp28._args)
                # State 88422
                if len(subjects29) >= 1:
                    tmp30 = subjects29.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp30)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88423
                        if len(subjects29) >= 1:
                            tmp32 = subjects29.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp32)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 88424
                                if len(subjects29) == 0:
                                    pass
                                    # State 88425
                                    if len(subjects) == 0:
                                        pass
                                        # 7: x**n*d
                            subjects29.appendleft(tmp32)
                    subjects29.appendleft(tmp30)
                if len(subjects29) >= 1:
                    tmp34 = subjects29.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.1', tmp34)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89510
                        if len(subjects29) >= 1 and subjects29[0] == 2:
                            tmp36 = subjects29.popleft()
                            # State 89511
                            if len(subjects29) == 0:
                                pass
                                # State 89512
                                if len(subjects) == 0:
                                    pass
                                    # 9: c*x**2
                            subjects29.appendleft(tmp36)
                    subjects29.appendleft(tmp34)
                if len(subjects29) >= 1:
                    tmp37 = subjects29.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp37)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89547
                        if len(subjects29) >= 1 and subjects29[0] == 2:
                            tmp39 = subjects29.popleft()
                            # State 89548
                            if len(subjects29) == 0:
                                pass
                                # State 89549
                                if len(subjects) == 0:
                                    pass
                                    # 11: v**2*c
                            subjects29.appendleft(tmp39)
                    subjects29.appendleft(tmp37)
                subjects.appendleft(tmp28)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 89187
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.4.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 89188
                if len(subjects) >= 1:
                    tmp42 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.4.1.1', tmp42)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89189
                        if len(subjects) == 0:
                            pass
                            # 8: b*x**n
                    subjects.appendleft(tmp42)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp44 = subjects.popleft()
                subjects45 = deque(tmp44._args)
                # State 89190
                if len(subjects45) >= 1:
                    tmp46 = subjects45.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.1', tmp46)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89191
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 89192
                            if len(subjects45) == 0:
                                pass
                                # State 89193
                                if len(subjects) == 0:
                                    pass
                                    # 8: b*x**n
                        if len(subjects45) >= 1:
                            tmp49 = subjects45.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.2', tmp49)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 89192
                                if len(subjects45) == 0:
                                    pass
                                    # State 89193
                                    if len(subjects) == 0:
                                        pass
                                        # 8: b*x**n
                            subjects45.appendleft(tmp49)
                    subjects45.appendleft(tmp46)
                subjects.appendleft(tmp44)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 103545
            if len(subjects) >= 1:
                tmp52 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp52)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103546
                    if len(subjects) == 0:
                        pass
                        # 13: x*f
                subjects.appendleft(tmp52)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 107904
            if len(subjects) >= 1:
                tmp55 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp55)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107905
                    if len(subjects) == 0:
                        pass
                        # 15: x*d
                subjects.appendleft(tmp55)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp57 = subjects.popleft()
            associative1 = tmp57
            associative_type1 = type(tmp57)
            subjects58 = deque(tmp57._args)
            matcher = CommutativeMatcher59373.get()
            tmp59 = subjects58
            subjects58 = []
            for s in tmp59:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp59, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 59374
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                if pattern_index == 1:
                    pass
                    # State 68458
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                if pattern_index == 2:
                    pass
                    # State 68645
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                if pattern_index == 3:
                    pass
                    # State 75917
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                if pattern_index == 4:
                    pass
                    # State 76106
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                if pattern_index == 5:
                    pass
                    # State 86489
                    if len(subjects) == 0:
                        pass
                        # 5: x*d
                if pattern_index == 6:
                    pass
                    # State 86694
                    if len(subjects) == 0:
                        pass
                        # 6: x*f
                if pattern_index == 7:
                    pass
                    # State 88430
                    if len(subjects) == 0:
                        pass
                        # 7: x**n*d
                if pattern_index == 8:
                    pass
                    # State 89199
                    if len(subjects) == 0:
                        pass
                        # 8: b*x**n
                if pattern_index == 9:
                    pass
                    # State 89516
                    if len(subjects) == 0:
                        pass
                        # 9: c*x**2
                if pattern_index == 10:
                    pass
                    # State 89518
                    if len(subjects) == 0:
                        pass
                        # 10: b*x
                if pattern_index == 11:
                    pass
                    # State 89553
                    if len(subjects) == 0:
                        pass
                        # 11: v**2*c
                if pattern_index == 12:
                    pass
                    # State 89555
                    if len(subjects) == 0:
                        pass
                        # 12: x*b
                if pattern_index == 13:
                    pass
                    # State 103547
                    if len(subjects) == 0:
                        pass
                        # 13: x*f
                if pattern_index == 14:
                    pass
                    # State 103936
                    if len(subjects) == 0:
                        pass
                        # 14: e*x
                if pattern_index == 15:
                    pass
                    # State 107906
                    if len(subjects) == 0:
                        pass
                        # 15: x*d
            subjects.appendleft(tmp57)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
