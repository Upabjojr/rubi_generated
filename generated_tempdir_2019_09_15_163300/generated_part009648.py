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


class CommutativeMatcher13520(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.2.1.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i3.1.2.1.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i3.1.2.1.2.1.1', 1, 1, None), Mul)
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
        if CommutativeMatcher13520._instance is None:
            CommutativeMatcher13520._instance = CommutativeMatcher13520()
        return CommutativeMatcher13520._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 13519
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 13521
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.2.1.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 13522
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp5 = subjects2.popleft()
                        # State 13523
                        if len(subjects2) == 0:
                            pass
                            # State 13524
                            if len(subjects) == 0:
                                pass
                                # 0: x**2
                                yield 0, subst1
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            subjects.appendleft(tmp1)
        return
        yield


from collections import deque