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

class CommutativeMatcher65941(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.2.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher65941._instance is None:
            CommutativeMatcher65941._instance = CommutativeMatcher65941()
        return CommutativeMatcher65941._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 65940
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 65942
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 65943
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 66270
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 66271
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 66576
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 66577
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 93577
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 93578
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 94286
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.3.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 94287
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                subjects.appendleft(tmp14)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp16 = subjects.popleft()
            associative1 = tmp16
            associative_type1 = type(tmp16)
            subjects17 = deque(tmp16._args)
            matcher = CommutativeMatcher65945.get()
            tmp18 = subjects17
            subjects17 = []
            for s in tmp18:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp18, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 65946
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                if pattern_index == 1:
                    pass
                    # State 66272
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                if pattern_index == 2:
                    pass
                    # State 66578
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                if pattern_index == 3:
                    pass
                    # State 93579
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                if pattern_index == 4:
                    pass
                    # State 94288
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
            subjects.appendleft(tmp16)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
