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


class CommutativeMatcher42152(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i2.2.1.2.2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.2.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher42152._instance is None:
            CommutativeMatcher42152._instance = CommutativeMatcher42152()
        return CommutativeMatcher42152._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 42151
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 42153
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 42154
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 42155
                        if len(subjects3) >= 1 and subjects3[0] == Integer(2):
                            tmp6 = subjects3.popleft()
                            # State 42156
                            if len(subjects3) == 0:
                                pass
                                # State 42157
                                if len(subjects) == 0:
                                    pass
                                    # 0: g*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201)
                                    yield 0, subst2
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 42165
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.1', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 42166
                    if len(subjects) == 0:
                        pass
                        # 1: f*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201)
                        yield 1, subst2
                subjects.appendleft(tmp8)
            if len(subjects) >= 1:
                tmp10 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0', tmp10)
                except ValueError:
                    pass
                else:
                    pass
                    # State 54362
                    if len(subjects) == 0:
                        pass
                        # 2: x*f /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                        yield 2, subst2
                subjects.appendleft(tmp10)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp12 = subjects.popleft()
            associative1 = tmp12
            associative_type1 = type(tmp12)
            subjects13 = deque(tmp12._args)
            matcher = CommutativeMatcher42159.get()
            tmp14 = subjects13
            subjects13 = []
            for s in tmp14:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp14, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 42164
                    if len(subjects) == 0:
                        pass
                        # 0: g*x**2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201)
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 42167
                    if len(subjects) == 0:
                        pass
                        # 1: f*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201)
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 54363
                    if len(subjects) == 0:
                        pass
                        # 2: x*f /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f1250)
                        yield 2, subst1
            subjects.appendleft(tmp12)
        return
        yield


from .generated_part000545 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset