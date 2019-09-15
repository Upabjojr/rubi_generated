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


class CommutativeMatcher2977(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.1', 1, 1, None), Mul)
]),
    2: (2, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.3.1.1.0', 1, 1, None), Mul)
]),
    8: (8, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.4.1.1.0', 1, 1, None), Mul)
]),
    9: (9, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.4.1.1.0', 1, 1, None), Mul)
]),
    10: (10, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    11: (11, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.2.2.1.0', 1, 1, None), Mul)
]),
    12: (12, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.1.0', 1, 1, None), Mul)
]),
    13: (13, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    14: (14, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    15: (15, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    16: (16, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    17: (17, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    18: (18, Multiset({10: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    19: (19, Multiset({11: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    20: (20, Multiset({12: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    21: (21, Multiset({13: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    22: (22, Multiset({14: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    23: (23, Multiset({15: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    24: (24, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.2.1.0', 1, 1, None), Mul)
]),
    25: (25, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.1.0', 1, 1, None), Mul)
]),
    26: (26, Multiset({16: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    27: (27, Multiset({17: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    28: (28, Multiset({18: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    29: (29, Multiset({19: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    30: (30, Multiset({20: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    31: (31, Multiset({21: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    32: (32, Multiset({22: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    33: (33, Multiset({23: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    34: (34, Multiset({24: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    35: (35, Multiset({}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.3.1.0', 1, 1, None), Mul)
]),
    36: (36, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.3.1.0', 1, 1, None), Mul)
]),
    37: (37, Multiset({25: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    38: (38, Multiset({26: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    39: (39, Multiset({27: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    40: (40, Multiset({28: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    41: (41, Multiset({29: 1}), [
      (VariableWithCount('i2.2.1.0', 1, 1, S(1)), Mul)
]),
    42: (42, Multiset({30: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    43: (43, Multiset({31: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    44: (44, Multiset({}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.2.0', 1, 1, None), Mul)
]),
    45: (45, Multiset({32: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    46: (46, Multiset({33: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    47: (47, Multiset({34: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    48: (48, Multiset({35: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    49: (49, Multiset({36: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    50: (50, Multiset({37: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    51: (51, Multiset({38: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    52: (52, Multiset({39: 1}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul)
]),
    53: (53, Multiset({40: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    54: (54, Multiset({41: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    55: (55, Multiset({42: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    56: (56, Multiset({43: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    57: (57, Multiset({44: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    58: (58, Multiset({45: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    59: (59, Multiset({46: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    60: (60, Multiset({47: 1, 48: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_2', 1, 1, S(1)), Mul),
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
]),
    61: (61, Multiset({49: 1}), [
      (VariableWithCount('i2.2.1.0_1', 1, 1, S(1)), Mul)
]),
    62: (62, Multiset({}), [
      (VariableWithCount('i2.2.1.0_2', 1, 1, None), Mul),
      (VariableWithCount('i2.2.1.0_3', 1, 1, S(1)), Mul)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Mul
    max_optional_count = 2
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher2977._instance is None:
            CommutativeMatcher2977._instance = CommutativeMatcher2977()
        return CommutativeMatcher2977._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 2976
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 5581
            if len(subjects2) >= 1:
                tmp3 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1', tmp3)
                except ValueError:
                    pass
                else:
                    pass
                    # State 5582
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp5 = subjects2.popleft()
                        # State 5583
                        if len(subjects2) == 0:
                            pass
                            # State 5584
                            if len(subjects) == 0:
                                pass
                                # 0: x**2
                                yield 0, subst1
                        subjects2.appendleft(tmp5)
                    if len(subjects2) >= 1:
                        tmp6 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp6)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 6376
                            if len(subjects2) == 0:
                                pass
                                # State 6377
                                if len(subjects) == 0:
                                    pass
                                    # 1: x**j
                                    yield 1, subst2
                        subjects2.appendleft(tmp6)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2_1', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 7859
                        if len(subjects2) == 0:
                            pass
                            # State 7860
                            if len(subjects) == 0:
                                pass
                                # 3: x**n
                                yield 3, subst2
                    if len(subjects2) >= 1:
                        tmp9 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2_1', tmp9)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7859
                            if len(subjects2) == 0:
                                pass
                                # State 7860
                                if len(subjects) == 0:
                                    pass
                                    # 3: x**n
                                    yield 3, subst2
                        subjects2.appendleft(tmp9)
                subjects2.appendleft(tmp3)
            if len(subjects2) >= 1:
                tmp11 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.1_1', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7780
                    if len(subjects2) >= 1:
                        tmp13 = subjects2.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2', tmp13)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 7781
                            if len(subjects2) == 0:
                                pass
                                # State 7782
                                if len(subjects) == 0:
                                    pass
                                    # 2: v**n
                                    yield 2, subst2
                        subjects2.appendleft(tmp13)
                subjects2.appendleft(tmp11)
            if len(subjects2) >= 1:
                tmp15 = subjects2.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.2.1.0', tmp15)
                except ValueError:
                    pass
                else:
                    pass
                    # State 151464
                    if len(subjects2) >= 1 and subjects2[0] == Integer(2):
                        tmp17 = subjects2.popleft()
                        # State 151465
                        if len(subjects2) == 0:
                            pass
                            # State 151466
                            if len(subjects) == 0:
                                pass
                                # 49: x**2
                                yield 49, subst1
                        subjects2.appendleft(tmp17)
                subjects2.appendleft(tmp15)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                tmp18 = subjects2.popleft()
                subjects19 = deque(tmp18._args)
                # State 16616
                if len(subjects19) >= 1:
                    tmp20 = subjects19.popleft()
                    subst1 = Substitution(subst0)
                    try:
                        subst1.try_add_variable('i2.2.1.2', tmp20)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 16617
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 16618
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 16619
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.4.1.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 16620
                                    if len(subjects19) >= 1:
                                        tmp25 = subjects19.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.3.1.1.0', tmp25)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 16621
                                            if len(subjects19) == 0:
                                                pass
                                                # State 16622
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16623
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 16624
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (F**(g*(e + f*x)))**n
                                                            yield 4, subst6
                                                if len(subjects2) >= 1:
                                                    tmp28 = subjects2.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.4', tmp28)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 16623
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 16624
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (F**(g*(e + f*x)))**n
                                                                yield 4, subst6
                                                    subjects2.appendleft(tmp28)
                                        subjects19.appendleft(tmp25)
                                if len(subjects19) >= 1 and isinstance(subjects19[0], Mul):
                                    tmp30 = subjects19.popleft()
                                    associative1 = tmp30
                                    associative_type1 = type(tmp30)
                                    subjects31 = deque(tmp30._args)
                                    matcher = CommutativeMatcher16626.get()
                                    tmp32 = subjects31
                                    subjects31 = []
                                    for s in tmp32:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp32, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 16627
                                            if len(subjects19) == 0:
                                                pass
                                                # State 16628
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.4', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16629
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 16630
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (F**(g*(e + f*x)))**n
                                                            yield 4, subst5
                                                if len(subjects2) >= 1:
                                                    tmp34 = subjects2.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.4', tmp34)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 16629
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 16630
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (F**(g*(e + f*x)))**n
                                                                yield 4, subst5
                                                    subjects2.appendleft(tmp34)
                                    subjects19.appendleft(tmp30)
                            if len(subjects19) >= 1 and isinstance(subjects19[0], Add):
                                tmp36 = subjects19.popleft()
                                associative1 = tmp36
                                associative_type1 = type(tmp36)
                                subjects37 = deque(tmp36._args)
                                matcher = CommutativeMatcher16632.get()
                                tmp38 = subjects37
                                subjects37 = []
                                for s in tmp38:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp38, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 16638
                                        if len(subjects19) == 0:
                                            pass
                                            # State 16639
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.4', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 16640
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 16641
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (F**(g*(e + f*x)))**n
                                                        yield 4, subst4
                                            if len(subjects2) >= 1:
                                                tmp40 = subjects2.popleft()
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.4', tmp40)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 16640
                                                    if len(subjects2) == 0:
                                                        pass
                                                        # State 16641
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (F**(g*(e + f*x)))**n
                                                            yield 4, subst4
                                                subjects2.appendleft(tmp40)
                                subjects19.appendleft(tmp36)
                        if len(subjects19) >= 1 and isinstance(subjects19[0], Mul):
                            tmp42 = subjects19.popleft()
                            associative1 = tmp42
                            associative_type1 = type(tmp42)
                            subjects43 = deque(tmp42._args)
                            matcher = CommutativeMatcher16643.get()
                            tmp44 = subjects43
                            subjects43 = []
                            for s in tmp44:
                                matcher.add_subject(s)
                            for pattern_index, subst2 in matcher.match(tmp44, subst1):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 16658
                                    if len(subjects19) == 0:
                                        pass
                                        # State 16659
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.4', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 16660
                                            if len(subjects2) == 0:
                                                pass
                                                # State 16661
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (F**(g*(e + f*x)))**n
                                                    yield 4, subst3
                                        if len(subjects2) >= 1:
                                            tmp46 = subjects2.popleft()
                                            subst3 = Substitution(subst2)
                                            try:
                                                subst3.try_add_variable('i2.2.1.4', tmp46)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 16660
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 16661
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (F**(g*(e + f*x)))**n
                                                        yield 4, subst3
                                            subjects2.appendleft(tmp46)
                            subjects19.appendleft(tmp42)
                    subjects19.appendleft(tmp20)
                subjects2.appendleft(tmp18)
            if len(subjects2) >= 1 and isinstance(subjects2[0], sin):
                tmp48 = subjects2.popleft()
                subjects49 = deque(tmp48._args)
                # State 63858
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63859
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 63860
                        if len(subjects49) >= 1:
                            tmp52 = subjects49.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp52)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 63861
                                if len(subjects49) == 0:
                                    pass
                                    # State 63862
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp54 = subjects2.popleft()
                                        # State 63863
                                        if len(subjects2) == 0:
                                            pass
                                            # State 63864
                                            if len(subjects) == 0:
                                                pass
                                                # 14: 1/sin(e + x*f)
                                                yield 14, subst3
                                        subjects2.appendleft(tmp54)
                            subjects49.appendleft(tmp52)
                    if len(subjects49) >= 1 and isinstance(subjects49[0], Mul):
                        tmp55 = subjects49.popleft()
                        associative1 = tmp55
                        associative_type1 = type(tmp55)
                        subjects56 = deque(tmp55._args)
                        matcher = CommutativeMatcher63866.get()
                        tmp57 = subjects56
                        subjects56 = []
                        for s in tmp57:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp57, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 63867
                                if len(subjects49) == 0:
                                    pass
                                    # State 63868
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp58 = subjects2.popleft()
                                        # State 63869
                                        if len(subjects2) == 0:
                                            pass
                                            # State 63870
                                            if len(subjects) == 0:
                                                pass
                                                # 14: 1/sin(e + x*f)
                                                yield 14, subst2
                                        subjects2.appendleft(tmp58)
                        subjects49.appendleft(tmp55)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 91093
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91094
                        if len(subjects49) >= 1:
                            tmp61 = subjects49.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp61)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 91095
                                if len(subjects49) == 0:
                                    pass
                                    # State 91096
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp63 = subjects2.popleft()
                                        # State 91097
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91098
                                            if len(subjects) == 0:
                                                pass
                                                # 26: 1/sin(e + x*f)
                                                yield 26, subst3
                                        subjects2.appendleft(tmp63)
                            subjects49.appendleft(tmp61)
                    if len(subjects49) >= 1 and isinstance(subjects49[0], Mul):
                        tmp64 = subjects49.popleft()
                        associative1 = tmp64
                        associative_type1 = type(tmp64)
                        subjects65 = deque(tmp64._args)
                        matcher = CommutativeMatcher91100.get()
                        tmp66 = subjects65
                        subjects65 = []
                        for s in tmp66:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp66, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 91101
                                if len(subjects49) == 0:
                                    pass
                                    # State 91102
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp67 = subjects2.popleft()
                                        # State 91103
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91104
                                            if len(subjects) == 0:
                                                pass
                                                # 26: 1/sin(e + x*f)
                                                yield 26, subst2
                                        subjects2.appendleft(tmp67)
                        subjects49.appendleft(tmp64)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 92092
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 92093
                        if len(subjects49) >= 1:
                            tmp70 = subjects49.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp70)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 92094
                                if len(subjects49) == 0:
                                    pass
                                    # State 92095
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp72 = subjects2.popleft()
                                        # State 92096
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92097
                                            if len(subjects) == 0:
                                                pass
                                                # 28: 1/sin(e + x*f)
                                                yield 28, subst3
                                        subjects2.appendleft(tmp72)
                            subjects49.appendleft(tmp70)
                    if len(subjects49) >= 1 and isinstance(subjects49[0], Mul):
                        tmp73 = subjects49.popleft()
                        associative1 = tmp73
                        associative_type1 = type(tmp73)
                        subjects74 = deque(tmp73._args)
                        matcher = CommutativeMatcher92099.get()
                        tmp75 = subjects74
                        subjects74 = []
                        for s in tmp75:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp75, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 92100
                                if len(subjects49) == 0:
                                    pass
                                    # State 92101
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp76 = subjects2.popleft()
                                        # State 92102
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92103
                                            if len(subjects) == 0:
                                                pass
                                                # 28: 1/sin(e + x*f)
                                                yield 28, subst2
                                        subjects2.appendleft(tmp76)
                        subjects49.appendleft(tmp73)
                if len(subjects49) >= 1 and isinstance(subjects49[0], Add):
                    tmp77 = subjects49.popleft()
                    associative1 = tmp77
                    associative_type1 = type(tmp77)
                    subjects78 = deque(tmp77._args)
                    matcher = CommutativeMatcher63872.get()
                    tmp79 = subjects78
                    subjects78 = []
                    for s in tmp79:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp79, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63878
                            if len(subjects49) == 0:
                                pass
                                # State 63879
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp80 = subjects2.popleft()
                                    # State 63880
                                    if len(subjects2) == 0:
                                        pass
                                        # State 63881
                                        if len(subjects) == 0:
                                            pass
                                            # 14: 1/sin(e + x*f)
                                            yield 14, subst1
                                    subjects2.appendleft(tmp80)
                        if pattern_index == 1:
                            pass
                            # State 91108
                            if len(subjects49) == 0:
                                pass
                                # State 91109
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp81 = subjects2.popleft()
                                    # State 91110
                                    if len(subjects2) == 0:
                                        pass
                                        # State 91111
                                        if len(subjects) == 0:
                                            pass
                                            # 26: 1/sin(e + x*f)
                                            yield 26, subst1
                                    subjects2.appendleft(tmp81)
                        if pattern_index == 2:
                            pass
                            # State 92107
                            if len(subjects49) == 0:
                                pass
                                # State 92108
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp82 = subjects2.popleft()
                                    # State 92109
                                    if len(subjects2) == 0:
                                        pass
                                        # State 92110
                                        if len(subjects) == 0:
                                            pass
                                            # 28: 1/sin(e + x*f)
                                            yield 28, subst1
                                    subjects2.appendleft(tmp82)
                    subjects49.appendleft(tmp77)
                subjects2.appendleft(tmp48)
            if len(subjects2) >= 1 and isinstance(subjects2[0], cos):
                tmp83 = subjects2.popleft()
                subjects84 = deque(tmp83._args)
                # State 64137
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 64138
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 64139
                        if len(subjects84) >= 1:
                            tmp87 = subjects84.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp87)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 64140
                                if len(subjects84) == 0:
                                    pass
                                    # State 64141
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp89 = subjects2.popleft()
                                        # State 64142
                                        if len(subjects2) == 0:
                                            pass
                                            # State 64143
                                            if len(subjects) == 0:
                                                pass
                                                # 15: 1/cos(e + x*f)
                                                yield 15, subst3
                                        subjects2.appendleft(tmp89)
                            subjects84.appendleft(tmp87)
                    if len(subjects84) >= 1 and isinstance(subjects84[0], Mul):
                        tmp90 = subjects84.popleft()
                        associative1 = tmp90
                        associative_type1 = type(tmp90)
                        subjects91 = deque(tmp90._args)
                        matcher = CommutativeMatcher64145.get()
                        tmp92 = subjects91
                        subjects91 = []
                        for s in tmp92:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp92, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 64146
                                if len(subjects84) == 0:
                                    pass
                                    # State 64147
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp93 = subjects2.popleft()
                                        # State 64148
                                        if len(subjects2) == 0:
                                            pass
                                            # State 64149
                                            if len(subjects) == 0:
                                                pass
                                                # 15: 1/cos(e + x*f)
                                                yield 15, subst2
                                        subjects2.appendleft(tmp93)
                        subjects84.appendleft(tmp90)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 91911
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 91912
                        if len(subjects84) >= 1:
                            tmp96 = subjects84.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp96)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 91913
                                if len(subjects84) == 0:
                                    pass
                                    # State 91914
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp98 = subjects2.popleft()
                                        # State 91915
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91916
                                            if len(subjects) == 0:
                                                pass
                                                # 27: 1/cos(e + x*f)
                                                yield 27, subst3
                                        subjects2.appendleft(tmp98)
                            subjects84.appendleft(tmp96)
                    if len(subjects84) >= 1 and isinstance(subjects84[0], Mul):
                        tmp99 = subjects84.popleft()
                        associative1 = tmp99
                        associative_type1 = type(tmp99)
                        subjects100 = deque(tmp99._args)
                        matcher = CommutativeMatcher91918.get()
                        tmp101 = subjects100
                        subjects100 = []
                        for s in tmp101:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp101, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 91919
                                if len(subjects84) == 0:
                                    pass
                                    # State 91920
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp102 = subjects2.popleft()
                                        # State 91921
                                        if len(subjects2) == 0:
                                            pass
                                            # State 91922
                                            if len(subjects) == 0:
                                                pass
                                                # 27: 1/cos(e + x*f)
                                                yield 27, subst2
                                        subjects2.appendleft(tmp102)
                        subjects84.appendleft(tmp99)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 92602
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 92603
                        if len(subjects84) >= 1:
                            tmp105 = subjects84.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp105)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 92604
                                if len(subjects84) == 0:
                                    pass
                                    # State 92605
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp107 = subjects2.popleft()
                                        # State 92606
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92607
                                            if len(subjects) == 0:
                                                pass
                                                # 29: 1/cos(e + x*f)
                                                yield 29, subst3
                                        subjects2.appendleft(tmp107)
                            subjects84.appendleft(tmp105)
                    if len(subjects84) >= 1 and isinstance(subjects84[0], Mul):
                        tmp108 = subjects84.popleft()
                        associative1 = tmp108
                        associative_type1 = type(tmp108)
                        subjects109 = deque(tmp108._args)
                        matcher = CommutativeMatcher92609.get()
                        tmp110 = subjects109
                        subjects109 = []
                        for s in tmp110:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp110, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 92610
                                if len(subjects84) == 0:
                                    pass
                                    # State 92611
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp111 = subjects2.popleft()
                                        # State 92612
                                        if len(subjects2) == 0:
                                            pass
                                            # State 92613
                                            if len(subjects) == 0:
                                                pass
                                                # 29: 1/cos(e + x*f)
                                                yield 29, subst2
                                        subjects2.appendleft(tmp111)
                        subjects84.appendleft(tmp108)
                if len(subjects84) >= 1 and isinstance(subjects84[0], Add):
                    tmp112 = subjects84.popleft()
                    associative1 = tmp112
                    associative_type1 = type(tmp112)
                    subjects113 = deque(tmp112._args)
                    matcher = CommutativeMatcher64151.get()
                    tmp114 = subjects113
                    subjects113 = []
                    for s in tmp114:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp114, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 64157
                            if len(subjects84) == 0:
                                pass
                                # State 64158
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp115 = subjects2.popleft()
                                    # State 64159
                                    if len(subjects2) == 0:
                                        pass
                                        # State 64160
                                        if len(subjects) == 0:
                                            pass
                                            # 15: 1/cos(e + x*f)
                                            yield 15, subst1
                                    subjects2.appendleft(tmp115)
                        if pattern_index == 1:
                            pass
                            # State 91926
                            if len(subjects84) == 0:
                                pass
                                # State 91927
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp116 = subjects2.popleft()
                                    # State 91928
                                    if len(subjects2) == 0:
                                        pass
                                        # State 91929
                                        if len(subjects) == 0:
                                            pass
                                            # 27: 1/cos(e + x*f)
                                            yield 27, subst1
                                    subjects2.appendleft(tmp116)
                        if pattern_index == 2:
                            pass
                            # State 92617
                            if len(subjects84) == 0:
                                pass
                                # State 92618
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp117 = subjects2.popleft()
                                    # State 92619
                                    if len(subjects2) == 0:
                                        pass
                                        # State 92620
                                        if len(subjects) == 0:
                                            pass
                                            # 29: 1/cos(e + x*f)
                                            yield 29, subst1
                                    subjects2.appendleft(tmp117)
                    subjects84.appendleft(tmp112)
                subjects2.appendleft(tmp83)
            if len(subjects2) >= 1 and isinstance(subjects2[0], tan):
                tmp118 = subjects2.popleft()
                subjects119 = deque(tmp118._args)
                # State 78597
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78598
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 78599
                        if len(subjects119) >= 1:
                            tmp122 = subjects119.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.3.1.0', tmp122)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 78600
                                if len(subjects119) == 0:
                                    pass
                                    # State 78601
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp124 = subjects2.popleft()
                                        # State 78602
                                        if len(subjects2) == 0:
                                            pass
                                            # State 78603
                                            if len(subjects) == 0:
                                                pass
                                                # 18: 1/tan(e + x*f)
                                                yield 18, subst3
                                        subjects2.appendleft(tmp124)
                            subjects119.appendleft(tmp122)
                    if len(subjects119) >= 1 and isinstance(subjects119[0], Mul):
                        tmp125 = subjects119.popleft()
                        associative1 = tmp125
                        associative_type1 = type(tmp125)
                        subjects126 = deque(tmp125._args)
                        matcher = CommutativeMatcher78605.get()
                        tmp127 = subjects126
                        subjects126 = []
                        for s in tmp127:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp127, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 78606
                                if len(subjects119) == 0:
                                    pass
                                    # State 78607
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp128 = subjects2.popleft()
                                        # State 78608
                                        if len(subjects2) == 0:
                                            pass
                                            # State 78609
                                            if len(subjects) == 0:
                                                pass
                                                # 18: 1/tan(e + x*f)
                                                yield 18, subst2
                                        subjects2.appendleft(tmp128)
                        subjects119.appendleft(tmp125)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 79457
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 79458
                        if len(subjects119) >= 1:
                            tmp131 = subjects119.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.3.1.0', tmp131)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 79459
                                if len(subjects119) == 0:
                                    pass
                                    # State 79460
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp133 = subjects2.popleft()
                                        # State 79461
                                        if len(subjects2) == 0:
                                            pass
                                            # State 79462
                                            if len(subjects) == 0:
                                                pass
                                                # 20: 1/tan(e + x*f)
                                                yield 20, subst3
                                        subjects2.appendleft(tmp133)
                            subjects119.appendleft(tmp131)
                    if len(subjects119) >= 1 and isinstance(subjects119[0], Mul):
                        tmp134 = subjects119.popleft()
                        associative1 = tmp134
                        associative_type1 = type(tmp134)
                        subjects135 = deque(tmp134._args)
                        matcher = CommutativeMatcher79464.get()
                        tmp136 = subjects135
                        subjects135 = []
                        for s in tmp136:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp136, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 79465
                                if len(subjects119) == 0:
                                    pass
                                    # State 79466
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp137 = subjects2.popleft()
                                        # State 79467
                                        if len(subjects2) == 0:
                                            pass
                                            # State 79468
                                            if len(subjects) == 0:
                                                pass
                                                # 20: 1/tan(e + x*f)
                                                yield 20, subst2
                                        subjects2.appendleft(tmp137)
                        subjects119.appendleft(tmp134)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 79911
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 79912
                        if len(subjects119) >= 1:
                            tmp140 = subjects119.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.1.0', tmp140)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 79913
                                if len(subjects119) == 0:
                                    pass
                                    # State 79914
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp142 = subjects2.popleft()
                                        # State 79915
                                        if len(subjects2) == 0:
                                            pass
                                            # State 79916
                                            if len(subjects) == 0:
                                                pass
                                                # 21: 1/tan(e + x*f)
                                                yield 21, subst3
                                        subjects2.appendleft(tmp142)
                            subjects119.appendleft(tmp140)
                    if len(subjects119) >= 1 and isinstance(subjects119[0], Mul):
                        tmp143 = subjects119.popleft()
                        associative1 = tmp143
                        associative_type1 = type(tmp143)
                        subjects144 = deque(tmp143._args)
                        matcher = CommutativeMatcher79918.get()
                        tmp145 = subjects144
                        subjects144 = []
                        for s in tmp145:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp145, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 79919
                                if len(subjects119) == 0:
                                    pass
                                    # State 79920
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp146 = subjects2.popleft()
                                        # State 79921
                                        if len(subjects2) == 0:
                                            pass
                                            # State 79922
                                            if len(subjects) == 0:
                                                pass
                                                # 21: 1/tan(e + x*f)
                                                yield 21, subst2
                                        subjects2.appendleft(tmp146)
                        subjects119.appendleft(tmp143)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.2.3.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80392
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.2.3.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80393
                        if len(subjects119) >= 1:
                            tmp149 = subjects119.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.3.1.0', tmp149)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80394
                                if len(subjects119) == 0:
                                    pass
                                    # State 80395
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp151 = subjects2.popleft()
                                        # State 80396
                                        if len(subjects2) == 0:
                                            pass
                                            # State 80397
                                            if len(subjects) == 0:
                                                pass
                                                # 23: 1/tan(e + x*f)
                                                yield 23, subst3
                                        subjects2.appendleft(tmp151)
                            subjects119.appendleft(tmp149)
                    if len(subjects119) >= 1 and isinstance(subjects119[0], Mul):
                        tmp152 = subjects119.popleft()
                        associative1 = tmp152
                        associative_type1 = type(tmp152)
                        subjects153 = deque(tmp152._args)
                        matcher = CommutativeMatcher80399.get()
                        tmp154 = subjects153
                        subjects153 = []
                        for s in tmp154:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp154, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80400
                                if len(subjects119) == 0:
                                    pass
                                    # State 80401
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp155 = subjects2.popleft()
                                        # State 80402
                                        if len(subjects2) == 0:
                                            pass
                                            # State 80403
                                            if len(subjects) == 0:
                                                pass
                                                # 23: 1/tan(e + x*f)
                                                yield 23, subst2
                                        subjects2.appendleft(tmp155)
                        subjects119.appendleft(tmp152)
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.4.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80840
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.4.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 80841
                        if len(subjects119) >= 1:
                            tmp158 = subjects119.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.4.1.0', tmp158)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 80842
                                if len(subjects119) == 0:
                                    pass
                                    # State 80843
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp160 = subjects2.popleft()
                                        # State 80844
                                        if len(subjects2) == 0:
                                            pass
                                            # State 80845
                                            if len(subjects) == 0:
                                                pass
                                                # 24: 1/tan(e + x*f)
                                                yield 24, subst3
                                        subjects2.appendleft(tmp160)
                            subjects119.appendleft(tmp158)
                    if len(subjects119) >= 1 and isinstance(subjects119[0], Mul):
                        tmp161 = subjects119.popleft()
                        associative1 = tmp161
                        associative_type1 = type(tmp161)
                        subjects162 = deque(tmp161._args)
                        matcher = CommutativeMatcher80847.get()
                        tmp163 = subjects162
                        subjects162 = []
                        for s in tmp163:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp163, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 80848
                                if len(subjects119) == 0:
                                    pass
                                    # State 80849
                                    if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                        tmp164 = subjects2.popleft()
                                        # State 80850
                                        if len(subjects2) == 0:
                                            pass
                                            # State 80851
                                            if len(subjects) == 0:
                                                pass
                                                # 24: 1/tan(e + x*f)
                                                yield 24, subst2
                                        subjects2.appendleft(tmp164)
                        subjects119.appendleft(tmp161)
                if len(subjects119) >= 1 and isinstance(subjects119[0], Add):
                    tmp165 = subjects119.popleft()
                    associative1 = tmp165
                    associative_type1 = type(tmp165)
                    subjects166 = deque(tmp165._args)
                    matcher = CommutativeMatcher78611.get()
                    tmp167 = subjects166
                    subjects166 = []
                    for s in tmp167:
                        matcher.add_subject(s)
                    for pattern_index, subst1 in matcher.match(tmp167, subst0):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 78617
                            if len(subjects119) == 0:
                                pass
                                # State 78618
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp168 = subjects2.popleft()
                                    # State 78619
                                    if len(subjects2) == 0:
                                        pass
                                        # State 78620
                                        if len(subjects) == 0:
                                            pass
                                            # 18: 1/tan(e + x*f)
                                            yield 18, subst1
                                    subjects2.appendleft(tmp168)
                        if pattern_index == 1:
                            pass
                            # State 79472
                            if len(subjects119) == 0:
                                pass
                                # State 79473
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp169 = subjects2.popleft()
                                    # State 79474
                                    if len(subjects2) == 0:
                                        pass
                                        # State 79475
                                        if len(subjects) == 0:
                                            pass
                                            # 20: 1/tan(e + x*f)
                                            yield 20, subst1
                                    subjects2.appendleft(tmp169)
                        if pattern_index == 2:
                            pass
                            # State 79926
                            if len(subjects119) == 0:
                                pass
                                # State 79927
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp170 = subjects2.popleft()
                                    # State 79928
                                    if len(subjects2) == 0:
                                        pass
                                        # State 79929
                                        if len(subjects) == 0:
                                            pass
                                            # 21: 1/tan(e + x*f)
                                            yield 21, subst1
                                    subjects2.appendleft(tmp170)
                        if pattern_index == 3:
                            pass
                            # State 80407
                            if len(subjects119) == 0:
                                pass
                                # State 80408
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp171 = subjects2.popleft()
                                    # State 80409
                                    if len(subjects2) == 0:
                                        pass
                                        # State 80410
                                        if len(subjects) == 0:
                                            pass
                                            # 23: 1/tan(e + x*f)
                                            yield 23, subst1
                                    subjects2.appendleft(tmp171)
                        if pattern_index == 4:
                            pass
                            # State 80855
                            if len(subjects119) == 0:
                                pass
                                # State 80856
                                if len(subjects2) >= 1 and subjects2[0] == Integer(-1):
                                    tmp172 = subjects2.popleft()
                                    # State 80857
                                    if len(subjects2) == 0:
                                        pass
                                        # State 80858
                                        if len(subjects) == 0:
                                            pass
                                            # 24: 1/tan(e + x*f)
                                            yield 24, subst1
                                    subjects2.appendleft(tmp172)
                    subjects119.appendleft(tmp165)
                subjects2.appendleft(tmp118)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp173 = subjects2.popleft()
                associative1 = tmp173
                associative_type1 = type(tmp173)
                subjects174 = deque(tmp173._args)
                matcher = CommutativeMatcher150991.get()
                tmp175 = subjects174
                subjects174 = []
                for s in tmp175:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp175, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 150998
                        if len(subjects2) >= 1 and subjects2[0] == Rational(1, 2):
                            tmp176 = subjects2.popleft()
                            # State 150999
                            if len(subjects2) == 0:
                                pass
                                # State 151000
                                if len(subjects) == 0:
                                    pass
                                    # 47: sqrt(x*e + 1)
                                    yield 47, subst1
                            subjects2.appendleft(tmp176)
                    if pattern_index == 1:
                        pass
                        # State 151004
                        if len(subjects2) >= 1 and subjects2[0] == Rational(-1, 2):
                            tmp177 = subjects2.popleft()
                            # State 151005
                            if len(subjects2) == 0:
                                pass
                                # State 151006
                                if len(subjects) == 0:
                                    pass
                                    # 48: 1/sqrt(x*g + 1)
                                    yield 48, subst1
                            subjects2.appendleft(tmp177)
                subjects2.appendleft(tmp173)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 7857
            if len(subjects) >= 1:
                tmp179 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.1', tmp179)
                except ValueError:
                    pass
                else:
                    pass
                    # State 7858
                    if len(subjects) == 0:
                        pass
                        # 3: x**n
                        yield 3, subst2
                subjects.appendleft(tmp179)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 16577
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp182 = subjects.popleft()
                subjects183 = deque(tmp182._args)
                # State 16578
                if len(subjects183) >= 1:
                    tmp184 = subjects183.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2', tmp184)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 16579
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.4.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 16580
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.4.1.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 16581
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.4.1.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 16582
                                    if len(subjects183) >= 1:
                                        tmp189 = subjects183.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.3.1.1.0', tmp189)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 16583
                                            if len(subjects183) == 0:
                                                pass
                                                # State 16584
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (F**(g*(e + f*x)))**n
                                                    yield 4, subst6
                                        subjects183.appendleft(tmp189)
                                if len(subjects183) >= 1 and isinstance(subjects183[0], Mul):
                                    tmp191 = subjects183.popleft()
                                    associative1 = tmp191
                                    associative_type1 = type(tmp191)
                                    subjects192 = deque(tmp191._args)
                                    matcher = CommutativeMatcher16586.get()
                                    tmp193 = subjects192
                                    subjects192 = []
                                    for s in tmp193:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp193, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 16587
                                            if len(subjects183) == 0:
                                                pass
                                                # State 16588
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (F**(g*(e + f*x)))**n
                                                    yield 4, subst5
                                    subjects183.appendleft(tmp191)
                            if len(subjects183) >= 1 and isinstance(subjects183[0], Add):
                                tmp194 = subjects183.popleft()
                                associative1 = tmp194
                                associative_type1 = type(tmp194)
                                subjects195 = deque(tmp194._args)
                                matcher = CommutativeMatcher16590.get()
                                tmp196 = subjects195
                                subjects195 = []
                                for s in tmp196:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp196, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 16596
                                        if len(subjects183) == 0:
                                            pass
                                            # State 16597
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (F**(g*(e + f*x)))**n
                                                yield 4, subst4
                                subjects183.appendleft(tmp194)
                        if len(subjects183) >= 1 and isinstance(subjects183[0], Mul):
                            tmp197 = subjects183.popleft()
                            associative1 = tmp197
                            associative_type1 = type(tmp197)
                            subjects198 = deque(tmp197._args)
                            matcher = CommutativeMatcher16599.get()
                            tmp199 = subjects198
                            subjects198 = []
                            for s in tmp199:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp199, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 16614
                                    if len(subjects183) == 0:
                                        pass
                                        # State 16615
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (F**(g*(e + f*x)))**n
                                            yield 4, subst3
                            subjects183.appendleft(tmp197)
                    subjects183.appendleft(tmp184)
                subjects.appendleft(tmp182)
        if len(subjects) >= 1 and isinstance(subjects[0], log):
            tmp200 = subjects.popleft()
            subjects201 = deque(tmp200._args)
            # State 38891
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 38892
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 38893
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 38894
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 38895
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 38896
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 38897
                                    if len(subjects201) >= 1 and isinstance(subjects201[0], Pow):
                                        tmp208 = subjects201.popleft()
                                        subjects209 = deque(tmp208._args)
                                        # State 38898
                                        if len(subjects209) >= 1:
                                            tmp210 = subjects209.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.1', tmp210)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 38899
                                                if len(subjects209) >= 1:
                                                    tmp212 = subjects209.popleft()
                                                    subst8 = Substitution(subst7)
                                                    try:
                                                        subst8.try_add_variable('i2.2.1.2', tmp212)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 38900
                                                        if len(subjects209) == 0:
                                                            pass
                                                            # State 38901
                                                            if len(subjects201) == 0:
                                                                pass
                                                                # State 38902
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                    yield 5, subst8
                                                    subjects209.appendleft(tmp212)
                                            subjects209.appendleft(tmp210)
                                        subjects201.appendleft(tmp208)
                                if len(subjects201) >= 1 and isinstance(subjects201[0], Mul):
                                    tmp214 = subjects201.popleft()
                                    associative1 = tmp214
                                    associative_type1 = type(tmp214)
                                    subjects215 = deque(tmp214._args)
                                    matcher = CommutativeMatcher38904.get()
                                    tmp216 = subjects215
                                    subjects215 = []
                                    for s in tmp216:
                                        matcher.add_subject(s)
                                    for pattern_index, subst6 in matcher.match(tmp216, subst5):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 38909
                                            if len(subjects201) == 0:
                                                pass
                                                # State 38910
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                    yield 5, subst6
                                    subjects201.appendleft(tmp214)
                            if len(subjects201) >= 1 and isinstance(subjects201[0], Add):
                                tmp217 = subjects201.popleft()
                                associative1 = tmp217
                                associative_type1 = type(tmp217)
                                subjects218 = deque(tmp217._args)
                                matcher = CommutativeMatcher38912.get()
                                tmp219 = subjects218
                                subjects218 = []
                                for s in tmp219:
                                    matcher.add_subject(s)
                                for pattern_index, subst5 in matcher.match(tmp219, subst4):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 38925
                                        if len(subjects201) == 0:
                                            pass
                                            # State 38926
                                            if len(subjects) == 0:
                                                pass
                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                yield 5, subst5
                                subjects201.appendleft(tmp217)
                        if len(subjects201) >= 1 and isinstance(subjects201[0], Pow):
                            tmp220 = subjects201.popleft()
                            subjects221 = deque(tmp220._args)
                            # State 38927
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 38928
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 38929
                                    if len(subjects221) >= 1 and isinstance(subjects221[0], Pow):
                                        tmp224 = subjects221.popleft()
                                        subjects225 = deque(tmp224._args)
                                        # State 38930
                                        if len(subjects225) >= 1:
                                            tmp226 = subjects225.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.1', tmp226)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 38931
                                                if len(subjects225) >= 1:
                                                    tmp228 = subjects225.popleft()
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2', tmp228)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 38932
                                                        if len(subjects225) == 0:
                                                            pass
                                                            # State 38933
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i2.2.1.2.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 38934
                                                                if len(subjects221) == 0:
                                                                    pass
                                                                    # State 38935
                                                                    if len(subjects201) == 0:
                                                                        pass
                                                                        # State 38936
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                            yield 5, subst8
                                                            if len(subjects221) >= 1:
                                                                tmp231 = subjects221.popleft()
                                                                subst8 = Substitution(subst7)
                                                                try:
                                                                    subst8.try_add_variable('i2.2.1.2.2.2', tmp231)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 38934
                                                                    if len(subjects221) == 0:
                                                                        pass
                                                                        # State 38935
                                                                        if len(subjects201) == 0:
                                                                            pass
                                                                            # State 38936
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                                yield 5, subst8
                                                                subjects221.appendleft(tmp231)
                                                    subjects225.appendleft(tmp228)
                                            subjects225.appendleft(tmp226)
                                        subjects221.appendleft(tmp224)
                                if len(subjects221) >= 1 and isinstance(subjects221[0], Mul):
                                    tmp233 = subjects221.popleft()
                                    associative1 = tmp233
                                    associative_type1 = type(tmp233)
                                    subjects234 = deque(tmp233._args)
                                    matcher = CommutativeMatcher38938.get()
                                    tmp235 = subjects234
                                    subjects234 = []
                                    for s in tmp235:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp235, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 38943
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 38944
                                                if len(subjects221) == 0:
                                                    pass
                                                    # State 38945
                                                    if len(subjects201) == 0:
                                                        pass
                                                        # State 38946
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                            yield 5, subst6
                                            if len(subjects221) >= 1:
                                                tmp237 = []
                                                tmp237.append(subjects221.popleft())
                                                while True:
                                                    if len(tmp237) > 1:
                                                        tmp238 = create_operation_expression(associative1, tmp237)
                                                    elif len(tmp237) == 1:
                                                        tmp238 = tmp237[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', tmp238)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 38944
                                                        if len(subjects221) == 0:
                                                            pass
                                                            # State 38945
                                                            if len(subjects201) == 0:
                                                                pass
                                                                # State 38946
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                    yield 5, subst6
                                                    if len(subjects221) == 0:
                                                        break
                                                    tmp237.append(subjects221.popleft())
                                                subjects221.extendleft(reversed(tmp237))
                                    subjects221.appendleft(tmp233)
                            if len(subjects221) >= 1 and isinstance(subjects221[0], Add):
                                tmp240 = subjects221.popleft()
                                associative1 = tmp240
                                associative_type1 = type(tmp240)
                                subjects241 = deque(tmp240._args)
                                matcher = CommutativeMatcher38948.get()
                                tmp242 = subjects241
                                subjects241 = []
                                for s in tmp242:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp242, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 38961
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 38962
                                            if len(subjects221) == 0:
                                                pass
                                                # State 38963
                                                if len(subjects201) == 0:
                                                    pass
                                                    # State 38964
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                        yield 5, subst5
                                        if len(subjects221) >= 1:
                                            tmp244 = []
                                            tmp244.append(subjects221.popleft())
                                            while True:
                                                if len(tmp244) > 1:
                                                    tmp245 = create_operation_expression(associative1, tmp244)
                                                elif len(tmp244) == 1:
                                                    tmp245 = tmp244[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp245)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 38962
                                                    if len(subjects221) == 0:
                                                        pass
                                                        # State 38963
                                                        if len(subjects201) == 0:
                                                            pass
                                                            # State 38964
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                yield 5, subst5
                                                if len(subjects221) == 0:
                                                    break
                                                tmp244.append(subjects221.popleft())
                                            subjects221.extendleft(reversed(tmp244))
                                subjects221.appendleft(tmp240)
                            subjects201.appendleft(tmp220)
                    if len(subjects201) >= 1 and isinstance(subjects201[0], Mul):
                        tmp247 = subjects201.popleft()
                        associative1 = tmp247
                        associative_type1 = type(tmp247)
                        subjects248 = deque(tmp247._args)
                        matcher = CommutativeMatcher38966.get()
                        tmp249 = subjects248
                        subjects248 = []
                        for s in tmp249:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp249, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 39031
                                if len(subjects201) == 0:
                                    pass
                                    # State 39032
                                    if len(subjects) == 0:
                                        pass
                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                        yield 5, subst3
                        subjects201.appendleft(tmp247)
                if len(subjects201) >= 1 and isinstance(subjects201[0], Pow):
                    tmp250 = subjects201.popleft()
                    subjects251 = deque(tmp250._args)
                    # State 39033
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 39034
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 39035
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 39036
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 39037
                                    if len(subjects251) >= 1 and isinstance(subjects251[0], Pow):
                                        tmp256 = subjects251.popleft()
                                        subjects257 = deque(tmp256._args)
                                        # State 39038
                                        if len(subjects257) >= 1:
                                            tmp258 = subjects257.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.1', tmp258)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 39039
                                                if len(subjects257) >= 1:
                                                    tmp260 = subjects257.popleft()
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2', tmp260)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 39040
                                                        if len(subjects257) == 0:
                                                            pass
                                                            # State 39041
                                                            subst8 = Substitution(subst7)
                                                            try:
                                                                subst8.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 39042
                                                                if len(subjects251) == 0:
                                                                    pass
                                                                    # State 39043
                                                                    if len(subjects201) == 0:
                                                                        pass
                                                                        # State 39044
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                            yield 5, subst8
                                                            if len(subjects251) >= 1:
                                                                tmp263 = subjects251.popleft()
                                                                subst8 = Substitution(subst7)
                                                                try:
                                                                    subst8.try_add_variable('i2.2.1.2.2', tmp263)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 39042
                                                                    if len(subjects251) == 0:
                                                                        pass
                                                                        # State 39043
                                                                        if len(subjects201) == 0:
                                                                            pass
                                                                            # State 39044
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                                yield 5, subst8
                                                                subjects251.appendleft(tmp263)
                                                    subjects257.appendleft(tmp260)
                                            subjects257.appendleft(tmp258)
                                        subjects251.appendleft(tmp256)
                                if len(subjects251) >= 1 and isinstance(subjects251[0], Mul):
                                    tmp265 = subjects251.popleft()
                                    associative1 = tmp265
                                    associative_type1 = type(tmp265)
                                    subjects266 = deque(tmp265._args)
                                    matcher = CommutativeMatcher39046.get()
                                    tmp267 = subjects266
                                    subjects266 = []
                                    for s in tmp267:
                                        matcher.add_subject(s)
                                    for pattern_index, subst5 in matcher.match(tmp267, subst4):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 39051
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 39052
                                                if len(subjects251) == 0:
                                                    pass
                                                    # State 39053
                                                    if len(subjects201) == 0:
                                                        pass
                                                        # State 39054
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                            yield 5, subst6
                                            if len(subjects251) >= 1:
                                                tmp269 = []
                                                tmp269.append(subjects251.popleft())
                                                while True:
                                                    if len(tmp269) > 1:
                                                        tmp270 = create_operation_expression(associative1, tmp269)
                                                    elif len(tmp269) == 1:
                                                        tmp270 = tmp269[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp270)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 39052
                                                        if len(subjects251) == 0:
                                                            pass
                                                            # State 39053
                                                            if len(subjects201) == 0:
                                                                pass
                                                                # State 39054
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                    yield 5, subst6
                                                    if len(subjects251) == 0:
                                                        break
                                                    tmp269.append(subjects251.popleft())
                                                subjects251.extendleft(reversed(tmp269))
                                    subjects251.appendleft(tmp265)
                            if len(subjects251) >= 1 and isinstance(subjects251[0], Add):
                                tmp272 = subjects251.popleft()
                                associative1 = tmp272
                                associative_type1 = type(tmp272)
                                subjects273 = deque(tmp272._args)
                                matcher = CommutativeMatcher39056.get()
                                tmp274 = subjects273
                                subjects273 = []
                                for s in tmp274:
                                    matcher.add_subject(s)
                                for pattern_index, subst4 in matcher.match(tmp274, subst3):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 39069
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 39070
                                            if len(subjects251) == 0:
                                                pass
                                                # State 39071
                                                if len(subjects201) == 0:
                                                    pass
                                                    # State 39072
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                        yield 5, subst5
                                        if len(subjects251) >= 1:
                                            tmp276 = []
                                            tmp276.append(subjects251.popleft())
                                            while True:
                                                if len(tmp276) > 1:
                                                    tmp277 = create_operation_expression(associative1, tmp276)
                                                elif len(tmp276) == 1:
                                                    tmp277 = tmp276[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp277)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 39070
                                                    if len(subjects251) == 0:
                                                        pass
                                                        # State 39071
                                                        if len(subjects201) == 0:
                                                            pass
                                                            # State 39072
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                yield 5, subst5
                                                if len(subjects251) == 0:
                                                    break
                                                tmp276.append(subjects251.popleft())
                                            subjects251.extendleft(reversed(tmp276))
                                subjects251.appendleft(tmp272)
                        if len(subjects251) >= 1 and isinstance(subjects251[0], Pow):
                            tmp279 = subjects251.popleft()
                            subjects280 = deque(tmp279._args)
                            # State 39073
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 39074
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 39075
                                    if len(subjects280) >= 1 and isinstance(subjects280[0], Pow):
                                        tmp283 = subjects280.popleft()
                                        subjects284 = deque(tmp283._args)
                                        # State 39076
                                        if len(subjects284) >= 1:
                                            tmp285 = subjects284.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.1', tmp285)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 39077
                                                if len(subjects284) >= 1:
                                                    tmp287 = subjects284.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2', tmp287)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 39078
                                                        if len(subjects284) == 0:
                                                            pass
                                                            # State 39079
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 39080
                                                                if len(subjects280) == 0:
                                                                    pass
                                                                    # State 39081
                                                                    subst8 = Substitution(subst7)
                                                                    try:
                                                                        subst8.try_add_variable('i2.2.1.2.2', 1)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 39082
                                                                        if len(subjects251) == 0:
                                                                            pass
                                                                            # State 39083
                                                                            if len(subjects201) == 0:
                                                                                pass
                                                                                # State 39084
                                                                                if len(subjects) == 0:
                                                                                    pass
                                                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                                    yield 5, subst8
                                                                    if len(subjects251) >= 1:
                                                                        tmp291 = subjects251.popleft()
                                                                        subst8 = Substitution(subst7)
                                                                        try:
                                                                            subst8.try_add_variable('i2.2.1.2.2', tmp291)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            # State 39082
                                                                            if len(subjects251) == 0:
                                                                                pass
                                                                                # State 39083
                                                                                if len(subjects201) == 0:
                                                                                    pass
                                                                                    # State 39084
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                                        yield 5, subst8
                                                                        subjects251.appendleft(tmp291)
                                                            if len(subjects280) >= 1:
                                                                tmp293 = subjects280.popleft()
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2.2', tmp293)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 39080
                                                                    if len(subjects280) == 0:
                                                                        pass
                                                                        # State 39081
                                                                        subst8 = Substitution(subst7)
                                                                        try:
                                                                            subst8.try_add_variable('i2.2.1.2.2', 1)
                                                                        except ValueError:
                                                                            pass
                                                                        else:
                                                                            pass
                                                                            # State 39082
                                                                            if len(subjects251) == 0:
                                                                                pass
                                                                                # State 39083
                                                                                if len(subjects201) == 0:
                                                                                    pass
                                                                                    # State 39084
                                                                                    if len(subjects) == 0:
                                                                                        pass
                                                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                                        yield 5, subst8
                                                                        if len(subjects251) >= 1:
                                                                            tmp296 = subjects251.popleft()
                                                                            subst8 = Substitution(subst7)
                                                                            try:
                                                                                subst8.try_add_variable('i2.2.1.2.2', tmp296)
                                                                            except ValueError:
                                                                                pass
                                                                            else:
                                                                                pass
                                                                                # State 39082
                                                                                if len(subjects251) == 0:
                                                                                    pass
                                                                                    # State 39083
                                                                                    if len(subjects201) == 0:
                                                                                        pass
                                                                                        # State 39084
                                                                                        if len(subjects) == 0:
                                                                                            pass
                                                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                                            yield 5, subst8
                                                                            subjects251.appendleft(tmp296)
                                                                subjects280.appendleft(tmp293)
                                                    subjects284.appendleft(tmp287)
                                            subjects284.appendleft(tmp285)
                                        subjects280.appendleft(tmp283)
                                if len(subjects280) >= 1 and isinstance(subjects280[0], Mul):
                                    tmp298 = subjects280.popleft()
                                    associative1 = tmp298
                                    associative_type1 = type(tmp298)
                                    subjects299 = deque(tmp298._args)
                                    matcher = CommutativeMatcher39086.get()
                                    tmp300 = subjects299
                                    subjects299 = []
                                    for s in tmp300:
                                        matcher.add_subject(s)
                                    for pattern_index, subst4 in matcher.match(tmp300, subst3):
                                        pass
                                        if pattern_index == 0:
                                            pass
                                            # State 39091
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 39092
                                                if len(subjects280) == 0:
                                                    pass
                                                    # State 39093
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 39094
                                                        if len(subjects251) == 0:
                                                            pass
                                                            # State 39095
                                                            if len(subjects201) == 0:
                                                                pass
                                                                # State 39096
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                    yield 5, subst6
                                                    if len(subjects251) >= 1:
                                                        tmp303 = subjects251.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2', tmp303)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 39094
                                                            if len(subjects251) == 0:
                                                                pass
                                                                # State 39095
                                                                if len(subjects201) == 0:
                                                                    pass
                                                                    # State 39096
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                        yield 5, subst6
                                                        subjects251.appendleft(tmp303)
                                            if len(subjects280) >= 1:
                                                tmp305 = []
                                                tmp305.append(subjects280.popleft())
                                                while True:
                                                    if len(tmp305) > 1:
                                                        tmp306 = create_operation_expression(associative1, tmp305)
                                                    elif len(tmp305) == 1:
                                                        tmp306 = tmp305[0]
                                                    else:
                                                        assert False, "Unreachable"
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2.2', tmp306)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 39092
                                                        if len(subjects280) == 0:
                                                            pass
                                                            # State 39093
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 39094
                                                                if len(subjects251) == 0:
                                                                    pass
                                                                    # State 39095
                                                                    if len(subjects201) == 0:
                                                                        pass
                                                                        # State 39096
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                            yield 5, subst6
                                                            if len(subjects251) >= 1:
                                                                tmp309 = subjects251.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i2.2.1.2.2', tmp309)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 39094
                                                                    if len(subjects251) == 0:
                                                                        pass
                                                                        # State 39095
                                                                        if len(subjects201) == 0:
                                                                            pass
                                                                            # State 39096
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                                yield 5, subst6
                                                                subjects251.appendleft(tmp309)
                                                    if len(subjects280) == 0:
                                                        break
                                                    tmp305.append(subjects280.popleft())
                                                subjects280.extendleft(reversed(tmp305))
                                    subjects280.appendleft(tmp298)
                            if len(subjects280) >= 1 and isinstance(subjects280[0], Add):
                                tmp311 = subjects280.popleft()
                                associative1 = tmp311
                                associative_type1 = type(tmp311)
                                subjects312 = deque(tmp311._args)
                                matcher = CommutativeMatcher39098.get()
                                tmp313 = subjects312
                                subjects312 = []
                                for s in tmp313:
                                    matcher.add_subject(s)
                                for pattern_index, subst3 in matcher.match(tmp313, subst2):
                                    pass
                                    if pattern_index == 0:
                                        pass
                                        # State 39111
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 39112
                                            if len(subjects280) == 0:
                                                pass
                                                # State 39113
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 39114
                                                    if len(subjects251) == 0:
                                                        pass
                                                        # State 39115
                                                        if len(subjects201) == 0:
                                                            pass
                                                            # State 39116
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                yield 5, subst5
                                                if len(subjects251) >= 1:
                                                    tmp316 = subjects251.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', tmp316)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 39114
                                                        if len(subjects251) == 0:
                                                            pass
                                                            # State 39115
                                                            if len(subjects201) == 0:
                                                                pass
                                                                # State 39116
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                    yield 5, subst5
                                                    subjects251.appendleft(tmp316)
                                        if len(subjects280) >= 1:
                                            tmp318 = []
                                            tmp318.append(subjects280.popleft())
                                            while True:
                                                if len(tmp318) > 1:
                                                    tmp319 = create_operation_expression(associative1, tmp318)
                                                elif len(tmp318) == 1:
                                                    tmp319 = tmp318[0]
                                                else:
                                                    assert False, "Unreachable"
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp319)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 39112
                                                    if len(subjects280) == 0:
                                                        pass
                                                        # State 39113
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', 1)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 39114
                                                            if len(subjects251) == 0:
                                                                pass
                                                                # State 39115
                                                                if len(subjects201) == 0:
                                                                    pass
                                                                    # State 39116
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                        yield 5, subst5
                                                        if len(subjects251) >= 1:
                                                            tmp322 = subjects251.popleft()
                                                            subst5 = Substitution(subst4)
                                                            try:
                                                                subst5.try_add_variable('i2.2.1.2.2', tmp322)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 39114
                                                                if len(subjects251) == 0:
                                                                    pass
                                                                    # State 39115
                                                                    if len(subjects201) == 0:
                                                                        pass
                                                                        # State 39116
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                                            yield 5, subst5
                                                            subjects251.appendleft(tmp322)
                                                if len(subjects280) == 0:
                                                    break
                                                tmp318.append(subjects280.popleft())
                                            subjects280.extendleft(reversed(tmp318))
                                subjects280.appendleft(tmp311)
                            subjects251.appendleft(tmp279)
                    if len(subjects251) >= 1 and isinstance(subjects251[0], Mul):
                        tmp324 = subjects251.popleft()
                        associative1 = tmp324
                        associative_type1 = type(tmp324)
                        subjects325 = deque(tmp324._args)
                        matcher = CommutativeMatcher39118.get()
                        tmp326 = subjects325
                        subjects325 = []
                        for s in tmp326:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp326, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 39183
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 39184
                                    if len(subjects251) == 0:
                                        pass
                                        # State 39185
                                        if len(subjects201) == 0:
                                            pass
                                            # State 39186
                                            if len(subjects) == 0:
                                                pass
                                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                yield 5, subst3
                                if len(subjects251) >= 1:
                                    tmp328 = []
                                    tmp328.append(subjects251.popleft())
                                    while True:
                                        if len(tmp328) > 1:
                                            tmp329 = create_operation_expression(associative1, tmp328)
                                        elif len(tmp328) == 1:
                                            tmp329 = tmp328[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2', tmp329)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 39184
                                            if len(subjects251) == 0:
                                                pass
                                                # State 39185
                                                if len(subjects201) == 0:
                                                    pass
                                                    # State 39186
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: log(c*(d*(x**j*f + e)**p)**q)
                                                        yield 5, subst3
                                        if len(subjects251) == 0:
                                            break
                                        tmp328.append(subjects251.popleft())
                                    subjects251.extendleft(reversed(tmp328))
                        subjects251.appendleft(tmp324)
                    subjects201.appendleft(tmp250)
            if len(subjects201) >= 1 and isinstance(subjects201[0], Mul):
                tmp331 = subjects201.popleft()
                associative1 = tmp331
                associative_type1 = type(tmp331)
                subjects332 = deque(tmp331._args)
                matcher = CommutativeMatcher39188.get()
                tmp333 = subjects332
                subjects332 = []
                for s in tmp333:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp333, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 39469
                        if len(subjects201) == 0:
                            pass
                            # State 39470
                            if len(subjects) == 0:
                                pass
                                # 5: log(c*(d*(x**j*f + e)**p)**q)
                                yield 5, subst1
                subjects201.appendleft(tmp331)
            subjects.appendleft(tmp200)
        if len(subjects) >= 1 and isinstance(subjects[0], sin):
            tmp334 = subjects.popleft()
            subjects335 = deque(tmp334._args)
            # State 60381
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 60382
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 60383
                    if len(subjects335) >= 1:
                        tmp338 = subjects335.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp338)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 60384
                            if len(subjects335) == 0:
                                pass
                                # State 60385
                                if len(subjects) == 0:
                                    pass
                                    # 6: sin(c + x*d)
                                    yield 6, subst3
                        subjects335.appendleft(tmp338)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 72393
                    if len(subjects335) >= 1:
                        tmp341 = subjects335.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp341)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 72394
                            if len(subjects335) == 0:
                                pass
                                # State 72395
                                if len(subjects) == 0:
                                    pass
                                    # 16: sin(x*f + e)
                                    yield 16, subst3
                        subjects335.appendleft(tmp341)
                if len(subjects335) >= 1 and isinstance(subjects335[0], Mul):
                    tmp343 = subjects335.popleft()
                    associative1 = tmp343
                    associative_type1 = type(tmp343)
                    subjects344 = deque(tmp343._args)
                    matcher = CommutativeMatcher60387.get()
                    tmp345 = subjects344
                    subjects344 = []
                    for s in tmp345:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp345, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 60388
                            if len(subjects335) == 0:
                                pass
                                # State 60389
                                if len(subjects) == 0:
                                    pass
                                    # 6: sin(c + x*d)
                                    yield 6, subst2
                        if pattern_index == 1:
                            pass
                            # State 72396
                            if len(subjects335) == 0:
                                pass
                                # State 72397
                                if len(subjects) == 0:
                                    pass
                                    # 16: sin(x*f + e)
                                    yield 16, subst2
                    subjects335.appendleft(tmp343)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 61265
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61266
                    if len(subjects335) >= 1:
                        tmp348 = subjects335.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp348)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61267
                            if len(subjects335) == 0:
                                pass
                                # State 61268
                                if len(subjects) == 0:
                                    pass
                                    # 8: sin(e + x*f)
                                    yield 8, subst3
                        subjects335.appendleft(tmp348)
                if len(subjects335) >= 1 and isinstance(subjects335[0], Mul):
                    tmp350 = subjects335.popleft()
                    associative1 = tmp350
                    associative_type1 = type(tmp350)
                    subjects351 = deque(tmp350._args)
                    matcher = CommutativeMatcher61270.get()
                    tmp352 = subjects351
                    subjects351 = []
                    for s in tmp352:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp352, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 61271
                            if len(subjects335) == 0:
                                pass
                                # State 61272
                                if len(subjects) == 0:
                                    pass
                                    # 8: sin(e + x*f)
                                    yield 8, subst2
                    subjects335.appendleft(tmp350)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 61537
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61538
                    if len(subjects335) >= 1:
                        tmp355 = subjects335.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp355)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61539
                            if len(subjects335) == 0:
                                pass
                                # State 61540
                                if len(subjects) == 0:
                                    pass
                                    # 10: sin(e + x*f)
                                    yield 10, subst3
                        subjects335.appendleft(tmp355)
                if len(subjects335) >= 1 and isinstance(subjects335[0], Mul):
                    tmp357 = subjects335.popleft()
                    associative1 = tmp357
                    associative_type1 = type(tmp357)
                    subjects358 = deque(tmp357._args)
                    matcher = CommutativeMatcher61542.get()
                    tmp359 = subjects358
                    subjects358 = []
                    for s in tmp359:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp359, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 61543
                            if len(subjects335) == 0:
                                pass
                                # State 61544
                                if len(subjects) == 0:
                                    pass
                                    # 10: sin(e + x*f)
                                    yield 10, subst2
                    subjects335.appendleft(tmp357)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63236
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63237
                    if len(subjects335) >= 1:
                        tmp362 = subjects335.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp362)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63238
                            if len(subjects335) == 0:
                                pass
                                # State 63239
                                if len(subjects) == 0:
                                    pass
                                    # 12: sin(e + x*f)
                                    yield 12, subst3
                        subjects335.appendleft(tmp362)
                if len(subjects335) >= 1 and isinstance(subjects335[0], Mul):
                    tmp364 = subjects335.popleft()
                    associative1 = tmp364
                    associative_type1 = type(tmp364)
                    subjects365 = deque(tmp364._args)
                    matcher = CommutativeMatcher63241.get()
                    tmp366 = subjects365
                    subjects365 = []
                    for s in tmp366:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp366, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63242
                            if len(subjects335) == 0:
                                pass
                                # State 63243
                                if len(subjects) == 0:
                                    pass
                                    # 12: sin(e + x*f)
                                    yield 12, subst2
                    subjects335.appendleft(tmp364)
            if len(subjects335) >= 1 and isinstance(subjects335[0], Add):
                tmp367 = subjects335.popleft()
                associative1 = tmp367
                associative_type1 = type(tmp367)
                subjects368 = deque(tmp367._args)
                matcher = CommutativeMatcher60391.get()
                tmp369 = subjects368
                subjects368 = []
                for s in tmp369:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp369, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 60397
                        if len(subjects335) == 0:
                            pass
                            # State 60398
                            if len(subjects) == 0:
                                pass
                                # 6: sin(c + x*d)
                                yield 6, subst1
                    if pattern_index == 1:
                        pass
                        # State 61276
                        if len(subjects335) == 0:
                            pass
                            # State 61277
                            if len(subjects) == 0:
                                pass
                                # 8: sin(e + x*f)
                                yield 8, subst1
                    if pattern_index == 2:
                        pass
                        # State 61548
                        if len(subjects335) == 0:
                            pass
                            # State 61549
                            if len(subjects) == 0:
                                pass
                                # 10: sin(e + x*f)
                                yield 10, subst1
                    if pattern_index == 3:
                        pass
                        # State 63247
                        if len(subjects335) == 0:
                            pass
                            # State 63248
                            if len(subjects) == 0:
                                pass
                                # 12: sin(e + x*f)
                                yield 12, subst1
                    if pattern_index == 4:
                        pass
                        # State 72401
                        if len(subjects335) == 0:
                            pass
                            # State 72402
                            if len(subjects) == 0:
                                pass
                                # 16: sin(x*f + e)
                                yield 16, subst1
                subjects335.appendleft(tmp367)
            subjects.appendleft(tmp334)
        if len(subjects) >= 1 and isinstance(subjects[0], cos):
            tmp370 = subjects.popleft()
            subjects371 = deque(tmp370._args)
            # State 60442
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 60443
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 60444
                    if len(subjects371) >= 1:
                        tmp374 = subjects371.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp374)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 60445
                            if len(subjects371) == 0:
                                pass
                                # State 60446
                                if len(subjects) == 0:
                                    pass
                                    # 7: cos(c + x*d)
                                    yield 7, subst3
                        subjects371.appendleft(tmp374)
                if len(subjects371) >= 1 and isinstance(subjects371[0], Mul):
                    tmp376 = subjects371.popleft()
                    associative1 = tmp376
                    associative_type1 = type(tmp376)
                    subjects377 = deque(tmp376._args)
                    matcher = CommutativeMatcher60448.get()
                    tmp378 = subjects377
                    subjects377 = []
                    for s in tmp378:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp378, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 60449
                            if len(subjects371) == 0:
                                pass
                                # State 60450
                                if len(subjects) == 0:
                                    pass
                                    # 7: cos(c + x*d)
                                    yield 7, subst2
                    subjects371.appendleft(tmp376)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 61311
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61312
                    if len(subjects371) >= 1:
                        tmp381 = subjects371.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.1.0', tmp381)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61313
                            if len(subjects371) == 0:
                                pass
                                # State 61314
                                if len(subjects) == 0:
                                    pass
                                    # 9: cos(e + x*f)
                                    yield 9, subst3
                        subjects371.appendleft(tmp381)
                if len(subjects371) >= 1 and isinstance(subjects371[0], Mul):
                    tmp383 = subjects371.popleft()
                    associative1 = tmp383
                    associative_type1 = type(tmp383)
                    subjects384 = deque(tmp383._args)
                    matcher = CommutativeMatcher61316.get()
                    tmp385 = subjects384
                    subjects384 = []
                    for s in tmp385:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp385, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 61317
                            if len(subjects371) == 0:
                                pass
                                # State 61318
                                if len(subjects) == 0:
                                    pass
                                    # 9: cos(e + x*f)
                                    yield 9, subst2
                    subjects371.appendleft(tmp383)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 61766
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 61767
                    if len(subjects371) >= 1:
                        tmp388 = subjects371.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp388)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 61768
                            if len(subjects371) == 0:
                                pass
                                # State 61769
                                if len(subjects) == 0:
                                    pass
                                    # 11: cos(e + x*f)
                                    yield 11, subst3
                        subjects371.appendleft(tmp388)
                if len(subjects371) >= 1 and isinstance(subjects371[0], Mul):
                    tmp390 = subjects371.popleft()
                    associative1 = tmp390
                    associative_type1 = type(tmp390)
                    subjects391 = deque(tmp390._args)
                    matcher = CommutativeMatcher61771.get()
                    tmp392 = subjects391
                    subjects391 = []
                    for s in tmp392:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp392, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 61772
                            if len(subjects371) == 0:
                                pass
                                # State 61773
                                if len(subjects) == 0:
                                    pass
                                    # 11: cos(e + x*f)
                                    yield 11, subst2
                    subjects371.appendleft(tmp390)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 63412
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 63413
                    if len(subjects371) >= 1:
                        tmp395 = subjects371.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp395)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 63414
                            if len(subjects371) == 0:
                                pass
                                # State 63415
                                if len(subjects) == 0:
                                    pass
                                    # 13: cos(e + x*f)
                                    yield 13, subst3
                        subjects371.appendleft(tmp395)
                if len(subjects371) >= 1 and isinstance(subjects371[0], Mul):
                    tmp397 = subjects371.popleft()
                    associative1 = tmp397
                    associative_type1 = type(tmp397)
                    subjects398 = deque(tmp397._args)
                    matcher = CommutativeMatcher63417.get()
                    tmp399 = subjects398
                    subjects398 = []
                    for s in tmp399:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp399, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 63418
                            if len(subjects371) == 0:
                                pass
                                # State 63419
                                if len(subjects) == 0:
                                    pass
                                    # 13: cos(e + x*f)
                                    yield 13, subst2
                    subjects371.appendleft(tmp397)
            if len(subjects371) >= 1 and isinstance(subjects371[0], Add):
                tmp400 = subjects371.popleft()
                associative1 = tmp400
                associative_type1 = type(tmp400)
                subjects401 = deque(tmp400._args)
                matcher = CommutativeMatcher60452.get()
                tmp402 = subjects401
                subjects401 = []
                for s in tmp402:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp402, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 60458
                        if len(subjects371) == 0:
                            pass
                            # State 60459
                            if len(subjects) == 0:
                                pass
                                # 7: cos(c + x*d)
                                yield 7, subst1
                    if pattern_index == 1:
                        pass
                        # State 61322
                        if len(subjects371) == 0:
                            pass
                            # State 61323
                            if len(subjects) == 0:
                                pass
                                # 9: cos(e + x*f)
                                yield 9, subst1
                    if pattern_index == 2:
                        pass
                        # State 61777
                        if len(subjects371) == 0:
                            pass
                            # State 61778
                            if len(subjects) == 0:
                                pass
                                # 11: cos(e + x*f)
                                yield 11, subst1
                    if pattern_index == 3:
                        pass
                        # State 63423
                        if len(subjects371) == 0:
                            pass
                            # State 63424
                            if len(subjects) == 0:
                                pass
                                # 13: cos(e + x*f)
                                yield 13, subst1
                subjects371.appendleft(tmp400)
            subjects.appendleft(tmp370)
        if len(subjects) >= 1 and isinstance(subjects[0], tan):
            tmp403 = subjects.popleft()
            subjects404 = deque(tmp403._args)
            # State 78490
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.3.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 78491
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.3.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 78492
                    if len(subjects404) >= 1:
                        tmp407 = subjects404.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.3.1.0', tmp407)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 78493
                            if len(subjects404) == 0:
                                pass
                                # State 78494
                                if len(subjects) == 0:
                                    pass
                                    # 17: tan(e + x*f)
                                    yield 17, subst3
                        subjects404.appendleft(tmp407)
                if len(subjects404) >= 1 and isinstance(subjects404[0], Mul):
                    tmp409 = subjects404.popleft()
                    associative1 = tmp409
                    associative_type1 = type(tmp409)
                    subjects410 = deque(tmp409._args)
                    matcher = CommutativeMatcher78496.get()
                    tmp411 = subjects410
                    subjects410 = []
                    for s in tmp411:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp411, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 78497
                            if len(subjects404) == 0:
                                pass
                                # State 78498
                                if len(subjects) == 0:
                                    pass
                                    # 17: tan(e + x*f)
                                    yield 17, subst2
                    subjects404.appendleft(tmp409)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 79405
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 79406
                    if len(subjects404) >= 1:
                        tmp414 = subjects404.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.1.0', tmp414)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 79407
                            if len(subjects404) == 0:
                                pass
                                # State 79408
                                if len(subjects) == 0:
                                    pass
                                    # 19: tan(c + x*d)
                                    yield 19, subst3
                        subjects404.appendleft(tmp414)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 87065
                    if len(subjects404) >= 1:
                        tmp417 = subjects404.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp417)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 87066
                            if len(subjects404) == 0:
                                pass
                                # State 87067
                                if len(subjects) == 0:
                                    pass
                                    # 25: tan(x*f + e)
                                    yield 25, subst3
                        subjects404.appendleft(tmp417)
                if len(subjects404) >= 1 and isinstance(subjects404[0], Mul):
                    tmp419 = subjects404.popleft()
                    associative1 = tmp419
                    associative_type1 = type(tmp419)
                    subjects420 = deque(tmp419._args)
                    matcher = CommutativeMatcher79410.get()
                    tmp421 = subjects420
                    subjects420 = []
                    for s in tmp421:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp421, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 79411
                            if len(subjects404) == 0:
                                pass
                                # State 79412
                                if len(subjects) == 0:
                                    pass
                                    # 19: tan(c + x*d)
                                    yield 19, subst2
                        if pattern_index == 1:
                            pass
                            # State 87068
                            if len(subjects404) == 0:
                                pass
                                # State 87069
                                if len(subjects) == 0:
                                    pass
                                    # 25: tan(x*f + e)
                                    yield 25, subst2
                    subjects404.appendleft(tmp419)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 80114
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 80115
                    if len(subjects404) >= 1:
                        tmp424 = subjects404.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.2.2.1.0', tmp424)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 80116
                            if len(subjects404) == 0:
                                pass
                                # State 80117
                                if len(subjects) == 0:
                                    pass
                                    # 22: tan(e + x*f)
                                    yield 22, subst3
                        subjects404.appendleft(tmp424)
                if len(subjects404) >= 1 and isinstance(subjects404[0], Mul):
                    tmp426 = subjects404.popleft()
                    associative1 = tmp426
                    associative_type1 = type(tmp426)
                    subjects427 = deque(tmp426._args)
                    matcher = CommutativeMatcher80119.get()
                    tmp428 = subjects427
                    subjects427 = []
                    for s in tmp428:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp428, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 80120
                            if len(subjects404) == 0:
                                pass
                                # State 80121
                                if len(subjects) == 0:
                                    pass
                                    # 22: tan(e + x*f)
                                    yield 22, subst2
                    subjects404.appendleft(tmp426)
            if len(subjects404) >= 1 and isinstance(subjects404[0], Add):
                tmp429 = subjects404.popleft()
                associative1 = tmp429
                associative_type1 = type(tmp429)
                subjects430 = deque(tmp429._args)
                matcher = CommutativeMatcher78500.get()
                tmp431 = subjects430
                subjects430 = []
                for s in tmp431:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp431, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 78506
                        if len(subjects404) == 0:
                            pass
                            # State 78507
                            if len(subjects) == 0:
                                pass
                                # 17: tan(e + x*f)
                                yield 17, subst1
                    if pattern_index == 1:
                        pass
                        # State 79416
                        if len(subjects404) == 0:
                            pass
                            # State 79417
                            if len(subjects) == 0:
                                pass
                                # 19: tan(c + x*d)
                                yield 19, subst1
                    if pattern_index == 2:
                        pass
                        # State 80125
                        if len(subjects404) == 0:
                            pass
                            # State 80126
                            if len(subjects) == 0:
                                pass
                                # 22: tan(e + x*f)
                                yield 22, subst1
                    if pattern_index == 3:
                        pass
                        # State 87073
                        if len(subjects404) == 0:
                            pass
                            # State 87074
                            if len(subjects) == 0:
                                pass
                                # 25: tan(x*f + e)
                                yield 25, subst1
                subjects404.appendleft(tmp429)
            subjects.appendleft(tmp403)
        if len(subjects) >= 1 and isinstance(subjects[0], asin):
            tmp432 = subjects.popleft()
            subjects433 = deque(tmp432._args)
            # State 108571
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108572
                if len(subjects433) >= 1:
                    tmp435 = subjects433.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp435)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108573
                        if len(subjects433) == 0:
                            pass
                            # State 108574
                            if len(subjects) == 0:
                                pass
                                # 30: asin(x*c)
                                yield 30, subst2
                    subjects433.appendleft(tmp435)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109874
                if len(subjects433) >= 1:
                    tmp438 = subjects433.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp438)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109875
                        if len(subjects433) == 0:
                            pass
                            # State 109876
                            if len(subjects) == 0:
                                pass
                                # 32: asin(c*x)
                                yield 32, subst2
                    subjects433.appendleft(tmp438)
            if len(subjects433) >= 1 and isinstance(subjects433[0], Mul):
                tmp440 = subjects433.popleft()
                associative1 = tmp440
                associative_type1 = type(tmp440)
                subjects441 = deque(tmp440._args)
                matcher = CommutativeMatcher108576.get()
                tmp442 = subjects441
                subjects441 = []
                for s in tmp442:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp442, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108577
                        if len(subjects433) == 0:
                            pass
                            # State 108578
                            if len(subjects) == 0:
                                pass
                                # 30: asin(x*c)
                                yield 30, subst1
                    if pattern_index == 1:
                        pass
                        # State 109877
                        if len(subjects433) == 0:
                            pass
                            # State 109878
                            if len(subjects) == 0:
                                pass
                                # 32: asin(c*x)
                                yield 32, subst1
                subjects433.appendleft(tmp440)
            subjects.appendleft(tmp432)
        if len(subjects) >= 1 and isinstance(subjects[0], acos):
            tmp443 = subjects.popleft()
            subjects444 = deque(tmp443._args)
            # State 108613
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 108614
                if len(subjects444) >= 1:
                    tmp446 = subjects444.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp446)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 108615
                        if len(subjects444) == 0:
                            pass
                            # State 108616
                            if len(subjects) == 0:
                                pass
                                # 31: acos(x*c)
                                yield 31, subst2
                    subjects444.appendleft(tmp446)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 109930
                if len(subjects444) >= 1:
                    tmp449 = subjects444.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp449)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 109931
                        if len(subjects444) == 0:
                            pass
                            # State 109932
                            if len(subjects) == 0:
                                pass
                                # 33: acos(c*x)
                                yield 33, subst2
                    subjects444.appendleft(tmp449)
            if len(subjects444) >= 1 and isinstance(subjects444[0], Mul):
                tmp451 = subjects444.popleft()
                associative1 = tmp451
                associative_type1 = type(tmp451)
                subjects452 = deque(tmp451._args)
                matcher = CommutativeMatcher108618.get()
                tmp453 = subjects452
                subjects452 = []
                for s in tmp453:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp453, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 108619
                        if len(subjects444) == 0:
                            pass
                            # State 108620
                            if len(subjects) == 0:
                                pass
                                # 31: acos(x*c)
                                yield 31, subst1
                    if pattern_index == 1:
                        pass
                        # State 109933
                        if len(subjects444) == 0:
                            pass
                            # State 109934
                            if len(subjects) == 0:
                                pass
                                # 33: acos(c*x)
                                yield 33, subst1
                subjects444.appendleft(tmp451)
            subjects.appendleft(tmp443)
        if len(subjects) >= 1 and isinstance(subjects[0], atan):
            tmp454 = subjects.popleft()
            subjects455 = deque(tmp454._args)
            # State 113216
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113217
                if len(subjects455) >= 1:
                    tmp457 = subjects455.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp457)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113218
                        if len(subjects455) == 0:
                            pass
                            # State 113219
                            if len(subjects) == 0:
                                pass
                                # 34: atan(x*c)
                                yield 34, subst2
                    subjects455.appendleft(tmp457)
            if len(subjects455) >= 1 and isinstance(subjects455[0], Mul):
                tmp459 = subjects455.popleft()
                associative1 = tmp459
                associative_type1 = type(tmp459)
                subjects460 = deque(tmp459._args)
                matcher = CommutativeMatcher113221.get()
                tmp461 = subjects460
                subjects460 = []
                for s in tmp461:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp461, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 113222
                        if len(subjects455) == 0:
                            pass
                            # State 113223
                            if len(subjects) == 0:
                                pass
                                # 34: atan(x*c)
                                yield 34, subst1
                subjects455.appendleft(tmp459)
            subjects.appendleft(tmp454)
        if len(subjects) >= 1 and isinstance(subjects[0], acot):
            tmp462 = subjects.popleft()
            subjects463 = deque(tmp462._args)
            # State 113259
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 113260
                if len(subjects463) >= 1:
                    tmp465 = subjects463.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp465)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 113261
                        if len(subjects463) == 0:
                            pass
                            # State 113262
                            if len(subjects) == 0:
                                pass
                                # 35: acot(x*c)
                                yield 35, subst2
                    subjects463.appendleft(tmp465)
            if len(subjects463) >= 1 and isinstance(subjects463[0], Mul):
                tmp467 = subjects463.popleft()
                associative1 = tmp467
                associative_type1 = type(tmp467)
                subjects468 = deque(tmp467._args)
                matcher = CommutativeMatcher113264.get()
                tmp469 = subjects468
                subjects468 = []
                for s in tmp469:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp469, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 113265
                        if len(subjects463) == 0:
                            pass
                            # State 113266
                            if len(subjects) == 0:
                                pass
                                # 35: acot(x*c)
                                yield 35, subst1
                subjects463.appendleft(tmp467)
            subjects.appendleft(tmp462)
        if len(subjects) >= 1 and isinstance(subjects[0], asec):
            tmp470 = subjects.popleft()
            subjects471 = deque(tmp470._args)
            # State 119986
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 119987
                if len(subjects471) >= 1:
                    tmp473 = subjects471.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp473)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 119988
                        if len(subjects471) == 0:
                            pass
                            # State 119989
                            if len(subjects) == 0:
                                pass
                                # 36: asec(x*c)
                                yield 36, subst2
                    subjects471.appendleft(tmp473)
            if len(subjects471) >= 1 and isinstance(subjects471[0], Mul):
                tmp475 = subjects471.popleft()
                associative1 = tmp475
                associative_type1 = type(tmp475)
                subjects476 = deque(tmp475._args)
                matcher = CommutativeMatcher119991.get()
                tmp477 = subjects476
                subjects476 = []
                for s in tmp477:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp477, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 119992
                        if len(subjects471) == 0:
                            pass
                            # State 119993
                            if len(subjects) == 0:
                                pass
                                # 36: asec(x*c)
                                yield 36, subst1
                subjects471.appendleft(tmp475)
            subjects.appendleft(tmp470)
        if len(subjects) >= 1 and isinstance(subjects[0], acsc):
            tmp478 = subjects.popleft()
            subjects479 = deque(tmp478._args)
            # State 120064
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 120065
                if len(subjects479) >= 1:
                    tmp481 = subjects479.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp481)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 120066
                        if len(subjects479) == 0:
                            pass
                            # State 120067
                            if len(subjects) == 0:
                                pass
                                # 37: acsc(x*c)
                                yield 37, subst2
                    subjects479.appendleft(tmp481)
            if len(subjects479) >= 1 and isinstance(subjects479[0], Mul):
                tmp483 = subjects479.popleft()
                associative1 = tmp483
                associative_type1 = type(tmp483)
                subjects484 = deque(tmp483._args)
                matcher = CommutativeMatcher120069.get()
                tmp485 = subjects484
                subjects484 = []
                for s in tmp485:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp485, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 120070
                        if len(subjects479) == 0:
                            pass
                            # State 120071
                            if len(subjects) == 0:
                                pass
                                # 37: acsc(x*c)
                                yield 37, subst1
                subjects479.appendleft(tmp483)
            subjects.appendleft(tmp478)
        if len(subjects) >= 1 and isinstance(subjects[0], sinh):
            tmp486 = subjects.popleft()
            subjects487 = deque(tmp486._args)
            # State 122170
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 122171
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 122172
                    if len(subjects487) >= 1:
                        tmp490 = subjects487.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp490)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 122173
                            if len(subjects487) == 0:
                                pass
                                # State 122174
                                if len(subjects) == 0:
                                    pass
                                    # 38: sinh(x*b + a)
                                    yield 38, subst3
                        subjects487.appendleft(tmp490)
                if len(subjects487) >= 1 and isinstance(subjects487[0], Mul):
                    tmp492 = subjects487.popleft()
                    associative1 = tmp492
                    associative_type1 = type(tmp492)
                    subjects493 = deque(tmp492._args)
                    matcher = CommutativeMatcher122176.get()
                    tmp494 = subjects493
                    subjects493 = []
                    for s in tmp494:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp494, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 122177
                            if len(subjects487) == 0:
                                pass
                                # State 122178
                                if len(subjects) == 0:
                                    pass
                                    # 38: sinh(x*b + a)
                                    yield 38, subst2
                    subjects487.appendleft(tmp492)
            if len(subjects487) >= 1 and isinstance(subjects487[0], Add):
                tmp495 = subjects487.popleft()
                associative1 = tmp495
                associative_type1 = type(tmp495)
                subjects496 = deque(tmp495._args)
                matcher = CommutativeMatcher122180.get()
                tmp497 = subjects496
                subjects496 = []
                for s in tmp497:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp497, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 122186
                        if len(subjects487) == 0:
                            pass
                            # State 122187
                            if len(subjects) == 0:
                                pass
                                # 38: sinh(x*b + a)
                                yield 38, subst1
                subjects487.appendleft(tmp495)
            subjects.appendleft(tmp486)
        if len(subjects) >= 1 and isinstance(subjects[0], tanh):
            tmp498 = subjects.popleft()
            subjects499 = deque(tmp498._args)
            # State 126398
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 126399
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 126400
                    if len(subjects499) >= 1:
                        tmp502 = subjects499.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp502)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 126401
                            if len(subjects499) == 0:
                                pass
                                # State 126402
                                if len(subjects) == 0:
                                    pass
                                    # 39: tanh(x*b + a)
                                    yield 39, subst3
                        subjects499.appendleft(tmp502)
                if len(subjects499) >= 1 and isinstance(subjects499[0], Mul):
                    tmp504 = subjects499.popleft()
                    associative1 = tmp504
                    associative_type1 = type(tmp504)
                    subjects505 = deque(tmp504._args)
                    matcher = CommutativeMatcher126404.get()
                    tmp506 = subjects505
                    subjects505 = []
                    for s in tmp506:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp506, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 126405
                            if len(subjects499) == 0:
                                pass
                                # State 126406
                                if len(subjects) == 0:
                                    pass
                                    # 39: tanh(x*b + a)
                                    yield 39, subst2
                    subjects499.appendleft(tmp504)
            if len(subjects499) >= 1 and isinstance(subjects499[0], Add):
                tmp507 = subjects499.popleft()
                associative1 = tmp507
                associative_type1 = type(tmp507)
                subjects508 = deque(tmp507._args)
                matcher = CommutativeMatcher126408.get()
                tmp509 = subjects508
                subjects508 = []
                for s in tmp509:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp509, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 126414
                        if len(subjects499) == 0:
                            pass
                            # State 126415
                            if len(subjects) == 0:
                                pass
                                # 39: tanh(x*b + a)
                                yield 39, subst1
                subjects499.appendleft(tmp507)
            subjects.appendleft(tmp498)
        if len(subjects) >= 1 and isinstance(subjects[0], asinh):
            tmp510 = subjects.popleft()
            subjects511 = deque(tmp510._args)
            # State 138304
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138305
                if len(subjects511) >= 1:
                    tmp513 = subjects511.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp513)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138306
                        if len(subjects511) == 0:
                            pass
                            # State 138307
                            if len(subjects) == 0:
                                pass
                                # 40: asinh(x*c)
                                yield 40, subst2
                    subjects511.appendleft(tmp513)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 139637
                if len(subjects511) >= 1:
                    tmp516 = subjects511.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.1.1', tmp516)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 139638
                        if len(subjects511) == 0:
                            pass
                            # State 139639
                            if len(subjects) == 0:
                                pass
                                # 42: asinh(c*x)
                                yield 42, subst2
                    subjects511.appendleft(tmp516)
            if len(subjects511) >= 1 and isinstance(subjects511[0], Mul):
                tmp518 = subjects511.popleft()
                associative1 = tmp518
                associative_type1 = type(tmp518)
                subjects519 = deque(tmp518._args)
                matcher = CommutativeMatcher138309.get()
                tmp520 = subjects519
                subjects519 = []
                for s in tmp520:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp520, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138310
                        if len(subjects511) == 0:
                            pass
                            # State 138311
                            if len(subjects) == 0:
                                pass
                                # 40: asinh(x*c)
                                yield 40, subst1
                    if pattern_index == 1:
                        pass
                        # State 139640
                        if len(subjects511) == 0:
                            pass
                            # State 139641
                            if len(subjects) == 0:
                                pass
                                # 42: asinh(c*x)
                                yield 42, subst1
                subjects511.appendleft(tmp518)
            subjects.appendleft(tmp510)
        if len(subjects) >= 1 and isinstance(subjects[0], acosh):
            tmp521 = subjects.popleft()
            subjects522 = deque(tmp521._args)
            # State 138520
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 138521
                if len(subjects522) >= 1:
                    tmp524 = subjects522.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp524)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 138522
                        if len(subjects522) == 0:
                            pass
                            # State 138523
                            if len(subjects) == 0:
                                pass
                                # 41: acosh(x*c)
                                yield 41, subst2
                    subjects522.appendleft(tmp524)
            if len(subjects522) >= 1 and isinstance(subjects522[0], Mul):
                tmp526 = subjects522.popleft()
                associative1 = tmp526
                associative_type1 = type(tmp526)
                subjects527 = deque(tmp526._args)
                matcher = CommutativeMatcher138525.get()
                tmp528 = subjects527
                subjects527 = []
                for s in tmp528:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp528, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 138526
                        if len(subjects522) == 0:
                            pass
                            # State 138527
                            if len(subjects) == 0:
                                pass
                                # 41: acosh(x*c)
                                yield 41, subst1
                subjects522.appendleft(tmp526)
            subjects.appendleft(tmp521)
        if len(subjects) >= 1 and isinstance(subjects[0], atanh):
            tmp529 = subjects.popleft()
            subjects530 = deque(tmp529._args)
            # State 142841
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142842
                if len(subjects530) >= 1:
                    tmp532 = subjects530.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp532)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142843
                        if len(subjects530) == 0:
                            pass
                            # State 142844
                            if len(subjects) == 0:
                                pass
                                # 43: atanh(x*c)
                                yield 43, subst2
                    subjects530.appendleft(tmp532)
            if len(subjects530) >= 1 and isinstance(subjects530[0], Mul):
                tmp534 = subjects530.popleft()
                associative1 = tmp534
                associative_type1 = type(tmp534)
                subjects535 = deque(tmp534._args)
                matcher = CommutativeMatcher142846.get()
                tmp536 = subjects535
                subjects535 = []
                for s in tmp536:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp536, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142847
                        if len(subjects530) == 0:
                            pass
                            # State 142848
                            if len(subjects) == 0:
                                pass
                                # 43: atanh(x*c)
                                yield 43, subst1
                subjects530.appendleft(tmp534)
            subjects.appendleft(tmp529)
        if len(subjects) >= 1 and isinstance(subjects[0], acoth):
            tmp537 = subjects.popleft()
            subjects538 = deque(tmp537._args)
            # State 142884
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 142885
                if len(subjects538) >= 1:
                    tmp540 = subjects538.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp540)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 142886
                        if len(subjects538) == 0:
                            pass
                            # State 142887
                            if len(subjects) == 0:
                                pass
                                # 44: acoth(x*c)
                                yield 44, subst2
                    subjects538.appendleft(tmp540)
            if len(subjects538) >= 1 and isinstance(subjects538[0], Mul):
                tmp542 = subjects538.popleft()
                associative1 = tmp542
                associative_type1 = type(tmp542)
                subjects543 = deque(tmp542._args)
                matcher = CommutativeMatcher142889.get()
                tmp544 = subjects543
                subjects543 = []
                for s in tmp544:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp544, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 142890
                        if len(subjects538) == 0:
                            pass
                            # State 142891
                            if len(subjects) == 0:
                                pass
                                # 44: acoth(x*c)
                                yield 44, subst1
                subjects538.appendleft(tmp542)
            subjects.appendleft(tmp537)
        if len(subjects) >= 1 and isinstance(subjects[0], asech):
            tmp545 = subjects.popleft()
            subjects546 = deque(tmp545._args)
            # State 149162
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 149163
                if len(subjects546) >= 1:
                    tmp548 = subjects546.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp548)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 149164
                        if len(subjects546) == 0:
                            pass
                            # State 149165
                            if len(subjects) == 0:
                                pass
                                # 45: asech(x*c)
                                yield 45, subst2
                    subjects546.appendleft(tmp548)
            if len(subjects546) >= 1 and isinstance(subjects546[0], Mul):
                tmp550 = subjects546.popleft()
                associative1 = tmp550
                associative_type1 = type(tmp550)
                subjects551 = deque(tmp550._args)
                matcher = CommutativeMatcher149167.get()
                tmp552 = subjects551
                subjects551 = []
                for s in tmp552:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp552, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 149168
                        if len(subjects546) == 0:
                            pass
                            # State 149169
                            if len(subjects) == 0:
                                pass
                                # 45: asech(x*c)
                                yield 45, subst1
                subjects546.appendleft(tmp550)
            subjects.appendleft(tmp545)
        if len(subjects) >= 1 and isinstance(subjects[0], acsch):
            tmp553 = subjects.popleft()
            subjects554 = deque(tmp553._args)
            # State 149240
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 149241
                if len(subjects554) >= 1:
                    tmp556 = subjects554.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.1', tmp556)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 149242
                        if len(subjects554) == 0:
                            pass
                            # State 149243
                            if len(subjects) == 0:
                                pass
                                # 46: acsch(x*c)
                                yield 46, subst2
                    subjects554.appendleft(tmp556)
            if len(subjects554) >= 1 and isinstance(subjects554[0], Mul):
                tmp558 = subjects554.popleft()
                associative1 = tmp558
                associative_type1 = type(tmp558)
                subjects559 = deque(tmp558._args)
                matcher = CommutativeMatcher149245.get()
                tmp560 = subjects559
                subjects559 = []
                for s in tmp560:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp560, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 149246
                        if len(subjects554) == 0:
                            pass
                            # State 149247
                            if len(subjects) == 0:
                                pass
                                # 46: acsch(x*c)
                                yield 46, subst1
                subjects554.appendleft(tmp558)
            subjects.appendleft(tmp553)
        return
        yield


from .generated_part006202 import *
from .generated_part006203 import *
from .generated_part006283 import *
from .generated_part006278 import *
from .generated_part006295 import *
from .generated_part006274 import *
from .generated_part006286 import *
from .generated_part006211 import *
from .generated_part006301 import *
from .generated_part006273 import *
from .generated_part006300 import *
from .generated_part006297 import *
from .generated_part006219 import *
from .generated_part006272 import *
from .generated_part006218 import *
from .generated_part006285 import *
from .generated_part006289 import *
from .generated_part006231 import *
from .generated_part006293 import *
from collections import deque
from .generated_part006298 import *
from .generated_part006281 import *
from .generated_part006206 import *
from .generated_part006186 import *
from .generated_part006237 import *
from .generated_part006279 import *
from matchpy.utils import VariableWithCount
from .generated_part006288 import *
from .generated_part006192 import *
from .generated_part006209 import *
from .generated_part006304 import *
from .generated_part006193 import *
from .generated_part006200 import *
from .generated_part006280 import *
from .generated_part006292 import *
from .generated_part006294 import *
from .generated_part006221 import *
from .generated_part006212 import *
from .generated_part006291 import *
from .generated_part006185 import *
from .generated_part006305 import *
from .generated_part006290 import *
from .generated_part006195 import *
from .generated_part006234 import *
from .generated_part006244 import *
from .generated_part006271 import *
from .generated_part006214 import *
from multiset import Multiset
from .generated_part006224 import *
from .generated_part006284 import *
from .generated_part006232 import *
from .generated_part006277 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part006207 import *
from .generated_part006303 import *
from .generated_part006205 import *
from .generated_part006302 import *
from .generated_part006204 import *
from .generated_part006188 import *
from .generated_part006194 import *
from .generated_part006199 import *
from .generated_part006235 import *
from .generated_part006222 import *
from .generated_part006275 import *
from .generated_part006198 import *
from .generated_part006197 import *