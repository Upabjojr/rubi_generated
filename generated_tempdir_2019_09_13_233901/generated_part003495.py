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

class CommutativeMatcher78054(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.2.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.4.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher78054._instance is None:
            CommutativeMatcher78054._instance = CommutativeMatcher78054()
        return CommutativeMatcher78054._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 78053
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 78055
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 78056
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 78310
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 78311
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 80339
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 80340
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 80787
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.4.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 80788
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 88781
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp14 = subjects.popleft()
                subjects15 = deque(tmp14._args)
                # State 88782
                if len(subjects15) >= 1:
                    tmp16 = subjects15.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp16)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88783
                        if len(subjects15) >= 1:
                            tmp18 = subjects15.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.2', tmp18)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 88784
                                if len(subjects15) == 0:
                                    pass
                                    # State 88785
                                    if len(subjects) == 0:
                                        pass
                                        # 4: x**n*d
                            subjects15.appendleft(tmp18)
                    subjects15.appendleft(tmp16)
                subjects.appendleft(tmp14)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp20 = subjects.popleft()
            associative1 = tmp20
            associative_type1 = type(tmp20)
            subjects21 = deque(tmp20._args)
            matcher = CommutativeMatcher78058.get()
            tmp22 = subjects21
            subjects21 = []
            for s in tmp22:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp22, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 78059
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 78312
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                if pattern_index == 2:
                    pass
                    # State 80341
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                if pattern_index == 3:
                    pass
                    # State 80789
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                if pattern_index == 4:
                    pass
                    # State 88790
                    if len(subjects) == 0:
                        pass
                        # 4: x**n*d
            subjects.appendleft(tmp20)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
