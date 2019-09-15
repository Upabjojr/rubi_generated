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


class CommutativeMatcher2560(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.0_1', 1, 1, None), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({3: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({4: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({5: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({6: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({7: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({8: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({9: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({10: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    13: (13, Multiset({11: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({12: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({13: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({14: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({15: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({16: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({17: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 1
    anonymous_patterns = {1, 2, 3, 4, 5}

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher2560._instance is None:
            CommutativeMatcher2560._instance = CommutativeMatcher2560()
        return CommutativeMatcher2560._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2559
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 14526
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 14527
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 14528
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 14529
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.3.1.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 14530
                                if len(subjects2) >= 1:
                                    tmp8 = subjects2.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.3.1.1.0', tmp8)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 14531
                                        if len(subjects2) == 0:
                                            pass
                                            # State 14532
                                            if len(subjects) == 0:
                                                pass
                                                # 0: F**(g*(e + x*f))
                                                yield 0, subst5
                                    subjects2.appendleft(tmp8)
                            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                                tmp10 = subjects2.popleft()
                                associative1 = tmp10
                                associative_type1 = type(tmp10)
                                subjects11 = deque(tmp10._args)
                                matcher = CommutativeMatcher14534.get()
                                tmp12 = subjects11
                                subjects11 = []
                                for s in tmp12:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp12, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 14535
                                        if len(subjects2) == 0:
                                            pass
                                            # State 14536
                                            if len(subjects) == 0:
                                                pass
                                                # 0: F**(g*(e + x*f))
                                                yield 0, subst4
                                subjects2.appendleft(tmp10)
                        if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                            tmp13 = subjects2.popleft()
                            associative1 = tmp13
                            associative_type1 = type(tmp13)
                            subjects14 = deque(tmp13._args)
                            matcher = CommutativeMatcher14538.get()
                            tmp15 = subjects14
                            subjects14 = []
                            for s in tmp15:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp15, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 14544
                                    if len(subjects2) == 0:
                                        pass
                                        # State 14545
                                        if len(subjects) == 0:
                                            pass
                                            # 0: F**(g*(e + x*f))
                                            yield 0, subst3
                            subjects2.appendleft(tmp13)
                    if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                        tmp16 = subjects2.popleft()
                        associative1 = tmp16
                        associative_type1 = type(tmp16)
                        subjects17 = deque(tmp16._args)
                        matcher = CommutativeMatcher14547.get()
                        tmp18 = subjects17
                        subjects17 = []
                        for s in tmp18:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp18, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 14562
                                if len(subjects2) == 0:
                                    pass
                                    # State 14563
                                    if len(subjects) == 0:
                                        pass
                                        # 0: F**(g*(e + x*f))
                                        yield 0, subst2
                        subjects2.appendleft(tmp16)
                subjects2.appendleft(tmp3)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 76729
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp20 = subjects2.popleft()
                    subjects21 = deque(tmp20._args)
                    # State 76730
                    if len(subjects21) >= 1 and isinstance(subjects21[0], cos):
                        tmp22 = subjects21.popleft()
                        subjects23 = deque(tmp22._args)
                        # State 76731
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2.3.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 76732
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 76733
                                if len(subjects23) >= 1:
                                    tmp26 = subjects23.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.2.3.1.0', tmp26)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 76734
                                        if len(subjects23) == 0:
                                            pass
                                            # State 76735
                                            if len(subjects21) >= 1 and subjects21[0] == Integer(-1):
                                                tmp28 = subjects21.popleft()
                                                # State 76736
                                                if len(subjects21) == 0:
                                                    pass
                                                    # State 76737
                                                    if len(subjects2) >= 1:
                                                        tmp29 = subjects2.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.2', tmp29)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 76738
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 76739
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 15: (d/cos(e + x*f))**p
                                                                    yield 15, subst5
                                                        subjects2.appendleft(tmp29)
                                                subjects21.appendleft(tmp28)
                                    subjects23.appendleft(tmp26)
                            if len(subjects23) >= 1 and isinstance(subjects23[0], Mul):
                                tmp31 = subjects23.popleft()
                                associative1 = tmp31
                                associative_type1 = type(tmp31)
                                subjects32 = deque(tmp31._args)
                                matcher = CommutativeMatcher76741.get()
                                tmp33 = subjects32
                                subjects32 = []
                                for s in tmp33:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp33, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 76742
                                        if len(subjects23) == 0:
                                            pass
                                            # State 76743
                                            if len(subjects21) >= 1 and subjects21[0] == Integer(-1):
                                                tmp34 = subjects21.popleft()
                                                # State 76744
                                                if len(subjects21) == 0:
                                                    pass
                                                    # State 76745
                                                    if len(subjects2) >= 1:
                                                        tmp35 = subjects2.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i2.2.2', tmp35)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 76746
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 76747
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 15: (d/cos(e + x*f))**p
                                                                    yield 15, subst4
                                                        subjects2.appendleft(tmp35)
                                                subjects21.appendleft(tmp34)
                                subjects23.appendleft(tmp31)
                        if len(subjects23) >= 1 and isinstance(subjects23[0], Add):
                            tmp37 = subjects23.popleft()
                            associative1 = tmp37
                            associative_type1 = type(tmp37)
                            subjects38 = deque(tmp37._args)
                            matcher = CommutativeMatcher76749.get()
                            tmp39 = subjects38
                            subjects38 = []
                            for s in tmp39:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp39, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 76755
                                    if len(subjects23) == 0:
                                        pass
                                        # State 76756
                                        if len(subjects21) >= 1 and subjects21[0] == Integer(-1):
                                            tmp40 = subjects21.popleft()
                                            # State 76757
                                            if len(subjects21) == 0:
                                                pass
                                                # State 76758
                                                if len(subjects2) >= 1:
                                                    tmp41 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.2', tmp41)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 76759
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 76760
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 15: (d/cos(e + x*f))**p
                                                                yield 15, subst3
                                                    subjects2.appendleft(tmp41)
                                            subjects21.appendleft(tmp40)
                            subjects23.appendleft(tmp37)
                        subjects21.appendleft(tmp22)
                    if len(subjects21) >= 1 and isinstance(subjects21[0], sin):
                        tmp43 = subjects21.popleft()
                        subjects44 = deque(tmp43._args)
                        # State 77016
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2.3.0', S(0))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 77017
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0_1', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 77018
                                if len(subjects44) >= 1:
                                    tmp47 = subjects44.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.2.3.1.0', tmp47)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 77019
                                        if len(subjects44) == 0:
                                            pass
                                            # State 77020
                                            if len(subjects21) >= 1 and subjects21[0] == Integer(-1):
                                                tmp49 = subjects21.popleft()
                                                # State 77021
                                                if len(subjects21) == 0:
                                                    pass
                                                    # State 77022
                                                    if len(subjects2) >= 1:
                                                        tmp50 = subjects2.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.2', tmp50)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 77023
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 77024
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 16: (d/sin(e + x*f))**p
                                                                    yield 16, subst5
                                                        subjects2.appendleft(tmp50)
                                                subjects21.appendleft(tmp49)
                                    subjects44.appendleft(tmp47)
                            if len(subjects44) >= 1 and isinstance(subjects44[0], Mul):
                                tmp52 = subjects44.popleft()
                                associative1 = tmp52
                                associative_type1 = type(tmp52)
                                subjects53 = deque(tmp52._args)
                                matcher = CommutativeMatcher77026.get()
                                tmp54 = subjects53
                                subjects53 = []
                                for s in tmp54:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp54, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 77027
                                        if len(subjects44) == 0:
                                            pass
                                            # State 77028
                                            if len(subjects21) >= 1 and subjects21[0] == Integer(-1):
                                                tmp55 = subjects21.popleft()
                                                # State 77029
                                                if len(subjects21) == 0:
                                                    pass
                                                    # State 77030
                                                    if len(subjects2) >= 1:
                                                        tmp56 = subjects2.popleft()
                                                        subst4 = Substitution(subst3)
                                                        try:
                                                            subst4.try_add_variable('i2.2.2', tmp56)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 77031
                                                            if len(subjects2) == 0:
                                                                pass
                                                                # State 77032
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 16: (d/sin(e + x*f))**p
                                                                    yield 16, subst4
                                                        subjects2.appendleft(tmp56)
                                                subjects21.appendleft(tmp55)
                                subjects44.appendleft(tmp52)
                        if len(subjects44) >= 1 and isinstance(subjects44[0], Add):
                            tmp58 = subjects44.popleft()
                            associative1 = tmp58
                            associative_type1 = type(tmp58)
                            subjects59 = deque(tmp58._args)
                            matcher = CommutativeMatcher77034.get()
                            tmp60 = subjects59
                            subjects59 = []
                            for s in tmp60:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp60, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 77040
                                    if len(subjects44) == 0:
                                        pass
                                        # State 77041
                                        if len(subjects21) >= 1 and subjects21[0] == Integer(-1):
                                            tmp61 = subjects21.popleft()
                                            # State 77042
                                            if len(subjects21) == 0:
                                                pass
                                                # State 77043
                                                if len(subjects2) >= 1:
                                                    tmp62 = subjects2.popleft()
                                                    subst3 = Substitution(subst2)
                                                    try:
                                                        subst3.try_add_variable('i2.2.2', tmp62)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 77044
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 77045
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 16: (d/sin(e + x*f))**p
                                                                yield 16, subst3
                                                    subjects2.appendleft(tmp62)
                                            subjects21.appendleft(tmp61)
                            subjects44.appendleft(tmp58)
                        subjects21.appendleft(tmp43)
                    subjects2.appendleft(tmp20)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp64 = subjects2.popleft()
                subjects65 = deque(tmp64._args)
                # State 57371
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57372
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 57373
                        if len(subjects65) >= 1:
                            tmp68 = subjects65.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp68)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 57374
                                if len(subjects65) == 0:
                                    pass
                                    # State 57375
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp70 = subjects2.popleft()
                                        # State 57376
                                        if len(subjects2) == 0:
                                            pass
                                            # State 57377
                                            if len(subjects) == 0:
                                                pass
                                                # 8: 1/cos(e + x*f)
                                                yield 8, subst3
                                        subjects2.appendleft(tmp70)
                            subjects65.appendleft(tmp68)
                    if len(subjects65) >= 1 and isinstance(subjects65[0], Mul):
                        tmp71 = subjects65.popleft()
                        associative1 = tmp71
                        associative_type1 = type(tmp71)
                        subjects72 = deque(tmp71._args)
                        matcher = CommutativeMatcher57379.get()
                        tmp73 = subjects72
                        subjects72 = []
                        for s in tmp73:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp73, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 57380
                                if len(subjects65) == 0:
                                    pass
                                    # State 57381
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp74 = subjects2.popleft()
                                        # State 57382
                                        if len(subjects2) == 0:
                                            pass
                                            # State 57383
                                            if len(subjects) == 0:
                                                pass
                                                # 8: 1/cos(e + x*f)
                                                yield 8, subst2
                                        subjects2.appendleft(tmp74)
                        subjects65.appendleft(tmp71)
                if len(subjects65) >= 1 and isinstance(subjects65[0], Add):
                    tmp75 = subjects65.popleft()
                    associative1 = tmp75
                    associative_type1 = type(tmp75)
                    subjects76 = deque(tmp75._args)
                    matcher = CommutativeMatcher57385.get()
                    tmp77 = subjects76
                    subjects76 = []
                    for s in tmp77:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp77, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57391
                            if len(subjects65) == 0:
                                pass
                                # State 57392
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp78 = subjects2.popleft()
                                    # State 57393
                                    if len(subjects2) == 0:
                                        pass
                                        # State 57394
                                        if len(subjects) == 0:
                                            pass
                                            # 8: 1/cos(e + x*f)
                                            yield 8, subst1
                                    subjects2.appendleft(tmp78)
                    subjects65.appendleft(tmp75)
                subjects2.appendleft(tmp64)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp79 = subjects2.popleft()
                subjects80 = deque(tmp79._args)
                # State 57542
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57543
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 57544
                        if len(subjects80) >= 1:
                            tmp83 = subjects80.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp83)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 57545
                                if len(subjects80) == 0:
                                    pass
                                    # State 57546
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp85 = subjects2.popleft()
                                        # State 57547
                                        if len(subjects2) == 0:
                                            pass
                                            # State 57548
                                            if len(subjects) == 0:
                                                pass
                                                # 9: 1/sin(e + x*f)
                                                yield 9, subst3
                                        subjects2.appendleft(tmp85)
                            subjects80.appendleft(tmp83)
                    if len(subjects80) >= 1 and isinstance(subjects80[0], Mul):
                        tmp86 = subjects80.popleft()
                        associative1 = tmp86
                        associative_type1 = type(tmp86)
                        subjects87 = deque(tmp86._args)
                        matcher = CommutativeMatcher57550.get()
                        tmp88 = subjects87
                        subjects87 = []
                        for s in tmp88:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp88, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 57551
                                if len(subjects80) == 0:
                                    pass
                                    # State 57552
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp89 = subjects2.popleft()
                                        # State 57553
                                        if len(subjects2) == 0:
                                            pass
                                            # State 57554
                                            if len(subjects) == 0:
                                                pass
                                                # 9: 1/sin(e + x*f)
                                                yield 9, subst2
                                        subjects2.appendleft(tmp89)
                        subjects80.appendleft(tmp86)
                if len(subjects80) >= 1 and isinstance(subjects80[0], Add):
                    tmp90 = subjects80.popleft()
                    associative1 = tmp90
                    associative_type1 = type(tmp90)
                    subjects91 = deque(tmp90._args)
                    matcher = CommutativeMatcher57556.get()
                    tmp92 = subjects91
                    subjects91 = []
                    for s in tmp92:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp92, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57562
                            if len(subjects80) == 0:
                                pass
                                # State 57563
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp93 = subjects2.popleft()
                                    # State 57564
                                    if len(subjects2) == 0:
                                        pass
                                        # State 57565
                                        if len(subjects) == 0:
                                            pass
                                            # 9: 1/sin(e + x*f)
                                            yield 9, subst1
                                    subjects2.appendleft(tmp93)
                    subjects80.appendleft(tmp90)
                subjects2.appendleft(tmp79)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp94 = subjects2.popleft()
                subjects95 = deque(tmp94._args)
                # State 59250
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59251
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 59252
                        if len(subjects95) >= 1:
                            tmp98 = subjects95.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp98)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 59253
                                if len(subjects95) == 0:
                                    pass
                                    # State 59254
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp100 = subjects2.popleft()
                                        # State 59255
                                        if len(subjects2) == 0:
                                            pass
                                            # State 59256
                                            if len(subjects) == 0:
                                                pass
                                                # 11: 1/tan(e + x*f)
                                                yield 11, subst3
                                        subjects2.appendleft(tmp100)
                            subjects95.appendleft(tmp98)
                    if len(subjects95) >= 1 and isinstance(subjects95[0], Mul):
                        tmp101 = subjects95.popleft()
                        associative1 = tmp101
                        associative_type1 = type(tmp101)
                        subjects102 = deque(tmp101._args)
                        matcher = CommutativeMatcher59258.get()
                        tmp103 = subjects102
                        subjects102 = []
                        for s in tmp103:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp103, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 59259
                                if len(subjects95) == 0:
                                    pass
                                    # State 59260
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp104 = subjects2.popleft()
                                        # State 59261
                                        if len(subjects2) == 0:
                                            pass
                                            # State 59262
                                            if len(subjects) == 0:
                                                pass
                                                # 11: 1/tan(e + x*f)
                                                yield 11, subst2
                                        subjects2.appendleft(tmp104)
                        subjects95.appendleft(tmp101)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76456
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 76457
                        if len(subjects95) >= 1:
                            tmp107 = subjects95.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.4.1.0', tmp107)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 76458
                                if len(subjects95) == 0:
                                    pass
                                    # State 76459
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp109 = subjects2.popleft()
                                        # State 76460
                                        if len(subjects2) == 0:
                                            pass
                                            # State 76461
                                            if len(subjects) == 0:
                                                pass
                                                # 14: 1/tan(e + x*f)
                                                yield 14, subst3
                                        subjects2.appendleft(tmp109)
                            subjects95.appendleft(tmp107)
                    if len(subjects95) >= 1 and isinstance(subjects95[0], Mul):
                        tmp110 = subjects95.popleft()
                        associative1 = tmp110
                        associative_type1 = type(tmp110)
                        subjects111 = deque(tmp110._args)
                        matcher = CommutativeMatcher76463.get()
                        tmp112 = subjects111
                        subjects111 = []
                        for s in tmp112:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp112, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 76464
                                if len(subjects95) == 0:
                                    pass
                                    # State 76465
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp113 = subjects2.popleft()
                                        # State 76466
                                        if len(subjects2) == 0:
                                            pass
                                            # State 76467
                                            if len(subjects) == 0:
                                                pass
                                                # 14: 1/tan(e + x*f)
                                                yield 14, subst2
                                        subjects2.appendleft(tmp113)
                        subjects95.appendleft(tmp110)
                if len(subjects95) >= 1 and isinstance(subjects95[0], Add):
                    tmp114 = subjects95.popleft()
                    associative1 = tmp114
                    associative_type1 = type(tmp114)
                    subjects115 = deque(tmp114._args)
                    matcher = CommutativeMatcher59264.get()
                    tmp116 = subjects115
                    subjects115 = []
                    for s in tmp116:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp116, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 59270
                            if len(subjects95) == 0:
                                pass
                                # State 59271
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp117 = subjects2.popleft()
                                    # State 59272
                                    if len(subjects2) == 0:
                                        pass
                                        # State 59273
                                        if len(subjects) == 0:
                                            pass
                                            # 11: 1/tan(e + x*f)
                                            yield 11, subst1
                                    subjects2.appendleft(tmp117)
                        if pattern_index == 1:
                            pass
                            # State 76471
                            if len(subjects95) == 0:
                                pass
                                # State 76472
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp118 = subjects2.popleft()
                                    # State 76473
                                    if len(subjects2) == 0:
                                        pass
                                        # State 76474
                                        if len(subjects) == 0:
                                            pass
                                            # 14: 1/tan(e + x*f)
                                            yield 14, subst1
                                    subjects2.appendleft(tmp118)
                    subjects95.appendleft(tmp114)
                subjects2.appendleft(tmp94)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp119 = subjects2.popleft()
                associative1 = tmp119
                associative_type1 = type(tmp119)
                subjects120 = deque(tmp119._args)
                matcher = CommutativeMatcher76762.get()
                tmp121 = subjects120
                subjects120 = []
                for s in tmp121:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp121, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 76788
                        if len(subjects2) >= 1:
                            tmp122 = []
                            tmp122.append(subjects2.popleft())
                            while True:
                                if len(tmp122) > 1:
                                    tmp123 = create_operation_expression(associative1, tmp122)
                                elif len(tmp122) == 1:
                                    tmp123 = tmp122[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp123)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 76789
                                    if len(subjects2) == 0:
                                        pass
                                        # State 76790
                                        if len(subjects) == 0:
                                            pass
                                            # 15: (d/cos(e + x*f))**p
                                            yield 15, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp122.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp122))
                    if pattern_index == 1:
                        pass
                        # State 77070
                        if len(subjects2) >= 1:
                            tmp125 = []
                            tmp125.append(subjects2.popleft())
                            while True:
                                if len(tmp125) > 1:
                                    tmp126 = create_operation_expression(associative1, tmp125)
                                elif len(tmp125) == 1:
                                    tmp126 = tmp125[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp126)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 77071
                                    if len(subjects2) == 0:
                                        pass
                                        # State 77072
                                        if len(subjects) == 0:
                                            pass
                                            # 16: (d/sin(e + x*f))**p
                                            yield 16, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp125.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp125))
                    if pattern_index == 2:
                        pass
                        # State 102467
                        if len(subjects2) >= 1:
                            tmp128 = []
                            tmp128.append(subjects2.popleft())
                            while True:
                                if len(tmp128) > 1:
                                    tmp129 = create_operation_expression(associative1, tmp128)
                                elif len(tmp128) == 1:
                                    tmp129 = tmp128[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2', tmp129)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 102468
                                    if len(subjects2) == 0:
                                        pass
                                        # State 102469
                                        if len(subjects) == 0:
                                            pass
                                            # 17: (F*b*(c + x*d))**p
                                            yield 17, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp128.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp128))
                subjects2.appendleft(tmp119)
            subjects.appendleft(tmp1)
        if len(subjects) >= 1 and subjects[0] == LambertW(Add(Symbol('a'), Mul(Symbol('b'), Symbol('x')))):
            tmp131 = subjects.popleft()
            # State 56701
            if len(subjects) == 0:
                pass
                # 1: LambertW(a + b*x)
                yield 1, subst0
            subjects.appendleft(tmp131)
        if len(subjects) >= 1 and subjects[0] == LambertW(Mul(Symbol('a'), Pow(Symbol('x'), Symbol('n')))):
            tmp132 = subjects.popleft()
            # State 56732
            if len(subjects) == 0:
                pass
                # 2: LambertW(a*x**n)
                yield 2, subst0
            subjects.appendleft(tmp132)
        if len(subjects) >= 1 and subjects[0] == LambertW(Mul(Symbol('a'), Symbol('x'))):
            tmp133 = subjects.popleft()
            # State 56748
            if len(subjects) == 0:
                pass
                # 3: LambertW(a*x)
                yield 3, subst0
            subjects.appendleft(tmp133)
        if len(subjects) >= 1 and subjects[0] == LambertW(Mul(Symbol('a'), Pow(Symbol('x'), Symbol('n')))):
            tmp134 = subjects.popleft()
            # State 56761
            if len(subjects) == 0:
                pass
                # 4: LambertW(a*x**n)
                yield 4, subst0
            subjects.appendleft(tmp134)
        if len(subjects) >= 1 and subjects[0] == LambertW(Add(Symbol('a'), Mul(Symbol('b'), Symbol('x')))):
            tmp135 = subjects.popleft()
            # State 56821
            if len(subjects) == 0:
                pass
                # 5: LambertW(a + b*x)
                yield 5, subst0
            subjects.appendleft(tmp135)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp136 = subjects.popleft()
            subjects137 = deque(tmp136._args)
            # State 56960
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 56961
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 56962
                    if len(subjects137) >= 1:
                        tmp140 = subjects137.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp140)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 56963
                            if len(subjects137) == 0:
                                pass
                                # State 56964
                                if len(subjects) == 0:
                                    pass
                                    # 6: cos(e + x*f)
                                    yield 6, subst3
                        subjects137.appendleft(tmp140)
                if len(subjects137) >= 1 and isinstance(subjects137[0], Mul):
                    tmp142 = subjects137.popleft()
                    associative1 = tmp142
                    associative_type1 = type(tmp142)
                    subjects143 = deque(tmp142._args)
                    matcher = CommutativeMatcher56966.get()
                    tmp144 = subjects143
                    subjects143 = []
                    for s in tmp144:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp144, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 56967
                            if len(subjects137) == 0:
                                pass
                                # State 56968
                                if len(subjects) == 0:
                                    pass
                                    # 6: cos(e + x*f)
                                    yield 6, subst2
                    subjects137.appendleft(tmp142)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 76127
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76128
                    if len(subjects137) >= 1:
                        tmp147 = subjects137.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp147)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 76129
                            if len(subjects137) == 0:
                                pass
                                # State 76130
                                if len(subjects) == 0:
                                    pass
                                    # 12: cos(e + x*f)
                                    yield 12, subst3
                        subjects137.appendleft(tmp147)
                if len(subjects137) >= 1 and isinstance(subjects137[0], Mul):
                    tmp149 = subjects137.popleft()
                    associative1 = tmp149
                    associative_type1 = type(tmp149)
                    subjects150 = deque(tmp149._args)
                    matcher = CommutativeMatcher76132.get()
                    tmp151 = subjects150
                    subjects150 = []
                    for s in tmp151:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp151, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 76133
                            if len(subjects137) == 0:
                                pass
                                # State 76134
                                if len(subjects) == 0:
                                    pass
                                    # 12: cos(e + x*f)
                                    yield 12, subst2
                    subjects137.appendleft(tmp149)
            if len(subjects137) >= 1 and isinstance(subjects137[0], Add):
                tmp152 = subjects137.popleft()
                associative1 = tmp152
                associative_type1 = type(tmp152)
                subjects153 = deque(tmp152._args)
                matcher = CommutativeMatcher56970.get()
                tmp154 = subjects153
                subjects153 = []
                for s in tmp154:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp154, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 56976
                        if len(subjects137) == 0:
                            pass
                            # State 56977
                            if len(subjects) == 0:
                                pass
                                # 6: cos(e + x*f)
                                yield 6, subst1
                    if pattern_index == 1:
                        pass
                        # State 76138
                        if len(subjects137) == 0:
                            pass
                            # State 76139
                            if len(subjects) == 0:
                                pass
                                # 12: cos(e + x*f)
                                yield 12, subst1
                subjects137.appendleft(tmp152)
            subjects.appendleft(tmp136)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp155 = subjects.popleft()
            subjects156 = deque(tmp155._args)
            # State 57127
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 57128
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 57129
                    if len(subjects156) >= 1:
                        tmp159 = subjects156.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp159)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 57130
                            if len(subjects156) == 0:
                                pass
                                # State 57131
                                if len(subjects) == 0:
                                    pass
                                    # 7: sin(e + x*f)
                                    yield 7, subst3
                        subjects156.appendleft(tmp159)
                if len(subjects156) >= 1 and isinstance(subjects156[0], Mul):
                    tmp161 = subjects156.popleft()
                    associative1 = tmp161
                    associative_type1 = type(tmp161)
                    subjects162 = deque(tmp161._args)
                    matcher = CommutativeMatcher57133.get()
                    tmp163 = subjects162
                    subjects162 = []
                    for s in tmp163:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp163, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 57134
                            if len(subjects156) == 0:
                                pass
                                # State 57135
                                if len(subjects) == 0:
                                    pass
                                    # 7: sin(e + x*f)
                                    yield 7, subst2
                    subjects156.appendleft(tmp161)
            if len(subjects156) >= 1 and isinstance(subjects156[0], Add):
                tmp164 = subjects156.popleft()
                associative1 = tmp164
                associative_type1 = type(tmp164)
                subjects165 = deque(tmp164._args)
                matcher = CommutativeMatcher57137.get()
                tmp166 = subjects165
                subjects165 = []
                for s in tmp166:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp166, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 57143
                        if len(subjects156) == 0:
                            pass
                            # State 57144
                            if len(subjects) == 0:
                                pass
                                # 7: sin(e + x*f)
                                yield 7, subst1
                subjects156.appendleft(tmp164)
            subjects.appendleft(tmp155)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp167 = subjects.popleft()
            subjects168 = deque(tmp167._args)
            # State 59159
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 59160
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 59161
                    if len(subjects168) >= 1:
                        tmp171 = subjects168.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp171)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 59162
                            if len(subjects168) == 0:
                                pass
                                # State 59163
                                if len(subjects) == 0:
                                    pass
                                    # 10: tan(e + x*f)
                                    yield 10, subst3
                        subjects168.appendleft(tmp171)
                if len(subjects168) >= 1 and isinstance(subjects168[0], Mul):
                    tmp173 = subjects168.popleft()
                    associative1 = tmp173
                    associative_type1 = type(tmp173)
                    subjects174 = deque(tmp173._args)
                    matcher = CommutativeMatcher59165.get()
                    tmp175 = subjects174
                    subjects174 = []
                    for s in tmp175:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp175, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 59166
                            if len(subjects168) == 0:
                                pass
                                # State 59167
                                if len(subjects) == 0:
                                    pass
                                    # 10: tan(e + x*f)
                                    yield 10, subst2
                    subjects168.appendleft(tmp173)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.4.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 76379
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.4.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 76380
                    if len(subjects168) >= 1:
                        tmp178 = subjects168.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.4.1.0', tmp178)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 76381
                            if len(subjects168) == 0:
                                pass
                                # State 76382
                                if len(subjects) == 0:
                                    pass
                                    # 13: tan(e + x*f)
                                    yield 13, subst3
                        subjects168.appendleft(tmp178)
                if len(subjects168) >= 1 and isinstance(subjects168[0], Mul):
                    tmp180 = subjects168.popleft()
                    associative1 = tmp180
                    associative_type1 = type(tmp180)
                    subjects181 = deque(tmp180._args)
                    matcher = CommutativeMatcher76384.get()
                    tmp182 = subjects181
                    subjects181 = []
                    for s in tmp182:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp182, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 76385
                            if len(subjects168) == 0:
                                pass
                                # State 76386
                                if len(subjects) == 0:
                                    pass
                                    # 13: tan(e + x*f)
                                    yield 13, subst2
                    subjects168.appendleft(tmp180)
            if len(subjects168) >= 1 and isinstance(subjects168[0], Add):
                tmp183 = subjects168.popleft()
                associative1 = tmp183
                associative_type1 = type(tmp183)
                subjects184 = deque(tmp183._args)
                matcher = CommutativeMatcher59169.get()
                tmp185 = subjects184
                subjects184 = []
                for s in tmp185:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp185, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 59175
                        if len(subjects168) == 0:
                            pass
                            # State 59176
                            if len(subjects) == 0:
                                pass
                                # 10: tan(e + x*f)
                                yield 10, subst1
                    if pattern_index == 1:
                        pass
                        # State 76390
                        if len(subjects168) == 0:
                            pass
                            # State 76391
                            if len(subjects) == 0:
                                pass
                                # 13: tan(e + x*f)
                                yield 13, subst1
                subjects168.appendleft(tmp183)
            subjects.appendleft(tmp167)
        return
        yield


from .generated_part002915 import *
from .generated_part002922 import *
from .generated_part002946 import *
from .generated_part002932 import *
from .generated_part002919 import *
from .generated_part002947 import *
from .generated_part002920 import *
from .generated_part002928 import *
from collections import deque
from .generated_part002945 import *
from .generated_part002949 import *
from matchpy.utils import VariableWithCount
from .generated_part002954 import *
from .generated_part002929 import *
from .generated_part002931 import *
from .generated_part002912 import *
from .generated_part002933 import *
from .generated_part002950 import *
from .generated_part002926 import *
from .generated_part002913 import *
from .generated_part002935 import *
from multiset import Multiset
from .generated_part002923 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part002953 import *
from .generated_part002952 import *
from .generated_part002925 import *