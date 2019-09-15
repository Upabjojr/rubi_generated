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


class CommutativeMatcher121972(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher121972._instance is None:
            CommutativeMatcher121972._instance = CommutativeMatcher121972()
        return CommutativeMatcher121972._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 121971
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 121973
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 121974
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 123954
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 123955
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 123956
                        if len(subjects6) >= 1:
                            tmp9 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp9)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 123957
                                if len(subjects6) == 0:
                                    pass
                                    # State 123958
                                    if len(subjects) == 0:
                                        pass
                                        # 1: d*x**n
                                        yield 1, subst3
                            subjects6.appendleft(tmp9)
                    subjects6.appendleft(tmp7)
                if len(subjects6) >= 1:
                    tmp11 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp11)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124441
                        if len(subjects6) >= 1:
                            tmp13 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp13)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124442
                                if len(subjects6) == 0:
                                    pass
                                    # State 124443
                                    if len(subjects) == 0:
                                        pass
                                        # 2: x**n*d
                                        yield 2, subst3
                            subjects6.appendleft(tmp13)
                    subjects6.appendleft(tmp11)
                if len(subjects6) >= 1:
                    tmp15 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp15)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124913
                        if len(subjects6) >= 1:
                            tmp17 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp17)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124914
                                if len(subjects6) == 0:
                                    pass
                                    # State 124915
                                    if len(subjects) == 0:
                                        pass
                                        # 3: x**n*d
                                        yield 3, subst3
                            subjects6.appendleft(tmp17)
                    subjects6.appendleft(tmp15)
                subjects.appendleft(tmp5)
            if len(subjects) >= 1:
                tmp19 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp19)
                except ValueError:
                    pass
                else:
                    pass
                    # State 136874
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                        yield 4, subst2
                subjects.appendleft(tmp19)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp21 = subjects.popleft()
            associative1 = tmp21
            associative_type1 = type(tmp21)
            subjects22 = deque(tmp21._args)
            matcher = CommutativeMatcher121976.get()
            tmp23 = subjects22
            subjects22 = []
            for s in tmp23:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp23, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 121977
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 123963
                    if len(subjects) == 0:
                        pass
                        # 1: d*x**n
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 124447
                    if len(subjects) == 0:
                        pass
                        # 2: x**n*d
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 124919
                    if len(subjects) == 0:
                        pass
                        # 3: x**n*d
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 136875
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                        yield 4, subst1
            subjects.appendleft(tmp21)
        return
        yield


from .generated_part005452 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset