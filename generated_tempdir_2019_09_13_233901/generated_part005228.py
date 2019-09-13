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

class CommutativeMatcher11776(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0_1', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({3: 1, 4: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    7: (7, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    8: (8, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    9: (9, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    10: (10, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Add)
]),
    11: (11, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.2.0_2', 1, 1, None), Add)
]),
    12: (12, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.2.0_3', 1, 1, None), Add)
]),
    13: (13, Multiset({10: 1, 11: 1}), [
      
]),
    14: (14, Multiset({10: 1, 12: 1}), [
      
]),
    15: (15, Multiset({13: 1}), [
      (VariableWithCount('i2.2.1.2.0_1', 1, 1, S(0)), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 1
    anonymous_patterns = {10}

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher11776._instance is None:
            CommutativeMatcher11776._instance = CommutativeMatcher11776()
        return CommutativeMatcher11776._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 11775
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 11777
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 11778
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp4 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.1', tmp4)
                except ValueError:
                    pass
                else:
                    pass
                    # State 12956
                    if len(subjects) == 0:
                        pass
                        # 4: b*x
                subjects.appendleft(tmp4)
            if len(subjects) >= 1:
                tmp6 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', tmp6)
                except ValueError:
                    pass
                else:
                    pass
                    # State 139679
                    if len(subjects) == 0:
                        pass
                        # 9: x*e2
                subjects.appendleft(tmp6)
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151016
                    if len(subjects) == 0:
                        pass
                        # 12: x*g
                subjects.appendleft(tmp8)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 151628
                if len(subjects) >= 1:
                    tmp11 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1', tmp11)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151629
                        if len(subjects) == 0:
                            pass
                            # 13: d*x**n
                    subjects.appendleft(tmp11)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp13 = subjects.popleft()
                subjects14 = deque(tmp13._args)
                # State 151630
                if len(subjects14) >= 1:
                    tmp15 = subjects14.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp15)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 151631
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 151632
                            if len(subjects14) == 0:
                                pass
                                # State 151633
                                if len(subjects) == 0:
                                    pass
                                    # 13: d*x**n
                        if len(subjects14) >= 1:
                            tmp18 = subjects14.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp18)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 151632
                                if len(subjects14) == 0:
                                    pass
                                    # State 151633
                                    if len(subjects) == 0:
                                        pass
                                        # 13: d*x**n
                            subjects14.appendleft(tmp18)
                    subjects14.appendleft(tmp15)
                subjects.appendleft(tmp13)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 12646
            if len(subjects) >= 1:
                tmp21 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp21)
                except ValueError:
                    pass
                else:
                    pass
                    # State 12647
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                subjects.appendleft(tmp21)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 12826
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 12827
                if len(subjects) >= 1:
                    tmp25 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1', tmp25)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12828
                        if len(subjects) == 0:
                            pass
                            # 2: b*x**p
                    subjects.appendleft(tmp25)
            if len(subjects) >= 1:
                tmp27 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', tmp27)
                except ValueError:
                    pass
                else:
                    pass
                    # State 139674
                    if len(subjects) == 0:
                        pass
                        # 8: x*e1
                subjects.appendleft(tmp27)
            if len(subjects) >= 1:
                tmp29 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp29)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151011
                    if len(subjects) == 0:
                        pass
                        # 11: x*e
                subjects.appendleft(tmp29)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp31 = subjects.popleft()
                subjects32 = deque(tmp31._args)
                # State 12829
                if len(subjects32) >= 1:
                    tmp33 = subjects32.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp33)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 12830
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 12831
                            if len(subjects32) == 0:
                                pass
                                # State 12832
                                if len(subjects) == 0:
                                    pass
                                    # 2: b*x**p
                        if len(subjects32) >= 1:
                            tmp36 = subjects32.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp36)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 12831
                                if len(subjects32) == 0:
                                    pass
                                    # State 12832
                                    if len(subjects) == 0:
                                        pass
                                        # 2: b*x**p
                            subjects32.appendleft(tmp36)
                        if len(subjects32) >= 1:
                            tmp38 = subjects32.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp38)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 14346
                                if len(subjects32) == 0:
                                    pass
                                    # State 14347
                                    if len(subjects) == 0:
                                        pass
                                        # 7: b*x**n
                            subjects32.appendleft(tmp38)
                        if len(subjects32) >= 1 and subjects32[0] == 2:
                            tmp40 = subjects32.popleft()
                            # State 12951
                            if len(subjects32) == 0:
                                pass
                                # State 12952
                                if len(subjects) == 0:
                                    pass
                                    # 3: c*x**2
                            subjects32.appendleft(tmp40)
                        if len(subjects32) >= 1 and subjects32[0] == 4:
                            tmp41 = subjects32.popleft()
                            # State 14221
                            if len(subjects32) == 0:
                                pass
                                # State 14222
                                if len(subjects) == 0:
                                    pass
                                    # 6: b*x**4
                            subjects32.appendleft(tmp41)
                    subjects32.appendleft(tmp33)
                if len(subjects32) >= 1:
                    tmp42 = subjects32.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp42)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 14016
                        if len(subjects32) >= 1 and subjects32[0] == 2:
                            tmp44 = subjects32.popleft()
                            # State 14017
                            if len(subjects32) == 0:
                                pass
                                # State 14018
                                if len(subjects) == 0:
                                    pass
                                    # 5: x**2*c
                            subjects32.appendleft(tmp44)
                    subjects32.appendleft(tmp42)
                subjects.appendleft(tmp31)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp45 = subjects.popleft()
            associative1 = tmp45
            associative_type1 = type(tmp45)
            subjects46 = deque(tmp45._args)
            matcher = CommutativeMatcher11780.get()
            tmp47 = subjects46
            subjects46 = []
            for s in tmp47:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp47, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 11781
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                if pattern_index == 1:
                    pass
                    # State 12648
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                if pattern_index == 2:
                    pass
                    # State 12839
                    if len(subjects) == 0:
                        pass
                        # 2: b*x**p
                if pattern_index == 3:
                    pass
                    # State 12955
                    if len(subjects) == 0:
                        pass
                        # 3: c*x**2
                if pattern_index == 4:
                    pass
                    # State 12957
                    if len(subjects) == 0:
                        pass
                        # 4: b*x
                if pattern_index == 5:
                    pass
                    # State 14022
                    if len(subjects) == 0:
                        pass
                        # 5: x**2*c
                if pattern_index == 6:
                    pass
                    # State 14225
                    if len(subjects) == 0:
                        pass
                        # 6: b*x**4
                if pattern_index == 7:
                    pass
                    # State 14350
                    if len(subjects) == 0:
                        pass
                        # 7: b*x**n
                if pattern_index == 8:
                    pass
                    # State 139675
                    if len(subjects) == 0:
                        pass
                        # 8: x*e1
                if pattern_index == 9:
                    pass
                    # State 139680
                    if len(subjects) == 0:
                        pass
                        # 9: x*e2
                if pattern_index == 10:
                    pass
                    # State 151012
                    if len(subjects) == 0:
                        pass
                        # 11: x*e
                if pattern_index == 11:
                    pass
                    # State 151017
                    if len(subjects) == 0:
                        pass
                        # 12: x*g
                if pattern_index == 12:
                    pass
                    # State 151634
                    if len(subjects) == 0:
                        pass
                        # 13: d*x**n
            subjects.appendleft(tmp45)
        if len(subjects) >= 1 and subjects[0] == 1:
            tmp48 = subjects.popleft()
            # State 151010
            if len(subjects) == 0:
                pass
                # 10: 1
            subjects.appendleft(tmp48)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
