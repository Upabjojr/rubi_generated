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


class CommutativeMatcher106976(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1, 2: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher106976._instance is None:
            CommutativeMatcher106976._instance = CommutativeMatcher106976()
        return CommutativeMatcher106976._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 106975
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 106977
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 106978
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 106979
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 106980
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp7 = subjects2.popleft()
                                # State 106981
                                if len(subjects2) == 0:
                                    pass
                                    # State 106982
                                    if len(subjects) == 0:
                                        pass
                                        # 0: 1/(c + x*d) /; (cons_f2) and (cons_f8) and (cons_f29)
                                        yield 0, subst3
                                        # 1: 1/(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f73)
                                        yield 1, subst3
                                subjects2.appendleft(tmp7)
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp8 = subjects2.popleft()
                    associative1 = tmp8
                    associative_type1 = type(tmp8)
                    subjects9 = deque(tmp8._args)
                    matcher = CommutativeMatcher106984.get()
                    tmp10 = subjects9
                    subjects9 = []
                    for s in tmp10:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp10, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 106985
                            if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                tmp11 = subjects2.popleft()
                                # State 106986
                                if len(subjects2) == 0:
                                    pass
                                    # State 106987
                                    if len(subjects) == 0:
                                        pass
                                        # 0: 1/(c + x*d) /; (cons_f2) and (cons_f8) and (cons_f29)
                                        yield 0, subst2
                                        # 1: 1/(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f73)
                                        yield 1, subst2
                                subjects2.appendleft(tmp11)
                    subjects2.appendleft(tmp8)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp12 = subjects2.popleft()
                associative1 = tmp12
                associative_type1 = type(tmp12)
                subjects13 = deque(tmp12._args)
                matcher = CommutativeMatcher106989.get()
                tmp14 = subjects13
                subjects13 = []
                for s in tmp14:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp14, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 106995
                        if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                            tmp15 = subjects2.popleft()
                            # State 106996
                            if len(subjects2) == 0:
                                pass
                                # State 106997
                                if len(subjects) == 0:
                                    pass
                                    # 0: 1/(c + x*d) /; (cons_f2) and (cons_f8) and (cons_f29)
                                    yield 0, subst1
                                    # 1: 1/(c + x*d) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f73)
                                    yield 1, subst1
                            subjects2.appendleft(tmp15)
                subjects2.appendleft(tmp12)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 107106
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i4.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 107107
                if len(subjects) >= 1:
                    tmp18 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i4.2.1.0', tmp18)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 107108
                        if len(subjects) == 0:
                            pass
                            # 2: a + b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f73)
                            yield 2, subst3
                    subjects.appendleft(tmp18)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp20 = subjects.popleft()
                associative1 = tmp20
                associative_type1 = type(tmp20)
                subjects21 = deque(tmp20._args)
                matcher = CommutativeMatcher107110.get()
                tmp22 = subjects21
                subjects21 = []
                for s in tmp22:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp22, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 107111
                        if len(subjects) == 0:
                            pass
                            # 2: a + b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f73)
                            yield 2, subst2
                subjects.appendleft(tmp20)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp23 = subjects.popleft()
            associative1 = tmp23
            associative_type1 = type(tmp23)
            subjects24 = deque(tmp23._args)
            matcher = CommutativeMatcher107113.get()
            tmp25 = subjects24
            subjects24 = []
            for s in tmp25:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp25, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 107119
                    if len(subjects) == 0:
                        pass
                        # 2: a + b*x /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f73)
                        yield 2, subst1
            subjects.appendleft(tmp23)
        return
        yield


from .generated_part001622 import *
from .generated_part001621 import *
from .generated_part001619 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part001618 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset