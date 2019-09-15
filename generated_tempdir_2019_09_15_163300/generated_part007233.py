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


class CommutativeMatcher25914(CommutativeMatcher):
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
]),
    4: (4, Multiset({4: 1}), [
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
        if CommutativeMatcher25914._instance is None:
            CommutativeMatcher25914._instance = CommutativeMatcher25914()
        return CommutativeMatcher25914._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 25913
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 25915
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 25916
                    if len(subjects) == 0:
                        pass
                        # 0: f*x
                        yield 0, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 26472
                    if len(subjects) == 0:
                        pass
                        # 1: f*x
                        yield 1, subst2
                subjects.appendleft(tmp4)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp6 = subjects.popleft()
                subjects7 = deque(tmp6._args)
                # State 49576
                if len(subjects7) >= 1:
                    tmp8 = subjects7.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp8)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 49577
                        if len(subjects7) >= 1:
                            tmp10 = subjects7.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2.1.2', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49578
                                if len(subjects7) == 0:
                                    pass
                                    # State 49579
                                    if len(subjects) == 0:
                                        pass
                                        # 2: e*x**n
                                        yield 2, subst3
                            subjects7.appendleft(tmp10)
                    subjects7.appendleft(tmp8)
                if len(subjects7) >= 1:
                    tmp12 = subjects7.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.0', tmp12)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 50054
                        if len(subjects7) >= 1:
                            tmp14 = subjects7.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2.1.2', tmp14)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 50055
                                if len(subjects7) == 0:
                                    pass
                                    # State 50056
                                    if len(subjects) == 0:
                                        pass
                                        # 3: e*x**n
                                        yield 3, subst3
                            subjects7.appendleft(tmp14)
                    subjects7.appendleft(tmp12)
                if len(subjects7) >= 1:
                    tmp16 = subjects7.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp16)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 50380
                        if len(subjects7) >= 1 and subjects7[0] == Integer(2):
                            tmp18 = subjects7.popleft()
                            # State 50381
                            if len(subjects7) == 0:
                                pass
                                # State 50382
                                if len(subjects) == 0:
                                    pass
                                    # 4: e*x**2
                                    yield 4, subst2
                            subjects7.appendleft(tmp18)
                    subjects7.appendleft(tmp16)
                subjects.appendleft(tmp6)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp19 = subjects.popleft()
            associative1 = tmp19
            associative_type1 = type(tmp19)
            subjects20 = deque(tmp19._args)
            matcher = CommutativeMatcher25918.get()
            tmp21 = subjects20
            subjects20 = []
            for s in tmp21:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp21, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 25919
                    if len(subjects) == 0:
                        pass
                        # 0: f*x
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 26473
                    if len(subjects) == 0:
                        pass
                        # 1: f*x
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 49584
                    if len(subjects) == 0:
                        pass
                        # 2: e*x**n
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 50060
                    if len(subjects) == 0:
                        pass
                        # 3: e*x**n
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 50386
                    if len(subjects) == 0:
                        pass
                        # 4: e*x**2
                        yield 4, subst1
            subjects.appendleft(tmp19)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part007234 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset