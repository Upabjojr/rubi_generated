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

class CommutativeMatcher58865(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher58865._instance is None:
            CommutativeMatcher58865._instance = CommutativeMatcher58865()
        return CommutativeMatcher58865._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 58864
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 58866
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58867
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 59040
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 59041
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 60183
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 60184
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 61511
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 61512
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 61938
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 61939
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 72169
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 72170
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                subjects.appendleft(tmp17)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp19 = subjects.popleft()
                subjects20 = deque(tmp19._args)
                # State 74158
                if len(subjects20) >= 1:
                    tmp21 = subjects20.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp21)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74159
                        if len(subjects20) >= 1:
                            tmp23 = subjects20.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp23)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74160
                                if len(subjects20) == 0:
                                    pass
                                    # State 74161
                                    if len(subjects) == 0:
                                        pass
                                        # 6: x**n*d
                            subjects20.appendleft(tmp23)
                    subjects20.appendleft(tmp21)
                if len(subjects20) >= 1:
                    tmp25 = subjects20.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp25)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74757
                        if len(subjects20) >= 1:
                            tmp27 = subjects20.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp27)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74758
                                if len(subjects20) == 0:
                                    pass
                                    # State 74759
                                    if len(subjects) == 0:
                                        pass
                                        # 7: x**n*d
                            subjects20.appendleft(tmp27)
                    subjects20.appendleft(tmp25)
                if len(subjects20) >= 1:
                    tmp29 = subjects20.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp29)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75181
                        if len(subjects20) >= 1:
                            tmp31 = subjects20.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp31)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75182
                                if len(subjects20) == 0:
                                    pass
                                    # State 75183
                                    if len(subjects) == 0:
                                        pass
                                        # 8: d*x**n
                            subjects20.appendleft(tmp31)
                    subjects20.appendleft(tmp29)
                subjects.appendleft(tmp19)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp33 = subjects.popleft()
            associative1 = tmp33
            associative_type1 = type(tmp33)
            subjects34 = deque(tmp33._args)
            matcher = CommutativeMatcher58869.get()
            tmp35 = subjects34
            subjects34 = []
            for s in tmp35:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp35, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 58870
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 59042
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                if pattern_index == 2:
                    pass
                    # State 60185
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                if pattern_index == 3:
                    pass
                    # State 61513
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                if pattern_index == 4:
                    pass
                    # State 61940
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                if pattern_index == 5:
                    pass
                    # State 72171
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                if pattern_index == 6:
                    pass
                    # State 74166
                    if len(subjects) == 0:
                        pass
                        # 6: x**n*d
                if pattern_index == 7:
                    pass
                    # State 74763
                    if len(subjects) == 0:
                        pass
                        # 7: x**n*d
                if pattern_index == 8:
                    pass
                    # State 75187
                    if len(subjects) == 0:
                        pass
                        # 8: d*x**n
            subjects.appendleft(tmp33)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
