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

class CommutativeMatcher23887(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(0)), Add)
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
        if CommutativeMatcher23887._instance is None:
            CommutativeMatcher23887._instance = CommutativeMatcher23887()
        return CommutativeMatcher23887._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 23886
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 23888
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 23889
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 27494
                    if len(subjects) == 0:
                        pass
                        # 1: k*x
                subjects.appendleft(tmp4)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 40519
                if len(subjects) >= 1:
                    tmp7 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 40520
                        if len(subjects) == 0:
                            pass
                            # 3: a*x**n
                    subjects.appendleft(tmp7)
            if len(subjects) >= 1:
                tmp9 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp9)
                except ValueError:
                    pass
                else:
                    pass
                    # State 48425
                    if len(subjects) == 0:
                        pass
                        # 4: b*x
                subjects.appendleft(tmp9)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp11 = subjects.popleft()
                subjects12 = deque(tmp11._args)
                # State 40492
                if len(subjects12) >= 1:
                    tmp13 = subjects12.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp13)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 40493
                        if len(subjects12) >= 1:
                            tmp15 = subjects12.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.1.2', tmp15)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 40494
                                if len(subjects12) == 0:
                                    pass
                                    # State 40495
                                    if len(subjects) == 0:
                                        pass
                                        # 2: b*x**mn
                            subjects12.appendleft(tmp15)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40521
                            if len(subjects12) == 0:
                                pass
                                # State 40522
                                if len(subjects) == 0:
                                    pass
                                    # 3: a*x**n
                        if len(subjects12) >= 1:
                            tmp18 = subjects12.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp18)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 40521
                                if len(subjects12) == 0:
                                    pass
                                    # State 40522
                                    if len(subjects) == 0:
                                        pass
                                        # 3: a*x**n
                            subjects12.appendleft(tmp18)
                    subjects12.appendleft(tmp13)
                subjects.appendleft(tmp11)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp20 = subjects.popleft()
            associative1 = tmp20
            associative_type1 = type(tmp20)
            subjects21 = deque(tmp20._args)
            matcher = CommutativeMatcher23891.get()
            tmp22 = subjects21
            subjects21 = []
            for s in tmp22:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp22, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 23892
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 27495
                    if len(subjects) == 0:
                        pass
                        # 1: k*x
                if pattern_index == 2:
                    pass
                    # State 40500
                    if len(subjects) == 0:
                        pass
                        # 2: b*x**mn
                if pattern_index == 3:
                    pass
                    # State 40527
                    if len(subjects) == 0:
                        pass
                        # 3: a*x**n
                if pattern_index == 4:
                    pass
                    # State 48426
                    if len(subjects) == 0:
                        pass
                        # 4: b*x
            subjects.appendleft(tmp20)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
