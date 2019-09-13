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

class CommutativeMatcher14805(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.4.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.4.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.4.0_1', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher14805._instance is None:
            CommutativeMatcher14805._instance = CommutativeMatcher14805()
        return CommutativeMatcher14805._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 14804
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 14806
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.4.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 14807
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.4.1.1.0', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 14808
                        if len(subjects) == 0:
                            pass
                            # 0: e + x*f
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp5 = subjects.popleft()
                associative1 = tmp5
                associative_type1 = type(tmp5)
                subjects6 = deque(tmp5._args)
                matcher = CommutativeMatcher14810.get()
                tmp7 = subjects6
                subjects6 = []
                for s in tmp7:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp7, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 14811
                        if len(subjects) == 0:
                            pass
                            # 0: e + x*f
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp8 = subjects.popleft()
            associative1 = tmp8
            associative_type1 = type(tmp8)
            subjects9 = deque(tmp8._args)
            matcher = CommutativeMatcher14813.get()
            tmp10 = subjects9
            subjects9 = []
            for s in tmp10:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp10, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 14819
                    if len(subjects) == 0:
                        pass
                        # 0: e + x*f
            subjects.appendleft(tmp8)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
