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


class CommutativeMatcher21590(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.2.2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.2.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.2.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.2.1.2.2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.2.2.1.1', 1, 1, None), Mul)
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
        if CommutativeMatcher21590._instance is None:
            CommutativeMatcher21590._instance = CommutativeMatcher21590()
        return CommutativeMatcher21590._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 21589
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 29687
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.2.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 29688
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 29689
                            if len(subjects2) == 0:
                                pass
                                # State 29690
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**m
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp7 = subjects2.popleft()
                        # State 44596
                        if len(subjects2) == 0:
                            pass
                            # State 44597
                            if len(subjects) == 0:
                                pass
                                # 1: x**2
                                yield 1, subst1
                        subjects2.appendleft(tmp7)
                subjects2.appendleft(tmp3)
            subjects.appendleft(tmp1)
        return
        yield


from collections import deque