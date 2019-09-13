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

class CommutativeMatcher49270(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.2.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.2.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.2.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher49270._instance is None:
            CommutativeMatcher49270._instance = CommutativeMatcher49270()
        return CommutativeMatcher49270._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 49269
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 49271
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i3.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 49272
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.2.1.2', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49273
                            if len(subjects2) == 0:
                                pass
                                # State 49274
                                if len(subjects) == 0:
                                    pass
                                    # 0: x**n
                        subjects2.appendleft(tmp5)
                subjects2.appendleft(tmp3)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 51275
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 51276
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.2.1.2.1.0', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 51277
                            if len(subjects2) >= 1:
                                tmp11 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2.1.2', tmp11)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51278
                                    if len(subjects2) == 0:
                                        pass
                                        # State 51279
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d + x*e)**n
                                subjects2.appendleft(tmp11)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 51479
                                if len(subjects2) == 0:
                                    pass
                                    # State 51480
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (d + x*e)**n
                            if len(subjects2) >= 1:
                                tmp14 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2.1.2', tmp14)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51479
                                    if len(subjects2) == 0:
                                        pass
                                        # State 51480
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (d + x*e)**n
                                subjects2.appendleft(tmp14)
                        subjects2.appendleft(tmp9)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp16 = subjects2.popleft()
                    associative1 = tmp16
                    associative_type1 = type(tmp16)
                    subjects17 = deque(tmp16._args)
                    matcher = CommutativeMatcher51281.get()
                    tmp18 = subjects17
                    subjects17 = []
                    for s in tmp18:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp18, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 51282
                            if len(subjects2) >= 1:
                                tmp19 = []
                                tmp19.append(subjects2.popleft())
                                while True:
                                    if len(tmp19) > 1:
                                        tmp20 = create_operation_expression(associative1, tmp19)
                                    elif len(tmp19) == 1:
                                        tmp20 = tmp19[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.2.1.2', tmp20)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 51283
                                        if len(subjects2) == 0:
                                            pass
                                            # State 51284
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (d + x*e)**n
                                    if len(subjects2) == 0:
                                        break
                                    tmp19.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp19))
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 51481
                                if len(subjects2) == 0:
                                    pass
                                    # State 51482
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (d + x*e)**n
                            if len(subjects2) >= 1:
                                tmp23 = []
                                tmp23.append(subjects2.popleft())
                                while True:
                                    if len(tmp23) > 1:
                                        tmp24 = create_operation_expression(associative1, tmp23)
                                    elif len(tmp23) == 1:
                                        tmp24 = tmp23[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.2.1.2', tmp24)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 51481
                                        if len(subjects2) == 0:
                                            pass
                                            # State 51482
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (d + x*e)**n
                                    if len(subjects2) == 0:
                                        break
                                    tmp23.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp23))
                    subjects2.appendleft(tmp16)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp26 = subjects2.popleft()
                associative1 = tmp26
                associative_type1 = type(tmp26)
                subjects27 = deque(tmp26._args)
                matcher = CommutativeMatcher51286.get()
                tmp28 = subjects27
                subjects27 = []
                for s in tmp28:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp28, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 51292
                        if len(subjects2) >= 1:
                            tmp29 = []
                            tmp29.append(subjects2.popleft())
                            while True:
                                if len(tmp29) > 1:
                                    tmp30 = create_operation_expression(associative1, tmp29)
                                elif len(tmp29) == 1:
                                    tmp30 = tmp29[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2.1.2', tmp30)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51293
                                    if len(subjects2) == 0:
                                        pass
                                        # State 51294
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d + x*e)**n
                                if len(subjects2) == 0:
                                    break
                                tmp29.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp29))
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 51483
                            if len(subjects2) == 0:
                                pass
                                # State 51484
                                if len(subjects) == 0:
                                    pass
                                    # 2: (d + x*e)**n
                        if len(subjects2) >= 1:
                            tmp33 = []
                            tmp33.append(subjects2.popleft())
                            while True:
                                if len(tmp33) > 1:
                                    tmp34 = create_operation_expression(associative1, tmp33)
                                elif len(tmp33) == 1:
                                    tmp34 = tmp33[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i3.2.1.2', tmp34)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51483
                                    if len(subjects2) == 0:
                                        pass
                                        # State 51484
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (d + x*e)**n
                                if len(subjects2) == 0:
                                    break
                                tmp33.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp33))
                subjects2.appendleft(tmp26)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 51464
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 51465
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i3.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 51466
                    if len(subjects) >= 1:
                        tmp39 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i3.2.1.2.1.0', tmp39)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 51467
                            if len(subjects) == 0:
                                pass
                                # 2: (d + x*e)**n
                        subjects.appendleft(tmp39)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp41 = subjects.popleft()
                    associative1 = tmp41
                    associative_type1 = type(tmp41)
                    subjects42 = deque(tmp41._args)
                    matcher = CommutativeMatcher51469.get()
                    tmp43 = subjects42
                    subjects42 = []
                    for s in tmp43:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp43, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 51470
                            if len(subjects) == 0:
                                pass
                                # 2: (d + x*e)**n
                    subjects.appendleft(tmp41)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp44 = subjects.popleft()
                associative1 = tmp44
                associative_type1 = type(tmp44)
                subjects45 = deque(tmp44._args)
                matcher = CommutativeMatcher51472.get()
                tmp46 = subjects45
                subjects45 = []
                for s in tmp46:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp46, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 51478
                        if len(subjects) == 0:
                            pass
                            # 2: (d + x*e)**n
                subjects.appendleft(tmp44)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
