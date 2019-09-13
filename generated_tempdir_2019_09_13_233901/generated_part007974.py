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

class CommutativeMatcher145223(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher145223._instance is None:
            CommutativeMatcher145223._instance = CommutativeMatcher145223()
        return CommutativeMatcher145223._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 145222
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 145224
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 145225
                    if len(subjects) == 0:
                        pass
                        # 0: x**n
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp4 = subjects.popleft()
            subjects5 = deque(tmp4._args)
            # State 145226
            if len(subjects5) >= 1:
                tmp6 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 145227
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 145228
                        if len(subjects5) == 0:
                            pass
                            # State 145229
                            if len(subjects) == 0:
                                pass
                                # 0: x**n
                    if len(subjects5) >= 1:
                        tmp9 = subjects5.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 145228
                            if len(subjects5) == 0:
                                pass
                                # State 145229
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects5.appendleft(tmp9)
                subjects5.appendleft(tmp6)
            if len(subjects5) >= 1:
                tmp11 = subjects5.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 145563
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 145564
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 145565
                            if len(subjects5) >= 1:
                                tmp15 = subjects5.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1', tmp15)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 145566
                                    if len(subjects5) == 0:
                                        pass
                                        # State 145567
                                        if len(subjects) == 0:
                                            pass
                                            # 1: f**(x*d + c)
                                subjects5.appendleft(tmp15)
                        if len(subjects5) >= 1 and isinstance(subjects5[0], Mul):
                            tmp17 = subjects5.popleft()
                            associative1 = tmp17
                            associative_type1 = type(tmp17)
                            subjects18 = deque(tmp17._args)
                            matcher = CommutativeMatcher145569.get()
                            tmp19 = subjects18
                            subjects18 = []
                            for s in tmp19:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp19, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 145570
                                    if len(subjects5) == 0:
                                        pass
                                        # State 145571
                                        if len(subjects) == 0:
                                            pass
                                            # 1: f**(x*d + c)
                            subjects5.appendleft(tmp17)
                    if len(subjects5) >= 1 and isinstance(subjects5[0], Add):
                        tmp20 = subjects5.popleft()
                        associative1 = tmp20
                        associative_type1 = type(tmp20)
                        subjects21 = deque(tmp20._args)
                        matcher = CommutativeMatcher145573.get()
                        tmp22 = subjects21
                        subjects21 = []
                        for s in tmp22:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp22, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 145579
                                if len(subjects5) == 0:
                                    pass
                                    # State 145580
                                    if len(subjects) == 0:
                                        pass
                                        # 1: f**(x*d + c)
                        subjects5.appendleft(tmp20)
                subjects5.appendleft(tmp11)
            subjects.appendleft(tmp4)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
