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

class CommutativeMatcher45880(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({1: 1}), [
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
        if CommutativeMatcher45880._instance is None:
            CommutativeMatcher45880._instance = CommutativeMatcher45880()
        return CommutativeMatcher45880._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 45879
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp1 = subjects.popleft()
            subjects2 = deque(tmp1._args)
            # State 45881
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i4.2.0', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 45882
                if len(subjects2) >= 1 and isinstance(subjects2[0], Pow):
                    tmp4 = subjects2.popleft()
                    subjects5 = deque(tmp4._args)
                    # State 45883
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i4.2.2.0', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 45884
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i4.2.2.2', S(1))
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 45885
                            if len(subjects5) >= 1:
                                tmp8 = subjects5.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i4.2.2.1', tmp8)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45886
                                    if len(subjects5) >= 1:
                                        tmp10 = subjects5.popleft()
                                        subst5 = Substitution(subst4)
                                        try:
                                            subst5.try_add_variable('i4.2.2', tmp10)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45887
                                            if len(subjects5) == 0:
                                                pass
                                                # State 45888
                                                if len(subjects2) >= 1:
                                                    tmp12 = subjects2.popleft()
                                                    subst6 = Substitution(subst5)
                                                    try:
                                                        subst6.try_add_variable('i4.2', tmp12)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 45889
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 45890
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (b*(c*x**n)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                                    subjects2.appendleft(tmp12)
                                        subjects5.appendleft(tmp10)
                                subjects5.appendleft(tmp8)
                        if len(subjects5) >= 1 and isinstance(subjects5[0], Pow):
                            tmp14 = subjects5.popleft()
                            subjects15 = deque(tmp14._args)
                            # State 45891
                            if len(subjects15) >= 1:
                                tmp16 = subjects15.popleft()
                                subst3 = Substitution(subst2)
                                try:
                                    subst3.try_add_variable('i4.2.2.1', tmp16)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45892
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i4.2.2.2', 1)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 45893
                                        if len(subjects15) == 0:
                                            pass
                                            # State 45894
                                            if len(subjects5) >= 1:
                                                tmp19 = subjects5.popleft()
                                                subst5 = Substitution(subst4)
                                                try:
                                                    subst5.try_add_variable('i4.2.2', tmp19)
                                                except ValueError:
                                                    pass
                                                else:
                                                    pass
                                                    # State 45895
                                                    if len(subjects5) == 0:
                                                        pass
                                                        # State 45896
                                                        if len(subjects2) >= 1:
                                                            tmp21 = subjects2.popleft()
                                                            subst6 = Substitution(subst5)
                                                            try:
                                                                subst6.try_add_variable('i4.2', tmp21)
                                                            except ValueError:
                                                                pass
                                                            else:
                                                                pass
                                                                # State 45897
                                                                if len(subjects2) == 0:
                                                                    pass
                                                                    # State 45898
                                                                    if len(subjects) == 0:
                                                                        pass
                                                                        # 0: (b*(c*x**n)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                                            subjects2.appendleft(tmp21)
                                                subjects5.appendleft(tmp19)
                                    if len(subjects15) >= 1:
                                        tmp23 = subjects15.popleft()
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i4.2.2.2', tmp23)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45893
                                            if len(subjects15) == 0:
                                                pass
                                                # State 45894
                                                if len(subjects5) >= 1:
                                                    tmp25 = subjects5.popleft()
                                                    subst5 = Substitution(subst4)
                                                    try:
                                                        subst5.try_add_variable('i4.2.2', tmp25)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 45895
                                                        if len(subjects5) == 0:
                                                            pass
                                                            # State 45896
                                                            if len(subjects2) >= 1:
                                                                tmp27 = subjects2.popleft()
                                                                subst6 = Substitution(subst5)
                                                                try:
                                                                    subst6.try_add_variable('i4.2', tmp27)
                                                                except ValueError:
                                                                    pass
                                                                else:
                                                                    pass
                                                                    # State 45897
                                                                    if len(subjects2) == 0:
                                                                        pass
                                                                        # State 45898
                                                                        if len(subjects) == 0:
                                                                            pass
                                                                            # 0: (b*(c*x**n)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                                                subjects2.appendleft(tmp27)
                                                    subjects5.appendleft(tmp25)
                                        subjects15.appendleft(tmp23)
                                subjects15.appendleft(tmp16)
                            subjects5.appendleft(tmp14)
                    if len(subjects5) >= 1 and isinstance(subjects5[0], Mul):
                        tmp29 = subjects5.popleft()
                        associative1 = tmp29
                        associative_type1 = type(tmp29)
                        subjects30 = deque(tmp29._args)
                        matcher = CommutativeMatcher45900.get()
                        tmp31 = subjects30
                        subjects30 = []
                        for s in tmp31:
                            matcher.add_subject(s)
                        for pattern_index, subst2 in matcher.match(tmp31, subst1):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 45907
                                if len(subjects5) >= 1:
                                    tmp32 = []
                                    tmp32.append(subjects5.popleft())
                                    while True:
                                        if len(tmp32) > 1:
                                            tmp33 = create_operation_expression(associative1, tmp32)
                                        elif len(tmp32) == 1:
                                            tmp33 = tmp32[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst3 = Substitution(subst2)
                                        try:
                                            subst3.try_add_variable('i4.2.2', tmp33)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 45908
                                            if len(subjects5) == 0:
                                                pass
                                                # State 45909
                                                if len(subjects2) >= 1:
                                                    tmp35 = subjects2.popleft()
                                                    subst4 = Substitution(subst3)
                                                    try:
                                                        subst4.try_add_variable('i4.2', tmp35)
                                                    except ValueError:
                                                        pass
                                                    else:
                                                        pass
                                                        # State 45910
                                                        if len(subjects2) == 0:
                                                            pass
                                                            # State 45911
                                                            if len(subjects) == 0:
                                                                pass
                                                                # 0: (b*(c*x**n)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                                    subjects2.appendleft(tmp35)
                                        if len(subjects5) == 0:
                                            break
                                        tmp32.append(subjects5.popleft())
                                    subjects5.extendleft(reversed(tmp32))
                        subjects5.appendleft(tmp29)
                    subjects2.appendleft(tmp4)
            if len(subjects2) >= 1 and isinstance(subjects2[0], Mul):
                tmp37 = subjects2.popleft()
                associative1 = tmp37
                associative_type1 = type(tmp37)
                subjects38 = deque(tmp37._args)
                matcher = CommutativeMatcher45913.get()
                tmp39 = subjects38
                subjects38 = []
                for s in tmp39:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp39, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 45937
                        if len(subjects2) >= 1:
                            tmp40 = []
                            tmp40.append(subjects2.popleft())
                            while True:
                                if len(tmp40) > 1:
                                    tmp41 = create_operation_expression(associative1, tmp40)
                                elif len(tmp40) == 1:
                                    tmp41 = tmp40[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i4.2', tmp41)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 45938
                                    if len(subjects2) == 0:
                                        pass
                                        # State 45939
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (b*(c*x**n)**p)**q /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f52) and (cons_f54) and (cons_f1203)
                                if len(subjects2) == 0:
                                    break
                                tmp40.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp40))
                    if pattern_index == 1:
                        pass
                        # State 47249
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i4.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 47250
                            if len(subjects2) == 0:
                                pass
                                # State 47251
                                if len(subjects) == 0:
                                    pass
                                    # 1: (e1*(c + x*d)**n2*(a + x*b)**n1)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
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
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i4.2', tmp45)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 47250
                                    if len(subjects2) == 0:
                                        pass
                                        # State 47251
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (e1*(c + x*d)**n2*(a + x*b)**n1)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                                if len(subjects2) == 0:
                                    break
                                tmp44.append(subjects2.popleft())
                            subjects2.extendleft(reversed(tmp44))
                subjects2.appendleft(tmp37)
            subjects.appendleft(tmp1)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 47142
            if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                tmp48 = subjects.popleft()
                associative1 = tmp48
                associative_type1 = type(tmp48)
                subjects49 = deque(tmp48._args)
                matcher = CommutativeMatcher47144.get()
                tmp50 = subjects49
                subjects49 = []
                for s in tmp50:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp50, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 47197
                        if len(subjects) == 0:
                            pass
                            # 1: (e1*(c + x*d)**n2*(a + x*b)**n1)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f654) and (cons_f1206) and (cons_f1205) and (cons_f73)
                subjects.appendleft(tmp48)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
