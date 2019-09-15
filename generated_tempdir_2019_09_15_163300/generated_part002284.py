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


class CommutativeMatcher13828(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    2: (2, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.0_1', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({4: 1, 5: 1}), [
      
]),
    6: (6, Multiset({4: 1, 6: 1}), [
      
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 1
    anonymous_patterns = {4}

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher13828._instance is None:
            CommutativeMatcher13828._instance = CommutativeMatcher13828()
        return CommutativeMatcher13828._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 13827
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 13829
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 13830
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 13831
                        if len(subjects3) >= 1 and subjects3[0] == Integer(2):
                            tmp6 = subjects3.popleft()
                            # State 13832
                            if len(subjects3) == 0:
                                pass
                                # State 13833
                                if len(subjects) == 0:
                                    pass
                                    # 0: c*x**2
                                    yield 0, subst2
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp7 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 150978
                    if len(subjects) == 0:
                        pass
                        # 5: x*e
                        yield 5, subst2
                subjects.appendleft(tmp7)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 13946
            if len(subjects) >= 1:
                tmp10 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.1', tmp10)
                except ValueError:
                    pass
                else:
                    pass
                    # State 13947
                    if len(subjects) == 0:
                        pass
                        # 1: b*x
                        yield 1, subst2
                subjects.appendleft(tmp10)
            if len(subjects) >= 1:
                tmp12 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp12)
                except ValueError:
                    pass
                else:
                    pass
                    # State 150882
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                        yield 2, subst2
                subjects.appendleft(tmp12)
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 150983
                    if len(subjects) == 0:
                        pass
                        # 6: x*g
                        yield 6, subst2
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 150897
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 150898
                    if len(subjects) == 0:
                        pass
                        # 3: x*g
                        yield 3, subst2
                subjects.appendleft(tmp17)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp19 = subjects.popleft()
            associative1 = tmp19
            associative_type1 = type(tmp19)
            subjects20 = deque(tmp19._args)
            matcher = CommutativeMatcher13835.get()
            tmp21 = subjects20
            subjects20 = []
            for s in tmp21:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp21, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 13840
                    if len(subjects) == 0:
                        pass
                        # 0: c*x**2
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 13948
                    if len(subjects) == 0:
                        pass
                        # 1: b*x
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 150883
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 150899
                    if len(subjects) == 0:
                        pass
                        # 3: x*g
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 150979
                    if len(subjects) == 0:
                        pass
                        # 5: x*e
                        yield 5, subst1
                if pattern_index == 5:
                    pass
                    # State 150984
                    if len(subjects) == 0:
                        pass
                        # 6: x*g
                        yield 6, subst1
            subjects.appendleft(tmp19)
        if len(subjects) >= 1 and subjects[0] == Integer(1):
            tmp22 = subjects.popleft()
            # State 150977
            if len(subjects) == 0:
                pass
                # 4: 1
                yield 4, subst0
            subjects.appendleft(tmp22)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part002285 import *