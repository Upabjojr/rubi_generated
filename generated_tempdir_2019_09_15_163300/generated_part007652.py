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


class CommutativeMatcher27571(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0_1', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1, 2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({1: 1}), [
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
        if CommutativeMatcher27571._instance is None:
            CommutativeMatcher27571._instance = CommutativeMatcher27571()
        return CommutativeMatcher27571._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 27570
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 27572
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 27573
                    if len(subjects) == 0:
                        pass
                        # 0: k*x
                        yield 0, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp4 = subjects.popleft()
                subjects5 = deque(tmp4._args)
                # State 53673
                if len(subjects5) >= 1:
                    tmp6 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp6)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53674
                        if len(subjects5) >= 1 and subjects5[0] == Integer(2):
                            tmp8 = subjects5.popleft()
                            # State 53675
                            if len(subjects5) == 0:
                                pass
                                # State 53676
                                if len(subjects) == 0:
                                    pass
                                    # 1: v**2*c
                                    yield 1, subst2
                            subjects5.appendleft(tmp8)
                    subjects5.appendleft(tmp6)
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 53682
            if len(subjects) >= 1:
                tmp10 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp10)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53683
                    if len(subjects) == 0:
                        pass
                        # 2: x*b
                        yield 2, subst2
                subjects.appendleft(tmp10)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp12 = subjects.popleft()
            associative1 = tmp12
            associative_type1 = type(tmp12)
            subjects13 = deque(tmp12._args)
            matcher = CommutativeMatcher27575.get()
            tmp14 = subjects13
            subjects13 = []
            for s in tmp14:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp14, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 27576
                    if len(subjects) == 0:
                        pass
                        # 0: k*x
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 53681
                    if len(subjects) == 0:
                        pass
                        # 1: v**2*c
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 53684
                    if len(subjects) == 0:
                        pass
                        # 2: x*b
                        yield 2, subst1
            subjects.appendleft(tmp12)
        return
        yield


from .generated_part007653 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset