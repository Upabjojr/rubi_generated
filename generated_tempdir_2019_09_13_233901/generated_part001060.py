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

class CommutativeMatcher51574(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
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
        if CommutativeMatcher51574._instance is None:
            CommutativeMatcher51574._instance = CommutativeMatcher51574()
        return CommutativeMatcher51574._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 51573
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 51575
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 51576
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 51577
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.2.1.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 51578
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp7 = subjects2.popleft()
                                # State 51579
                                if len(subjects2) == 0:
                                    pass
                                    # State 51580
                                    if len(subjects) == 0:
                                        pass
                                        # 0: 1/(f + x*g)
                                subjects2.appendleft(tmp7)
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp8 = subjects2.popleft()
                    associative1 = tmp8
                    associative_type1 = type(tmp8)
                    subjects9 = deque(tmp8._args)
                    matcher = CommutativeMatcher51582.get()
                    tmp10 = subjects9
                    subjects9 = []
                    for s in tmp10:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp10, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 51583
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp11 = subjects2.popleft()
                                # State 51584
                                if len(subjects2) == 0:
                                    pass
                                    # State 51585
                                    if len(subjects) == 0:
                                        pass
                                        # 0: 1/(f + x*g)
                                subjects2.appendleft(tmp11)
                    subjects2.appendleft(tmp8)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp12 = subjects2.popleft()
                associative1 = tmp12
                associative_type1 = type(tmp12)
                subjects13 = deque(tmp12._args)
                matcher = CommutativeMatcher51587.get()
                tmp14 = subjects13
                subjects13 = []
                for s in tmp14:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp14, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 51593
                        if len(subjects2) >= 1 and subjects2[0] == -1:
                            tmp15 = subjects2.popleft()
                            # State 51594
                            if len(subjects2) == 0:
                                pass
                                # State 51595
                                if len(subjects) == 0:
                                    pass
                                    # 0: 1/(f + x*g)
                            subjects2.appendleft(tmp15)
                subjects2.appendleft(tmp12)
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
