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


class CommutativeMatcher10048(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher10048._instance is None:
            CommutativeMatcher10048._instance = CommutativeMatcher10048()
        return CommutativeMatcher10048._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 10047
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 10049
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 10050
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 10051
                            if len(subjects2) == 0:
                                pass
                                # State 10052
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f52) and (cons_f4) and (cons_f5) and (cons_f800)
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                        tmp7 = subjects2.popleft()
                        # State 10595
                        if len(subjects2) == 0:
                            pass
                            # State 10596
                            if len(subjects) == 0:
                                pass
                                # 1: 1/x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                yield 1, subst1
                        subjects2.appendleft(tmp7)
                subjects2.appendleft(tmp3)
            subjects.appendleft(tmp1)
        return
        yield


from collections import deque