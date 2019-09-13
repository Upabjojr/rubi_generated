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

class CommutativeMatcher46835(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.3.2.2.0_1', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.3.2.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.3.2.2.0_1', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.3.2.2.0_1', 1, 1, S(0)), Add)
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
        if CommutativeMatcher46835._instance is None:
            CommutativeMatcher46835._instance = CommutativeMatcher46835()
        return CommutativeMatcher46835._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 46834
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 46836
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 46837
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 47671
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                subjects.appendleft(tmp4)
            if len(subjects) >= 1:
                tmp6 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 48543
                    if len(subjects) == 0:
                        pass
                        # 5: x*d
                subjects.appendleft(tmp6)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 47655
            if len(subjects) >= 1:
                tmp9 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp9)
                except ValueError:
                    pass
                else:
                    pass
                    # State 47656
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                subjects.appendleft(tmp9)
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 48532
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 48296
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 48297
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 48988
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 48989
                    if len(subjects) == 0:
                        pass
                        # 6: x*d
                subjects.appendleft(tmp17)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp19 = subjects.popleft()
            associative1 = tmp19
            associative_type1 = type(tmp19)
            subjects20 = deque(tmp19._args)
            matcher = CommutativeMatcher46839.get()
            tmp21 = subjects20
            subjects20 = []
            for s in tmp21:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp21, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 46840
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                if pattern_index == 1:
                    pass
                    # State 47657
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                if pattern_index == 2:
                    pass
                    # State 47672
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                if pattern_index == 3:
                    pass
                    # State 48298
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                if pattern_index == 4:
                    pass
                    # State 48533
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                if pattern_index == 5:
                    pass
                    # State 48544
                    if len(subjects) == 0:
                        pass
                        # 5: x*d
                if pattern_index == 6:
                    pass
                    # State 48990
                    if len(subjects) == 0:
                        pass
                        # 6: x*d
            subjects.appendleft(tmp19)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
