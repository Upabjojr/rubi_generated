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

class CommutativeMatcher101528(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
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
        if CommutativeMatcher101528._instance is None:
            CommutativeMatcher101528._instance = CommutativeMatcher101528()
        return CommutativeMatcher101528._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 101527
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 101529
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 101530
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 103809
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103810
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                subjects.appendleft(tmp5)
            if len(subjects) >= 1:
                tmp7 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1.0', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 104105
                    if len(subjects) == 0:
                        pass
                        # 2: e*x
                subjects.appendleft(tmp7)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp9 = subjects.popleft()
            associative1 = tmp9
            associative_type1 = type(tmp9)
            subjects10 = deque(tmp9._args)
            matcher = CommutativeMatcher101532.get()
            tmp11 = subjects10
            subjects10 = []
            for s in tmp11:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp11, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 101533
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                if pattern_index == 1:
                    pass
                    # State 103811
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                if pattern_index == 2:
                    pass
                    # State 104106
                    if len(subjects) == 0:
                        pass
                        # 2: e*x
            subjects.appendleft(tmp9)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
