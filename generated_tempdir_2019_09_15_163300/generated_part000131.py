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


class CommutativeMatcher40692(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 1
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher40692._instance is None:
            CommutativeMatcher40692._instance = CommutativeMatcher40692()
        return CommutativeMatcher40692._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 40691
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 40693
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp2 = subjects.popleft()
                associative1 = tmp2
                associative_type1 = type(tmp2)
                subjects3 = deque(tmp2._args)
                matcher = CommutativeMatcher40695.get()
                tmp4 = subjects3
                subjects3 = []
                for s in tmp4:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp4, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 40711
                        if len(subjects) == 0:
                            pass
                            # 0: (e + f*x + g*x**2)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                            yield 0, subst2
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 44918
                    if len(subjects) == 0:
                        pass
                        # 1: v**p /; (cons_f5) and (cons_f554) and (cons_f1202)
                        yield 1, subst2
                subjects.appendleft(tmp5)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp7 = subjects.popleft()
            subjects8 = deque(tmp7._args)
            # State 40712
            if len(subjects8) >= 1 and isinstance(subjects8[0], Add):
                tmp9 = subjects8.popleft()
                associative1 = tmp9
                associative_type1 = type(tmp9)
                subjects10 = deque(tmp9._args)
                matcher = CommutativeMatcher40714.get()
                tmp11 = subjects10
                subjects10 = []
                for s in tmp11:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp11, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 40730
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40731
                            if len(subjects8) == 0:
                                pass
                                # State 40732
                                if len(subjects) == 0:
                                    pass
                                    # 0: (e + f*x + g*x**2)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                    yield 0, subst2
                        if len(subjects8) >= 1:
                            tmp13 = []
                            tmp13.append(subjects8.popleft())
                            while True:
                                if len(tmp13) > 1:
                                    tmp14 = create_operation_expression(associative1, tmp13)
                                elif len(tmp13) == 1:
                                    tmp14 = tmp13[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp14)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 40731
                                    if len(subjects8) == 0:
                                        pass
                                        # State 40732
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (e + f*x + g*x**2)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f127) and (cons_f210) and (cons_f52) and (cons_f4) and (cons_f1201) and (cons_f40)
                                            yield 0, subst2
                                if len(subjects8) == 0:
                                    break
                                tmp13.append(subjects8.popleft())
                            subjects8.extendleft(reversed(tmp13))
                subjects8.appendleft(tmp9)
            if len(subjects8) >= 1:
                tmp16 = subjects8.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.2.1', tmp16)
                except ValueError:
                    pass
                else:
                    pass
                    # State 44919
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 44920
                        if len(subjects8) == 0:
                            pass
                            # State 44921
                            if len(subjects) == 0:
                                pass
                                # 1: v**p /; (cons_f5) and (cons_f554) and (cons_f1202)
                                yield 1, subst2
                    if len(subjects8) >= 1:
                        tmp19 = subjects8.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', tmp19)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 44920
                            if len(subjects8) == 0:
                                pass
                                # State 44921
                                if len(subjects) == 0:
                                    pass
                                    # 1: v**p /; (cons_f5) and (cons_f554) and (cons_f1202)
                                    yield 1, subst2
                        subjects8.appendleft(tmp19)
                subjects8.appendleft(tmp16)
            subjects.appendleft(tmp7)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part000132 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part000134 import *