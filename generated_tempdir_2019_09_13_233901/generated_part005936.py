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

class CommutativeMatcher17263(CommutativeMatcher):
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
    7: (7, Multiset({}), [
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
        if CommutativeMatcher17263._instance is None:
            CommutativeMatcher17263._instance = CommutativeMatcher17263()
        return CommutativeMatcher17263._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 17262
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 17264
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 17265
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 17266
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 17267
                            if len(subjects2) >= 1:
                                tmp7 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.2', tmp7)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17268
                                    if len(subjects2) == 0:
                                        pass
                                        # State 17269
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (x*d + c)**n
                                subjects2.appendleft(tmp7)
                            if len(subjects2) >= 1 and subjects2[0] == 2:
                                tmp9 = subjects2.popleft()
                                # State 17448
                                if len(subjects2) == 0:
                                    pass
                                    # State 17449
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (x*d + c)**2
                                subjects2.appendleft(tmp9)
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp10 = subjects2.popleft()
                                # State 17489
                                if len(subjects2) == 0:
                                    pass
                                    # State 17490
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
                    # State 17540
                    if len(subjects2) >= 1:
                        tmp12 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2.1.0', tmp12)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 17541
                            if len(subjects2) >= 1:
                                tmp14 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.2', tmp14)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17542
                                    if len(subjects2) == 0:
                                        pass
                                        # State 17543
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
                    matcher = CommutativeMatcher17271.get()
                    tmp18 = subjects17
                    subjects17 = []
                    for s in tmp18:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp18, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 17272
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
                                        # State 17273
                                        if len(subjects2) == 0:
                                            pass
                                            # State 17274
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (x*d + c)**n
                                    if len(subjects2) == 0:
                                        break
                                    tmp19.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp19))
                            if len(subjects2) >= 1 and subjects2[0] == 2:
                                tmp22 = subjects2.popleft()
                                # State 17450
                                if len(subjects2) == 0:
                                    pass
                                    # State 17451
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (x*d + c)**2
                                subjects2.appendleft(tmp22)
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp23 = subjects2.popleft()
                                # State 17491
                                if len(subjects2) == 0:
                                    pass
                                    # State 17492
                                    if len(subjects) == 0:
                                        pass
                                        # 3: 1/(x*d + c)
                                subjects2.appendleft(tmp23)
                        if pattern_index == 1:
                            pass
                            # State 17544
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
                                        # State 17545
                                        if len(subjects2) == 0:
                                            pass
                                            # State 17546
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
                # State 17362
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 17363
                    if len(subjects2) >= 1:
                        tmp29 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp29)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 17364
                            if len(subjects2) >= 1:
                                tmp31 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.2', tmp31)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17365
                                    if len(subjects2) == 0:
                                        pass
                                        # State 17366
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
                    matcher = CommutativeMatcher17368.get()
                    tmp35 = subjects34
                    subjects34 = []
                    for s in tmp35:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp35, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 17369
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
                                        # State 17370
                                        if len(subjects2) == 0:
                                            pass
                                            # State 17371
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (e + x*f)**n
                                    if len(subjects2) == 0:
                                        break
                                    tmp36.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp36))
                    subjects2.appendleft(tmp33)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp39 = subjects2.popleft()
                associative1 = tmp39
                associative_type1 = type(tmp39)
                subjects40 = deque(tmp39._args)
                matcher = CommutativeMatcher17276.get()
                tmp41 = subjects40
                subjects40 = []
                for s in tmp41:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp41, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 17282
                        if len(subjects2) >= 1:
                            tmp42 = []
                            tmp42.append(subjects2.popleft())
                            while True:
                                if len(tmp42) > 1:
                                    tmp43 = create_operation_expression(associative1, tmp42)
                                elif len(tmp42) == 1:
                                    tmp43 = tmp42[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.1.2', tmp43)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17283
                                    if len(subjects2) == 0:
                                        pass
                                        # State 17284
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (x*d + c)**n
                                if len(subjects2) == 0:
                                    break
                                tmp42.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp42))
                        if len(subjects2) >= 1 and subjects2[0] == 2:
                            tmp45 = subjects2.popleft()
                            # State 17452
                            if len(subjects2) == 0:
                                pass
                                # State 17453
                                if len(subjects) == 0:
                                    pass
                                    # 2: (x*d + c)**2
                            subjects2.appendleft(tmp45)
                        if len(subjects2) >= 1 and subjects2[0] == -1:
                            tmp46 = subjects2.popleft()
                            # State 17493
                            if len(subjects2) == 0:
                                pass
                                # State 17494
                                if len(subjects) == 0:
                                    pass
                                    # 3: 1/(x*d + c)
                            subjects2.appendleft(tmp46)
                    if pattern_index == 1:
                        pass
                        # State 17375
                        if len(subjects2) >= 1:
                            tmp47 = []
                            tmp47.append(subjects2.popleft())
                            while True:
                                if len(tmp47) > 1:
                                    tmp48 = create_operation_expression(associative1, tmp47)
                                elif len(tmp47) == 1:
                                    tmp48 = tmp47[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.1.2', tmp48)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17376
                                    if len(subjects2) == 0:
                                        pass
                                        # State 17377
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (e + x*f)**n
                                if len(subjects2) == 0:
                                    break
                                tmp47.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp47))
                    if pattern_index == 2:
                        pass
                        # State 17550
                        if len(subjects2) >= 1:
                            tmp50 = []
                            tmp50.append(subjects2.popleft())
                            while True:
                                if len(tmp50) > 1:
                                    tmp51 = create_operation_expression(associative1, tmp50)
                                elif len(tmp50) == 1:
                                    tmp51 = tmp50[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.1.2', tmp51)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 17551
                                    if len(subjects2) == 0:
                                        pass
                                        # State 17552
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (c + x*d)**n
                                if len(subjects2) == 0:
                                    break
                                tmp50.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp50))
                subjects2.appendleft(tmp39)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 17626
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 17627
                if len(subjects) >= 1:
                    tmp55 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.0', tmp55)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17628
                        if len(subjects) == 0:
                            pass
                            # 5: x*b + a
                    subjects.appendleft(tmp55)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp57 = subjects.popleft()
                associative1 = tmp57
                associative_type1 = type(tmp57)
                subjects58 = deque(tmp57._args)
                matcher = CommutativeMatcher17630.get()
                tmp59 = subjects58
                subjects58 = []
                for s in tmp59:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp59, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 17631
                        if len(subjects) == 0:
                            pass
                            # 5: x*b + a
                subjects.appendleft(tmp57)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp60 = subjects.popleft()
            associative1 = tmp60
            associative_type1 = type(tmp60)
            subjects61 = deque(tmp60._args)
            matcher = CommutativeMatcher17633.get()
            tmp62 = subjects61
            subjects61 = []
            for s in tmp62:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp62, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 17639
                    if len(subjects) == 0:
                        pass
                        # 5: x*b + a
            subjects.appendleft(tmp60)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
