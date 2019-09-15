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


class CommutativeMatcher114322(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i4.2.0', 1, 1, None), Mul),
      (VariableWithCount('i4.2.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i4.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher114322._instance is None:
            CommutativeMatcher114322._instance = CommutativeMatcher114322()
        return CommutativeMatcher114322._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 114321
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp1 = subjects.popleft()
            associative1 = tmp1
            associative_type1 = type(tmp1)
            subjects2 = deque(tmp1._args)
            matcher = CommutativeMatcher114520.get()
            tmp3 = subjects2
            subjects2 = []
            for s in tmp3:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp3, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 114526
                    if len(subjects) == 0:
                        pass
                        # 0: a + x*b /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 0, subst1
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part010050 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset