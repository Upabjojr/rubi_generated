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

class CommutativeMatcher104418(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
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
        if CommutativeMatcher104418._instance is None:
            CommutativeMatcher104418._instance = CommutativeMatcher104418()
        return CommutativeMatcher104418._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 104417
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 104419
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 104420
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 104421
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i4.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 104422
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i4.1.2.1', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 104423
                                if len(subjects3) == 0:
                                    pass
                                    # State 104424
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1711)
                            subjects3.appendleft(tmp6)
                    if len(subjects3) >= 1 and isinstance(subjects3[0], Pow):
                        tmp8 = subjects3.popleft()
                        subjects9 = deque(tmp8._args)
                        # State 104425
                        if len(subjects9) >= 1:
                            tmp10 = subjects9.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i4.1.2.1', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 104426
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i4.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 104427
                                    if len(subjects9) == 0:
                                        pass
                                        # State 104428
                                        if len(subjects3) == 0:
                                            pass
                                            # State 104429
                                            if len(subjects) == 0:
                                                pass
                                                # 0: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1711)
                                if len(subjects9) >= 1:
                                    tmp13 = subjects9.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i4.1.2.2', tmp13)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 104427
                                        if len(subjects9) == 0:
                                            pass
                                            # State 104428
                                            if len(subjects3) == 0:
                                                pass
                                                # State 104429
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1711)
                                    subjects9.appendleft(tmp13)
                            subjects9.appendleft(tmp10)
                        subjects3.appendleft(tmp8)
                if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                    tmp15 = subjects3.popleft()
                    associative1 = tmp15
                    associative_type1 = type(tmp15)
                    subjects16 = deque(tmp15._args)
                    matcher = CommutativeMatcher104431.get()
                    tmp17 = subjects16
                    subjects16 = []
                    for s in tmp17:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp17, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 104438
                            if len(subjects3) == 0:
                                pass
                                # State 104439
                                if len(subjects) == 0:
                                    pass
                                    # 0: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1711)
                    subjects3.appendleft(tmp15)
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp18 = subjects.popleft()
            associative1 = tmp18
            associative_type1 = type(tmp18)
            subjects19 = deque(tmp18._args)
            matcher = CommutativeMatcher104441.get()
            tmp20 = subjects19
            subjects19 = []
            for s in tmp20:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp20, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 104462
                    if len(subjects) == 0:
                        pass
                        # 0: b*log(c*x**n) /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f1711)
            subjects.appendleft(tmp18)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
