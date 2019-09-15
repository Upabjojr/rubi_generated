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


class CommutativeMatcher121954(CommutativeMatcher):
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
        if CommutativeMatcher121954._instance is None:
            CommutativeMatcher121954._instance = CommutativeMatcher121954()
        return CommutativeMatcher121954._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 121953
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 121955
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 121956
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
            # State 123930
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 123931
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 123932
                        if len(subjects6) >= 1:
                            tmp9 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp9)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 123933
                                if len(subjects6) == 0:
                                    pass
                                    # State 123934
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
                        # State 124423
                        if len(subjects6) >= 1:
                            tmp13 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp13)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124424
                                if len(subjects6) == 0:
                                    pass
                                    # State 124425
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
                        # State 124895
                        if len(subjects6) >= 1:
                            tmp17 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp17)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124896
                                if len(subjects6) == 0:
                                    pass
                                    # State 124897
                                    if len(subjects) == 0:
                                        pass
                                        # 3: x**n*d
                                        yield 3, subst3
                            subjects6.appendleft(tmp17)
                    subjects6.appendleft(tmp15)
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp19 = subjects.popleft()
            associative1 = tmp19
            associative_type1 = type(tmp19)
            subjects20 = deque(tmp19._args)
            matcher = CommutativeMatcher121958.get()
            tmp21 = subjects20
            subjects20 = []
            for s in tmp21:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp21, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 121959
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 123939
                    if len(subjects) == 0:
                        pass
                        # 1: d*x**n
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 124429
                    if len(subjects) == 0:
                        pass
                        # 2: x**n*d
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 124901
                    if len(subjects) == 0:
                        pass
                        # 3: x**n*d
                        yield 3, subst1
            subjects.appendleft(tmp19)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part004769 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset