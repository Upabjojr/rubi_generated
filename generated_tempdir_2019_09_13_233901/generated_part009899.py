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

class CommutativeMatcher105746(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i5.1.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i5.1.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i5.1.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i5.1.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher105746._instance is None:
            CommutativeMatcher105746._instance = CommutativeMatcher105746()
        return CommutativeMatcher105746._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 105745
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i5.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 105747
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i5.1.2.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 105748
                    if len(subjects) == 0:
                        pass
                        # 0: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1721)
                        # 1: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1723)
                        # 2: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                        # 3: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 105749
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i5.1.2.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 105750
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i5.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 105751
                        if len(subjects5) == 0:
                            pass
                            # State 105752
                            if len(subjects) == 0:
                                pass
                                # 0: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1721)
                                # 1: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1723)
                                # 2: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                # 3: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                    if len(subjects5) >= 1:
                        tmp9 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i5.1.2.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 105751
                            if len(subjects5) == 0:
                                pass
                                # State 105752
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1721)
                                    # 1: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1723)
                                    # 2: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1713)
                                    # 3: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f1713)
                        subjects5.appendleft(tmp9)
                subjects5.appendleft(tmp6)
            subjects.appendleft(tmp4)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
