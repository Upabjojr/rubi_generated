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

class CommutativeMatcher23919(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({10: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher23919._instance is None:
            CommutativeMatcher23919._instance = CommutativeMatcher23919()
        return CommutativeMatcher23919._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 23918
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 23920
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.1.1.2.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 23921
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.0', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 23922
                        if len(subjects) == 0:
                            pass
                            # 0: e + f*x
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp5 = subjects.popleft()
                associative1 = tmp5
                associative_type1 = type(tmp5)
                subjects6 = deque(tmp5._args)
                matcher = CommutativeMatcher23924.get()
                tmp7 = subjects6
                subjects6 = []
                for s in tmp7:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp7, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 23925
                        if len(subjects) == 0:
                            pass
                            # 0: e + f*x
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 24235
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.1.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 24236
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.1.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 24237
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i2.1.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 24238
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24239
                            if len(subjects) >= 1:
                                tmp13 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.0', tmp13)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24240
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (d*(e + f*x)**p)**q
                                subjects.appendleft(tmp13)
                            if len(subjects) >= 1:
                                tmp15 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.1', tmp15)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26617
                                    if len(subjects) == 0:
                                        pass
                                        # 3: (d*(e + f*x)**p)**q
                                subjects.appendleft(tmp15)
                            if len(subjects) >= 1:
                                tmp17 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.3.1.0', tmp17)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27684
                                    if len(subjects) == 0:
                                        pass
                                        # 5: (d*(e + f*x)**p)**q
                                subjects.appendleft(tmp17)
                        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                            tmp19 = subjects.popleft()
                            associative1 = tmp19
                            associative_type1 = type(tmp19)
                            subjects20 = deque(tmp19._args)
                            matcher = CommutativeMatcher24242.get()
                            tmp21 = subjects20
                            subjects20 = []
                            for s in tmp21:
                                matcher.add_subject(s)
                            for pattern_index, subst5 in matcher.match(tmp21, subst4):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 24243
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (d*(e + f*x)**p)**q
                                if pattern_index == 1:
                                    pass
                                    # State 26618
                                    if len(subjects) == 0:
                                        pass
                                        # 3: (d*(e + f*x)**p)**q
                                if pattern_index == 2:
                                    pass
                                    # State 27685
                                    if len(subjects) == 0:
                                        pass
                                        # 5: (d*(e + f*x)**p)**q
                            subjects.appendleft(tmp19)
                    if len(subjects) >= 1 and isinstance(subjects[0], Add):
                        tmp22 = subjects.popleft()
                        associative1 = tmp22
                        associative_type1 = type(tmp22)
                        subjects23 = deque(tmp22._args)
                        matcher = CommutativeMatcher24245.get()
                        tmp24 = subjects23
                        subjects23 = []
                        for s in tmp24:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp24, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 24251
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d*(e + f*x)**p)**q
                            if pattern_index == 1:
                                pass
                                # State 26621
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x)**p)**q
                            if pattern_index == 2:
                                pass
                                # State 27263
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(e + f*x)**p)**q
                            if pattern_index == 3:
                                pass
                                # State 27688
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x)**p)**q
                        subjects.appendleft(tmp22)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp25 = subjects.popleft()
                    subjects26 = deque(tmp25._args)
                    # State 24252
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 24253
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24254
                            if len(subjects26) >= 1:
                                tmp29 = subjects26.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.0', tmp29)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24255
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 24256
                                        if len(subjects26) == 0:
                                            pass
                                            # State 24257
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (d*(e + f*x)**p)**q
                                    if len(subjects26) >= 1:
                                        tmp32 = subjects26.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2.2', tmp32)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24256
                                            if len(subjects26) == 0:
                                                pass
                                                # State 24257
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*(e + f*x)**p)**q
                                        subjects26.appendleft(tmp32)
                                subjects26.appendleft(tmp29)
                            if len(subjects26) >= 1:
                                tmp34 = subjects26.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.1', tmp34)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26622
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 26623
                                        if len(subjects26) == 0:
                                            pass
                                            # State 26624
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (d*(e + f*x)**p)**q
                                    if len(subjects26) >= 1:
                                        tmp37 = subjects26.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2.2', tmp37)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26623
                                            if len(subjects26) == 0:
                                                pass
                                                # State 26624
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x)**p)**q
                                        subjects26.appendleft(tmp37)
                                subjects26.appendleft(tmp34)
                            if len(subjects26) >= 1:
                                tmp39 = subjects26.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.3.1.0', tmp39)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27689
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27690
                                        if len(subjects26) == 0:
                                            pass
                                            # State 27691
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x)**p)**q
                                    if len(subjects26) >= 1:
                                        tmp42 = subjects26.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2.2', tmp42)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27690
                                            if len(subjects26) == 0:
                                                pass
                                                # State 27691
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x)**p)**q
                                        subjects26.appendleft(tmp42)
                                subjects26.appendleft(tmp39)
                        if len(subjects26) >= 1 and isinstance(subjects26[0], Mul):
                            tmp44 = subjects26.popleft()
                            associative1 = tmp44
                            associative_type1 = type(tmp44)
                            subjects45 = deque(tmp44._args)
                            matcher = CommutativeMatcher24259.get()
                            tmp46 = subjects45
                            subjects45 = []
                            for s in tmp46:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp46, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 24260
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 24261
                                        if len(subjects26) == 0:
                                            pass
                                            # State 24262
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (d*(e + f*x)**p)**q
                                    if len(subjects26) >= 1:
                                        tmp48 = []
                                        tmp48.append(subjects26.popleft())
                                        while True:
                                            if len(tmp48) > 1:
                                                tmp49 = create_operation_expression(associative1, tmp48)
                                            elif len(tmp48) == 1:
                                                tmp49 = tmp48[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.2', tmp49)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24261
                                                if len(subjects26) == 0:
                                                    pass
                                                    # State 24262
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*(e + f*x)**p)**q
                                            if len(subjects26) == 0:
                                                break
                                            tmp48.append(subjects26.popleft())
                                        subjects26.extendleft(reversed(tmp48))
                                if pattern_index == 1:
                                    pass
                                    # State 26625
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 26626
                                        if len(subjects26) == 0:
                                            pass
                                            # State 26627
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (d*(e + f*x)**p)**q
                                    if len(subjects26) >= 1:
                                        tmp52 = []
                                        tmp52.append(subjects26.popleft())
                                        while True:
                                            if len(tmp52) > 1:
                                                tmp53 = create_operation_expression(associative1, tmp52)
                                            elif len(tmp52) == 1:
                                                tmp53 = tmp52[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.2', tmp53)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26626
                                                if len(subjects26) == 0:
                                                    pass
                                                    # State 26627
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x)**p)**q
                                            if len(subjects26) == 0:
                                                break
                                            tmp52.append(subjects26.popleft())
                                        subjects26.extendleft(reversed(tmp52))
                                if pattern_index == 2:
                                    pass
                                    # State 27692
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27693
                                        if len(subjects26) == 0:
                                            pass
                                            # State 27694
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x)**p)**q
                                    if len(subjects26) >= 1:
                                        tmp56 = []
                                        tmp56.append(subjects26.popleft())
                                        while True:
                                            if len(tmp56) > 1:
                                                tmp57 = create_operation_expression(associative1, tmp56)
                                            elif len(tmp56) == 1:
                                                tmp57 = tmp56[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2.2', tmp57)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27693
                                                if len(subjects26) == 0:
                                                    pass
                                                    # State 27694
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x)**p)**q
                                            if len(subjects26) == 0:
                                                break
                                            tmp56.append(subjects26.popleft())
                                        subjects26.extendleft(reversed(tmp56))
                            subjects26.appendleft(tmp44)
                    if len(subjects26) >= 1 and isinstance(subjects26[0], Add):
                        tmp59 = subjects26.popleft()
                        associative1 = tmp59
                        associative_type1 = type(tmp59)
                        subjects60 = deque(tmp59._args)
                        matcher = CommutativeMatcher24264.get()
                        tmp61 = subjects60
                        subjects60 = []
                        for s in tmp61:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp61, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 24270
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24271
                                    if len(subjects26) == 0:
                                        pass
                                        # State 24272
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*(e + f*x)**p)**q
                                if len(subjects26) >= 1:
                                    tmp63 = []
                                    tmp63.append(subjects26.popleft())
                                    while True:
                                        if len(tmp63) > 1:
                                            tmp64 = create_operation_expression(associative1, tmp63)
                                        elif len(tmp63) == 1:
                                            tmp64 = tmp63[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', tmp64)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24271
                                            if len(subjects26) == 0:
                                                pass
                                                # State 24272
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*(e + f*x)**p)**q
                                        if len(subjects26) == 0:
                                            break
                                        tmp63.append(subjects26.popleft())
                                    subjects26.extendleft(reversed(tmp63))
                            if pattern_index == 1:
                                pass
                                # State 26630
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26631
                                    if len(subjects26) == 0:
                                        pass
                                        # State 26632
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x)**p)**q
                                if len(subjects26) >= 1:
                                    tmp67 = []
                                    tmp67.append(subjects26.popleft())
                                    while True:
                                        if len(tmp67) > 1:
                                            tmp68 = create_operation_expression(associative1, tmp67)
                                        elif len(tmp67) == 1:
                                            tmp68 = tmp67[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', tmp68)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26631
                                            if len(subjects26) == 0:
                                                pass
                                                # State 26632
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x)**p)**q
                                        if len(subjects26) == 0:
                                            break
                                        tmp67.append(subjects26.popleft())
                                    subjects26.extendleft(reversed(tmp67))
                            if pattern_index == 2:
                                pass
                                # State 27264
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27265
                                    if len(subjects26) == 0:
                                        pass
                                        # State 27266
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(e + f*x)**p)**q
                                if len(subjects26) >= 1:
                                    tmp71 = []
                                    tmp71.append(subjects26.popleft())
                                    while True:
                                        if len(tmp71) > 1:
                                            tmp72 = create_operation_expression(associative1, tmp71)
                                        elif len(tmp71) == 1:
                                            tmp72 = tmp71[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', tmp72)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27265
                                            if len(subjects26) == 0:
                                                pass
                                                # State 27266
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(e + f*x)**p)**q
                                        if len(subjects26) == 0:
                                            break
                                        tmp71.append(subjects26.popleft())
                                    subjects26.extendleft(reversed(tmp71))
                            if pattern_index == 3:
                                pass
                                # State 27697
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27698
                                    if len(subjects26) == 0:
                                        pass
                                        # State 27699
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x)**p)**q
                                if len(subjects26) >= 1:
                                    tmp75 = []
                                    tmp75.append(subjects26.popleft())
                                    while True:
                                        if len(tmp75) > 1:
                                            tmp76 = create_operation_expression(associative1, tmp75)
                                        elif len(tmp75) == 1:
                                            tmp76 = tmp75[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2.2', tmp76)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27698
                                            if len(subjects26) == 0:
                                                pass
                                                # State 27699
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x)**p)**q
                                        if len(subjects26) == 0:
                                            break
                                        tmp75.append(subjects26.popleft())
                                    subjects26.extendleft(reversed(tmp75))
                        subjects26.appendleft(tmp59)
                    subjects.appendleft(tmp25)
            if len(subjects) >= 1:
                tmp78 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp78)
                except ValueError:
                    pass
                else:
                    pass
                    # State 40403
                    if len(subjects) == 0:
                        pass
                        # 6: x**n
                subjects.appendleft(tmp78)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.1.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 49360
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.1.1.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 49361
                    if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                        tmp82 = subjects.popleft()
                        subjects83 = deque(tmp82._args)
                        # State 49362
                        if len(subjects83) >= 1:
                            tmp84 = subjects83.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp84)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49363
                                if len(subjects83) >= 1:
                                    tmp86 = subjects83.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.1.2', tmp86)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49364
                                        if len(subjects83) == 0:
                                            pass
                                            # State 49365
                                            if len(subjects) == 0:
                                                pass
                                                # 7: (d + e*x**n)**p
                                    subjects83.appendleft(tmp86)
                            subjects83.appendleft(tmp84)
                        if len(subjects83) >= 1:
                            tmp88 = subjects83.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.1.0', tmp88)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49904
                                if len(subjects83) >= 1:
                                    tmp90 = subjects83.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.1.2', tmp90)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49905
                                        if len(subjects83) == 0:
                                            pass
                                            # State 49906
                                            if len(subjects) == 0:
                                                pass
                                                # 9: (d + e*x**n)**p
                                    subjects83.appendleft(tmp90)
                            subjects83.appendleft(tmp88)
                        if len(subjects83) >= 1:
                            tmp92 = subjects83.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.1', tmp92)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 50230
                                if len(subjects83) >= 1 and subjects83[0] == 2:
                                    tmp94 = subjects83.popleft()
                                    # State 50231
                                    if len(subjects83) == 0:
                                        pass
                                        # State 50232
                                        if len(subjects) == 0:
                                            pass
                                            # 10: (d + e*x**2)**p
                                    subjects83.appendleft(tmp94)
                            subjects83.appendleft(tmp92)
                        subjects.appendleft(tmp82)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp95 = subjects.popleft()
                    associative1 = tmp95
                    associative_type1 = type(tmp95)
                    subjects96 = deque(tmp95._args)
                    matcher = CommutativeMatcher49367.get()
                    tmp97 = subjects96
                    subjects96 = []
                    for s in tmp97:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp97, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 49372
                            if len(subjects) == 0:
                                pass
                                # 7: (d + e*x**n)**p
                        if pattern_index == 1:
                            pass
                            # State 49910
                            if len(subjects) == 0:
                                pass
                                # 9: (d + e*x**n)**p
                        if pattern_index == 2:
                            pass
                            # State 50236
                            if len(subjects) == 0:
                                pass
                                # 10: (d + e*x**2)**p
                    subjects.appendleft(tmp95)
            if len(subjects) >= 1:
                tmp98 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.1', tmp98)
                except ValueError:
                    pass
                else:
                    pass
                    # State 49772
                    if len(subjects) == 0:
                        pass
                        # 8: v**p
                subjects.appendleft(tmp98)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp100 = subjects.popleft()
                associative1 = tmp100
                associative_type1 = type(tmp100)
                subjects101 = deque(tmp100._args)
                matcher = CommutativeMatcher24274.get()
                tmp102 = subjects101
                subjects101 = []
                for s in tmp102:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp102, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 24311
                        if len(subjects) == 0:
                            pass
                            # 1: (d*(e + f*x)**p)**q
                    if pattern_index == 1:
                        pass
                        # State 26649
                        if len(subjects) == 0:
                            pass
                            # 3: (d*(e + f*x)**p)**q
                    if pattern_index == 2:
                        pass
                        # State 27271
                        if len(subjects) == 0:
                            pass
                            # 4: (d*(e + f*x)**p)**q
                    if pattern_index == 3:
                        pass
                        # State 27716
                        if len(subjects) == 0:
                            pass
                            # 5: (d*(e + f*x)**p)**q
                subjects.appendleft(tmp100)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp103 = subjects.popleft()
                associative1 = tmp103
                associative_type1 = type(tmp103)
                subjects104 = deque(tmp103._args)
                matcher = CommutativeMatcher49374.get()
                tmp105 = subjects104
                subjects104 = []
                for s in tmp105:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp105, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 49387
                        if len(subjects) == 0:
                            pass
                            # 7: (d + e*x**n)**p
                    if pattern_index == 1:
                        pass
                        # State 49918
                        if len(subjects) == 0:
                            pass
                            # 9: (d + e*x**n)**p
                    if pattern_index == 2:
                        pass
                        # State 50244
                        if len(subjects) == 0:
                            pass
                            # 10: (d + e*x**2)**p
                subjects.appendleft(tmp103)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp106 = subjects.popleft()
            associative1 = tmp106
            associative_type1 = type(tmp106)
            subjects107 = deque(tmp106._args)
            matcher = CommutativeMatcher23927.get()
            tmp108 = subjects107
            subjects107 = []
            for s in tmp108:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp108, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 23933
                    if len(subjects) == 0:
                        pass
                        # 0: e + f*x
            subjects.appendleft(tmp106)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp109 = subjects.popleft()
            subjects110 = deque(tmp109._args)
            # State 24312
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 24313
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 24314
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 24315
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24316
                            if len(subjects110) >= 1:
                                tmp115 = subjects110.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.0', tmp115)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24317
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 24318
                                        if len(subjects110) == 0:
                                            pass
                                            # State 24319
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (d*(e + f*x)**p)**q
                                    if len(subjects110) >= 1:
                                        tmp118 = subjects110.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2', tmp118)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24318
                                            if len(subjects110) == 0:
                                                pass
                                                # State 24319
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*(e + f*x)**p)**q
                                        subjects110.appendleft(tmp118)
                                subjects110.appendleft(tmp115)
                            if len(subjects110) >= 1:
                                tmp120 = subjects110.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.1', tmp120)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26650
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 26651
                                        if len(subjects110) == 0:
                                            pass
                                            # State 26652
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (d*(e + f*x)**p)**q
                                    if len(subjects110) >= 1:
                                        tmp123 = subjects110.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2', tmp123)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26651
                                            if len(subjects110) == 0:
                                                pass
                                                # State 26652
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x)**p)**q
                                        subjects110.appendleft(tmp123)
                                subjects110.appendleft(tmp120)
                            if len(subjects110) >= 1:
                                tmp125 = subjects110.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.3.1.0', tmp125)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27717
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27718
                                        if len(subjects110) == 0:
                                            pass
                                            # State 27719
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x)**p)**q
                                    if len(subjects110) >= 1:
                                        tmp128 = subjects110.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2', tmp128)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27718
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27719
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x)**p)**q
                                        subjects110.appendleft(tmp128)
                                subjects110.appendleft(tmp125)
                        if len(subjects110) >= 1 and isinstance(subjects110[0], Mul):
                            tmp130 = subjects110.popleft()
                            associative1 = tmp130
                            associative_type1 = type(tmp130)
                            subjects131 = deque(tmp130._args)
                            matcher = CommutativeMatcher24321.get()
                            tmp132 = subjects131
                            subjects131 = []
                            for s in tmp132:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp132, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 24322
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 24323
                                        if len(subjects110) == 0:
                                            pass
                                            # State 24324
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (d*(e + f*x)**p)**q
                                    if len(subjects110) >= 1:
                                        tmp134 = []
                                        tmp134.append(subjects110.popleft())
                                        while True:
                                            if len(tmp134) > 1:
                                                tmp135 = create_operation_expression(associative1, tmp134)
                                            elif len(tmp134) == 1:
                                                tmp135 = tmp134[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', tmp135)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24323
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 24324
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*(e + f*x)**p)**q
                                            if len(subjects110) == 0:
                                                break
                                            tmp134.append(subjects110.popleft())
                                        subjects110.extendleft(reversed(tmp134))
                                if pattern_index == 1:
                                    pass
                                    # State 26653
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 26654
                                        if len(subjects110) == 0:
                                            pass
                                            # State 26655
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (d*(e + f*x)**p)**q
                                    if len(subjects110) >= 1:
                                        tmp138 = []
                                        tmp138.append(subjects110.popleft())
                                        while True:
                                            if len(tmp138) > 1:
                                                tmp139 = create_operation_expression(associative1, tmp138)
                                            elif len(tmp138) == 1:
                                                tmp139 = tmp138[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', tmp139)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26654
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 26655
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x)**p)**q
                                            if len(subjects110) == 0:
                                                break
                                            tmp138.append(subjects110.popleft())
                                        subjects110.extendleft(reversed(tmp138))
                                if pattern_index == 2:
                                    pass
                                    # State 27720
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27721
                                        if len(subjects110) == 0:
                                            pass
                                            # State 27722
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x)**p)**q
                                    if len(subjects110) >= 1:
                                        tmp142 = []
                                        tmp142.append(subjects110.popleft())
                                        while True:
                                            if len(tmp142) > 1:
                                                tmp143 = create_operation_expression(associative1, tmp142)
                                            elif len(tmp142) == 1:
                                                tmp143 = tmp142[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', tmp143)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27721
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27722
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x)**p)**q
                                            if len(subjects110) == 0:
                                                break
                                            tmp142.append(subjects110.popleft())
                                        subjects110.extendleft(reversed(tmp142))
                            subjects110.appendleft(tmp130)
                    if len(subjects110) >= 1 and isinstance(subjects110[0], Add):
                        tmp145 = subjects110.popleft()
                        associative1 = tmp145
                        associative_type1 = type(tmp145)
                        subjects146 = deque(tmp145._args)
                        matcher = CommutativeMatcher24326.get()
                        tmp147 = subjects146
                        subjects146 = []
                        for s in tmp147:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp147, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 24332
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24333
                                    if len(subjects110) == 0:
                                        pass
                                        # State 24334
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*(e + f*x)**p)**q
                                if len(subjects110) >= 1:
                                    tmp149 = []
                                    tmp149.append(subjects110.popleft())
                                    while True:
                                        if len(tmp149) > 1:
                                            tmp150 = create_operation_expression(associative1, tmp149)
                                        elif len(tmp149) == 1:
                                            tmp150 = tmp149[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', tmp150)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24333
                                            if len(subjects110) == 0:
                                                pass
                                                # State 24334
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*(e + f*x)**p)**q
                                        if len(subjects110) == 0:
                                            break
                                        tmp149.append(subjects110.popleft())
                                    subjects110.extendleft(reversed(tmp149))
                            if pattern_index == 1:
                                pass
                                # State 26658
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26659
                                    if len(subjects110) == 0:
                                        pass
                                        # State 26660
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x)**p)**q
                                if len(subjects110) >= 1:
                                    tmp153 = []
                                    tmp153.append(subjects110.popleft())
                                    while True:
                                        if len(tmp153) > 1:
                                            tmp154 = create_operation_expression(associative1, tmp153)
                                        elif len(tmp153) == 1:
                                            tmp154 = tmp153[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', tmp154)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26659
                                            if len(subjects110) == 0:
                                                pass
                                                # State 26660
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x)**p)**q
                                        if len(subjects110) == 0:
                                            break
                                        tmp153.append(subjects110.popleft())
                                    subjects110.extendleft(reversed(tmp153))
                            if pattern_index == 2:
                                pass
                                # State 27272
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27273
                                    if len(subjects110) == 0:
                                        pass
                                        # State 27274
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(e + f*x)**p)**q
                                if len(subjects110) >= 1:
                                    tmp157 = []
                                    tmp157.append(subjects110.popleft())
                                    while True:
                                        if len(tmp157) > 1:
                                            tmp158 = create_operation_expression(associative1, tmp157)
                                        elif len(tmp157) == 1:
                                            tmp158 = tmp157[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', tmp158)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27273
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27274
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(e + f*x)**p)**q
                                        if len(subjects110) == 0:
                                            break
                                        tmp157.append(subjects110.popleft())
                                    subjects110.extendleft(reversed(tmp157))
                            if pattern_index == 3:
                                pass
                                # State 27725
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27726
                                    if len(subjects110) == 0:
                                        pass
                                        # State 27727
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x)**p)**q
                                if len(subjects110) >= 1:
                                    tmp161 = []
                                    tmp161.append(subjects110.popleft())
                                    while True:
                                        if len(tmp161) > 1:
                                            tmp162 = create_operation_expression(associative1, tmp161)
                                        elif len(tmp161) == 1:
                                            tmp162 = tmp161[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', tmp162)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27726
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27727
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x)**p)**q
                                        if len(subjects110) == 0:
                                            break
                                        tmp161.append(subjects110.popleft())
                                    subjects110.extendleft(reversed(tmp161))
                        subjects110.appendleft(tmp145)
                if len(subjects110) >= 1 and isinstance(subjects110[0], Pow):
                    tmp164 = subjects110.popleft()
                    subjects165 = deque(tmp164._args)
                    # State 24335
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 24336
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24337
                            if len(subjects165) >= 1:
                                tmp168 = subjects165.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.0', tmp168)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24338
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 24339
                                        if len(subjects165) == 0:
                                            pass
                                            # State 24340
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24341
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 24342
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*(e + f*x)**p)**q
                                            if len(subjects110) >= 1:
                                                tmp172 = subjects110.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', tmp172)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24341
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 24342
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: (d*(e + f*x)**p)**q
                                                subjects110.appendleft(tmp172)
                                    if len(subjects165) >= 1:
                                        tmp174 = subjects165.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', tmp174)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24339
                                            if len(subjects165) == 0:
                                                pass
                                                # State 24340
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24341
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 24342
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: (d*(e + f*x)**p)**q
                                                if len(subjects110) >= 1:
                                                    tmp177 = subjects110.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp177)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 24341
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 24342
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (d*(e + f*x)**p)**q
                                                    subjects110.appendleft(tmp177)
                                        subjects165.appendleft(tmp174)
                                subjects165.appendleft(tmp168)
                            if len(subjects165) >= 1:
                                tmp179 = subjects165.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.1', tmp179)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26661
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 26662
                                        if len(subjects165) == 0:
                                            pass
                                            # State 26663
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26664
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 26665
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x)**p)**q
                                            if len(subjects110) >= 1:
                                                tmp183 = subjects110.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', tmp183)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26664
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 26665
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: (d*(e + f*x)**p)**q
                                                subjects110.appendleft(tmp183)
                                    if len(subjects165) >= 1:
                                        tmp185 = subjects165.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', tmp185)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26662
                                            if len(subjects165) == 0:
                                                pass
                                                # State 26663
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26664
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 26665
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: (d*(e + f*x)**p)**q
                                                if len(subjects110) >= 1:
                                                    tmp188 = subjects110.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp188)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 26664
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 26665
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: (d*(e + f*x)**p)**q
                                                    subjects110.appendleft(tmp188)
                                        subjects165.appendleft(tmp185)
                                subjects165.appendleft(tmp179)
                            if len(subjects165) >= 1:
                                tmp190 = subjects165.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.0', tmp190)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27728
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27729
                                        if len(subjects165) == 0:
                                            pass
                                            # State 27730
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27731
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27732
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x)**p)**q
                                            if len(subjects110) >= 1:
                                                tmp194 = subjects110.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', tmp194)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27731
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27732
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x)**p)**q
                                                subjects110.appendleft(tmp194)
                                    if len(subjects165) >= 1:
                                        tmp196 = subjects165.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.1.1.2.2.2', tmp196)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27729
                                            if len(subjects165) == 0:
                                                pass
                                                # State 27730
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27731
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27732
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x)**p)**q
                                                if len(subjects110) >= 1:
                                                    tmp199 = subjects110.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp199)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27731
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 27732
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x)**p)**q
                                                    subjects110.appendleft(tmp199)
                                        subjects165.appendleft(tmp196)
                                subjects165.appendleft(tmp190)
                        if len(subjects165) >= 1 and isinstance(subjects165[0], Mul):
                            tmp201 = subjects165.popleft()
                            associative1 = tmp201
                            associative_type1 = type(tmp201)
                            subjects202 = deque(tmp201._args)
                            matcher = CommutativeMatcher24344.get()
                            tmp203 = subjects202
                            subjects202 = []
                            for s in tmp203:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp203, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 24345
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 24346
                                        if len(subjects165) == 0:
                                            pass
                                            # State 24347
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24348
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 24349
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*(e + f*x)**p)**q
                                            if len(subjects110) >= 1:
                                                tmp206 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp206)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24348
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 24349
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: (d*(e + f*x)**p)**q
                                                subjects110.appendleft(tmp206)
                                    if len(subjects165) >= 1:
                                        tmp208 = []
                                        tmp208.append(subjects165.popleft())
                                        while True:
                                            if len(tmp208) > 1:
                                                tmp209 = create_operation_expression(associative1, tmp208)
                                            elif len(tmp208) == 1:
                                                tmp209 = tmp208[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2.2', tmp209)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24346
                                                if len(subjects165) == 0:
                                                    pass
                                                    # State 24347
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 24348
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 24349
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (d*(e + f*x)**p)**q
                                                    if len(subjects110) >= 1:
                                                        tmp212 = subjects110.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', tmp212)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 24348
                                                            if len(subjects110) == 0:
                                                                pass
                                                                # State 24349
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 1: (d*(e + f*x)**p)**q
                                                        subjects110.appendleft(tmp212)
                                            if len(subjects165) == 0:
                                                break
                                            tmp208.append(subjects165.popleft())
                                        subjects165.extendleft(reversed(tmp208))
                                if pattern_index == 1:
                                    pass
                                    # State 26666
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 26667
                                        if len(subjects165) == 0:
                                            pass
                                            # State 26668
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26669
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 26670
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x)**p)**q
                                            if len(subjects110) >= 1:
                                                tmp216 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp216)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26669
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 26670
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: (d*(e + f*x)**p)**q
                                                subjects110.appendleft(tmp216)
                                    if len(subjects165) >= 1:
                                        tmp218 = []
                                        tmp218.append(subjects165.popleft())
                                        while True:
                                            if len(tmp218) > 1:
                                                tmp219 = create_operation_expression(associative1, tmp218)
                                            elif len(tmp218) == 1:
                                                tmp219 = tmp218[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2.2', tmp219)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26667
                                                if len(subjects165) == 0:
                                                    pass
                                                    # State 26668
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 26669
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 26670
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: (d*(e + f*x)**p)**q
                                                    if len(subjects110) >= 1:
                                                        tmp222 = subjects110.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', tmp222)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 26669
                                                            if len(subjects110) == 0:
                                                                pass
                                                                # State 26670
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 3: (d*(e + f*x)**p)**q
                                                        subjects110.appendleft(tmp222)
                                            if len(subjects165) == 0:
                                                break
                                            tmp218.append(subjects165.popleft())
                                        subjects165.extendleft(reversed(tmp218))
                                if pattern_index == 2:
                                    pass
                                    # State 27733
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27734
                                        if len(subjects165) == 0:
                                            pass
                                            # State 27735
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27736
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27737
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x)**p)**q
                                            if len(subjects110) >= 1:
                                                tmp226 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp226)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27736
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27737
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x)**p)**q
                                                subjects110.appendleft(tmp226)
                                    if len(subjects165) >= 1:
                                        tmp228 = []
                                        tmp228.append(subjects165.popleft())
                                        while True:
                                            if len(tmp228) > 1:
                                                tmp229 = create_operation_expression(associative1, tmp228)
                                            elif len(tmp228) == 1:
                                                tmp229 = tmp228[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2.2', tmp229)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27734
                                                if len(subjects165) == 0:
                                                    pass
                                                    # State 27735
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27736
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 27737
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x)**p)**q
                                                    if len(subjects110) >= 1:
                                                        tmp232 = subjects110.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', tmp232)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 27736
                                                            if len(subjects110) == 0:
                                                                pass
                                                                # State 27737
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x)**p)**q
                                                        subjects110.appendleft(tmp232)
                                            if len(subjects165) == 0:
                                                break
                                            tmp228.append(subjects165.popleft())
                                        subjects165.extendleft(reversed(tmp228))
                            subjects165.appendleft(tmp201)
                    if len(subjects165) >= 1 and isinstance(subjects165[0], Add):
                        tmp234 = subjects165.popleft()
                        associative1 = tmp234
                        associative_type1 = type(tmp234)
                        subjects235 = deque(tmp234._args)
                        matcher = CommutativeMatcher24351.get()
                        tmp236 = subjects235
                        subjects235 = []
                        for s in tmp236:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp236, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 24357
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24358
                                    if len(subjects165) == 0:
                                        pass
                                        # State 24359
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24360
                                            if len(subjects110) == 0:
                                                pass
                                                # State 24361
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*(e + f*x)**p)**q
                                        if len(subjects110) >= 1:
                                            tmp239 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp239)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 24360
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 24361
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*(e + f*x)**p)**q
                                            subjects110.appendleft(tmp239)
                                if len(subjects165) >= 1:
                                    tmp241 = []
                                    tmp241.append(subjects165.popleft())
                                    while True:
                                        if len(tmp241) > 1:
                                            tmp242 = create_operation_expression(associative1, tmp241)
                                        elif len(tmp241) == 1:
                                            tmp242 = tmp241[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2.2', tmp242)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 24358
                                            if len(subjects165) == 0:
                                                pass
                                                # State 24359
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 24360
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 24361
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: (d*(e + f*x)**p)**q
                                                if len(subjects110) >= 1:
                                                    tmp245 = subjects110.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.2.2', tmp245)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 24360
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 24361
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (d*(e + f*x)**p)**q
                                                    subjects110.appendleft(tmp245)
                                        if len(subjects165) == 0:
                                            break
                                        tmp241.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp241))
                            if pattern_index == 1:
                                pass
                                # State 26673
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26674
                                    if len(subjects165) == 0:
                                        pass
                                        # State 26675
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26676
                                            if len(subjects110) == 0:
                                                pass
                                                # State 26677
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x)**p)**q
                                        if len(subjects110) >= 1:
                                            tmp249 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp249)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 26676
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 26677
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x)**p)**q
                                            subjects110.appendleft(tmp249)
                                if len(subjects165) >= 1:
                                    tmp251 = []
                                    tmp251.append(subjects165.popleft())
                                    while True:
                                        if len(tmp251) > 1:
                                            tmp252 = create_operation_expression(associative1, tmp251)
                                        elif len(tmp251) == 1:
                                            tmp252 = tmp251[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2.2', tmp252)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 26674
                                            if len(subjects165) == 0:
                                                pass
                                                # State 26675
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 26676
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 26677
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: (d*(e + f*x)**p)**q
                                                if len(subjects110) >= 1:
                                                    tmp255 = subjects110.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.2.2', tmp255)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 26676
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 26677
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: (d*(e + f*x)**p)**q
                                                    subjects110.appendleft(tmp255)
                                        if len(subjects165) == 0:
                                            break
                                        tmp251.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp251))
                            if pattern_index == 2:
                                pass
                                # State 27275
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27276
                                    if len(subjects165) == 0:
                                        pass
                                        # State 27277
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27278
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27279
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(e + f*x)**p)**q
                                        if len(subjects110) >= 1:
                                            tmp259 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp259)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27278
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27279
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (d*(e + f*x)**p)**q
                                            subjects110.appendleft(tmp259)
                                if len(subjects165) >= 1:
                                    tmp261 = []
                                    tmp261.append(subjects165.popleft())
                                    while True:
                                        if len(tmp261) > 1:
                                            tmp262 = create_operation_expression(associative1, tmp261)
                                        elif len(tmp261) == 1:
                                            tmp262 = tmp261[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2.2', tmp262)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27276
                                            if len(subjects165) == 0:
                                                pass
                                                # State 27277
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27278
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27279
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (d*(e + f*x)**p)**q
                                                if len(subjects110) >= 1:
                                                    tmp265 = subjects110.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.2.2', tmp265)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27278
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 27279
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (d*(e + f*x)**p)**q
                                                    subjects110.appendleft(tmp265)
                                        if len(subjects165) == 0:
                                            break
                                        tmp261.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp261))
                            if pattern_index == 3:
                                pass
                                # State 27740
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27741
                                    if len(subjects165) == 0:
                                        pass
                                        # State 27742
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27743
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27744
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x)**p)**q
                                        if len(subjects110) >= 1:
                                            tmp269 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp269)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27743
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27744
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x)**p)**q
                                            subjects110.appendleft(tmp269)
                                if len(subjects165) >= 1:
                                    tmp271 = []
                                    tmp271.append(subjects165.popleft())
                                    while True:
                                        if len(tmp271) > 1:
                                            tmp272 = create_operation_expression(associative1, tmp271)
                                        elif len(tmp271) == 1:
                                            tmp272 = tmp271[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.1.1.2.2.2', tmp272)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27741
                                            if len(subjects165) == 0:
                                                pass
                                                # State 27742
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27743
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27744
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x)**p)**q
                                                if len(subjects110) >= 1:
                                                    tmp275 = subjects110.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.2.2', tmp275)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27743
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 27744
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x)**p)**q
                                                    subjects110.appendleft(tmp275)
                                        if len(subjects165) == 0:
                                            break
                                        tmp271.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp271))
                        subjects165.appendleft(tmp234)
                    subjects110.appendleft(tmp164)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 26396
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 26397
                    if len(subjects110) >= 1:
                        tmp279 = subjects110.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp279)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 26398
                            if len(subjects110) >= 1 and subjects110[0] == -1:
                                tmp281 = subjects110.popleft()
                                # State 26399
                                if len(subjects110) == 0:
                                    pass
                                    # State 26400
                                    if len(subjects) == 0:
                                        pass
                                        # 2: 1/(e + f*x)
                                subjects110.appendleft(tmp281)
                        subjects110.appendleft(tmp279)
                    if len(subjects110) >= 1 and isinstance(subjects110[0], Pow):
                        tmp282 = subjects110.popleft()
                        subjects283 = deque(tmp282._args)
                        # State 49388
                        if len(subjects283) >= 1:
                            tmp284 = subjects283.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.0', tmp284)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49389
                                if len(subjects283) >= 1:
                                    tmp286 = subjects283.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.1.2', tmp286)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49390
                                        if len(subjects283) == 0:
                                            pass
                                            # State 49391
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49392
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 49393
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: (d + e*x**n)**p
                                            if len(subjects110) >= 1:
                                                tmp289 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp289)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 49392
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 49393
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 7: (d + e*x**n)**p
                                                subjects110.appendleft(tmp289)
                                    subjects283.appendleft(tmp286)
                            subjects283.appendleft(tmp284)
                        if len(subjects283) >= 1:
                            tmp291 = subjects283.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.0', tmp291)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49919
                                if len(subjects283) >= 1:
                                    tmp293 = subjects283.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.1.2', tmp293)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49920
                                        if len(subjects283) == 0:
                                            pass
                                            # State 49921
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49922
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 49923
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 9: (d + e*x**n)**p
                                            if len(subjects110) >= 1:
                                                tmp296 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp296)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 49922
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 49923
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 9: (d + e*x**n)**p
                                                subjects110.appendleft(tmp296)
                                    subjects283.appendleft(tmp293)
                            subjects283.appendleft(tmp291)
                        if len(subjects283) >= 1:
                            tmp298 = subjects283.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.1', tmp298)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 50245
                                if len(subjects283) >= 1 and subjects283[0] == 2:
                                    tmp300 = subjects283.popleft()
                                    # State 50246
                                    if len(subjects283) == 0:
                                        pass
                                        # State 50247
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 50248
                                            if len(subjects110) == 0:
                                                pass
                                                # State 50249
                                                if len(subjects) == 0:
                                                    pass
                                                    # 10: (d + e*x**2)**p
                                        if len(subjects110) >= 1:
                                            tmp302 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp302)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 50248
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 50249
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 10: (d + e*x**2)**p
                                            subjects110.appendleft(tmp302)
                                    subjects283.appendleft(tmp300)
                            subjects283.appendleft(tmp298)
                        subjects110.appendleft(tmp282)
                if len(subjects110) >= 1 and isinstance(subjects110[0], Mul):
                    tmp304 = subjects110.popleft()
                    associative1 = tmp304
                    associative_type1 = type(tmp304)
                    subjects305 = deque(tmp304._args)
                    matcher = CommutativeMatcher26402.get()
                    tmp306 = subjects305
                    subjects305 = []
                    for s in tmp306:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp306, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 26403
                            if len(subjects110) >= 1 and subjects110[0] == -1:
                                tmp307 = subjects110.popleft()
                                # State 26404
                                if len(subjects110) == 0:
                                    pass
                                    # State 26405
                                    if len(subjects) == 0:
                                        pass
                                        # 2: 1/(e + f*x)
                                subjects110.appendleft(tmp307)
                        if pattern_index == 1:
                            pass
                            # State 49398
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49399
                                if len(subjects110) == 0:
                                    pass
                                    # State 49400
                                    if len(subjects) == 0:
                                        pass
                                        # 7: (d + e*x**n)**p
                            if len(subjects110) >= 1:
                                tmp309 = []
                                tmp309.append(subjects110.popleft())
                                while True:
                                    if len(tmp309) > 1:
                                        tmp310 = create_operation_expression(associative1, tmp309)
                                    elif len(tmp309) == 1:
                                        tmp310 = tmp309[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.1.1.2.2', tmp310)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49399
                                        if len(subjects110) == 0:
                                            pass
                                            # State 49400
                                            if len(subjects) == 0:
                                                pass
                                                # 7: (d + e*x**n)**p
                                    if len(subjects110) == 0:
                                        break
                                    tmp309.append(subjects110.popleft())
                                subjects110.extendleft(reversed(tmp309))
                        if pattern_index == 2:
                            pass
                            # State 49927
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49928
                                if len(subjects110) == 0:
                                    pass
                                    # State 49929
                                    if len(subjects) == 0:
                                        pass
                                        # 9: (d + e*x**n)**p
                            if len(subjects110) >= 1:
                                tmp313 = []
                                tmp313.append(subjects110.popleft())
                                while True:
                                    if len(tmp313) > 1:
                                        tmp314 = create_operation_expression(associative1, tmp313)
                                    elif len(tmp313) == 1:
                                        tmp314 = tmp313[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.1.1.2.2', tmp314)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49928
                                        if len(subjects110) == 0:
                                            pass
                                            # State 49929
                                            if len(subjects) == 0:
                                                pass
                                                # 9: (d + e*x**n)**p
                                    if len(subjects110) == 0:
                                        break
                                    tmp313.append(subjects110.popleft())
                                subjects110.extendleft(reversed(tmp313))
                        if pattern_index == 3:
                            pass
                            # State 50253
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 50254
                                if len(subjects110) == 0:
                                    pass
                                    # State 50255
                                    if len(subjects) == 0:
                                        pass
                                        # 10: (d + e*x**2)**p
                            if len(subjects110) >= 1:
                                tmp317 = []
                                tmp317.append(subjects110.popleft())
                                while True:
                                    if len(tmp317) > 1:
                                        tmp318 = create_operation_expression(associative1, tmp317)
                                    elif len(tmp317) == 1:
                                        tmp318 = tmp317[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.1.1.2.2', tmp318)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50254
                                        if len(subjects110) == 0:
                                            pass
                                            # State 50255
                                            if len(subjects) == 0:
                                                pass
                                                # 10: (d + e*x**2)**p
                                    if len(subjects110) == 0:
                                        break
                                    tmp317.append(subjects110.popleft())
                                subjects110.extendleft(reversed(tmp317))
                    subjects110.appendleft(tmp304)
            if len(subjects110) >= 1:
                tmp320 = subjects110.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp320)
                except ValueError:
                    pass
                else:
                    pass
                    # State 40404
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 40405
                        if len(subjects110) == 0:
                            pass
                            # State 40406
                            if len(subjects) == 0:
                                pass
                                # 6: x**n
                    if len(subjects110) >= 1:
                        tmp323 = subjects110.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', tmp323)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40405
                            if len(subjects110) == 0:
                                pass
                                # State 40406
                                if len(subjects) == 0:
                                    pass
                                    # 6: x**n
                        subjects110.appendleft(tmp323)
                subjects110.appendleft(tmp320)
            if len(subjects110) >= 1:
                tmp325 = subjects110.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.2.1', tmp325)
                except ValueError:
                    pass
                else:
                    pass
                    # State 49773
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 49774
                        if len(subjects110) == 0:
                            pass
                            # State 49775
                            if len(subjects) == 0:
                                pass
                                # 8: v**p
                    if len(subjects110) >= 1:
                        tmp328 = subjects110.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', tmp328)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49774
                            if len(subjects110) == 0:
                                pass
                                # State 49775
                                if len(subjects) == 0:
                                    pass
                                    # 8: v**p
                        subjects110.appendleft(tmp328)
                subjects110.appendleft(tmp325)
            if len(subjects110) >= 1 and isinstance(subjects110[0], Mul):
                tmp330 = subjects110.popleft()
                associative1 = tmp330
                associative_type1 = type(tmp330)
                subjects331 = deque(tmp330._args)
                matcher = CommutativeMatcher24363.get()
                tmp332 = subjects331
                subjects331 = []
                for s in tmp332:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp332, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 24400
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 24401
                            if len(subjects110) == 0:
                                pass
                                # State 24402
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d*(e + f*x)**p)**q
                        if len(subjects110) >= 1:
                            tmp334 = []
                            tmp334.append(subjects110.popleft())
                            while True:
                                if len(tmp334) > 1:
                                    tmp335 = create_operation_expression(associative1, tmp334)
                                elif len(tmp334) == 1:
                                    tmp335 = tmp334[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp335)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 24401
                                    if len(subjects110) == 0:
                                        pass
                                        # State 24402
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*(e + f*x)**p)**q
                                if len(subjects110) == 0:
                                    break
                                tmp334.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp334))
                    if pattern_index == 1:
                        pass
                        # State 26694
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 26695
                            if len(subjects110) == 0:
                                pass
                                # State 26696
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x)**p)**q
                        if len(subjects110) >= 1:
                            tmp338 = []
                            tmp338.append(subjects110.popleft())
                            while True:
                                if len(tmp338) > 1:
                                    tmp339 = create_operation_expression(associative1, tmp338)
                                elif len(tmp338) == 1:
                                    tmp339 = tmp338[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp339)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 26695
                                    if len(subjects110) == 0:
                                        pass
                                        # State 26696
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x)**p)**q
                                if len(subjects110) == 0:
                                    break
                                tmp338.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp338))
                    if pattern_index == 2:
                        pass
                        # State 27284
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 27285
                            if len(subjects110) == 0:
                                pass
                                # State 27286
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(e + f*x)**p)**q
                        if len(subjects110) >= 1:
                            tmp342 = []
                            tmp342.append(subjects110.popleft())
                            while True:
                                if len(tmp342) > 1:
                                    tmp343 = create_operation_expression(associative1, tmp342)
                                elif len(tmp342) == 1:
                                    tmp343 = tmp342[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp343)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27285
                                    if len(subjects110) == 0:
                                        pass
                                        # State 27286
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(e + f*x)**p)**q
                                if len(subjects110) == 0:
                                    break
                                tmp342.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp342))
                    if pattern_index == 3:
                        pass
                        # State 27761
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 27762
                            if len(subjects110) == 0:
                                pass
                                # State 27763
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x)**p)**q
                        if len(subjects110) >= 1:
                            tmp346 = []
                            tmp346.append(subjects110.popleft())
                            while True:
                                if len(tmp346) > 1:
                                    tmp347 = create_operation_expression(associative1, tmp346)
                                elif len(tmp346) == 1:
                                    tmp347 = tmp346[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp347)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27762
                                    if len(subjects110) == 0:
                                        pass
                                        # State 27763
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x)**p)**q
                                if len(subjects110) == 0:
                                    break
                                tmp346.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp346))
                subjects110.appendleft(tmp330)
            if len(subjects110) >= 1 and isinstance(subjects110[0], Add):
                tmp349 = subjects110.popleft()
                associative1 = tmp349
                associative_type1 = type(tmp349)
                subjects350 = deque(tmp349._args)
                matcher = CommutativeMatcher26407.get()
                tmp351 = subjects350
                subjects350 = []
                for s in tmp351:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp351, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 26413
                        if len(subjects110) >= 1 and subjects110[0] == -1:
                            tmp352 = subjects110.popleft()
                            # State 26414
                            if len(subjects110) == 0:
                                pass
                                # State 26415
                                if len(subjects) == 0:
                                    pass
                                    # 2: 1/(e + f*x)
                            subjects110.appendleft(tmp352)
                    if pattern_index == 1:
                        pass
                        # State 49410
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49411
                            if len(subjects110) == 0:
                                pass
                                # State 49412
                                if len(subjects) == 0:
                                    pass
                                    # 7: (d + e*x**n)**p
                        if len(subjects110) >= 1:
                            tmp354 = []
                            tmp354.append(subjects110.popleft())
                            while True:
                                if len(tmp354) > 1:
                                    tmp355 = create_operation_expression(associative1, tmp354)
                                elif len(tmp354) == 1:
                                    tmp355 = tmp354[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp355)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49411
                                    if len(subjects110) == 0:
                                        pass
                                        # State 49412
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d + e*x**n)**p
                                if len(subjects110) == 0:
                                    break
                                tmp354.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp354))
                    if pattern_index == 2:
                        pass
                        # State 49937
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49938
                            if len(subjects110) == 0:
                                pass
                                # State 49939
                                if len(subjects) == 0:
                                    pass
                                    # 9: (d + e*x**n)**p
                        if len(subjects110) >= 1:
                            tmp358 = []
                            tmp358.append(subjects110.popleft())
                            while True:
                                if len(tmp358) > 1:
                                    tmp359 = create_operation_expression(associative1, tmp358)
                                elif len(tmp358) == 1:
                                    tmp359 = tmp358[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp359)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49938
                                    if len(subjects110) == 0:
                                        pass
                                        # State 49939
                                        if len(subjects) == 0:
                                            pass
                                            # 9: (d + e*x**n)**p
                                if len(subjects110) == 0:
                                    break
                                tmp358.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp358))
                    if pattern_index == 3:
                        pass
                        # State 50263
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 50264
                            if len(subjects110) == 0:
                                pass
                                # State 50265
                                if len(subjects) == 0:
                                    pass
                                    # 10: (d + e*x**2)**p
                        if len(subjects110) >= 1:
                            tmp362 = []
                            tmp362.append(subjects110.popleft())
                            while True:
                                if len(tmp362) > 1:
                                    tmp363 = create_operation_expression(associative1, tmp362)
                                elif len(tmp362) == 1:
                                    tmp363 = tmp362[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp363)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 50264
                                    if len(subjects110) == 0:
                                        pass
                                        # State 50265
                                        if len(subjects) == 0:
                                            pass
                                            # 10: (d + e*x**2)**p
                                if len(subjects110) == 0:
                                    break
                                tmp362.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp362))
                subjects110.appendleft(tmp349)
            subjects.appendleft(tmp109)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
