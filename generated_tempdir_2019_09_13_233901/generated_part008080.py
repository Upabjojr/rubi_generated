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

class CommutativeMatcher17029(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1, 7: 1}), [
      (VariableWithCount('i4.0', 1, 1, S(0)), Add)
])
}
    subjects = {}
    subjects_by_id = {}
    bipartite = BipartiteGraph()
    associative = Add
    max_optional_count = 1
    anonymous_patterns = set()

    def __init__(self):
        self.add_subject(None)

    @staticmethod
    def get():
        if CommutativeMatcher17029._instance is None:
            CommutativeMatcher17029._instance = CommutativeMatcher17029()
        return CommutativeMatcher17029._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 17028
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 17030
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i4.1.1.0', S(0))
            except ValueError:
                pass
            else:
                pass
                # State 17031
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i4.1.1.1.0_1', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 17032
                    if len(subjects) >= 1:
                        tmp4 = subjects.popleft()
                        subst4 = Substitution(subst3)
                        try:
                            subst4.try_add_variable('i4.1.1.1.0', tmp4)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 17033
                            if len(subjects) == 0:
                                pass
                                # 0: b*(c + x*d) /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1115)
                        subjects.appendleft(tmp4)
                if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                    tmp6 = subjects.popleft()
                    associative1 = tmp6
                    associative_type1 = type(tmp6)
                    subjects7 = deque(tmp6._args)
                    matcher = CommutativeMatcher17035.get()
                    tmp8 = subjects7
                    subjects7 = []
                    for s in tmp8:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp8, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 17036
                            if len(subjects) == 0:
                                pass
                                # 0: b*(c + x*d) /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1115)
                    subjects.appendleft(tmp6)
            if len(subjects) >= 1 and isinstance(subjects[0], Add):
                tmp9 = subjects.popleft()
                associative1 = tmp9
                associative_type1 = type(tmp9)
                subjects10 = deque(tmp9._args)
                matcher = CommutativeMatcher17038.get()
                tmp11 = subjects10
                subjects10 = []
                for s in tmp11:
                    matcher.add_subject(s)
                for pattern_index, subst2 in matcher.match(tmp11, subst1):
                    pass
                    if pattern_index == 0:
                        pass
                        # State 17044
                        if len(subjects) == 0:
                            pass
                            # 0: b*(c + x*d) /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1115)
                subjects.appendleft(tmp9)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp12 = subjects.popleft()
                subjects13 = deque(tmp12._args)
                # State 17121
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 17122
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i4.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17123
                        if len(subjects13) >= 1:
                            tmp16 = subjects13.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i4.1.2.1.0', tmp16)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 17124
                                if len(subjects13) >= 1 and subjects13[0] == 2:
                                    tmp18 = subjects13.popleft()
                                    # State 17125
                                    if len(subjects13) == 0:
                                        pass
                                        # State 17126
                                        if len(subjects) == 0:
                                            pass
                                            # 1: b*(c + x*d)**2 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f481)
                                            # 2: b*(c + x*d)**2 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f482)
                                    subjects13.appendleft(tmp18)
                                if len(subjects13) >= 1:
                                    tmp19 = subjects13.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i4.1.2', tmp19)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 17197
                                        if len(subjects13) == 0:
                                            pass
                                            # State 17198
                                            if len(subjects) == 0:
                                                pass
                                                # 3: b*(c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f198)
                                                # 4: b*(c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f25)
                                                # 5: b*(c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1117)
                                    subjects13.appendleft(tmp19)
                            subjects13.appendleft(tmp16)
                    if len(subjects13) >= 1 and isinstance(subjects13[0], Mul):
                        tmp21 = subjects13.popleft()
                        associative1 = tmp21
                        associative_type1 = type(tmp21)
                        subjects22 = deque(tmp21._args)
                        matcher = CommutativeMatcher17128.get()
                        tmp23 = subjects22
                        subjects22 = []
                        for s in tmp23:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp23, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 17129
                                if len(subjects13) >= 1 and subjects13[0] == 2:
                                    tmp24 = subjects13.popleft()
                                    # State 17130
                                    if len(subjects13) == 0:
                                        pass
                                        # State 17131
                                        if len(subjects) == 0:
                                            pass
                                            # 1: b*(c + x*d)**2 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f481)
                                            # 2: b*(c + x*d)**2 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f482)
                                    subjects13.appendleft(tmp24)
                                if len(subjects13) >= 1:
                                    tmp25 = []
                                    tmp25.append(subjects13.popleft())
                                    while True:
                                        if len(tmp25) > 1:
                                            tmp26 = create_operation_expression(associative1, tmp25)
                                        elif len(tmp25) == 1:
                                            tmp26 = tmp25[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i4.1.2', tmp26)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 17199
                                            if len(subjects13) == 0:
                                                pass
                                                # State 17200
                                                if len(subjects) == 0:
                                                    pass
                                                    # 3: b*(c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f198)
                                                    # 4: b*(c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f25)
                                                    # 5: b*(c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1117)
                                        if len(subjects13) == 0:
                                            break
                                        tmp25.append(subjects13.popleft())
                                    subjects13.extendleft(reversed(tmp25))
                        subjects13.appendleft(tmp21)
                if len(subjects13) >= 1:
                    tmp28 = subjects13.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i4.1.1', tmp28)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 17674
                        if len(subjects13) >= 1 and subjects13[0] == 2:
                            tmp30 = subjects13.popleft()
                            # State 17675
                            if len(subjects13) == 0:
                                pass
                                # State 17676
                                if len(subjects) == 0:
                                    pass
                                    # 6: c*x**2 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f1132)
                            subjects13.appendleft(tmp30)
                    subjects13.appendleft(tmp28)
                if len(subjects13) >= 1 and isinstance(subjects13[0], Add):
                    tmp31 = subjects13.popleft()
                    associative1 = tmp31
                    associative_type1 = type(tmp31)
                    subjects32 = deque(tmp31._args)
                    matcher = CommutativeMatcher17133.get()
                    tmp33 = subjects32
                    subjects32 = []
                    for s in tmp33:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp33, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 17139
                            if len(subjects13) >= 1 and subjects13[0] == 2:
                                tmp34 = subjects13.popleft()
                                # State 17140
                                if len(subjects13) == 0:
                                    pass
                                    # State 17141
                                    if len(subjects) == 0:
                                        pass
                                        # 1: b*(c + x*d)**2 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f481)
                                        # 2: b*(c + x*d)**2 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f482)
                                subjects13.appendleft(tmp34)
                            if len(subjects13) >= 1:
                                tmp35 = []
                                tmp35.append(subjects13.popleft())
                                while True:
                                    if len(tmp35) > 1:
                                        tmp36 = create_operation_expression(associative1, tmp35)
                                    elif len(tmp35) == 1:
                                        tmp36 = tmp35[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i4.1.2', tmp36)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 17201
                                        if len(subjects13) == 0:
                                            pass
                                            # State 17202
                                            if len(subjects) == 0:
                                                pass
                                                # 3: b*(c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f198)
                                                # 4: b*(c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f25)
                                                # 5: b*(c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1117)
                                    if len(subjects13) == 0:
                                        break
                                    tmp35.append(subjects13.popleft())
                                subjects13.extendleft(reversed(tmp35))
                    subjects13.appendleft(tmp31)
                subjects.appendleft(tmp12)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 17681
            if len(subjects) >= 1:
                tmp39 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i4.1.1', tmp39)
                except ValueError:
                    pass
                else:
                    pass
                    # State 17682
                    if len(subjects) == 0:
                        pass
                        # 7: b*x /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f1132)
                subjects.appendleft(tmp39)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp41 = subjects.popleft()
            associative1 = tmp41
            associative_type1 = type(tmp41)
            subjects42 = deque(tmp41._args)
            matcher = CommutativeMatcher17046.get()
            tmp43 = subjects42
            subjects42 = []
            for s in tmp43:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp43, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 17061
                    if len(subjects) == 0:
                        pass
                        # 0: b*(c + x*d) /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1115)
                if pattern_index == 1:
                    pass
                    # State 17163
                    if len(subjects) == 0:
                        pass
                        # 1: b*(c + x*d)**2 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f481)
                        # 2: b*(c + x*d)**2 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f482)
                if pattern_index == 2:
                    pass
                    # State 17209
                    if len(subjects) == 0:
                        pass
                        # 3: b*(c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f198)
                        # 4: b*(c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f1116) and (cons_f25)
                        # 5: b*(c + x*d)**n /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f4) and (cons_f1117)
                if pattern_index == 3:
                    pass
                    # State 17680
                    if len(subjects) == 0:
                        pass
                        # 6: c*x**2 /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f1132)
                if pattern_index == 4:
                    pass
                    # State 17683
                    if len(subjects) == 0:
                        pass
                        # 7: b*x /; (cons_f1101) and (cons_f2) and (cons_f3) and (cons_f8) and (cons_f1132)
            subjects.appendleft(tmp41)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
