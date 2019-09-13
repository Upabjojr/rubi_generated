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

class CommutativeMatcher124324(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher124324._instance is None:
            CommutativeMatcher124324._instance = CommutativeMatcher124324()
        return CommutativeMatcher124324._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 124323
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 124325
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 124326
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124327
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124328
                                if len(subjects3) == 0:
                                    pass
                                    # State 124329
                                    if len(subjects) == 0:
                                        pass
                                        # 0: x**n*d
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                if len(subjects3) >= 1:
                    tmp8 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp8)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124830
                        if len(subjects3) >= 1:
                            tmp10 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124831
                                if len(subjects3) == 0:
                                    pass
                                    # State 124832
                                    if len(subjects) == 0:
                                        pass
                                        # 1: x**n*d
                            subjects3.appendleft(tmp10)
                    subjects3.appendleft(tmp8)
                if len(subjects3) >= 1:
                    tmp12 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp12)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125217
                        if len(subjects3) >= 1:
                            tmp14 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp14)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125218
                                if len(subjects3) == 0:
                                    pass
                                    # State 125219
                                    if len(subjects) == 0:
                                        pass
                                        # 2: d*x**n
                            subjects3.appendleft(tmp14)
                    subjects3.appendleft(tmp12)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp16 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp16)
                except ValueError:
                    pass
                else:
                    pass
                    # State 136864
                    if len(subjects) == 0:
                        pass
                        # 3: x*b
                subjects.appendleft(tmp16)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp18 = subjects.popleft()
            associative1 = tmp18
            associative_type1 = type(tmp18)
            subjects19 = deque(tmp18._args)
            matcher = CommutativeMatcher124331.get()
            tmp20 = subjects19
            subjects19 = []
            for s in tmp20:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp20, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 124336
                    if len(subjects) == 0:
                        pass
                        # 0: x**n*d
                if pattern_index == 1:
                    pass
                    # State 124836
                    if len(subjects) == 0:
                        pass
                        # 1: x**n*d
                if pattern_index == 2:
                    pass
                    # State 125223
                    if len(subjects) == 0:
                        pass
                        # 2: d*x**n
                if pattern_index == 3:
                    pass
                    # State 136865
                    if len(subjects) == 0:
                        pass
                        # 3: x*b
            subjects.appendleft(tmp18)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
