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

class CommutativeMatcher16968(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.3.0', 1, 1, None), Mul),
      (VariableWithCount('i2.3.0_1', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({0: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({1: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({3: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({4: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({5: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({6: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({7: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({8: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    10: (10, Multiset({9: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({10: 1}), [
      (VariableWithCount('i2.1.1.2.0', 1, 1, S(1)), Mul)
]),
    12: (12, Multiset({11: 1}), [
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
        if CommutativeMatcher16968._instance is None:
            CommutativeMatcher16968._instance = CommutativeMatcher16968()
        return CommutativeMatcher16968._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 16967
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.1.1.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 24029
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.1.1.2.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 24030
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.0', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 24031
                        if len(subjects) == 0:
                            pass
                            # 0: e + f*x
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp5 = subjects.popleft()
                associative1 = tmp5
                associative_type1 = type(tmp5)
                subjects6 = deque(tmp5._args)
                matcher = CommutativeMatcher24033.get()
                tmp7 = subjects6
                subjects6 = []
                for s in tmp7:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp7, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 24034
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
            # State 25292
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.1.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 25293
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.1.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 25294
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i2.1.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 25295
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25296
                            if len(subjects) >= 1:
                                tmp13 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.0', tmp13)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25297
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
                                    # State 27146
                                    if len(subjects) == 0:
                                        pass
                                        # 4: (d*(e + f*x)**p)**q
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
                                    # State 28213
                                    if len(subjects) == 0:
                                        pass
                                        # 6: (d*(e + f*x)**p)**q
                                subjects.appendleft(tmp17)
                        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                            tmp19 = subjects.popleft()
                            associative1 = tmp19
                            associative_type1 = type(tmp19)
                            subjects20 = deque(tmp19._args)
                            matcher = CommutativeMatcher25299.get()
                            tmp21 = subjects20
                            subjects20 = []
                            for s in tmp21:
                                matcher.add_subject(s)
                            for pattern_index, subst5 in matcher.match(tmp21, subst4):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 25300
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (d*(e + f*x)**p)**q
                                if pattern_index == 1:
                                    pass
                                    # State 27147
                                    if len(subjects) == 0:
                                        pass
                                        # 4: (d*(e + f*x)**p)**q
                                if pattern_index == 2:
                                    pass
                                    # State 28214
                                    if len(subjects) == 0:
                                        pass
                                        # 6: (d*(e + f*x)**p)**q
                            subjects.appendleft(tmp19)
                    if len(subjects) >= 1 and isinstance(subjects[0], Add):
                        tmp22 = subjects.popleft()
                        associative1 = tmp22
                        associative_type1 = type(tmp22)
                        subjects23 = deque(tmp22._args)
                        matcher = CommutativeMatcher25302.get()
                        tmp24 = subjects23
                        subjects23 = []
                        for s in tmp24:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp24, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 25308
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d*(e + f*x)**p)**q
                            if pattern_index == 1:
                                pass
                                # State 27150
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(e + f*x)**p)**q
                            if pattern_index == 2:
                                pass
                                # State 27432
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x)**p)**q
                            if pattern_index == 3:
                                pass
                                # State 28217
                                if len(subjects) == 0:
                                    pass
                                    # 6: (d*(e + f*x)**p)**q
                        subjects.appendleft(tmp22)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp25 = subjects.popleft()
                    subjects26 = deque(tmp25._args)
                    # State 25309
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 25310
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25311
                            if len(subjects26) >= 1:
                                tmp29 = subjects26.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.0', tmp29)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25312
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 25313
                                        if len(subjects26) == 0:
                                            pass
                                            # State 25314
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
                                            # State 25313
                                            if len(subjects26) == 0:
                                                pass
                                                # State 25314
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
                                    # State 27151
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27152
                                        if len(subjects26) == 0:
                                            pass
                                            # State 27153
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (d*(e + f*x)**p)**q
                                    if len(subjects26) >= 1:
                                        tmp37 = subjects26.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2.2', tmp37)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27152
                                            if len(subjects26) == 0:
                                                pass
                                                # State 27153
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(e + f*x)**p)**q
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
                                    # State 28218
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 28219
                                        if len(subjects26) == 0:
                                            pass
                                            # State 28220
                                            if len(subjects) == 0:
                                                pass
                                                # 6: (d*(e + f*x)**p)**q
                                    if len(subjects26) >= 1:
                                        tmp42 = subjects26.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2.2', tmp42)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28219
                                            if len(subjects26) == 0:
                                                pass
                                                # State 28220
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x)**p)**q
                                        subjects26.appendleft(tmp42)
                                subjects26.appendleft(tmp39)
                        if len(subjects26) >= 1 and isinstance(subjects26[0], Mul):
                            tmp44 = subjects26.popleft()
                            associative1 = tmp44
                            associative_type1 = type(tmp44)
                            subjects45 = deque(tmp44._args)
                            matcher = CommutativeMatcher25316.get()
                            tmp46 = subjects45
                            subjects45 = []
                            for s in tmp46:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp46, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 25317
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 25318
                                        if len(subjects26) == 0:
                                            pass
                                            # State 25319
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
                                                # State 25318
                                                if len(subjects26) == 0:
                                                    pass
                                                    # State 25319
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*(e + f*x)**p)**q
                                            if len(subjects26) == 0:
                                                break
                                            tmp48.append(subjects26.popleft())
                                        subjects26.extendleft(reversed(tmp48))
                                if pattern_index == 1:
                                    pass
                                    # State 27154
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27155
                                        if len(subjects26) == 0:
                                            pass
                                            # State 27156
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (d*(e + f*x)**p)**q
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
                                                # State 27155
                                                if len(subjects26) == 0:
                                                    pass
                                                    # State 27156
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (d*(e + f*x)**p)**q
                                            if len(subjects26) == 0:
                                                break
                                            tmp52.append(subjects26.popleft())
                                        subjects26.extendleft(reversed(tmp52))
                                if pattern_index == 2:
                                    pass
                                    # State 28221
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 28222
                                        if len(subjects26) == 0:
                                            pass
                                            # State 28223
                                            if len(subjects) == 0:
                                                pass
                                                # 6: (d*(e + f*x)**p)**q
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
                                                # State 28222
                                                if len(subjects26) == 0:
                                                    pass
                                                    # State 28223
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(e + f*x)**p)**q
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
                        matcher = CommutativeMatcher25321.get()
                        tmp61 = subjects60
                        subjects60 = []
                        for s in tmp61:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp61, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 25327
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25328
                                    if len(subjects26) == 0:
                                        pass
                                        # State 25329
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
                                            # State 25328
                                            if len(subjects26) == 0:
                                                pass
                                                # State 25329
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*(e + f*x)**p)**q
                                        if len(subjects26) == 0:
                                            break
                                        tmp63.append(subjects26.popleft())
                                    subjects26.extendleft(reversed(tmp63))
                            if pattern_index == 1:
                                pass
                                # State 27159
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27160
                                    if len(subjects26) == 0:
                                        pass
                                        # State 27161
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(e + f*x)**p)**q
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
                                            # State 27160
                                            if len(subjects26) == 0:
                                                pass
                                                # State 27161
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(e + f*x)**p)**q
                                        if len(subjects26) == 0:
                                            break
                                        tmp67.append(subjects26.popleft())
                                    subjects26.extendleft(reversed(tmp67))
                            if pattern_index == 2:
                                pass
                                # State 27433
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27434
                                    if len(subjects26) == 0:
                                        pass
                                        # State 27435
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x)**p)**q
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
                                            # State 27434
                                            if len(subjects26) == 0:
                                                pass
                                                # State 27435
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x)**p)**q
                                        if len(subjects26) == 0:
                                            break
                                        tmp71.append(subjects26.popleft())
                                    subjects26.extendleft(reversed(tmp71))
                            if pattern_index == 3:
                                pass
                                # State 28226
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28227
                                    if len(subjects26) == 0:
                                        pass
                                        # State 28228
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x)**p)**q
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
                                            # State 28227
                                            if len(subjects26) == 0:
                                                pass
                                                # State 28228
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x)**p)**q
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
                    # State 40440
                    if len(subjects) == 0:
                        pass
                        # 7: x**n
                subjects.appendleft(tmp78)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.1.1.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 49703
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.1.1.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 49704
                    if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                        tmp82 = subjects.popleft()
                        subjects83 = deque(tmp82._args)
                        # State 49705
                        if len(subjects83) >= 1:
                            tmp84 = subjects83.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp84)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49706
                                if len(subjects83) >= 1:
                                    tmp86 = subjects83.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.1.2', tmp86)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49707
                                        if len(subjects83) == 0:
                                            pass
                                            # State 49708
                                            if len(subjects) == 0:
                                                pass
                                                # 8: (d + e*x**n)**p
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
                                # State 50145
                                if len(subjects83) >= 1:
                                    tmp90 = subjects83.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.1.2', tmp90)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50146
                                        if len(subjects83) == 0:
                                            pass
                                            # State 50147
                                            if len(subjects) == 0:
                                                pass
                                                # 10: (d + e*x**n)**p
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
                                # State 50471
                                if len(subjects83) >= 1 and subjects83[0] == 2:
                                    tmp94 = subjects83.popleft()
                                    # State 50472
                                    if len(subjects83) == 0:
                                        pass
                                        # State 50473
                                        if len(subjects) == 0:
                                            pass
                                            # 11: (d + e*x**2)**p
                                    subjects83.appendleft(tmp94)
                            subjects83.appendleft(tmp92)
                        subjects.appendleft(tmp82)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp95 = subjects.popleft()
                    associative1 = tmp95
                    associative_type1 = type(tmp95)
                    subjects96 = deque(tmp95._args)
                    matcher = CommutativeMatcher49710.get()
                    tmp97 = subjects96
                    subjects96 = []
                    for s in tmp97:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp97, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 49715
                            if len(subjects) == 0:
                                pass
                                # 8: (d + e*x**n)**p
                        if pattern_index == 1:
                            pass
                            # State 50151
                            if len(subjects) == 0:
                                pass
                                # 10: (d + e*x**n)**p
                        if pattern_index == 2:
                            pass
                            # State 50477
                            if len(subjects) == 0:
                                pass
                                # 11: (d + e*x**2)**p
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
                    # State 49809
                    if len(subjects) == 0:
                        pass
                        # 9: v**p
                subjects.appendleft(tmp98)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp100 = subjects.popleft()
                associative1 = tmp100
                associative_type1 = type(tmp100)
                subjects101 = deque(tmp100._args)
                matcher = CommutativeMatcher25331.get()
                tmp102 = subjects101
                subjects101 = []
                for s in tmp102:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp102, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 25368
                        if len(subjects) == 0:
                            pass
                            # 1: (d*(e + f*x)**p)**q
                    if pattern_index == 1:
                        pass
                        # State 27178
                        if len(subjects) == 0:
                            pass
                            # 4: (d*(e + f*x)**p)**q
                    if pattern_index == 2:
                        pass
                        # State 27440
                        if len(subjects) == 0:
                            pass
                            # 5: (d*(e + f*x)**p)**q
                    if pattern_index == 3:
                        pass
                        # State 28245
                        if len(subjects) == 0:
                            pass
                            # 6: (d*(e + f*x)**p)**q
                subjects.appendleft(tmp100)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp103 = subjects.popleft()
                associative1 = tmp103
                associative_type1 = type(tmp103)
                subjects104 = deque(tmp103._args)
                matcher = CommutativeMatcher49717.get()
                tmp105 = subjects104
                subjects104 = []
                for s in tmp105:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp105, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 49730
                        if len(subjects) == 0:
                            pass
                            # 8: (d + e*x**n)**p
                    if pattern_index == 1:
                        pass
                        # State 50159
                        if len(subjects) == 0:
                            pass
                            # 10: (d + e*x**n)**p
                    if pattern_index == 2:
                        pass
                        # State 50485
                        if len(subjects) == 0:
                            pass
                            # 11: (d + e*x**2)**p
                subjects.appendleft(tmp103)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp106 = subjects.popleft()
            associative1 = tmp106
            associative_type1 = type(tmp106)
            subjects107 = deque(tmp106._args)
            matcher = CommutativeMatcher24036.get()
            tmp108 = subjects107
            subjects107 = []
            for s in tmp108:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp108, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 24042
                    if len(subjects) == 0:
                        pass
                        # 0: e + f*x
            subjects.appendleft(tmp106)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp109 = subjects.popleft()
            subjects110 = deque(tmp109._args)
            # State 25369
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.1.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 25370
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 25371
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 25372
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25373
                            if len(subjects110) >= 1:
                                tmp115 = subjects110.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.0', tmp115)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25374
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 25375
                                        if len(subjects110) == 0:
                                            pass
                                            # State 25376
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
                                            # State 25375
                                            if len(subjects110) == 0:
                                                pass
                                                # State 25376
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
                                    # State 27179
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27180
                                        if len(subjects110) == 0:
                                            pass
                                            # State 27181
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (d*(e + f*x)**p)**q
                                    if len(subjects110) >= 1:
                                        tmp123 = subjects110.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2', tmp123)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27180
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27181
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(e + f*x)**p)**q
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
                                    # State 28246
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 28247
                                        if len(subjects110) == 0:
                                            pass
                                            # State 28248
                                            if len(subjects) == 0:
                                                pass
                                                # 6: (d*(e + f*x)**p)**q
                                    if len(subjects110) >= 1:
                                        tmp128 = subjects110.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.1.1.2.2', tmp128)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28247
                                            if len(subjects110) == 0:
                                                pass
                                                # State 28248
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x)**p)**q
                                        subjects110.appendleft(tmp128)
                                subjects110.appendleft(tmp125)
                        if len(subjects110) >= 1 and isinstance(subjects110[0], Mul):
                            tmp130 = subjects110.popleft()
                            associative1 = tmp130
                            associative_type1 = type(tmp130)
                            subjects131 = deque(tmp130._args)
                            matcher = CommutativeMatcher25378.get()
                            tmp132 = subjects131
                            subjects131 = []
                            for s in tmp132:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp132, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 25379
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 25380
                                        if len(subjects110) == 0:
                                            pass
                                            # State 25381
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
                                                # State 25380
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 25381
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*(e + f*x)**p)**q
                                            if len(subjects110) == 0:
                                                break
                                            tmp134.append(subjects110.popleft())
                                        subjects110.extendleft(reversed(tmp134))
                                if pattern_index == 1:
                                    pass
                                    # State 27182
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27183
                                        if len(subjects110) == 0:
                                            pass
                                            # State 27184
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (d*(e + f*x)**p)**q
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
                                                # State 27183
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27184
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (d*(e + f*x)**p)**q
                                            if len(subjects110) == 0:
                                                break
                                            tmp138.append(subjects110.popleft())
                                        subjects110.extendleft(reversed(tmp138))
                                if pattern_index == 2:
                                    pass
                                    # State 28249
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 28250
                                        if len(subjects110) == 0:
                                            pass
                                            # State 28251
                                            if len(subjects) == 0:
                                                pass
                                                # 6: (d*(e + f*x)**p)**q
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
                                                # State 28250
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 28251
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(e + f*x)**p)**q
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
                        matcher = CommutativeMatcher25383.get()
                        tmp147 = subjects146
                        subjects146 = []
                        for s in tmp147:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp147, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 25389
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25390
                                    if len(subjects110) == 0:
                                        pass
                                        # State 25391
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
                                            # State 25390
                                            if len(subjects110) == 0:
                                                pass
                                                # State 25391
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*(e + f*x)**p)**q
                                        if len(subjects110) == 0:
                                            break
                                        tmp149.append(subjects110.popleft())
                                    subjects110.extendleft(reversed(tmp149))
                            if pattern_index == 1:
                                pass
                                # State 27187
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27188
                                    if len(subjects110) == 0:
                                        pass
                                        # State 27189
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(e + f*x)**p)**q
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
                                            # State 27188
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27189
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(e + f*x)**p)**q
                                        if len(subjects110) == 0:
                                            break
                                        tmp153.append(subjects110.popleft())
                                    subjects110.extendleft(reversed(tmp153))
                            if pattern_index == 2:
                                pass
                                # State 27441
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27442
                                    if len(subjects110) == 0:
                                        pass
                                        # State 27443
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x)**p)**q
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
                                            # State 27442
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27443
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x)**p)**q
                                        if len(subjects110) == 0:
                                            break
                                        tmp157.append(subjects110.popleft())
                                    subjects110.extendleft(reversed(tmp157))
                            if pattern_index == 3:
                                pass
                                # State 28254
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28255
                                    if len(subjects110) == 0:
                                        pass
                                        # State 28256
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x)**p)**q
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
                                            # State 28255
                                            if len(subjects110) == 0:
                                                pass
                                                # State 28256
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x)**p)**q
                                        if len(subjects110) == 0:
                                            break
                                        tmp161.append(subjects110.popleft())
                                    subjects110.extendleft(reversed(tmp161))
                        subjects110.appendleft(tmp145)
                if len(subjects110) >= 1 and isinstance(subjects110[0], Pow):
                    tmp164 = subjects110.popleft()
                    subjects165 = deque(tmp164._args)
                    # State 25392
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 25393
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.1.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25394
                            if len(subjects165) >= 1:
                                tmp168 = subjects165.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.0', tmp168)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25395
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 25396
                                        if len(subjects165) == 0:
                                            pass
                                            # State 25397
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 25398
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 25399
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
                                                    # State 25398
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 25399
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
                                            # State 25396
                                            if len(subjects165) == 0:
                                                pass
                                                # State 25397
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 25398
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 25399
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
                                                        # State 25398
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 25399
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
                                    # State 27190
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27191
                                        if len(subjects165) == 0:
                                            pass
                                            # State 27192
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27193
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27194
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (d*(e + f*x)**p)**q
                                            if len(subjects110) >= 1:
                                                tmp183 = subjects110.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', tmp183)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27193
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27194
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (d*(e + f*x)**p)**q
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
                                            # State 27191
                                            if len(subjects165) == 0:
                                                pass
                                                # State 27192
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27193
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27194
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (d*(e + f*x)**p)**q
                                                if len(subjects110) >= 1:
                                                    tmp188 = subjects110.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp188)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27193
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 27194
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (d*(e + f*x)**p)**q
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
                                    # State 28257
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 28258
                                        if len(subjects165) == 0:
                                            pass
                                            # State 28259
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 28260
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 28261
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(e + f*x)**p)**q
                                            if len(subjects110) >= 1:
                                                tmp194 = subjects110.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', tmp194)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28260
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 28261
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: (d*(e + f*x)**p)**q
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
                                            # State 28258
                                            if len(subjects165) == 0:
                                                pass
                                                # State 28259
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28260
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 28261
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: (d*(e + f*x)**p)**q
                                                if len(subjects110) >= 1:
                                                    tmp199 = subjects110.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.1.1.2.2', tmp199)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 28260
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 28261
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: (d*(e + f*x)**p)**q
                                                    subjects110.appendleft(tmp199)
                                        subjects165.appendleft(tmp196)
                                subjects165.appendleft(tmp190)
                        if len(subjects165) >= 1 and isinstance(subjects165[0], Mul):
                            tmp201 = subjects165.popleft()
                            associative1 = tmp201
                            associative_type1 = type(tmp201)
                            subjects202 = deque(tmp201._args)
                            matcher = CommutativeMatcher25401.get()
                            tmp203 = subjects202
                            subjects202 = []
                            for s in tmp203:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp203, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 25402
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 25403
                                        if len(subjects165) == 0:
                                            pass
                                            # State 25404
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 25405
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 25406
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
                                                    # State 25405
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 25406
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
                                                # State 25403
                                                if len(subjects165) == 0:
                                                    pass
                                                    # State 25404
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 25405
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 25406
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
                                                            # State 25405
                                                            if len(subjects110) == 0:
                                                                pass
                                                                # State 25406
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
                                    # State 27195
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27196
                                        if len(subjects165) == 0:
                                            pass
                                            # State 27197
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27198
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27199
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (d*(e + f*x)**p)**q
                                            if len(subjects110) >= 1:
                                                tmp216 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp216)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27198
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27199
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (d*(e + f*x)**p)**q
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
                                                # State 27196
                                                if len(subjects165) == 0:
                                                    pass
                                                    # State 27197
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27198
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 27199
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (d*(e + f*x)**p)**q
                                                    if len(subjects110) >= 1:
                                                        tmp222 = subjects110.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', tmp222)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 27198
                                                            if len(subjects110) == 0:
                                                                pass
                                                                # State 27199
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 4: (d*(e + f*x)**p)**q
                                                        subjects110.appendleft(tmp222)
                                            if len(subjects165) == 0:
                                                break
                                            tmp218.append(subjects165.popleft())
                                        subjects165.extendleft(reversed(tmp218))
                                if pattern_index == 2:
                                    pass
                                    # State 28262
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 28263
                                        if len(subjects165) == 0:
                                            pass
                                            # State 28264
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 28265
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 28266
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(e + f*x)**p)**q
                                            if len(subjects110) >= 1:
                                                tmp226 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp226)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28265
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 28266
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: (d*(e + f*x)**p)**q
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
                                                # State 28263
                                                if len(subjects165) == 0:
                                                    pass
                                                    # State 28264
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.1.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 28265
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 28266
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: (d*(e + f*x)**p)**q
                                                    if len(subjects110) >= 1:
                                                        tmp232 = subjects110.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.1.1.2.2', tmp232)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 28265
                                                            if len(subjects110) == 0:
                                                                pass
                                                                # State 28266
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 6: (d*(e + f*x)**p)**q
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
                        matcher = CommutativeMatcher25408.get()
                        tmp236 = subjects235
                        subjects235 = []
                        for s in tmp236:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp236, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 25414
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25415
                                    if len(subjects165) == 0:
                                        pass
                                        # State 25416
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25417
                                            if len(subjects110) == 0:
                                                pass
                                                # State 25418
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
                                                # State 25417
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 25418
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
                                            # State 25415
                                            if len(subjects165) == 0:
                                                pass
                                                # State 25416
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 25417
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 25418
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
                                                        # State 25417
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 25418
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
                                # State 27202
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27203
                                    if len(subjects165) == 0:
                                        pass
                                        # State 27204
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27205
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27206
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(e + f*x)**p)**q
                                        if len(subjects110) >= 1:
                                            tmp249 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp249)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27205
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27206
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (d*(e + f*x)**p)**q
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
                                            # State 27203
                                            if len(subjects165) == 0:
                                                pass
                                                # State 27204
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27205
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27206
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (d*(e + f*x)**p)**q
                                                if len(subjects110) >= 1:
                                                    tmp255 = subjects110.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.2.2', tmp255)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27205
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 27206
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (d*(e + f*x)**p)**q
                                                    subjects110.appendleft(tmp255)
                                        if len(subjects165) == 0:
                                            break
                                        tmp251.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp251))
                            if pattern_index == 2:
                                pass
                                # State 27444
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27445
                                    if len(subjects165) == 0:
                                        pass
                                        # State 27446
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27447
                                            if len(subjects110) == 0:
                                                pass
                                                # State 27448
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x)**p)**q
                                        if len(subjects110) >= 1:
                                            tmp259 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp259)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 27447
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 27448
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x)**p)**q
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
                                            # State 27445
                                            if len(subjects165) == 0:
                                                pass
                                                # State 27446
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 27447
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 27448
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x)**p)**q
                                                if len(subjects110) >= 1:
                                                    tmp265 = subjects110.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.2.2', tmp265)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 27447
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 27448
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x)**p)**q
                                                    subjects110.appendleft(tmp265)
                                        if len(subjects165) == 0:
                                            break
                                        tmp261.append(subjects165.popleft())
                                    subjects165.extendleft(reversed(tmp261))
                            if pattern_index == 3:
                                pass
                                # State 28269
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.1.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28270
                                    if len(subjects165) == 0:
                                        pass
                                        # State 28271
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 28272
                                            if len(subjects110) == 0:
                                                pass
                                                # State 28273
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x)**p)**q
                                        if len(subjects110) >= 1:
                                            tmp269 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp269)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 28272
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 28273
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(e + f*x)**p)**q
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
                                            # State 28270
                                            if len(subjects165) == 0:
                                                pass
                                                # State 28271
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.1.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 28272
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 28273
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: (d*(e + f*x)**p)**q
                                                if len(subjects110) >= 1:
                                                    tmp275 = subjects110.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.1.1.2.2', tmp275)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 28272
                                                        if len(subjects110) == 0:
                                                            pass
                                                            # State 28273
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: (d*(e + f*x)**p)**q
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
                # State 25969
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.1.1.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 25970
                    if len(subjects110) >= 1:
                        tmp279 = subjects110.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp279)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25971
                            if len(subjects110) >= 1 and subjects110[0] == -1:
                                tmp281 = subjects110.popleft()
                                # State 25972
                                if len(subjects110) == 0:
                                    pass
                                    # State 25973
                                    if len(subjects) == 0:
                                        pass
                                        # 2: 1/(e + f*x)
                                subjects110.appendleft(tmp281)
                        subjects110.appendleft(tmp279)
                    if len(subjects110) >= 1:
                        tmp282 = subjects110.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp282)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 26505
                            if len(subjects110) >= 1 and subjects110[0] == -1:
                                tmp284 = subjects110.popleft()
                                # State 26506
                                if len(subjects110) == 0:
                                    pass
                                    # State 26507
                                    if len(subjects) == 0:
                                        pass
                                        # 3: 1/(e + f*x)
                                subjects110.appendleft(tmp284)
                        subjects110.appendleft(tmp282)
                    if len(subjects110) >= 1 and isinstance(subjects110[0], Pow):
                        tmp285 = subjects110.popleft()
                        subjects286 = deque(tmp285._args)
                        # State 49731
                        if len(subjects286) >= 1:
                            tmp287 = subjects286.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.0', tmp287)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49732
                                if len(subjects286) >= 1:
                                    tmp289 = subjects286.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.1.2', tmp289)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 49733
                                        if len(subjects286) == 0:
                                            pass
                                            # State 49734
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 49735
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 49736
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 8: (d + e*x**n)**p
                                            if len(subjects110) >= 1:
                                                tmp292 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp292)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 49735
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 49736
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 8: (d + e*x**n)**p
                                                subjects110.appendleft(tmp292)
                                    subjects286.appendleft(tmp289)
                            subjects286.appendleft(tmp287)
                        if len(subjects286) >= 1:
                            tmp294 = subjects286.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.0', tmp294)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 50160
                                if len(subjects286) >= 1:
                                    tmp296 = subjects286.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.1.1.2.2.1.2', tmp296)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50161
                                        if len(subjects286) == 0:
                                            pass
                                            # State 50162
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.1.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 50163
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 50164
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 10: (d + e*x**n)**p
                                            if len(subjects110) >= 1:
                                                tmp299 = subjects110.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.1.1.2.2', tmp299)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 50163
                                                    if len(subjects110) == 0:
                                                        pass
                                                        # State 50164
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 10: (d + e*x**n)**p
                                                subjects110.appendleft(tmp299)
                                    subjects286.appendleft(tmp296)
                            subjects286.appendleft(tmp294)
                        if len(subjects286) >= 1:
                            tmp301 = subjects286.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.1', tmp301)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 50486
                                if len(subjects286) >= 1 and subjects286[0] == 2:
                                    tmp303 = subjects286.popleft()
                                    # State 50487
                                    if len(subjects286) == 0:
                                        pass
                                        # State 50488
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.1.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 50489
                                            if len(subjects110) == 0:
                                                pass
                                                # State 50490
                                                if len(subjects) == 0:
                                                    pass
                                                    # 11: (d + e*x**2)**p
                                        if len(subjects110) >= 1:
                                            tmp305 = subjects110.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.1.1.2.2', tmp305)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 50489
                                                if len(subjects110) == 0:
                                                    pass
                                                    # State 50490
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 11: (d + e*x**2)**p
                                            subjects110.appendleft(tmp305)
                                    subjects286.appendleft(tmp303)
                            subjects286.appendleft(tmp301)
                        subjects110.appendleft(tmp285)
                if len(subjects110) >= 1 and isinstance(subjects110[0], Mul):
                    tmp307 = subjects110.popleft()
                    associative1 = tmp307
                    associative_type1 = type(tmp307)
                    subjects308 = deque(tmp307._args)
                    matcher = CommutativeMatcher25975.get()
                    tmp309 = subjects308
                    subjects308 = []
                    for s in tmp309:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp309, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 25976
                            if len(subjects110) >= 1 and subjects110[0] == -1:
                                tmp310 = subjects110.popleft()
                                # State 25977
                                if len(subjects110) == 0:
                                    pass
                                    # State 25978
                                    if len(subjects) == 0:
                                        pass
                                        # 2: 1/(e + f*x)
                                subjects110.appendleft(tmp310)
                        if pattern_index == 1:
                            pass
                            # State 26508
                            if len(subjects110) >= 1 and subjects110[0] == -1:
                                tmp311 = subjects110.popleft()
                                # State 26509
                                if len(subjects110) == 0:
                                    pass
                                    # State 26510
                                    if len(subjects) == 0:
                                        pass
                                        # 3: 1/(e + f*x)
                                subjects110.appendleft(tmp311)
                        if pattern_index == 2:
                            pass
                            # State 49741
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49742
                                if len(subjects110) == 0:
                                    pass
                                    # State 49743
                                    if len(subjects) == 0:
                                        pass
                                        # 8: (d + e*x**n)**p
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
                                        # State 49742
                                        if len(subjects110) == 0:
                                            pass
                                            # State 49743
                                            if len(subjects) == 0:
                                                pass
                                                # 8: (d + e*x**n)**p
                                    if len(subjects110) == 0:
                                        break
                                    tmp313.append(subjects110.popleft())
                                subjects110.extendleft(reversed(tmp313))
                        if pattern_index == 3:
                            pass
                            # State 50168
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 50169
                                if len(subjects110) == 0:
                                    pass
                                    # State 50170
                                    if len(subjects) == 0:
                                        pass
                                        # 10: (d + e*x**n)**p
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
                                        # State 50169
                                        if len(subjects110) == 0:
                                            pass
                                            # State 50170
                                            if len(subjects) == 0:
                                                pass
                                                # 10: (d + e*x**n)**p
                                    if len(subjects110) == 0:
                                        break
                                    tmp317.append(subjects110.popleft())
                                subjects110.extendleft(reversed(tmp317))
                        if pattern_index == 4:
                            pass
                            # State 50494
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 50495
                                if len(subjects110) == 0:
                                    pass
                                    # State 50496
                                    if len(subjects) == 0:
                                        pass
                                        # 11: (d + e*x**2)**p
                            if len(subjects110) >= 1:
                                tmp321 = []
                                tmp321.append(subjects110.popleft())
                                while True:
                                    if len(tmp321) > 1:
                                        tmp322 = create_operation_expression(associative1, tmp321)
                                    elif len(tmp321) == 1:
                                        tmp322 = tmp321[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.1.1.2.2', tmp322)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 50495
                                        if len(subjects110) == 0:
                                            pass
                                            # State 50496
                                            if len(subjects) == 0:
                                                pass
                                                # 11: (d + e*x**2)**p
                                    if len(subjects110) == 0:
                                        break
                                    tmp321.append(subjects110.popleft())
                                subjects110.extendleft(reversed(tmp321))
                    subjects110.appendleft(tmp307)
            if len(subjects110) >= 1:
                tmp324 = subjects110.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp324)
                except ValueError:
                    pass
                else:
                    pass
                    # State 40441
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 40442
                        if len(subjects110) == 0:
                            pass
                            # State 40443
                            if len(subjects) == 0:
                                pass
                                # 7: x**n
                    if len(subjects110) >= 1:
                        tmp327 = subjects110.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', tmp327)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 40442
                            if len(subjects110) == 0:
                                pass
                                # State 40443
                                if len(subjects) == 0:
                                    pass
                                    # 7: x**n
                        subjects110.appendleft(tmp327)
                subjects110.appendleft(tmp324)
            if len(subjects110) >= 1:
                tmp329 = subjects110.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.1.1.2.1', tmp329)
                except ValueError:
                    pass
                else:
                    pass
                    # State 49810
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 49811
                        if len(subjects110) == 0:
                            pass
                            # State 49812
                            if len(subjects) == 0:
                                pass
                                # 9: v**p
                    if len(subjects110) >= 1:
                        tmp332 = subjects110.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', tmp332)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49811
                            if len(subjects110) == 0:
                                pass
                                # State 49812
                                if len(subjects) == 0:
                                    pass
                                    # 9: v**p
                        subjects110.appendleft(tmp332)
                subjects110.appendleft(tmp329)
            if len(subjects110) >= 1 and isinstance(subjects110[0], Mul):
                tmp334 = subjects110.popleft()
                associative1 = tmp334
                associative_type1 = type(tmp334)
                subjects335 = deque(tmp334._args)
                matcher = CommutativeMatcher25420.get()
                tmp336 = subjects335
                subjects335 = []
                for s in tmp336:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp336, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 25457
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25458
                            if len(subjects110) == 0:
                                pass
                                # State 25459
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d*(e + f*x)**p)**q
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
                                    # State 25458
                                    if len(subjects110) == 0:
                                        pass
                                        # State 25459
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*(e + f*x)**p)**q
                                if len(subjects110) == 0:
                                    break
                                tmp338.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp338))
                    if pattern_index == 1:
                        pass
                        # State 27223
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 27224
                            if len(subjects110) == 0:
                                pass
                                # State 27225
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
                                    # State 27224
                                    if len(subjects110) == 0:
                                        pass
                                        # State 27225
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(e + f*x)**p)**q
                                if len(subjects110) == 0:
                                    break
                                tmp342.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp342))
                    if pattern_index == 2:
                        pass
                        # State 27453
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 27454
                            if len(subjects110) == 0:
                                pass
                                # State 27455
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
                                    # State 27454
                                    if len(subjects110) == 0:
                                        pass
                                        # State 27455
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x)**p)**q
                                if len(subjects110) == 0:
                                    break
                                tmp346.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp346))
                    if pattern_index == 3:
                        pass
                        # State 28290
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 28291
                            if len(subjects110) == 0:
                                pass
                                # State 28292
                                if len(subjects) == 0:
                                    pass
                                    # 6: (d*(e + f*x)**p)**q
                        if len(subjects110) >= 1:
                            tmp350 = []
                            tmp350.append(subjects110.popleft())
                            while True:
                                if len(tmp350) > 1:
                                    tmp351 = create_operation_expression(associative1, tmp350)
                                elif len(tmp350) == 1:
                                    tmp351 = tmp350[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp351)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 28291
                                    if len(subjects110) == 0:
                                        pass
                                        # State 28292
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x)**p)**q
                                if len(subjects110) == 0:
                                    break
                                tmp350.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp350))
                subjects110.appendleft(tmp334)
            if len(subjects110) >= 1 and isinstance(subjects110[0], Add):
                tmp353 = subjects110.popleft()
                associative1 = tmp353
                associative_type1 = type(tmp353)
                subjects354 = deque(tmp353._args)
                matcher = CommutativeMatcher25980.get()
                tmp355 = subjects354
                subjects354 = []
                for s in tmp355:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp355, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 25986
                        if len(subjects110) >= 1 and subjects110[0] == -1:
                            tmp356 = subjects110.popleft()
                            # State 25987
                            if len(subjects110) == 0:
                                pass
                                # State 25988
                                if len(subjects) == 0:
                                    pass
                                    # 2: 1/(e + f*x)
                            subjects110.appendleft(tmp356)
                    if pattern_index == 1:
                        pass
                        # State 26513
                        if len(subjects110) >= 1 and subjects110[0] == -1:
                            tmp357 = subjects110.popleft()
                            # State 26514
                            if len(subjects110) == 0:
                                pass
                                # State 26515
                                if len(subjects) == 0:
                                    pass
                                    # 3: 1/(e + f*x)
                            subjects110.appendleft(tmp357)
                    if pattern_index == 2:
                        pass
                        # State 49753
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 49754
                            if len(subjects110) == 0:
                                pass
                                # State 49755
                                if len(subjects) == 0:
                                    pass
                                    # 8: (d + e*x**n)**p
                        if len(subjects110) >= 1:
                            tmp359 = []
                            tmp359.append(subjects110.popleft())
                            while True:
                                if len(tmp359) > 1:
                                    tmp360 = create_operation_expression(associative1, tmp359)
                                elif len(tmp359) == 1:
                                    tmp360 = tmp359[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp360)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 49754
                                    if len(subjects110) == 0:
                                        pass
                                        # State 49755
                                        if len(subjects) == 0:
                                            pass
                                            # 8: (d + e*x**n)**p
                                if len(subjects110) == 0:
                                    break
                                tmp359.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp359))
                    if pattern_index == 3:
                        pass
                        # State 50178
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 50179
                            if len(subjects110) == 0:
                                pass
                                # State 50180
                                if len(subjects) == 0:
                                    pass
                                    # 10: (d + e*x**n)**p
                        if len(subjects110) >= 1:
                            tmp363 = []
                            tmp363.append(subjects110.popleft())
                            while True:
                                if len(tmp363) > 1:
                                    tmp364 = create_operation_expression(associative1, tmp363)
                                elif len(tmp363) == 1:
                                    tmp364 = tmp363[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp364)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 50179
                                    if len(subjects110) == 0:
                                        pass
                                        # State 50180
                                        if len(subjects) == 0:
                                            pass
                                            # 10: (d + e*x**n)**p
                                if len(subjects110) == 0:
                                    break
                                tmp363.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp363))
                    if pattern_index == 4:
                        pass
                        # State 50504
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.1.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 50505
                            if len(subjects110) == 0:
                                pass
                                # State 50506
                                if len(subjects) == 0:
                                    pass
                                    # 11: (d + e*x**2)**p
                        if len(subjects110) >= 1:
                            tmp367 = []
                            tmp367.append(subjects110.popleft())
                            while True:
                                if len(tmp367) > 1:
                                    tmp368 = create_operation_expression(associative1, tmp367)
                                elif len(tmp367) == 1:
                                    tmp368 = tmp367[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.1.1.2.2', tmp368)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 50505
                                    if len(subjects110) == 0:
                                        pass
                                        # State 50506
                                        if len(subjects) == 0:
                                            pass
                                            # 11: (d + e*x**2)**p
                                if len(subjects110) == 0:
                                    break
                                tmp367.append(subjects110.popleft())
                            subjects110.extendleft(reversed(tmp367))
                subjects110.appendleft(tmp353)
            subjects.appendleft(tmp109)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
