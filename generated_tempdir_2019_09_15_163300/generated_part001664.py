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


class CommutativeMatcher128992(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher128992._instance is None:
            CommutativeMatcher128992._instance = CommutativeMatcher128992()
        return CommutativeMatcher128992._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 128991
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 128993
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 128994
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i4.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 128995
                        if len(subjects3) >= 1 and subjects3[0] == Integer(2):
                            tmp6 = subjects3.popleft()
                            # State 128996
                            if len(subjects3) == 0:
                                pass
                                # State 128997
                                if len(subjects) == 0:
                                    pass
                                    # 0: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                                    yield 0, subst2
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 129005
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.1.1', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 129006
                    if len(subjects) == 0:
                        pass
                        # 1: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 1, subst2
                subjects.appendleft(tmp8)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp10 = subjects.popleft()
            associative1 = tmp10
            associative_type1 = type(tmp10)
            subjects11 = deque(tmp10._args)
            matcher = CommutativeMatcher128999.get()
            tmp12 = subjects11
            subjects11 = []
            for s in tmp12:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp12, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 129004
                    if len(subjects) == 0:
                        pass
                        # 0: c*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 129007
                    if len(subjects) == 0:
                        pass
                        # 1: b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1581)
                        yield 1, subst1
            subjects.appendleft(tmp10)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part001665 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset