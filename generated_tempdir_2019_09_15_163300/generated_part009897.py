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


class CommutativeMatcher89887(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i5.1.0', 1, 1, None), Mul),
      (VariableWithCount('i5.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i5.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher89887._instance is None:
            CommutativeMatcher89887._instance = CommutativeMatcher89887()
        return CommutativeMatcher89887._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 89886
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 105691
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i5.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 105692
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i5.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 105693
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i5.1.2.1', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 105694
                            if len(subjects2) == 0:
                                pass
                                # State 105695
                                if len(subjects) == 0:
                                    pass
                                    # 0: log(c*x**n)
                                    yield 0, subst3
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp7 = subjects2.popleft()
                    subjects8 = deque(tmp7._args)
                    # State 105696
                    if len(subjects8) >= 1:
                        tmp9 = subjects8.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i5.1.2.1', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 105697
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i5.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105698
                                if len(subjects8) == 0:
                                    pass
                                    # State 105699
                                    if len(subjects2) == 0:
                                        pass
                                        # State 105700
                                        if len(subjects) == 0:
                                            pass
                                            # 0: log(c*x**n)
                                            yield 0, subst3
                            if len(subjects8) >= 1:
                                tmp12 = subjects8.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i5.1.2.2', tmp12)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 105698
                                    if len(subjects8) == 0:
                                        pass
                                        # State 105699
                                        if len(subjects2) == 0:
                                            pass
                                            # State 105700
                                            if len(subjects) == 0:
                                                pass
                                                # 0: log(c*x**n)
                                                yield 0, subst3
                                subjects8.appendleft(tmp12)
                        subjects8.appendleft(tmp9)
                    subjects2.appendleft(tmp7)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp14 = subjects2.popleft()
                associative1 = tmp14
                associative_type1 = type(tmp14)
                subjects15 = deque(tmp14._args)
                matcher = CommutativeMatcher105702.get()
                tmp16 = subjects15
                subjects15 = []
                for s in tmp16:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp16, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 105709
                        if len(subjects2) == 0:
                            pass
                            # State 105710
                            if len(subjects) == 0:
                                pass
                                # 0: log(c*x**n)
                                yield 0, subst1
                subjects2.appendleft(tmp14)
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part009898 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset