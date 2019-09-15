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


class CommutativeMatcher141768(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i4.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher141768._instance is None:
            CommutativeMatcher141768._instance = CommutativeMatcher141768()
        return CommutativeMatcher141768._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 141767
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 141769
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.3.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 141770
                    if len(subjects) == 0:
                        pass
                        # 0: x*b /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127)
                        yield 0, subst2
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp4 = subjects.popleft()
            associative1 = tmp4
            associative_type1 = type(tmp4)
            subjects5 = deque(tmp4._args)
            matcher = CommutativeMatcher141772.get()
            tmp6 = subjects5
            subjects5 = []
            for s in tmp6:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp6, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 141773
                    if len(subjects) == 0:
                        pass
                        # 0: x*b /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f127)
                        yield 0, subst1
            subjects.appendleft(tmp4)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part008901 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset