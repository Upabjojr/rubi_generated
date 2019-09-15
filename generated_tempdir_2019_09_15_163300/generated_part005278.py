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


class CommutativeMatcher67476(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.2.3.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.4.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.4.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher67476._instance is None:
            CommutativeMatcher67476._instance = CommutativeMatcher67476()
        return CommutativeMatcher67476._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 67475
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 67477
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 67478
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 67603
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 67604
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                        yield 1, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 77788
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 77789
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst2
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 78235
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 78236
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst2
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 80445
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.3.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 80446
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                        yield 4, subst2
                subjects.appendleft(tmp14)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 80893
            if len(subjects) >= 1:
                tmp17 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.4.1.0', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 80894
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                        yield 5, subst2
                subjects.appendleft(tmp17)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 85016
            if len(subjects) >= 1:
                tmp20 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.4.1.0', tmp20)
                except ValueError:
                    pass
                else:
                    pass
                    # State 85017
                    if len(subjects) == 0:
                        pass
                        # 6: x*d
                        yield 6, subst2
                subjects.appendleft(tmp20)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 88382
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp23 = subjects.popleft()
                subjects24 = deque(tmp23._args)
                # State 88383
                if len(subjects24) >= 1:
                    tmp25 = subjects24.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.1', tmp25)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88384
                        if len(subjects24) >= 1:
                            tmp27 = subjects24.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.2', tmp27)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 88385
                                if len(subjects24) == 0:
                                    pass
                                    # State 88386
                                    if len(subjects) == 0:
                                        pass
                                        # 7: d*x**n
                                        yield 7, subst3
                            subjects24.appendleft(tmp27)
                    subjects24.appendleft(tmp25)
                if len(subjects24) >= 1:
                    tmp29 = subjects24.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0_1', tmp29)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 88949
                        if len(subjects24) >= 1:
                            tmp31 = subjects24.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.2', tmp31)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 88950
                                if len(subjects24) == 0:
                                    pass
                                    # State 88951
                                    if len(subjects) == 0:
                                        pass
                                        # 8: x**n*d
                                        yield 8, subst3
                            subjects24.appendleft(tmp31)
                    subjects24.appendleft(tmp29)
                subjects.appendleft(tmp23)
            if len(subjects) >= 1:
                tmp33 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp33)
                except ValueError:
                    pass
                else:
                    pass
                    # State 107618
                    if len(subjects) == 0:
                        pass
                        # 9: x*e
                        yield 9, subst2
                subjects.appendleft(tmp33)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp35 = subjects.popleft()
            associative1 = tmp35
            associative_type1 = type(tmp35)
            subjects36 = deque(tmp35._args)
            matcher = CommutativeMatcher67480.get()
            tmp37 = subjects36
            subjects36 = []
            for s in tmp37:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp37, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 67481
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 67605
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 77790
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 78237
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 80447
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 80895
                    if len(subjects) == 0:
                        pass
                        # 5: x*f
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 85018
                    if len(subjects) == 0:
                        pass
                        # 6: x*d
                        yield 6, subst1
                if pattern_index == 7:
                    pass
                    # State 88391
                    if len(subjects) == 0:
                        pass
                        # 7: d*x**n
                        yield 7, subst1
                if pattern_index == 8:
                    pass
                    # State 88955
                    if len(subjects) == 0:
                        pass
                        # 8: x**n*d
                        yield 8, subst1
                if pattern_index == 9:
                    pass
                    # State 107619
                    if len(subjects) == 0:
                        pass
                        # 9: x*e
                        yield 9, subst1
            subjects.appendleft(tmp35)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part005279 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset