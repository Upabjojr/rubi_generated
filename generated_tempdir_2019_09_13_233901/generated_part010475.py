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

class CommutativeMatcher122456(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i3.1.1', 1, 1, None), Mul)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 1
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher122456._instance is None:
            CommutativeMatcher122456._instance = CommutativeMatcher122456()
        return CommutativeMatcher122456._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 122455
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 122457
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 122458
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 122459
                            if len(subjects2) == 0:
                                pass
                                # State 122460
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects2.appendleft(tmp5)
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp7 = subjects2.popleft()
                        # State 125570
                        if len(subjects2) == 0:
                            pass
                            # State 125571
                            if len(subjects) == 0:
                                pass
                                # 1: x**2
                        subjects2.appendleft(tmp7)
                subjects2.appendleft(tmp3)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp8 = subjects.popleft()
            subjects9 = deque(tmp8._args)
            # State 133926
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 133927
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 133928
                    if len(subjects9) >= 1:
                        tmp12 = subjects9.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1', tmp12)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 133929
                            if len(subjects9) == 0:
                                pass
                                # State 133930
                                if len(subjects) == 0:
                                    pass
                                    # 2: log(c*RFx**p)
                        subjects9.appendleft(tmp12)
                if len(subjects9) >= 1 and isinstance(subjects9[0], Pow):
                    tmp14 = subjects9.popleft()
                    subjects15 = deque(tmp14._args)
                    # State 133931
                    if len(subjects15) >= 1:
                        tmp16 = subjects15.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.1', tmp16)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 133932
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 133933
                                if len(subjects15) == 0:
                                    pass
                                    # State 133934
                                    if len(subjects9) == 0:
                                        pass
                                        # State 133935
                                        if len(subjects) == 0:
                                            pass
                                            # 2: log(c*RFx**p)
                            if len(subjects15) >= 1:
                                tmp19 = subjects15.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', tmp19)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 133933
                                    if len(subjects15) == 0:
                                        pass
                                        # State 133934
                                        if len(subjects9) == 0:
                                            pass
                                            # State 133935
                                            if len(subjects) == 0:
                                                pass
                                                # 2: log(c*RFx**p)
                                subjects15.appendleft(tmp19)
                        subjects15.appendleft(tmp16)
                    subjects9.appendleft(tmp14)
            if len(subjects9) >= 1 and isinstance(subjects9[0], Mul):
                tmp21 = subjects9.popleft()
                associative1 = tmp21
                associative_type1 = type(tmp21)
                subjects22 = deque(tmp21._args)
                matcher = CommutativeMatcher133937.get()
                tmp23 = subjects22
                subjects22 = []
                for s in tmp23:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp23, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 133944
                        if len(subjects9) == 0:
                            pass
                            # State 133945
                            if len(subjects) == 0:
                                pass
                                # 2: log(c*RFx**p)
                subjects9.appendleft(tmp21)
            subjects.appendleft(tmp8)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
