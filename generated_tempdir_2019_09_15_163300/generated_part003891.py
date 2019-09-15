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


class CommutativeMatcher24351(CommutativeMatcher):
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
        if CommutativeMatcher24351._instance is None:
            CommutativeMatcher24351._instance = CommutativeMatcher24351()
        return CommutativeMatcher24351._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 24350
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 24352
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 24353
                    if len(subjects) == 0:
                        pass
                        # 0: f*x
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
                    # State 26671
                    if len(subjects) == 0:
                        pass
                        # 1: f*x
                        yield 1, subst2
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
                    # State 27738
                    if len(subjects) == 0:
                        pass
                        # 2: f*x
                        yield 2, subst2
                subjects.appendleft(tmp6)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp8 = subjects.popleft()
            associative1 = tmp8
            associative_type1 = type(tmp8)
            subjects9 = deque(tmp8._args)
            matcher = CommutativeMatcher24355.get()
            tmp10 = subjects9
            subjects9 = []
            for s in tmp10:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp10, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 24356
                    if len(subjects) == 0:
                        pass
                        # 0: f*x
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 26672
                    if len(subjects) == 0:
                        pass
                        # 1: f*x
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 27739
                    if len(subjects) == 0:
                        pass
                        # 2: f*x
                        yield 2, subst1
            subjects.appendleft(tmp8)
        return
        yield


from .generated_part003892 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset