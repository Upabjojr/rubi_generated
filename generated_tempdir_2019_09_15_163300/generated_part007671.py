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


class CommutativeMatcher55412(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher55412._instance is None:
            CommutativeMatcher55412._instance = CommutativeMatcher55412()
        return CommutativeMatcher55412._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 55411
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 55413
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 55414
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 55481
                    if len(subjects) == 0:
                        pass
                        # 1: b*x
                        yield 1, subst2
                subjects.appendleft(tmp4)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp6 = subjects.popleft()
            associative1 = tmp6
            associative_type1 = type(tmp6)
            subjects7 = deque(tmp6._args)
            matcher = CommutativeMatcher55416.get()
            tmp8 = subjects7
            subjects7 = []
            for s in tmp8:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp8, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 55417
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 55482
                    if len(subjects) == 0:
                        pass
                        # 1: b*x
                        yield 1, subst1
            subjects.appendleft(tmp6)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part007672 import *