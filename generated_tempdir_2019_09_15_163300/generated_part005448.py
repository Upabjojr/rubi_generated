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


class CommutativeMatcher121891(CommutativeMatcher):
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
        if CommutativeMatcher121891._instance is None:
            CommutativeMatcher121891._instance = CommutativeMatcher121891()
        return CommutativeMatcher121891._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 121890
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 121892
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 121893
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp4 = subjects.popleft()
                subjects5 = deque(tmp4._args)
                # State 123744
                if len(subjects5) >= 1:
                    tmp6 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp6)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 123745
                        if len(subjects5) >= 1:
                            tmp8 = subjects5.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp8)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 123746
                                if len(subjects5) == 0:
                                    pass
                                    # State 123747
                                    if len(subjects) == 0:
                                        pass
                                        # 1: d*x**n
                                        yield 1, subst3
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
                        # State 124194
                        if len(subjects5) >= 1:
                            tmp12 = subjects5.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124195
                                if len(subjects5) == 0:
                                    pass
                                    # State 124196
                                    if len(subjects) == 0:
                                        pass
                                        # 2: x**n*d
                                        yield 2, subst3
                            subjects5.appendleft(tmp12)
                    subjects5.appendleft(tmp10)
                if len(subjects5) >= 1:
                    tmp14 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp14)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124750
                        if len(subjects5) >= 1:
                            tmp16 = subjects5.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp16)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124751
                                if len(subjects5) == 0:
                                    pass
                                    # State 124752
                                    if len(subjects) == 0:
                                        pass
                                        # 3: x**n*d
                                        yield 3, subst3
                            subjects5.appendleft(tmp16)
                    subjects5.appendleft(tmp14)
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132697
            if len(subjects) >= 1:
                tmp19 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp19)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132698
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                        yield 4, subst2
                subjects.appendleft(tmp19)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp21 = subjects.popleft()
            associative1 = tmp21
            associative_type1 = type(tmp21)
            subjects22 = deque(tmp21._args)
            matcher = CommutativeMatcher121895.get()
            tmp23 = subjects22
            subjects22 = []
            for s in tmp23:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp23, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 121896
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 123752
                    if len(subjects) == 0:
                        pass
                        # 1: d*x**n
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 124200
                    if len(subjects) == 0:
                        pass
                        # 2: x**n*d
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 124756
                    if len(subjects) == 0:
                        pass
                        # 3: x**n*d
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 132699
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                        yield 4, subst1
            subjects.appendleft(tmp21)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part005449 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset