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


class CommutativeMatcher112438(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 0
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher112438._instance is None:
            CommutativeMatcher112438._instance = CommutativeMatcher112438()
        return CommutativeMatcher112438._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 112437
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 112439
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 112440
                if len(subjects3) >= 1 and isinstance(subjects3[0], Add):
                    tmp4 = subjects3.popleft()
                    associative1 = tmp4
                    associative_type1 = type(tmp4)
                    subjects5 = deque(tmp4._args)
                    matcher = CommutativeMatcher112442.get()
                    tmp6 = subjects5
                    subjects5 = []
                    for s in tmp6:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp6, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 112455
                            if len(subjects3) >= 1 and subjects3[0] == Rational(1, 2):
                                tmp7 = subjects3.popleft()
                                # State 112456
                                if len(subjects3) == 0:
                                    pass
                                    # State 112457
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*sqrt(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1770)
                                        yield 0, subst2
                                subjects3.appendleft(tmp7)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 112479
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp9 = subjects.popleft()
                subjects10 = deque(tmp9._args)
                # State 112480
                if len(subjects10) >= 1:
                    tmp11 = subjects10.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.1.1', tmp11)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 112481
                        if len(subjects10) >= 1 and subjects10[0] == Integer(2):
                            tmp13 = subjects10.popleft()
                            # State 112482
                            if len(subjects10) == 0:
                                pass
                                # State 112483
                                if len(subjects) == 0:
                                    pass
                                    # 1: a*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                                    yield 1, subst2
                            subjects10.appendleft(tmp13)
                    subjects10.appendleft(tmp11)
                subjects.appendleft(tmp9)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp14 = subjects.popleft()
            associative1 = tmp14
            associative_type1 = type(tmp14)
            subjects15 = deque(tmp14._args)
            matcher = CommutativeMatcher112459.get()
            tmp16 = subjects15
            subjects15 = []
            for s in tmp16:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp16, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 112478
                    if len(subjects) == 0:
                        pass
                        # 0: b*sqrt(c + d*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1770)
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 112487
                    if len(subjects) == 0:
                        pass
                        # 1: a*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29)
                        yield 1, subst1
            subjects.appendleft(tmp14)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part010310 import *
from collections import deque
from .generated_part010308 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset