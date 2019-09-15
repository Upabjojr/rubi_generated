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


class CommutativeMatcher67166(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher67166._instance is None:
            CommutativeMatcher67166._instance = CommutativeMatcher67166()
        return CommutativeMatcher67166._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 67165
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 67167
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 67168
                    if len(subjects) == 0:
                        pass
                        # 0: x*e
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 77477
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 77478
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 87345
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp8 = subjects.popleft()
                subjects9 = deque(tmp8._args)
                # State 87346
                if len(subjects9) >= 1:
                    tmp10 = subjects9.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.1.1', tmp10)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 87347
                        if len(subjects9) >= 1:
                            tmp12 = subjects9.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.2', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 87348
                                if len(subjects9) == 0:
                                    pass
                                    # State 87349
                                    if len(subjects) == 0:
                                        pass
                                        # 2: d*x**n
                                        yield 2, subst3
                            subjects9.appendleft(tmp12)
                    subjects9.appendleft(tmp10)
                subjects.appendleft(tmp8)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp14 = subjects.popleft()
            associative1 = tmp14
            associative_type1 = type(tmp14)
            subjects15 = deque(tmp14._args)
            matcher = CommutativeMatcher67170.get()
            tmp16 = subjects15
            subjects15 = []
            for s in tmp16:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp16, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 67171
                    if len(subjects) == 0:
                        pass
                        # 0: x*e
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 77479
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 87354
                    if len(subjects) == 0:
                        pass
                        # 2: d*x**n
                        yield 2, subst1
            subjects.appendleft(tmp14)
        return
        yield


from .generated_part009810 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset