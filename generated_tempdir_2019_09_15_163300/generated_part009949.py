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


class CommutativeMatcher20488(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher20488._instance is None:
            CommutativeMatcher20488._instance = CommutativeMatcher20488()
        return CommutativeMatcher20488._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 20487
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.0', S(0))
        except ValueError:
            pass
        else:
            pass
            # State 20489
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i4.1.1.0_1', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 20490
                if len(subjects) >= 1:
                    tmp3 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i4.1.1.0', tmp3)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 20491
                        if len(subjects) == 0:
                            pass
                            # 0: e + x*f /; (cons_f29) and (cons_f50) and (cons_f127) and (cons_f1159)
                            yield 0, subst3
                    subjects.appendleft(tmp3)
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp5 = subjects.popleft()
                associative1 = tmp5
                associative_type1 = type(tmp5)
                subjects6 = deque(tmp5._args)
                matcher = CommutativeMatcher20493.get()
                tmp7 = subjects6
                subjects6 = []
                for s in tmp7:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp7, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 20494
                        if len(subjects) == 0:
                            pass
                            # 0: e + x*f /; (cons_f29) and (cons_f50) and (cons_f127) and (cons_f1159)
                            yield 0, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 47376
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp9 = subjects.popleft()
                associative1 = tmp9
                associative_type1 = type(tmp9)
                subjects10 = deque(tmp9._args)
                matcher = CommutativeMatcher47378.get()
                tmp11 = subjects10
                subjects10 = []
                for s in tmp11:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp11, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 47431
                        if len(subjects) == 0:
                            pass
                            # 2: (e1*(c + x*d)**n2*(a + x*b)**n1)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                            yield 2, subst2
                subjects.appendleft(tmp9)
        if len(subjects) >= 1 and isinstance(subjects[0], Add):
            tmp12 = subjects.popleft()
            associative1 = tmp12
            associative_type1 = type(tmp12)
            subjects13 = deque(tmp12._args)
            matcher = CommutativeMatcher20496.get()
            tmp14 = subjects13
            subjects13 = []
            for s in tmp14:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp14, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 20502
                    if len(subjects) == 0:
                        pass
                        # 0: e + x*f /; (cons_f29) and (cons_f50) and (cons_f127) and (cons_f1159)
                        yield 0, subst1
            subjects.appendleft(tmp12)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp15 = subjects.popleft()
            subjects16 = deque(tmp15._args)
            # State 46023
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 46024
                if len(subjects16) >= 1 and isinstance(subjects16[0], Pow):
                    tmp18 = subjects16.popleft()
                    subjects19 = deque(tmp18._args)
                    # State 46025
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i4.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 46026
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 46027
                            if len(subjects19) >= 1:
                                tmp22 = subjects19.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i4.2.2.1', tmp22)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46028
                                    if len(subjects19) >= 1:
                                        tmp24 = subjects19.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i4.2.2', tmp24)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 46029
                                            if len(subjects19) == 0:
                                                pass
                                                # State 46030
                                                if len(subjects16) >= 1:
                                                    tmp26 = subjects16.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i4.2', tmp26)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 46031
                                                        if len(subjects16) == 0:
                                                            pass
                                                            # State 46032
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (b*(c*x**n)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                                                yield 1, subst6
                                                    subjects16.appendleft(tmp26)
                                        subjects19.appendleft(tmp24)
                                subjects19.appendleft(tmp22)
                        if len(subjects19) >= 1 and isinstance(subjects19[0], Pow):
                            tmp28 = subjects19.popleft()
                            subjects29 = deque(tmp28._args)
                            # State 46033
                            if len(subjects29) >= 1:
                                tmp30 = subjects29.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i4.2.2.1', tmp30)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46034
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i4.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 46035
                                        if len(subjects29) == 0:
                                            pass
                                            # State 46036
                                            if len(subjects19) >= 1:
                                                tmp33 = subjects19.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i4.2.2', tmp33)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 46037
                                                    if len(subjects19) == 0:
                                                        pass
                                                        # State 46038
                                                        if len(subjects16) >= 1:
                                                            tmp35 = subjects16.popleft()
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i4.2', tmp35)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 46039
                                                                if len(subjects16) == 0:
                                                                    pass
                                                                    # State 46040
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 1: (b*(c*x**n)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                                                        yield 1, subst6
                                                            subjects16.appendleft(tmp35)
                                                subjects19.appendleft(tmp33)
                                    if len(subjects29) >= 1:
                                        tmp37 = subjects29.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i4.2.2.2', tmp37)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 46035
                                            if len(subjects29) == 0:
                                                pass
                                                # State 46036
                                                if len(subjects19) >= 1:
                                                    tmp39 = subjects19.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i4.2.2', tmp39)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 46037
                                                        if len(subjects19) == 0:
                                                            pass
                                                            # State 46038
                                                            if len(subjects16) >= 1:
                                                                tmp41 = subjects16.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i4.2', tmp41)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 46039
                                                                    if len(subjects16) == 0:
                                                                        pass
                                                                        # State 46040
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 1: (b*(c*x**n)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                                                            yield 1, subst6
                                                                subjects16.appendleft(tmp41)
                                                    subjects19.appendleft(tmp39)
                                        subjects29.appendleft(tmp37)
                                subjects29.appendleft(tmp30)
                            subjects19.appendleft(tmp28)
                    if len(subjects19) >= 1 and isinstance(subjects19[0], Mul):
                        tmp43 = subjects19.popleft()
                        associative1 = tmp43
                        associative_type1 = type(tmp43)
                        subjects44 = deque(tmp43._args)
                        matcher = CommutativeMatcher46042.get()
                        tmp45 = subjects44
                        subjects44 = []
                        for s in tmp45:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp45, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 46049
                                if len(subjects19) >= 1:
                                    tmp46 = []
                                    tmp46.append(subjects19.popleft())
                                    while True:
                                        if len(tmp46) > 1:
                                            tmp47 = create_operation_expression(associative1, tmp46)
                                        elif len(tmp46) == 1:
                                            tmp47 = tmp46[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i4.2.2', tmp47)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 46050
                                            if len(subjects19) == 0:
                                                pass
                                                # State 46051
                                                if len(subjects16) >= 1:
                                                    tmp49 = subjects16.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i4.2', tmp49)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 46052
                                                        if len(subjects16) == 0:
                                                            pass
                                                            # State 46053
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 1: (b*(c*x**n)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                                                yield 1, subst4
                                                    subjects16.appendleft(tmp49)
                                        if len(subjects19) == 0:
                                            break
                                        tmp46.append(subjects19.popleft())
                                    subjects19.extendleft(reversed(tmp46))
                        subjects19.appendleft(tmp43)
                    subjects16.appendleft(tmp18)
            if len(subjects16) >= 1 and isinstance(subjects16[0], Mul):
                tmp51 = subjects16.popleft()
                associative1 = tmp51
                associative_type1 = type(tmp51)
                subjects52 = deque(tmp51._args)
                matcher = CommutativeMatcher46055.get()
                tmp53 = subjects52
                subjects52 = []
                for s in tmp53:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp53, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 46079
                        if len(subjects16) >= 1:
                            tmp54 = []
                            tmp54.append(subjects16.popleft())
                            while True:
                                if len(tmp54) > 1:
                                    tmp55 = create_operation_expression(associative1, tmp54)
                                elif len(tmp54) == 1:
                                    tmp55 = tmp54[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i4.2', tmp55)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 46080
                                    if len(subjects16) == 0:
                                        pass
                                        # State 46081
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (b*(c*x**n)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                            yield 1, subst2
                                if len(subjects16) == 0:
                                    break
                                tmp54.append(subjects16.popleft())
                            subjects16.extendleft(reversed(tmp54))
                    if pattern_index == 1:
                        pass
                        # State 47483
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i4.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47484
                            if len(subjects16) == 0:
                                pass
                                # State 47485
                                if len(subjects) == 0:
                                    pass
                                    # 2: (e1*(c + x*d)**n2*(a + x*b)**n1)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                    yield 2, subst2
                        if len(subjects16) >= 1:
                            tmp58 = []
                            tmp58.append(subjects16.popleft())
                            while True:
                                if len(tmp58) > 1:
                                    tmp59 = create_operation_expression(associative1, tmp58)
                                elif len(tmp58) == 1:
                                    tmp59 = tmp58[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i4.2', tmp59)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47484
                                    if len(subjects16) == 0:
                                        pass
                                        # State 47485
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (e1*(c + x*d)**n2*(a + x*b)**n1)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                            yield 2, subst2
                                if len(subjects16) == 0:
                                    break
                                tmp58.append(subjects16.popleft())
                            subjects16.extendleft(reversed(tmp58))
                subjects16.appendleft(tmp51)
            subjects.appendleft(tmp15)
        return
        yield


from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part009959 import *
from .generated_part009961 import *
from collections import deque
from .generated_part009962 import *
from .generated_part009951 import *
from .generated_part009950 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset