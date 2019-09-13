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

class CommutativeMatcher123982(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 1
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher123982._instance is None:
            CommutativeMatcher123982._instance = CommutativeMatcher123982()
        return CommutativeMatcher123982._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 123981
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 123983
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0_1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 123984
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 123985
                            if len(subjects2) == 0:
                                pass
                                # State 123986
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp7 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 124607
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 124608
                            if len(subjects2) == 0:
                                pass
                                # State 124609
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                        subjects2.appendleft(tmp9)
                subjects2.appendleft(tmp7)
            if len(subjects2) >= 1:
                tmp11 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1.1', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125031
                    if len(subjects2) >= 1:
                        tmp13 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.1.2', tmp13)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 125032
                            if len(subjects2) == 0:
                                pass
                                # State 125033
                                if len(subjects) == 0:
                                    pass
                                    # 2: x**n
                        subjects2.appendleft(tmp13)
                subjects2.appendleft(tmp11)
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
