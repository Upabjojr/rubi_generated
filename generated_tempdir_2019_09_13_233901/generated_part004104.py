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

class CommutativeMatcher3794(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1, 2: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({3: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, None), Add)
]),
    3: (3, Multiset({4: 1}), [
      (VariableWithCount('i2.2.0_4', 1, 1, None), Add)
]),
    4: (4, Multiset({5: 1}), [
      (VariableWithCount('i2.2.0_4', 1, 1, None), Add)
]),
    5: (5, Multiset({6: 1}), [
      (VariableWithCount('i2.2.0_4', 1, 1, None), Add)
]),
    6: (6, Multiset({7: 1}), [
      (VariableWithCount('i2.2.0_4', 1, 1, None), Add)
]),
    7: (7, Multiset({8: 1}), [
      (VariableWithCount('i2.2.0_5', 1, 1, None), Add)
]),
    8: (8, Multiset({9: 1}), [
      (VariableWithCount('i2.2.0_3', 1, 1, S(0)), Add)
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
        if CommutativeMatcher3794._instance is None:
            CommutativeMatcher3794._instance = CommutativeMatcher3794()
        return CommutativeMatcher3794._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 3793
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_4', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 3795
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 3796
                    if len(subjects) == 0:
                        pass
                        # 0: x*h
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp4 = subjects.popleft()
                subjects5 = deque(tmp4._args)
                # State 5886
                if len(subjects5) >= 1:
                    tmp6 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp6)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 5887
                        if len(subjects5) >= 1 and subjects5[0] == 2:
                            tmp8 = subjects5.popleft()
                            # State 5888
                            if len(subjects5) == 0:
                                pass
                                # State 5889
                                if len(subjects) == 0:
                                    pass
                                    # 1: v**2*f
                            subjects5.appendleft(tmp8)
                    subjects5.appendleft(tmp6)
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_5', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 5895
            if len(subjects) >= 1:
                tmp10 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp10)
                except ValueError:
                    pass
                else:
                    pass
                    # State 5896
                    if len(subjects) == 0:
                        pass
                        # 2: x*e
                subjects.appendleft(tmp10)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 7908
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp13 = subjects.popleft()
                subjects14 = deque(tmp13._args)
                # State 7909
                if len(subjects14) >= 1:
                    tmp15 = subjects14.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1', tmp15)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7910
                        if len(subjects14) >= 1:
                            tmp17 = subjects14.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2', tmp17)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7911
                                if len(subjects14) == 0:
                                    pass
                                    # State 7912
                                    if len(subjects) == 0:
                                        pass
                                        # 3: f*x**n
                            subjects14.appendleft(tmp17)
                    subjects14.appendleft(tmp15)
                subjects.appendleft(tmp13)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 7934
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp20 = subjects.popleft()
                subjects21 = deque(tmp20._args)
                # State 7935
                if len(subjects21) >= 1:
                    tmp22 = subjects21.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp22)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7936
                        if len(subjects21) >= 1:
                            tmp24 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp24)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7937
                                if len(subjects21) == 0:
                                    pass
                                    # State 7938
                                    if len(subjects) == 0:
                                        pass
                                        # 4: x**n*f
                            subjects21.appendleft(tmp24)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8101
                            if len(subjects21) == 0:
                                pass
                                # State 8102
                                if len(subjects) == 0:
                                    pass
                                    # 7: x**n2*f1
                        if len(subjects21) >= 1:
                            tmp27 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp27)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 8101
                                if len(subjects21) == 0:
                                    pass
                                    # State 8102
                                    if len(subjects) == 0:
                                        pass
                                        # 7: x**n2*f1
                            subjects21.appendleft(tmp27)
                    subjects21.appendleft(tmp22)
                if len(subjects21) >= 1:
                    tmp29 = subjects21.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp29)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7966
                        if len(subjects21) >= 1:
                            tmp31 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', tmp31)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 7967
                                if len(subjects21) == 0:
                                    pass
                                    # State 7968
                                    if len(subjects) == 0:
                                        pass
                                        # 5: x**n*f
                            subjects21.appendleft(tmp31)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8073
                            if len(subjects21) == 0:
                                pass
                                # State 8074
                                if len(subjects) == 0:
                                    pass
                                    # 6: x**n*f
                        if len(subjects21) >= 1:
                            tmp34 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp34)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 8073
                                if len(subjects21) == 0:
                                    pass
                                    # State 8074
                                    if len(subjects) == 0:
                                        pass
                                        # 6: x**n*f
                            subjects21.appendleft(tmp34)
                    subjects21.appendleft(tmp29)
                subjects.appendleft(tmp20)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 8071
                if len(subjects) >= 1:
                    tmp37 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0_1', tmp37)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8072
                        if len(subjects) == 0:
                            pass
                            # 6: x**n*f
                    subjects.appendleft(tmp37)
                if len(subjects) >= 1:
                    tmp39 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0', tmp39)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8100
                        if len(subjects) == 0:
                            pass
                            # 7: x**n2*f1
                    subjects.appendleft(tmp39)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_3', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 8118
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 8119
                if len(subjects) >= 1:
                    tmp43 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.0', tmp43)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8120
                        if len(subjects) == 0:
                            pass
                            # 8: x**n2*f2
                    subjects.appendleft(tmp43)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp45 = subjects.popleft()
                subjects46 = deque(tmp45._args)
                # State 8121
                if len(subjects46) >= 1:
                    tmp47 = subjects46.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp47)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 8122
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2_1', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 8123
                            if len(subjects46) == 0:
                                pass
                                # State 8124
                                if len(subjects) == 0:
                                    pass
                                    # 8: x**n2*f2
                        if len(subjects46) >= 1:
                            tmp50 = subjects46.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2_1', tmp50)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 8123
                                if len(subjects46) == 0:
                                    pass
                                    # State 8124
                                    if len(subjects) == 0:
                                        pass
                                        # 8: x**n2*f2
                            subjects46.appendleft(tmp50)
                    subjects46.appendleft(tmp47)
                subjects.appendleft(tmp45)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_7', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 151701
            if len(subjects) >= 1:
                tmp53 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0_6', tmp53)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151702
                    if len(subjects) == 0:
                        pass
                        # 9: z*h
                subjects.appendleft(tmp53)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp55 = subjects.popleft()
            associative1 = tmp55
            associative_type1 = type(tmp55)
            subjects56 = deque(tmp55._args)
            matcher = CommutativeMatcher3798.get()
            tmp57 = subjects56
            subjects56 = []
            for s in tmp57:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp57, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 3799
                    if len(subjects) == 0:
                        pass
                        # 0: x*h
                if pattern_index == 1:
                    pass
                    # State 5894
                    if len(subjects) == 0:
                        pass
                        # 1: v**2*f
                if pattern_index == 2:
                    pass
                    # State 5897
                    if len(subjects) == 0:
                        pass
                        # 2: x*e
                if pattern_index == 3:
                    pass
                    # State 7916
                    if len(subjects) == 0:
                        pass
                        # 3: f*x**n
                if pattern_index == 4:
                    pass
                    # State 7942
                    if len(subjects) == 0:
                        pass
                        # 4: x**n*f
                if pattern_index == 5:
                    pass
                    # State 7972
                    if len(subjects) == 0:
                        pass
                        # 5: x**n*f
                if pattern_index == 6:
                    pass
                    # State 8079
                    if len(subjects) == 0:
                        pass
                        # 6: x**n*f
                if pattern_index == 7:
                    pass
                    # State 8106
                    if len(subjects) == 0:
                        pass
                        # 7: x**n2*f1
                if pattern_index == 8:
                    pass
                    # State 8125
                    if len(subjects) == 0:
                        pass
                        # 8: x**n2*f2
                if pattern_index == 9:
                    pass
                    # State 151703
                    if len(subjects) == 0:
                        pass
                        # 9: z*h
            subjects.appendleft(tmp55)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
