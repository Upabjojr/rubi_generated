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


class CommutativeMatcher47829(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.3.2.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher47829._instance is None:
            CommutativeMatcher47829._instance = CommutativeMatcher47829()
        return CommutativeMatcher47829._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 47828
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 47830
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 47831
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst2
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
                    # State 48647
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                        yield 1, subst2
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 49091
            if len(subjects) >= 1:
                tmp7 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 49092
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                        yield 2, subst2
                subjects.appendleft(tmp7)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp9 = subjects.popleft()
            associative1 = tmp9
            associative_type1 = type(tmp9)
            subjects10 = deque(tmp9._args)
            matcher = CommutativeMatcher47833.get()
            tmp11 = subjects10
            subjects10 = []
            for s in tmp11:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp11, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 47834
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 48648
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 49093
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                        yield 2, subst1
            subjects.appendleft(tmp9)
        return
        yield


from .generated_part006744 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset