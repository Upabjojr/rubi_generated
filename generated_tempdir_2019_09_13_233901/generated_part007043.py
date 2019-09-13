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

class CommutativeMatcher125827(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1, 4: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({5: 1, 6: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({7: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({9: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({10: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, None), Add)
]),
    9: (9, Multiset({11: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher125827._instance is None:
            CommutativeMatcher125827._instance = CommutativeMatcher125827()
        return CommutativeMatcher125827._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 125826
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 125828
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125829
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp4 = subjects.popleft()
                subjects5 = deque(tmp4._args)
                # State 127955
                if len(subjects5) >= 1:
                    tmp6 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp6)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 127956
                        if len(subjects5) >= 1:
                            tmp8 = subjects5.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp8)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 127957
                                if len(subjects5) == 0:
                                    pass
                                    # State 127958
                                    if len(subjects) == 0:
                                        pass
                                        # 1: x**n*b
                            subjects5.appendleft(tmp8)
                    subjects5.appendleft(tmp6)
                if len(subjects5) >= 1:
                    tmp10 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.1', tmp10)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 129104
                        if len(subjects5) >= 1 and subjects5[0] == 2:
                            tmp12 = subjects5.popleft()
                            # State 129105
                            if len(subjects5) == 0:
                                pass
                                # State 129106
                                if len(subjects) == 0:
                                    pass
                                    # 3: c*x**2
                            subjects5.appendleft(tmp12)
                    subjects5.appendleft(tmp10)
                if len(subjects5) >= 1:
                    tmp13 = subjects5.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp13)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 129135
                        if len(subjects5) >= 1 and subjects5[0] == 2:
                            tmp15 = subjects5.popleft()
                            # State 129136
                            if len(subjects5) == 0:
                                pass
                                # State 129137
                                if len(subjects) == 0:
                                    pass
                                    # 5: x**2*c
                            subjects5.appendleft(tmp15)
                    subjects5.appendleft(tmp13)
                subjects.appendleft(tmp4)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 128755
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.4.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 128756
                if len(subjects) >= 1:
                    tmp18 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.4.1.1', tmp18)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128757
                        if len(subjects) == 0:
                            pass
                            # 2: b*x**n
                    subjects.appendleft(tmp18)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp20 = subjects.popleft()
                subjects21 = deque(tmp20._args)
                # State 128758
                if len(subjects21) >= 1:
                    tmp22 = subjects21.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.1', tmp22)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128759
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 128760
                            if len(subjects21) == 0:
                                pass
                                # State 128761
                                if len(subjects) == 0:
                                    pass
                                    # 2: b*x**n
                        if len(subjects21) >= 1:
                            tmp25 = subjects21.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.2', tmp25)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 128760
                                if len(subjects21) == 0:
                                    pass
                                    # State 128761
                                    if len(subjects) == 0:
                                        pass
                                        # 2: b*x**n
                            subjects21.appendleft(tmp25)
                    subjects21.appendleft(tmp22)
                subjects.appendleft(tmp20)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 129111
            if len(subjects) >= 1:
                tmp28 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1', tmp28)
                except ValueError:
                    pass
                else:
                    pass
                    # State 129112
                    if len(subjects) == 0:
                        pass
                        # 4: b*x
                subjects.appendleft(tmp28)
            if len(subjects) >= 1:
                tmp30 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp30)
                except ValueError:
                    pass
                else:
                    pass
                    # State 129142
                    if len(subjects) == 0:
                        pass
                        # 6: x*b
                subjects.appendleft(tmp30)
            if len(subjects) >= 1:
                tmp32 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1.0', tmp32)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132618
                    if len(subjects) == 0:
                        pass
                        # 9: e*x
                subjects.appendleft(tmp32)
            if len(subjects) >= 1:
                tmp34 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp34)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137634
                    if len(subjects) == 0:
                        pass
                        # 11: x*e
                subjects.appendleft(tmp34)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132140
            if len(subjects) >= 1:
                tmp37 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp37)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132141
                    if len(subjects) == 0:
                        pass
                        # 7: x*b
                subjects.appendleft(tmp37)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 132434
            if len(subjects) >= 1:
                tmp40 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp40)
                except ValueError:
                    pass
                else:
                    pass
                    # State 132435
                    if len(subjects) == 0:
                        pass
                        # 8: x*f
                subjects.appendleft(tmp40)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 137618
            if len(subjects) >= 1:
                tmp43 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp43)
                except ValueError:
                    pass
                else:
                    pass
                    # State 137619
                    if len(subjects) == 0:
                        pass
                        # 10: x*d
                subjects.appendleft(tmp43)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp45 = subjects.popleft()
            associative1 = tmp45
            associative_type1 = type(tmp45)
            subjects46 = deque(tmp45._args)
            matcher = CommutativeMatcher125831.get()
            tmp47 = subjects46
            subjects46 = []
            for s in tmp47:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp47, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 125832
                    if len(subjects) == 0:
                        pass
                        # 0: x*b
                if pattern_index == 1:
                    pass
                    # State 127963
                    if len(subjects) == 0:
                        pass
                        # 1: x**n*b
                if pattern_index == 2:
                    pass
                    # State 128767
                    if len(subjects) == 0:
                        pass
                        # 2: b*x**n
                if pattern_index == 3:
                    pass
                    # State 129110
                    if len(subjects) == 0:
                        pass
                        # 3: c*x**2
                if pattern_index == 4:
                    pass
                    # State 129113
                    if len(subjects) == 0:
                        pass
                        # 4: b*x
                if pattern_index == 5:
                    pass
                    # State 129141
                    if len(subjects) == 0:
                        pass
                        # 5: x**2*c
                if pattern_index == 6:
                    pass
                    # State 129143
                    if len(subjects) == 0:
                        pass
                        # 6: x*b
                if pattern_index == 7:
                    pass
                    # State 132142
                    if len(subjects) == 0:
                        pass
                        # 7: x*b
                if pattern_index == 8:
                    pass
                    # State 132436
                    if len(subjects) == 0:
                        pass
                        # 8: x*f
                if pattern_index == 9:
                    pass
                    # State 132619
                    if len(subjects) == 0:
                        pass
                        # 9: e*x
                if pattern_index == 10:
                    pass
                    # State 137620
                    if len(subjects) == 0:
                        pass
                        # 10: x*d
                if pattern_index == 11:
                    pass
                    # State 137635
                    if len(subjects) == 0:
                        pass
                        # 11: x*e
            subjects.appendleft(tmp45)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
