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

class CommutativeMatcher50675(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.2.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.2.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher50675._instance is None:
            CommutativeMatcher50675._instance = CommutativeMatcher50675()
        return CommutativeMatcher50675._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 50674
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 50676
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.2.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 50677
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp5 = subjects2.popleft()
                        # State 50678
                        if len(subjects2) == 0:
                            pass
                            # State 50679
                            if len(subjects) == 0:
                                pass
                                # 0: x**2
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 52743
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 52744
                    if len(subjects2) >= 1:
                        tmp8 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.2.1.2.1.0', tmp8)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 52745
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp10 = subjects2.popleft()
                                # State 52746
                                if len(subjects2) == 0:
                                    pass
                                    # State 52747
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/(f + x*g)
                                subjects2.appendleft(tmp10)
                        subjects2.appendleft(tmp8)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp11 = subjects2.popleft()
                    associative1 = tmp11
                    associative_type1 = type(tmp11)
                    subjects12 = deque(tmp11._args)
                    matcher = CommutativeMatcher52749.get()
                    tmp13 = subjects12
                    subjects12 = []
                    for s in tmp13:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp13, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 52750
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp14 = subjects2.popleft()
                                # State 52751
                                if len(subjects2) == 0:
                                    pass
                                    # State 52752
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/(f + x*g)
                                subjects2.appendleft(tmp14)
                    subjects2.appendleft(tmp11)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp15 = subjects2.popleft()
                associative1 = tmp15
                associative_type1 = type(tmp15)
                subjects16 = deque(tmp15._args)
                matcher = CommutativeMatcher52754.get()
                tmp17 = subjects16
                subjects16 = []
                for s in tmp17:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp17, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 52760
                        if len(subjects2) >= 1 and subjects2[0] == -1:
                            tmp18 = subjects2.popleft()
                            # State 52761
                            if len(subjects2) == 0:
                                pass
                                # State 52762
                                if len(subjects) == 0:
                                    pass
                                    # 1: 1/(f + x*g)
                            subjects2.appendleft(tmp18)
                subjects2.appendleft(tmp15)
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
