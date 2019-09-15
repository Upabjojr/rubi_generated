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


class CommutativeMatcher22135(CommutativeMatcher):
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
        if CommutativeMatcher22135._instance is None:
            CommutativeMatcher22135._instance = CommutativeMatcher22135()
        return CommutativeMatcher22135._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 22134
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 22136
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 22137
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst2
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
                    # State 44861
                    if len(subjects) == 0:
                        pass
                        # 4: f*x
                        yield 4, subst2
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 30019
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp7 = subjects.popleft()
                subjects8 = deque(tmp7._args)
                # State 30020
                if len(subjects8) >= 1:
                    tmp9 = subjects8.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2.1.1', tmp9)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 30021
                        if len(subjects8) >= 1:
                            tmp11 = subjects8.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2.1.2', tmp11)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 30022
                                if len(subjects8) == 0:
                                    pass
                                    # State 30023
                                    if len(subjects) == 0:
                                        pass
                                        # 1: f*x**m
                                        yield 1, subst3
                            subjects8.appendleft(tmp11)
                        if len(subjects8) >= 1 and subjects8[0] == Integer(2):
                            tmp13 = subjects8.popleft()
                            # State 44856
                            if len(subjects8) == 0:
                                pass
                                # State 44857
                                if len(subjects) == 0:
                                    pass
                                    # 3: g*x**2
                                    yield 3, subst2
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
                        # State 40356
                        if len(subjects8) >= 1:
                            tmp16 = subjects8.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp16)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 40357
                                if len(subjects8) == 0:
                                    pass
                                    # State 40358
                                    if len(subjects) == 0:
                                        pass
                                        # 2: x**j*f
                                        yield 2, subst3
                            subjects8.appendleft(tmp16)
                    subjects8.appendleft(tmp14)
                subjects.appendleft(tmp7)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp18 = subjects.popleft()
            associative1 = tmp18
            associative_type1 = type(tmp18)
            subjects19 = deque(tmp18._args)
            matcher = CommutativeMatcher22139.get()
            tmp20 = subjects19
            subjects19 = []
            for s in tmp20:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp20, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 22140
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 30028
                    if len(subjects) == 0:
                        pass
                        # 1: f*x**m
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 40362
                    if len(subjects) == 0:
                        pass
                        # 2: x**j*f
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 44860
                    if len(subjects) == 0:
                        pass
                        # 3: g*x**2
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 44862
                    if len(subjects) == 0:
                        pass
                        # 4: f*x
                        yield 4, subst1
            subjects.appendleft(tmp18)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part005393 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset