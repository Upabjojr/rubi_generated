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

class CommutativeMatcher122401(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher122401._instance is None:
            CommutativeMatcher122401._instance = CommutativeMatcher122401()
        return CommutativeMatcher122401._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 122400
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 122402
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 122403
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 122404
                            if len(subjects2) == 0:
                                pass
                                # State 122405
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n /; (cons_f8) and (cons_f29) and (cons_f87) and (cons_f167)
                                    # 1: x**n /; (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1500)
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp7 = subjects.popleft()
            subjects8 = deque(tmp7._args)
            # State 133784
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 133785
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 133786
                    if len(subjects8) >= 1:
                        tmp11 = subjects8.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.2.1', tmp11)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 133787
                            if len(subjects8) == 0:
                                pass
                                # State 133788
                                if len(subjects) == 0:
                                    pass
                                    # 2: log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1879)
                        subjects8.appendleft(tmp11)
                if len(subjects8) >= 1 and isinstance(subjects8[0], Pow):
                    tmp13 = subjects8.popleft()
                    subjects14 = deque(tmp13._args)
                    # State 133789
                    if len(subjects14) >= 1:
                        tmp15 = subjects14.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.2.1', tmp15)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 133790
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 133791
                                if len(subjects14) == 0:
                                    pass
                                    # State 133792
                                    if len(subjects8) == 0:
                                        pass
                                        # State 133793
                                        if len(subjects) == 0:
                                            pass
                                            # 2: log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1879)
                            if len(subjects14) >= 1:
                                tmp18 = subjects14.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i3.1.2.2', tmp18)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 133791
                                    if len(subjects14) == 0:
                                        pass
                                        # State 133792
                                        if len(subjects8) == 0:
                                            pass
                                            # State 133793
                                            if len(subjects) == 0:
                                                pass
                                                # 2: log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1879)
                                subjects14.appendleft(tmp18)
                        subjects14.appendleft(tmp15)
                    subjects8.appendleft(tmp13)
            if len(subjects8) >= 1 and isinstance(subjects8[0], Mul):
                tmp20 = subjects8.popleft()
                associative1 = tmp20
                associative_type1 = type(tmp20)
                subjects21 = deque(tmp20._args)
                matcher = CommutativeMatcher133795.get()
                tmp22 = subjects21
                subjects21 = []
                for s in tmp22:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp22, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 133802
                        if len(subjects8) == 0:
                            pass
                            # State 133803
                            if len(subjects) == 0:
                                pass
                                # 2: log(c*RFx**p) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1879)
                subjects8.appendleft(tmp20)
            subjects.appendleft(tmp7)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
