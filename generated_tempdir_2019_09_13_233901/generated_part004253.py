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

class CommutativeMatcher117129(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher117129._instance is None:
            CommutativeMatcher117129._instance = CommutativeMatcher117129()
        return CommutativeMatcher117129._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 117128
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 117130
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 117131
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.2.1.1', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 117132
                        if len(subjects) == 0:
                            pass
                            # 0: b*x**n
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 117133
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.2.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 117134
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 117135
                            if len(subjects6) == 0:
                                pass
                                # State 117136
                                if len(subjects) == 0:
                                    pass
                                    # 0: b*x**n
                        if len(subjects6) >= 1:
                            tmp10 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.2.1.2', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 117135
                                if len(subjects6) == 0:
                                    pass
                                    # State 117136
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**n
                            subjects6.appendleft(tmp10)
                    subjects6.appendleft(tmp7)
                if len(subjects6) >= 1:
                    tmp12 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp12)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 117464
                        if len(subjects6) >= 1 and subjects6[0] == 2:
                            tmp14 = subjects6.popleft()
                            # State 117465
                            if len(subjects6) == 0:
                                pass
                                # State 117466
                                if len(subjects) == 0:
                                    pass
                                    # 2: x**2*b
                            subjects6.appendleft(tmp14)
                    subjects6.appendleft(tmp12)
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 117389
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp16 = subjects.popleft()
                subjects17 = deque(tmp16._args)
                # State 117390
                if len(subjects17) >= 1:
                    tmp18 = subjects17.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp18)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 117391
                        if len(subjects17) >= 1 and subjects17[0] == 2:
                            tmp20 = subjects17.popleft()
                            # State 117392
                            if len(subjects17) == 0:
                                pass
                                # State 117393
                                if len(subjects) == 0:
                                    pass
                                    # 1: e*x**2
                            subjects17.appendleft(tmp20)
                    subjects17.appendleft(tmp18)
                subjects.appendleft(tmp16)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp21 = subjects.popleft()
            associative1 = tmp21
            associative_type1 = type(tmp21)
            subjects22 = deque(tmp21._args)
            matcher = CommutativeMatcher117138.get()
            tmp23 = subjects22
            subjects22 = []
            for s in tmp23:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp23, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 117145
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**n
                if pattern_index == 1:
                    pass
                    # State 117397
                    if len(subjects) == 0:
                        pass
                        # 1: e*x**2
                if pattern_index == 2:
                    pass
                    # State 117467
                    if len(subjects) == 0:
                        pass
                        # 2: x**2*b
            subjects.appendleft(tmp21)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque