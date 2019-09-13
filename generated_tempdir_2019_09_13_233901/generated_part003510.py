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

class CommutativeMatcher58847(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.2.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
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
        if CommutativeMatcher58847._instance is None:
            CommutativeMatcher58847._instance = CommutativeMatcher58847()
        return CommutativeMatcher58847._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 58846
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 58848
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58849
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
            # State 59027
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 59028
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 61498
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 61499
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 74135
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp11 = subjects.popleft()
                subjects12 = deque(tmp11._args)
                # State 74136
                if len(subjects12) >= 1:
                    tmp13 = subjects12.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp13)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74137
                        if len(subjects12) >= 1:
                            tmp15 = subjects12.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp15)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74138
                                if len(subjects12) == 0:
                                    pass
                                    # State 74139
                                    if len(subjects) == 0:
                                        pass
                                        # 3: x**n*d
                            subjects12.appendleft(tmp15)
                    subjects12.appendleft(tmp13)
                if len(subjects12) >= 1:
                    tmp17 = subjects12.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp17)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74739
                        if len(subjects12) >= 1:
                            tmp19 = subjects12.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp19)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74740
                                if len(subjects12) == 0:
                                    pass
                                    # State 74741
                                    if len(subjects) == 0:
                                        pass
                                        # 4: x**n*d
                            subjects12.appendleft(tmp19)
                    subjects12.appendleft(tmp17)
                if len(subjects12) >= 1:
                    tmp21 = subjects12.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp21)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75163
                        if len(subjects12) >= 1:
                            tmp23 = subjects12.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp23)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75164
                                if len(subjects12) == 0:
                                    pass
                                    # State 75165
                                    if len(subjects) == 0:
                                        pass
                                        # 5: d*x**n
                            subjects12.appendleft(tmp23)
                    subjects12.appendleft(tmp21)
                subjects.appendleft(tmp11)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp25 = subjects.popleft()
            associative1 = tmp25
            associative_type1 = type(tmp25)
            subjects26 = deque(tmp25._args)
            matcher = CommutativeMatcher58851.get()
            tmp27 = subjects26
            subjects26 = []
            for s in tmp27:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp27, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 58852
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 59029
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                if pattern_index == 2:
                    pass
                    # State 61500
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                if pattern_index == 3:
                    pass
                    # State 74144
                    if len(subjects) == 0:
                        pass
                        # 3: x**n*d
                if pattern_index == 4:
                    pass
                    # State 74745
                    if len(subjects) == 0:
                        pass
                        # 4: x**n*d
                if pattern_index == 5:
                    pass
                    # State 75169
                    if len(subjects) == 0:
                        pass
                        # 5: d*x**n
            subjects.appendleft(tmp25)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
