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

class CommutativeMatcher59347(CommutativeMatcher):
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
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.4.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1, 7: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({8: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({9: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({10: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
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
        if CommutativeMatcher59347._instance is None:
            CommutativeMatcher59347._instance = CommutativeMatcher59347()
        return CommutativeMatcher59347._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 59346
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 59348
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 59349
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
            # State 68439
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 68440
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
            # State 71204
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 71205
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 76087
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 76088
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 86470
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.4.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 86471
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 89145
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.4.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 89146
                if len(subjects) >= 1:
                    tmp18 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.4.1.1', tmp18)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89147
                        if len(subjects) == 0:
                            pass
                            # 5: b*x**n
                    subjects.appendleft(tmp18)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp20 = subjects.popleft()
                subjects21 = deque(tmp20._args)
                # State 89148
                if len(subjects21) >= 1:
                    tmp22 = subjects21.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.1', tmp22)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89149
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 89150
                            if len(subjects21) == 0:
                                pass
                                # State 89151
                                if len(subjects) == 0:
                                    pass
                                    # 5: b*x**n
                        if len(subjects21) >= 1:
                            tmp25 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.2', tmp25)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 89150
                                if len(subjects21) == 0:
                                    pass
                                    # State 89151
                                    if len(subjects) == 0:
                                        pass
                                        # 5: b*x**n
                            subjects21.appendleft(tmp25)
                    subjects21.appendleft(tmp22)
                subjects.appendleft(tmp20)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 89533
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp28 = subjects.popleft()
                subjects29 = deque(tmp28._args)
                # State 89534
                if len(subjects29) >= 1:
                    tmp30 = subjects29.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp30)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89535
                        if len(subjects29) >= 1 and subjects29[0] == 2:
                            tmp32 = subjects29.popleft()
                            # State 89536
                            if len(subjects29) == 0:
                                pass
                                # State 89537
                                if len(subjects) == 0:
                                    pass
                                    # 6: v**2*c
                            subjects29.appendleft(tmp32)
                    subjects29.appendleft(tmp30)
                subjects.appendleft(tmp28)
            if len(subjects) >= 1:
                tmp33 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp33)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103588
                    if len(subjects) == 0:
                        pass
                        # 9: x*f
                subjects.appendleft(tmp33)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 89542
            if len(subjects) >= 1:
                tmp36 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp36)
                except ValueError:
                    pass
                else:
                    pass
                    # State 89543
                    if len(subjects) == 0:
                        pass
                        # 7: x*b
                subjects.appendleft(tmp36)
            if len(subjects) >= 1:
                tmp38 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1.0', tmp38)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103919
                    if len(subjects) == 0:
                        pass
                        # 10: e*x
                subjects.appendleft(tmp38)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 103531
            if len(subjects) >= 1:
                tmp41 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp41)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103532
                    if len(subjects) == 0:
                        pass
                        # 8: x*f
                subjects.appendleft(tmp41)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp43 = subjects.popleft()
            associative1 = tmp43
            associative_type1 = type(tmp43)
            subjects44 = deque(tmp43._args)
            matcher = CommutativeMatcher59351.get()
            tmp45 = subjects44
            subjects44 = []
            for s in tmp45:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp45, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 59352
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                if pattern_index == 1:
                    pass
                    # State 68441
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                if pattern_index == 2:
                    pass
                    # State 71206
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                if pattern_index == 3:
                    pass
                    # State 76089
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                if pattern_index == 4:
                    pass
                    # State 86472
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                if pattern_index == 5:
                    pass
                    # State 89158
                    if len(subjects) == 0:
                        pass
                        # 5: b*x**n
                if pattern_index == 6:
                    pass
                    # State 89541
                    if len(subjects) == 0:
                        pass
                        # 6: v**2*c
                if pattern_index == 7:
                    pass
                    # State 89544
                    if len(subjects) == 0:
                        pass
                        # 7: x*b
                if pattern_index == 8:
                    pass
                    # State 103533
                    if len(subjects) == 0:
                        pass
                        # 8: x*f
                if pattern_index == 9:
                    pass
                    # State 103589
                    if len(subjects) == 0:
                        pass
                        # 9: x*f
                if pattern_index == 10:
                    pass
                    # State 103920
                    if len(subjects) == 0:
                        pass
                        # 10: e*x
            subjects.appendleft(tmp43)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
