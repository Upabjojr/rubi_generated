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


class CommutativeMatcher77678(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.2.2.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher77678._instance is None:
            CommutativeMatcher77678._instance = CommutativeMatcher77678()
        return CommutativeMatcher77678._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 77677
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 77679
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 77680
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 77732
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 77733
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                        yield 1, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 77810
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 77811
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                        yield 2, subst2
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 78179
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 78180
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst2
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 80138
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 80139
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                        yield 4, subst2
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 88103
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp17 = subjects.popleft()
                subjects18 = deque(tmp17._args)
                # State 88104
                if len(subjects18) >= 1:
                    tmp19 = subjects18.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp19)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88105
                        if len(subjects18) >= 1:
                            tmp21 = subjects18.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp21)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 88106
                                if len(subjects18) == 0:
                                    pass
                                    # State 88107
                                    if len(subjects) == 0:
                                        pass
                                        # 5: d*x**n
                                        yield 5, subst3
                            subjects18.appendleft(tmp21)
                    subjects18.appendleft(tmp19)
                if len(subjects18) >= 1:
                    tmp23 = subjects18.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp23)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88651
                        if len(subjects18) >= 1:
                            tmp25 = subjects18.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp25)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 88652
                                if len(subjects18) == 0:
                                    pass
                                    # State 88653
                                    if len(subjects) == 0:
                                        pass
                                        # 6: x**n*d
                                        yield 6, subst3
                            subjects18.appendleft(tmp25)
                    subjects18.appendleft(tmp23)
                subjects.appendleft(tmp17)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp27 = subjects.popleft()
            associative1 = tmp27
            associative_type1 = type(tmp27)
            subjects28 = deque(tmp27._args)
            matcher = CommutativeMatcher77682.get()
            tmp29 = subjects28
            subjects28 = []
            for s in tmp29:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp29, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 77683
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 77734
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 77812
                    if len(subjects) == 0:
                        pass
                        # 2: x*d
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 78181
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 80140
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 88112
                    if len(subjects) == 0:
                        pass
                        # 5: d*x**n
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 88657
                    if len(subjects) == 0:
                        pass
                        # 6: x**n*d
                        yield 6, subst1
            subjects.appendleft(tmp27)
        return
        yield


from .generated_part004752 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset