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

class CommutativeMatcher25984(CommutativeMatcher):
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
        if CommutativeMatcher25984._instance is None:
            CommutativeMatcher25984._instance = CommutativeMatcher25984()
        return CommutativeMatcher25984._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 25983
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 49748
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.0', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 49749
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49750
                            if len(subjects2) == 0:
                                pass
                                # State 49751
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
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
                    # State 50174
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 50175
                            if len(subjects2) == 0:
                                pass
                                # State 50176
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
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
                    # State 50500
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp13 = subjects2.popleft()
                        # State 50501
                        if len(subjects2) == 0:
                            pass
                            # State 50502
                            if len(subjects) == 0:
                                pass
                                # 2: x**2
                        subjects2.appendleft(tmp13)
                subjects2.appendleft(tmp11)
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque