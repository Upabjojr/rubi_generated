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

class CommutativeMatcher56446(CommutativeMatcher):
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
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher56446._instance is None:
            CommutativeMatcher56446._instance = CommutativeMatcher56446()
        return CommutativeMatcher56446._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 56445
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 123494
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 123495
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 123496
                            if len(subjects2) == 0:
                                pass
                                # State 123497
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
                        # State 125432
                        if len(subjects2) == 0:
                            pass
                            # State 125433
                            if len(subjects) == 0:
                                pass
                                # 2: x**n
                    if len(subjects2) >= 1:
                        tmp8 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.1.2', tmp8)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 125432
                            if len(subjects2) == 0:
                                pass
                                # State 125433
                                if len(subjects) == 0:
                                    pass
                                    # 2: x**n
                        subjects2.appendleft(tmp8)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp10 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.0', tmp10)
                except ValueError:
                    pass
                else:
                    pass
                    # State 124502
                    if len(subjects2) >= 1:
                        tmp12 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp12)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 124503
                            if len(subjects2) == 0:
                                pass
                                # State 124504
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**n
                        subjects2.appendleft(tmp12)
                subjects2.appendleft(tmp10)
            if len(subjects2) >= 1:
                tmp14 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125667
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp16 = subjects2.popleft()
                        # State 125668
                        if len(subjects2) == 0:
                            pass
                            # State 125669
                            if len(subjects) == 0:
                                pass
                                # 3: x**2
                        subjects2.appendleft(tmp16)
                subjects2.appendleft(tmp14)
            if len(subjects2) >= 1:
                tmp17 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.0', tmp17)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125704
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp19 = subjects2.popleft()
                        # State 125705
                        if len(subjects2) == 0:
                            pass
                            # State 125706
                            if len(subjects) == 0:
                                pass
                                # 4: x**2
                        subjects2.appendleft(tmp19)
                subjects2.appendleft(tmp17)
            if len(subjects2) >= 1:
                tmp20 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.1.1', tmp20)
                except ValueError:
                    pass
                else:
                    pass
                    # State 131934
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 131935
                        if len(subjects2) == 0:
                            pass
                            # State 131936
                            if len(subjects) == 0:
                                pass
                                # 5: x**n
                    if len(subjects2) >= 1:
                        tmp23 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.4.1.2', tmp23)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 131935
                            if len(subjects2) == 0:
                                pass
                                # State 131936
                                if len(subjects) == 0:
                                    pass
                                    # 5: x**n
                        subjects2.appendleft(tmp23)
                subjects2.appendleft(tmp20)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 125430
            if len(subjects) >= 1:
                tmp26 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1', tmp26)
                except ValueError:
                    pass
                else:
                    pass
                    # State 125431
                    if len(subjects) == 0:
                        pass
                        # 2: x**n
                subjects.appendleft(tmp26)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 131932
            if len(subjects) >= 1:
                tmp29 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.1', tmp29)
                except ValueError:
                    pass
                else:
                    pass
                    # State 131933
                    if len(subjects) == 0:
                        pass
                        # 5: x**n
                subjects.appendleft(tmp29)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp31 = subjects.popleft()
            subjects32 = deque(tmp31._args)
            # State 134625
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 134626
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 134627
                    if len(subjects32) >= 1:
                        tmp35 = subjects32.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1', tmp35)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 134628
                            if len(subjects32) == 0:
                                pass
                                # State 134629
                                if len(subjects) == 0:
                                    pass
                                    # 6: log(x**n*c)
                        subjects32.appendleft(tmp35)
                if len(subjects32) >= 1 and isinstance(subjects32[0], Pow):
                    tmp37 = subjects32.popleft()
                    subjects38 = deque(tmp37._args)
                    # State 134630
                    if len(subjects38) >= 1:
                        tmp39 = subjects38.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1', tmp39)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 134631
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 134632
                                if len(subjects38) == 0:
                                    pass
                                    # State 134633
                                    if len(subjects32) == 0:
                                        pass
                                        # State 134634
                                        if len(subjects) == 0:
                                            pass
                                            # 6: log(x**n*c)
                            if len(subjects38) >= 1:
                                tmp42 = subjects38.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', tmp42)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 134632
                                    if len(subjects38) == 0:
                                        pass
                                        # State 134633
                                        if len(subjects32) == 0:
                                            pass
                                            # State 134634
                                            if len(subjects) == 0:
                                                pass
                                                # 6: log(x**n*c)
                                subjects38.appendleft(tmp42)
                        subjects38.appendleft(tmp39)
                    subjects32.appendleft(tmp37)
            if len(subjects32) >= 1 and isinstance(subjects32[0], Mul):
                tmp44 = subjects32.popleft()
                associative1 = tmp44
                associative_type1 = type(tmp44)
                subjects45 = deque(tmp44._args)
                matcher = CommutativeMatcher134636.get()
                tmp46 = subjects45
                subjects45 = []
                for s in tmp46:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp46, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 134643
                        if len(subjects32) == 0:
                            pass
                            # State 134644
                            if len(subjects) == 0:
                                pass
                                # 6: log(x**n*c)
                subjects32.appendleft(tmp44)
            subjects.appendleft(tmp31)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
