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

class CommutativeMatcher27543(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({}), [
      (VariableWithCount('i2.2.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher27543._instance is None:
            CommutativeMatcher27543._instance = CommutativeMatcher27543()
        return CommutativeMatcher27543._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 27542
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 27544
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 27545
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 27546
                    if len(subjects) >= 1:
                        tmp4 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', tmp4)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 27547
                            if len(subjects) == 0:
                                pass
                                # 0: (j + k*x)**m
                        subjects.appendleft(tmp4)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp6 = subjects.popleft()
                    associative1 = tmp6
                    associative_type1 = type(tmp6)
                    subjects7 = deque(tmp6._args)
                    matcher = CommutativeMatcher27549.get()
                    tmp8 = subjects7
                    subjects7 = []
                    for s in tmp8:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp8, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 27550
                            if len(subjects) == 0:
                                pass
                                # 0: (j + k*x)**m
                    subjects.appendleft(tmp6)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp9 = subjects.popleft()
                associative1 = tmp9
                associative_type1 = type(tmp9)
                subjects10 = deque(tmp9._args)
                matcher = CommutativeMatcher27552.get()
                tmp11 = subjects10
                subjects10 = []
                for s in tmp11:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp11, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 27558
                        if len(subjects) == 0:
                            pass
                            # 0: (j + k*x)**m
                subjects.appendleft(tmp9)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 53462
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp13 = subjects.popleft()
                subjects14 = deque(tmp13._args)
                # State 53463
                if len(subjects14) >= 1:
                    tmp15 = subjects14.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', tmp15)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53464
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53465
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53466
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.4.1.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53467
                                    if len(subjects14) >= 1:
                                        tmp20 = subjects14.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.0', tmp20)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 53468
                                            if len(subjects14) == 0:
                                                pass
                                                # State 53469
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (F**(c*(x*b + a)))**n
                                        subjects14.appendleft(tmp20)
                                if len(subjects14) >= 1 and isinstance(subjects14[0], Mul):
                                    tmp22 = subjects14.popleft()
                                    associative1 = tmp22
                                    associative_type1 = type(tmp22)
                                    subjects23 = deque(tmp22._args)
                                    matcher = CommutativeMatcher53471.get()
                                    tmp24 = subjects23
                                    subjects23 = []
                                    for s in tmp24:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp24, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 53472
                                            if len(subjects14) == 0:
                                                pass
                                                # State 53473
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (F**(c*(x*b + a)))**n
                                    subjects14.appendleft(tmp22)
                            if len(subjects14) >= 1 and isinstance(subjects14[0], Add):
                                tmp25 = subjects14.popleft()
                                associative1 = tmp25
                                associative_type1 = type(tmp25)
                                subjects26 = deque(tmp25._args)
                                matcher = CommutativeMatcher53475.get()
                                tmp27 = subjects26
                                subjects26 = []
                                for s in tmp27:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp27, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 53481
                                        if len(subjects14) == 0:
                                            pass
                                            # State 53482
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (F**(c*(x*b + a)))**n
                                subjects14.appendleft(tmp25)
                        if len(subjects14) >= 1 and isinstance(subjects14[0], Mul):
                            tmp28 = subjects14.popleft()
                            associative1 = tmp28
                            associative_type1 = type(tmp28)
                            subjects29 = deque(tmp28._args)
                            matcher = CommutativeMatcher53484.get()
                            tmp30 = subjects29
                            subjects29 = []
                            for s in tmp30:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp30, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 53499
                                    if len(subjects14) == 0:
                                        pass
                                        # State 53500
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (F**(c*(x*b + a)))**n
                            subjects14.appendleft(tmp28)
                    subjects14.appendleft(tmp15)
                subjects.appendleft(tmp13)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp31 = subjects.popleft()
            subjects32 = deque(tmp31._args)
            # State 27559
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 27560
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 27561
                    if len(subjects32) >= 1:
                        tmp35 = subjects32.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0', tmp35)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 27562
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 27563
                                if len(subjects32) == 0:
                                    pass
                                    # State 27564
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (j + k*x)**m
                            if len(subjects32) >= 1:
                                tmp38 = subjects32.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2', tmp38)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27563
                                    if len(subjects32) == 0:
                                        pass
                                        # State 27564
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (j + k*x)**m
                                subjects32.appendleft(tmp38)
                        subjects32.appendleft(tmp35)
                if len(subjects32) >= 1 and isinstance(subjects32[0], Mul):
                    tmp40 = subjects32.popleft()
                    associative1 = tmp40
                    associative_type1 = type(tmp40)
                    subjects41 = deque(tmp40._args)
                    matcher = CommutativeMatcher27566.get()
                    tmp42 = subjects41
                    subjects41 = []
                    for s in tmp42:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp42, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 27567
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 27568
                                if len(subjects32) == 0:
                                    pass
                                    # State 27569
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (j + k*x)**m
                            if len(subjects32) >= 1:
                                tmp44 = []
                                tmp44.append(subjects32.popleft())
                                while True:
                                    if len(tmp44) > 1:
                                        tmp45 = create_operation_expression(associative1, tmp44)
                                    elif len(tmp44) == 1:
                                        tmp45 = tmp44[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2', tmp45)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 27568
                                        if len(subjects32) == 0:
                                            pass
                                            # State 27569
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (j + k*x)**m
                                    if len(subjects32) == 0:
                                        break
                                    tmp44.append(subjects32.popleft())
                                subjects32.extendleft(reversed(tmp44))
                    subjects32.appendleft(tmp40)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 53717
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 53718
                    if len(subjects32) >= 1 and isinstance(subjects32[0], Pow):
                        tmp49 = subjects32.popleft()
                        subjects50 = deque(tmp49._args)
                        # State 53719
                        if len(subjects50) >= 1:
                            tmp51 = subjects50.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.0', tmp51)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53720
                                if len(subjects50) >= 1 and subjects50[0] == 2:
                                    tmp53 = subjects50.popleft()
                                    # State 53721
                                    if len(subjects50) == 0:
                                        pass
                                        # State 53722
                                        if len(subjects32) >= 1 and subjects32[0] == 1/2:
                                            tmp54 = subjects32.popleft()
                                            # State 53723
                                            if len(subjects32) == 0:
                                                pass
                                                # State 53724
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: sqrt(v**2*c + a)
                                            subjects32.appendleft(tmp54)
                                    subjects50.appendleft(tmp53)
                            subjects50.appendleft(tmp51)
                        subjects32.appendleft(tmp49)
                if len(subjects32) >= 1 and isinstance(subjects32[0], Mul):
                    tmp55 = subjects32.popleft()
                    associative1 = tmp55
                    associative_type1 = type(tmp55)
                    subjects56 = deque(tmp55._args)
                    matcher = CommutativeMatcher53726.get()
                    tmp57 = subjects56
                    subjects56 = []
                    for s in tmp57:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp57, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 53731
                            if len(subjects32) >= 1 and subjects32[0] == 1/2:
                                tmp58 = subjects32.popleft()
                                # State 53732
                                if len(subjects32) == 0:
                                    pass
                                    # State 53733
                                    if len(subjects) == 0:
                                        pass
                                        # 3: sqrt(v**2*c + a)
                                subjects32.appendleft(tmp58)
                    subjects32.appendleft(tmp55)
            if len(subjects32) >= 1:
                tmp59 = subjects32.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp59)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53768
                    if len(subjects32) >= 1 and subjects32[0] == 1/2:
                        tmp61 = subjects32.popleft()
                        # State 53769
                        if len(subjects32) == 0:
                            pass
                            # State 53770
                            if len(subjects) == 0:
                                pass
                                # 4: sqrt(u)
                        subjects32.appendleft(tmp61)
                subjects32.appendleft(tmp59)
            if len(subjects32) >= 1 and isinstance(subjects32[0], Add):
                tmp62 = subjects32.popleft()
                associative1 = tmp62
                associative_type1 = type(tmp62)
                subjects63 = deque(tmp62._args)
                matcher = CommutativeMatcher27571.get()
                tmp64 = subjects63
                subjects63 = []
                for s in tmp64:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp64, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 27577
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 27578
                            if len(subjects32) == 0:
                                pass
                                # State 27579
                                if len(subjects) == 0:
                                    pass
                                    # 0: (j + k*x)**m
                        if len(subjects32) >= 1:
                            tmp66 = []
                            tmp66.append(subjects32.popleft())
                            while True:
                                if len(tmp66) > 1:
                                    tmp67 = create_operation_expression(associative1, tmp66)
                                elif len(tmp66) == 1:
                                    tmp67 = tmp66[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2', tmp67)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 27578
                                    if len(subjects32) == 0:
                                        pass
                                        # State 27579
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (j + k*x)**m
                                if len(subjects32) == 0:
                                    break
                                tmp66.append(subjects32.popleft())
                            subjects32.extendleft(reversed(tmp66))
                    if pattern_index == 1:
                        pass
                        # State 53685
                        if len(subjects32) >= 1 and subjects32[0] == 1/2:
                            tmp69 = subjects32.popleft()
                            # State 53686
                            if len(subjects32) == 0:
                                pass
                                # State 53687
                                if len(subjects) == 0:
                                    pass
                                    # 2: sqrt(v**2*c + x*b + a)
                            subjects32.appendleft(tmp69)
                    if pattern_index == 2:
                        pass
                        # State 53734
                        if len(subjects32) >= 1 and subjects32[0] == 1/2:
                            tmp70 = subjects32.popleft()
                            # State 53735
                            if len(subjects32) == 0:
                                pass
                                # State 53736
                                if len(subjects) == 0:
                                    pass
                                    # 3: sqrt(v**2*c + a)
                            subjects32.appendleft(tmp70)
                subjects32.appendleft(tmp62)
            if len(subjects32) >= 1 and isinstance(subjects32[0], Pow):
                tmp71 = subjects32.popleft()
                subjects72 = deque(tmp71._args)
                # State 53501
                if len(subjects72) >= 1:
                    tmp73 = subjects72.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp73)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53502
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53503
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53504
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.4.1.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 53505
                                    if len(subjects72) >= 1:
                                        tmp78 = subjects72.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.0', tmp78)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 53506
                                            if len(subjects72) == 0:
                                                pass
                                                # State 53507
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 53508
                                                    if len(subjects32) == 0:
                                                        pass
                                                        # State 53509
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: (F**(c*(x*b + a)))**n
                                                if len(subjects32) >= 1:
                                                    tmp81 = subjects32.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.4', tmp81)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 53508
                                                        if len(subjects32) == 0:
                                                            pass
                                                            # State 53509
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (F**(c*(x*b + a)))**n
                                                    subjects32.appendleft(tmp81)
                                        subjects72.appendleft(tmp78)
                                if len(subjects72) >= 1 and isinstance(subjects72[0], Mul):
                                    tmp83 = subjects72.popleft()
                                    associative1 = tmp83
                                    associative_type1 = type(tmp83)
                                    subjects84 = deque(tmp83._args)
                                    matcher = CommutativeMatcher53511.get()
                                    tmp85 = subjects84
                                    subjects84 = []
                                    for s in tmp85:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp85, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 53512
                                            if len(subjects72) == 0:
                                                pass
                                                # State 53513
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 53514
                                                    if len(subjects32) == 0:
                                                        pass
                                                        # State 53515
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: (F**(c*(x*b + a)))**n
                                                if len(subjects32) >= 1:
                                                    tmp87 = subjects32.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.4', tmp87)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 53514
                                                        if len(subjects32) == 0:
                                                            pass
                                                            # State 53515
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (F**(c*(x*b + a)))**n
                                                    subjects32.appendleft(tmp87)
                                    subjects72.appendleft(tmp83)
                            if len(subjects72) >= 1 and isinstance(subjects72[0], Add):
                                tmp89 = subjects72.popleft()
                                associative1 = tmp89
                                associative_type1 = type(tmp89)
                                subjects90 = deque(tmp89._args)
                                matcher = CommutativeMatcher53517.get()
                                tmp91 = subjects90
                                subjects90 = []
                                for s in tmp91:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp91, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 53523
                                        if len(subjects72) == 0:
                                            pass
                                            # State 53524
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.4', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 53525
                                                if len(subjects32) == 0:
                                                    pass
                                                    # State 53526
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (F**(c*(x*b + a)))**n
                                            if len(subjects32) >= 1:
                                                tmp93 = subjects32.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.4', tmp93)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 53525
                                                    if len(subjects32) == 0:
                                                        pass
                                                        # State 53526
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 1: (F**(c*(x*b + a)))**n
                                                subjects32.appendleft(tmp93)
                                subjects72.appendleft(tmp89)
                        if len(subjects72) >= 1 and isinstance(subjects72[0], Mul):
                            tmp95 = subjects72.popleft()
                            associative1 = tmp95
                            associative_type1 = type(tmp95)
                            subjects96 = deque(tmp95._args)
                            matcher = CommutativeMatcher53528.get()
                            tmp97 = subjects96
                            subjects96 = []
                            for s in tmp97:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp97, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 53543
                                    if len(subjects72) == 0:
                                        pass
                                        # State 53544
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.4', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 53545
                                            if len(subjects32) == 0:
                                                pass
                                                # State 53546
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (F**(c*(x*b + a)))**n
                                        if len(subjects32) >= 1:
                                            tmp99 = subjects32.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.4', tmp99)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 53545
                                                if len(subjects32) == 0:
                                                    pass
                                                    # State 53546
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (F**(c*(x*b + a)))**n
                                            subjects32.appendleft(tmp99)
                            subjects72.appendleft(tmp95)
                    subjects72.appendleft(tmp73)
                subjects32.appendleft(tmp71)
            subjects.appendleft(tmp31)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
