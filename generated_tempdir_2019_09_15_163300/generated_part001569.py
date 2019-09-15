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


class CommutativeMatcher47056(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i4.2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i4.2.2.0_1', 1, 1, S(0)), Add)
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
        if CommutativeMatcher47056._instance is None:
            CommutativeMatcher47056._instance = CommutativeMatcher47056()
        return CommutativeMatcher47056._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 47055
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 47057
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 47058
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 47075
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.2.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 47076
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst2
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp7 = subjects.popleft()
            associative1 = tmp7
            associative_type1 = type(tmp7)
            subjects8 = deque(tmp7._args)
            matcher = CommutativeMatcher47060.get()
            tmp9 = subjects8
            subjects8 = []
            for s in tmp9:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp9, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 47061
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 47077
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst1
            subjects.appendleft(tmp7)
        return
        yield


from .generated_part001570 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset