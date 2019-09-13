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

class CommutativeMatcher13284(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i3.1.2.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i3.1.2.1.2.0', 1, 1, None), Add)
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
        if CommutativeMatcher13284._instance is None:
            CommutativeMatcher13284._instance = CommutativeMatcher13284()
        return CommutativeMatcher13284._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 13283
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 13285
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 13286
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.1.2.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 13287
                        if len(subjects3) >= 1 and subjects3[0] == 2:
                            tmp6 = subjects3.popleft()
                            # State 13288
                            if len(subjects3) == 0:
                                pass
                                # State 13289
                                if len(subjects) == 0:
                                    pass
                                    # 0: c*x**2
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 13297
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.2.1.1', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 13298
                    if len(subjects) == 0:
                        pass
                        # 1: b*x
                subjects.appendleft(tmp8)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp10 = subjects.popleft()
            associative1 = tmp10
            associative_type1 = type(tmp10)
            subjects11 = deque(tmp10._args)
            matcher = CommutativeMatcher13291.get()
            tmp12 = subjects11
            subjects11 = []
            for s in tmp12:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp12, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 13296
                    if len(subjects) == 0:
                        pass
                        # 0: c*x**2
                if pattern_index == 1:
                    pass
                    # State 13299
                    if len(subjects) == 0:
                        pass
                        # 1: b*x
            subjects.appendleft(tmp10)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
