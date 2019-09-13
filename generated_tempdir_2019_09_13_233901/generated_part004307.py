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

class CommutativeMatcher128719(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.4.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.4.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.4.1.0_1', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({}), [
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.3.1.1.0', 1, 1, None), Mul)
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
        if CommutativeMatcher128719._instance is None:
            CommutativeMatcher128719._instance = CommutativeMatcher128719()
        return CommutativeMatcher128719._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 128718
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 128720
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 128721
                    if len(subjects) == 0:
                        pass
                        # 0: x**n
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 128722
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.1.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 128723
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128724
                        if len(subjects5) == 0:
                            pass
                            # State 128725
                            if len(subjects) == 0:
                                pass
                                # 0: x**n
                    if len(subjects5) >= 1:
                        tmp9 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.4.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 128724
                            if len(subjects5) == 0:
                                pass
                                # State 128725
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects5.appendleft(tmp9)
                subjects5.appendleft(tmp6)
            if len(subjects5) >= 1:
                tmp11 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 129126
                    if len(subjects5) >= 1 and subjects5[0] == 2:
                        tmp13 = subjects5.popleft()
                        # State 129127
                        if len(subjects5) == 0:
                            pass
                            # State 129128
                            if len(subjects) == 0:
                                pass
                                # 1: x**2
                        subjects5.appendleft(tmp13)
                subjects5.appendleft(tmp11)
            subjects.appendleft(tmp4)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
