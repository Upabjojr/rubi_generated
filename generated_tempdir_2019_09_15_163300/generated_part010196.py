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


class CommutativeMatcher49198(CommutativeMatcher):
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
        if CommutativeMatcher49198._instance is None:
            CommutativeMatcher49198._instance = CommutativeMatcher49198()
        return CommutativeMatcher49198._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 49197
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i3.2.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 49199
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp2 = subjects.popleft()
                subjects3 = deque(tmp2._args)
                # State 49200
                if len(subjects3) >= 1:
                    tmp4 = subjects3.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i3.2.1.1', tmp4)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 49201
                        if len(subjects3) >= 1:
                            tmp6 = subjects3.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i3.2.1.2', tmp6)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 49202
                                if len(subjects3) == 0:
                                    pass
                                    # State 49203
                                    if len(subjects) == 0:
                                        pass
                                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                                        yield 0, subst3
                            subjects3.appendleft(tmp6)
                    subjects3.appendleft(tmp4)
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i3.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 51166
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i3.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 51167
                        if len(subjects3) >= 1:
                            tmp10 = subjects3.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i3.2.1.2.1.0', tmp10)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 51168
                                if len(subjects3) >= 1:
                                    tmp12 = subjects3.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.2.1.2', tmp12)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 51169
                                        if len(subjects3) == 0:
                                            pass
                                            # State 51170
                                            if len(subjects) == 0:
                                                pass
                                                # 1: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f89) and (cons_f465)
                                                yield 1, subst5
                                    subjects3.appendleft(tmp12)
                                subst5 = Substitution(subst4)
                                try:
                                    subst5.try_add_variable('i3.2.1.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 51365
                                    if len(subjects3) == 0:
                                        pass
                                        # State 51366
                                        if len(subjects) == 0:
                                            pass
                                            # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                            yield 2, subst5
                                if len(subjects3) >= 1:
                                    tmp15 = subjects3.popleft()
                                    subst5 = Substitution(subst4)
                                    try:
                                        subst5.try_add_variable('i3.2.1.2', tmp15)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 51365
                                        if len(subjects3) == 0:
                                            pass
                                            # State 51366
                                            if len(subjects) == 0:
                                                pass
                                                # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                                yield 2, subst5
                                    subjects3.appendleft(tmp15)
                            subjects3.appendleft(tmp10)
                    if len(subjects3) >= 1 and isinstance(subjects3[0], Mul):
                        tmp17 = subjects3.popleft()
                        associative1 = tmp17
                        associative_type1 = type(tmp17)
                        subjects18 = deque(tmp17._args)
                        matcher = CommutativeMatcher51172.get()
                        tmp19 = subjects18
                        subjects18 = []
                        for s in tmp19:
                            matcher.add_subject(s)
                        for pattern_index, subst3 in matcher.match(tmp19, subst2):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 51173
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
                                            # State 51174
                                            if len(subjects3) == 0:
                                                pass
                                                # State 51175
                                                if len(subjects) == 0:
                                                    pass
                                                    # 1: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f89) and (cons_f465)
                                                    yield 1, subst4
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
                                    # State 51367
                                    if len(subjects3) == 0:
                                        pass
                                        # State 51368
                                        if len(subjects) == 0:
                                            pass
                                            # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                            yield 2, subst4
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
                                            # State 51367
                                            if len(subjects3) == 0:
                                                pass
                                                # State 51368
                                                if len(subjects) == 0:
                                                    pass
                                                    # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                                    yield 2, subst4
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
                    matcher = CommutativeMatcher51177.get()
                    tmp29 = subjects28
                    subjects28 = []
                    for s in tmp29:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp29, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 51183
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
                                        # State 51184
                                        if len(subjects3) == 0:
                                            pass
                                            # State 51185
                                            if len(subjects) == 0:
                                                pass
                                                # 1: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f89) and (cons_f465)
                                                yield 1, subst3
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
                                # State 51369
                                if len(subjects3) == 0:
                                    pass
                                    # State 51370
                                    if len(subjects) == 0:
                                        pass
                                        # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                        yield 2, subst3
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
                                        # State 51369
                                        if len(subjects3) == 0:
                                            pass
                                            # State 51370
                                            if len(subjects) == 0:
                                                pass
                                                # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                                yield 2, subst3
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
                # State 51350
                subst3 = Substitution(subst2)
                try:
                    subst3.try_add_variable('i3.2.1.2.0', S(0))
                except ValueError:
                    pass
                else:
                    pass
                    # State 51351
                    subst4 = Substitution(subst3)
                    try:
                        subst4.try_add_variable('i3.2.1.2.1.0_1', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 51352
                        if len(subjects) >= 1:
                            tmp40 = subjects.popleft()
                            subst5 = Substitution(subst4)
                            try:
                                subst5.try_add_variable('i3.2.1.2.1.0', tmp40)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 51353
                                if len(subjects) == 0:
                                    pass
                                    # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                    yield 2, subst5
                            subjects.appendleft(tmp40)
                    if len(subjects) >= 1 and isinstance(subjects[0], Mul):
                        tmp42 = subjects.popleft()
                        associative1 = tmp42
                        associative_type1 = type(tmp42)
                        subjects43 = deque(tmp42._args)
                        matcher = CommutativeMatcher51355.get()
                        tmp44 = subjects43
                        subjects43 = []
                        for s in tmp44:
                            matcher.add_subject(s)
                        for pattern_index, subst4 in matcher.match(tmp44, subst3):
                            pass
                            if pattern_index == 0:
                                pass
                                # State 51356
                                if len(subjects) == 0:
                                    pass
                                    # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                    yield 2, subst4
                        subjects.appendleft(tmp42)
                if len(subjects) >= 1 and isinstance(subjects[0], Add):
                    tmp45 = subjects.popleft()
                    associative1 = tmp45
                    associative_type1 = type(tmp45)
                    subjects46 = deque(tmp45._args)
                    matcher = CommutativeMatcher51358.get()
                    tmp47 = subjects46
                    subjects46 = []
                    for s in tmp47:
                        matcher.add_subject(s)
                    for pattern_index, subst3 in matcher.match(tmp47, subst2):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 51364
                            if len(subjects) == 0:
                                pass
                                # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                                yield 2, subst3
                    subjects.appendleft(tmp45)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp48 = subjects.popleft()
            associative1 = tmp48
            associative_type1 = type(tmp48)
            subjects49 = deque(tmp48._args)
            matcher = CommutativeMatcher49205.get()
            tmp50 = subjects49
            subjects49 = []
            for s in tmp50:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp50, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 49210
                    if len(subjects) == 0:
                        pass
                        # 0: b*x**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f4) and (cons_f5) and (cons_f808)
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 51206
                    if len(subjects) == 0:
                        pass
                        # 1: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f5) and (cons_f89) and (cons_f465)
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 51392
                    if len(subjects) == 0:
                        pass
                        # 2: b*(d + x*e)**n /; (cons_f2) and (cons_f3) and (cons_f8) and (cons_f29) and (cons_f50) and (cons_f4) and (cons_f5) and (cons_f1233)
                        yield 2, subst1
            subjects.appendleft(tmp48)
        return
        yield


from .generated_part010201 import *
from .generated_part010200 import *
from .generated_part010197 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from collections import deque
from .generated_part010198 import *
from .generated_part010203 import *
from matchpy.utils import VariableWithCount
from multiset import Multiset