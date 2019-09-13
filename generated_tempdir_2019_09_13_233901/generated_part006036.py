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

class CommutativeMatcher17761(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher17761._instance is None:
            CommutativeMatcher17761._instance = CommutativeMatcher17761()
        return CommutativeMatcher17761._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 17760
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 17762
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 17763
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.1.0', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17764
                        if len(subjects) == 0:
                            pass
                            # 0: c + x*d
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp5 = subjects.popleft()
                associative1 = tmp5
                associative_type1 = type(tmp5)
                subjects6 = deque(tmp5._args)
                matcher = CommutativeMatcher17766.get()
                tmp7 = subjects6
                subjects6 = []
                for s in tmp7:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp7, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 17767
                        if len(subjects) == 0:
                            pass
                            # 0: c + x*d
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 18083
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.3.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 18084
                if len(subjects) >= 1:
                    tmp10 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.3.1.1.0', tmp10)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 18085
                        if len(subjects) == 0:
                            pass
                            # 1: c + x*d
                    subjects.appendleft(tmp10)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp12 = subjects.popleft()
                associative1 = tmp12
                associative_type1 = type(tmp12)
                subjects13 = deque(tmp12._args)
                matcher = CommutativeMatcher18087.get()
                tmp14 = subjects13
                subjects13 = []
                for s in tmp14:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp14, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 18088
                        if len(subjects) == 0:
                            pass
                            # 1: c + x*d
                subjects.appendleft(tmp12)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp15 = subjects.popleft()
            associative1 = tmp15
            associative_type1 = type(tmp15)
            subjects16 = deque(tmp15._args)
            matcher = CommutativeMatcher17769.get()
            tmp17 = subjects16
            subjects16 = []
            for s in tmp17:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp17, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 17775
                    if len(subjects) == 0:
                        pass
                        # 0: c + x*d
                if pattern_index == 1:
                    pass
                    # State 18092
                    if len(subjects) == 0:
                        pass
                        # 1: c + x*d
            subjects.appendleft(tmp15)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
