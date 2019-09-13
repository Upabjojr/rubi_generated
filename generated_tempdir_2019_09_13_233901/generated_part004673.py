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

class CommutativeMatcher21641(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher21641._instance is None:
            CommutativeMatcher21641._instance = CommutativeMatcher21641()
        return CommutativeMatcher21641._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 21640
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 21642
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 21643
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 21644
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 21645
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21646
                            if len(subjects) >= 1:
                                tmp6 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp6)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21647
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(e + x*f)**p)**q
                                subjects.appendleft(tmp6)
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35546
                            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                                tmp9 = subjects.popleft()
                                subjects10 = deque(tmp9._args)
                                # State 35547
                                if len(subjects10) >= 1:
                                    tmp11 = subjects10.popleft()
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2.1.1', tmp11)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35548
                                        if len(subjects10) >= 1:
                                            tmp13 = subjects10.popleft()
                                            subst7 = Substitution(subst6)
                                            try:
                                                subst7.try_add_variable('i2.2.1.2.2.2.1.2', tmp13)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35549
                                                if len(subjects10) == 0:
                                                    pass
                                                    # State 35550
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                            subjects10.appendleft(tmp13)
                                    subjects10.appendleft(tmp11)
                                subjects.appendleft(tmp9)
                        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                            tmp15 = subjects.popleft()
                            associative1 = tmp15
                            associative_type1 = type(tmp15)
                            subjects16 = deque(tmp15._args)
                            matcher = CommutativeMatcher21649.get()
                            tmp17 = subjects16
                            subjects16 = []
                            for s in tmp17:
                                matcher.add_subject(s)
                            for pattern_index, subst5 in matcher.match(tmp17, subst4):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 21650
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (d*(e + x*f)**p)**q
                                if pattern_index == 1:
                                    pass
                                    # State 35555
                                    if len(subjects) == 0:
                                        pass
                                        # 5: (d*(e + f*x**m)**p)**q
                            subjects.appendleft(tmp15)
                    if len(subjects) >= 1:
                        tmp18 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.1', tmp18)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45728
                            if len(subjects) == 0:
                                pass
                                # 7: (d*v**p)**q
                        subjects.appendleft(tmp18)
                    if len(subjects) >= 1 and isinstance(subjects[0], Add):
                        tmp20 = subjects.popleft()
                        associative1 = tmp20
                        associative_type1 = type(tmp20)
                        subjects21 = deque(tmp20._args)
                        matcher = CommutativeMatcher21652.get()
                        tmp22 = subjects21
                        subjects21 = []
                        for s in tmp22:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp22, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 21658
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q
                            if pattern_index == 1:
                                pass
                                # State 29736
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x**m)**p)**q
                            if pattern_index == 2:
                                pass
                                # State 35556
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x**m)**p)**q
                            if pattern_index == 3:
                                pass
                                # State 44636
                                if len(subjects) == 0:
                                    pass
                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                        subjects.appendleft(tmp20)
                    if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                        tmp23 = subjects.popleft()
                        associative1 = tmp23
                        associative_type1 = type(tmp23)
                        subjects24 = deque(tmp23._args)
                        matcher = CommutativeMatcher33045.get()
                        tmp25 = subjects24
                        subjects24 = []
                        for s in tmp25:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp25, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 33069
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                        subjects.appendleft(tmp23)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp26 = subjects.popleft()
                    subjects27 = deque(tmp26._args)
                    # State 21659
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 21660
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21661
                            if len(subjects27) >= 1:
                                tmp30 = subjects27.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp30)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21662
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 21663
                                        if len(subjects27) == 0:
                                            pass
                                            # State 21664
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                    if len(subjects27) >= 1:
                                        tmp33 = subjects27.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp33)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21663
                                            if len(subjects27) == 0:
                                                pass
                                                # State 21664
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        subjects27.appendleft(tmp33)
                                subjects27.appendleft(tmp30)
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35557
                            if len(subjects27) >= 1 and isinstance(subjects27[0], Pow):
                                tmp36 = subjects27.popleft()
                                subjects37 = deque(tmp36._args)
                                # State 35558
                                if len(subjects37) >= 1:
                                    tmp38 = subjects37.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.1', tmp38)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35559
                                        if len(subjects37) >= 1:
                                            tmp40 = subjects37.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.2', tmp40)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35560
                                                if len(subjects37) == 0:
                                                    pass
                                                    # State 35561
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35562
                                                        if len(subjects27) == 0:
                                                            pass
                                                            # State 35563
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                    if len(subjects27) >= 1:
                                                        tmp43 = subjects27.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2.2', tmp43)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35562
                                                            if len(subjects27) == 0:
                                                                pass
                                                                # State 35563
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                        subjects27.appendleft(tmp43)
                                            subjects37.appendleft(tmp40)
                                    subjects37.appendleft(tmp38)
                                subjects27.appendleft(tmp36)
                        if len(subjects27) >= 1 and isinstance(subjects27[0], Mul):
                            tmp45 = subjects27.popleft()
                            associative1 = tmp45
                            associative_type1 = type(tmp45)
                            subjects46 = deque(tmp45._args)
                            matcher = CommutativeMatcher21666.get()
                            tmp47 = subjects46
                            subjects46 = []
                            for s in tmp47:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp47, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 21667
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 21668
                                        if len(subjects27) == 0:
                                            pass
                                            # State 21669
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                    if len(subjects27) >= 1:
                                        tmp49 = []
                                        tmp49.append(subjects27.popleft())
                                        while True:
                                            if len(tmp49) > 1:
                                                tmp50 = create_operation_expression(associative1, tmp49)
                                            elif len(tmp49) == 1:
                                                tmp50 = tmp49[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', tmp50)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21668
                                                if len(subjects27) == 0:
                                                    pass
                                                    # State 21669
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            if len(subjects27) == 0:
                                                break
                                            tmp49.append(subjects27.popleft())
                                        subjects27.extendleft(reversed(tmp49))
                                if pattern_index == 1:
                                    pass
                                    # State 35568
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35569
                                        if len(subjects27) == 0:
                                            pass
                                            # State 35570
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x**m)**p)**q
                                    if len(subjects27) >= 1:
                                        tmp53 = []
                                        tmp53.append(subjects27.popleft())
                                        while True:
                                            if len(tmp53) > 1:
                                                tmp54 = create_operation_expression(associative1, tmp53)
                                            elif len(tmp53) == 1:
                                                tmp54 = tmp53[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', tmp54)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35569
                                                if len(subjects27) == 0:
                                                    pass
                                                    # State 35570
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                            if len(subjects27) == 0:
                                                break
                                            tmp53.append(subjects27.popleft())
                                        subjects27.extendleft(reversed(tmp53))
                            subjects27.appendleft(tmp45)
                    if len(subjects27) >= 1:
                        tmp56 = subjects27.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1', tmp56)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25778
                            if len(subjects27) >= 1:
                                tmp58 = subjects27.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp58)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25779
                                    if len(subjects27) == 0:
                                        pass
                                        # State 25780
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q
                                subjects27.appendleft(tmp58)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45729
                                if len(subjects27) == 0:
                                    pass
                                    # State 45730
                                    if len(subjects) == 0:
                                        pass
                                        # 7: (d*v**p)**q
                            if len(subjects27) >= 1:
                                tmp61 = subjects27.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp61)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45729
                                    if len(subjects27) == 0:
                                        pass
                                        # State 45730
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*v**p)**q
                                subjects27.appendleft(tmp61)
                        subjects27.appendleft(tmp56)
                    if len(subjects27) >= 1 and isinstance(subjects27[0], Add):
                        tmp63 = subjects27.popleft()
                        associative1 = tmp63
                        associative_type1 = type(tmp63)
                        subjects64 = deque(tmp63._args)
                        matcher = CommutativeMatcher21671.get()
                        tmp65 = subjects64
                        subjects64 = []
                        for s in tmp65:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp65, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 21677
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21678
                                    if len(subjects27) == 0:
                                        pass
                                        # State 21679
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                if len(subjects27) >= 1:
                                    tmp67 = []
                                    tmp67.append(subjects27.popleft())
                                    while True:
                                        if len(tmp67) > 1:
                                            tmp68 = create_operation_expression(associative1, tmp67)
                                        elif len(tmp67) == 1:
                                            tmp68 = tmp67[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp68)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21678
                                            if len(subjects27) == 0:
                                                pass
                                                # State 21679
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        if len(subjects27) == 0:
                                            break
                                        tmp67.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp67))
                            if pattern_index == 1:
                                pass
                                # State 29747
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 29748
                                    if len(subjects27) == 0:
                                        pass
                                        # State 29749
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                if len(subjects27) >= 1:
                                    tmp71 = []
                                    tmp71.append(subjects27.popleft())
                                    while True:
                                        if len(tmp71) > 1:
                                            tmp72 = create_operation_expression(associative1, tmp71)
                                        elif len(tmp71) == 1:
                                            tmp72 = tmp71[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp72)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 29748
                                            if len(subjects27) == 0:
                                                pass
                                                # State 29749
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                        if len(subjects27) == 0:
                                            break
                                        tmp71.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp71))
                            if pattern_index == 2:
                                pass
                                # State 35571
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35572
                                    if len(subjects27) == 0:
                                        pass
                                        # State 35573
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                if len(subjects27) >= 1:
                                    tmp75 = []
                                    tmp75.append(subjects27.popleft())
                                    while True:
                                        if len(tmp75) > 1:
                                            tmp76 = create_operation_expression(associative1, tmp75)
                                        elif len(tmp75) == 1:
                                            tmp76 = tmp75[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp76)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35572
                                            if len(subjects27) == 0:
                                                pass
                                                # State 35573
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                        if len(subjects27) == 0:
                                            break
                                        tmp75.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp75))
                            if pattern_index == 3:
                                pass
                                # State 44644
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44645
                                    if len(subjects27) == 0:
                                        pass
                                        # State 44646
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                if len(subjects27) >= 1:
                                    tmp79 = []
                                    tmp79.append(subjects27.popleft())
                                    while True:
                                        if len(tmp79) > 1:
                                            tmp80 = create_operation_expression(associative1, tmp79)
                                        elif len(tmp79) == 1:
                                            tmp80 = tmp79[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp80)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44645
                                            if len(subjects27) == 0:
                                                pass
                                                # State 44646
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                        if len(subjects27) == 0:
                                            break
                                        tmp79.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp79))
                        subjects27.appendleft(tmp63)
                    if len(subjects27) >= 1 and isinstance(subjects27[0], Mul):
                        tmp82 = subjects27.popleft()
                        associative1 = tmp82
                        associative_type1 = type(tmp82)
                        subjects83 = deque(tmp82._args)
                        matcher = CommutativeMatcher33071.get()
                        tmp84 = subjects83
                        subjects83 = []
                        for s in tmp84:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp84, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 33095
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 33096
                                    if len(subjects27) == 0:
                                        pass
                                        # State 33097
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                if len(subjects27) >= 1:
                                    tmp86 = []
                                    tmp86.append(subjects27.popleft())
                                    while True:
                                        if len(tmp86) > 1:
                                            tmp87 = create_operation_expression(associative1, tmp86)
                                        elif len(tmp86) == 1:
                                            tmp87 = tmp86[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp87)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 33096
                                            if len(subjects27) == 0:
                                                pass
                                                # State 33097
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                        if len(subjects27) == 0:
                                            break
                                        tmp86.append(subjects27.popleft())
                                    subjects27.extendleft(reversed(tmp86))
                        subjects27.appendleft(tmp82)
                    subjects.appendleft(tmp26)
            if len(subjects) >= 1:
                tmp89 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1', tmp89)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53303
                    if len(subjects) == 0:
                        pass
                        # 9: RFx**p
                subjects.appendleft(tmp89)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp91 = subjects.popleft()
                associative1 = tmp91
                associative_type1 = type(tmp91)
                subjects92 = deque(tmp91._args)
                matcher = CommutativeMatcher21681.get()
                tmp93 = subjects92
                subjects92 = []
                for s in tmp93:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp93, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 21718
                        if len(subjects) == 0:
                            pass
                            # 0: (d*(e + x*f)**p)**q
                    if pattern_index == 1:
                        pass
                        # State 25784
                        if len(subjects) == 0:
                            pass
                            # 1: (d*v**p)**q
                    if pattern_index == 2:
                        pass
                        # State 29774
                        if len(subjects) == 0:
                            pass
                            # 3: (d*(e + f*x**m)**p)**q
                    if pattern_index == 3:
                        pass
                        # State 33152
                        if len(subjects) == 0:
                            pass
                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                    if pattern_index == 4:
                        pass
                        # State 35602
                        if len(subjects) == 0:
                            pass
                            # 5: (d*(e + f*x**m)**p)**q
                    if pattern_index == 5:
                        pass
                        # State 44665
                        if len(subjects) == 0:
                            pass
                            # 6: (d*(e + f*x + g*x**2)**p)**q
                    if pattern_index == 6:
                        pass
                        # State 45734
                        if len(subjects) == 0:
                            pass
                            # 7: (d*v**p)**q
                subjects.appendleft(tmp91)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp94 = subjects.popleft()
                associative1 = tmp94
                associative_type1 = type(tmp94)
                subjects95 = deque(tmp94._args)
                matcher = CommutativeMatcher50989.get()
                tmp96 = subjects95
                subjects95 = []
                for s in tmp96:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp96, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 51002
                        if len(subjects) == 0:
                            pass
                            # 8: (d + e*x**2)**p
                subjects.appendleft(tmp94)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 26228
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 26229
                if len(subjects) >= 1:
                    tmp99 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.1.1.0', tmp99)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 26230
                        if len(subjects) == 0:
                            pass
                            # 2: e + x*f
                    subjects.appendleft(tmp99)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp101 = subjects.popleft()
                associative1 = tmp101
                associative_type1 = type(tmp101)
                subjects102 = deque(tmp101._args)
                matcher = CommutativeMatcher26232.get()
                tmp103 = subjects102
                subjects102 = []
                for s in tmp103:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp103, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 26233
                        if len(subjects) == 0:
                            pass
                            # 2: e + x*f
                subjects.appendleft(tmp101)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp104 = subjects.popleft()
            subjects105 = deque(tmp104._args)
            # State 21719
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 21720
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 21721
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 21722
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21723
                            if len(subjects105) >= 1:
                                tmp110 = subjects105.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp110)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21724
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 21725
                                        if len(subjects105) == 0:
                                            pass
                                            # State 21726
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                    if len(subjects105) >= 1:
                                        tmp113 = subjects105.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2', tmp113)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21725
                                            if len(subjects105) == 0:
                                                pass
                                                # State 21726
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        subjects105.appendleft(tmp113)
                                subjects105.appendleft(tmp110)
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35603
                            if len(subjects105) >= 1 and isinstance(subjects105[0], Pow):
                                tmp116 = subjects105.popleft()
                                subjects117 = deque(tmp116._args)
                                # State 35604
                                if len(subjects117) >= 1:
                                    tmp118 = subjects117.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.1', tmp118)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35605
                                        if len(subjects117) >= 1:
                                            tmp120 = subjects117.popleft()
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2.2.1.2', tmp120)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35606
                                                if len(subjects117) == 0:
                                                    pass
                                                    # State 35607
                                                    subst7 = Substitution(subst6)
                                                    try:
                                                        subst7.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35608
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 35609
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                    if len(subjects105) >= 1:
                                                        tmp123 = subjects105.popleft()
                                                        subst7 = Substitution(subst6)
                                                        try:
                                                            subst7.try_add_variable('i2.2.1.2.2', tmp123)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35608
                                                            if len(subjects105) == 0:
                                                                pass
                                                                # State 35609
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                        subjects105.appendleft(tmp123)
                                            subjects117.appendleft(tmp120)
                                    subjects117.appendleft(tmp118)
                                subjects105.appendleft(tmp116)
                        if len(subjects105) >= 1 and isinstance(subjects105[0], Mul):
                            tmp125 = subjects105.popleft()
                            associative1 = tmp125
                            associative_type1 = type(tmp125)
                            subjects126 = deque(tmp125._args)
                            matcher = CommutativeMatcher21728.get()
                            tmp127 = subjects126
                            subjects126 = []
                            for s in tmp127:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp127, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 21729
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 21730
                                        if len(subjects105) == 0:
                                            pass
                                            # State 21731
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (d*(e + x*f)**p)**q
                                    if len(subjects105) >= 1:
                                        tmp129 = []
                                        tmp129.append(subjects105.popleft())
                                        while True:
                                            if len(tmp129) > 1:
                                                tmp130 = create_operation_expression(associative1, tmp129)
                                            elif len(tmp129) == 1:
                                                tmp130 = tmp129[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', tmp130)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21730
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 21731
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            if len(subjects105) == 0:
                                                break
                                            tmp129.append(subjects105.popleft())
                                        subjects105.extendleft(reversed(tmp129))
                                if pattern_index == 1:
                                    pass
                                    # State 35614
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35615
                                        if len(subjects105) == 0:
                                            pass
                                            # State 35616
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (d*(e + f*x**m)**p)**q
                                    if len(subjects105) >= 1:
                                        tmp133 = []
                                        tmp133.append(subjects105.popleft())
                                        while True:
                                            if len(tmp133) > 1:
                                                tmp134 = create_operation_expression(associative1, tmp133)
                                            elif len(tmp133) == 1:
                                                tmp134 = tmp133[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', tmp134)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35615
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 35616
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                            if len(subjects105) == 0:
                                                break
                                            tmp133.append(subjects105.popleft())
                                        subjects105.extendleft(reversed(tmp133))
                            subjects105.appendleft(tmp125)
                    if len(subjects105) >= 1:
                        tmp136 = subjects105.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1', tmp136)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45735
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45736
                                if len(subjects105) == 0:
                                    pass
                                    # State 45737
                                    if len(subjects) == 0:
                                        pass
                                        # 7: (d*v**p)**q
                            if len(subjects105) >= 1:
                                tmp139 = subjects105.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', tmp139)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45736
                                    if len(subjects105) == 0:
                                        pass
                                        # State 45737
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*v**p)**q
                                subjects105.appendleft(tmp139)
                        subjects105.appendleft(tmp136)
                    if len(subjects105) >= 1 and isinstance(subjects105[0], Add):
                        tmp141 = subjects105.popleft()
                        associative1 = tmp141
                        associative_type1 = type(tmp141)
                        subjects142 = deque(tmp141._args)
                        matcher = CommutativeMatcher21733.get()
                        tmp143 = subjects142
                        subjects142 = []
                        for s in tmp143:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp143, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 21739
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21740
                                    if len(subjects105) == 0:
                                        pass
                                        # State 21741
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                if len(subjects105) >= 1:
                                    tmp145 = []
                                    tmp145.append(subjects105.popleft())
                                    while True:
                                        if len(tmp145) > 1:
                                            tmp146 = create_operation_expression(associative1, tmp145)
                                        elif len(tmp145) == 1:
                                            tmp146 = tmp145[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp146)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21740
                                            if len(subjects105) == 0:
                                                pass
                                                # State 21741
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        if len(subjects105) == 0:
                                            break
                                        tmp145.append(subjects105.popleft())
                                    subjects105.extendleft(reversed(tmp145))
                            if pattern_index == 1:
                                pass
                                # State 29785
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 29786
                                    if len(subjects105) == 0:
                                        pass
                                        # State 29787
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                if len(subjects105) >= 1:
                                    tmp149 = []
                                    tmp149.append(subjects105.popleft())
                                    while True:
                                        if len(tmp149) > 1:
                                            tmp150 = create_operation_expression(associative1, tmp149)
                                        elif len(tmp149) == 1:
                                            tmp150 = tmp149[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp150)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 29786
                                            if len(subjects105) == 0:
                                                pass
                                                # State 29787
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                        if len(subjects105) == 0:
                                            break
                                        tmp149.append(subjects105.popleft())
                                    subjects105.extendleft(reversed(tmp149))
                            if pattern_index == 2:
                                pass
                                # State 35617
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35618
                                    if len(subjects105) == 0:
                                        pass
                                        # State 35619
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                if len(subjects105) >= 1:
                                    tmp153 = []
                                    tmp153.append(subjects105.popleft())
                                    while True:
                                        if len(tmp153) > 1:
                                            tmp154 = create_operation_expression(associative1, tmp153)
                                        elif len(tmp153) == 1:
                                            tmp154 = tmp153[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp154)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35618
                                            if len(subjects105) == 0:
                                                pass
                                                # State 35619
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                        if len(subjects105) == 0:
                                            break
                                        tmp153.append(subjects105.popleft())
                                    subjects105.extendleft(reversed(tmp153))
                            if pattern_index == 3:
                                pass
                                # State 44673
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44674
                                    if len(subjects105) == 0:
                                        pass
                                        # State 44675
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                if len(subjects105) >= 1:
                                    tmp157 = []
                                    tmp157.append(subjects105.popleft())
                                    while True:
                                        if len(tmp157) > 1:
                                            tmp158 = create_operation_expression(associative1, tmp157)
                                        elif len(tmp157) == 1:
                                            tmp158 = tmp157[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp158)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44674
                                            if len(subjects105) == 0:
                                                pass
                                                # State 44675
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                        if len(subjects105) == 0:
                                            break
                                        tmp157.append(subjects105.popleft())
                                    subjects105.extendleft(reversed(tmp157))
                        subjects105.appendleft(tmp141)
                    if len(subjects105) >= 1 and isinstance(subjects105[0], Mul):
                        tmp160 = subjects105.popleft()
                        associative1 = tmp160
                        associative_type1 = type(tmp160)
                        subjects161 = deque(tmp160._args)
                        matcher = CommutativeMatcher33154.get()
                        tmp162 = subjects161
                        subjects161 = []
                        for s in tmp162:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp162, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 33178
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 33179
                                    if len(subjects105) == 0:
                                        pass
                                        # State 33180
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                if len(subjects105) >= 1:
                                    tmp164 = []
                                    tmp164.append(subjects105.popleft())
                                    while True:
                                        if len(tmp164) > 1:
                                            tmp165 = create_operation_expression(associative1, tmp164)
                                        elif len(tmp164) == 1:
                                            tmp165 = tmp164[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp165)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 33179
                                            if len(subjects105) == 0:
                                                pass
                                                # State 33180
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                        if len(subjects105) == 0:
                                            break
                                        tmp164.append(subjects105.popleft())
                                    subjects105.extendleft(reversed(tmp164))
                        subjects105.appendleft(tmp160)
                if len(subjects105) >= 1 and isinstance(subjects105[0], Pow):
                    tmp167 = subjects105.popleft()
                    subjects168 = deque(tmp167._args)
                    # State 21742
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 21743
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21744
                            if len(subjects168) >= 1:
                                tmp171 = subjects168.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0', tmp171)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21745
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 21746
                                        if len(subjects168) == 0:
                                            pass
                                            # State 21747
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21748
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 21749
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            if len(subjects105) >= 1:
                                                tmp175 = subjects105.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', tmp175)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21748
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 21749
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                subjects105.appendleft(tmp175)
                                    if len(subjects168) >= 1:
                                        tmp177 = subjects168.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp177)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21746
                                            if len(subjects168) == 0:
                                                pass
                                                # State 21747
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21748
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 21749
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                if len(subjects105) >= 1:
                                                    tmp180 = subjects105.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp180)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 21748
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 21749
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                    subjects105.appendleft(tmp180)
                                        subjects168.appendleft(tmp177)
                                subjects168.appendleft(tmp171)
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35620
                            if len(subjects168) >= 1 and isinstance(subjects168[0], Pow):
                                tmp183 = subjects168.popleft()
                                subjects184 = deque(tmp183._args)
                                # State 35621
                                if len(subjects184) >= 1:
                                    tmp185 = subjects184.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2.1.1', tmp185)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35622
                                        if len(subjects184) >= 1:
                                            tmp187 = subjects184.popleft()
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2.1.2', tmp187)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35623
                                                if len(subjects184) == 0:
                                                    pass
                                                    # State 35624
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35625
                                                        if len(subjects168) == 0:
                                                            pass
                                                            # State 35626
                                                            subst7 = Substitution(subst6)
                                                            try:
                                                                subst7.try_add_variable('i2.2.1.2.2', 1)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 35627
                                                                if len(subjects105) == 0:
                                                                    pass
                                                                    # State 35628
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 5: (d*(e + f*x**m)**p)**q
                                                            if len(subjects105) >= 1:
                                                                tmp191 = subjects105.popleft()
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', tmp191)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 35627
                                                                    if len(subjects105) == 0:
                                                                        pass
                                                                        # State 35628
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: (d*(e + f*x**m)**p)**q
                                                                subjects105.appendleft(tmp191)
                                                    if len(subjects168) >= 1:
                                                        tmp193 = subjects168.popleft()
                                                        subst6 = Substitution(subst5)
                                                        try:
                                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp193)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35625
                                                            if len(subjects168) == 0:
                                                                pass
                                                                # State 35626
                                                                subst7 = Substitution(subst6)
                                                                try:
                                                                    subst7.try_add_variable('i2.2.1.2.2', 1)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 35627
                                                                    if len(subjects105) == 0:
                                                                        pass
                                                                        # State 35628
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 5: (d*(e + f*x**m)**p)**q
                                                                if len(subjects105) >= 1:
                                                                    tmp196 = subjects105.popleft()
                                                                    subst7 = Substitution(subst6)
                                                                    try:
                                                                        subst7.try_add_variable('i2.2.1.2.2', tmp196)
                                                                    except ValueError:
                                                                        pass
                                                                    else:
                                                                        pass
                                                                        # State 35627
                                                                        if len(subjects105) == 0:
                                                                            pass
                                                                            # State 35628
                                                                            if len(subjects) == 0:
                                                                                pass
                                                                                # 5: (d*(e + f*x**m)**p)**q
                                                                    subjects105.appendleft(tmp196)
                                                        subjects168.appendleft(tmp193)
                                            subjects184.appendleft(tmp187)
                                    subjects184.appendleft(tmp185)
                                subjects168.appendleft(tmp183)
                        if len(subjects168) >= 1 and isinstance(subjects168[0], Mul):
                            tmp198 = subjects168.popleft()
                            associative1 = tmp198
                            associative_type1 = type(tmp198)
                            subjects199 = deque(tmp198._args)
                            matcher = CommutativeMatcher21751.get()
                            tmp200 = subjects199
                            subjects199 = []
                            for s in tmp200:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp200, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 21752
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 21753
                                        if len(subjects168) == 0:
                                            pass
                                            # State 21754
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21755
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 21756
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            if len(subjects105) >= 1:
                                                tmp203 = subjects105.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp203)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21755
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 21756
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                subjects105.appendleft(tmp203)
                                    if len(subjects168) >= 1:
                                        tmp205 = []
                                        tmp205.append(subjects168.popleft())
                                        while True:
                                            if len(tmp205) > 1:
                                                tmp206 = create_operation_expression(associative1, tmp205)
                                            elif len(tmp205) == 1:
                                                tmp206 = tmp205[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2.2', tmp206)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21753
                                                if len(subjects168) == 0:
                                                    pass
                                                    # State 21754
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 21755
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 21756
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                    if len(subjects105) >= 1:
                                                        tmp209 = subjects105.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', tmp209)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 21755
                                                            if len(subjects105) == 0:
                                                                pass
                                                                # State 21756
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 0: (d*(e + x*f)**p)**q
                                                        subjects105.appendleft(tmp209)
                                            if len(subjects168) == 0:
                                                break
                                            tmp205.append(subjects168.popleft())
                                        subjects168.extendleft(reversed(tmp205))
                                if pattern_index == 1:
                                    pass
                                    # State 35633
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35634
                                        if len(subjects168) == 0:
                                            pass
                                            # State 35635
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35636
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 35637
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                            if len(subjects105) >= 1:
                                                tmp213 = subjects105.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp213)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 35636
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 35637
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x**m)**p)**q
                                                subjects105.appendleft(tmp213)
                                    if len(subjects168) >= 1:
                                        tmp215 = []
                                        tmp215.append(subjects168.popleft())
                                        while True:
                                            if len(tmp215) > 1:
                                                tmp216 = create_operation_expression(associative1, tmp215)
                                            elif len(tmp215) == 1:
                                                tmp216 = tmp215[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2.2', tmp216)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35634
                                                if len(subjects168) == 0:
                                                    pass
                                                    # State 35635
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35636
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 35637
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                    if len(subjects105) >= 1:
                                                        tmp219 = subjects105.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', tmp219)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 35636
                                                            if len(subjects105) == 0:
                                                                pass
                                                                # State 35637
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 5: (d*(e + f*x**m)**p)**q
                                                        subjects105.appendleft(tmp219)
                                            if len(subjects168) == 0:
                                                break
                                            tmp215.append(subjects168.popleft())
                                        subjects168.extendleft(reversed(tmp215))
                            subjects168.appendleft(tmp198)
                    if len(subjects168) >= 1:
                        tmp221 = subjects168.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.1', tmp221)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25785
                            if len(subjects168) >= 1:
                                tmp223 = subjects168.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', tmp223)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25786
                                    if len(subjects168) == 0:
                                        pass
                                        # State 25787
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 25788
                                            if len(subjects105) == 0:
                                                pass
                                                # State 25789
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*v**p)**q
                                        if len(subjects105) >= 1:
                                            tmp226 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp226)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 25788
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 25789
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*v**p)**q
                                            subjects105.appendleft(tmp226)
                                subjects168.appendleft(tmp223)
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45738
                                if len(subjects168) == 0:
                                    pass
                                    # State 45739
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45740
                                        if len(subjects105) == 0:
                                            pass
                                            # State 45741
                                            if len(subjects) == 0:
                                                pass
                                                # 7: (d*v**p)**q
                                    if len(subjects105) >= 1:
                                        tmp230 = subjects105.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp230)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45740
                                            if len(subjects105) == 0:
                                                pass
                                                # State 45741
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (d*v**p)**q
                                        subjects105.appendleft(tmp230)
                            if len(subjects168) >= 1:
                                tmp232 = subjects168.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', tmp232)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45738
                                    if len(subjects168) == 0:
                                        pass
                                        # State 45739
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45740
                                            if len(subjects105) == 0:
                                                pass
                                                # State 45741
                                                if len(subjects) == 0:
                                                    pass
                                                    # 7: (d*v**p)**q
                                        if len(subjects105) >= 1:
                                            tmp235 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp235)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45740
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 45741
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 7: (d*v**p)**q
                                            subjects105.appendleft(tmp235)
                                subjects168.appendleft(tmp232)
                        subjects168.appendleft(tmp221)
                    if len(subjects168) >= 1 and isinstance(subjects168[0], Add):
                        tmp237 = subjects168.popleft()
                        associative1 = tmp237
                        associative_type1 = type(tmp237)
                        subjects238 = deque(tmp237._args)
                        matcher = CommutativeMatcher21758.get()
                        tmp239 = subjects238
                        subjects238 = []
                        for s in tmp239:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp239, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 21764
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21765
                                    if len(subjects168) == 0:
                                        pass
                                        # State 21766
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21767
                                            if len(subjects105) == 0:
                                                pass
                                                # State 21768
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + x*f)**p)**q
                                        if len(subjects105) >= 1:
                                            tmp242 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp242)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 21767
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 21768
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + x*f)**p)**q
                                            subjects105.appendleft(tmp242)
                                if len(subjects168) >= 1:
                                    tmp244 = []
                                    tmp244.append(subjects168.popleft())
                                    while True:
                                        if len(tmp244) > 1:
                                            tmp245 = create_operation_expression(associative1, tmp244)
                                        elif len(tmp244) == 1:
                                            tmp245 = tmp244[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp245)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 21765
                                            if len(subjects168) == 0:
                                                pass
                                                # State 21766
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 21767
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 21768
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + x*f)**p)**q
                                                if len(subjects105) >= 1:
                                                    tmp248 = subjects105.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp248)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 21767
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 21768
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + x*f)**p)**q
                                                    subjects105.appendleft(tmp248)
                                        if len(subjects168) == 0:
                                            break
                                        tmp244.append(subjects168.popleft())
                                    subjects168.extendleft(reversed(tmp244))
                            if pattern_index == 1:
                                pass
                                # State 29798
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 29799
                                    if len(subjects168) == 0:
                                        pass
                                        # State 29800
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 29801
                                            if len(subjects105) == 0:
                                                pass
                                                # State 29802
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: (d*(e + f*x**m)**p)**q
                                        if len(subjects105) >= 1:
                                            tmp252 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp252)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 29801
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 29802
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 3: (d*(e + f*x**m)**p)**q
                                            subjects105.appendleft(tmp252)
                                if len(subjects168) >= 1:
                                    tmp254 = []
                                    tmp254.append(subjects168.popleft())
                                    while True:
                                        if len(tmp254) > 1:
                                            tmp255 = create_operation_expression(associative1, tmp254)
                                        elif len(tmp254) == 1:
                                            tmp255 = tmp254[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp255)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 29799
                                            if len(subjects168) == 0:
                                                pass
                                                # State 29800
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 29801
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 29802
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 3: (d*(e + f*x**m)**p)**q
                                                if len(subjects105) >= 1:
                                                    tmp258 = subjects105.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp258)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 29801
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 29802
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 3: (d*(e + f*x**m)**p)**q
                                                    subjects105.appendleft(tmp258)
                                        if len(subjects168) == 0:
                                            break
                                        tmp254.append(subjects168.popleft())
                                    subjects168.extendleft(reversed(tmp254))
                            if pattern_index == 2:
                                pass
                                # State 35638
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35639
                                    if len(subjects168) == 0:
                                        pass
                                        # State 35640
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35641
                                            if len(subjects105) == 0:
                                                pass
                                                # State 35642
                                                if len(subjects) == 0:
                                                    pass
                                                    # 5: (d*(e + f*x**m)**p)**q
                                        if len(subjects105) >= 1:
                                            tmp262 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp262)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35641
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 35642
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 5: (d*(e + f*x**m)**p)**q
                                            subjects105.appendleft(tmp262)
                                if len(subjects168) >= 1:
                                    tmp264 = []
                                    tmp264.append(subjects168.popleft())
                                    while True:
                                        if len(tmp264) > 1:
                                            tmp265 = create_operation_expression(associative1, tmp264)
                                        elif len(tmp264) == 1:
                                            tmp265 = tmp264[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp265)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 35639
                                            if len(subjects168) == 0:
                                                pass
                                                # State 35640
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 35641
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 35642
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 5: (d*(e + f*x**m)**p)**q
                                                if len(subjects105) >= 1:
                                                    tmp268 = subjects105.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp268)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 35641
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 35642
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 5: (d*(e + f*x**m)**p)**q
                                                    subjects105.appendleft(tmp268)
                                        if len(subjects168) == 0:
                                            break
                                        tmp264.append(subjects168.popleft())
                                    subjects168.extendleft(reversed(tmp264))
                            if pattern_index == 3:
                                pass
                                # State 44683
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44684
                                    if len(subjects168) == 0:
                                        pass
                                        # State 44685
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44686
                                            if len(subjects105) == 0:
                                                pass
                                                # State 44687
                                                if len(subjects) == 0:
                                                    pass
                                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                                        if len(subjects105) >= 1:
                                            tmp272 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp272)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 44686
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 44687
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 6: (d*(e + f*x + g*x**2)**p)**q
                                            subjects105.appendleft(tmp272)
                                if len(subjects168) >= 1:
                                    tmp274 = []
                                    tmp274.append(subjects168.popleft())
                                    while True:
                                        if len(tmp274) > 1:
                                            tmp275 = create_operation_expression(associative1, tmp274)
                                        elif len(tmp274) == 1:
                                            tmp275 = tmp274[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp275)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 44684
                                            if len(subjects168) == 0:
                                                pass
                                                # State 44685
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 44686
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 44687
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                                if len(subjects105) >= 1:
                                                    tmp278 = subjects105.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp278)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 44686
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 44687
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 6: (d*(e + f*x + g*x**2)**p)**q
                                                    subjects105.appendleft(tmp278)
                                        if len(subjects168) == 0:
                                            break
                                        tmp274.append(subjects168.popleft())
                                    subjects168.extendleft(reversed(tmp274))
                        subjects168.appendleft(tmp237)
                    if len(subjects168) >= 1 and isinstance(subjects168[0], Mul):
                        tmp280 = subjects168.popleft()
                        associative1 = tmp280
                        associative_type1 = type(tmp280)
                        subjects281 = deque(tmp280._args)
                        matcher = CommutativeMatcher33182.get()
                        tmp282 = subjects281
                        subjects281 = []
                        for s in tmp282:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp282, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 33206
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 33207
                                    if len(subjects168) == 0:
                                        pass
                                        # State 33208
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 33209
                                            if len(subjects105) == 0:
                                                pass
                                                # State 33210
                                                if len(subjects) == 0:
                                                    pass
                                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                                        if len(subjects105) >= 1:
                                            tmp285 = subjects105.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp285)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 33209
                                                if len(subjects105) == 0:
                                                    pass
                                                    # State 33210
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (d*(x**m*(f + e*x**r))**p)**q
                                            subjects105.appendleft(tmp285)
                                if len(subjects168) >= 1:
                                    tmp287 = []
                                    tmp287.append(subjects168.popleft())
                                    while True:
                                        if len(tmp287) > 1:
                                            tmp288 = create_operation_expression(associative1, tmp287)
                                        elif len(tmp287) == 1:
                                            tmp288 = tmp287[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp288)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 33207
                                            if len(subjects168) == 0:
                                                pass
                                                # State 33208
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 33209
                                                    if len(subjects105) == 0:
                                                        pass
                                                        # State 33210
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                if len(subjects105) >= 1:
                                                    tmp291 = subjects105.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp291)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 33209
                                                        if len(subjects105) == 0:
                                                            pass
                                                            # State 33210
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 4: (d*(x**m*(f + e*x**r))**p)**q
                                                    subjects105.appendleft(tmp291)
                                        if len(subjects168) == 0:
                                            break
                                        tmp287.append(subjects168.popleft())
                                    subjects168.extendleft(reversed(tmp287))
                        subjects168.appendleft(tmp280)
                    subjects105.appendleft(tmp167)
            if len(subjects105) >= 1:
                tmp293 = subjects105.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.1', tmp293)
                except ValueError:
                    pass
                else:
                    pass
                    # State 53304
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 53305
                        if len(subjects105) == 0:
                            pass
                            # State 53306
                            if len(subjects) == 0:
                                pass
                                # 9: RFx**p
                    if len(subjects105) >= 1:
                        tmp296 = subjects105.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', tmp296)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 53305
                            if len(subjects105) == 0:
                                pass
                                # State 53306
                                if len(subjects) == 0:
                                    pass
                                    # 9: RFx**p
                        subjects105.appendleft(tmp296)
                subjects105.appendleft(tmp293)
            if len(subjects105) >= 1 and isinstance(subjects105[0], Mul):
                tmp298 = subjects105.popleft()
                associative1 = tmp298
                associative_type1 = type(tmp298)
                subjects299 = deque(tmp298._args)
                matcher = CommutativeMatcher21770.get()
                tmp300 = subjects299
                subjects299 = []
                for s in tmp300:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp300, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 21807
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21808
                            if len(subjects105) == 0:
                                pass
                                # State 21809
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + x*f)**p)**q
                        if len(subjects105) >= 1:
                            tmp302 = []
                            tmp302.append(subjects105.popleft())
                            while True:
                                if len(tmp302) > 1:
                                    tmp303 = create_operation_expression(associative1, tmp302)
                                elif len(tmp302) == 1:
                                    tmp303 = tmp302[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp303)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21808
                                    if len(subjects105) == 0:
                                        pass
                                        # State 21809
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + x*f)**p)**q
                                if len(subjects105) == 0:
                                    break
                                tmp302.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp302))
                    if pattern_index == 1:
                        pass
                        # State 25793
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25794
                            if len(subjects105) == 0:
                                pass
                                # State 25795
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d*v**p)**q
                        if len(subjects105) >= 1:
                            tmp306 = []
                            tmp306.append(subjects105.popleft())
                            while True:
                                if len(tmp306) > 1:
                                    tmp307 = create_operation_expression(associative1, tmp306)
                                elif len(tmp306) == 1:
                                    tmp307 = tmp306[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp307)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 25794
                                    if len(subjects105) == 0:
                                        pass
                                        # State 25795
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q
                                if len(subjects105) == 0:
                                    break
                                tmp306.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp306))
                    if pattern_index == 2:
                        pass
                        # State 29827
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 29828
                            if len(subjects105) == 0:
                                pass
                                # State 29829
                                if len(subjects) == 0:
                                    pass
                                    # 3: (d*(e + f*x**m)**p)**q
                        if len(subjects105) >= 1:
                            tmp310 = []
                            tmp310.append(subjects105.popleft())
                            while True:
                                if len(tmp310) > 1:
                                    tmp311 = create_operation_expression(associative1, tmp310)
                                elif len(tmp310) == 1:
                                    tmp311 = tmp310[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp311)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 29828
                                    if len(subjects105) == 0:
                                        pass
                                        # State 29829
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (d*(e + f*x**m)**p)**q
                                if len(subjects105) == 0:
                                    break
                                tmp310.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp310))
                    if pattern_index == 3:
                        pass
                        # State 33265
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 33266
                            if len(subjects105) == 0:
                                pass
                                # State 33267
                                if len(subjects) == 0:
                                    pass
                                    # 4: (d*(x**m*(f + e*x**r))**p)**q
                        if len(subjects105) >= 1:
                            tmp314 = []
                            tmp314.append(subjects105.popleft())
                            while True:
                                if len(tmp314) > 1:
                                    tmp315 = create_operation_expression(associative1, tmp314)
                                elif len(tmp314) == 1:
                                    tmp315 = tmp314[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp315)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 33266
                                    if len(subjects105) == 0:
                                        pass
                                        # State 33267
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (d*(x**m*(f + e*x**r))**p)**q
                                if len(subjects105) == 0:
                                    break
                                tmp314.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp314))
                    if pattern_index == 4:
                        pass
                        # State 35671
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35672
                            if len(subjects105) == 0:
                                pass
                                # State 35673
                                if len(subjects) == 0:
                                    pass
                                    # 5: (d*(e + f*x**m)**p)**q
                        if len(subjects105) >= 1:
                            tmp318 = []
                            tmp318.append(subjects105.popleft())
                            while True:
                                if len(tmp318) > 1:
                                    tmp319 = create_operation_expression(associative1, tmp318)
                                elif len(tmp318) == 1:
                                    tmp319 = tmp318[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp319)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35672
                                    if len(subjects105) == 0:
                                        pass
                                        # State 35673
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (d*(e + f*x**m)**p)**q
                                if len(subjects105) == 0:
                                    break
                                tmp318.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp318))
                    if pattern_index == 5:
                        pass
                        # State 44706
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 44707
                            if len(subjects105) == 0:
                                pass
                                # State 44708
                                if len(subjects) == 0:
                                    pass
                                    # 6: (d*(e + f*x + g*x**2)**p)**q
                        if len(subjects105) >= 1:
                            tmp322 = []
                            tmp322.append(subjects105.popleft())
                            while True:
                                if len(tmp322) > 1:
                                    tmp323 = create_operation_expression(associative1, tmp322)
                                elif len(tmp322) == 1:
                                    tmp323 = tmp322[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp323)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44707
                                    if len(subjects105) == 0:
                                        pass
                                        # State 44708
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (d*(e + f*x + g*x**2)**p)**q
                                if len(subjects105) == 0:
                                    break
                                tmp322.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp322))
                    if pattern_index == 6:
                        pass
                        # State 45745
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45746
                            if len(subjects105) == 0:
                                pass
                                # State 45747
                                if len(subjects) == 0:
                                    pass
                                    # 7: (d*v**p)**q
                        if len(subjects105) >= 1:
                            tmp326 = []
                            tmp326.append(subjects105.popleft())
                            while True:
                                if len(tmp326) > 1:
                                    tmp327 = create_operation_expression(associative1, tmp326)
                                elif len(tmp326) == 1:
                                    tmp327 = tmp326[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp327)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45746
                                    if len(subjects105) == 0:
                                        pass
                                        # State 45747
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (d*v**p)**q
                                if len(subjects105) == 0:
                                    break
                                tmp326.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp326))
                subjects105.appendleft(tmp298)
            if len(subjects105) >= 1 and isinstance(subjects105[0], Add):
                tmp329 = subjects105.popleft()
                associative1 = tmp329
                associative_type1 = type(tmp329)
                subjects330 = deque(tmp329._args)
                matcher = CommutativeMatcher51004.get()
                tmp331 = subjects330
                subjects330 = []
                for s in tmp331:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp331, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 51017
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 51018
                            if len(subjects105) == 0:
                                pass
                                # State 51019
                                if len(subjects) == 0:
                                    pass
                                    # 8: (d + e*x**2)**p
                        if len(subjects105) >= 1:
                            tmp333 = []
                            tmp333.append(subjects105.popleft())
                            while True:
                                if len(tmp333) > 1:
                                    tmp334 = create_operation_expression(associative1, tmp333)
                                elif len(tmp333) == 1:
                                    tmp334 = tmp333[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp334)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51018
                                    if len(subjects105) == 0:
                                        pass
                                        # State 51019
                                        if len(subjects) == 0:
                                            pass
                                            # 8: (d + e*x**2)**p
                                if len(subjects105) == 0:
                                    break
                                tmp333.append(subjects105.popleft())
                            subjects105.extendleft(reversed(tmp333))
                subjects105.appendleft(tmp329)
            subjects.appendleft(tmp104)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp336 = subjects.popleft()
            associative1 = tmp336
            associative_type1 = type(tmp336)
            subjects337 = deque(tmp336._args)
            matcher = CommutativeMatcher26235.get()
            tmp338 = subjects337
            subjects337 = []
            for s in tmp338:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp338, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 26241
                    if len(subjects) == 0:
                        pass
                        # 2: e + x*f
            subjects.appendleft(tmp336)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
