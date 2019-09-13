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

class CommutativeMatcher59426(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher59426._instance is None:
            CommutativeMatcher59426._instance = CommutativeMatcher59426()
        return CommutativeMatcher59426._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 59425
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 59427
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 59428
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 89584
                    if len(subjects) == 0:
                        pass
                        # 3: b*x
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 89377
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.4.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 89378
                if len(subjects) >= 1:
                    tmp8 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.4.1.1', tmp8)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89379
                        if len(subjects) == 0:
                            pass
                            # 1: b*x**n
                    subjects.appendleft(tmp8)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp10 = subjects.popleft()
                subjects11 = deque(tmp10._args)
                # State 89380
                if len(subjects11) >= 1:
                    tmp12 = subjects11.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.1', tmp12)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 89381
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 89382
                            if len(subjects11) == 0:
                                pass
                                # State 89383
                                if len(subjects) == 0:
                                    pass
                                    # 1: b*x**n
                        if len(subjects11) >= 1:
                            tmp15 = subjects11.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.2', tmp15)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 89382
                                if len(subjects11) == 0:
                                    pass
                                    # State 89383
                                    if len(subjects) == 0:
                                        pass
                                        # 1: b*x**n
                            subjects11.appendleft(tmp15)
                        if len(subjects11) >= 1 and subjects11[0] == 2:
                            tmp17 = subjects11.popleft()
                            # State 89579
                            if len(subjects11) == 0:
                                pass
                                # State 89580
                                if len(subjects) == 0:
                                    pass
                                    # 2: c*x**2
                            subjects11.appendleft(tmp17)
                    subjects11.appendleft(tmp12)
                subjects.appendleft(tmp10)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp18 = subjects.popleft()
            associative1 = tmp18
            associative_type1 = type(tmp18)
            subjects19 = deque(tmp18._args)
            matcher = CommutativeMatcher59430.get()
            tmp20 = subjects19
            subjects19 = []
            for s in tmp20:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp20, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 59431
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 89390
                    if len(subjects) == 0:
                        pass
                        # 1: b*x**n
                if pattern_index == 2:
                    pass
                    # State 89583
                    if len(subjects) == 0:
                        pass
                        # 2: c*x**2
                if pattern_index == 3:
                    pass
                    # State 89585
                    if len(subjects) == 0:
                        pass
                        # 3: b*x
            subjects.appendleft(tmp18)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
