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

class CommutativeMatcher122411(CommutativeMatcher):
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
        if CommutativeMatcher122411._instance is None:
            CommutativeMatcher122411._instance = CommutativeMatcher122411()
        return CommutativeMatcher122411._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 122410
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 122412
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 122413
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 122414
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 122415
                                if len(subjects3) == 0:
                                    pass
                                    # State 122416
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**n /; (cons_f8) and (cons_f29) and (cons_f87) and (cons_f167)
                                        # 1: b*x**n /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1500)
                            subjects3.appendleft(tmp6)
                        if len(subjects3) >= 1 and subjects3[0] == 2:
                            tmp8 = subjects3.popleft()
                            # State 125556
                            if len(subjects3) == 0:
                                pass
                                # State 125557
                                if len(subjects) == 0:
                                    pass
                                    # 2: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f14)
                            subjects3.appendleft(tmp8)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp9 = subjects.popleft()
                subjects10 = deque(tmp9._args)
                # State 133808
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 133809
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 133810
                        if len(subjects10) >= 1:
                            tmp13 = subjects10.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.2.1', tmp13)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 133811
                                if len(subjects10) == 0:
                                    pass
                                    # State 133812
                                    if len(subjects) == 0:
                                        pass
                                        # 4: b*log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1879)
                            subjects10.appendleft(tmp13)
                    if len(subjects10) >= 1 and isinstance(subjects10[0], Pow):
                        tmp15 = subjects10.popleft()
                        subjects16 = deque(tmp15._args)
                        # State 133813
                        if len(subjects16) >= 1:
                            tmp17 = subjects16.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1', tmp17)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 133814
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 133815
                                    if len(subjects16) == 0:
                                        pass
                                        # State 133816
                                        if len(subjects10) == 0:
                                            pass
                                            # State 133817
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
                                        # State 133815
                                        if len(subjects16) == 0:
                                            pass
                                            # State 133816
                                            if len(subjects10) == 0:
                                                pass
                                                # State 133817
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
                    matcher = CommutativeMatcher133819.get()
                    tmp24 = subjects23
                    subjects23 = []
                    for s in tmp24:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp24, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 133826
                            if len(subjects10) == 0:
                                pass
                                # State 133827
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
            # State 125561
            if len(subjects) >= 1:
                tmp26 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.1', tmp26)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125562
                    if len(subjects) == 0:
                        pass
                        # 3: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f14)
                subjects.appendleft(tmp26)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp28 = subjects.popleft()
            associative1 = tmp28
            associative_type1 = type(tmp28)
            subjects29 = deque(tmp28._args)
            matcher = CommutativeMatcher122418.get()
            tmp30 = subjects29
            subjects29 = []
            for s in tmp30:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp30, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 122423
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**n /; (cons_f8) and (cons_f29) and (cons_f87) and (cons_f167)
                        # 1: b*x**n /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1500)
                if pattern_index == 1:
                    pass
                    # State 125560
                    if len(subjects) == 0:
                        pass
                        # 2: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f14)
                if pattern_index == 2:
                    pass
                    # State 125563
                    if len(subjects) == 0:
                        pass
                        # 3: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f14)
                if pattern_index == 3:
                    pass
                    # State 133848
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
