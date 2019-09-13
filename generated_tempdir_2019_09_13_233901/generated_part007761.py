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

class CommutativeMatcher115962(CommutativeMatcher):
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
        if CommutativeMatcher115962._instance is None:
            CommutativeMatcher115962._instance = CommutativeMatcher115962()
        return CommutativeMatcher115962._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 115961
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 115963
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 115964
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 115965
                            if len(subjects2) == 0:
                                pass
                                # State 115966
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp7 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 116233
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 116234
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.3.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 116235
                            if len(subjects2) >= 1:
                                tmp11 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1', tmp11)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 116236
                                    if len(subjects2) == 0:
                                        pass
                                        # State 116237
                                        if len(subjects) == 0:
                                            pass
                                            # 1: f**(x*d + c)
                                subjects2.appendleft(tmp11)
                        if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                            tmp13 = subjects2.popleft()
                            associative1 = tmp13
                            associative_type1 = type(tmp13)
                            subjects14 = deque(tmp13._args)
                            matcher = CommutativeMatcher116239.get()
                            tmp15 = subjects14
                            subjects14 = []
                            for s in tmp15:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp15, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 116240
                                    if len(subjects2) == 0:
                                        pass
                                        # State 116241
                                        if len(subjects) == 0:
                                            pass
                                            # 1: f**(x*d + c)
                            subjects2.appendleft(tmp13)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                        tmp16 = subjects2.popleft()
                        associative1 = tmp16
                        associative_type1 = type(tmp16)
                        subjects17 = deque(tmp16._args)
                        matcher = CommutativeMatcher116243.get()
                        tmp18 = subjects17
                        subjects17 = []
                        for s in tmp18:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp18, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 116249
                                if len(subjects2) == 0:
                                    pass
                                    # State 116250
                                    if len(subjects) == 0:
                                        pass
                                        # 1: f**(x*d + c)
                        subjects2.appendleft(tmp16)
                subjects2.appendleft(tmp7)
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
