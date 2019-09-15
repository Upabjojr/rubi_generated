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


class CommutativeMatcher134692(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i5.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher134692._instance is None:
            CommutativeMatcher134692._instance = CommutativeMatcher134692()
        return CommutativeMatcher134692._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 134691
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i5.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 134693
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i5.2.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 134694
                    if len(subjects) == 0:
                        pass
                        # 0: x**n /; (cons_f8) and (cons_f1875)
                        yield 0, subst2
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 134695
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i5.2.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 134696
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i5.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 134697
                        if len(subjects5) == 0:
                            pass
                            # State 134698
                            if len(subjects) == 0:
                                pass
                                # 0: x**n /; (cons_f8) and (cons_f1875)
                                yield 0, subst2
                    if len(subjects5) >= 1:
                        tmp9 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i5.2.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 134697
                            if len(subjects5) == 0:
                                pass
                                # State 134698
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n /; (cons_f8) and (cons_f1875)
                                    yield 0, subst2
                        subjects5.appendleft(tmp9)
                subjects5.appendleft(tmp6)
            subjects.appendleft(tmp4)
        return
        yield


from collections import deque