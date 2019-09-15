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


class CommutativeMatcher68766(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher68766._instance is None:
            CommutativeMatcher68766._instance = CommutativeMatcher68766()
        return CommutativeMatcher68766._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 68765
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 68767
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.3.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 68768
                    if len(subjects) == 0:
                        pass
                        # 0: x*e
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 97827
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 97828
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.3.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 97829
                        if len(subjects6) >= 1:
                            tmp9 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.3.1.2', tmp9)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 97830
                                if len(subjects6) == 0:
                                    pass
                                    # State 97831
                                    if len(subjects) == 0:
                                        pass
                                        # 1: d*x**n
                                        yield 1, subst3
                            subjects6.appendleft(tmp9)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp11 = subjects.popleft()
            associative1 = tmp11
            associative_type1 = type(tmp11)
            subjects12 = deque(tmp11._args)
            matcher = CommutativeMatcher68770.get()
            tmp13 = subjects12
            subjects12 = []
            for s in tmp13:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp13, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 68771
                    if len(subjects) == 0:
                        pass
                        # 0: x*e
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 97836
                    if len(subjects) == 0:
                        pass
                        # 1: d*x**n
                        yield 1, subst1
            subjects.appendleft(tmp11)
        return
        yield


from .generated_part001238 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset