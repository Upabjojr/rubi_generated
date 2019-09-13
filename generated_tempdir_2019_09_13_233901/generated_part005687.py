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

class CommutativeMatcher151248(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.3.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.3.2.0_1', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1, 0: 1}), [
      
]),
    3: (3, Multiset({2: 1, 1: 1}), [
      
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 1
    anonymous_patterns = {2}

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher151248._instance is None:
            CommutativeMatcher151248._instance = CommutativeMatcher151248()
        return CommutativeMatcher151248._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 151247
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 151249
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151250
                    if len(subjects) == 0:
                        pass
                        # 0: x*e
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 151267
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151268
                    if len(subjects) == 0:
                        pass
                        # 1: x*g
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp7 = subjects.popleft()
            associative1 = tmp7
            associative_type1 = type(tmp7)
            subjects8 = deque(tmp7._args)
            matcher = CommutativeMatcher151252.get()
            tmp9 = subjects8
            subjects8 = []
            for s in tmp9:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp9, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 151253
                    if len(subjects) == 0:
                        pass
                        # 0: x*e
                if pattern_index == 1:
                    pass
                    # State 151269
                    if len(subjects) == 0:
                        pass
                        # 1: x*g
            subjects.appendleft(tmp7)
        if len(subjects) >= 1 and subjects[0] == 1:
            tmp10 = subjects.popleft()
            # State 151425
            if len(subjects) == 0:
                pass
                # 2: 1
            subjects.appendleft(tmp10)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
