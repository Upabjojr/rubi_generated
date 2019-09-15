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


class CommutativeMatcher104743(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
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
        if CommutativeMatcher104743._instance is None:
            CommutativeMatcher104743._instance = CommutativeMatcher104743()
        return CommutativeMatcher104743._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 104742
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 104744
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 104745
                    if len(subjects) == 0:
                        pass
                        # 0: RFx**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1712)
                        yield 0, subst2
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 104746
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.2.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 104747
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 104748
                        if len(subjects5) == 0:
                            pass
                            # State 104749
                            if len(subjects) == 0:
                                pass
                                # 0: RFx**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1712)
                                yield 0, subst2
                    if len(subjects5) >= 1:
                        tmp9 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 104748
                            if len(subjects5) == 0:
                                pass
                                # State 104749
                                if len(subjects) == 0:
                                    pass
                                    # 0: RFx**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1712)
                                    yield 0, subst2
                        subjects5.appendleft(tmp9)
                subjects5.appendleft(tmp6)
            subjects.appendleft(tmp4)
        return
        yield


from collections import deque