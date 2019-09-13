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

class CommutativeMatcher48049(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1, 1: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(1)), Mul)
]),
    1: (1, Multiset({2: 1, 3: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(1)), Mul)
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
        if CommutativeMatcher48049._instance is None:
            CommutativeMatcher48049._instance = CommutativeMatcher48049()
        return CommutativeMatcher48049._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 48048
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.2', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 48050
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 48051
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i2.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 48052
                    if len(subjects) >= 1:
                        tmp4 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.0', tmp4)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48053
                            if len(subjects) == 0:
                                pass
                                # 0: (x*b + a)**n1
                        subjects.appendleft(tmp4)
                    if len(subjects) >= 1:
                        tmp6 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i2.2.1.1', tmp6)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48845
                            if len(subjects) == 0:
                                pass
                                # 2: (x*b + a)**n1
                        subjects.appendleft(tmp6)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp8 = subjects.popleft()
                    associative1 = tmp8
                    associative_type1 = type(tmp8)
                    subjects9 = deque(tmp8._args)
                    matcher = CommutativeMatcher48055.get()
                    tmp10 = subjects9
                    subjects9 = []
                    for s in tmp10:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp10, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 48056
                            if len(subjects) == 0:
                                pass
                                # 0: (x*b + a)**n1
                        if pattern_index == 1:
                            pass
                            # State 48846
                            if len(subjects) == 0:
                                pass
                                # 2: (x*b + a)**n1
                    subjects.appendleft(tmp8)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp11 = subjects.popleft()
                associative1 = tmp11
                associative_type1 = type(tmp11)
                subjects12 = deque(tmp11._args)
                matcher = CommutativeMatcher48058.get()
                tmp13 = subjects12
                subjects12 = []
                for s in tmp13:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp13, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 48064
                        if len(subjects) == 0:
                            pass
                            # 0: (x*b + a)**n1
                    if pattern_index == 1:
                        pass
                        # State 48849
                        if len(subjects) == 0:
                            pass
                            # 2: (x*b + a)**n1
                subjects.appendleft(tmp11)
        if len(subjects) >= 1 and isinstance(subjects[0], Pow):
            tmp14 = subjects.popleft()
            subjects15 = deque(tmp14._args)
            # State 48065
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 48066
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 48067
                    if len(subjects15) >= 1:
                        tmp18 = subjects15.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp18)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48068
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 48069
                                if len(subjects15) == 0:
                                    pass
                                    # State 48070
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (x*b + a)**n1
                            if len(subjects15) >= 1:
                                tmp21 = subjects15.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.2', tmp21)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48069
                                    if len(subjects15) == 0:
                                        pass
                                        # State 48070
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (x*b + a)**n1
                                subjects15.appendleft(tmp21)
                        subjects15.appendleft(tmp18)
                    if len(subjects15) >= 1:
                        tmp23 = subjects15.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp23)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48850
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 48851
                                if len(subjects15) == 0:
                                    pass
                                    # State 48852
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (x*b + a)**n1
                            if len(subjects15) >= 1:
                                tmp26 = subjects15.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.2', tmp26)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48851
                                    if len(subjects15) == 0:
                                        pass
                                        # State 48852
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (x*b + a)**n1
                                subjects15.appendleft(tmp26)
                        subjects15.appendleft(tmp23)
                if len(subjects15) >= 1 and isinstance(subjects15[0], Mul):
                    tmp28 = subjects15.popleft()
                    associative1 = tmp28
                    associative_type1 = type(tmp28)
                    subjects29 = deque(tmp28._args)
                    matcher = CommutativeMatcher48072.get()
                    tmp30 = subjects29
                    subjects29 = []
                    for s in tmp30:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp30, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 48073
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 48074
                                if len(subjects15) == 0:
                                    pass
                                    # State 48075
                                    if len(subjects) == 0:
                                        pass
                                        # 0: (x*b + a)**n1
                            if len(subjects15) >= 1:
                                tmp32 = []
                                tmp32.append(subjects15.popleft())
                                while True:
                                    if len(tmp32) > 1:
                                        tmp33 = create_operation_expression(associative1, tmp32)
                                    elif len(tmp32) == 1:
                                        tmp33 = tmp32[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.2.2', tmp33)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 48074
                                        if len(subjects15) == 0:
                                            pass
                                            # State 48075
                                            if len(subjects) == 0:
                                                pass
                                                # 0: (x*b + a)**n1
                                    if len(subjects15) == 0:
                                        break
                                    tmp32.append(subjects15.popleft())
                                subjects15.extendleft(reversed(tmp32))
                        if pattern_index == 1:
                            pass
                            # State 48853
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.2.2.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 48854
                                if len(subjects15) == 0:
                                    pass
                                    # State 48855
                                    if len(subjects) == 0:
                                        pass
                                        # 2: (x*b + a)**n1
                            if len(subjects15) >= 1:
                                tmp36 = []
                                tmp36.append(subjects15.popleft())
                                while True:
                                    if len(tmp36) > 1:
                                        tmp37 = create_operation_expression(associative1, tmp36)
                                    elif len(tmp36) == 1:
                                        tmp37 = tmp36[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.2.2', tmp37)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 48854
                                        if len(subjects15) == 0:
                                            pass
                                            # State 48855
                                            if len(subjects) == 0:
                                                pass
                                                # 2: (x*b + a)**n1
                                    if len(subjects15) == 0:
                                        break
                                    tmp36.append(subjects15.popleft())
                                subjects15.extendleft(reversed(tmp36))
                    subjects15.appendleft(tmp28)
            subst1 = Substitution(subst0)
            try:
                subst1.try_add_variable('i2.2.2.2.0_1', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 48086
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.2.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 48087
                    if len(subjects15) >= 1:
                        tmp41 = subjects15.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.0', tmp41)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48088
                            if len(subjects15) >= 1:
                                tmp43 = subjects15.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.2_1', tmp43)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48089
                                    if len(subjects15) == 0:
                                        pass
                                        # State 48090
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (x*d + c)**n2
                                subjects15.appendleft(tmp43)
                        subjects15.appendleft(tmp41)
                    if len(subjects15) >= 1:
                        tmp45 = subjects15.popleft()
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.2.1.1', tmp45)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48861
                            if len(subjects15) >= 1:
                                tmp47 = subjects15.popleft()
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.2.2.2_1', tmp47)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48862
                                    if len(subjects15) == 0:
                                        pass
                                        # State 48863
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (x*d + c)**n2
                                subjects15.appendleft(tmp47)
                        subjects15.appendleft(tmp45)
                if len(subjects15) >= 1 and isinstance(subjects15[0], Mul):
                    tmp49 = subjects15.popleft()
                    associative1 = tmp49
                    associative_type1 = type(tmp49)
                    subjects50 = deque(tmp49._args)
                    matcher = CommutativeMatcher48092.get()
                    tmp51 = subjects50
                    subjects50 = []
                    for s in tmp51:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp51, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 48093
                            if len(subjects15) >= 1:
                                tmp52 = []
                                tmp52.append(subjects15.popleft())
                                while True:
                                    if len(tmp52) > 1:
                                        tmp53 = create_operation_expression(associative1, tmp52)
                                    elif len(tmp52) == 1:
                                        tmp53 = tmp52[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.2.2_1', tmp53)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 48094
                                        if len(subjects15) == 0:
                                            pass
                                            # State 48095
                                            if len(subjects) == 0:
                                                pass
                                                # 1: (x*d + c)**n2
                                    if len(subjects15) == 0:
                                        break
                                    tmp52.append(subjects15.popleft())
                                subjects15.extendleft(reversed(tmp52))
                        if pattern_index == 1:
                            pass
                            # State 48864
                            if len(subjects15) >= 1:
                                tmp55 = []
                                tmp55.append(subjects15.popleft())
                                while True:
                                    if len(tmp55) > 1:
                                        tmp56 = create_operation_expression(associative1, tmp55)
                                    elif len(tmp55) == 1:
                                        tmp56 = tmp55[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.2.2.2_1', tmp56)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 48865
                                        if len(subjects15) == 0:
                                            pass
                                            # State 48866
                                            if len(subjects) == 0:
                                                pass
                                                # 3: (x*d + c)**n2
                                    if len(subjects15) == 0:
                                        break
                                    tmp55.append(subjects15.popleft())
                                subjects15.extendleft(reversed(tmp55))
                    subjects15.appendleft(tmp49)
            if len(subjects15) >= 1 and isinstance(subjects15[0], Add):
                tmp58 = subjects15.popleft()
                associative1 = tmp58
                associative_type1 = type(tmp58)
                subjects59 = deque(tmp58._args)
                matcher = CommutativeMatcher48077.get()
                tmp60 = subjects59
                subjects59 = []
                for s in tmp60:
                    matcher.add_subject(s)
                for pattern_index, subst1 in matcher.match(tmp60, subst0):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 48083
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48084
                            if len(subjects15) == 0:
                                pass
                                # State 48085
                                if len(subjects) == 0:
                                    pass
                                    # 0: (x*b + a)**n1
                        if len(subjects15) >= 1:
                            tmp62 = []
                            tmp62.append(subjects15.popleft())
                            while True:
                                if len(tmp62) > 1:
                                    tmp63 = create_operation_expression(associative1, tmp62)
                                elif len(tmp62) == 1:
                                    tmp63 = tmp62[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2.2', tmp63)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48084
                                    if len(subjects15) == 0:
                                        pass
                                        # State 48085
                                        if len(subjects) == 0:
                                            pass
                                            # 0: (x*b + a)**n1
                                if len(subjects15) == 0:
                                    break
                                tmp62.append(subjects15.popleft())
                            subjects15.extendleft(reversed(tmp62))
                    if pattern_index == 1:
                        pass
                        # State 48099
                        if len(subjects15) >= 1:
                            tmp65 = []
                            tmp65.append(subjects15.popleft())
                            while True:
                                if len(tmp65) > 1:
                                    tmp66 = create_operation_expression(associative1, tmp65)
                                elif len(tmp65) == 1:
                                    tmp66 = tmp65[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2.2_1', tmp66)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48100
                                    if len(subjects15) == 0:
                                        pass
                                        # State 48101
                                        if len(subjects) == 0:
                                            pass
                                            # 1: (x*d + c)**n2
                                if len(subjects15) == 0:
                                    break
                                tmp65.append(subjects15.popleft())
                            subjects15.extendleft(reversed(tmp65))
                    if pattern_index == 2:
                        pass
                        # State 48858
                        subst2 = Substitution(subst1)
                        try:
                            subst2.try_add_variable('i2.2.2.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 48859
                            if len(subjects15) == 0:
                                pass
                                # State 48860
                                if len(subjects) == 0:
                                    pass
                                    # 2: (x*b + a)**n1
                        if len(subjects15) >= 1:
                            tmp69 = []
                            tmp69.append(subjects15.popleft())
                            while True:
                                if len(tmp69) > 1:
                                    tmp70 = create_operation_expression(associative1, tmp69)
                                elif len(tmp69) == 1:
                                    tmp70 = tmp69[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2.2', tmp70)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48859
                                    if len(subjects15) == 0:
                                        pass
                                        # State 48860
                                        if len(subjects) == 0:
                                            pass
                                            # 2: (x*b + a)**n1
                                if len(subjects15) == 0:
                                    break
                                tmp69.append(subjects15.popleft())
                            subjects15.extendleft(reversed(tmp69))
                    if pattern_index == 3:
                        pass
                        # State 48869
                        if len(subjects15) >= 1:
                            tmp72 = []
                            tmp72.append(subjects15.popleft())
                            while True:
                                if len(tmp72) > 1:
                                    tmp73 = create_operation_expression(associative1, tmp72)
                                elif len(tmp72) == 1:
                                    tmp73 = tmp72[0]
                                else:
                                    assert False, "Unreachable"
                                subst2 = Substitution(subst1)
                                try:
                                    subst2.try_add_variable('i2.2.2.2_1', tmp73)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 48870
                                    if len(subjects15) == 0:
                                        pass
                                        # State 48871
                                        if len(subjects) == 0:
                                            pass
                                            # 3: (x*d + c)**n2
                                if len(subjects15) == 0:
                                    break
                                tmp72.append(subjects15.popleft())
                            subjects15.extendleft(reversed(tmp72))
                subjects15.appendleft(tmp58)
            subjects.appendleft(tmp14)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
