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


class CommutativeMatcher13017(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.1.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher13017._instance is None:
            CommutativeMatcher13017._instance = CommutativeMatcher13017()
        return CommutativeMatcher13017._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 13016
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.1.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 13018
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 13019
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 13020
                        if len(subjects3) >= 1 and subjects3[0] == Rational(1, 2):
                            tmp6 = subjects3.popleft()
                            # State 13021
                            if len(subjects3) == 0:
                                pass
                                # State 13022
                                if len(subjects) == 0:
                                    pass
                                    # 0: k*sqrt(v)
                                    yield 0, subst2
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp7 = subjects.popleft()
            associative1 = tmp7
            associative_type1 = type(tmp7)
            subjects8 = deque(tmp7._args)
            matcher = CommutativeMatcher13024.get()
            tmp9 = subjects8
            subjects8 = []
            for s in tmp9:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp9, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 13029
                    if len(subjects) == 0:
                        pass
                        # 0: k*sqrt(v)
                        yield 0, subst1
            subjects.appendleft(tmp7)
        return
        yield


from .generated_part002328 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset