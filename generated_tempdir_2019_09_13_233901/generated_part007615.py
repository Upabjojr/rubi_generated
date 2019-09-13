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

class CommutativeMatcher27503(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      
]),
    1: (1, Multiset({0: 1, 2: 1}), [
      
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.0_1', 1, 1, None), Add)
]),
    3: (3, Multiset({3: 1, 4: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({5: 1, 4: 1}), [
      (VariableWithCount('i2.2.0_2', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({6: 1, 7: 1}), [
      (VariableWithCount('i2.2.0', 1, 1, S(0)), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 1
    anonymous_patterns = {0}

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher27503._instance is None:
            CommutativeMatcher27503._instance = CommutativeMatcher27503()
        return CommutativeMatcher27503._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 27502
        if len(subjects) >= 1 and subjects[0] == 1:
            tmp1 = subjects.popleft()
            # State 27504
            if len(subjects) == 0:
                pass
                # 0: 1
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 27505
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 27506
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.0_1', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 27507
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 27508
                        if len(subjects) >= 1:
                            tmp6 = subjects.popleft()
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 27509
                                if len(subjects) == 0:
                                    pass
                                    # 1: i*(j + k*x)**m
                            subjects.appendleft(tmp6)
                    if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                        tmp8 = subjects.popleft()
                        associative1 = tmp8
                        associative_type1 = type(tmp8)
                        subjects9 = deque(tmp8._args)
                        matcher = CommutativeMatcher27511.get()
                        tmp10 = subjects9
                        subjects9 = []
                        for s in tmp10:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp10, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 27512
                                if len(subjects) == 0:
                                    pass
                                    # 1: i*(j + k*x)**m
                        subjects.appendleft(tmp8)
                if len(subjects) >= 1 and isinstance(subjects[0], Add):
                    tmp11 = subjects.popleft()
                    associative1 = tmp11
                    associative_type1 = type(tmp11)
                    subjects12 = deque(tmp11._args)
                    matcher = CommutativeMatcher27514.get()
                    tmp13 = subjects12
                    subjects12 = []
                    for s in tmp13:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp13, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 27520
                            if len(subjects) == 0:
                                pass
                                # 1: i*(j + k*x)**m
                    subjects.appendleft(tmp11)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.4', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 53377
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp15 = subjects.popleft()
                    subjects16 = deque(tmp15._args)
                    # State 53378
                    if len(subjects16) >= 1:
                        tmp17 = subjects16.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2', tmp17)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53379
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.4.0', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53380
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.4.1.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53381
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.4.1.1.0', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 53382
                                        if len(subjects16) >= 1:
                                            tmp22 = subjects16.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.0', tmp22)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 53383
                                                if len(subjects16) == 0:
                                                    pass
                                                    # State 53384
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: e*(F**(c*(x*b + a)))**n
                                            subjects16.appendleft(tmp22)
                                    if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                                        tmp24 = subjects16.popleft()
                                        associative1 = tmp24
                                        associative_type1 = type(tmp24)
                                        subjects25 = deque(tmp24._args)
                                        matcher = CommutativeMatcher53386.get()
                                        tmp26 = subjects25
                                        subjects25 = []
                                        for s in tmp26:
                                            matcher.add_subject(s)
                                        for pattern_index, subst6 in matcher.match(tmp26, subst5):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 53387
                                                if len(subjects16) == 0:
                                                    pass
                                                    # State 53388
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: e*(F**(c*(x*b + a)))**n
                                        subjects16.appendleft(tmp24)
                                if len(subjects16) >= 1 and isinstance(subjects16[0], Add):
                                    tmp27 = subjects16.popleft()
                                    associative1 = tmp27
                                    associative_type1 = type(tmp27)
                                    subjects28 = deque(tmp27._args)
                                    matcher = CommutativeMatcher53390.get()
                                    tmp29 = subjects28
                                    subjects28 = []
                                    for s in tmp29:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp29, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 53396
                                            if len(subjects16) == 0:
                                                pass
                                                # State 53397
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: e*(F**(c*(x*b + a)))**n
                                    subjects16.appendleft(tmp27)
                            if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                                tmp30 = subjects16.popleft()
                                associative1 = tmp30
                                associative_type1 = type(tmp30)
                                subjects31 = deque(tmp30._args)
                                matcher = CommutativeMatcher53399.get()
                                tmp32 = subjects31
                                subjects31 = []
                                for s in tmp32:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp32, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 53414
                                        if len(subjects16) == 0:
                                            pass
                                            # State 53415
                                            if len(subjects) == 0:
                                                pass
                                                # 2: e*(F**(c*(x*b + a)))**n
                                subjects16.appendleft(tmp30)
                        subjects16.appendleft(tmp17)
                    subjects.appendleft(tmp15)
            if len(subjects) >= 1:
                tmp33 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0_1', tmp33)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53772
                    if len(subjects) == 0:
                        pass
                        # 7: x*e
                subjects.appendleft(tmp33)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp35 = subjects.popleft()
                subjects36 = deque(tmp35._args)
                # State 27521
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0_1', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 27522
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 27523
                        if len(subjects36) >= 1:
                            tmp39 = subjects36.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.1.0', tmp39)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 27524
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27525
                                    if len(subjects36) == 0:
                                        pass
                                        # State 27526
                                        if len(subjects) == 0:
                                            pass
                                            # 1: i*(j + k*x)**m
                                if len(subjects36) >= 1:
                                    tmp42 = subjects36.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2', tmp42)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27525
                                        if len(subjects36) == 0:
                                            pass
                                            # State 27526
                                            if len(subjects) == 0:
                                                pass
                                                # 1: i*(j + k*x)**m
                                    subjects36.appendleft(tmp42)
                            subjects36.appendleft(tmp39)
                    if len(subjects36) >= 1 and isinstance(subjects36[0], Mul):
                        tmp44 = subjects36.popleft()
                        associative1 = tmp44
                        associative_type1 = type(tmp44)
                        subjects45 = deque(tmp44._args)
                        matcher = CommutativeMatcher27528.get()
                        tmp46 = subjects45
                        subjects45 = []
                        for s in tmp46:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp46, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 27529
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27530
                                    if len(subjects36) == 0:
                                        pass
                                        # State 27531
                                        if len(subjects) == 0:
                                            pass
                                            # 1: i*(j + k*x)**m
                                if len(subjects36) >= 1:
                                    tmp48 = []
                                    tmp48.append(subjects36.popleft())
                                    while True:
                                        if len(tmp48) > 1:
                                            tmp49 = create_operation_expression(associative1, tmp48)
                                        elif len(tmp48) == 1:
                                            tmp49 = tmp48[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2', tmp49)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 27530
                                            if len(subjects36) == 0:
                                                pass
                                                # State 27531
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: i*(j + k*x)**m
                                        if len(subjects36) == 0:
                                            break
                                        tmp48.append(subjects36.popleft())
                                    subjects36.extendleft(reversed(tmp48))
                        subjects36.appendleft(tmp44)
                if len(subjects36) >= 1 and isinstance(subjects36[0], Add):
                    tmp51 = subjects36.popleft()
                    associative1 = tmp51
                    associative_type1 = type(tmp51)
                    subjects52 = deque(tmp51._args)
                    matcher = CommutativeMatcher27533.get()
                    tmp53 = subjects52
                    subjects52 = []
                    for s in tmp53:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp53, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 27539
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 27540
                                if len(subjects36) == 0:
                                    pass
                                    # State 27541
                                    if len(subjects) == 0:
                                        pass
                                        # 1: i*(j + k*x)**m
                            if len(subjects36) >= 1:
                                tmp55 = []
                                tmp55.append(subjects36.popleft())
                                while True:
                                    if len(tmp55) > 1:
                                        tmp56 = create_operation_expression(associative1, tmp55)
                                    elif len(tmp55) == 1:
                                        tmp56 = tmp55[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2', tmp56)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27540
                                        if len(subjects36) == 0:
                                            pass
                                            # State 27541
                                            if len(subjects) == 0:
                                                pass
                                                # 1: i*(j + k*x)**m
                                    if len(subjects36) == 0:
                                        break
                                    tmp55.append(subjects36.popleft())
                                subjects36.extendleft(reversed(tmp55))
                    subjects36.appendleft(tmp51)
                if len(subjects36) >= 1 and isinstance(subjects36[0], Pow):
                    tmp58 = subjects36.popleft()
                    subjects59 = deque(tmp58._args)
                    # State 53416
                    if len(subjects59) >= 1:
                        tmp60 = subjects59.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp60)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53417
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.4.0', S(1))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53418
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.4.1.0', S(0))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53419
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.4.1.1.0', S(1))
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 53420
                                        if len(subjects59) >= 1:
                                            tmp65 = subjects59.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.0', tmp65)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 53421
                                                if len(subjects59) == 0:
                                                    pass
                                                    # State 53422
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.4', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 53423
                                                        if len(subjects36) == 0:
                                                            pass
                                                            # State 53424
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: e*(F**(c*(x*b + a)))**n
                                                    if len(subjects36) >= 1:
                                                        tmp68 = subjects36.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.4', tmp68)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 53423
                                                            if len(subjects36) == 0:
                                                                pass
                                                                # State 53424
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 2: e*(F**(c*(x*b + a)))**n
                                                        subjects36.appendleft(tmp68)
                                            subjects59.appendleft(tmp65)
                                    if len(subjects59) >= 1 and isinstance(subjects59[0], Mul):
                                        tmp70 = subjects59.popleft()
                                        associative1 = tmp70
                                        associative_type1 = type(tmp70)
                                        subjects71 = deque(tmp70._args)
                                        matcher = CommutativeMatcher53426.get()
                                        tmp72 = subjects71
                                        subjects71 = []
                                        for s in tmp72:
                                            matcher.add_subject(s)
                                        for pattern_index, subst5 in matcher.match(tmp72, subst4):
                                            pass
                                            if pattern_index == 0:
                                                pass
                                                # State 53427
                                                if len(subjects59) == 0:
                                                    pass
                                                    # State 53428
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.4', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 53429
                                                        if len(subjects36) == 0:
                                                            pass
                                                            # State 53430
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: e*(F**(c*(x*b + a)))**n
                                                    if len(subjects36) >= 1:
                                                        tmp74 = subjects36.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.4', tmp74)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 53429
                                                            if len(subjects36) == 0:
                                                                pass
                                                                # State 53430
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 2: e*(F**(c*(x*b + a)))**n
                                                        subjects36.appendleft(tmp74)
                                        subjects59.appendleft(tmp70)
                                if len(subjects59) >= 1 and isinstance(subjects59[0], Add):
                                    tmp76 = subjects59.popleft()
                                    associative1 = tmp76
                                    associative_type1 = type(tmp76)
                                    subjects77 = deque(tmp76._args)
                                    matcher = CommutativeMatcher53432.get()
                                    tmp78 = subjects77
                                    subjects77 = []
                                    for s in tmp78:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp78, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 53438
                                            if len(subjects59) == 0:
                                                pass
                                                # State 53439
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 53440
                                                    if len(subjects36) == 0:
                                                        pass
                                                        # State 53441
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: e*(F**(c*(x*b + a)))**n
                                                if len(subjects36) >= 1:
                                                    tmp80 = subjects36.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.4', tmp80)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 53440
                                                        if len(subjects36) == 0:
                                                            pass
                                                            # State 53441
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: e*(F**(c*(x*b + a)))**n
                                                    subjects36.appendleft(tmp80)
                                    subjects59.appendleft(tmp76)
                            if len(subjects59) >= 1 and isinstance(subjects59[0], Mul):
                                tmp82 = subjects59.popleft()
                                associative1 = tmp82
                                associative_type1 = type(tmp82)
                                subjects83 = deque(tmp82._args)
                                matcher = CommutativeMatcher53443.get()
                                tmp84 = subjects83
                                subjects83 = []
                                for s in tmp84:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp84, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 53458
                                        if len(subjects59) == 0:
                                            pass
                                            # State 53459
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.4', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 53460
                                                if len(subjects36) == 0:
                                                    pass
                                                    # State 53461
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: e*(F**(c*(x*b + a)))**n
                                            if len(subjects36) >= 1:
                                                tmp86 = subjects36.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.4', tmp86)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 53460
                                                    if len(subjects36) == 0:
                                                        pass
                                                        # State 53461
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: e*(F**(c*(x*b + a)))**n
                                                subjects36.appendleft(tmp86)
                                subjects59.appendleft(tmp82)
                        subjects59.appendleft(tmp60)
                    subjects36.appendleft(tmp58)
                subjects.appendleft(tmp35)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 53651
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp89 = subjects.popleft()
                subjects90 = deque(tmp89._args)
                # State 53652
                if len(subjects90) >= 1 and isinstance(subjects90[0], Add):
                    tmp91 = subjects90.popleft()
                    associative1 = tmp91
                    associative_type1 = type(tmp91)
                    subjects92 = deque(tmp91._args)
                    matcher = CommutativeMatcher53654.get()
                    tmp93 = subjects92
                    subjects92 = []
                    for s in tmp93:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp93, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 53670
                            if len(subjects90) >= 1 and subjects90[0] == 1/2:
                                tmp94 = subjects90.popleft()
                                # State 53671
                                if len(subjects90) == 0:
                                    pass
                                    # State 53672
                                    if len(subjects) == 0:
                                        pass
                                        # 3: f*sqrt(v**2*c + x*b + a)
                                subjects90.appendleft(tmp94)
                        if pattern_index == 1:
                            pass
                            # State 53714
                            if len(subjects90) >= 1 and subjects90[0] == 1/2:
                                tmp95 = subjects90.popleft()
                                # State 53715
                                if len(subjects90) == 0:
                                    pass
                                    # State 53716
                                    if len(subjects) == 0:
                                        pass
                                        # 5: f*sqrt(v**2*c + a)
                                subjects90.appendleft(tmp95)
                    subjects90.appendleft(tmp91)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 53697
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53698
                        if len(subjects90) >= 1 and isinstance(subjects90[0], Pow):
                            tmp98 = subjects90.popleft()
                            subjects99 = deque(tmp98._args)
                            # State 53699
                            if len(subjects99) >= 1:
                                tmp100 = subjects99.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.0', tmp100)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53700
                                    if len(subjects99) >= 1 and subjects99[0] == 2:
                                        tmp102 = subjects99.popleft()
                                        # State 53701
                                        if len(subjects99) == 0:
                                            pass
                                            # State 53702
                                            if len(subjects90) >= 1 and subjects90[0] == 1/2:
                                                tmp103 = subjects90.popleft()
                                                # State 53703
                                                if len(subjects90) == 0:
                                                    pass
                                                    # State 53704
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: f*sqrt(v**2*c + a)
                                                subjects90.appendleft(tmp103)
                                        subjects99.appendleft(tmp102)
                                subjects99.appendleft(tmp100)
                            subjects90.appendleft(tmp98)
                    if len(subjects90) >= 1 and isinstance(subjects90[0], Mul):
                        tmp104 = subjects90.popleft()
                        associative1 = tmp104
                        associative_type1 = type(tmp104)
                        subjects105 = deque(tmp104._args)
                        matcher = CommutativeMatcher53706.get()
                        tmp106 = subjects105
                        subjects105 = []
                        for s in tmp106:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp106, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 53711
                                if len(subjects90) >= 1 and subjects90[0] == 1/2:
                                    tmp107 = subjects90.popleft()
                                    # State 53712
                                    if len(subjects90) == 0:
                                        pass
                                        # State 53713
                                        if len(subjects) == 0:
                                            pass
                                            # 5: f*sqrt(v**2*c + a)
                                    subjects90.appendleft(tmp107)
                        subjects90.appendleft(tmp104)
                if len(subjects90) >= 1:
                    tmp108 = subjects90.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp108)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53765
                        if len(subjects90) >= 1 and subjects90[0] == 1/2:
                            tmp110 = subjects90.popleft()
                            # State 53766
                            if len(subjects90) == 0:
                                pass
                                # State 53767
                                if len(subjects) == 0:
                                    pass
                                    # 6: f*sqrt(u)
                            subjects90.appendleft(tmp110)
                    subjects90.appendleft(tmp108)
                subjects.appendleft(tmp89)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 53689
            if len(subjects) >= 1:
                tmp112 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.0', tmp112)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53690
                    if len(subjects) == 0:
                        pass
                        # 4: x*e
                subjects.appendleft(tmp112)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp114 = subjects.popleft()
            associative1 = tmp114
            associative_type1 = type(tmp114)
            subjects115 = deque(tmp114._args)
            matcher = CommutativeMatcher27543.get()
            tmp116 = subjects115
            subjects115 = []
            for s in tmp116:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp116, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 27580
                    if len(subjects) == 0:
                        pass
                        # 1: i*(j + k*x)**m
                if pattern_index == 1:
                    pass
                    # State 53547
                    if len(subjects) == 0:
                        pass
                        # 2: e*(F**(c*(x*b + a)))**n
                if pattern_index == 2:
                    pass
                    # State 53688
                    if len(subjects) == 0:
                        pass
                        # 3: f*sqrt(v**2*c + x*b + a)
                if pattern_index == 3:
                    pass
                    # State 53691
                    if len(subjects) == 0:
                        pass
                        # 4: x*e
                if pattern_index == 4:
                    pass
                    # State 53737
                    if len(subjects) == 0:
                        pass
                        # 5: f*sqrt(v**2*c + a)
                if pattern_index == 5:
                    pass
                    # State 53771
                    if len(subjects) == 0:
                        pass
                        # 6: f*sqrt(u)
                if pattern_index == 6:
                    pass
                    # State 53773
                    if len(subjects) == 0:
                        pass
                        # 7: x*e
            subjects.appendleft(tmp114)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
