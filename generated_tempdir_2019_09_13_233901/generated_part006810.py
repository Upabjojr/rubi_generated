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

class CommutativeMatcher55440(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher55440._instance is None:
            CommutativeMatcher55440._instance = CommutativeMatcher55440()
        return CommutativeMatcher55440._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 55439
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 55441
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 55442
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 55443
                        if len(subjects3) >= 1 and subjects3[0] == 2:
                            tmp6 = subjects3.popleft()
                            # State 55444
                            if len(subjects3) == 0:
                                pass
                                # State 55445
                                if len(subjects) == 0:
                                    pass
                                    # 0: d*x**2
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                if len(subjects3) >= 1:
                    tmp7 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 55497
                        if len(subjects3) >= 1 and subjects3[0] == 2:
                            tmp9 = subjects3.popleft()
                            # State 55498
                            if len(subjects3) == 0:
                                pass
                                # State 55499
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**2*d
                            subjects3.appendleft(tmp9)
                    subjects3.appendleft(tmp7)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp10 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1', tmp10)
                except ValueError:
                    pass
                else:
                    pass
                    # State 56184
                    if len(subjects) == 0:
                        pass
                        # 3: x*b
                subjects.appendleft(tmp10)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 56164
            if len(subjects) >= 1:
                tmp13 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp13)
                except ValueError:
                    pass
                else:
                    pass
                    # State 56165
                    if len(subjects) == 0:
                        pass
                        # 2: v*b
                subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp15 = subjects.popleft()
            associative1 = tmp15
            associative_type1 = type(tmp15)
            subjects16 = deque(tmp15._args)
            matcher = CommutativeMatcher55447.get()
            tmp17 = subjects16
            subjects16 = []
            for s in tmp17:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp17, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 55452
                    if len(subjects) == 0:
                        pass
                        # 0: d*x**2
                if pattern_index == 1:
                    pass
                    # State 55503
                    if len(subjects) == 0:
                        pass
                        # 1: x**2*d
                if pattern_index == 2:
                    pass
                    # State 56166
                    if len(subjects) == 0:
                        pass
                        # 2: v*b
                if pattern_index == 3:
                    pass
                    # State 56185
                    if len(subjects) == 0:
                        pass
                        # 3: x*b
            subjects.appendleft(tmp15)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
