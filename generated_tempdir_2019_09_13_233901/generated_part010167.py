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

class CommutativeMatcher49157(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i3.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i3.2.0', 1, 1, None), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i3.2.0', 1, 1, None), Add)
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
        if CommutativeMatcher49157._instance is None:
            CommutativeMatcher49157._instance = CommutativeMatcher49157()
        return CommutativeMatcher49157._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 49156
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 49158
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 49159
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.2.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 49160
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.2.1.2', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49161
                                if len(subjects3) == 0:
                                    pass
                                    # State 49162
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 51121
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 51122
                        if len(subjects3) >= 1:
                            tmp10 = subjects3.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.2.1.2.1.0', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 51123
                                if len(subjects3) >= 1:
                                    tmp12 = subjects3.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.2.1.2', tmp12)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 51124
                                        if len(subjects3) == 0:
                                            pass
                                            # State 51125
                                            if len(subjects) == 0:
                                                pass
                                                # 1: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f89) and (cons_f465)
                                    subjects3.appendleft(tmp12)
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51318
                                    if len(subjects3) == 0:
                                        pass
                                        # State 51319
                                        if len(subjects) == 0:
                                            pass
                                            # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                if len(subjects3) >= 1:
                                    tmp15 = subjects3.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.2.1.2', tmp15)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 51318
                                        if len(subjects3) == 0:
                                            pass
                                            # State 51319
                                            if len(subjects) == 0:
                                                pass
                                                # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                    subjects3.appendleft(tmp15)
                            subjects3.appendleft(tmp10)
                    if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                        tmp17 = subjects3.popleft()
                        associative1 = tmp17
                        associative_type1 = type(tmp17)
                        subjects18 = deque(tmp17._args)
                        matcher = CommutativeMatcher51127.get()
                        tmp19 = subjects18
                        subjects18 = []
                        for s in tmp19:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp19, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 51128
                                if len(subjects3) >= 1:
                                    tmp20 = []
                                    tmp20.append(subjects3.popleft())
                                    while True:
                                        if len(tmp20) > 1:
                                            tmp21 = create_operation_expression(associative1, tmp20)
                                        elif len(tmp20) == 1:
                                            tmp21 = tmp20[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.2.1.2', tmp21)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 51129
                                            if len(subjects3) == 0:
                                                pass
                                                # State 51130
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f89) and (cons_f465)
                                        if len(subjects3) == 0:
                                            break
                                        tmp20.append(subjects3.popleft())
                                    subjects3.extendleft(reversed(tmp20))
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i3.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51320
                                    if len(subjects3) == 0:
                                        pass
                                        # State 51321
                                        if len(subjects) == 0:
                                            pass
                                            # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                if len(subjects3) >= 1:
                                    tmp24 = []
                                    tmp24.append(subjects3.popleft())
                                    while True:
                                        if len(tmp24) > 1:
                                            tmp25 = create_operation_expression(associative1, tmp24)
                                        elif len(tmp24) == 1:
                                            tmp25 = tmp24[0]
                                        else:
                                            assert False, "Unreachable"
                                        subst4 = Substitution(subst3)
                                        try:
                                            subst4.try_add_variable('i3.2.1.2', tmp25)
                                        except ValueError:
                                            pass
                                        else:
                                            pass
                                            # State 51320
                                            if len(subjects3) == 0:
                                                pass
                                                # State 51321
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                        if len(subjects3) == 0:
                                            break
                                        tmp24.append(subjects3.popleft())
                                    subjects3.extendleft(reversed(tmp24))
                        subjects3.appendleft(tmp17)
                if len(subjects3) >= 1 and isinstance(subjects3[0], Add):
                    tmp27 = subjects3.popleft()
                    associative1 = tmp27
                    associative_type1 = type(tmp27)
                    subjects28 = deque(tmp27._args)
                    matcher = CommutativeMatcher51132.get()
                    tmp29 = subjects28
                    subjects28 = []
                    for s in tmp29:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp29, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 51138
                            if len(subjects3) >= 1:
                                tmp30 = []
                                tmp30.append(subjects3.popleft())
                                while True:
                                    if len(tmp30) > 1:
                                        tmp31 = create_operation_expression(associative1, tmp30)
                                    elif len(tmp30) == 1:
                                        tmp31 = tmp30[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.2.1.2', tmp31)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 51139
                                        if len(subjects3) == 0:
                                            pass
                                            # State 51140
                                            if len(subjects) == 0:
                                                pass
                                                # 1: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f89) and (cons_f465)
                                    if len(subjects3) == 0:
                                        break
                                    tmp30.append(subjects3.popleft())
                                subjects3.extendleft(reversed(tmp30))
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.2.1.2', 1)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 51322
                                if len(subjects3) == 0:
                                    pass
                                    # State 51323
                                    if len(subjects) == 0:
                                        pass
                                        # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                            if len(subjects3) >= 1:
                                tmp34 = []
                                tmp34.append(subjects3.popleft())
                                while True:
                                    if len(tmp34) > 1:
                                        tmp35 = create_operation_expression(associative1, tmp34)
                                    elif len(tmp34) == 1:
                                        tmp35 = tmp34[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i3.2.1.2', tmp35)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 51322
                                        if len(subjects3) == 0:
                                            pass
                                            # State 51323
                                            if len(subjects) == 0:
                                                pass
                                                # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                    if len(subjects3) == 0:
                                        break
                                    tmp34.append(subjects3.popleft())
                                subjects3.extendleft(reversed(tmp34))
                    subjects3.appendleft(tmp27)
                subjects.appendleft(tmp2)
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i3.2.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 51303
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i3.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 51304
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i3.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 51305
                        if len(subjects) >= 1:
                            tmp40 = subjects.popleft()
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i3.2.1.2.1.0', tmp40)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 51306
                                if len(subjects) == 0:
                                    pass
                                    # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                            subjects.appendleft(tmp40)
                    if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                        tmp42 = subjects.popleft()
                        associative1 = tmp42
                        associative_type1 = type(tmp42)
                        subjects43 = deque(tmp42._args)
                        matcher = CommutativeMatcher51308.get()
                        tmp44 = subjects43
                        subjects43 = []
                        for s in tmp44:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp44, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 51309
                                if len(subjects) == 0:
                                    pass
                                    # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                        subjects.appendleft(tmp42)
                if len(subjects) >= 1 and isinstance(subjects[0], Add):
                    tmp45 = subjects.popleft()
                    associative1 = tmp45
                    associative_type1 = type(tmp45)
                    subjects46 = deque(tmp45._args)
                    matcher = CommutativeMatcher51311.get()
                    tmp47 = subjects46
                    subjects46 = []
                    for s in tmp47:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp47, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 51317
                            if len(subjects) == 0:
                                pass
                                # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                    subjects.appendleft(tmp45)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp48 = subjects.popleft()
            associative1 = tmp48
            associative_type1 = type(tmp48)
            subjects49 = deque(tmp48._args)
            matcher = CommutativeMatcher49164.get()
            tmp50 = subjects49
            subjects49 = []
            for s in tmp50:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp50, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 49169
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                if pattern_index == 1:
                    pass
                    # State 51161
                    if len(subjects) == 0:
                        pass
                        # 1: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f89) and (cons_f465)
                if pattern_index == 2:
                    pass
                    # State 51345
                    if len(subjects) == 0:
                        pass
                        # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
            subjects.appendleft(tmp48)
        return
        yield


from matchpy.utils import VariableWithCount
from matchpy.matching.many_to_one import CommutativeMatcher
from multiset import Multiset
from collections import deque
