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


class CommutativeMatcher54129(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.2.0_2', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.1.1.2.0_1', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, None), Add)
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
        if CommutativeMatcher54129._instance is None:
            CommutativeMatcher54129._instance = CommutativeMatcher54129()
        return CommutativeMatcher54129._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 54128
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 54130
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 54131
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 114015
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 114016
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114017
                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                            tmp9 = subjects6.popleft()
                            # State 114018
                            if len(subjects6) == 0:
                                pass
                                # State 114019
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**2*g
                                    yield 1, subst2
                            subjects6.appendleft(tmp9)
                    subjects6.appendleft(tmp7)
                if len(subjects6) >= 1:
                    tmp10 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp10)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114165
                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                            tmp12 = subjects6.popleft()
                            # State 114166
                            if len(subjects6) == 0:
                                pass
                                # State 114167
                                if len(subjects) == 0:
                                    pass
                                    # 2: g*x**2
                                    yield 2, subst2
                            subjects6.appendleft(tmp12)
                    subjects6.appendleft(tmp10)
                if len(subjects6) >= 1:
                    tmp13 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.0', tmp13)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114258
                        if len(subjects6) >= 1 and subjects6[0] == Integer(2):
                            tmp15 = subjects6.popleft()
                            # State 114259
                            if len(subjects6) == 0:
                                pass
                                # State 114260
                                if len(subjects) == 0:
                                    pass
                                    # 3: g*x**2
                                    yield 3, subst2
                            subjects6.appendleft(tmp15)
                    subjects6.appendleft(tmp13)
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp16 = subjects.popleft()
            associative1 = tmp16
            associative_type1 = type(tmp16)
            subjects17 = deque(tmp16._args)
            matcher = CommutativeMatcher54133.get()
            tmp18 = subjects17
            subjects17 = []
            for s in tmp18:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp18, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 54134
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 114024
                    if len(subjects) == 0:
                        pass
                        # 1: x**2*g
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 114171
                    if len(subjects) == 0:
                        pass
                        # 2: g*x**2
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 114264
                    if len(subjects) == 0:
                        pass
                        # 3: g*x**2
                        yield 3, subst1
            subjects.appendleft(tmp16)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part007500 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset