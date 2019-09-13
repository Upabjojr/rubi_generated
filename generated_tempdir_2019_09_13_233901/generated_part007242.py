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

class CommutativeMatcher24969(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.1.1.2.2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.2.2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.2.2.2.0', 1, 1, None), Add)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.1.1.2.2.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher24969._instance is None:
            CommutativeMatcher24969._instance = CommutativeMatcher24969()
        return CommutativeMatcher24969._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 24968
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 24970
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 24971
                    if len(subjects) == 0:
                        pass
                        # 0: f*x
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
                    # State 26981
                    if len(subjects) == 0:
                        pass
                        # 1: f*x
                subjects.appendleft(tmp4)
            if len(subjects) >= 1:
                tmp6 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 28048
                    if len(subjects) == 0:
                        pass
                        # 2: f*x
                subjects.appendleft(tmp6)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp8 = subjects.popleft()
            associative1 = tmp8
            associative_type1 = type(tmp8)
            subjects9 = deque(tmp8._args)
            matcher = CommutativeMatcher24973.get()
            tmp10 = subjects9
            subjects9 = []
            for s in tmp10:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp10, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 24974
                    if len(subjects) == 0:
                        pass
                        # 0: f*x
                if pattern_index == 1:
                    pass
                    # State 26982
                    if len(subjects) == 0:
                        pass
                        # 1: f*x
                if pattern_index == 2:
                    pass
                    # State 28049
                    if len(subjects) == 0:
                        pass
                        # 2: f*x
            subjects.appendleft(tmp8)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
