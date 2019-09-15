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


class CommutativeMatcher13137(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i3.1.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i3.1.2.1.2.1.1', 1, 1, None), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i3.1.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher13137._instance is None:
            CommutativeMatcher13137._instance = CommutativeMatcher13137()
        return CommutativeMatcher13137._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 13136
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 13138
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp3 = subjects2.popleft()
                associative1 = tmp3
                associative_type1 = type(tmp3)
                subjects4 = deque(tmp3._args)
                matcher = CommutativeMatcher13140.get()
                tmp5 = subjects4
                subjects4 = []
                for s in tmp5:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp5, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 13156
                        if len(subjects2) >= 1 and subjects2[0] == Rational(1, 2):
                            tmp6 = subjects2.popleft()
                            # State 13157
                            if len(subjects2) == 0:
                                pass
                                # State 13158
                                if len(subjects) == 0:
                                    pass
                                    # 0: sqrt(a + b*x + c*x**2)
                                    yield 0, subst1
                            subjects2.appendleft(tmp6)
                    if pattern_index == 1:
                        pass
                        # State 13571
                        if len(subjects2) >= 1 and subjects2[0] == Rational(1, 2):
                            tmp7 = subjects2.popleft()
                            # State 13572
                            if len(subjects2) == 0:
                                pass
                                # State 13573
                                if len(subjects) == 0:
                                    pass
                                    # 1: sqrt(a + c*x**2)
                                    yield 1, subst1
                            subjects2.appendleft(tmp7)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp8 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.2.1.1', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 13675
                    if len(subjects2) >= 1 and subjects2[0] == Rational(1, 2):
                        tmp10 = subjects2.popleft()
                        # State 13676
                        if len(subjects2) == 0:
                            pass
                            # State 13677
                            if len(subjects) == 0:
                                pass
                                # 2: sqrt(v)
                                yield 2, subst1
                        subjects2.appendleft(tmp10)
                subjects2.appendleft(tmp8)
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part001028 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset