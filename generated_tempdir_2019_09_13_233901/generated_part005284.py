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

class CommutativeMatcher129399(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher129399._instance is None:
            CommutativeMatcher129399._instance = CommutativeMatcher129399()
        return CommutativeMatcher129399._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 129398
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 129400
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 129401
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 130849
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 130850
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 130851
                        if len(subjects6) >= 1:
                            tmp9 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.2', tmp9)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 130852
                                if len(subjects6) == 0:
                                    pass
                                    # State 130853
                                    if len(subjects) == 0:
                                        pass
                                        # 1: d*x**n
                            subjects6.appendleft(tmp9)
                    subjects6.appendleft(tmp7)
                if len(subjects6) >= 1:
                    tmp11 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp11)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131444
                        if len(subjects6) >= 1:
                            tmp13 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.2', tmp13)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 131445
                                if len(subjects6) == 0:
                                    pass
                                    # State 131446
                                    if len(subjects) == 0:
                                        pass
                                        # 2: x**n*d
                            subjects6.appendleft(tmp13)
                    subjects6.appendleft(tmp11)
                subjects.appendleft(tmp5)
            if len(subjects) >= 1:
                tmp15 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp15)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137157
                    if len(subjects) == 0:
                        pass
                        # 3: x*e
                subjects.appendleft(tmp15)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp17 = subjects.popleft()
            associative1 = tmp17
            associative_type1 = type(tmp17)
            subjects18 = deque(tmp17._args)
            matcher = CommutativeMatcher129403.get()
            tmp19 = subjects18
            subjects18 = []
            for s in tmp19:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp19, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 129404
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 130858
                    if len(subjects) == 0:
                        pass
                        # 1: d*x**n
                if pattern_index == 2:
                    pass
                    # State 131450
                    if len(subjects) == 0:
                        pass
                        # 2: x**n*d
                if pattern_index == 3:
                    pass
                    # State 137158
                    if len(subjects) == 0:
                        pass
                        # 3: x*e
            subjects.appendleft(tmp17)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
