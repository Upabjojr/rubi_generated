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


class CommutativeMatcher150991(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      
]),
    1: (1, Multiset({0: 1, 2: 1}), [
      
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 0
    anonymous_patterns = {0}

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher150991._instance is None:
            CommutativeMatcher150991._instance = CommutativeMatcher150991()
        return CommutativeMatcher150991._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 150990
        if len(subjects) >= 1 and subjects[0] == Integer(1):
            tmp1 = subjects.popleft()
            # State 150992
            if len(subjects) == 0:
                pass
                # 0: 1
                yield 0, subst0
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 150993
            if len(subjects) >= 1:
                tmp3 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 150994
                    if len(subjects) == 0:
                        pass
                        # 1: x*e
                        yield 1, subst2
                subjects.appendleft(tmp3)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 151001
            if len(subjects) >= 1:
                tmp6 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151002
                    if len(subjects) == 0:
                        pass
                        # 2: x*g
                        yield 2, subst2
                subjects.appendleft(tmp6)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp8 = subjects.popleft()
            associative1 = tmp8
            associative_type1 = type(tmp8)
            subjects9 = deque(tmp8._args)
            matcher = CommutativeMatcher150996.get()
            tmp10 = subjects9
            subjects9 = []
            for s in tmp10:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp10, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 150997
                    if len(subjects) == 0:
                        pass
                        # 1: x*e
                        yield 1, subst1
                if pattern_index == 1:
                    pass
                    # State 151003
                    if len(subjects) == 0:
                        pass
                        # 2: x*g
                        yield 2, subst1
            subjects.appendleft(tmp8)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part006210 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset