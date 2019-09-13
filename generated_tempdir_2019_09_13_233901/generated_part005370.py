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

class CommutativeMatcher22065(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.2.2.0', 1, 1, None), Add)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.2.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({3: 1, 4: 1}), [
      (VariableWithCount('i2.2.1.2.2.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher22065._instance is None:
            CommutativeMatcher22065._instance = CommutativeMatcher22065()
        return CommutativeMatcher22065._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 22064
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 22066
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 22067
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 44828
                    if len(subjects) == 0:
                        pass
                        # 4: f*x
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 29977
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp7 = subjects.popleft()
                subjects8 = deque(tmp7._args)
                # State 29978
                if len(subjects8) >= 1:
                    tmp9 = subjects8.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2.1.1', tmp9)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 29979
                        if len(subjects8) >= 1:
                            tmp11 = subjects8.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2.1.2', tmp11)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 29980
                                if len(subjects8) == 0:
                                    pass
                                    # State 29981
                                    if len(subjects) == 0:
                                        pass
                                        # 1: f*x**m
                            subjects8.appendleft(tmp11)
                        if len(subjects8) >= 1 and subjects8[0] == 2:
                            tmp13 = subjects8.popleft()
                            # State 44823
                            if len(subjects8) == 0:
                                pass
                                # State 44824
                                if len(subjects) == 0:
                                    pass
                                    # 3: g*x**2
                            subjects8.appendleft(tmp13)
                    subjects8.appendleft(tmp9)
                if len(subjects8) >= 1:
                    tmp14 = subjects8.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp14)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 40290
                        if len(subjects8) >= 1:
                            tmp16 = subjects8.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp16)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 40291
                                if len(subjects8) == 0:
                                    pass
                                    # State 40292
                                    if len(subjects) == 0:
                                        pass
                                        # 2: x**j*f
                            subjects8.appendleft(tmp16)
                    subjects8.appendleft(tmp14)
                subjects.appendleft(tmp7)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp18 = subjects.popleft()
            associative1 = tmp18
            associative_type1 = type(tmp18)
            subjects19 = deque(tmp18._args)
            matcher = CommutativeMatcher22069.get()
            tmp20 = subjects19
            subjects19 = []
            for s in tmp20:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp20, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 22070
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 29986
                    if len(subjects) == 0:
                        pass
                        # 1: f*x**m
                if pattern_index == 2:
                    pass
                    # State 40296
                    if len(subjects) == 0:
                        pass
                        # 2: x**j*f
                if pattern_index == 3:
                    pass
                    # State 44827
                    if len(subjects) == 0:
                        pass
                        # 3: g*x**2
                if pattern_index == 4:
                    pass
                    # State 44829
                    if len(subjects) == 0:
                        pass
                        # 4: f*x
            subjects.appendleft(tmp18)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
