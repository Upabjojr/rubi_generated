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


class CommutativeMatcher121853(CommutativeMatcher):
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
        if CommutativeMatcher121853._instance is None:
            CommutativeMatcher121853._instance = CommutativeMatcher121853()
        return CommutativeMatcher121853._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 121852
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 121854
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 121855
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp4 = subjects.popleft()
                subjects5 = deque(tmp4._args)
                # State 124081
                if len(subjects5) >= 1:
                    tmp6 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp6)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124082
                        if len(subjects5) >= 1:
                            tmp8 = subjects5.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp8)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124083
                                if len(subjects5) == 0:
                                    pass
                                    # State 124084
                                    if len(subjects) == 0:
                                        pass
                                        # 1: x**n*d
                                        yield 1, subst3
                            subjects5.appendleft(tmp8)
                    subjects5.appendleft(tmp6)
                if len(subjects5) >= 1:
                    tmp10 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp10)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 124667
                        if len(subjects5) >= 1:
                            tmp12 = subjects5.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 124668
                                if len(subjects5) == 0:
                                    pass
                                    # State 124669
                                    if len(subjects) == 0:
                                        pass
                                        # 2: x**n*d
                                        yield 2, subst3
                            subjects5.appendleft(tmp12)
                    subjects5.appendleft(tmp10)
                if len(subjects5) >= 1:
                    tmp14 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp14)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125091
                        if len(subjects5) >= 1:
                            tmp16 = subjects5.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp16)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 125092
                                if len(subjects5) == 0:
                                    pass
                                    # State 125093
                                    if len(subjects) == 0:
                                        pass
                                        # 3: d*x**n
                                        yield 3, subst3
                            subjects5.appendleft(tmp16)
                    subjects5.appendleft(tmp14)
                subjects.appendleft(tmp4)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp18 = subjects.popleft()
            associative1 = tmp18
            associative_type1 = type(tmp18)
            subjects19 = deque(tmp18._args)
            matcher = CommutativeMatcher121857.get()
            tmp20 = subjects19
            subjects19 = []
            for s in tmp20:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp20, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 121858
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 124089
                    if len(subjects) == 0:
                        pass
                        # 1: x**n*d
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 124673
                    if len(subjects) == 0:
                        pass
                        # 2: x**n*d
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 125097
                    if len(subjects) == 0:
                        pass
                        # 3: d*x**n
                        yield 3, subst1
            subjects.appendleft(tmp18)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part003681 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset