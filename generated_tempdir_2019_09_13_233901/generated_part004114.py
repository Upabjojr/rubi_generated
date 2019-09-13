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

class CommutativeMatcher46124(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1, 2: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({3: 1, 4: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
]),
    3: (3, Multiset({3: 1, 5: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
]),
    4: (4, Multiset({6: 1, 7: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
]),
    5: (5, Multiset({8: 1, 9: 1}), [
      (VariableWithCount('i2.3.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher46124._instance is None:
            CommutativeMatcher46124._instance = CommutativeMatcher46124()
        return CommutativeMatcher46124._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 46123
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 46125
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 46126
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 46127
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 46128
                            if len(subjects2) >= 1:
                                tmp7 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2', tmp7)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46129
                                    if len(subjects2) == 0:
                                        pass
                                        # State 46130
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (c*x**n)**p
                                subjects2.appendleft(tmp7)
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp9 = subjects2.popleft()
                    subjects10 = deque(tmp9._args)
                    # State 46131
                    if len(subjects10) >= 1:
                        tmp11 = subjects10.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2.2.1', tmp11)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 46132
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 46133
                                if len(subjects10) == 0:
                                    pass
                                    # State 46134
                                    if len(subjects2) >= 1:
                                        tmp14 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i2.3.2.2', tmp14)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 46135
                                            if len(subjects2) == 0:
                                                pass
                                                # State 46136
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (c*x**n)**p
                                        subjects2.appendleft(tmp14)
                            if len(subjects10) >= 1:
                                tmp16 = subjects10.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i2.3.2.2.2', tmp16)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46133
                                    if len(subjects10) == 0:
                                        pass
                                        # State 46134
                                        if len(subjects2) >= 1:
                                            tmp18 = subjects2.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i2.3.2.2', tmp18)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 46135
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 46136
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (c*x**n)**p
                                            subjects2.appendleft(tmp18)
                                subjects10.appendleft(tmp16)
                        subjects10.appendleft(tmp11)
                    subjects2.appendleft(tmp9)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 46747
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 46748
                    if len(subjects2) >= 1:
                        tmp22 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0', tmp22)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 46749
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp24 = subjects2.popleft()
                                # State 46750
                                if len(subjects2) == 0:
                                    pass
                                    # State 46751
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/(c + x*d)
                                subjects2.appendleft(tmp24)
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 48918
                                if len(subjects2) == 0:
                                    pass
                                    # State 48919
                                    if len(subjects) == 0:
                                        pass
                                        # 8: (c + x*d)**n1
                            if len(subjects2) >= 1:
                                tmp26 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2', tmp26)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48918
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48919
                                        if len(subjects) == 0:
                                            pass
                                            # 8: (c + x*d)**n1
                                subjects2.appendleft(tmp26)
                        subjects2.appendleft(tmp22)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 47557
                    if len(subjects2) >= 1:
                        tmp29 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp29)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47558
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 47559
                                if len(subjects2) == 0:
                                    pass
                                    # State 47560
                                    if len(subjects) == 0:
                                        pass
                                        # 3: (x*b + a)**n1
                            if len(subjects2) >= 1:
                                tmp32 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2', tmp32)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47559
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47560
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (x*b + a)**n1
                                subjects2.appendleft(tmp32)
                        subjects2.appendleft(tmp29)
                    if len(subjects2) >= 1:
                        tmp34 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp34)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48467
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 48468
                                if len(subjects2) == 0:
                                    pass
                                    # State 48469
                                    if len(subjects) == 0:
                                        pass
                                        # 6: (x*b + a)**n1
                            if len(subjects2) >= 1:
                                tmp37 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2', tmp37)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48468
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48469
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (x*b + a)**n1
                                subjects2.appendleft(tmp37)
                        subjects2.appendleft(tmp34)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp39 = subjects2.popleft()
                    associative1 = tmp39
                    associative_type1 = type(tmp39)
                    subjects40 = deque(tmp39._args)
                    matcher = CommutativeMatcher46753.get()
                    tmp41 = subjects40
                    subjects40 = []
                    for s in tmp41:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp41, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 46754
                            if len(subjects2) >= 1 and subjects2[0] == -1:
                                tmp42 = subjects2.popleft()
                                # State 46755
                                if len(subjects2) == 0:
                                    pass
                                    # State 46756
                                    if len(subjects) == 0:
                                        pass
                                        # 1: 1/(c + x*d)
                                subjects2.appendleft(tmp42)
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 48920
                                if len(subjects2) == 0:
                                    pass
                                    # State 48921
                                    if len(subjects) == 0:
                                        pass
                                        # 8: (c + x*d)**n1
                            if len(subjects2) >= 1:
                                tmp44 = []
                                tmp44.append(subjects2.popleft())
                                while True:
                                    if len(tmp44) > 1:
                                        tmp45 = create_operation_expression(associative1, tmp44)
                                    elif len(tmp44) == 1:
                                        tmp45 = tmp44[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2', tmp45)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 48920
                                        if len(subjects2) == 0:
                                            pass
                                            # State 48921
                                            if len(subjects) == 0:
                                                pass
                                                # 8: (c + x*d)**n1
                                    if len(subjects2) == 0:
                                        break
                                    tmp44.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp44))
                        if pattern_index == 1:
                            pass
                            # State 47561
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 47562
                                if len(subjects2) == 0:
                                    pass
                                    # State 47563
                                    if len(subjects) == 0:
                                        pass
                                        # 3: (x*b + a)**n1
                            if len(subjects2) >= 1:
                                tmp48 = []
                                tmp48.append(subjects2.popleft())
                                while True:
                                    if len(tmp48) > 1:
                                        tmp49 = create_operation_expression(associative1, tmp48)
                                    elif len(tmp48) == 1:
                                        tmp49 = tmp48[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2', tmp49)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 47562
                                        if len(subjects2) == 0:
                                            pass
                                            # State 47563
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (x*b + a)**n1
                                    if len(subjects2) == 0:
                                        break
                                    tmp48.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp48))
                        if pattern_index == 2:
                            pass
                            # State 48470
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 48471
                                if len(subjects2) == 0:
                                    pass
                                    # State 48472
                                    if len(subjects) == 0:
                                        pass
                                        # 6: (x*b + a)**n1
                            if len(subjects2) >= 1:
                                tmp52 = []
                                tmp52.append(subjects2.popleft())
                                while True:
                                    if len(tmp52) > 1:
                                        tmp53 = create_operation_expression(associative1, tmp52)
                                    elif len(tmp52) == 1:
                                        tmp53 = tmp52[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2', tmp53)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 48471
                                        if len(subjects2) == 0:
                                            pass
                                            # State 48472
                                            if len(subjects) == 0:
                                                pass
                                                # 6: (x*b + a)**n1
                                    if len(subjects2) == 0:
                                        break
                                    tmp52.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp52))
                    subjects2.appendleft(tmp39)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.3.2.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 47570
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 47571
                    if len(subjects2) >= 1:
                        tmp57 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp57)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47572
                            if len(subjects2) >= 1:
                                tmp59 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2_1', tmp59)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47573
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47574
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (x*d + c)**n2
                                subjects2.appendleft(tmp59)
                        subjects2.appendleft(tmp57)
                    if len(subjects2) >= 1:
                        tmp61 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp61)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48478
                            if len(subjects2) >= 1:
                                tmp63 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2_1', tmp63)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48479
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48480
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (x*d + c)**n2
                                subjects2.appendleft(tmp63)
                        subjects2.appendleft(tmp61)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.2.2.1.0_2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 48924
                    if len(subjects2) >= 1:
                        tmp66 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.2.2.1.0', tmp66)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48925
                            if len(subjects2) >= 1:
                                tmp68 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2_1', tmp68)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48926
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48927
                                        if len(subjects) == 0:
                                            pass
                                            # 9: (c + x*d)**n2
                                subjects2.appendleft(tmp68)
                        subjects2.appendleft(tmp66)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp70 = subjects2.popleft()
                    associative1 = tmp70
                    associative_type1 = type(tmp70)
                    subjects71 = deque(tmp70._args)
                    matcher = CommutativeMatcher47576.get()
                    tmp72 = subjects71
                    subjects71 = []
                    for s in tmp72:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp72, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 47577
                            if len(subjects2) >= 1:
                                tmp73 = []
                                tmp73.append(subjects2.popleft())
                                while True:
                                    if len(tmp73) > 1:
                                        tmp74 = create_operation_expression(associative1, tmp73)
                                    elif len(tmp73) == 1:
                                        tmp74 = tmp73[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2_1', tmp74)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 47578
                                        if len(subjects2) == 0:
                                            pass
                                            # State 47579
                                            if len(subjects) == 0:
                                                pass
                                                # 4: (x*d + c)**n2
                                    if len(subjects2) == 0:
                                        break
                                    tmp73.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp73))
                        if pattern_index == 1:
                            pass
                            # State 48481
                            if len(subjects2) >= 1:
                                tmp76 = []
                                tmp76.append(subjects2.popleft())
                                while True:
                                    if len(tmp76) > 1:
                                        tmp77 = create_operation_expression(associative1, tmp76)
                                    elif len(tmp76) == 1:
                                        tmp77 = tmp76[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2_1', tmp77)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 48482
                                        if len(subjects2) == 0:
                                            pass
                                            # State 48483
                                            if len(subjects) == 0:
                                                pass
                                                # 7: (x*d + c)**n2
                                    if len(subjects2) == 0:
                                        break
                                    tmp76.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp76))
                        if pattern_index == 2:
                            pass
                            # State 48928
                            if len(subjects2) >= 1:
                                tmp79 = []
                                tmp79.append(subjects2.popleft())
                                while True:
                                    if len(tmp79) > 1:
                                        tmp80 = create_operation_expression(associative1, tmp79)
                                    elif len(tmp79) == 1:
                                        tmp80 = tmp79[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2_1', tmp80)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 48929
                                        if len(subjects2) == 0:
                                            pass
                                            # State 48930
                                            if len(subjects) == 0:
                                                pass
                                                # 9: (c + x*d)**n2
                                    if len(subjects2) == 0:
                                        break
                                    tmp79.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp79))
                    subjects2.appendleft(tmp70)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 48249
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 48250
                    if len(subjects2) >= 1:
                        tmp84 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp84)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48251
                            if len(subjects2) >= 1:
                                tmp86 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.2.2_1', tmp86)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48252
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48253
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (e + x*f)**n2
                                subjects2.appendleft(tmp86)
                        subjects2.appendleft(tmp84)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp88 = subjects2.popleft()
                    associative1 = tmp88
                    associative_type1 = type(tmp88)
                    subjects89 = deque(tmp88._args)
                    matcher = CommutativeMatcher48255.get()
                    tmp90 = subjects89
                    subjects89 = []
                    for s in tmp90:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp90, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 48256
                            if len(subjects2) >= 1:
                                tmp91 = []
                                tmp91.append(subjects2.popleft())
                                while True:
                                    if len(tmp91) > 1:
                                        tmp92 = create_operation_expression(associative1, tmp91)
                                    elif len(tmp91) == 1:
                                        tmp92 = tmp91[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.2.2_1', tmp92)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 48257
                                        if len(subjects2) == 0:
                                            pass
                                            # State 48258
                                            if len(subjects) == 0:
                                                pass
                                                # 5: (e + x*f)**n2
                                    if len(subjects2) == 0:
                                        break
                                    tmp91.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp91))
                    subjects2.appendleft(tmp88)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp94 = subjects2.popleft()
                associative1 = tmp94
                associative_type1 = type(tmp94)
                subjects95 = deque(tmp94._args)
                matcher = CommutativeMatcher46138.get()
                tmp96 = subjects95
                subjects95 = []
                for s in tmp96:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp96, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46145
                        if len(subjects2) >= 1:
                            tmp97 = []
                            tmp97.append(subjects2.popleft())
                            while True:
                                if len(tmp97) > 1:
                                    tmp98 = create_operation_expression(associative1, tmp97)
                                elif len(tmp97) == 1:
                                    tmp98 = tmp97[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2', tmp98)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46146
                                    if len(subjects2) == 0:
                                        pass
                                        # State 46147
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (c*x**n)**p
                                if len(subjects2) == 0:
                                    break
                                tmp97.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp97))
                subjects2.appendleft(tmp94)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp100 = subjects2.popleft()
                associative1 = tmp100
                associative_type1 = type(tmp100)
                subjects101 = deque(tmp100._args)
                matcher = CommutativeMatcher46758.get()
                tmp102 = subjects101
                subjects101 = []
                for s in tmp102:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp102, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46764
                        if len(subjects2) >= 1 and subjects2[0] == -1:
                            tmp103 = subjects2.popleft()
                            # State 46765
                            if len(subjects2) == 0:
                                pass
                                # State 46766
                                if len(subjects) == 0:
                                    pass
                                    # 1: 1/(c + x*d)
                            subjects2.appendleft(tmp103)
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48922
                            if len(subjects2) == 0:
                                pass
                                # State 48923
                                if len(subjects) == 0:
                                    pass
                                    # 8: (c + x*d)**n1
                        if len(subjects2) >= 1:
                            tmp105 = []
                            tmp105.append(subjects2.popleft())
                            while True:
                                if len(tmp105) > 1:
                                    tmp106 = create_operation_expression(associative1, tmp105)
                                elif len(tmp105) == 1:
                                    tmp106 = tmp105[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2', tmp106)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48922
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48923
                                        if len(subjects) == 0:
                                            pass
                                            # 8: (c + x*d)**n1
                                if len(subjects2) == 0:
                                    break
                                tmp105.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp105))
                    if pattern_index == 1:
                        pass
                        # State 47567
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47568
                            if len(subjects2) == 0:
                                pass
                                # State 47569
                                if len(subjects) == 0:
                                    pass
                                    # 3: (x*b + a)**n1
                        if len(subjects2) >= 1:
                            tmp109 = []
                            tmp109.append(subjects2.popleft())
                            while True:
                                if len(tmp109) > 1:
                                    tmp110 = create_operation_expression(associative1, tmp109)
                                elif len(tmp109) == 1:
                                    tmp110 = tmp109[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2', tmp110)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47568
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47569
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (x*b + a)**n1
                                if len(subjects2) == 0:
                                    break
                                tmp109.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp109))
                    if pattern_index == 2:
                        pass
                        # State 47582
                        if len(subjects2) >= 1:
                            tmp112 = []
                            tmp112.append(subjects2.popleft())
                            while True:
                                if len(tmp112) > 1:
                                    tmp113 = create_operation_expression(associative1, tmp112)
                                elif len(tmp112) == 1:
                                    tmp113 = tmp112[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2_1', tmp113)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47583
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47584
                                        if len(subjects) == 0:
                                            pass
                                            # 4: (x*d + c)**n2
                                if len(subjects2) == 0:
                                    break
                                tmp112.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp112))
                    if pattern_index == 3:
                        pass
                        # State 48262
                        if len(subjects2) >= 1:
                            tmp115 = []
                            tmp115.append(subjects2.popleft())
                            while True:
                                if len(tmp115) > 1:
                                    tmp116 = create_operation_expression(associative1, tmp115)
                                elif len(tmp115) == 1:
                                    tmp116 = tmp115[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2_1', tmp116)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48263
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48264
                                        if len(subjects) == 0:
                                            pass
                                            # 5: (e + x*f)**n2
                                if len(subjects2) == 0:
                                    break
                                tmp115.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp115))
                    if pattern_index == 4:
                        pass
                        # State 48475
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.3.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48476
                            if len(subjects2) == 0:
                                pass
                                # State 48477
                                if len(subjects) == 0:
                                    pass
                                    # 6: (x*b + a)**n1
                        if len(subjects2) >= 1:
                            tmp119 = []
                            tmp119.append(subjects2.popleft())
                            while True:
                                if len(tmp119) > 1:
                                    tmp120 = create_operation_expression(associative1, tmp119)
                                elif len(tmp119) == 1:
                                    tmp120 = tmp119[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2', tmp120)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48476
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48477
                                        if len(subjects) == 0:
                                            pass
                                            # 6: (x*b + a)**n1
                                if len(subjects2) == 0:
                                    break
                                tmp119.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp119))
                    if pattern_index == 5:
                        pass
                        # State 48486
                        if len(subjects2) >= 1:
                            tmp122 = []
                            tmp122.append(subjects2.popleft())
                            while True:
                                if len(tmp122) > 1:
                                    tmp123 = create_operation_expression(associative1, tmp122)
                                elif len(tmp122) == 1:
                                    tmp123 = tmp122[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2_1', tmp123)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48487
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48488
                                        if len(subjects) == 0:
                                            pass
                                            # 7: (x*d + c)**n2
                                if len(subjects2) == 0:
                                    break
                                tmp122.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp122))
                    if pattern_index == 6:
                        pass
                        # State 48934
                        if len(subjects2) >= 1:
                            tmp125 = []
                            tmp125.append(subjects2.popleft())
                            while True:
                                if len(tmp125) > 1:
                                    tmp126 = create_operation_expression(associative1, tmp125)
                                elif len(tmp125) == 1:
                                    tmp126 = tmp125[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.3.2.2_1', tmp126)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48935
                                    if len(subjects2) == 0:
                                        pass
                                        # State 48936
                                        if len(subjects) == 0:
                                            pass
                                            # 9: (c + x*d)**n2
                                if len(subjects2) == 0:
                                    break
                                tmp125.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp125))
                subjects2.appendleft(tmp100)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 46767
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.2.1.1.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 46768
                if len(subjects) >= 1:
                    tmp130 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.2.2.1.0', tmp130)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 46769
                        if len(subjects) == 0:
                            pass
                            # 2: a + b*x
                    subjects.appendleft(tmp130)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp132 = subjects.popleft()
                associative1 = tmp132
                associative_type1 = type(tmp132)
                subjects133 = deque(tmp132._args)
                matcher = CommutativeMatcher46771.get()
                tmp134 = subjects133
                subjects133 = []
                for s in tmp134:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp134, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46772
                        if len(subjects) == 0:
                            pass
                            # 2: a + b*x
                subjects.appendleft(tmp132)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 47542
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 47543
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.3.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 47544
                    if len(subjects) >= 1:
                        tmp138 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.0', tmp138)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47545
                            if len(subjects) == 0:
                                pass
                                # 3: (x*b + a)**n1
                        subjects.appendleft(tmp138)
                    if len(subjects) >= 1:
                        tmp140 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.1', tmp140)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48462
                            if len(subjects) == 0:
                                pass
                                # 6: (x*b + a)**n1
                        subjects.appendleft(tmp140)
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.3.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 48911
                    if len(subjects) >= 1:
                        tmp143 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.3.2.2.1.0', tmp143)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48912
                            if len(subjects) == 0:
                                pass
                                # 8: (c + x*d)**n1
                        subjects.appendleft(tmp143)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp145 = subjects.popleft()
                    associative1 = tmp145
                    associative_type1 = type(tmp145)
                    subjects146 = deque(tmp145._args)
                    matcher = CommutativeMatcher47547.get()
                    tmp147 = subjects146
                    subjects146 = []
                    for s in tmp147:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp147, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 47548
                            if len(subjects) == 0:
                                pass
                                # 3: (x*b + a)**n1
                        if pattern_index == 1:
                            pass
                            # State 48463
                            if len(subjects) == 0:
                                pass
                                # 6: (x*b + a)**n1
                        if pattern_index == 2:
                            pass
                            # State 48913
                            if len(subjects) == 0:
                                pass
                                # 8: (c + x*d)**n1
                    subjects.appendleft(tmp145)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp148 = subjects.popleft()
                associative1 = tmp148
                associative_type1 = type(tmp148)
                subjects149 = deque(tmp148._args)
                matcher = CommutativeMatcher47550.get()
                tmp150 = subjects149
                subjects149 = []
                for s in tmp150:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp150, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 47556
                        if len(subjects) == 0:
                            pass
                            # 3: (x*b + a)**n1
                    if pattern_index == 1:
                        pass
                        # State 48466
                        if len(subjects) == 0:
                            pass
                            # 6: (x*b + a)**n1
                    if pattern_index == 2:
                        pass
                        # State 48917
                        if len(subjects) == 0:
                            pass
                            # 8: (c + x*d)**n1
                subjects.appendleft(tmp148)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp151 = subjects.popleft()
            associative1 = tmp151
            associative_type1 = type(tmp151)
            subjects152 = deque(tmp151._args)
            matcher = CommutativeMatcher46774.get()
            tmp153 = subjects152
            subjects152 = []
            for s in tmp153:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp153, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 46780
                    if len(subjects) == 0:
                        pass
                        # 2: a + b*x
            subjects.appendleft(tmp151)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
