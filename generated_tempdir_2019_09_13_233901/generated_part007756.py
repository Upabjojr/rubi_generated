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

class CommutativeMatcher78118(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1, 4: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({5: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
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
        if CommutativeMatcher78118._instance is None:
            CommutativeMatcher78118._instance = CommutativeMatcher78118()
        return CommutativeMatcher78118._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 78117
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 78119
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 78120
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 81729
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.3.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 81730
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 86675
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 86676
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 89492
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp11 = subjects.popleft()
                subjects12 = deque(tmp11._args)
                # State 89493
                if len(subjects12) >= 1:
                    tmp13 = subjects12.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.0', tmp13)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89494
                        if len(subjects12) >= 1 and subjects12[0] == 2:
                            tmp15 = subjects12.popleft()
                            # State 89495
                            if len(subjects12) == 0:
                                pass
                                # State 89496
                                if len(subjects) == 0:
                                    pass
                                    # 3: x**2*c
                            subjects12.appendleft(tmp15)
                    subjects12.appendleft(tmp13)
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 89502
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.0', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 89503
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                subjects.appendleft(tmp17)
            if len(subjects) >= 1:
                tmp19 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp19)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107895
                    if len(subjects) == 0:
                        pass
                        # 5: x*d
                subjects.appendleft(tmp19)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp21 = subjects.popleft()
            associative1 = tmp21
            associative_type1 = type(tmp21)
            subjects22 = deque(tmp21._args)
            matcher = CommutativeMatcher78122.get()
            tmp23 = subjects22
            subjects22 = []
            for s in tmp23:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp23, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 78123
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 81731
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                if pattern_index == 2:
                    pass
                    # State 86677
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                if pattern_index == 3:
                    pass
                    # State 89501
                    if len(subjects) == 0:
                        pass
                        # 3: x**2*c
                if pattern_index == 4:
                    pass
                    # State 89504
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                if pattern_index == 5:
                    pass
                    # State 107896
                    if len(subjects) == 0:
                        pass
                        # 5: x*d
            subjects.appendleft(tmp21)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
