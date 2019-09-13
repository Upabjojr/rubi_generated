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

class CommutativeMatcher128710(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1, 2: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({3: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({4: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({5: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
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
        if CommutativeMatcher128710._instance is None:
            CommutativeMatcher128710._instance = CommutativeMatcher128710()
        return CommutativeMatcher128710._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 128709
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 128711
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.4.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 128712
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.4.1.1', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128713
                        if len(subjects) == 0:
                            pass
                            # 0: b*x**n
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 128714
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128715
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 128716
                            if len(subjects6) == 0:
                                pass
                                # State 128717
                                if len(subjects) == 0:
                                    pass
                                    # 0: b*x**n
                        if len(subjects6) >= 1:
                            tmp10 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.2', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 128716
                                if len(subjects6) == 0:
                                    pass
                                    # State 128717
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**n
                            subjects6.appendleft(tmp10)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 129121
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp13 = subjects.popleft()
                subjects14 = deque(tmp13._args)
                # State 129122
                if len(subjects14) >= 1:
                    tmp15 = subjects14.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp15)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 129123
                        if len(subjects14) >= 1 and subjects14[0] == 2:
                            tmp17 = subjects14.popleft()
                            # State 129124
                            if len(subjects14) == 0:
                                pass
                                # State 129125
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**2*c
                            subjects14.appendleft(tmp17)
                    subjects14.appendleft(tmp15)
                subjects.appendleft(tmp13)
            if len(subjects) >= 1:
                tmp18 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp18)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132183
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                subjects.appendleft(tmp18)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 129130
            if len(subjects) >= 1:
                tmp21 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp21)
                except ValueError:
                    pass
                else:
                    pass
                    # State 129131
                    if len(subjects) == 0:
                        pass
                        # 2: x*b
                subjects.appendleft(tmp21)
            if len(subjects) >= 1:
                tmp23 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1.0', tmp23)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132602
                    if len(subjects) == 0:
                        pass
                        # 5: e*x
                subjects.appendleft(tmp23)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132126
            if len(subjects) >= 1:
                tmp26 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp26)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132127
                    if len(subjects) == 0:
                        pass
                        # 3: x*b
                subjects.appendleft(tmp26)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp28 = subjects.popleft()
            associative1 = tmp28
            associative_type1 = type(tmp28)
            subjects29 = deque(tmp28._args)
            matcher = CommutativeMatcher128719.get()
            tmp30 = subjects29
            subjects29 = []
            for s in tmp30:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp30, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 128726
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**n
                if pattern_index == 1:
                    pass
                    # State 129129
                    if len(subjects) == 0:
                        pass
                        # 1: x**2*c
                if pattern_index == 2:
                    pass
                    # State 129132
                    if len(subjects) == 0:
                        pass
                        # 2: x*b
                if pattern_index == 3:
                    pass
                    # State 132128
                    if len(subjects) == 0:
                        pass
                        # 3: x*b
                if pattern_index == 4:
                    pass
                    # State 132184
                    if len(subjects) == 0:
                        pass
                        # 4: x*b
                if pattern_index == 5:
                    pass
                    # State 132603
                    if len(subjects) == 0:
                        pass
                        # 5: e*x
            subjects.appendleft(tmp28)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
