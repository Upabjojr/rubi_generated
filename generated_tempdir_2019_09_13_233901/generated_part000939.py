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

class CommutativeMatcher144166(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.3.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.2.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher144166._instance is None:
            CommutativeMatcher144166._instance = CommutativeMatcher144166()
        return CommutativeMatcher144166._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 144165
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp1 = subjects.popleft()
            associative1 = tmp1
            associative_type1 = type(tmp1)
            subjects2 = deque(tmp1._args)
            matcher = CommutativeMatcher144348.get()
            tmp3 = subjects2
            subjects2 = []
            for s in tmp3:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp3, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 144354
                    if len(subjects) == 0:
                        pass
                        # 0: a + x*b
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 144547
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 144548
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 144549
                    if len(subjects5) >= 1:
                        tmp8 = subjects5.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0', tmp8)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 144550
                            if len(subjects5) >= 1 and subjects5[0] == -1:
                                tmp10 = subjects5.popleft()
                                # State 144551
                                if len(subjects5) == 0:
                                    pass
                                    # State 144552
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/(a + x*b)
                                subjects5.appendleft(tmp10)
                        subjects5.appendleft(tmp8)
                if len(subjects5) >= 1 and isinstance(subjects5[0], Mul):
                    tmp11 = subjects5.popleft()
                    associative1 = tmp11
                    associative_type1 = type(tmp11)
                    subjects12 = deque(tmp11._args)
                    matcher = CommutativeMatcher144554.get()
                    tmp13 = subjects12
                    subjects12 = []
                    for s in tmp13:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp13, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 144555
                            if len(subjects5) >= 1 and subjects5[0] == -1:
                                tmp14 = subjects5.popleft()
                                # State 144556
                                if len(subjects5) == 0:
                                    pass
                                    # State 144557
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/(a + x*b)
                                subjects5.appendleft(tmp14)
                    subjects5.appendleft(tmp11)
            if len(subjects5) >= 1 and isinstance(subjects5[0], Add):
                tmp15 = subjects5.popleft()
                associative1 = tmp15
                associative_type1 = type(tmp15)
                subjects16 = deque(tmp15._args)
                matcher = CommutativeMatcher144559.get()
                tmp17 = subjects16
                subjects16 = []
                for s in tmp17:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp17, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 144565
                        if len(subjects5) >= 1 and subjects5[0] == -1:
                            tmp18 = subjects5.popleft()
                            # State 144566
                            if len(subjects5) == 0:
                                pass
                                # State 144567
                                if len(subjects) == 0:
                                    pass
                                    # 1: 1/(a + x*b)
                            subjects5.appendleft(tmp18)
                subjects5.appendleft(tmp15)
            subjects.appendleft(tmp4)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
