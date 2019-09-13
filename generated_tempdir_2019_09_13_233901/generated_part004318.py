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

class CommutativeMatcher139719(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher139719._instance is None:
            CommutativeMatcher139719._instance = CommutativeMatcher139719()
        return CommutativeMatcher139719._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 139718
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 140737
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 140738
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 140739
                            if len(subjects2) == 0:
                                pass
                                # State 140740
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**p
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 141470
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 141471
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.2.1.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 141472
                        if len(subjects2) >= 1:
                            tmp10 = subjects2.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.2.1.1', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 141473
                                if len(subjects2) >= 1 and subjects2[0] == -1:
                                    tmp12 = subjects2.popleft()
                                    # State 141474
                                    if len(subjects2) == 0:
                                        pass
                                        # State 141475
                                        if len(subjects) == 0:
                                            pass
                                            # 1: 1/(a + b*x**n)
                                    subjects2.appendleft(tmp12)
                            subjects2.appendleft(tmp10)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                        tmp13 = subjects2.popleft()
                        subjects14 = deque(tmp13._args)
                        # State 141476
                        if len(subjects14) >= 1:
                            tmp15 = subjects14.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.2.1.1', tmp15)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 141477
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 141478
                                    if len(subjects14) == 0:
                                        pass
                                        # State 141479
                                        if len(subjects2) >= 1 and subjects2[0] == -1:
                                            tmp18 = subjects2.popleft()
                                            # State 141480
                                            if len(subjects2) == 0:
                                                pass
                                                # State 141481
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: 1/(a + b*x**n)
                                            subjects2.appendleft(tmp18)
                                if len(subjects14) >= 1:
                                    tmp19 = subjects14.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.2.1.2', tmp19)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 141478
                                        if len(subjects14) == 0:
                                            pass
                                            # State 141479
                                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                                tmp21 = subjects2.popleft()
                                                # State 141480
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 141481
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: 1/(a + b*x**n)
                                                subjects2.appendleft(tmp21)
                                    subjects14.appendleft(tmp19)
                            subjects14.appendleft(tmp15)
                        subjects2.appendleft(tmp13)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp22 = subjects2.popleft()
                    associative1 = tmp22
                    associative_type1 = type(tmp22)
                    subjects23 = deque(tmp22._args)
                    matcher = CommutativeMatcher141483.get()
                    tmp24 = subjects23
                    subjects23 = []
                    for s in tmp24:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp24, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 141490
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp25 = subjects2.popleft()
                                # State 141491
                                if len(subjects2) == 0:
                                    pass
                                    # State 141492
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/(a + b*x**n)
                                subjects2.appendleft(tmp25)
                    subjects2.appendleft(tmp22)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp26 = subjects2.popleft()
                associative1 = tmp26
                associative_type1 = type(tmp26)
                subjects27 = deque(tmp26._args)
                matcher = CommutativeMatcher141494.get()
                tmp28 = subjects27
                subjects27 = []
                for s in tmp28:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp28, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 141511
                        if len(subjects2) >= 1 and subjects2[0] == -1:
                            tmp29 = subjects2.popleft()
                            # State 141512
                            if len(subjects2) == 0:
                                pass
                                # State 141513
                                if len(subjects) == 0:
                                    pass
                                    # 1: 1/(a + b*x**n)
                            subjects2.appendleft(tmp29)
                subjects2.appendleft(tmp26)
            subjects.appendleft(tmp1)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
