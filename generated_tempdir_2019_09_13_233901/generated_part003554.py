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

class CommutativeMatcher13985(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0_2', 1, 1, None), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0_3', 1, 1, None), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 0
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher13985._instance is None:
            CommutativeMatcher13985._instance = CommutativeMatcher13985()
        return CommutativeMatcher13985._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 13984
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 13986
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 13987
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 13988
                        if len(subjects3) >= 1 and subjects3[0] == 2:
                            tmp6 = subjects3.popleft()
                            # State 13989
                            if len(subjects3) == 0:
                                pass
                                # State 13990
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**2*c
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp7 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 139661
                    if len(subjects) == 0:
                        pass
                        # 1: x*e1
                subjects.appendleft(tmp7)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 139666
            if len(subjects) >= 1:
                tmp10 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', tmp10)
                except ValueError:
                    pass
                else:
                    pass
                    # State 139667
                    if len(subjects) == 0:
                        pass
                        # 2: x*e2
                subjects.appendleft(tmp10)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp12 = subjects.popleft()
            associative1 = tmp12
            associative_type1 = type(tmp12)
            subjects13 = deque(tmp12._args)
            matcher = CommutativeMatcher13992.get()
            tmp14 = subjects13
            subjects13 = []
            for s in tmp14:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp14, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 13997
                    if len(subjects) == 0:
                        pass
                        # 0: x**2*c
                if pattern_index == 1:
                    pass
                    # State 139662
                    if len(subjects) == 0:
                        pass
                        # 1: x*e1
                if pattern_index == 2:
                    pass
                    # State 139668
                    if len(subjects) == 0:
                        pass
                        # 2: x*e2
            subjects.appendleft(tmp12)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
