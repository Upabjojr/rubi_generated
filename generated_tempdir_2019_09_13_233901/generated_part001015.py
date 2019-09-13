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

class CommutativeMatcher53745(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher53745._instance is None:
            CommutativeMatcher53745._instance = CommutativeMatcher53745()
        return CommutativeMatcher53745._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 53744
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 53746
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 53747
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53748
                        if len(subjects3) >= 1 and subjects3[0] == 1/2:
                            tmp6 = subjects3.popleft()
                            # State 53749
                            if len(subjects3) == 0:
                                pass
                                # State 53750
                                if len(subjects) == 0:
                                    pass
                                    # 0: f*sqrt(u) /; (cons_f127) and (cons_f818) and (cons_f819)
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 53758
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0_1', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53759
                    if len(subjects) == 0:
                        pass
                        # 1: x*e /; (cons_f29) and (cons_f50) and (cons_f127) and (cons_f818) and (cons_f819) and (cons_f1240)
                subjects.appendleft(tmp8)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp10 = subjects.popleft()
            associative1 = tmp10
            associative_type1 = type(tmp10)
            subjects11 = deque(tmp10._args)
            matcher = CommutativeMatcher53752.get()
            tmp12 = subjects11
            subjects11 = []
            for s in tmp12:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp12, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 53757
                    if len(subjects) == 0:
                        pass
                        # 0: f*sqrt(u) /; (cons_f127) and (cons_f818) and (cons_f819)
                if pattern_index == 1:
                    pass
                    # State 53760
                    if len(subjects) == 0:
                        pass
                        # 1: x*e /; (cons_f29) and (cons_f50) and (cons_f127) and (cons_f818) and (cons_f819) and (cons_f1240)
            subjects.appendleft(tmp10)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
