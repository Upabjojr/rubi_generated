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


class CommutativeMatcher21492(CommutativeMatcher):
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
    3: (3, Multiset({2: 1, 3: 1}), [
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
        if CommutativeMatcher21492._instance is None:
            CommutativeMatcher21492._instance = CommutativeMatcher21492()
        return CommutativeMatcher21492._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 21491
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 21493
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 21494
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
                    # State 44557
                    if len(subjects) == 0:
                        pass
                        # 3: f*x
                        yield 3, subst2
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 29628
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp7 = subjects.popleft()
                subjects8 = deque(tmp7._args)
                # State 29629
                if len(subjects8) >= 1:
                    tmp9 = subjects8.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2.1.1', tmp9)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 29630
                        if len(subjects8) >= 1:
                            tmp11 = subjects8.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2.1.2', tmp11)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 29631
                                if len(subjects8) == 0:
                                    pass
                                    # State 29632
                                    if len(subjects) == 0:
                                        pass
                                        # 1: f*x**m
                                        yield 1, subst3
                            subjects8.appendleft(tmp11)
                        if len(subjects8) >= 1 and subjects8[0] == Integer(2):
                            tmp13 = subjects8.popleft()
                            # State 44552
                            if len(subjects8) == 0:
                                pass
                                # State 44553
                                if len(subjects) == 0:
                                    pass
                                    # 2: g*x**2
                                    yield 2, subst2
                            subjects8.appendleft(tmp13)
                    subjects8.appendleft(tmp9)
                subjects.appendleft(tmp7)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp14 = subjects.popleft()
            associative1 = tmp14
            associative_type1 = type(tmp14)
            subjects15 = deque(tmp14._args)
            matcher = CommutativeMatcher21496.get()
            tmp16 = subjects15
            subjects15 = []
            for s in tmp16:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp16, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 21497
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 29637
                    if len(subjects) == 0:
                        pass
                        # 1: f*x**m
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 44556
                    if len(subjects) == 0:
                        pass
                        # 2: g*x**2
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 44558
                    if len(subjects) == 0:
                        pass
                        # 3: f*x
                        yield 3, subst1
            subjects.appendleft(tmp14)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from multiset import Multiset
from matchpy.utils import VariableWithCount
from .generated_part004623 import *