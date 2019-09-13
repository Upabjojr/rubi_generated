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

class CommutativeMatcher93132(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher93132._instance is None:
            CommutativeMatcher93132._instance = CommutativeMatcher93132()
        return CommutativeMatcher93132._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 93131
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 93133
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 93134
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 98473
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp5 = subjects.popleft()
                subjects6 = deque(tmp5._args)
                # State 98474
                if len(subjects6) >= 1:
                    tmp7 = subjects6.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 98475
                        if len(subjects6) >= 1:
                            tmp9 = subjects6.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.2', tmp9)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 98476
                                if len(subjects6) == 0:
                                    pass
                                    # State 98477
                                    if len(subjects) == 0:
                                        pass
                                        # 1: d*x**n
                            subjects6.appendleft(tmp9)
                    subjects6.appendleft(tmp7)
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp11 = subjects.popleft()
            associative1 = tmp11
            associative_type1 = type(tmp11)
            subjects12 = deque(tmp11._args)
            matcher = CommutativeMatcher93136.get()
            tmp13 = subjects12
            subjects12 = []
            for s in tmp13:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp13, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 93137
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 98482
                    if len(subjects) == 0:
                        pass
                        # 1: d*x**n
            subjects.appendleft(tmp11)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
