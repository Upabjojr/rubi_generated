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

class CommutativeMatcher132003(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.3.0_2', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
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
        if CommutativeMatcher132003._instance is None:
            CommutativeMatcher132003._instance = CommutativeMatcher132003()
        return CommutativeMatcher132003._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 132002
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132004
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132005
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132452
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132453
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132921
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132922
                    if len(subjects) == 0:
                        pass
                        # 2: x*e
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 137498
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137499
                    if len(subjects) == 0:
                        pass
                        # 3: x*d
                subjects.appendleft(tmp11)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp13 = subjects.popleft()
            associative1 = tmp13
            associative_type1 = type(tmp13)
            subjects14 = deque(tmp13._args)
            matcher = CommutativeMatcher132007.get()
            tmp15 = subjects14
            subjects14 = []
            for s in tmp15:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp15, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 132008
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                if pattern_index == 1:
                    pass
                    # State 132454
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                if pattern_index == 2:
                    pass
                    # State 132923
                    if len(subjects) == 0:
                        pass
                        # 2: x*e
                if pattern_index == 3:
                    pass
                    # State 137500
                    if len(subjects) == 0:
                        pass
                        # 3: x*d
            subjects.appendleft(tmp13)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
