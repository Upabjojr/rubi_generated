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

class CommutativeMatcher42597(CommutativeMatcher):
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
        if CommutativeMatcher42597._instance is None:
            CommutativeMatcher42597._instance = CommutativeMatcher42597()
        return CommutativeMatcher42597._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 42596
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 42598
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 42599
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 42600
                    if len(subjects) >= 1 and isinstance(subjects[0], Add):
                        tmp4 = subjects.popleft()
                        associative1 = tmp4
                        associative_type1 = type(tmp4)
                        subjects5 = deque(tmp4._args)
                        matcher = CommutativeMatcher42602.get()
                        tmp6 = subjects5
                        subjects5 = []
                        for s in tmp6:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp6, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 42618
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + f*x + g*x**2)**p)**q
                            if pattern_index == 1:
                                pass
                                # State 54658
                                if len(subjects) == 0:
                                    pass
                                    # 2: (d*(e + x*f)**p)**q
                        subjects.appendleft(tmp4)
                    if len(subjects) >= 1:
                        tmp7 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.1', tmp7)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45245
                            if len(subjects) == 0:
                                pass
                                # 1: (d*v**p)**q
                        subjects.appendleft(tmp7)
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 54650
                        subst5 = Substitution(subst4)
                        try:
                            subst5.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 54651
                            if len(subjects) >= 1:
                                tmp11 = subjects.popleft()
                                subst6 = Substitution(subst5)
                                try:
                                    subst6.try_add_variable('i2.2.1.2.2.2.1.0', tmp11)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54652
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (d*(e + x*f)**p)**q
                                subjects.appendleft(tmp11)
                        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                            tmp13 = subjects.popleft()
                            associative1 = tmp13
                            associative_type1 = type(tmp13)
                            subjects14 = deque(tmp13._args)
                            matcher = CommutativeMatcher54654.get()
                            tmp15 = subjects14
                            subjects14 = []
                            for s in tmp15:
                                matcher.add_subject(s)
                            for pattern_index, subst5 in matcher.match(tmp15, subst4):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 54655
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (d*(e + x*f)**p)**q
                            subjects.appendleft(tmp13)
                if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                    tmp16 = subjects.popleft()
                    subjects17 = deque(tmp16._args)
                    # State 42619
                    if len(subjects17) >= 1 and isinstance(subjects17[0], Add):
                        tmp18 = subjects17.popleft()
                        associative1 = tmp18
                        associative_type1 = type(tmp18)
                        subjects19 = deque(tmp18._args)
                        matcher = CommutativeMatcher42621.get()
                        tmp20 = subjects19
                        subjects19 = []
                        for s in tmp20:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp20, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 42637
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 42638
                                    if len(subjects17) == 0:
                                        pass
                                        # State 42639
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + f*x + g*x**2)**p)**q
                                if len(subjects17) >= 1:
                                    tmp22 = []
                                    tmp22.append(subjects17.popleft())
                                    while True:
                                        if len(tmp22) > 1:
                                            tmp23 = create_operation_expression(associative1, tmp22)
                                        elif len(tmp22) == 1:
                                            tmp23 = tmp22[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp23)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 42638
                                            if len(subjects17) == 0:
                                                pass
                                                # State 42639
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + f*x + g*x**2)**p)**q
                                        if len(subjects17) == 0:
                                            break
                                        tmp22.append(subjects17.popleft())
                                    subjects17.extendleft(reversed(tmp22))
                            if pattern_index == 1:
                                pass
                                # State 54671
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54672
                                    if len(subjects17) == 0:
                                        pass
                                        # State 54673
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (d*(e + x*f)**p)**q
                                if len(subjects17) >= 1:
                                    tmp26 = []
                                    tmp26.append(subjects17.popleft())
                                    while True:
                                        if len(tmp26) > 1:
                                            tmp27 = create_operation_expression(associative1, tmp26)
                                        elif len(tmp26) == 1:
                                            tmp27 = tmp26[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2.2', tmp27)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54672
                                            if len(subjects17) == 0:
                                                pass
                                                # State 54673
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: (d*(e + x*f)**p)**q
                                        if len(subjects17) == 0:
                                            break
                                        tmp26.append(subjects17.popleft())
                                    subjects17.extendleft(reversed(tmp26))
                        subjects17.appendleft(tmp18)
                    if len(subjects17) >= 1:
                        tmp29 = subjects17.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1', tmp29)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45246
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45247
                                if len(subjects17) == 0:
                                    pass
                                    # State 45248
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (d*v**p)**q
                            if len(subjects17) >= 1:
                                tmp32 = subjects17.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2', tmp32)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45247
                                    if len(subjects17) == 0:
                                        pass
                                        # State 45248
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q
                                subjects17.appendleft(tmp32)
                        subjects17.appendleft(tmp29)
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 54659
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 54660
                            if len(subjects17) >= 1:
                                tmp36 = subjects17.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp36)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54661
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54662
                                        if len(subjects17) == 0:
                                            pass
                                            # State 54663
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (d*(e + x*f)**p)**q
                                    if len(subjects17) >= 1:
                                        tmp39 = subjects17.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2.2', tmp39)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54662
                                            if len(subjects17) == 0:
                                                pass
                                                # State 54663
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: (d*(e + x*f)**p)**q
                                        subjects17.appendleft(tmp39)
                                subjects17.appendleft(tmp36)
                        if len(subjects17) >= 1 and isinstance(subjects17[0], Mul):
                            tmp41 = subjects17.popleft()
                            associative1 = tmp41
                            associative_type1 = type(tmp41)
                            subjects42 = deque(tmp41._args)
                            matcher = CommutativeMatcher54665.get()
                            tmp43 = subjects42
                            subjects42 = []
                            for s in tmp43:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp43, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 54666
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54667
                                        if len(subjects17) == 0:
                                            pass
                                            # State 54668
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (d*(e + x*f)**p)**q
                                    if len(subjects17) >= 1:
                                        tmp45 = []
                                        tmp45.append(subjects17.popleft())
                                        while True:
                                            if len(tmp45) > 1:
                                                tmp46 = create_operation_expression(associative1, tmp45)
                                            elif len(tmp45) == 1:
                                                tmp46 = tmp45[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2.2', tmp46)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54667
                                                if len(subjects17) == 0:
                                                    pass
                                                    # State 54668
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: (d*(e + x*f)**p)**q
                                            if len(subjects17) == 0:
                                                break
                                            tmp45.append(subjects17.popleft())
                                        subjects17.extendleft(reversed(tmp45))
                            subjects17.appendleft(tmp41)
                    subjects.appendleft(tmp16)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp48 = subjects.popleft()
                associative1 = tmp48
                associative_type1 = type(tmp48)
                subjects49 = deque(tmp48._args)
                matcher = CommutativeMatcher42641.get()
                tmp50 = subjects49
                subjects49 = []
                for s in tmp50:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp50, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 42682
                        if len(subjects) == 0:
                            pass
                            # 0: (d*(e + f*x + g*x**2)**p)**q
                    if pattern_index == 1:
                        pass
                        # State 45253
                        if len(subjects) == 0:
                            pass
                            # 1: (d*v**p)**q
                    if pattern_index == 2:
                        pass
                        # State 54698
                        if len(subjects) == 0:
                            pass
                            # 2: (d*(e + x*f)**p)**q
                subjects.appendleft(tmp48)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp51 = subjects.popleft()
            subjects52 = deque(tmp51._args)
            # State 42683
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.1.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 42684
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 42685
                    if len(subjects52) >= 1 and isinstance(subjects52[0], Add):
                        tmp55 = subjects52.popleft()
                        associative1 = tmp55
                        associative_type1 = type(tmp55)
                        subjects56 = deque(tmp55._args)
                        matcher = CommutativeMatcher42687.get()
                        tmp57 = subjects56
                        subjects56 = []
                        for s in tmp57:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp57, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 42703
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 42704
                                    if len(subjects52) == 0:
                                        pass
                                        # State 42705
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + f*x + g*x**2)**p)**q
                                if len(subjects52) >= 1:
                                    tmp59 = []
                                    tmp59.append(subjects52.popleft())
                                    while True:
                                        if len(tmp59) > 1:
                                            tmp60 = create_operation_expression(associative1, tmp59)
                                        elif len(tmp59) == 1:
                                            tmp60 = tmp59[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp60)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 42704
                                            if len(subjects52) == 0:
                                                pass
                                                # State 42705
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + f*x + g*x**2)**p)**q
                                        if len(subjects52) == 0:
                                            break
                                        tmp59.append(subjects52.popleft())
                                    subjects52.extendleft(reversed(tmp59))
                            if pattern_index == 1:
                                pass
                                # State 54711
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54712
                                    if len(subjects52) == 0:
                                        pass
                                        # State 54713
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (d*(e + x*f)**p)**q
                                if len(subjects52) >= 1:
                                    tmp63 = []
                                    tmp63.append(subjects52.popleft())
                                    while True:
                                        if len(tmp63) > 1:
                                            tmp64 = create_operation_expression(associative1, tmp63)
                                        elif len(tmp63) == 1:
                                            tmp64 = tmp63[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp64)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54712
                                            if len(subjects52) == 0:
                                                pass
                                                # State 54713
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: (d*(e + x*f)**p)**q
                                        if len(subjects52) == 0:
                                            break
                                        tmp63.append(subjects52.popleft())
                                    subjects52.extendleft(reversed(tmp63))
                        subjects52.appendleft(tmp55)
                    if len(subjects52) >= 1:
                        tmp66 = subjects52.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.1', tmp66)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45254
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.1.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45255
                                if len(subjects52) == 0:
                                    pass
                                    # State 45256
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (d*v**p)**q
                            if len(subjects52) >= 1:
                                tmp69 = subjects52.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2', tmp69)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45255
                                    if len(subjects52) == 0:
                                        pass
                                        # State 45256
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q
                                subjects52.appendleft(tmp69)
                        subjects52.appendleft(tmp66)
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 54699
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 54700
                            if len(subjects52) >= 1:
                                tmp73 = subjects52.popleft()
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i2.2.1.2.2.2.1.0', tmp73)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54701
                                    subst6 = Substitution(subst5)
                                    try:
                                        subst6.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54702
                                        if len(subjects52) == 0:
                                            pass
                                            # State 54703
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (d*(e + x*f)**p)**q
                                    if len(subjects52) >= 1:
                                        tmp76 = subjects52.popleft()
                                        subst6 = Substitution(subst5)
                                        try:
                                            subst6.try_add_variable('i2.2.1.2.2', tmp76)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54702
                                            if len(subjects52) == 0:
                                                pass
                                                # State 54703
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: (d*(e + x*f)**p)**q
                                        subjects52.appendleft(tmp76)
                                subjects52.appendleft(tmp73)
                        if len(subjects52) >= 1 and isinstance(subjects52[0], Mul):
                            tmp78 = subjects52.popleft()
                            associative1 = tmp78
                            associative_type1 = type(tmp78)
                            subjects79 = deque(tmp78._args)
                            matcher = CommutativeMatcher54705.get()
                            tmp80 = subjects79
                            subjects79 = []
                            for s in tmp80:
                                matcher.add_subject(s)
                            for pattern_index, subst4 in matcher.match(tmp80, subst3):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 54706
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54707
                                        if len(subjects52) == 0:
                                            pass
                                            # State 54708
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (d*(e + x*f)**p)**q
                                    if len(subjects52) >= 1:
                                        tmp82 = []
                                        tmp82.append(subjects52.popleft())
                                        while True:
                                            if len(tmp82) > 1:
                                                tmp83 = create_operation_expression(associative1, tmp82)
                                            elif len(tmp82) == 1:
                                                tmp83 = tmp82[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', tmp83)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54707
                                                if len(subjects52) == 0:
                                                    pass
                                                    # State 54708
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: (d*(e + x*f)**p)**q
                                            if len(subjects52) == 0:
                                                break
                                            tmp82.append(subjects52.popleft())
                                        subjects52.extendleft(reversed(tmp82))
                            subjects52.appendleft(tmp78)
                if len(subjects52) >= 1 and isinstance(subjects52[0], Pow):
                    tmp85 = subjects52.popleft()
                    subjects86 = deque(tmp85._args)
                    # State 42706
                    if len(subjects86) >= 1 and isinstance(subjects86[0], Add):
                        tmp87 = subjects86.popleft()
                        associative1 = tmp87
                        associative_type1 = type(tmp87)
                        subjects88 = deque(tmp87._args)
                        matcher = CommutativeMatcher42708.get()
                        tmp89 = subjects88
                        subjects88 = []
                        for s in tmp89:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp89, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 42724
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 42725
                                    if len(subjects86) == 0:
                                        pass
                                        # State 42726
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 42727
                                            if len(subjects52) == 0:
                                                pass
                                                # State 42728
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (d*(e + f*x + g*x**2)**p)**q
                                        if len(subjects52) >= 1:
                                            tmp92 = subjects52.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp92)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 42727
                                                if len(subjects52) == 0:
                                                    pass
                                                    # State 42728
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (d*(e + f*x + g*x**2)**p)**q
                                            subjects52.appendleft(tmp92)
                                if len(subjects86) >= 1:
                                    tmp94 = []
                                    tmp94.append(subjects86.popleft())
                                    while True:
                                        if len(tmp94) > 1:
                                            tmp95 = create_operation_expression(associative1, tmp94)
                                        elif len(tmp94) == 1:
                                            tmp95 = tmp94[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp95)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 42725
                                            if len(subjects86) == 0:
                                                pass
                                                # State 42726
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 42727
                                                    if len(subjects52) == 0:
                                                        pass
                                                        # State 42728
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 0: (d*(e + f*x + g*x**2)**p)**q
                                                if len(subjects52) >= 1:
                                                    tmp98 = subjects52.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp98)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 42727
                                                        if len(subjects52) == 0:
                                                            pass
                                                            # State 42728
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (d*(e + f*x + g*x**2)**p)**q
                                                    subjects52.appendleft(tmp98)
                                        if len(subjects86) == 0:
                                            break
                                        tmp94.append(subjects86.popleft())
                                    subjects86.extendleft(reversed(tmp94))
                            if pattern_index == 1:
                                pass
                                # State 54730
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54731
                                    if len(subjects86) == 0:
                                        pass
                                        # State 54732
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54733
                                            if len(subjects52) == 0:
                                                pass
                                                # State 54734
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: (d*(e + x*f)**p)**q
                                        if len(subjects52) >= 1:
                                            tmp102 = subjects52.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp102)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54733
                                                if len(subjects52) == 0:
                                                    pass
                                                    # State 54734
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: (d*(e + x*f)**p)**q
                                            subjects52.appendleft(tmp102)
                                if len(subjects86) >= 1:
                                    tmp104 = []
                                    tmp104.append(subjects86.popleft())
                                    while True:
                                        if len(tmp104) > 1:
                                            tmp105 = create_operation_expression(associative1, tmp104)
                                        elif len(tmp104) == 1:
                                            tmp105 = tmp104[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i2.2.1.2.2.2', tmp105)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54731
                                            if len(subjects86) == 0:
                                                pass
                                                # State 54732
                                                subst4 = Substitution(subst3)
                                                try:
                                                    subst4.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54733
                                                    if len(subjects52) == 0:
                                                        pass
                                                        # State 54734
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: (d*(e + x*f)**p)**q
                                                if len(subjects52) >= 1:
                                                    tmp108 = subjects52.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i2.2.1.2.2', tmp108)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54733
                                                        if len(subjects52) == 0:
                                                            pass
                                                            # State 54734
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: (d*(e + x*f)**p)**q
                                                    subjects52.appendleft(tmp108)
                                        if len(subjects86) == 0:
                                            break
                                        tmp104.append(subjects86.popleft())
                                    subjects86.extendleft(reversed(tmp104))
                        subjects86.appendleft(tmp87)
                    if len(subjects86) >= 1:
                        tmp110 = subjects86.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2.1', tmp110)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45257
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.1.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45258
                                if len(subjects86) == 0:
                                    pass
                                    # State 45259
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45260
                                        if len(subjects52) == 0:
                                            pass
                                            # State 45261
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (d*v**p)**q
                                    if len(subjects52) >= 1:
                                        tmp114 = subjects52.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', tmp114)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45260
                                            if len(subjects52) == 0:
                                                pass
                                                # State 45261
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*v**p)**q
                                        subjects52.appendleft(tmp114)
                            if len(subjects86) >= 1:
                                tmp116 = subjects86.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.2.1.2.2.2', tmp116)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45258
                                    if len(subjects86) == 0:
                                        pass
                                        # State 45259
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.2.1.2.2', 1)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45260
                                            if len(subjects52) == 0:
                                                pass
                                                # State 45261
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: (d*v**p)**q
                                        if len(subjects52) >= 1:
                                            tmp119 = subjects52.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2', tmp119)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45260
                                                if len(subjects52) == 0:
                                                    pass
                                                    # State 45261
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 1: (d*v**p)**q
                                            subjects52.appendleft(tmp119)
                                subjects86.appendleft(tmp116)
                        subjects86.appendleft(tmp110)
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.2.1.2.2.2.0', S(0))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 54714
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.2.2.2.1.0_1', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 54715
                            if len(subjects86) >= 1:
                                tmp123 = subjects86.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.1.2.2.2.1.0', tmp123)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54716
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54717
                                        if len(subjects86) == 0:
                                            pass
                                            # State 54718
                                            subst6 = Substitution(subst5)
                                            try:
                                                subst6.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54719
                                                if len(subjects52) == 0:
                                                    pass
                                                    # State 54720
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: (d*(e + x*f)**p)**q
                                            if len(subjects52) >= 1:
                                                tmp127 = subjects52.popleft()
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', tmp127)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54719
                                                    if len(subjects52) == 0:
                                                        pass
                                                        # State 54720
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: (d*(e + x*f)**p)**q
                                                subjects52.appendleft(tmp127)
                                    if len(subjects86) >= 1:
                                        tmp129 = subjects86.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i2.2.1.2.2.2', tmp129)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 54717
                                            if len(subjects86) == 0:
                                                pass
                                                # State 54718
                                                subst6 = Substitution(subst5)
                                                try:
                                                    subst6.try_add_variable('i2.2.1.2.2', 1)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54719
                                                    if len(subjects52) == 0:
                                                        pass
                                                        # State 54720
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: (d*(e + x*f)**p)**q
                                                if len(subjects52) >= 1:
                                                    tmp132 = subjects52.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i2.2.1.2.2', tmp132)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54719
                                                        if len(subjects52) == 0:
                                                            pass
                                                            # State 54720
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: (d*(e + x*f)**p)**q
                                                    subjects52.appendleft(tmp132)
                                        subjects86.appendleft(tmp129)
                                subjects86.appendleft(tmp123)
                        if len(subjects86) >= 1 and isinstance(subjects86[0], Mul):
                            tmp134 = subjects86.popleft()
                            associative1 = tmp134
                            associative_type1 = type(tmp134)
                            subjects135 = deque(tmp134._args)
                            matcher = CommutativeMatcher54722.get()
                            tmp136 = subjects135
                            subjects135 = []
                            for s in tmp136:
                                matcher.add_subject(s)
                            for pattern_index, subst3 in matcher.match(tmp136, subst2):
                                pass
                                if pattern_index == 0:
                                    pass
                                    # State 54723
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.2.1.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 54724
                                        if len(subjects86) == 0:
                                            pass
                                            # State 54725
                                            subst5 = Substitution(subst4)
                                            try:
                                                subst5.try_add_variable('i2.2.1.2.2', 1)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54726
                                                if len(subjects52) == 0:
                                                    pass
                                                    # State 54727
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 2: (d*(e + x*f)**p)**q
                                            if len(subjects52) >= 1:
                                                tmp139 = subjects52.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i2.2.1.2.2', tmp139)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 54726
                                                    if len(subjects52) == 0:
                                                        pass
                                                        # State 54727
                                                        if len(subjects) == 0:
                                                            pass
                                                            # 2: (d*(e + x*f)**p)**q
                                                subjects52.appendleft(tmp139)
                                    if len(subjects86) >= 1:
                                        tmp141 = []
                                        tmp141.append(subjects86.popleft())
                                        while True:
                                            if len(tmp141) > 1:
                                                tmp142 = create_operation_expression(associative1, tmp141)
                                            elif len(tmp141) == 1:
                                                tmp142 = tmp141[0]
                                            else:
                                                assert False, "Unreachable"
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.2.1.2.2.2', tmp142)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 54724
                                                if len(subjects86) == 0:
                                                    pass
                                                    # State 54725
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i2.2.1.2.2', 1)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 54726
                                                        if len(subjects52) == 0:
                                                            pass
                                                            # State 54727
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 2: (d*(e + x*f)**p)**q
                                                    if len(subjects52) >= 1:
                                                        tmp145 = subjects52.popleft()
                                                        subst5 = Substitution(subst4)
                                                        try:
                                                            subst5.try_add_variable('i2.2.1.2.2', tmp145)
                                                        except ValueError:
                                                            pass
                                                        else:
                                                            pass
                                                            # State 54726
                                                            if len(subjects52) == 0:
                                                                pass
                                                                # State 54727
                                                                if len(subjects) == 0:
                                                                    pass
                                                                    # 2: (d*(e + x*f)**p)**q
                                                        subjects52.appendleft(tmp145)
                                            if len(subjects86) == 0:
                                                break
                                            tmp141.append(subjects86.popleft())
                                        subjects86.extendleft(reversed(tmp141))
                            subjects86.appendleft(tmp134)
                    subjects52.appendleft(tmp85)
            if len(subjects52) >= 1 and isinstance(subjects52[0], Mul):
                tmp147 = subjects52.popleft()
                associative1 = tmp147
                associative_type1 = type(tmp147)
                subjects148 = deque(tmp147._args)
                matcher = CommutativeMatcher42730.get()
                tmp149 = subjects148
                subjects148 = []
                for s in tmp149:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp149, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 42771
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 42772
                            if len(subjects52) == 0:
                                pass
                                # State 42773
                                if len(subjects) == 0:
                                    pass
                                    # 0: (d*(e + f*x + g*x**2)**p)**q
                        if len(subjects52) >= 1:
                            tmp151 = []
                            tmp151.append(subjects52.popleft())
                            while True:
                                if len(tmp151) > 1:
                                    tmp152 = create_operation_expression(associative1, tmp151)
                                elif len(tmp151) == 1:
                                    tmp152 = tmp151[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp152)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 42772
                                    if len(subjects52) == 0:
                                        pass
                                        # State 42773
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (d*(e + f*x + g*x**2)**p)**q
                                if len(subjects52) == 0:
                                    break
                                tmp151.append(subjects52.popleft())
                            subjects52.extendleft(reversed(tmp151))
                    if pattern_index == 1:
                        pass
                        # State 45266
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45267
                            if len(subjects52) == 0:
                                pass
                                # State 45268
                                if len(subjects) == 0:
                                    pass
                                    # 1: (d*v**p)**q
                        if len(subjects52) >= 1:
                            tmp155 = []
                            tmp155.append(subjects52.popleft())
                            while True:
                                if len(tmp155) > 1:
                                    tmp156 = create_operation_expression(associative1, tmp155)
                                elif len(tmp155) == 1:
                                    tmp156 = tmp155[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp156)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45267
                                    if len(subjects52) == 0:
                                        pass
                                        # State 45268
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (d*v**p)**q
                                if len(subjects52) == 0:
                                    break
                                tmp155.append(subjects52.popleft())
                            subjects52.extendleft(reversed(tmp155))
                    if pattern_index == 2:
                        pass
                        # State 54759
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.1.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 54760
                            if len(subjects52) == 0:
                                pass
                                # State 54761
                                if len(subjects) == 0:
                                    pass
                                    # 2: (d*(e + x*f)**p)**q
                        if len(subjects52) >= 1:
                            tmp159 = []
                            tmp159.append(subjects52.popleft())
                            while True:
                                if len(tmp159) > 1:
                                    tmp160 = create_operation_expression(associative1, tmp159)
                                elif len(tmp159) == 1:
                                    tmp160 = tmp159[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.1.2.2', tmp160)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 54760
                                    if len(subjects52) == 0:
                                        pass
                                        # State 54761
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (d*(e + x*f)**p)**q
                                if len(subjects52) == 0:
                                    break
                                tmp159.append(subjects52.popleft())
                            subjects52.extendleft(reversed(tmp159))
                subjects52.appendleft(tmp147)
            subjects.appendleft(tmp51)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque