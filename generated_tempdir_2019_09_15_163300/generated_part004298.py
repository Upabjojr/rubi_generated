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


class CommutativeMatcher134424(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.1.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher134424._instance is None:
            CommutativeMatcher134424._instance = CommutativeMatcher134424()
        return CommutativeMatcher134424._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 134423
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 134425
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 134426
                    if len(subjects) == 0:
                        pass
                        # 0: x**n
                        yield 0, subst2
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 134427
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1.2.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 134428
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 134429
                        if len(subjects5) == 0:
                            pass
                            # State 134430
                            if len(subjects) == 0:
                                pass
                                # 0: x**n
                                yield 0, subst2
                    if len(subjects5) >= 1:
                        tmp9 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 134429
                            if len(subjects5) == 0:
                                pass
                                # State 134430
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects5.appendleft(tmp9)
                subjects5.appendleft(tmp6)
            subjects.appendleft(tmp4)
        return
        yield


from collections import deque