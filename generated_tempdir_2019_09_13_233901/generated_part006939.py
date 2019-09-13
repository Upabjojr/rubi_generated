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

class CommutativeMatcher57254(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.1.0_1', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i2.2.1.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.3.1.0_1', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({}), [
      (VariableWithCount('i2.2.1.2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({0: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({1: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({2: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({}), [
      (VariableWithCount('i2.2.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.3.1.0_1', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({}), [
      (VariableWithCount('i2.2.1.2.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.3.1.0_1', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({}), [
      (VariableWithCount('i2.2.1.4.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.4.1.0_1', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({}), [
      (VariableWithCount('i2.2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({}), [
      (VariableWithCount('i2.4.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.4.1.0_1', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({}), [
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.3.1.1.0', 1, 1, None), Mul)
]),
    16: (16, Multiset({}), [
      (VariableWithCount('i2.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0_3', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({3: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({4: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.3.1.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({}), [
      (VariableWithCount('i2.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0_2', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher57254._instance is None:
            CommutativeMatcher57254._instance = CommutativeMatcher57254()
        return CommutativeMatcher57254._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 57253
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 74628
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 74629
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 74630
                            if len(subjects2) == 0:
                                pass
                                # State 74631
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects2.appendleft(tmp5)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75478
                        if len(subjects2) == 0:
                            pass
                            # State 75479
                            if len(subjects) == 0:
                                pass
                                # 1: x**n
                    if len(subjects2) >= 1:
                        tmp8 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2', tmp8)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 75478
                            if len(subjects2) == 0:
                                pass
                                # State 75479
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                        subjects2.appendleft(tmp8)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp10 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.0', tmp10)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75805
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp12 = subjects2.popleft()
                        # State 75806
                        if len(subjects2) == 0:
                            pass
                            # State 75807
                            if len(subjects) == 0:
                                pass
                                # 2: v**2
                        subjects2.appendleft(tmp12)
                subjects2.appendleft(tmp10)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp13 = subjects2.popleft()
                associative1 = tmp13
                associative_type1 = type(tmp13)
                subjects14 = deque(tmp13._args)
                matcher = CommutativeMatcher107373.get()
                tmp15 = subjects14
                subjects14 = []
                for s in tmp15:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp15, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 107379
                        if len(subjects2) >= 1:
                            tmp16 = []
                            tmp16.append(subjects2.popleft())
                            while True:
                                if len(tmp16) > 1:
                                    tmp17 = create_operation_expression(associative1, tmp16)
                                elif len(tmp16) == 1:
                                    tmp17 = tmp16[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.1.2', tmp17)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 107380
                                    if len(subjects2) == 0:
                                        pass
                                        # State 107381
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (x*d + c)**n
                                if len(subjects2) == 0:
                                    break
                                tmp16.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp16))
                subjects2.appendleft(tmp13)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 75476
            if len(subjects) >= 1:
                tmp20 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1', tmp20)
                except ValueError:
                    pass
                else:
                    pass
                    # State 75477
                    if len(subjects) == 0:
                        pass
                        # 1: x**n
                subjects.appendleft(tmp20)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp22 = subjects.popleft()
            subjects23 = deque(tmp22._args)
            # State 105011
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 105012
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 105013
                    if len(subjects23) >= 1:
                        tmp26 = subjects23.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1', tmp26)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 105014
                            if len(subjects23) == 0:
                                pass
                                # State 105015
                                if len(subjects) == 0:
                                    pass
                                    # 3: log(x**n*c)
                        subjects23.appendleft(tmp26)
                if len(subjects23) >= 1 and isinstance(subjects23[0], Pow):
                    tmp28 = subjects23.popleft()
                    subjects29 = deque(tmp28._args)
                    # State 105016
                    if len(subjects29) >= 1:
                        tmp30 = subjects29.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1', tmp30)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 105017
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105018
                                if len(subjects29) == 0:
                                    pass
                                    # State 105019
                                    if len(subjects23) == 0:
                                        pass
                                        # State 105020
                                        if len(subjects) == 0:
                                            pass
                                            # 3: log(x**n*c)
                            if len(subjects29) >= 1:
                                tmp33 = subjects29.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.3.1.2.2', tmp33)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 105018
                                    if len(subjects29) == 0:
                                        pass
                                        # State 105019
                                        if len(subjects23) == 0:
                                            pass
                                            # State 105020
                                            if len(subjects) == 0:
                                                pass
                                                # 3: log(x**n*c)
                                subjects29.appendleft(tmp33)
                        subjects29.appendleft(tmp30)
                    subjects23.appendleft(tmp28)
            if len(subjects23) >= 1 and isinstance(subjects23[0], Mul):
                tmp35 = subjects23.popleft()
                associative1 = tmp35
                associative_type1 = type(tmp35)
                subjects36 = deque(tmp35._args)
                matcher = CommutativeMatcher105022.get()
                tmp37 = subjects36
                subjects36 = []
                for s in tmp37:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp37, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 105029
                        if len(subjects23) == 0:
                            pass
                            # State 105030
                            if len(subjects) == 0:
                                pass
                                # 3: log(x**n*c)
                subjects23.appendleft(tmp35)
            subjects.appendleft(tmp22)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
