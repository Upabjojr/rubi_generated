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


class CommutativeMatcher26386(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.1.1.2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.1.1.2.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.1.1.2.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher26386._instance is None:
            CommutativeMatcher26386._instance = CommutativeMatcher26386()
        return CommutativeMatcher26386._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 26385
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 26387
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 26388
                    if len(subjects) == 0:
                        pass
                        # 0: f*x
                        yield 0, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp4 = subjects.popleft()
                subjects5 = deque(tmp4._args)
                # State 49347
                if len(subjects5) >= 1:
                    tmp6 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp6)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 49348
                        if len(subjects5) >= 1:
                            tmp8 = subjects5.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2.1.2', tmp8)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49349
                                if len(subjects5) == 0:
                                    pass
                                    # State 49350
                                    if len(subjects) == 0:
                                        pass
                                        # 1: e*x**n
                                        yield 1, subst3
                            subjects5.appendleft(tmp8)
                    subjects5.appendleft(tmp6)
                if len(subjects5) >= 1:
                    tmp10 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.0', tmp10)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 49893
                        if len(subjects5) >= 1:
                            tmp12 = subjects5.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2.1.2', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49894
                                if len(subjects5) == 0:
                                    pass
                                    # State 49895
                                    if len(subjects) == 0:
                                        pass
                                        # 2: e*x**n
                                        yield 2, subst3
                            subjects5.appendleft(tmp12)
                    subjects5.appendleft(tmp10)
                if len(subjects5) >= 1:
                    tmp14 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp14)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 50219
                        if len(subjects5) >= 1 and subjects5[0] == Integer(2):
                            tmp16 = subjects5.popleft()
                            # State 50220
                            if len(subjects5) == 0:
                                pass
                                # State 50221
                                if len(subjects) == 0:
                                    pass
                                    # 3: e*x**2
                                    yield 3, subst2
                            subjects5.appendleft(tmp16)
                    subjects5.appendleft(tmp14)
                subjects.appendleft(tmp4)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp17 = subjects.popleft()
            associative1 = tmp17
            associative_type1 = type(tmp17)
            subjects18 = deque(tmp17._args)
            matcher = CommutativeMatcher26390.get()
            tmp19 = subjects18
            subjects18 = []
            for s in tmp19:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp19, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 26391
                    if len(subjects) == 0:
                        pass
                        # 0: f*x
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 49355
                    if len(subjects) == 0:
                        pass
                        # 1: e*x**n
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 49899
                    if len(subjects) == 0:
                        pass
                        # 2: e*x**n
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 50225
                    if len(subjects) == 0:
                        pass
                        # 3: e*x**2
                        yield 3, subst1
            subjects.appendleft(tmp17)
        return
        yield


from .generated_part003865 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset