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


class CommutativeMatcher25939(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.1.1.2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.1.1.2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.1.1.2.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.2.2.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i2.1.1.2.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher25939._instance is None:
            CommutativeMatcher25939._instance = CommutativeMatcher25939()
        return CommutativeMatcher25939._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 25938
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 49634
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.0', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 49635
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49636
                            if len(subjects2) == 0:
                                pass
                                # State 49637
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp7 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1.0', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 50094
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 50095
                            if len(subjects2) == 0:
                                pass
                                # State 50096
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                                    yield 1, subst2
                        subjects2.appendleft(tmp9)
                subjects2.appendleft(tmp7)
            if len(subjects2) >= 1:
                tmp11 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 50420
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp13 = subjects2.popleft()
                        # State 50421
                        if len(subjects2) == 0:
                            pass
                            # State 50422
                            if len(subjects) == 0:
                                pass
                                # 2: x**2
                                yield 2, subst1
                        subjects2.appendleft(tmp13)
                subjects2.appendleft(tmp11)
            subjects.appendleft(tmp1)
        return
        yield


from collections import deque