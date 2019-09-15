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


class CommutativeMatcher124022(CommutativeMatcher):
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
        if CommutativeMatcher124022._instance is None:
            CommutativeMatcher124022._instance = CommutativeMatcher124022()
        return CommutativeMatcher124022._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 124021
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 124023
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 124024
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124025
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124026
                                if len(subjects3) == 0:
                                    pass
                                    # State 124027
                                    if len(subjects) == 0:
                                        pass
                                        # 0: x**n*d
                                        yield 0, subst3
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                if len(subjects3) >= 1:
                    tmp8 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp8)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124630
                        if len(subjects3) >= 1:
                            tmp10 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124631
                                if len(subjects3) == 0:
                                    pass
                                    # State 124632
                                    if len(subjects) == 0:
                                        pass
                                        # 1: x**n*d
                                        yield 1, subst3
                            subjects3.appendleft(tmp10)
                    subjects3.appendleft(tmp8)
                if len(subjects3) >= 1:
                    tmp12 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp12)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125054
                        if len(subjects3) >= 1:
                            tmp14 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp14)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125055
                                if len(subjects3) == 0:
                                    pass
                                    # State 125056
                                    if len(subjects) == 0:
                                        pass
                                        # 2: d*x**n
                                        yield 2, subst3
                            subjects3.appendleft(tmp14)
                    subjects3.appendleft(tmp12)
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp16 = subjects.popleft()
            associative1 = tmp16
            associative_type1 = type(tmp16)
            subjects17 = deque(tmp16._args)
            matcher = CommutativeMatcher124029.get()
            tmp18 = subjects17
            subjects17 = []
            for s in tmp18:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp18, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 124034
                    if len(subjects) == 0:
                        pass
                        # 0: x**n*d
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 124636
                    if len(subjects) == 0:
                        pass
                        # 1: x**n*d
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 125060
                    if len(subjects) == 0:
                        pass
                        # 2: d*x**n
                        yield 2, subst1
            subjects.appendleft(tmp16)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part003283 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset