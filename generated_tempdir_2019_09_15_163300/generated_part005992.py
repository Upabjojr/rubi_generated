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


class CommutativeMatcher17288(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1, 8: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({9: 1, 10: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    10: (10, Multiset({12: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher17288._instance is None:
            CommutativeMatcher17288._instance = CommutativeMatcher17288()
        return CommutativeMatcher17288._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 17287
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 17289
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 17290
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 17291
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17292
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 17293
                                if len(subjects3) >= 1:
                                    tmp8 = subjects3.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.3.1.2', tmp8)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 17294
                                        if len(subjects3) == 0:
                                            pass
                                            # State 17295
                                            if len(subjects) == 0:
                                                pass
                                                # 0: b*(x*d + c)**n
                                                yield 0, subst5
                                    subjects3.appendleft(tmp8)
                                if len(subjects3) >= 1 and subjects3[0] == Integer(2):
                                    tmp10 = subjects3.popleft()
                                    # State 17456
                                    if len(subjects3) == 0:
                                        pass
                                        # State 17457
                                        if len(subjects) == 0:
                                            pass
                                            # 2: b*(x*d + c)**2
                                            yield 2, subst4
                                    subjects3.appendleft(tmp10)
                                if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                    tmp11 = subjects3.popleft()
                                    # State 17497
                                    if len(subjects3) == 0:
                                        pass
                                        # State 17498
                                        if len(subjects) == 0:
                                            pass
                                            # 3: b/(x*d + c)
                                            yield 3, subst4
                                    subjects3.appendleft(tmp11)
                            subjects3.appendleft(tmp6)
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17555
                        if len(subjects3) >= 1:
                            tmp13 = subjects3.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.1.2.1.0', tmp13)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 17556
                                if len(subjects3) >= 1:
                                    tmp15 = subjects3.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.3.1.2', tmp15)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 17557
                                        if len(subjects3) == 0:
                                            pass
                                            # State 17558
                                            if len(subjects) == 0:
                                                pass
                                                # 4: b*(c + x*d)**n
                                                yield 4, subst5
                                    subjects3.appendleft(tmp15)
                            subjects3.appendleft(tmp13)
                    if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                        tmp17 = subjects3.popleft()
                        associative1 = tmp17
                        associative_type1 = type(tmp17)
                        subjects18 = deque(tmp17._args)
                        matcher = CommutativeMatcher17297.get()
                        tmp19 = subjects18
                        subjects18 = []
                        for s in tmp19:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp19, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 17298
                                if len(subjects3) >= 1:
                                    tmp20 = []
                                    tmp20.append(subjects3.popleft())
                                    while True:
                                        if len(tmp20) > 1:
                                            tmp21 = create_operation_expression(associative1, tmp20)
                                        elif len(tmp20) == 1:
                                            tmp21 = tmp20[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.1.2', tmp21)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 17299
                                            if len(subjects3) == 0:
                                                pass
                                                # State 17300
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: b*(x*d + c)**n
                                                    yield 0, subst4
                                        if len(subjects3) == 0:
                                            break
                                        tmp20.append(subjects3.popleft())
                                    subjects3.extendleft(reversed(tmp20))
                                if len(subjects3) >= 1 and subjects3[0] == Integer(2):
                                    tmp23 = subjects3.popleft()
                                    # State 17458
                                    if len(subjects3) == 0:
                                        pass
                                        # State 17459
                                        if len(subjects) == 0:
                                            pass
                                            # 2: b*(x*d + c)**2
                                            yield 2, subst3
                                    subjects3.appendleft(tmp23)
                                if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                    tmp24 = subjects3.popleft()
                                    # State 17499
                                    if len(subjects3) == 0:
                                        pass
                                        # State 17500
                                        if len(subjects) == 0:
                                            pass
                                            # 3: b/(x*d + c)
                                            yield 3, subst3
                                    subjects3.appendleft(tmp24)
                            if pattern_index == 1:
                                pass
                                # State 17559
                                if len(subjects3) >= 1:
                                    tmp25 = []
                                    tmp25.append(subjects3.popleft())
                                    while True:
                                        if len(tmp25) > 1:
                                            tmp26 = create_operation_expression(associative1, tmp25)
                                        elif len(tmp25) == 1:
                                            tmp26 = tmp25[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.1.2', tmp26)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 17560
                                            if len(subjects3) == 0:
                                                pass
                                                # State 17561
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: b*(c + x*d)**n
                                                    yield 4, subst4
                                        if len(subjects3) == 0:
                                            break
                                        tmp25.append(subjects3.popleft())
                                    subjects3.extendleft(reversed(tmp25))
                        subjects3.appendleft(tmp17)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 17380
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17381
                        if len(subjects3) >= 1:
                            tmp30 = subjects3.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.0', tmp30)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 17382
                                if len(subjects3) >= 1:
                                    tmp32 = subjects3.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.3.1.2', tmp32)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 17383
                                        if len(subjects3) == 0:
                                            pass
                                            # State 17384
                                            if len(subjects) == 0:
                                                pass
                                                # 1: b*(e + x*f)**n
                                                yield 1, subst5
                                    subjects3.appendleft(tmp32)
                            subjects3.appendleft(tmp30)
                    if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                        tmp34 = subjects3.popleft()
                        associative1 = tmp34
                        associative_type1 = type(tmp34)
                        subjects35 = deque(tmp34._args)
                        matcher = CommutativeMatcher17386.get()
                        tmp36 = subjects35
                        subjects35 = []
                        for s in tmp36:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp36, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 17387
                                if len(subjects3) >= 1:
                                    tmp37 = []
                                    tmp37.append(subjects3.popleft())
                                    while True:
                                        if len(tmp37) > 1:
                                            tmp38 = create_operation_expression(associative1, tmp37)
                                        elif len(tmp37) == 1:
                                            tmp38 = tmp37[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.1.2', tmp38)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 17388
                                            if len(subjects3) == 0:
                                                pass
                                                # State 17389
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: b*(e + x*f)**n
                                                    yield 1, subst4
                                        if len(subjects3) == 0:
                                            break
                                        tmp37.append(subjects3.popleft())
                                    subjects3.extendleft(reversed(tmp37))
                        subjects3.appendleft(tmp34)
                if len(subjects3) >= 1:
                    tmp40 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.3.1.1', tmp40)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17688
                        if len(subjects3) >= 1 and subjects3[0] == Integer(2):
                            tmp42 = subjects3.popleft()
                            # State 17689
                            if len(subjects3) == 0:
                                pass
                                # State 17690
                                if len(subjects) == 0:
                                    pass
                                    # 7: c*x**2
                                    yield 7, subst2
                            subjects3.appendleft(tmp42)
                    subjects3.appendleft(tmp40)
                if len(subjects3) >= 1:
                    tmp43 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.0', tmp43)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17707
                        if len(subjects3) >= 1 and subjects3[0] == Integer(2):
                            tmp45 = subjects3.popleft()
                            # State 17708
                            if len(subjects3) == 0:
                                pass
                                # State 17709
                                if len(subjects) == 0:
                                    pass
                                    # 9: v**2*c
                                    yield 9, subst2
                            subjects3.appendleft(tmp45)
                    subjects3.appendleft(tmp43)
                if len(subjects3) >= 1 and isinstance(subjects3[0], Add):
                    tmp46 = subjects3.popleft()
                    associative1 = tmp46
                    associative_type1 = type(tmp46)
                    subjects47 = deque(tmp46._args)
                    matcher = CommutativeMatcher17302.get()
                    tmp48 = subjects47
                    subjects47 = []
                    for s in tmp48:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp48, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 17308
                            if len(subjects3) >= 1:
                                tmp49 = []
                                tmp49.append(subjects3.popleft())
                                while True:
                                    if len(tmp49) > 1:
                                        tmp50 = create_operation_expression(associative1, tmp49)
                                    elif len(tmp49) == 1:
                                        tmp50 = tmp49[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.1.2', tmp50)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 17309
                                        if len(subjects3) == 0:
                                            pass
                                            # State 17310
                                            if len(subjects) == 0:
                                                pass
                                                # 0: b*(x*d + c)**n
                                                yield 0, subst3
                                    if len(subjects3) == 0:
                                        break
                                    tmp49.append(subjects3.popleft())
                                subjects3.extendleft(reversed(tmp49))
                            if len(subjects3) >= 1 and subjects3[0] == Integer(2):
                                tmp52 = subjects3.popleft()
                                # State 17460
                                if len(subjects3) == 0:
                                    pass
                                    # State 17461
                                    if len(subjects) == 0:
                                        pass
                                        # 2: b*(x*d + c)**2
                                        yield 2, subst2
                                subjects3.appendleft(tmp52)
                            if len(subjects3) >= 1 and subjects3[0] == Integer(-1):
                                tmp53 = subjects3.popleft()
                                # State 17501
                                if len(subjects3) == 0:
                                    pass
                                    # State 17502
                                    if len(subjects) == 0:
                                        pass
                                        # 3: b/(x*d + c)
                                        yield 3, subst2
                                subjects3.appendleft(tmp53)
                        if pattern_index == 1:
                            pass
                            # State 17393
                            if len(subjects3) >= 1:
                                tmp54 = []
                                tmp54.append(subjects3.popleft())
                                while True:
                                    if len(tmp54) > 1:
                                        tmp55 = create_operation_expression(associative1, tmp54)
                                    elif len(tmp54) == 1:
                                        tmp55 = tmp54[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.1.2', tmp55)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 17394
                                        if len(subjects3) == 0:
                                            pass
                                            # State 17395
                                            if len(subjects) == 0:
                                                pass
                                                # 1: b*(e + x*f)**n
                                                yield 1, subst3
                                    if len(subjects3) == 0:
                                        break
                                    tmp54.append(subjects3.popleft())
                                subjects3.extendleft(reversed(tmp54))
                        if pattern_index == 2:
                            pass
                            # State 17565
                            if len(subjects3) >= 1:
                                tmp57 = []
                                tmp57.append(subjects3.popleft())
                                while True:
                                    if len(tmp57) > 1:
                                        tmp58 = create_operation_expression(associative1, tmp57)
                                    elif len(tmp57) == 1:
                                        tmp58 = tmp57[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.1.2', tmp58)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 17566
                                        if len(subjects3) == 0:
                                            pass
                                            # State 17567
                                            if len(subjects) == 0:
                                                pass
                                                # 4: b*(c + x*d)**n
                                                yield 4, subst3
                                    if len(subjects3) == 0:
                                        break
                                    tmp57.append(subjects3.popleft())
                                subjects3.extendleft(reversed(tmp57))
                    subjects3.appendleft(tmp46)
                subjects.appendleft(tmp2)
            if len(subjects) >= 1:
                tmp60 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp60)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103800
                    if len(subjects) == 0:
                        pass
                        # 12: x*f
                        yield 12, subst2
                subjects.appendleft(tmp60)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 17615
            if len(subjects) >= 1:
                tmp63 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp63)
                except ValueError:
                    pass
                else:
                    pass
                    # State 17616
                    if len(subjects) == 0:
                        pass
                        # 5: v*b
                        yield 5, subst2
                subjects.appendleft(tmp63)
            if len(subjects) >= 1:
                tmp65 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1', tmp65)
                except ValueError:
                    pass
                else:
                    pass
                    # State 17695
                    if len(subjects) == 0:
                        pass
                        # 8: b*x
                        yield 8, subst2
                subjects.appendleft(tmp65)
            if len(subjects) >= 1:
                tmp67 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp67)
                except ValueError:
                    pass
                else:
                    pass
                    # State 17714
                    if len(subjects) == 0:
                        pass
                        # 10: x*b
                        yield 10, subst2
                subjects.appendleft(tmp67)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 101231
            if len(subjects) >= 1:
                tmp70 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp70)
                except ValueError:
                    pass
                else:
                    pass
                    # State 101232
                    if len(subjects) == 0:
                        pass
                        # 11: x*f
                        yield 11, subst2
                subjects.appendleft(tmp70)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp72 = subjects.popleft()
            associative1 = tmp72
            associative_type1 = type(tmp72)
            subjects73 = deque(tmp72._args)
            matcher = CommutativeMatcher17312.get()
            tmp74 = subjects73
            subjects73 = []
            for s in tmp74:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp74, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 17334
                    if len(subjects) == 0:
                        pass
                        # 0: b*(x*d + c)**n
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 17412
                    if len(subjects) == 0:
                        pass
                        # 1: b*(e + x*f)**n
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 17468
                    if len(subjects) == 0:
                        pass
                        # 2: b*(x*d + c)**2
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 17509
                    if len(subjects) == 0:
                        pass
                        # 3: b/(x*d + c)
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 17581
                    if len(subjects) == 0:
                        pass
                        # 4: b*(c + x*d)**n
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 17617
                    if len(subjects) == 0:
                        pass
                        # 5: v*b
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 17656
                    if len(subjects) == 0:
                        pass
                        # 6: f*(x*b + a)/(x*d + c)
                        yield 6, subst1
                if pattern_index == 7:
                    pass
                    # State 17694
                    if len(subjects) == 0:
                        pass
                        # 7: c*x**2
                        yield 7, subst1
                if pattern_index == 8:
                    pass
                    # State 17696
                    if len(subjects) == 0:
                        pass
                        # 8: b*x
                        yield 8, subst1
                if pattern_index == 9:
                    pass
                    # State 17713
                    if len(subjects) == 0:
                        pass
                        # 9: v**2*c
                        yield 9, subst1
                if pattern_index == 10:
                    pass
                    # State 17715
                    if len(subjects) == 0:
                        pass
                        # 10: x*b
                        yield 10, subst1
                if pattern_index == 11:
                    pass
                    # State 101233
                    if len(subjects) == 0:
                        pass
                        # 11: x*f
                        yield 11, subst1
                if pattern_index == 12:
                    pass
                    # State 103801
                    if len(subjects) == 0:
                        pass
                        # 12: x*f
                        yield 12, subst1
            subjects.appendleft(tmp72)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part005997 import *
from .generated_part005995 import *
from collections import deque
from .generated_part005994 import *
from .generated_part005993 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset