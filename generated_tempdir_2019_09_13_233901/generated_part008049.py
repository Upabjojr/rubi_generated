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

class CommutativeMatcher125802(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1, 2: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({4: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
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
        if CommutativeMatcher125802._instance is None:
            CommutativeMatcher125802._instance = CommutativeMatcher125802()
        return CommutativeMatcher125802._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 125801
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 125803
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125804
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 129086
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 129087
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.0', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 129088
                        if len(subjects6) >= 1 and subjects6[0] == 2:
                            tmp9 = subjects6.popleft()
                            # State 129089
                            if len(subjects6) == 0:
                                pass
                                # State 129090
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**2*c
                            subjects6.appendleft(tmp9)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 129096
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 129097
                    if len(subjects) == 0:
                        pass
                        # 2: x*b
                subjects.appendleft(tmp11)
            if len(subjects) >= 1:
                tmp13 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp13)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137609
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                subjects.appendleft(tmp13)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132408
            if len(subjects) >= 1:
                tmp16 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp16)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132409
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                subjects.appendleft(tmp16)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp18 = subjects.popleft()
            associative1 = tmp18
            associative_type1 = type(tmp18)
            subjects19 = deque(tmp18._args)
            matcher = CommutativeMatcher125806.get()
            tmp20 = subjects19
            subjects19 = []
            for s in tmp20:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp20, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 125807
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 129095
                    if len(subjects) == 0:
                        pass
                        # 1: x**2*c
                if pattern_index == 2:
                    pass
                    # State 129098
                    if len(subjects) == 0:
                        pass
                        # 2: x*b
                if pattern_index == 3:
                    pass
                    # State 132410
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                if pattern_index == 4:
                    pass
                    # State 137610
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
            subjects.appendleft(tmp18)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
