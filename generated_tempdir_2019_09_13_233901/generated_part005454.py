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

class CommutativeMatcher126020(CommutativeMatcher):
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
        if CommutativeMatcher126020._instance is None:
            CommutativeMatcher126020._instance = CommutativeMatcher126020()
        return CommutativeMatcher126020._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 126019
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 126021
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 126022
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp4 = subjects.popleft()
                subjects5 = deque(tmp4._args)
                # State 127663
                if len(subjects5) >= 1:
                    tmp6 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp6)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 127664
                        if len(subjects5) >= 1:
                            tmp8 = subjects5.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp8)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 127665
                                if len(subjects5) == 0:
                                    pass
                                    # State 127666
                                    if len(subjects) == 0:
                                        pass
                                        # 2: d*x**n
                            subjects5.appendleft(tmp8)
                    subjects5.appendleft(tmp6)
                if len(subjects5) >= 1:
                    tmp10 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp10)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128207
                        if len(subjects5) >= 1:
                            tmp12 = subjects5.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 128208
                                if len(subjects5) == 0:
                                    pass
                                    # State 128209
                                    if len(subjects) == 0:
                                        pass
                                        # 3: x**n*d
                            subjects5.appendleft(tmp12)
                    subjects5.appendleft(tmp10)
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 126225
            if len(subjects) >= 1:
                tmp15 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp15)
                except ValueError:
                    pass
                else:
                    pass
                    # State 126226
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                subjects.appendleft(tmp15)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp17 = subjects.popleft()
            associative1 = tmp17
            associative_type1 = type(tmp17)
            subjects18 = deque(tmp17._args)
            matcher = CommutativeMatcher126024.get()
            tmp19 = subjects18
            subjects18 = []
            for s in tmp19:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp19, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 126025
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                if pattern_index == 1:
                    pass
                    # State 126227
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                if pattern_index == 2:
                    pass
                    # State 127671
                    if len(subjects) == 0:
                        pass
                        # 2: d*x**n
                if pattern_index == 3:
                    pass
                    # State 128213
                    if len(subjects) == 0:
                        pass
                        # 3: x**n*d
            subjects.appendleft(tmp17)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
