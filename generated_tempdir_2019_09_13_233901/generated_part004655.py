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

class CommutativeMatcher21599(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher21599._instance is None:
            CommutativeMatcher21599._instance = CommutativeMatcher21599()
        return CommutativeMatcher21599._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 21598
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 21600
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 21601
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 21602
                    if len(subjects) >= 1:
                        tmp4 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0', tmp4)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21603
                            if len(subjects) == 0:
                                pass
                                # 0: (e + x*f)**p
                        subjects.appendleft(tmp4)
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 35514
                    if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                        tmp7 = subjects.popleft()
                        subjects8 = deque(tmp7._args)
                        # State 35515
                        if len(subjects8) >= 1:
                            tmp9 = subjects8.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2.1.1', tmp9)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 35516
                                if len(subjects8) >= 1:
                                    tmp11 = subjects8.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2.1.2', tmp11)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35517
                                        if len(subjects8) == 0:
                                            pass
                                            # State 35518
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (e + f*x**m)**p
                                    subjects8.appendleft(tmp11)
                            subjects8.appendleft(tmp9)
                        subjects.appendleft(tmp7)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp13 = subjects.popleft()
                    associative1 = tmp13
                    associative_type1 = type(tmp13)
                    subjects14 = deque(tmp13._args)
                    matcher = CommutativeMatcher21605.get()
                    tmp15 = subjects14
                    subjects14 = []
                    for s in tmp15:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp15, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 21606
                            if len(subjects) == 0:
                                pass
                                # 0: (e + x*f)**p
                        if pattern_index == 1:
                            pass
                            # State 35523
                            if len(subjects) == 0:
                                pass
                                # 4: (e + f*x**m)**p
                    subjects.appendleft(tmp13)
            if len(subjects) >= 1:
                tmp16 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1', tmp16)
                except ValueError:
                    pass
                else:
                    pass
                    # State 45721
                    if len(subjects) == 0:
                        pass
                        # 6: v**p
                subjects.appendleft(tmp16)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp18 = subjects.popleft()
                associative1 = tmp18
                associative_type1 = type(tmp18)
                subjects19 = deque(tmp18._args)
                matcher = CommutativeMatcher21608.get()
                tmp20 = subjects19
                subjects19 = []
                for s in tmp20:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp20, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 21614
                        if len(subjects) == 0:
                            pass
                            # 0: (e + x*f)**p
                    if pattern_index == 1:
                        pass
                        # State 29708
                        if len(subjects) == 0:
                            pass
                            # 2: (e + f*x**m)**p
                    if pattern_index == 2:
                        pass
                        # State 35524
                        if len(subjects) == 0:
                            pass
                            # 4: (e + f*x**m)**p
                    if pattern_index == 3:
                        pass
                        # State 44614
                        if len(subjects) == 0:
                            pass
                            # 5: (e + f*x + g*x**2)**p
                subjects.appendleft(tmp18)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp21 = subjects.popleft()
                associative1 = tmp21
                associative_type1 = type(tmp21)
                subjects22 = deque(tmp21._args)
                matcher = CommutativeMatcher32987.get()
                tmp23 = subjects22
                subjects22 = []
                for s in tmp23:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp23, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 33011
                        if len(subjects) == 0:
                            pass
                            # 3: (x**m*(f + e*x**r))**p
                subjects.appendleft(tmp21)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp24 = subjects.popleft()
            subjects25 = deque(tmp24._args)
            # State 21615
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 21616
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 21617
                    if len(subjects25) >= 1:
                        tmp28 = subjects25.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0', tmp28)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21618
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 21619
                                if len(subjects25) == 0:
                                    pass
                                    # State 21620
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (e + x*f)**p
                            if len(subjects25) >= 1:
                                tmp31 = subjects25.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp31)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21619
                                    if len(subjects25) == 0:
                                        pass
                                        # State 21620
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (e + x*f)**p
                                subjects25.appendleft(tmp31)
                        subjects25.appendleft(tmp28)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 35525
                    if len(subjects25) >= 1 and isinstance(subjects25[0], Pow):
                        tmp34 = subjects25.popleft()
                        subjects35 = deque(tmp34._args)
                        # State 35526
                        if len(subjects35) >= 1:
                            tmp36 = subjects35.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2.1.1', tmp36)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 35527
                                if len(subjects35) >= 1:
                                    tmp38 = subjects35.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2.1.2', tmp38)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35528
                                        if len(subjects35) == 0:
                                            pass
                                            # State 35529
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 35530
                                                if len(subjects25) == 0:
                                                    pass
                                                    # State 35531
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 4: (e + f*x**m)**p
                                            if len(subjects25) >= 1:
                                                tmp41 = subjects25.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2.2', tmp41)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 35530
                                                    if len(subjects25) == 0:
                                                        pass
                                                        # State 35531
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 4: (e + f*x**m)**p
                                                subjects25.appendleft(tmp41)
                                    subjects35.appendleft(tmp38)
                            subjects35.appendleft(tmp36)
                        subjects25.appendleft(tmp34)
                if len(subjects25) >= 1 and isinstance(subjects25[0], Mul):
                    tmp43 = subjects25.popleft()
                    associative1 = tmp43
                    associative_type1 = type(tmp43)
                    subjects44 = deque(tmp43._args)
                    matcher = CommutativeMatcher21622.get()
                    tmp45 = subjects44
                    subjects44 = []
                    for s in tmp45:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp45, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 21623
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 21624
                                if len(subjects25) == 0:
                                    pass
                                    # State 21625
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (e + x*f)**p
                            if len(subjects25) >= 1:
                                tmp47 = []
                                tmp47.append(subjects25.popleft())
                                while True:
                                    if len(tmp47) > 1:
                                        tmp48 = create_operation_expression(associative1, tmp47)
                                    elif len(tmp47) == 1:
                                        tmp48 = tmp47[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2.2.2', tmp48)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 21624
                                        if len(subjects25) == 0:
                                            pass
                                            # State 21625
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (e + x*f)**p
                                    if len(subjects25) == 0:
                                        break
                                    tmp47.append(subjects25.popleft())
                                subjects25.extendleft(reversed(tmp47))
                        if pattern_index == 1:
                            pass
                            # State 35536
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 35537
                                if len(subjects25) == 0:
                                    pass
                                    # State 35538
                                    if len(subjects) == 0:
                                        pass
                                        # 4: (e + f*x**m)**p
                            if len(subjects25) >= 1:
                                tmp51 = []
                                tmp51.append(subjects25.popleft())
                                while True:
                                    if len(tmp51) > 1:
                                        tmp52 = create_operation_expression(associative1, tmp51)
                                    elif len(tmp51) == 1:
                                        tmp52 = tmp51[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.1.2.2.2', tmp52)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 35537
                                        if len(subjects25) == 0:
                                            pass
                                            # State 35538
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (e + f*x**m)**p
                                    if len(subjects25) == 0:
                                        break
                                    tmp51.append(subjects25.popleft())
                                subjects25.extendleft(reversed(tmp51))
                    subjects25.appendleft(tmp43)
            if len(subjects25) >= 1:
                tmp54 = subjects25.popleft()
                subst1 = Substitution(subst0)
                try:
                    subst1.try_add_variable('i2.2.1.2.2.1', tmp54)
                except ValueError:
                    pass
                else:
                    pass
                    # State 25771
                    if len(subjects25) >= 1:
                        tmp56 = subjects25.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', tmp56)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 25772
                            if len(subjects25) == 0:
                                pass
                                # State 25773
                                if len(subjects) == 0:
                                    pass
                                    # 1: v**p
                        subjects25.appendleft(tmp56)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2', 1)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 45722
                        if len(subjects25) == 0:
                            pass
                            # State 45723
                            if len(subjects) == 0:
                                pass
                                # 6: v**p
                    if len(subjects25) >= 1:
                        tmp59 = subjects25.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', tmp59)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45722
                            if len(subjects25) == 0:
                                pass
                                # State 45723
                                if len(subjects) == 0:
                                    pass
                                    # 6: v**p
                        subjects25.appendleft(tmp59)
                subjects25.appendleft(tmp54)
            if len(subjects25) >= 1 and isinstance(subjects25[0], Add):
                tmp61 = subjects25.popleft()
                associative1 = tmp61
                associative_type1 = type(tmp61)
                subjects62 = deque(tmp61._args)
                matcher = CommutativeMatcher21627.get()
                tmp63 = subjects62
                subjects62 = []
                for s in tmp63:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp63, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 21633
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 21634
                            if len(subjects25) == 0:
                                pass
                                # State 21635
                                if len(subjects) == 0:
                                    pass
                                    # 0: (e + x*f)**p
                        if len(subjects25) >= 1:
                            tmp65 = []
                            tmp65.append(subjects25.popleft())
                            while True:
                                if len(tmp65) > 1:
                                    tmp66 = create_operation_expression(associative1, tmp65)
                                elif len(tmp65) == 1:
                                    tmp66 = tmp65[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp66)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 21634
                                    if len(subjects25) == 0:
                                        pass
                                        # State 21635
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (e + x*f)**p
                                if len(subjects25) == 0:
                                    break
                                tmp65.append(subjects25.popleft())
                            subjects25.extendleft(reversed(tmp65))
                    if pattern_index == 1:
                        pass
                        # State 29719
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 29720
                            if len(subjects25) == 0:
                                pass
                                # State 29721
                                if len(subjects) == 0:
                                    pass
                                    # 2: (e + f*x**m)**p
                        if len(subjects25) >= 1:
                            tmp69 = []
                            tmp69.append(subjects25.popleft())
                            while True:
                                if len(tmp69) > 1:
                                    tmp70 = create_operation_expression(associative1, tmp69)
                                elif len(tmp69) == 1:
                                    tmp70 = tmp69[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp70)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 29720
                                    if len(subjects25) == 0:
                                        pass
                                        # State 29721
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (e + f*x**m)**p
                                if len(subjects25) == 0:
                                    break
                                tmp69.append(subjects25.popleft())
                            subjects25.extendleft(reversed(tmp69))
                    if pattern_index == 2:
                        pass
                        # State 35539
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 35540
                            if len(subjects25) == 0:
                                pass
                                # State 35541
                                if len(subjects) == 0:
                                    pass
                                    # 4: (e + f*x**m)**p
                        if len(subjects25) >= 1:
                            tmp73 = []
                            tmp73.append(subjects25.popleft())
                            while True:
                                if len(tmp73) > 1:
                                    tmp74 = create_operation_expression(associative1, tmp73)
                                elif len(tmp73) == 1:
                                    tmp74 = tmp73[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp74)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 35540
                                    if len(subjects25) == 0:
                                        pass
                                        # State 35541
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (e + f*x**m)**p
                                if len(subjects25) == 0:
                                    break
                                tmp73.append(subjects25.popleft())
                            subjects25.extendleft(reversed(tmp73))
                    if pattern_index == 3:
                        pass
                        # State 44622
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 44623
                            if len(subjects25) == 0:
                                pass
                                # State 44624
                                if len(subjects) == 0:
                                    pass
                                    # 5: (e + f*x + g*x**2)**p
                        if len(subjects25) >= 1:
                            tmp77 = []
                            tmp77.append(subjects25.popleft())
                            while True:
                                if len(tmp77) > 1:
                                    tmp78 = create_operation_expression(associative1, tmp77)
                                elif len(tmp77) == 1:
                                    tmp78 = tmp77[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp78)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 44623
                                    if len(subjects25) == 0:
                                        pass
                                        # State 44624
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (e + f*x + g*x**2)**p
                                if len(subjects25) == 0:
                                    break
                                tmp77.append(subjects25.popleft())
                            subjects25.extendleft(reversed(tmp77))
                subjects25.appendleft(tmp61)
            if len(subjects25) >= 1 and isinstance(subjects25[0], Mul):
                tmp80 = subjects25.popleft()
                associative1 = tmp80
                associative_type1 = type(tmp80)
                subjects81 = deque(tmp80._args)
                matcher = CommutativeMatcher33013.get()
                tmp82 = subjects81
                subjects81 = []
                for s in tmp82:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp82, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 33037
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 33038
                            if len(subjects25) == 0:
                                pass
                                # State 33039
                                if len(subjects) == 0:
                                    pass
                                    # 3: (x**m*(f + e*x**r))**p
                        if len(subjects25) >= 1:
                            tmp84 = []
                            tmp84.append(subjects25.popleft())
                            while True:
                                if len(tmp84) > 1:
                                    tmp85 = create_operation_expression(associative1, tmp84)
                                elif len(tmp84) == 1:
                                    tmp85 = tmp84[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2.2', tmp85)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 33038
                                    if len(subjects25) == 0:
                                        pass
                                        # State 33039
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (x**m*(f + e*x**r))**p
                                if len(subjects25) == 0:
                                    break
                                tmp84.append(subjects25.popleft())
                            subjects25.extendleft(reversed(tmp84))
                subjects25.appendleft(tmp80)
            subjects.appendleft(tmp24)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
