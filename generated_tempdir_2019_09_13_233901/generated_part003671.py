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

class CommutativeMatcher78025(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher78025._instance is None:
            CommutativeMatcher78025._instance = CommutativeMatcher78025()
        return CommutativeMatcher78025._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 78024
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 78026
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 78027
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 78286
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 78287
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
            # State 78681
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 78682
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
            # State 80088
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 80089
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
            # State 81027
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 81028
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
            # State 86753
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 86754
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                subjects.appendleft(tmp17)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp19 = subjects.popleft()
                subjects20 = deque(tmp19._args)
                # State 88556
                if len(subjects20) >= 1:
                    tmp21 = subjects20.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp21)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88557
                        if len(subjects20) >= 1:
                            tmp23 = subjects20.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp23)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 88558
                                if len(subjects20) == 0:
                                    pass
                                    # State 88559
                                    if len(subjects) == 0:
                                        pass
                                        # 6: x**n*d
                            subjects20.appendleft(tmp23)
                    subjects20.appendleft(tmp21)
                subjects.appendleft(tmp19)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp25 = subjects.popleft()
            associative1 = tmp25
            associative_type1 = type(tmp25)
            subjects26 = deque(tmp25._args)
            matcher = CommutativeMatcher78029.get()
            tmp27 = subjects26
            subjects26 = []
            for s in tmp27:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp27, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 78030
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                if pattern_index == 1:
                    pass
                    # State 78288
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                if pattern_index == 2:
                    pass
                    # State 78683
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                if pattern_index == 3:
                    pass
                    # State 80090
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                if pattern_index == 4:
                    pass
                    # State 81029
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                if pattern_index == 5:
                    pass
                    # State 86755
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                if pattern_index == 6:
                    pass
                    # State 88564
                    if len(subjects) == 0:
                        pass
                        # 6: x**n*d
            subjects.appendleft(tmp25)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
