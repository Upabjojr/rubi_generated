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


class CommutativeMatcher113985(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.1.1.2.0_2', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.2.0_1', 1, 1, S(0)), Add)
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
        if CommutativeMatcher113985._instance is None:
            CommutativeMatcher113985._instance = CommutativeMatcher113985()
        return CommutativeMatcher113985._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 113984
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 113986
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 113987
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.0', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113988
                        if len(subjects3) >= 1 and subjects3[0] == Integer(2):
                            tmp6 = subjects3.popleft()
                            # State 113989
                            if len(subjects3) == 0:
                                pass
                                # State 113990
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**2*g
                                    yield 0, subst2
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                if len(subjects3) >= 1:
                    tmp7 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp7)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 114141
                        if len(subjects3) >= 1 and subjects3[0] == Integer(2):
                            tmp9 = subjects3.popleft()
                            # State 114142
                            if len(subjects3) == 0:
                                pass
                                # State 114143
                                if len(subjects) == 0:
                                    pass
                                    # 1: g*x**2
                                    yield 1, subst2
                            subjects3.appendleft(tmp9)
                    subjects3.appendleft(tmp7)
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp10 = subjects.popleft()
            associative1 = tmp10
            associative_type1 = type(tmp10)
            subjects11 = deque(tmp10._args)
            matcher = CommutativeMatcher113992.get()
            tmp12 = subjects11
            subjects11 = []
            for s in tmp12:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp12, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 113997
                    if len(subjects) == 0:
                        pass
                        # 0: x**2*g
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 114147
                    if len(subjects) == 0:
                        pass
                        # 1: g*x**2
                        yield 1, subst1
            subjects.appendleft(tmp10)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part007153 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset