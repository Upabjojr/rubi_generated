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

class CommutativeMatcher14705(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.3.1.0_2', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher14705._instance is None:
            CommutativeMatcher14705._instance = CommutativeMatcher14705()
        return CommutativeMatcher14705._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 14704
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 14706
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 14707
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.0', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 16944
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                subjects.appendleft(tmp4)
            if len(subjects) >= 1:
                tmp6 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.1.0', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 17945
                    if len(subjects) == 0:
                        pass
                        # 2: x*g
                subjects.appendleft(tmp6)
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103885
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                subjects.appendleft(tmp8)
            if len(subjects) >= 1:
                tmp10 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp10)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103954
                    if len(subjects) == 0:
                        pass
                        # 5: b*x
                subjects.appendleft(tmp10)
            if len(subjects) >= 1:
                tmp12 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp12)
                except ValueError:
                    pass
                else:
                    pass
                    # State 104002
                    if len(subjects) == 0:
                        pass
                        # 6: x*b
                subjects.appendleft(tmp12)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 101407
            if len(subjects) >= 1:
                tmp15 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1.0', tmp15)
                except ValueError:
                    pass
                else:
                    pass
                    # State 101408
                    if len(subjects) == 0:
                        pass
                        # 3: x*b
                subjects.appendleft(tmp15)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp17 = subjects.popleft()
            associative1 = tmp17
            associative_type1 = type(tmp17)
            subjects18 = deque(tmp17._args)
            matcher = CommutativeMatcher14709.get()
            tmp19 = subjects18
            subjects18 = []
            for s in tmp19:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp19, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 14710
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 16945
                    if len(subjects) == 0:
                        pass
                        # 1: x*b
                if pattern_index == 2:
                    pass
                    # State 17946
                    if len(subjects) == 0:
                        pass
                        # 2: x*g
                if pattern_index == 3:
                    pass
                    # State 101409
                    if len(subjects) == 0:
                        pass
                        # 3: x*b
                if pattern_index == 4:
                    pass
                    # State 103886
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                if pattern_index == 5:
                    pass
                    # State 103955
                    if len(subjects) == 0:
                        pass
                        # 5: b*x
                if pattern_index == 6:
                    pass
                    # State 104003
                    if len(subjects) == 0:
                        pass
                        # 6: x*b
            subjects.appendleft(tmp17)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
