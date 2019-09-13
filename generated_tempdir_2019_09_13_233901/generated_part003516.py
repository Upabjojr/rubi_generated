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

class CommutativeMatcher58890(CommutativeMatcher):
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
        if CommutativeMatcher58890._instance is None:
            CommutativeMatcher58890._instance = CommutativeMatcher58890()
        return CommutativeMatcher58890._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 58889
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 58891
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58892
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
            # State 59088
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 59089
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
            # State 61727
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 61728
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
            # State 74362
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp11 = subjects.popleft()
                subjects12 = deque(tmp11._args)
                # State 74363
                if len(subjects12) >= 1:
                    tmp13 = subjects12.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp13)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74364
                        if len(subjects12) >= 1:
                            tmp15 = subjects12.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp15)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74365
                                if len(subjects12) == 0:
                                    pass
                                    # State 74366
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
                        # State 74902
                        if len(subjects12) >= 1:
                            tmp19 = subjects12.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp19)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74903
                                if len(subjects12) == 0:
                                    pass
                                    # State 74904
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
                        # State 75289
                        if len(subjects12) >= 1:
                            tmp23 = subjects12.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp23)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75290
                                if len(subjects12) == 0:
                                    pass
                                    # State 75291
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
            matcher = CommutativeMatcher58894.get()
            tmp27 = subjects26
            subjects26 = []
            for s in tmp27:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp27, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 58895
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 59090
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                if pattern_index == 2:
                    pass
                    # State 61729
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                if pattern_index == 3:
                    pass
                    # State 74371
                    if len(subjects) == 0:
                        pass
                        # 3: x**n*d
                if pattern_index == 4:
                    pass
                    # State 74908
                    if len(subjects) == 0:
                        pass
                        # 4: x**n*d
                if pattern_index == 5:
                    pass
                    # State 75295
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
