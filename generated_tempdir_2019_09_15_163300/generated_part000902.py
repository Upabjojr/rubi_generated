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


class CommutativeMatcher144482(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.2.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher144482._instance is None:
            CommutativeMatcher144482._instance = CommutativeMatcher144482()
        return CommutativeMatcher144482._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 144481
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 144483
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 144484
                    if len(subjects) == 0:
                        pass
                        # 0: x*b /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 0, subst2
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp4 = subjects.popleft()
            associative1 = tmp4
            associative_type1 = type(tmp4)
            subjects5 = deque(tmp4._args)
            matcher = CommutativeMatcher144486.get()
            tmp6 = subjects5
            subjects5 = []
            for s in tmp6:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp6, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 144487
                    if len(subjects) == 0:
                        pass
                        # 0: x*b /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 0, subst1
            subjects.appendleft(tmp4)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part000903 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset