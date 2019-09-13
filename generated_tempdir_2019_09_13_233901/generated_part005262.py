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

class CommutativeMatcher61903(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.4.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.2.3.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher61903._instance is None:
            CommutativeMatcher61903._instance = CommutativeMatcher61903()
        return CommutativeMatcher61903._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 61902
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 61904
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 61905
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 63916
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 63917
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 64484
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 64485
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 64708
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 64709
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 91195
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.4.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 91196
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 92145
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.3.1.0', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 92146
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                subjects.appendleft(tmp17)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 98827
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp20 = subjects.popleft()
                subjects21 = deque(tmp20._args)
                # State 98828
                if len(subjects21) >= 1:
                    tmp22 = subjects21.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.1', tmp22)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98829
                        if len(subjects21) >= 1:
                            tmp24 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.2', tmp24)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 98830
                                if len(subjects21) == 0:
                                    pass
                                    # State 98831
                                    if len(subjects) == 0:
                                        pass
                                        # 6: d*x**n
                            subjects21.appendleft(tmp24)
                    subjects21.appendleft(tmp22)
                if len(subjects21) >= 1:
                    tmp26 = subjects21.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp26)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 99390
                        if len(subjects21) >= 1:
                            tmp28 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.2', tmp28)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 99391
                                if len(subjects21) == 0:
                                    pass
                                    # State 99392
                                    if len(subjects) == 0:
                                        pass
                                        # 7: x**n*d
                            subjects21.appendleft(tmp28)
                    subjects21.appendleft(tmp26)
                subjects.appendleft(tmp20)
            if len(subjects) >= 1:
                tmp30 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp30)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107554
                    if len(subjects) == 0:
                        pass
                        # 8: x*e
                subjects.appendleft(tmp30)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp32 = subjects.popleft()
            associative1 = tmp32
            associative_type1 = type(tmp32)
            subjects33 = deque(tmp32._args)
            matcher = CommutativeMatcher61907.get()
            tmp34 = subjects33
            subjects33 = []
            for s in tmp34:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp34, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 61908
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 63918
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                if pattern_index == 2:
                    pass
                    # State 64486
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                if pattern_index == 3:
                    pass
                    # State 64710
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                if pattern_index == 4:
                    pass
                    # State 91197
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                if pattern_index == 5:
                    pass
                    # State 92147
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                if pattern_index == 6:
                    pass
                    # State 98836
                    if len(subjects) == 0:
                        pass
                        # 6: d*x**n
                if pattern_index == 7:
                    pass
                    # State 99396
                    if len(subjects) == 0:
                        pass
                        # 7: x**n*d
                if pattern_index == 8:
                    pass
                    # State 107555
                    if len(subjects) == 0:
                        pass
                        # 8: x*e
            subjects.appendleft(tmp32)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
