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


class CommutativeMatcher50636(CommutativeMatcher):
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
        if CommutativeMatcher50636._instance is None:
            CommutativeMatcher50636._instance = CommutativeMatcher50636()
        return CommutativeMatcher50636._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 50635
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 50637
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.2.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 50638
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp5 = subjects2.popleft()
                        # State 50639
                        if len(subjects2) == 0:
                            pass
                            # State 50640
                            if len(subjects) == 0:
                                pass
                                # 0: x**2
                                yield 0, subst1
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 52650
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 52651
                    if len(subjects2) >= 1:
                        tmp8 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.2.1.2.1.0', tmp8)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 52652
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp10 = subjects2.popleft()
                                # State 52653
                                if len(subjects2) == 0:
                                    pass
                                    # State 52654
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/(f + x*g)
                                        yield 1, subst3
                                subjects2.appendleft(tmp10)
                        subjects2.appendleft(tmp8)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp11 = subjects2.popleft()
                    associative1 = tmp11
                    associative_type1 = type(tmp11)
                    subjects12 = deque(tmp11._args)
                    matcher = CommutativeMatcher52656.get()
                    tmp13 = subjects12
                    subjects12 = []
                    for s in tmp13:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp13, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 52657
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp14 = subjects2.popleft()
                                # State 52658
                                if len(subjects2) == 0:
                                    pass
                                    # State 52659
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/(f + x*g)
                                        yield 1, subst2
                                subjects2.appendleft(tmp14)
                    subjects2.appendleft(tmp11)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp15 = subjects2.popleft()
                associative1 = tmp15
                associative_type1 = type(tmp15)
                subjects16 = deque(tmp15._args)
                matcher = CommutativeMatcher52661.get()
                tmp17 = subjects16
                subjects16 = []
                for s in tmp17:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp17, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 52667
                        if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                            tmp18 = subjects2.popleft()
                            # State 52668
                            if len(subjects2) == 0:
                                pass
                                # State 52669
                                if len(subjects) == 0:
                                    pass
                                    # 1: 1/(f + x*g)
                                    yield 1, subst1
                            subjects2.appendleft(tmp18)
                subjects2.appendleft(tmp15)
            subjects.appendleft(tmp1)
        return
        yield


from .generated_part009289 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part009288 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset