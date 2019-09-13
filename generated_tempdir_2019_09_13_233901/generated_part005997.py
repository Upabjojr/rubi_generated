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

class CommutativeMatcher17312(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({}), [
      (VariableWithCount('i2.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({3: 1, 5: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({6: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({}), [
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.3.1.1', 1, 1, None), Mul)
]),
    9: (9, Multiset({7: 1}), [
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0_1', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({}), [
      (VariableWithCount('i2.2.1.3.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.3.1.0_1', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher17312._instance is None:
            CommutativeMatcher17312._instance = CommutativeMatcher17312()
        return CommutativeMatcher17312._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 17311
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 17313
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 17314
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 17315
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 17316
                            if len(subjects2) >= 1:
                                tmp7 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.2', tmp7)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17317
                                    if len(subjects2) == 0:
                                        pass
                                        # State 17318
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (x*d + c)**n
                                subjects2.appendleft(tmp7)
                            if len(subjects2) >= 1 and subjects2[0] == 2:
                                tmp9 = subjects2.popleft()
                                # State 17462
                                if len(subjects2) == 0:
                                    pass
                                    # State 17463
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (x*d + c)**2
                                subjects2.appendleft(tmp9)
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp10 = subjects2.popleft()
                                # State 17503
                                if len(subjects2) == 0:
                                    pass
                                    # State 17504
                                    if len(subjects) == 0:
                                        pass
                                        # 3: 1/(x*d + c)
                                subjects2.appendleft(tmp10)
                        subjects2.appendleft(tmp5)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 17568
                    if len(subjects2) >= 1:
                        tmp12 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2.1.0', tmp12)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 17569
                            if len(subjects2) >= 1:
                                tmp14 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.2', tmp14)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17570
                                    if len(subjects2) == 0:
                                        pass
                                        # State 17571
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (c + x*d)**n
                                subjects2.appendleft(tmp14)
                        subjects2.appendleft(tmp12)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp16 = subjects2.popleft()
                    associative1 = tmp16
                    associative_type1 = type(tmp16)
                    subjects17 = deque(tmp16._args)
                    matcher = CommutativeMatcher17320.get()
                    tmp18 = subjects17
                    subjects17 = []
                    for s in tmp18:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp18, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 17321
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
                                        subst3.try_add_variable('i2.3.1.2', tmp20)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 17322
                                        if len(subjects2) == 0:
                                            pass
                                            # State 17323
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (x*d + c)**n
                                    if len(subjects2) == 0:
                                        break
                                    tmp19.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp19))
                            if len(subjects2) >= 1 and subjects2[0] == 2:
                                tmp22 = subjects2.popleft()
                                # State 17464
                                if len(subjects2) == 0:
                                    pass
                                    # State 17465
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (x*d + c)**2
                                subjects2.appendleft(tmp22)
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp23 = subjects2.popleft()
                                # State 17505
                                if len(subjects2) == 0:
                                    pass
                                    # State 17506
                                    if len(subjects) == 0:
                                        pass
                                        # 3: 1/(x*d + c)
                                subjects2.appendleft(tmp23)
                        if pattern_index == 1:
                            pass
                            # State 17572
                            if len(subjects2) >= 1:
                                tmp24 = []
                                tmp24.append(subjects2.popleft())
                                while True:
                                    if len(tmp24) > 1:
                                        tmp25 = create_operation_expression(associative1, tmp24)
                                    elif len(tmp24) == 1:
                                        tmp25 = tmp24[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.1.2', tmp25)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 17573
                                        if len(subjects2) == 0:
                                            pass
                                            # State 17574
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (c + x*d)**n
                                    if len(subjects2) == 0:
                                        break
                                    tmp24.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp24))
                    subjects2.appendleft(tmp16)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 17396
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 17397
                    if len(subjects2) >= 1:
                        tmp29 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp29)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 17398
                            if len(subjects2) >= 1:
                                tmp31 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.2', tmp31)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17399
                                    if len(subjects2) == 0:
                                        pass
                                        # State 17400
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (e + x*f)**n
                                subjects2.appendleft(tmp31)
                        subjects2.appendleft(tmp29)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp33 = subjects2.popleft()
                    associative1 = tmp33
                    associative_type1 = type(tmp33)
                    subjects34 = deque(tmp33._args)
                    matcher = CommutativeMatcher17402.get()
                    tmp35 = subjects34
                    subjects34 = []
                    for s in tmp35:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp35, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 17403
                            if len(subjects2) >= 1:
                                tmp36 = []
                                tmp36.append(subjects2.popleft())
                                while True:
                                    if len(tmp36) > 1:
                                        tmp37 = create_operation_expression(associative1, tmp36)
                                    elif len(tmp36) == 1:
                                        tmp37 = tmp36[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.1.2', tmp37)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 17404
                                        if len(subjects2) == 0:
                                            pass
                                            # State 17405
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (e + x*f)**n
                                    if len(subjects2) == 0:
                                        break
                                    tmp36.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp36))
                    subjects2.appendleft(tmp33)
            if len(subjects2) >= 1:
                tmp39 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.3.1.1', tmp39)
                except ValueError:
                    pass
                else:
                    pass
                    # State 17691
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp41 = subjects2.popleft()
                        # State 17692
                        if len(subjects2) == 0:
                            pass
                            # State 17693
                            if len(subjects) == 0:
                                pass
                                # 6: x**2
                        subjects2.appendleft(tmp41)
                subjects2.appendleft(tmp39)
            if len(subjects2) >= 1:
                tmp42 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.0', tmp42)
                except ValueError:
                    pass
                else:
                    pass
                    # State 17710
                    if len(subjects2) >= 1 and subjects2[0] == 2:
                        tmp44 = subjects2.popleft()
                        # State 17711
                        if len(subjects2) == 0:
                            pass
                            # State 17712
                            if len(subjects) == 0:
                                pass
                                # 7: v**2
                        subjects2.appendleft(tmp44)
                subjects2.appendleft(tmp42)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp45 = subjects2.popleft()
                associative1 = tmp45
                associative_type1 = type(tmp45)
                subjects46 = deque(tmp45._args)
                matcher = CommutativeMatcher17325.get()
                tmp47 = subjects46
                subjects46 = []
                for s in tmp47:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp47, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 17331
                        if len(subjects2) >= 1:
                            tmp48 = []
                            tmp48.append(subjects2.popleft())
                            while True:
                                if len(tmp48) > 1:
                                    tmp49 = create_operation_expression(associative1, tmp48)
                                elif len(tmp48) == 1:
                                    tmp49 = tmp48[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.1.2', tmp49)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17332
                                    if len(subjects2) == 0:
                                        pass
                                        # State 17333
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (x*d + c)**n
                                if len(subjects2) == 0:
                                    break
                                tmp48.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp48))
                        if len(subjects2) >= 1 and subjects2[0] == 2:
                            tmp51 = subjects2.popleft()
                            # State 17466
                            if len(subjects2) == 0:
                                pass
                                # State 17467
                                if len(subjects) == 0:
                                    pass
                                    # 2: (x*d + c)**2
                            subjects2.appendleft(tmp51)
                        if len(subjects2) >= 1 and subjects2[0] == -1:
                            tmp52 = subjects2.popleft()
                            # State 17507
                            if len(subjects2) == 0:
                                pass
                                # State 17508
                                if len(subjects) == 0:
                                    pass
                                    # 3: 1/(x*d + c)
                            subjects2.appendleft(tmp52)
                    if pattern_index == 1:
                        pass
                        # State 17409
                        if len(subjects2) >= 1:
                            tmp53 = []
                            tmp53.append(subjects2.popleft())
                            while True:
                                if len(tmp53) > 1:
                                    tmp54 = create_operation_expression(associative1, tmp53)
                                elif len(tmp53) == 1:
                                    tmp54 = tmp53[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.1.2', tmp54)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17410
                                    if len(subjects2) == 0:
                                        pass
                                        # State 17411
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (e + x*f)**n
                                if len(subjects2) == 0:
                                    break
                                tmp53.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp53))
                    if pattern_index == 2:
                        pass
                        # State 17578
                        if len(subjects2) >= 1:
                            tmp56 = []
                            tmp56.append(subjects2.popleft())
                            while True:
                                if len(tmp56) > 1:
                                    tmp57 = create_operation_expression(associative1, tmp56)
                                elif len(tmp56) == 1:
                                    tmp57 = tmp56[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.1.2', tmp57)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17579
                                    if len(subjects2) == 0:
                                        pass
                                        # State 17580
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (c + x*d)**n
                                if len(subjects2) == 0:
                                    break
                                tmp56.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp56))
                subjects2.appendleft(tmp45)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 17642
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 17643
                if len(subjects) >= 1:
                    tmp61 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.0', tmp61)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17644
                        if len(subjects) == 0:
                            pass
                            # 5: x*b + a
                    subjects.appendleft(tmp61)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp63 = subjects.popleft()
                associative1 = tmp63
                associative_type1 = type(tmp63)
                subjects64 = deque(tmp63._args)
                matcher = CommutativeMatcher17646.get()
                tmp65 = subjects64
                subjects64 = []
                for s in tmp65:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp65, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 17647
                        if len(subjects) == 0:
                            pass
                            # 5: x*b + a
                subjects.appendleft(tmp63)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp66 = subjects.popleft()
            associative1 = tmp66
            associative_type1 = type(tmp66)
            subjects67 = deque(tmp66._args)
            matcher = CommutativeMatcher17649.get()
            tmp68 = subjects67
            subjects67 = []
            for s in tmp68:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp68, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 17655
                    if len(subjects) == 0:
                        pass
                        # 5: x*b + a
            subjects.appendleft(tmp66)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
