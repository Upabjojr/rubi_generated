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

class CommutativeMatcher48077(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.2.2.0_1', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.2.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.2.2.0_1', 1, 1, S(0)), Add)
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
        if CommutativeMatcher48077._instance is None:
            CommutativeMatcher48077._instance = CommutativeMatcher48077()
        return CommutativeMatcher48077._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 48076
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 48078
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 48079
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 48856
                    if len(subjects) == 0:
                        pass
                        # 2: x*b
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 48096
            if len(subjects) >= 1:
                tmp7 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 48097
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                subjects.appendleft(tmp7)
            if len(subjects) >= 1:
                tmp9 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp9)
                except ValueError:
                    pass
                else:
                    pass
                    # State 48867
                    if len(subjects) == 0:
                        pass
                        # 3: x*d
                subjects.appendleft(tmp9)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp11 = subjects.popleft()
            associative1 = tmp11
            associative_type1 = type(tmp11)
            subjects12 = deque(tmp11._args)
            matcher = CommutativeMatcher48081.get()
            tmp13 = subjects12
            subjects12 = []
            for s in tmp13:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp13, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 48082
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                if pattern_index == 1:
                    pass
                    # State 48098
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                if pattern_index == 2:
                    pass
                    # State 48857
                    if len(subjects) == 0:
                        pass
                        # 2: x*b
                if pattern_index == 3:
                    pass
                    # State 48868
                    if len(subjects) == 0:
                        pass
                        # 3: x*d
            subjects.appendleft(tmp11)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
