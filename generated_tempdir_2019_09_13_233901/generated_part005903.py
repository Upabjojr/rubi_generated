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

class CommutativeMatcher14688(CommutativeMatcher):
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
        if CommutativeMatcher14688._instance is None:
            CommutativeMatcher14688._instance = CommutativeMatcher14688()
        return CommutativeMatcher14688._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 14687
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 14689
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 14690
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.1.0', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 17939
                    if len(subjects) == 0:
                        pass
                        # 1: x*g
                subjects.appendleft(tmp4)
            if len(subjects) >= 1:
                tmp6 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103948
                    if len(subjects) == 0:
                        pass
                        # 3: b*x
                subjects.appendleft(tmp6)
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103996
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 101399
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 101400
                    if len(subjects) == 0:
                        pass
                        # 2: x*b
                subjects.appendleft(tmp11)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp13 = subjects.popleft()
            associative1 = tmp13
            associative_type1 = type(tmp13)
            subjects14 = deque(tmp13._args)
            matcher = CommutativeMatcher14692.get()
            tmp15 = subjects14
            subjects14 = []
            for s in tmp15:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp15, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 14693
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 17940
                    if len(subjects) == 0:
                        pass
                        # 1: x*g
                if pattern_index == 2:
                    pass
                    # State 101401
                    if len(subjects) == 0:
                        pass
                        # 2: x*b
                if pattern_index == 3:
                    pass
                    # State 103949
                    if len(subjects) == 0:
                        pass
                        # 3: b*x
                if pattern_index == 4:
                    pass
                    # State 103997
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
            subjects.appendleft(tmp13)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
