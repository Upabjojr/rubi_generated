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


class CommutativeMatcher13338(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({4: 1}), [
      (VariableWithCount('i3.1.2.0', 1, 1, None), Add)
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
        if CommutativeMatcher13338._instance is None:
            CommutativeMatcher13338._instance = CommutativeMatcher13338()
        return CommutativeMatcher13338._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 13337
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 13339
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 13340
                if len(subjects3) >= 1 and isinstance(subjects3[0], Add):
                    tmp4 = subjects3.popleft()
                    associative1 = tmp4
                    associative_type1 = type(tmp4)
                    subjects5 = deque(tmp4._args)
                    matcher = CommutativeMatcher13342.get()
                    tmp6 = subjects5
                    subjects5 = []
                    for s in tmp6:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp6, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 13358
                            if len(subjects3) >= 1 and subjects3[0] == Rational(1, 2):
                                tmp7 = subjects3.popleft()
                                # State 13359
                                if len(subjects3) == 0:
                                    pass
                                    # State 13360
                                    if len(subjects) == 0:
                                        pass
                                        # 0: f*sqrt(a + b*x + c*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                                        yield 0, subst2
                                subjects3.appendleft(tmp7)
                        if pattern_index == 1:
                            pass
                            # State 13617
                            if len(subjects3) >= 1 and subjects3[0] == Rational(1, 2):
                                tmp8 = subjects3.popleft()
                                # State 13618
                                if len(subjects3) == 0:
                                    pass
                                    # State 13619
                                    if len(subjects) == 0:
                                        pass
                                        # 2: f*sqrt(a + c*x**2) /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                                        yield 2, subst2
                                subjects3.appendleft(tmp8)
                    subjects3.appendleft(tmp4)
                if len(subjects3) >= 1:
                    tmp9 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2.1.1', tmp9)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 13721
                        if len(subjects3) >= 1 and subjects3[0] == Rational(1, 2):
                            tmp11 = subjects3.popleft()
                            # State 13722
                            if len(subjects3) == 0:
                                pass
                                # State 13723
                                if len(subjects) == 0:
                                    pass
                                    # 4: f*sqrt(v) /; (cons_f127) and (cons_f820) and (cons_f821) and (cons_f1058)
                                    yield 4, subst2
                            subjects3.appendleft(tmp11)
                    subjects3.appendleft(tmp9)
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 13385
            if len(subjects) >= 1:
                tmp13 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.2.1.1', tmp13)
                except ValueError:
                    pass
                else:
                    pass
                    # State 13386
                    if len(subjects) == 0:
                        pass
                        # 1: e*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                        yield 1, subst2
                        # 3: e*x /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                        yield 3, subst2
                subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp15 = subjects.popleft()
            associative1 = tmp15
            associative_type1 = type(tmp15)
            subjects16 = deque(tmp15._args)
            matcher = CommutativeMatcher13362.get()
            tmp17 = subjects16
            subjects16 = []
            for s in tmp17:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp17, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 13384
                    if len(subjects) == 0:
                        pass
                        # 0: f*sqrt(a + b*x + c*x**2) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 13387
                    if len(subjects) == 0:
                        pass
                        # 1: e*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                        yield 1, subst1
                        # 3: e*x /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                        yield 3, subst1
                if pattern_index == 2:
                    pass
                    # State 13623
                    if len(subjects) == 0:
                        pass
                        # 2: f*sqrt(a + c*x**2) /; (cons_f2) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f211) and (cons_f4) and (cons_f1057)
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 13727
                    if len(subjects) == 0:
                        pass
                        # 4: f*sqrt(v) /; (cons_f127) and (cons_f820) and (cons_f821) and (cons_f1058)
                        yield 4, subst1
            subjects.appendleft(tmp15)
        return
        yield


from .generated_part009047 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part009049 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset