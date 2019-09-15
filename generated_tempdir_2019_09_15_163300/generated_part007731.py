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


class CommutativeMatcher56424(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.1', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({2: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({}), [
      (VariableWithCount('i2.1.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({5: 1}), [
      (VariableWithCount('i2.4.1.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.1.0_1', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.3.1.1.0', 1, 1, None), Mul)
]),
    16: (16, Multiset({6: 1}), [
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
        if CommutativeMatcher56424._instance is None:
            CommutativeMatcher56424._instance = CommutativeMatcher56424()
        return CommutativeMatcher56424._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 56423
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 123480
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 123481
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 123482
                            if len(subjects2) == 0:
                                pass
                                # State 123483
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                                    yield 0, subst2
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp7 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0', tmp7)
                except ValueError:
                    pass
                else:
                    pass
                    # State 124475
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 124476
                            if len(subjects2) == 0:
                                pass
                                # State 124477
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                                    yield 1, subst2
                        subjects2.appendleft(tmp9)
                subjects2.appendleft(tmp7)
            if len(subjects2) >= 1:
                tmp11 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1.1', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125541
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 125542
                        if len(subjects2) == 0:
                            pass
                            # State 125543
                            if len(subjects) == 0:
                                pass
                                # 2: x**n
                                yield 2, subst2
                    if len(subjects2) >= 1:
                        tmp14 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2', tmp14)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 125542
                            if len(subjects2) == 0:
                                pass
                                # State 125543
                                if len(subjects) == 0:
                                    pass
                                    # 2: x**n
                                    yield 2, subst2
                        subjects2.appendleft(tmp14)
                subjects2.appendleft(tmp11)
            if len(subjects2) >= 1:
                tmp16 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.0', tmp16)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125653
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp18 = subjects2.popleft()
                        # State 125654
                        if len(subjects2) == 0:
                            pass
                            # State 125655
                            if len(subjects) == 0:
                                pass
                                # 3: x**2
                                yield 3, subst1
                        subjects2.appendleft(tmp18)
                subjects2.appendleft(tmp16)
            if len(subjects2) >= 1:
                tmp19 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.0', tmp19)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125688
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp21 = subjects2.popleft()
                        # State 125689
                        if len(subjects2) == 0:
                            pass
                            # State 125690
                            if len(subjects) == 0:
                                pass
                                # 4: x**2
                                yield 4, subst1
                        subjects2.appendleft(tmp21)
                subjects2.appendleft(tmp19)
            if len(subjects2) >= 1:
                tmp22 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.1.1', tmp22)
                except ValueError:
                    pass
                else:
                    pass
                    # State 131888
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131889
                        if len(subjects2) == 0:
                            pass
                            # State 131890
                            if len(subjects) == 0:
                                pass
                                # 5: x**n
                                yield 5, subst2
                    if len(subjects2) >= 1:
                        tmp25 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.4.1.2', tmp25)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 131889
                            if len(subjects2) == 0:
                                pass
                                # State 131890
                                if len(subjects) == 0:
                                    pass
                                    # 5: x**n
                                    yield 5, subst2
                        subjects2.appendleft(tmp25)
                subjects2.appendleft(tmp22)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 125539
            if len(subjects) >= 1:
                tmp28 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1', tmp28)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125540
                    if len(subjects) == 0:
                        pass
                        # 2: x**n
                        yield 2, subst2
                subjects.appendleft(tmp28)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 131886
            if len(subjects) >= 1:
                tmp31 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.1', tmp31)
                except ValueError:
                    pass
                else:
                    pass
                    # State 131887
                    if len(subjects) == 0:
                        pass
                        # 5: x**n
                        yield 5, subst2
                subjects.appendleft(tmp31)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp33 = subjects.popleft()
            subjects34 = deque(tmp33._args)
            # State 134534
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 134535
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 134536
                    if len(subjects34) >= 1:
                        tmp37 = subjects34.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1', tmp37)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 134537
                            if len(subjects34) == 0:
                                pass
                                # State 134538
                                if len(subjects) == 0:
                                    pass
                                    # 6: log(x**n*c)
                                    yield 6, subst3
                        subjects34.appendleft(tmp37)
                if len(subjects34) >= 1 and isinstance(subjects34[0], Pow):
                    tmp39 = subjects34.popleft()
                    subjects40 = deque(tmp39._args)
                    # State 134539
                    if len(subjects40) >= 1:
                        tmp41 = subjects40.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1', tmp41)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 134540
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 134541
                                if len(subjects40) == 0:
                                    pass
                                    # State 134542
                                    if len(subjects34) == 0:
                                        pass
                                        # State 134543
                                        if len(subjects) == 0:
                                            pass
                                            # 6: log(x**n*c)
                                            yield 6, subst3
                            if len(subjects40) >= 1:
                                tmp44 = subjects40.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', tmp44)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 134541
                                    if len(subjects40) == 0:
                                        pass
                                        # State 134542
                                        if len(subjects34) == 0:
                                            pass
                                            # State 134543
                                            if len(subjects) == 0:
                                                pass
                                                # 6: log(x**n*c)
                                                yield 6, subst3
                                subjects40.appendleft(tmp44)
                        subjects40.appendleft(tmp41)
                    subjects34.appendleft(tmp39)
            if len(subjects34) >= 1 and isinstance(subjects34[0], Mul):
                tmp46 = subjects34.popleft()
                associative1 = tmp46
                associative_type1 = type(tmp46)
                subjects47 = deque(tmp46._args)
                matcher = CommutativeMatcher134545.get()
                tmp48 = subjects47
                subjects47 = []
                for s in tmp48:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp48, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 134552
                        if len(subjects34) == 0:
                            pass
                            # State 134553
                            if len(subjects) == 0:
                                pass
                                # 6: log(x**n*c)
                                yield 6, subst1
                subjects34.appendleft(tmp46)
            subjects.appendleft(tmp33)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part007732 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset