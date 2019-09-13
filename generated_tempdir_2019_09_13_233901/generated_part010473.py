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

class CommutativeMatcher122449(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({4: 1}), [
      (VariableWithCount('i3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher122449._instance is None:
            CommutativeMatcher122449._instance = CommutativeMatcher122449()
        return CommutativeMatcher122449._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 122448
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 122450
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 122451
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 122452
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 122453
                                if len(subjects3) == 0:
                                    pass
                                    # State 122454
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**n /; (cons_f8) and (cons_f29) and (cons_f87) and (cons_f167)
                                        # 1: b*x**n /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1500)
                            subjects3.appendleft(tmp6)
                        if len(subjects3) >= 1 and subjects3[0] == 2:
                            tmp8 = subjects3.popleft()
                            # State 125568
                            if len(subjects3) == 0:
                                pass
                                # State 125569
                                if len(subjects) == 0:
                                    pass
                                    # 2: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f14)
                            subjects3.appendleft(tmp8)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp9 = subjects.popleft()
                subjects10 = deque(tmp9._args)
                # State 133906
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 133907
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 133908
                        if len(subjects10) >= 1:
                            tmp13 = subjects10.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1', tmp13)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 133909
                                if len(subjects10) == 0:
                                    pass
                                    # State 133910
                                    if len(subjects) == 0:
                                        pass
                                        # 4: b*log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1879)
                            subjects10.appendleft(tmp13)
                    if len(subjects10) >= 1 and isinstance(subjects10[0], Pow):
                        tmp15 = subjects10.popleft()
                        subjects16 = deque(tmp15._args)
                        # State 133911
                        if len(subjects16) >= 1:
                            tmp17 = subjects16.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1', tmp17)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 133912
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 133913
                                    if len(subjects16) == 0:
                                        pass
                                        # State 133914
                                        if len(subjects10) == 0:
                                            pass
                                            # State 133915
                                            if len(subjects) == 0:
                                                pass
                                                # 4: b*log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1879)
                                if len(subjects16) >= 1:
                                    tmp20 = subjects16.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i3.1.2.2', tmp20)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 133913
                                        if len(subjects16) == 0:
                                            pass
                                            # State 133914
                                            if len(subjects10) == 0:
                                                pass
                                                # State 133915
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: b*log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1879)
                                    subjects16.appendleft(tmp20)
                            subjects16.appendleft(tmp17)
                        subjects10.appendleft(tmp15)
                if len(subjects10) >= 1 and isinstance(subjects10[0], Mul):
                    tmp22 = subjects10.popleft()
                    associative1 = tmp22
                    associative_type1 = type(tmp22)
                    subjects23 = deque(tmp22._args)
                    matcher = CommutativeMatcher133917.get()
                    tmp24 = subjects23
                    subjects23 = []
                    for s in tmp24:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp24, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 133924
                            if len(subjects10) == 0:
                                pass
                                # State 133925
                                if len(subjects) == 0:
                                    pass
                                    # 4: b*log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1879)
                    subjects10.appendleft(tmp22)
                subjects.appendleft(tmp9)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 125573
            if len(subjects) >= 1:
                tmp26 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.1', tmp26)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125574
                    if len(subjects) == 0:
                        pass
                        # 3: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f14)
                subjects.appendleft(tmp26)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp28 = subjects.popleft()
            associative1 = tmp28
            associative_type1 = type(tmp28)
            subjects29 = deque(tmp28._args)
            matcher = CommutativeMatcher122456.get()
            tmp30 = subjects29
            subjects29 = []
            for s in tmp30:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp30, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 122461
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**n /; (cons_f8) and (cons_f29) and (cons_f87) and (cons_f167)
                        # 1: b*x**n /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1500)
                if pattern_index == 1:
                    pass
                    # State 125572
                    if len(subjects) == 0:
                        pass
                        # 2: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f14)
                if pattern_index == 2:
                    pass
                    # State 125575
                    if len(subjects) == 0:
                        pass
                        # 3: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f14)
                if pattern_index == 3:
                    pass
                    # State 133946
                    if len(subjects) == 0:
                        pass
                        # 4: b*log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1879)
            subjects.appendleft(tmp28)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
