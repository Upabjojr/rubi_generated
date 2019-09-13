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

class CommutativeMatcher57950(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i3.1.1', 1, 1, None), Mul)
]),
    4: (4, Multiset({2: 1}), [
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
        if CommutativeMatcher57950._instance is None:
            CommutativeMatcher57950._instance = CommutativeMatcher57950()
        return CommutativeMatcher57950._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 57949
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 72564
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72565
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp5 = subjects2.popleft()
                        # State 72566
                        if len(subjects2) == 0:
                            pass
                            # State 72567
                            if len(subjects) == 0:
                                pass
                                # 0: x**2
                        subjects2.appendleft(tmp5)
                    if len(subjects2) >= 1:
                        tmp6 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp6)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 72605
                            if len(subjects2) == 0:
                                pass
                                # State 72606
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                        subjects2.appendleft(tmp6)
                subjects2.appendleft(tmp3)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp8 = subjects.popleft()
            subjects9 = deque(tmp8._args)
            # State 104701
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 104702
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 104703
                    if len(subjects9) >= 1:
                        tmp12 = subjects9.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1', tmp12)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 104704
                            if len(subjects9) == 0:
                                pass
                                # State 104705
                                if len(subjects) == 0:
                                    pass
                                    # 2: log(c*RFx**p)
                        subjects9.appendleft(tmp12)
                if len(subjects9) >= 1 and isinstance(subjects9[0], Pow):
                    tmp14 = subjects9.popleft()
                    subjects15 = deque(tmp14._args)
                    # State 104706
                    if len(subjects15) >= 1:
                        tmp16 = subjects15.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.1', tmp16)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 104707
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 104708
                                if len(subjects15) == 0:
                                    pass
                                    # State 104709
                                    if len(subjects9) == 0:
                                        pass
                                        # State 104710
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
                                    # State 104708
                                    if len(subjects15) == 0:
                                        pass
                                        # State 104709
                                        if len(subjects9) == 0:
                                            pass
                                            # State 104710
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
                matcher = CommutativeMatcher104712.get()
                tmp23 = subjects22
                subjects22 = []
                for s in tmp23:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp23, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 104719
                        if len(subjects9) == 0:
                            pass
                            # State 104720
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
