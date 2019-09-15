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


class CommutativeMatcher45849(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i4.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1, 2: 1}), [
      (VariableWithCount('i4.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher45849._instance is None:
            CommutativeMatcher45849._instance = CommutativeMatcher45849()
        return CommutativeMatcher45849._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 45848
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 45850
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 45851
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.2.2.2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 45852
                    if len(subjects2) >= 1:
                        tmp5 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.2.2.1', tmp5)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45853
                            if len(subjects2) >= 1:
                                tmp7 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i4.2.2', tmp7)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45854
                                    if len(subjects2) == 0:
                                        pass
                                        # State 45855
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (c*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                            yield 0, subst4
                                subjects2.appendleft(tmp7)
                        subjects2.appendleft(tmp5)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp9 = subjects2.popleft()
                    subjects10 = deque(tmp9._args)
                    # State 45856
                    if len(subjects10) >= 1:
                        tmp11 = subjects10.popleft()
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i4.2.2.1', tmp11)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45857
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i4.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 45858
                                if len(subjects10) == 0:
                                    pass
                                    # State 45859
                                    if len(subjects2) >= 1:
                                        tmp14 = subjects2.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i4.2.2', tmp14)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45860
                                            if len(subjects2) == 0:
                                                pass
                                                # State 45861
                                                if len(subjects) == 0:
                                                    pass
                                                    # 0: (c*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                                    yield 0, subst4
                                        subjects2.appendleft(tmp14)
                            if len(subjects10) >= 1:
                                tmp16 = subjects10.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i4.2.2.2', tmp16)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45858
                                    if len(subjects10) == 0:
                                        pass
                                        # State 45859
                                        if len(subjects2) >= 1:
                                            tmp18 = subjects2.popleft()
                                            subst4 = Substitution(subst3)
                                            try:
                                                subst4.try_add_variable('i4.2.2', tmp18)
                                            except ValueError:
                                                pass
                                            else:
                                                pass
                                                # State 45860
                                                if len(subjects2) == 0:
                                                    pass
                                                    # State 45861
                                                    if len(subjects) == 0:
                                                        pass
                                                        # 0: (c*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                                        yield 0, subst4
                                            subjects2.appendleft(tmp18)
                                subjects10.appendleft(tmp16)
                        subjects10.appendleft(tmp11)
                    subjects2.appendleft(tmp9)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 47100
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 47101
                    if len(subjects2) >= 1:
                        tmp22 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.2.2.1.0', tmp22)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47102
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i4.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 47103
                                if len(subjects2) == 0:
                                    pass
                                    # State 47104
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (a + x*b)**n1 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                        yield 1, subst4
                            if len(subjects2) >= 1:
                                tmp25 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i4.2.2', tmp25)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47103
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47104
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (a + x*b)**n1 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                            yield 1, subst4
                                subjects2.appendleft(tmp25)
                        subjects2.appendleft(tmp22)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp27 = subjects2.popleft()
                    associative1 = tmp27
                    associative_type1 = type(tmp27)
                    subjects28 = deque(tmp27._args)
                    matcher = CommutativeMatcher47106.get()
                    tmp29 = subjects28
                    subjects28 = []
                    for s in tmp29:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp29, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 47107
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i4.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 47108
                                if len(subjects2) == 0:
                                    pass
                                    # State 47109
                                    if len(subjects) == 0:
                                        pass
                                        # 1: (a + x*b)**n1 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                        yield 1, subst3
                            if len(subjects2) >= 1:
                                tmp31 = []
                                tmp31.append(subjects2.popleft())
                                while True:
                                    if len(tmp31) > 1:
                                        tmp32 = create_operation_expression(associative1, tmp31)
                                    elif len(tmp31) == 1:
                                        tmp32 = tmp31[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i4.2.2', tmp32)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 47108
                                        if len(subjects2) == 0:
                                            pass
                                            # State 47109
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (a + x*b)**n1 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                                yield 1, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp31.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp31))
                    subjects2.appendleft(tmp27)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 47120
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.2.2.1.0_2', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 47121
                    if len(subjects2) >= 1:
                        tmp36 = subjects2.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.2.2.1.0', tmp36)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47122
                            if len(subjects2) >= 1:
                                tmp38 = subjects2.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i4.2.2_1', tmp38)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47123
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47124
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (c + x*d)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                            yield 2, subst4
                                subjects2.appendleft(tmp38)
                        subjects2.appendleft(tmp36)
                if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                    tmp40 = subjects2.popleft()
                    associative1 = tmp40
                    associative_type1 = type(tmp40)
                    subjects41 = deque(tmp40._args)
                    matcher = CommutativeMatcher47126.get()
                    tmp42 = subjects41
                    subjects41 = []
                    for s in tmp42:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp42, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 47127
                            if len(subjects2) >= 1:
                                tmp43 = []
                                tmp43.append(subjects2.popleft())
                                while True:
                                    if len(tmp43) > 1:
                                        tmp44 = create_operation_expression(associative1, tmp43)
                                    elif len(tmp43) == 1:
                                        tmp44 = tmp43[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i4.2.2_1', tmp44)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 47128
                                        if len(subjects2) == 0:
                                            pass
                                            # State 47129
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (c + x*d)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                                yield 2, subst3
                                    if len(subjects2) == 0:
                                        break
                                    tmp43.append(subjects2.popleft())
                                subjects2.extendleft(reversed(tmp43))
                    subjects2.appendleft(tmp40)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp46 = subjects2.popleft()
                associative1 = tmp46
                associative_type1 = type(tmp46)
                subjects47 = deque(tmp46._args)
                matcher = CommutativeMatcher45863.get()
                tmp48 = subjects47
                subjects47 = []
                for s in tmp48:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp48, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 45870
                        if len(subjects2) >= 1:
                            tmp49 = []
                            tmp49.append(subjects2.popleft())
                            while True:
                                if len(tmp49) > 1:
                                    tmp50 = create_operation_expression(associative1, tmp49)
                                elif len(tmp49) == 1:
                                    tmp50 = tmp49[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i4.2.2', tmp50)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45871
                                    if len(subjects2) == 0:
                                        pass
                                        # State 45872
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (c*x**n)**p /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                            yield 0, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp49.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp49))
                subjects2.appendleft(tmp46)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Add):
                tmp52 = subjects2.popleft()
                associative1 = tmp52
                associative_type1 = type(tmp52)
                subjects53 = deque(tmp52._args)
                matcher = CommutativeMatcher47111.get()
                tmp54 = subjects53
                subjects53 = []
                for s in tmp54:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp54, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 47117
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i4.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47118
                            if len(subjects2) == 0:
                                pass
                                # State 47119
                                if len(subjects) == 0:
                                    pass
                                    # 1: (a + x*b)**n1 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                    yield 1, subst2
                        if len(subjects2) >= 1:
                            tmp56 = []
                            tmp56.append(subjects2.popleft())
                            while True:
                                if len(tmp56) > 1:
                                    tmp57 = create_operation_expression(associative1, tmp56)
                                elif len(tmp56) == 1:
                                    tmp57 = tmp56[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i4.2.2', tmp57)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47118
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47119
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (a + x*b)**n1 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                            yield 1, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp56.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp56))
                    if pattern_index == 1:
                        pass
                        # State 47133
                        if len(subjects2) >= 1:
                            tmp59 = []
                            tmp59.append(subjects2.popleft())
                            while True:
                                if len(tmp59) > 1:
                                    tmp60 = create_operation_expression(associative1, tmp59)
                                elif len(tmp59) == 1:
                                    tmp60 = tmp59[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i4.2.2_1', tmp60)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47134
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47135
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (c + x*d)**n2 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                            yield 2, subst2
                                if len(subjects2) == 0:
                                    break
                                tmp59.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp59))
                subjects2.appendleft(tmp52)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 47085
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i4.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 47086
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i4.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 47087
                    if len(subjects) >= 1:
                        tmp65 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i4.2.2.1.0', tmp65)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47088
                            if len(subjects) == 0:
                                pass
                                # 1: (a + x*b)**n1 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                yield 1, subst4
                        subjects.appendleft(tmp65)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp67 = subjects.popleft()
                    associative1 = tmp67
                    associative_type1 = type(tmp67)
                    subjects68 = deque(tmp67._args)
                    matcher = CommutativeMatcher47090.get()
                    tmp69 = subjects68
                    subjects68 = []
                    for s in tmp69:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp69, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 47091
                            if len(subjects) == 0:
                                pass
                                # 1: (a + x*b)**n1 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                yield 1, subst3
                    subjects.appendleft(tmp67)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp70 = subjects.popleft()
                associative1 = tmp70
                associative_type1 = type(tmp70)
                subjects71 = deque(tmp70._args)
                matcher = CommutativeMatcher47093.get()
                tmp72 = subjects71
                subjects71 = []
                for s in tmp72:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp72, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 47099
                        if len(subjects) == 0:
                            pass
                            # 1: (a + x*b)**n1 /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                            yield 1, subst2
                subjects.appendleft(tmp70)
        return
        yield


from .generated_part001555 import *
from .generated_part001557 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part001561 import *
from collections import deque
from .generated_part001556 import *
from .generated_part001558 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset
from .generated_part001560 import *