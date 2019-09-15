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


class CommutativeMatcher57228(CommutativeMatcher):
    _instance = None
    patterns = {
    0: (0, Multiset({0: 1}), [
      (VariableWithCount('i2.2.2.0', 1, 1, S(0)), Add)
]),
    1: (1, Multiset({1: 1}), [
      (VariableWithCount('i2.2.1.2.0', 1, 1, S(0)), Add)
]),
    2: (2, Multiset({2: 1}), [
      (VariableWithCount('i2.2.1.3.0', 1, 1, S(0)), Add)
]),
    3: (3, Multiset({3: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    4: (4, Multiset({4: 1}), [
      (VariableWithCount('i2.2.1.2.2.0', 1, 1, S(0)), Add)
]),
    5: (5, Multiset({5: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    6: (6, Multiset({6: 1}), [
      (VariableWithCount('i2.2.1.4.0', 1, 1, S(0)), Add)
]),
    7: (7, Multiset({7: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    8: (8, Multiset({8: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    9: (9, Multiset({9: 1}), [
      (VariableWithCount('i2.3.0_1', 1, 1, S(0)), Add)
]),
    10: (10, Multiset({10: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
]),
    11: (11, Multiset({11: 1}), [
      (VariableWithCount('i2.3.0', 1, 1, S(0)), Add)
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
        if CommutativeMatcher57228._instance is None:
            CommutativeMatcher57228._instance = CommutativeMatcher57228()
        return CommutativeMatcher57228._instance

    @staticmethod
    def get_match_iter(subject):
        subjects = deque([subject]) if subject is not None else deque()
        subst0 = Substitution()
        # State 57227
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 57229
            if len(subjects) >= 1:
                tmp2 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp2)
                except ValueError:
                    pass
                else:
                    pass
                    # State 57230
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst2
                subjects.appendleft(tmp2)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 58502
            if len(subjects) >= 1:
                tmp5 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.1.0', tmp5)
                except ValueError:
                    pass
                else:
                    pass
                    # State 58503
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst2
                subjects.appendleft(tmp5)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 64315
            if len(subjects) >= 1:
                tmp8 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.3.1.0', tmp8)
                except ValueError:
                    pass
                else:
                    pass
                    # State 64316
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst2
                subjects.appendleft(tmp8)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 65655
            if len(subjects) >= 1:
                tmp11 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.0', tmp11)
                except ValueError:
                    pass
                else:
                    pass
                    # State 65656
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst2
                subjects.appendleft(tmp11)
            if len(subjects) >= 1:
                tmp13 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.1.0', tmp13)
                except ValueError:
                    pass
                else:
                    pass
                    # State 104047
                    if len(subjects) == 0:
                        pass
                        # 9: e*x
                        yield 9, subst2
                subjects.appendleft(tmp13)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.2.2.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 68404
            if len(subjects) >= 1:
                tmp16 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.2.2.1.0', tmp16)
                except ValueError:
                    pass
                else:
                    pass
                    # State 68405
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                        yield 4, subst2
                subjects.appendleft(tmp16)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.3.1.0', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 75438
            subst2 = Substitution(subst1)
            try:
                subst2.try_add_variable('i2.3.1.2', S(1))
            except ValueError:
                pass
            else:
                pass
                # State 75439
                if len(subjects) >= 1:
                    tmp20 = subjects.popleft()
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.1', tmp20)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75440
                        if len(subjects) == 0:
                            pass
                            # 5: x**n*b
                            yield 5, subst3
                    subjects.appendleft(tmp20)
            if len(subjects) >= 1:
                tmp22 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.2.1.0', tmp22)
                except ValueError:
                    pass
                else:
                    pass
                    # State 100917
                    if len(subjects) == 0:
                        pass
                        # 7: x*b
                        yield 7, subst2
                subjects.appendleft(tmp22)
            if len(subjects) >= 1:
                tmp24 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.0', tmp24)
                except ValueError:
                    pass
                else:
                    pass
                    # State 103420
                    if len(subjects) == 0:
                        pass
                        # 8: x*f
                        yield 8, subst2
                subjects.appendleft(tmp24)
            if len(subjects) >= 1 and isinstance(subjects[0], Pow):
                tmp26 = subjects.popleft()
                subjects27 = deque(tmp26._args)
                # State 75441
                if len(subjects27) >= 1:
                    tmp28 = subjects27.popleft()
                    subst2 = Substitution(subst1)
                    try:
                        subst2.try_add_variable('i2.1', tmp28)
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 75442
                        subst3 = Substitution(subst2)
                        try:
                            subst3.try_add_variable('i2.3.1.2', 1)
                        except ValueError:
                            pass
                        else:
                            pass
                            # State 75443
                            if len(subjects27) == 0:
                                pass
                                # State 75444
                                if len(subjects) == 0:
                                    pass
                                    # 5: x**n*b
                                    yield 5, subst3
                        if len(subjects27) >= 1:
                            tmp31 = subjects27.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.3.1.2', tmp31)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 75443
                                if len(subjects27) == 0:
                                    pass
                                    # State 75444
                                    if len(subjects) == 0:
                                        pass
                                        # 5: x**n*b
                                        yield 5, subst3
                            subjects27.appendleft(tmp31)
                    subjects27.appendleft(tmp28)
                if len(subjects27) >= 1 and isinstance(subjects27[0], Add):
                    tmp33 = subjects27.popleft()
                    associative1 = tmp33
                    associative_type1 = type(tmp33)
                    subjects34 = deque(tmp33._args)
                    matcher = CommutativeMatcher107313.get()
                    tmp35 = subjects34
                    subjects34 = []
                    for s in tmp35:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp35, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 107319
                            if len(subjects27) >= 1:
                                tmp36 = []
                                tmp36.append(subjects27.popleft())
                                while True:
                                    if len(tmp36) > 1:
                                        tmp37 = create_operation_expression(associative1, tmp36)
                                    elif len(tmp36) == 1:
                                        tmp37 = tmp36[0]
                                    else:
                                        assert False, "Unreachable"
                                    subst3 = Substitution(subst2)
                                    try:
                                        subst3.try_add_variable('i2.3.1.2', tmp37)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 107320
                                        if len(subjects27) == 0:
                                            pass
                                            # State 107321
                                            if len(subjects) == 0:
                                                pass
                                                # 11: b*(x*d + c)**n
                                                yield 11, subst3
                                    if len(subjects27) == 0:
                                        break
                                    tmp36.append(subjects27.popleft())
                                subjects27.extendleft(reversed(tmp36))
                    subjects27.appendleft(tmp33)
                subjects.appendleft(tmp26)
            if len(subjects) >= 1 and isinstance(subjects[0], log):
                tmp39 = subjects.popleft()
                subjects40 = deque(tmp39._args)
                # State 105189
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.3.1.2.0', S(1))
                except ValueError:
                    pass
                else:
                    pass
                    # State 105190
                    subst3 = Substitution(subst2)
                    try:
                        subst3.try_add_variable('i2.3.1.2.2', S(1))
                    except ValueError:
                        pass
                    else:
                        pass
                        # State 105191
                        if len(subjects40) >= 1:
                            tmp43 = subjects40.popleft()
                            subst4 = Substitution(subst3)
                            try:
                                subst4.try_add_variable('i2.1', tmp43)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105192
                                if len(subjects40) == 0:
                                    pass
                                    # State 105193
                                    if len(subjects) == 0:
                                        pass
                                        # 10: b*log(x**n*c)
                                        yield 10, subst4
                            subjects40.appendleft(tmp43)
                    if len(subjects40) >= 1 and isinstance(subjects40[0], Pow):
                        tmp45 = subjects40.popleft()
                        subjects46 = deque(tmp45._args)
                        # State 105194
                        if len(subjects46) >= 1:
                            tmp47 = subjects46.popleft()
                            subst3 = Substitution(subst2)
                            try:
                                subst3.try_add_variable('i2.1', tmp47)
                            except ValueError:
                                pass
                            else:
                                pass
                                # State 105195
                                subst4 = Substitution(subst3)
                                try:
                                    subst4.try_add_variable('i2.3.1.2.2', 1)
                                except ValueError:
                                    pass
                                else:
                                    pass
                                    # State 105196
                                    if len(subjects46) == 0:
                                        pass
                                        # State 105197
                                        if len(subjects40) == 0:
                                            pass
                                            # State 105198
                                            if len(subjects) == 0:
                                                pass
                                                # 10: b*log(x**n*c)
                                                yield 10, subst4
                                if len(subjects46) >= 1:
                                    tmp50 = subjects46.popleft()
                                    subst4 = Substitution(subst3)
                                    try:
                                        subst4.try_add_variable('i2.3.1.2.2', tmp50)
                                    except ValueError:
                                        pass
                                    else:
                                        pass
                                        # State 105196
                                        if len(subjects46) == 0:
                                            pass
                                            # State 105197
                                            if len(subjects40) == 0:
                                                pass
                                                # State 105198
                                                if len(subjects) == 0:
                                                    pass
                                                    # 10: b*log(x**n*c)
                                                    yield 10, subst4
                                    subjects46.appendleft(tmp50)
                            subjects46.appendleft(tmp47)
                        subjects40.appendleft(tmp45)
                if len(subjects40) >= 1 and isinstance(subjects40[0], Mul):
                    tmp52 = subjects40.popleft()
                    associative1 = tmp52
                    associative_type1 = type(tmp52)
                    subjects53 = deque(tmp52._args)
                    matcher = CommutativeMatcher105200.get()
                    tmp54 = subjects53
                    subjects53 = []
                    for s in tmp54:
                        matcher.add_subject(s)
                    for pattern_index, subst2 in matcher.match(tmp54, subst1):
                        pass
                        if pattern_index == 0:
                            pass
                            # State 105207
                            if len(subjects40) == 0:
                                pass
                                # State 105208
                                if len(subjects) == 0:
                                    pass
                                    # 10: b*log(x**n*c)
                                    yield 10, subst2
                    subjects40.appendleft(tmp52)
                subjects.appendleft(tmp39)
        subst1 = Substitution(subst0)
        try:
            subst1.try_add_variable('i2.2.1.4.1.0_1', S(1))
        except ValueError:
            pass
        else:
            pass
            # State 95047
            if len(subjects) >= 1:
                tmp56 = subjects.popleft()
                subst2 = Substitution(subst1)
                try:
                    subst2.try_add_variable('i2.2.1.4.1.0', tmp56)
                except ValueError:
                    pass
                else:
                    pass
                    # State 95048
                    if len(subjects) == 0:
                        pass
                        # 6: x*d
                        yield 6, subst2
                subjects.appendleft(tmp56)
        if len(subjects) >= 1 and isinstance(subjects[0], Mul):
            tmp58 = subjects.popleft()
            associative1 = tmp58
            associative_type1 = type(tmp58)
            subjects59 = deque(tmp58._args)
            matcher = CommutativeMatcher57232.get()
            tmp60 = subjects59
            subjects59 = []
            for s in tmp60:
                matcher.add_subject(s)
            for pattern_index, subst1 in matcher.match(tmp60, subst0):
                pass
                if pattern_index == 0:
                    pass
                    # State 57233
                    if len(subjects) == 0:
                        pass
                        # 0: x*f
                        yield 0, subst1
                if pattern_index == 1:
                    pass
                    # State 58504
                    if len(subjects) == 0:
                        pass
                        # 1: x*d
                        yield 1, subst1
                if pattern_index == 2:
                    pass
                    # State 64317
                    if len(subjects) == 0:
                        pass
                        # 2: x*f
                        yield 2, subst1
                if pattern_index == 3:
                    pass
                    # State 65657
                    if len(subjects) == 0:
                        pass
                        # 3: x*f
                        yield 3, subst1
                if pattern_index == 4:
                    pass
                    # State 68406
                    if len(subjects) == 0:
                        pass
                        # 4: x*d
                        yield 4, subst1
                if pattern_index == 5:
                    pass
                    # State 75451
                    if len(subjects) == 0:
                        pass
                        # 5: x**n*b
                        yield 5, subst1
                if pattern_index == 6:
                    pass
                    # State 95049
                    if len(subjects) == 0:
                        pass
                        # 6: x*d
                        yield 6, subst1
                if pattern_index == 7:
                    pass
                    # State 100918
                    if len(subjects) == 0:
                        pass
                        # 7: x*b
                        yield 7, subst1
                if pattern_index == 8:
                    pass
                    # State 103421
                    if len(subjects) == 0:
                        pass
                        # 8: x*f
                        yield 8, subst1
                if pattern_index == 9:
                    pass
                    # State 104048
                    if len(subjects) == 0:
                        pass
                        # 9: e*x
                        yield 9, subst1
                if pattern_index == 10:
                    pass
                    # State 105229
                    if len(subjects) == 0:
                        pass
                        # 10: b*log(x**n*c)
                        yield 10, subst1
                if pattern_index == 11:
                    pass
                    # State 107332
                    if len(subjects) == 0:
                        pass
                        # 11: b*(x*d + c)**n
                        yield 11, subst1
            subjects.appendleft(tmp58)
        return
        yield


from .generated_part004217 import *
from matchpy.matching.many_to_one import CommutativeMatcher
from .generated_part004218 import *
from .generated_part004215 import *
from collections import deque
from matchpy.utils import VariableWithCount
from multiset import Multiset