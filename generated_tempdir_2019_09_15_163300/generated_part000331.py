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


class CommutativeMatcher12689(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
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
        if CommutativeMatcher12689._instance is None:
            CommutativeMatcher12689._instance = CommutativeMatcher12689()
        return CommutativeMatcher12689._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 12688
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 12690
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 12691
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12692
                        if len(subjects) == 0:
                            pass
                            # 0: b*x**p
                            yield 0, subst3
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 12693
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12694
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 12695
                            if len(subjects6) == 0:
                                pass
                                # State 12696
                                if len(subjects) == 0:
                                    pass
                                    # 0: b*x**p
                                    yield 0, subst3
                        if len(subjects6) >= 1:
                            tmp10 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 12695
                                if len(subjects6) == 0:
                                    pass
                                    # State 12696
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**p
                                        yield 0, subst3
                            subjects6.appendleft(tmp10)
                        if len(subjects6) >= 1:
                            tmp12 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp12)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 14366
                                if len(subjects6) == 0:
                                    pass
                                    # State 14367
                                    if len(subjects) == 0:
                                        pass
                                        # 1: b*x**n
                                        yield 1, subst3
                            subjects6.appendleft(tmp12)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp14 = subjects.popleft()
            associative1 = tmp14
            associative_type1 = type(tmp14)
            subjects15 = deque(tmp14._args)
            matcher = CommutativeMatcher12698.get()
            tmp16 = subjects15
            subjects15 = []
            for s in tmp16:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp16, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 12705
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**p
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 14370
                    if len(subjects) == 0:
                        pass
                        # 1: b*x**n
                        yield 1, subst1
            subjects.appendleft(tmp14)
        return
        yield


from .generated_part000332 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset