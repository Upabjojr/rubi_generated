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

class CommutativeMatcher18412(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({}), [
      (VariableWithCount('i3.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i3.1.2.1.1', 1, 1, None), Mul)
]),
    3: (3, Multiset({2: 1}), [
      (VariableWithCount('i3.1.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher18412._instance is None:
            CommutativeMatcher18412._instance = CommutativeMatcher18412()
        return CommutativeMatcher18412._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 18411
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.1.4', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 18413
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 18414
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.1.2', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 18415
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i3.1.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18416
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.1.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 18417
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.1.4.1.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18418
                                    if len(subjects3) >= 1:
                                        tmp9 = subjects3.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i3.1.4.1.1.0', tmp9)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 18419
                                            if len(subjects3) == 0:
                                                pass
                                                # State 18420
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (F**(e*(c + x*d)))**n
                                        subjects3.appendleft(tmp9)
                                if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                                    tmp11 = subjects3.popleft()
                                    associative1 = tmp11
                                    associative_type1 = type(tmp11)
                                    subjects12 = deque(tmp11._args)
                                    matcher = CommutativeMatcher18422.get()
                                    tmp13 = subjects12
                                    subjects12 = []
                                    for s in tmp13:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp13, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 18423
                                            if len(subjects3) == 0:
                                                pass
                                                # State 18424
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (F**(e*(c + x*d)))**n
                                    subjects3.appendleft(tmp11)
                            if len(subjects3) >= 1 and isinstance(subjects3[0], Add):
                                tmp14 = subjects3.popleft()
                                associative1 = tmp14
                                associative_type1 = type(tmp14)
                                subjects15 = deque(tmp14._args)
                                matcher = CommutativeMatcher18426.get()
                                tmp16 = subjects15
                                subjects15 = []
                                for s in tmp16:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp16, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 18432
                                        if len(subjects3) == 0:
                                            pass
                                            # State 18433
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (F**(e*(c + x*d)))**n
                                subjects3.appendleft(tmp14)
                        if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                            tmp17 = subjects3.popleft()
                            associative1 = tmp17
                            associative_type1 = type(tmp17)
                            subjects18 = deque(tmp17._args)
                            matcher = CommutativeMatcher18435.get()
                            tmp19 = subjects18
                            subjects18 = []
                            for s in tmp19:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp19, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 18450
                                    if len(subjects3) == 0:
                                        pass
                                        # State 18451
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (F**(e*(c + x*d)))**n
                            subjects3.appendleft(tmp17)
                    subjects3.appendleft(tmp4)
                subjects.appendleft(tmp2)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp20 = subjects.popleft()
            subjects21 = deque(tmp20._args)
            # State 18452
            if len(subjects21) >= 1 and isinstance(subjects21[0], Pow):
                tmp22 = subjects21.popleft()
                subjects23 = deque(tmp22._args)
                # State 18453
                if len(subjects23) >= 1:
                    tmp24 = subjects23.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i3.1.2', tmp24)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 18454
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i3.1.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 18455
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 18456
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.1.4.1.1.0_1', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 18457
                                    if len(subjects23) >= 1:
                                        tmp29 = subjects23.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i3.1.4.1.1.0', tmp29)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 18458
                                            if len(subjects23) == 0:
                                                pass
                                                # State 18459
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i3.1.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 18460
                                                    if len(subjects21) == 0:
                                                        pass
                                                        # State 18461
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (F**(e*(c + x*d)))**n
                                                if len(subjects21) >= 1:
                                                    tmp32 = subjects21.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i3.1.4', tmp32)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 18460
                                                        if len(subjects21) == 0:
                                                            pass
                                                            # State 18461
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (F**(e*(c + x*d)))**n
                                                    subjects21.appendleft(tmp32)
                                        subjects23.appendleft(tmp29)
                                if len(subjects23) >= 1 and isinstance(subjects23[0], Mul):
                                    tmp34 = subjects23.popleft()
                                    associative1 = tmp34
                                    associative_type1 = type(tmp34)
                                    subjects35 = deque(tmp34._args)
                                    matcher = CommutativeMatcher18463.get()
                                    tmp36 = subjects35
                                    subjects35 = []
                                    for s in tmp36:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp36, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 18464
                                            if len(subjects23) == 0:
                                                pass
                                                # State 18465
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i3.1.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 18466
                                                    if len(subjects21) == 0:
                                                        pass
                                                        # State 18467
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (F**(e*(c + x*d)))**n
                                                if len(subjects21) >= 1:
                                                    tmp38 = subjects21.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i3.1.4', tmp38)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 18466
                                                        if len(subjects21) == 0:
                                                            pass
                                                            # State 18467
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (F**(e*(c + x*d)))**n
                                                    subjects21.appendleft(tmp38)
                                    subjects23.appendleft(tmp34)
                            if len(subjects23) >= 1 and isinstance(subjects23[0], Add):
                                tmp40 = subjects23.popleft()
                                associative1 = tmp40
                                associative_type1 = type(tmp40)
                                subjects41 = deque(tmp40._args)
                                matcher = CommutativeMatcher18469.get()
                                tmp42 = subjects41
                                subjects41 = []
                                for s in tmp42:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp42, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 18475
                                        if len(subjects23) == 0:
                                            pass
                                            # State 18476
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i3.1.4', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 18477
                                                if len(subjects21) == 0:
                                                    pass
                                                    # State 18478
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (F**(e*(c + x*d)))**n
                                            if len(subjects21) >= 1:
                                                tmp44 = subjects21.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i3.1.4', tmp44)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 18477
                                                    if len(subjects21) == 0:
                                                        pass
                                                        # State 18478
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (F**(e*(c + x*d)))**n
                                                subjects21.appendleft(tmp44)
                                subjects23.appendleft(tmp40)
                        if len(subjects23) >= 1 and isinstance(subjects23[0], Mul):
                            tmp46 = subjects23.popleft()
                            associative1 = tmp46
                            associative_type1 = type(tmp46)
                            subjects47 = deque(tmp46._args)
                            matcher = CommutativeMatcher18480.get()
                            tmp48 = subjects47
                            subjects47 = []
                            for s in tmp48:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp48, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 18495
                                    if len(subjects23) == 0:
                                        pass
                                        # State 18496
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i3.1.4', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 18497
                                            if len(subjects21) == 0:
                                                pass
                                                # State 18498
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (F**(e*(c + x*d)))**n
                                        if len(subjects21) >= 1:
                                            tmp50 = subjects21.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i3.1.4', tmp50)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 18497
                                                if len(subjects21) == 0:
                                                    pass
                                                    # State 18498
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (F**(e*(c + x*d)))**n
                                            subjects21.appendleft(tmp50)
                            subjects23.appendleft(tmp46)
                    subjects23.appendleft(tmp24)
                subjects21.appendleft(tmp22)
            if len(subjects21) >= 1 and isinstance(subjects21[0], Add):
                tmp52 = subjects21.popleft()
                associative1 = tmp52
                associative_type1 = type(tmp52)
                subjects53 = deque(tmp52._args)
                matcher = CommutativeMatcher53579.get()
                tmp54 = subjects53
                subjects53 = []
                for s in tmp54:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp54, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 53595
                        if len(subjects21) >= 1 and subjects21[0] == 1/2:
                            tmp55 = subjects21.popleft()
                            # State 53596
                            if len(subjects21) == 0:
                                pass
                                # State 53597
                                if len(subjects) == 0:
                                    pass
                                    # 1: sqrt(a + b*x + c*x**2)
                            subjects21.appendleft(tmp55)
                    if pattern_index == 1:
                        pass
                        # State 53643
                        if len(subjects21) >= 1 and subjects21[0] == 1/2:
                            tmp56 = subjects21.popleft()
                            # State 53644
                            if len(subjects21) == 0:
                                pass
                                # State 53645
                                if len(subjects) == 0:
                                    pass
                                    # 2: sqrt(a + c*x**2)
                            subjects21.appendleft(tmp56)
                subjects21.appendleft(tmp52)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i3.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 53626
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 53627
                    if len(subjects21) >= 1 and isinstance(subjects21[0], Pow):
                        tmp59 = subjects21.popleft()
                        subjects60 = deque(tmp59._args)
                        # State 53628
                        if len(subjects60) >= 1:
                            tmp61 = subjects60.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.1.2.1.1', tmp61)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 53629
                                if len(subjects60) >= 1 and subjects60[0] == 2:
                                    tmp63 = subjects60.popleft()
                                    # State 53630
                                    if len(subjects60) == 0:
                                        pass
                                        # State 53631
                                        if len(subjects21) >= 1 and subjects21[0] == 1/2:
                                            tmp64 = subjects21.popleft()
                                            # State 53632
                                            if len(subjects21) == 0:
                                                pass
                                                # State 53633
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: sqrt(a + c*x**2)
                                            subjects21.appendleft(tmp64)
                                    subjects60.appendleft(tmp63)
                            subjects60.appendleft(tmp61)
                        subjects21.appendleft(tmp59)
                if len(subjects21) >= 1 and isinstance(subjects21[0], Mul):
                    tmp65 = subjects21.popleft()
                    associative1 = tmp65
                    associative_type1 = type(tmp65)
                    subjects66 = deque(tmp65._args)
                    matcher = CommutativeMatcher53635.get()
                    tmp67 = subjects66
                    subjects66 = []
                    for s in tmp67:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp67, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 53640
                            if len(subjects21) >= 1 and subjects21[0] == 1/2:
                                tmp68 = subjects21.popleft()
                                # State 53641
                                if len(subjects21) == 0:
                                    pass
                                    # State 53642
                                    if len(subjects) == 0:
                                        pass
                                        # 2: sqrt(a + c*x**2)
                                subjects21.appendleft(tmp68)
                    subjects21.appendleft(tmp65)
            subjects.appendleft(tmp20)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
