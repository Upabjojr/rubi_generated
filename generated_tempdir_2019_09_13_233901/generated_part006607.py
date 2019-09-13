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

class CommutativeMatcher14171(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.1.2.0', 1, 1, None), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 0
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher14171._instance is None:
            CommutativeMatcher14171._instance = CommutativeMatcher14171()
        return CommutativeMatcher14171._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 14170
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 14172
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 14173
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1.2.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 14174
                        if len(subjects3) >= 1 and subjects3[0] == 2:
                            tmp6 = subjects3.popleft()
                            # State 14175
                            if len(subjects3) == 0:
                                pass
                                # State 14176
                                if len(subjects) == 0:
                                    pass
                                    # 0: d*x**2
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp7 = subjects.popleft()
            associative1 = tmp7
            associative_type1 = type(tmp7)
            subjects8 = deque(tmp7._args)
            matcher = CommutativeMatcher14178.get()
            tmp9 = subjects8
            subjects8 = []
            for s in tmp9:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp9, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 14183
                    if len(subjects) == 0:
                        pass
                        # 0: d*x**2
            subjects.appendleft(tmp7)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
