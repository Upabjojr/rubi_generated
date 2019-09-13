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

class CommutativeMatcher23891(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.2.2.1.0', 1, 1, None), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher23891._instance is None:
            CommutativeMatcher23891._instance = CommutativeMatcher23891()
        return CommutativeMatcher23891._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 23890
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 40496
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 40497
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40498
                            if len(subjects2) == 0:
                                pass
                                # State 40499
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**mn
                        subjects2.appendleft(tmp5)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 40525
                        if len(subjects2) == 0:
                            pass
                            # State 40526
                            if len(subjects) == 0:
                                pass
                                # 1: x**n
                    if len(subjects2) >= 1:
                        tmp8 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp8)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40525
                            if len(subjects2) == 0:
                                pass
                                # State 40526
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                        subjects2.appendleft(tmp8)
                subjects2.appendleft(tmp3)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 40523
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 40524
                    if len(subjects) == 0:
                        pass
                        # 1: x**n
                subjects.appendleft(tmp11)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
