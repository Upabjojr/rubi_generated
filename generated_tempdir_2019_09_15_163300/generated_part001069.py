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


class CommutativeMatcher51631(CommutativeMatcher):
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
        if CommutativeMatcher51631._instance is None:
            CommutativeMatcher51631._instance = CommutativeMatcher51631()
        return CommutativeMatcher51631._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 51630
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 51632
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 51633
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 51634
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.2.1.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 51635
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp7 = subjects2.popleft()
                                # State 51636
                                if len(subjects2) == 0:
                                    pass
                                    # State 51637
                                    if len(subjects) == 0:
                                        pass
                                        # 0: 1/(f + x*g)
                                        yield 0, subst3
                                subjects2.appendleft(tmp7)
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp8 = subjects2.popleft()
                    associative1 = tmp8
                    associative_type1 = type(tmp8)
                    subjects9 = deque(tmp8._args)
                    matcher = CommutativeMatcher51639.get()
                    tmp10 = subjects9
                    subjects9 = []
                    for s in tmp10:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp10, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 51640
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp11 = subjects2.popleft()
                                # State 51641
                                if len(subjects2) == 0:
                                    pass
                                    # State 51642
                                    if len(subjects) == 0:
                                        pass
                                        # 0: 1/(f + x*g)
                                        yield 0, subst2
                                subjects2.appendleft(tmp11)
                    subjects2.appendleft(tmp8)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp12 = subjects2.popleft()
                associative1 = tmp12
                associative_type1 = type(tmp12)
                subjects13 = deque(tmp12._args)
                matcher = CommutativeMatcher51644.get()
                tmp14 = subjects13
                subjects13 = []
                for s in tmp14:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp14, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 51650
                        if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                            tmp15 = subjects2.popleft()
                            # State 51651
                            if len(subjects2) == 0:
                                pass
                                # State 51652
                                if len(subjects) == 0:
                                    pass
                                    # 0: 1/(f + x*g)
                                    yield 0, subst1
                            subjects2.appendleft(tmp15)
                subjects2.appendleft(tmp12)
            subjects.appendleft(tmp1)
        return
        yield


from .generated_part001070 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part001071 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset