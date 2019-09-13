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

class CommutativeMatcher58464(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.4.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.2.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
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
        if CommutativeMatcher58464._instance is None:
            CommutativeMatcher58464._instance = CommutativeMatcher58464()
        return CommutativeMatcher58464._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 58463
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 58465
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58466
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 58666
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58667
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 59116
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 59117
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 59474
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 59475
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                subjects.appendleft(tmp11)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 61790
            if len(subjects) >= 1:
                tmp14 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0', tmp14)
                except ValueError:
                    pass
                else:
                    pass
                    # State 61791
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
            # State 74012
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp17 = subjects.popleft()
                subjects18 = deque(tmp17._args)
                # State 74013
                if len(subjects18) >= 1:
                    tmp19 = subjects18.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp19)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74014
                        if len(subjects18) >= 1:
                            tmp21 = subjects18.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp21)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74015
                                if len(subjects18) == 0:
                                    pass
                                    # State 74016
                                    if len(subjects) == 0:
                                        pass
                                        # 5: d*x**n
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
                        # State 74477
                        if len(subjects18) >= 1:
                            tmp25 = subjects18.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp25)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74478
                                if len(subjects18) == 0:
                                    pass
                                    # State 74479
                                    if len(subjects) == 0:
                                        pass
                                        # 6: x**n*d
                            subjects18.appendleft(tmp25)
                    subjects18.appendleft(tmp23)
                if len(subjects18) >= 1:
                    tmp27 = subjects18.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.0', tmp27)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 74985
                        if len(subjects18) >= 1:
                            tmp29 = subjects18.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.1.2', tmp29)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 74986
                                if len(subjects18) == 0:
                                    pass
                                    # State 74987
                                    if len(subjects) == 0:
                                        pass
                                        # 7: x**n*d
                            subjects18.appendleft(tmp29)
                    subjects18.appendleft(tmp27)
                subjects.appendleft(tmp17)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp31 = subjects.popleft()
            associative1 = tmp31
            associative_type1 = type(tmp31)
            subjects32 = deque(tmp31._args)
            matcher = CommutativeMatcher58468.get()
            tmp33 = subjects32
            subjects32 = []
            for s in tmp33:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp33, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 58469
                    if len(subjects) == 0:
                        pass
                        # 0: x*d
                if pattern_index == 1:
                    pass
                    # State 58668
                    if len(subjects) == 0:
                        pass
                        # 1: x*f
                if pattern_index == 2:
                    pass
                    # State 59118
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                if pattern_index == 3:
                    pass
                    # State 59476
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                if pattern_index == 4:
                    pass
                    # State 61792
                    if len(subjects) == 0:
                        pass
                        # 4: x*f
                if pattern_index == 5:
                    pass
                    # State 74021
                    if len(subjects) == 0:
                        pass
                        # 5: d*x**n
                if pattern_index == 6:
                    pass
                    # State 74483
                    if len(subjects) == 0:
                        pass
                        # 6: x**n*d
                if pattern_index == 7:
                    pass
                    # State 74991
                    if len(subjects) == 0:
                        pass
                        # 7: x**n*d
            subjects.appendleft(tmp31)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
