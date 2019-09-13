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

class CommutativeMatcher72650(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher72650._instance is None:
            CommutativeMatcher72650._instance = CommutativeMatcher72650()
        return CommutativeMatcher72650._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 72649
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 72651
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72652
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 72653
                            if len(subjects2) == 0:
                                pass
                                # State 72654
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f378) and (cons_f167)
                                    # 1: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f198)
                                    # 2: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f491)
                                    # 3: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4)
                                    # 4: x**n /; (cons_f4) and (cons_f70) and (cons_f71)
                                    # 5: x**n /; (cons_f4) and (cons_f70)
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
